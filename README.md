# Employing issue prioritization to predict voting behavior
This project uses voters' prioritization of political issues to predict their 2016 Presidential vote choice. 

#### -- Project Status: Active

## Project Intro
I use likert scale ratings of issue importance to predict an individual's 2016 vote. The data comes from a bipartisan foundation, the Democracy Fund, and uses complex survey design to represent the U.S. registered voter population. 

### Technologies/Libraries

* CSS
* Flask
* Jupyter
* Heroku
* HTML
* Matplotlib
* NumPy
* pandas
* pickle
* Python
* random
* Regular expressions
* scikit-learn
* seaborn
* SMOTE (Synthetic Minority Oversampling Technique)
* weightedcalcs

## Getting Started

1. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).

2. Raw Data is kept [here](https://github.com/ali0003433/predict-by-issue-prioritization/tree/master/data/raw)

3. Data dictionary and description of survey methodology can be found [here](https://github.com/ali0003433/predict-by-issue-prioritization/tree/master/references)<br>
    
4. Notebooks are kept [here](https://github.com/ali0003433/predict-by-issue-prioritization/tree/master/notebooks): <br> 
  0 - Topic Selection notebook is kept [here](https://github.com/ali0003433/predict-by-issue-prioritization/blob/master/notebooks/0-al-topic-selection.ipynb) <br>
  1 - Preprocessing notebook is kept [here](https://github.com/ali0003433/predict-by-issue-prioritization/blob/master/notebooks/1-al-preprocessing.ipynb) <br>
  2 - Exploration notebook is kept [here](https://github.com/ali0003433/predict-by-issue-prioritization/blob/master/notebooks/2-al-exploration.ipynb) <br> 
  3 - Model selection notebook is kept [here](https://github.com/ali0003433/predict-by-issue-prioritization/blob/master/notebooks/3-al-modeling.ipynb) <br> 
 
 5. Source code is kept [here](https://github.com/ali0003433/predict-by-issue-prioritization/tree/master/src)

 6. Repo for Flask web app can be found [here](https://github.com/ali0003433/pred-by-issue-app)

## Process 
Cross-Industry Standard Process for Data Mining (CRISP-DM)
- Business understanding: Research political campaign data and predictive election models. 
- Data understanding: Explore and visualize Voter Study Group data. Read reports that have been written by others using this dataset. 
- Data preparation: Eliminate unnecessary features then convert needed features to dummy variables. Use SMOTE to oversample minority class. 
- Modeling: Compare Random Forest, Logistic Regression, Support Vector Machines, K-Nearest Neighbors. 
- Evaluation: Create custom metric and evaluate multiple models with those metrics, iteratively. Use grid search and cross validation to tune parameters. 
- Deployment: Deploy web app to heroku using Python, Flask, HTML/CSS. 

## Deliverables
* [Web app](https://make-prediction.herokuapp.com/)
* [Slide deck](https://github.com/ali0003433/predict-by-issue-prioritization/blob/master/reports/pred-deck.pdf)

## Contact
* Alyssa Liguori, Alyssa.Liguori@protonmail.com 


