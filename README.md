# Capstone WIMT

Where Is My Transport is a company offering mobility data solutions for emerging-market megacities.
In this project, we try to analyze one of the most common issues that a data solution's company with mobile apps have to face: the push-notifications have a very low ratio of opening.
### TIM, PUT THE IMAGE HERE

The notebooks on this project are the following:
- Data_Cleaning: This notebook include the data cleaning, feature engineering, NLP processing of our project. Exports the two dataframes that are going to be used for EDA and for modeling.
- EDA_Capstone: Exploratory data analysis of our project, focusing on user identification and classification, and to get a deeper understanding on the notifications.
- Basemodel_Decision_Tree: Basemodel used for classification. Plots decision tree, for a basic concept of features affecting the model.
- Random forest classifier: Random forest model, with basic weight estimation. Discarded, as got worse results than XGBoost.
- Model_XGBoost: Final model used for classification. Includes cross validation, hyperparameter tuning, and features' importance evaluation.
## Setup

Run this commands in terminal:

pyenv local 3.8.5
python -m venv .venv
pip install --upgrade pip
pip install -r requirements.txt

The requirements.txt file contains the libraries needed for deployment.