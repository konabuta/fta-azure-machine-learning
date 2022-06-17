<!-- 
## Goal of this blog
MLOps is a concept and technology of DevOps of machine learning. Many customers are confusing about MLOps because "MLOps" become buzz phrase like AI we saw a few years ago. This blog will introduce "MLOps Maturity Model" created mainly by CSE team which defines what to implement in each level and will be very helpful customers to set concrete goals of their machine learning projects in implementing MLOps technology.

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


## Introduction
MLOps (machine learning operations) is based on DevOps principles and practices that increase overall workflow efficiencies and qualities in the machine learning lifecycle. This blog will introduce MLOps Maturity Model and MLOps architecture patterns using Azure Machine Learning and GitHub. Practical code snippets and step-by-step sample codes are out of scope of this blog, but will be published in our next blog.


### MLOps Maturity Model

To clarify the principles and practices of MLOps, Microsoft defines MLOps maturity model. Because different AI Systems have different requirements and difference organizations have different maturity levels, MLOps maturity model will be useful and helpful in the following points.

- understand the current MLOps level of your organization and implemented technologies.
- set concrete goals for your MLOps projects.
- plan the long-term roadmap of your organization and the technologies of MLOps


This table is an abstract of each level of MLOps maturity model. Be careful, it is general guidance. We recommend you customize it for your own MLOps project. We will introduce more details in the following sections of this blog.

|Maturity Level| Training Process | Release Process| Integration into app|
|---|---|---|---|
|Level 0 - No MLOps|Untracked, file is provided for handoff|Manual, hand-off|Manual, heavily DS driven|
|Level 1 - DevOps no MLOps|Untracked, file is provided for handoff|Manual, hand-off to SWE|Manual, heavily DS driven, basic integration tests added|
|Level 2 - Automated Training|Tracked, run results and model artifacts are captured in a repeatable way|Manual release,clean handoff process, managed by SWE team|Manual, heavily DS driven, basic integration tests added|
|Level 3 - Automated Model Deployment|Tracked, run results and model artifacts are captured in a repeatable way|Automated, CI/CD pipeline set up, everything is version controlled|Semi-automated, unit and integration tests added, still needs human signoff|
|Level 4 - Full MLOps Automated Retraining|Tracked, run results and model artifacts are captured in a repeatable way, retraining set up based on metrics from app|Automated, CI/CD pipeline set up, everything is version controlled, A/B testing has been added|Semi-automated, unit and integration tests added, may need human signoff|


