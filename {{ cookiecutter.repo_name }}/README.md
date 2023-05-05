{{cookiecutter.project_name}}
==============================
#### -- Project Status: [Active, On-Hold, Completed]

## Project Intro/Objective
The purpose of this project is ________. (Describe the main goals of the project and potential civic impact. Limit to a short paragraph, 3-6 Sentences)

### Collaborators
|Name                      |  Github Page      |  Personal Website  |
|--------------------------|-------------------|--------------------|
|{{cookiecutter.author_name}} | [{{cookiecutter.author_name}}](https://github.com/{{cookiecutter.author_name}})| - |

### Methods Used
* Inferential Statistics
* Machine Learning
* Data Visualization
* Predictive Modeling
* etc.

### Technologies
* R
* Python
* D3
* PostGres, MySql
* Pandas, jupyter
* HTML
* JavaScript
* etc.

## Project Description
{{cookiecutter.description}}

(Provide more detailed overview of the project.  Talk a bit about your data sources and what questions and hypothesis you are exploring. What specific data analysis/visualization and modelling work are you using to solve the problem? What blockers and challenges are you facing?  Feel free to number or bullet point things here)

## Project Organization
------------

    ├── LICENSE
    ├── README.md                    <- The top-level README for developers using this project.
    │   
    ├── data
    │   ├── external                 <- Data from third party sources.
    │   ├── interim                  <- Intermediate data that has been transformed.
    │   ├── processed                <- The final, canonical data sets for modeling.
    │   └── raw                      <- The original, immutable data dump.
    │
    ├── docs               
    │
    ├── models                       <- Trained and serialized models
    │   └── model_outputs            <- Model predictions, or model summaries
    │
    ├── notebooks                    <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                                   the creator's initials, and a short `-` delimited description, e.g.
    │                                   `1.0-jqp-initial-data-exploration`.
    │
    ├── references                   <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports                      <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures                  <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt             <- The requirements file for reproducing the analysis environment, e.g.
    │                                      generated with `pip freeze > requirements.txt`
    │
    ├── setup.py                     <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                          <- Source code for use in this project.
    ├── __init__.py                  <- Makes src a Python module
    │   │   
    │   ├── common                   <-  Functions used across the project
    │   │
    │   ├── data                     <- Scripts to reading and writing data etc
    │   │
    │   ├── features                 <- Scripts to create features features for modeling
    │   │
    │   ├── model_evaluation         <- Scripts that analyse model performance and model selection
    │   │
    │   ├── modelling                <- Scripts to train models and then use trained models to make
    │   │                                  predictions
    │   │
    │   ├── reporting                <- Scripts to produce reporting tables
    │   │
    │   └── visualization            <- Scripts to create exploratory and results oriented visualizations
    │
    └── tox.ini                      <- tox file with settings for running tox; see tox.readthedocs.io


--------

## Getting Started

1. Clone this repo.
2. Raw Data is being kept [here](Repo folder containing raw data) within this repo.
3. Data processing/transformation scripts are being kept [here](Repo folder containing data processing scripts/notebooks)
4. etc...
5. Follow setup [instructions](Link to file)

## Featured Notebooks/Analysis/Deliverables
* [Notebook/Markdown/Slide Deck Title](#)
* [Notebook/Markdown/Slide DeckTitle](#)

---
<p><small>This project file structure is based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a> and <a target="_blank" href="https://github.com/dssg/hitchhikers-guide/tree/master/sources/curriculum/0_before_you_start/pipelines-and-project-workflow">DSSG machine learning pipeline</a>.</small></p>