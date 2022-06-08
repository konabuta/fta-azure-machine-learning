# imports
import time
import mlflow
import argparse

import pandas as pd
import lightgbm as lgb

from sklearn.metrics import log_loss, accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# Method for Data Preprocessing
def preprocess_data(df, categorical_cols, float_cols):

    df[categorical_cols] = df[categorical_cols].astype('category')
    df[float_cols] = df[float_cols].astype('float')

    X = df.drop(["Survived", "PassengerId"], axis=1)
    y = df["Survived"]

    enc = LabelEncoder()
    y = enc.fit_transform(y)

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    return X_train, X_test, y_train, y_test, enc, categorical_cols


# Method of Model Training
def train_model(params, num_boost_round, X_train, X_test, y_train, y_test, categorical_cols):
    t1 = time.time()
    train_data = lgb.Dataset(X_train, label=y_train, categorical_feature=categorical_cols)
    test_data = lgb.Dataset(X_test, label=y_test, categorical_feature=categorical_cols)
    model = lgb.train(
        params,
        train_data,
        num_boost_round=num_boost_round,
        valid_sets=[test_data],
        valid_names=["test"],
    )
    t2 = time.time()

    return model, t2 - t1


# Method for Model Evaluation
def evaluate_model(model, X_test, y_test):
    y_proba = model.predict(X_test)
    y_pred = y_proba.argmax(axis=1)
    loss = log_loss(y_test, y_proba)
    acc = accuracy_score(y_test, y_pred)

    return loss, acc


print("*" * 60)
print("\n\n")

mlflow.log_param("hello_param", "world")

# args
parser = argparse.ArgumentParser()
parser.add_argument("--input-data", type=str)
parser.add_argument("--num-boost-round", type=int, default=10)
parser.add_argument("--boosting", type=str, default="gbdt")
parser.add_argument("--num-iterations", type=int, default=16)
parser.add_argument("--num-leaves", type=int, default=31)
parser.add_argument("--num-threads", type=int, default=0)
parser.add_argument("--learning-rate", type=float, default=0.1)
parser.add_argument("--metric", type=str, default="multi_logloss")
parser.add_argument("--seed", type=int, default=42)
parser.add_argument("--verbose", type=int, default=0)
parser.add_argument("--titanic-csv", type=str)

args = parser.parse_args()

seed = 1234

# Automatic Logging for LightGBM
mlflow.lightgbm.autolog()


# LightGBM Parameters
num_boost_round = args.num_boost_round

params = {
    "objective": "multiclass",
    "num_class": 2,
    "boosting": args.boosting,
    "num_iterations": args.num_iterations,
    "num_leaves": args.num_leaves,
    "num_threads": args.num_threads,
    "learning_rate": args.learning_rate,
    "metric": args.metric,
    "seed": args.seed,
    "verbose": args.verbose,
}

# Data Loading
df = pd.read_csv(args.titanic_csv)

# Feature Engineering
categorical_cols = ['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked']
float_cols = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare']
X_train, X_test, y_train, y_test, enc, categorical_cols = preprocess_data(df, categorical_cols, float_cols)

# Model Training
model, train_time = train_model(
    params, num_boost_round, X_train, X_test, y_train, y_test, categorical_cols
)

# Model Evaluation
loss, acc = evaluate_model(model, X_test, y_test)

print("\n\n")
print("*" * 60)

# #Model Registry
# model = mlflow.lightgbm.save_model(model, "./outputs/model")