>caution: As you go to high level maturity, not only technologies but also organization, people and cultures, are very importance. This blog is focus on technology. Please see [AI Business school](https://www.microsoft.com/en-us/ai/ai-business-school) to learn about AI strategies in your organization, AI-ready culture etc.


<br/>

### MLOps with Azure Machine Learning

Azure Machine Learning is a open-source friendly machine learning platform to implement full machine learning lifecycle and MLOps in cooperation with GitHub (or Azure DevOps) and Responsible AI technologies etc.


### Azure Machine Learning Workspace and assets

In the following sections, we will use Azure Machine Learning Workspace and assets to use to implement MLOps. 

Azure Machine Learning Workspace is the top-level resource of Azure Machine Learning. Azure Machine Learning Workspace works with  `Azure Storage Account`, `Azure Container Registry`, `Azure Key Vault`, `Azure Application Insights` , and related Azure services depending on your requirements.

Here is a list of Azure Machine Learning assets you should know before reading this blog.

- Data (Datastores & Datasets)
    - connect to Azure storages and manage subset of data.
- Job (Experiments and Runs)
    - handle job request sand manage metrics and logs in the experiments.
- Model
    - managed trained model with metadata.
- Environment
    - create and manage runtime (Docker Image) for training and inference.
- Component
    - create and manage a self-contained piece of code that does one step in a machine learning pipeline. 
- Pipeline
    - create and manage reproducible machine learning workflow. 
- Endpoint
    - create and manage inference environments like Managed Endpoint.

For more details, please check out [How Azure Machine Learning works: resources and assets (v2)](https://docs.microsoft.com/en-us/azure/machine-learning/concept-azure-machine-learning-v2?tabs=cli).
<br/>

## Maturity Model with Azure Machine Learning

In this section, we will explain the abstract of each level of MLOps Maturity model and the architecture pattern of Azure Machine Learning.

---

### Level 0 : No MLOps

This level is often called _PoC_ or _Experiment_ in machine learning projects. Data scientists pre-processes data manually from data source and train and deploy model interactively and exploratory. They work on a individual basis to find best model.

There will be reproducibility issues with your machine learning models. Assets generated in the platform which is not maintained by the organizations. And no test is configured. So deployed model (often manually) is unreliable and not responsible.



<img src="docs/images/level0.png" width-500 /><br/>


| People | Model Creation | Model Release | Application Integration |
| ------ | -------------- | ------------- | ----------------------- |
| <ul><li>Data scientists: siloed, not in regular communications with the larger team<li>Data engineers (_if exists_): siloed, not in regular communications with the larger team<li>Software engineers: siloed, receive model remotely from the other team members</ul> | <ul><li>Data gathered manually<li>Compute is likely not managed<li>Experiments aren't predictably tracked<li>End result may be a single model file manually handed off with inputs/outputs</ul> | <ul><li>Manual process<li>Scoring script may be manually created well after experiments, not version controlled<li>Release handled by data scientist or data engineer alone</ul> | <ul><li>Heavily reliant on data scientist expertise to implement<li>Manual releases each time</ul> |

#### Azure Machine Learning Architecture
<img src="docs/images/level0-azureml.png" width-500 /><br/>

If you use Azure Machine Learning, `Compute Instance` is a good place to start for your machine learning journey. It includes essential Python/R libraries and development tools like JupyterLab, R Studio and VSCode remote development feature.

#### Challenges

- Reproducibility
    - It is very difficult to reproduce training model jobs because data scientists use their own customized machine learning tools and codes and Python/R packages that are used by each data scientist are not shared within the organization.
- Quality & Security
    - No test is configured. Or test policies are not designed across the organization.
    - There are security concerns in machine learning tools that are not maintained by IT.
- Scalability
    - Often compute resources don't have enough power to run jobs at scale.
    - High-performance compute resources are not shared within the organization, which leads to cost increase.
- Other
    - Data source is not maintained for machine learning. It requires manual steps to get training data.


#### What's next?

- Standardize the machine learning platform across the organizations and create shared high-performance compute resources.
- Setup code repository and share code used by data scientists.
- Configure and automate code test against train and score scripts.
- Setup data pipeline to be able to get data easily.


Next, we will introduce _Level 1 : DevOps no MLOps_

<br />

---

### Level 1 : DevOps no MLOps

This is a level that data scientists work on a standardized machine learning platform. And data pipeline is maintained by data engineers, so it is easy to get data for training model.

Reproduce the model training is still difficult because machine learning assets like data, python packages are not shared. Sometime job dependencies within a training workflow are complicated but they are not shared by each data scientists.

<img src="docs/images/level1.png" width-500 /><br/>


| People | Model Creation | Model Release | Application Integration |
| ------ | -------------- | ------------- | ----------------------- |
| <ul><li>Data scientists: siloed, not in regular communications with the larger team<li>Data engineers (if exists): siloed, not in regular communication with the larger team<li>Software engineers: siloed, receive model remotely from the other team members</ul> | <ul><li>Data pipeline gathers data automatically<li>Compute is or isn't managed<li>Experiments aren't predictably tracked<li>End result may be a single model file manually handed off with inputs/outputs</ul> | <ul><li>Manual process<li>Scoring script may be manually created well after experiments, likely version controlled<li>Is handed off to software engineers</ul> | <ul><li>Basic integration tests exist for the model<li>Heavily reliant on data scientist expertise to implement model<li>Releases automated<li>Application code has unit tests</ul> |


#### Azure Machine Learning Architecture
<img src="docs/images/level1-azureml.png" width-500 /><br/>

Azure Machine Learning is a shared and collaborative machine learning platform. By using `Data (datastore)` feature to connect to Azure storage services, you can access to data source easily from Azure Machine Learning. Once you trained model, you can register it to `Model` feature and deploy it using `Managed Endpoints` that is a new version of endpoint feature.

Azure Machine Learning can integrate with GitHub. So you can share your train and inference code on GitHub and you can test codes automatically using GitHub Actions.


#### Challenges

- Reproducibility
    - Assets in machine learning lifecycle are not shared in the organization.
    - Some training model workflow has complex job dependencies and is difficult to run by others.


#### What's next?

- Ensure reproducibility of the experiments.
    - Create pipeline to automate and reproduce model training.
    - Save assets associated with the experiments only code but also data, metrics/logs, models etc.
- Operate model.
    - Register the model and associate it with the experiments.

---

### Level 2 : Automated Training

<img src="docs/images/level2.png" width-500 /><br/>


| People | Model Creation | Model Release | Application Integration |
| ------ | -------------- | ------------- | ----------------------- |
| <ul><li>Data scientists: Working directly with data engineers to convert experimentation code into repeatable scripts/jobs<li>Data engineers: Working with data scientists<li>Software engineers: siloed, receive model remotely from the other team members</ul> | <ul><li>Data pipeline gathers data automatically<li>Compute managed<li>Experiment results tracked<li>Both training code and resulting models are version controlled</ul> | <ul><li>Manual release<li>Scoring script is version controlled with tests<li>Release managed by Software engineering team</ul> | <ul><li>Basic integration tests exist for the model<li>Heavily reliant on data scientist expertise to implement model<li>Application code has unit tests</ul> |

#### Azure Machine Learning perspective

<img src="docs/images/level2-azureml.png" width-500 /><br/>

Training model are defined by `Pipeline` which defines complex job dependencies. `Job` manages your training job and logs parameters and metrics. `Data` is an abstract data source for training job. And `Environment` defines Python packages, environment variables, and Docker settings.

Azure Machine Learning CLI v2 is a new version of Azure Machine Learning. You can define your job using YAML files and execute your job via Azure Machine Learning CLI v2. Python SDK v1&v2 is also available if you want to define by Python code. 


>caution: Using `Pipeline` is not mandatory.if your job has complex dependencies, `Pipeline` is very useful. If your job has simple dependencies, you can use `Job` to run and manage your job.


And you can use GitHub Actions to trigger model training job easily via Azure ML CLI v2. Typical cases of triggering model training job are as follows:

- Trigger job every time code in GitHub is changed by pull request.
- Trigger job on a schedule to learn new data.




#### Challenges

- Deployment
    - Deploy models into multiple inference endpoints quickly.
- Model quality
    - Test the trained model behavior and performance.
    - Ensure the model has interpretability/explainability and fairness.

#### What's next?

- Deploy pipelines.
    - Define the workflow of your model deployment for automation.
- Improve the model qualities.
    - Automate test model using test data.
    - Increase transparency by using interpretable machine learning model or use explainability techniques to the trained model.
    - Evaluate fairness of the trained model. And mitigate the model bias if necessary.


---

### Level 3 : Automated Model Deployment

<img src="docs/images/level3.png" width-500 /><br/>



| People | Model Creation | Model Release | Application Integration |
| ------ | -------------- | ------------- | ----------------------- |
| <ul><li>Data scientists: Working directly with data engineers to convert experimentation code into repeatable scripts/jobs<li>Data engineers: Working with data scientists and software engineers to manage inputs/outputs<li>Software engineers: Working with data engineers to automate model integration into application code</ul> | <ul><li>Data pipeline gathers data automatically<li>Compute managed<li>Experiment results tracked<li>Both training code and resulting models are version controlled</ul> | <ul><li>Automatic release<li>Scoring script is version controlled with tests<li>Release managed by continuous delivery (CI/CD) pipeline</ul> | <ul><li>Unit and integration tests for each model release<li>Less reliant on data scientist expertise to implement model<li>Application code has unit/integration tests</ul> |

#### Azure Machine Learning perspective
<img src="docs/images/level3-azureml.png" width-500 /><br/>

`Managed (online/batch) Endpoint` is very useful to deploy model in Azure Machine Learning. You can deploy it using Azure ML CLI v2 which can be executed by GitHub Actions. If you want to put gate between Stage and Production, you can use GitHub environments.

As for responsible ai, Azure Machine Learning can integrate with responsible ai toolbox and fairness toolkit which also can be executed by GitHub Actions.




#### Challenges

- Model degradation
    - Model is not upgraded after deployment. User experience gets worse due to model performance degradation over time.
- Model Retraining
    - Inference environments are not monitored enough. It is difficult to decide when to retrain model.
    - It is difficult to deploy new model into production inference environment without affecting customers.


#### What's next?

- Implementing monitoring system.
    - Detect data drift by scanning data regularly.
    - Monitor metrics and logs that are associated with your model and system performance.
- Automation
    - Trigger training pipeline for retraining model based on metrics and logs (above).
    - Rollout new model safely into production endpoint using blue-green deployment.

---

### Level 4 : Full MLOps Automated Retraining



<img src="docs/images/level4.png" width-500 /><br/>

| People | Model Creation | Model Release | Application Integration |
| ------ | -------------- | ------------- | ----------------------- |
| <ul><li>Data scientists: Working directly with data engineers to convert experimentation code into repeatable scripts/jobs. Working with software engineers to identify markers for data engineers<li>Data engineers: Working with data scientists and software engineers to manage inputs/outputs<li>Software engineers: Working with data engineers to automate model integration into application code. Implementing post-deployment metrics gathering</ul> | <ul><li>Data pipeline gathers data automatically<li>Retraining triggered automatically based on production metrics<li>Compute managed<li>Experiment results tracked<li>Both training code and resulting models are version controlled</ul> | <ul><li>Automatic Release<li>Scoring Script is version controlled with tests<li>Release managed by continuous integration and CI/CD pipeline</ul> | <ul><li>Unit and Integration tests for each model release<li>Less reliant on data scientist expertise to implement model<li>Application code has unit/integration tests</ul> |

#### Azure Machine Learning perspective

<img src="docs/images/level4-azureml.png" width-500 /><br/>

Metrics and logs are logged and analyzed in Azure Monitor and Azure Application Insights. You can check if deployed model performs well or not and system performance is enough or not. Retraining job is triggered by the defined metrics automatically or via human judgments.

When deploying new model into existing inference endpoint (`Managed Online Endpoint` in this case), you can use blue-green deployment to control traffics into production inference endpoint before rolling new model out completely to minimize the risk of failures.


---

## Summary

We introduced a concept of MLOps maturity model and explained the architecture and product features of Azure Machine Learning and GitHub etc in each maturity levels. We also discussed the challenges and what's next items for each maturity levels. We will describe how to implement MLOps with Azure Machine Learning and GitHub in the next blog.


## About the author

Keita Onabuta

Meer