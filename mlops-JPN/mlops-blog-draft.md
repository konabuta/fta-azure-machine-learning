<!-- 
## Goal of this blog
MLops is just a concept of DevOps of machine learning. Many customers are confusing about MLOps because "MLOps" become buzz phrase like AI we saw a few years ago. This blog introduce "MLOps Maturity Model" created mainly by CSE team which defines what to implement in each level and will be very helpful customers to set a concrete goal of their machine learning projects in implementing MLOps technology.

## Agenda
- Introduction
    - Introduction to MLOps and Maturity Model
- Maturity Model with Azure Machine Learning
    - Level 0 : No MLOps
    - Level 1 : DevOps no MLOps
    - Level 2 : Automated Training
    - Level 3 : Automated Model Deployment
    - Level 4 : Full MLOps Automated Retraining
- Code examples using
    - next blog?
-->


# MLOps Maturity Model with Azure Machine Learning (Concept)


<br/>

## Introduction
MLOps (machine learning operations) is based on DevOps principles and practices that increases workflow efficiencies in machine learning lifecycle. By implementing MLOps, you can make your ML project more agile and more scalable and increase the quality and responsibility.

### MLOps Maturity Model

To clarify the principle and practice of MLOps, Microsoft defines MLOps maturity model. Because different AI Systems have different requirements and difference organizations and team have different maturity levels, MLOps maturity model will be helpful in the following points.

- set a goal of their machine learning projects in implementing MLOps technologies.
- set a plan to grow your MLOps capability in increments.


This table is a abstract of each level of MLOps maturity model. We will introduce more details in the following sections of this blog.

|Maturity Level| Training Process | Release Process| Integration into app|
|---|---|---|---|
|Level 0 - No MLOps|Untracked, file is provided for handoff|Manual, hand-off|Manual, heavily DS driven|
|Level 1 - DevOps no MLOps|Untracked, file is provided for handoff|Manual, hand-off to SWE|Manual, heavily DS driven, basic integration tests added|
|Level 2 - Automated Training|Tracked, run results and model artifacts are captured in a repeatable way|Manual release,clean handoff process, managed by SWE team|Manual, heavily DS driven, basic integration tests added|
|Level 3 - Automated Model Deployment|Tracked, run results and model artifacts are captured in a repeatable way|Automated, CI/CD pipeline set up, everything is version controlled|Semi-automated, unit and integration tests added, still needs human signoff|
|Level 4 - Full MLOps Automated Retraining|Tracked, run results and model artifacts are captured in a repeatable way, retraining set up based on metrics from app|Automated, CI/CD pipeline set up, everything is version controlled, A/B testing has been added|Semi-automated, unit and integration tests added, may need human signoff|




### MLOps with Azure Machine Learning

In Azure, you can use Azure Machine Learning to implement fully machine learning lifecycle and MLOps in cooperation with GitHub (or Azure DevOps) and Responsible AI technologies etc.


### Azure Machine Learning Workspace and assets

In the following sections, we will use Azure Machine Learning Workspace and assets to use to implement MLOps. 

Azure Machine Learning Workspace is the top-level resource for Azure Machine Learning. Azure Machine Learning Workspace works with  `Azure Storage Account`, `Azure Container Registry`, `Azure Key Vault`, `Azure Application Insights` and related Azure services depending on your requirements.

Here is a list of Azure Machine Learning assets you should know before reading this blog.

- Datastores & Datasets
- Experiments and Runs
- Models
- Environments
- Endpoints
- Pipelines

<br/>

## Maturity Model with Azure Machine Learning

In this section, we will explain the details of each level of Maturity Model.

---

### Level 0 : No MLOps

This is the level to preprocess data, train model and deploy model interactively and exploratory. Data scientists work on a individual basis. There will be reproducibility issues of your machine learning models. Assets generated in the platform which is not maintained by the organization and team are unreliable and not responsible.



<!-- general diagram -->

##### Training Process
##### Release Process
##### Integration into app


#### Implementation with Azure Machine Learning

<!-- Azure ML Diagram -->


#### Challenges



#### What's next?





---

### Level 1 : DevOps no MLOps

xxxx

<img src="https://storage.googleapis.com/zenn-user-upload/714ed3ab4090-20211215.png" with=500 /><br/>

##### Training Process
##### Release Process
##### Integration into app


#### Implementation with Azure Machine Learning

<img src="https://storage.googleapis.com/zenn-user-upload/fab9f7aab2b2-20211222.png" width-500 /><br/>


#### Challenges

- Reproducibility
    - Asset tracking, reproduce experiments
    - execute as a pipeline
    - model is saved and ready to compare new model with old model.

#### What's next?

- Reproducibility
    - Experiment can be reproduced. Assets are saved associated with experiments. 
- Operate model
    - Models are maintained and can be associated with experiments and endpoints.
---

### Level 2 : Automated Training

xxxx


<!-- general diagram -->

##### Training Process
##### Release Process
##### Integration into app


#### Implementation with Azure Machine Learning

<!-- Azure ML Diagram -->


#### Challenges


#### What's next?


---

### Level 3 : Automated Model Deployment

xxxx


<!-- general diagram -->

##### Training Process
##### Release Process
##### Integration into app


#### Implementation with Azure Machine Learning

<!-- Azure ML Diagram -->


#### Challenges


#### What's next?


---

### Level 4 : Full MLOps Automated Retraining

xxxx


<!-- general diagram -->

##### Training Process
##### Release Process
##### Integration into app


#### Implementation with Azure Machine Learning

<!-- Azure ML Diagram -->


#### Challenges


#### What's next?


---

## Conclusion


## About the author

Keita Onabuta