import time
import sys
from logging import getLogger
import pandas as pd
import numpy as np
import pyarrow.feather as feather
from sklearn.model_selection import train_test_split
from sklearn.model_selection import RepeatedStratifiedKFold,GridSearchCV
from sklearn.metrics import balanced_accuracy_score, confusion_matrix, classification_report
from sklearn.tree import DecisionTreeClassifier
import warnings
import mlflow
from mlflow.sklearn import save_model
from config import TRACKING_URI, EXPERIMENT_NAME
warnings.filterwarnings("ignore")
logger = getLogger(__name__)
def __get_data():
    logger.info("Getting the data")
    export_df = feather.read_feather("data/cleaned_data.feather")
    basemodel_df=pd.get_dummies(data=export_df,columns= ["cause","effect"],drop_first=True)
    basemodel_df.drop(['event_timestamp', 'event_name', 'user_id', 'document_id','surrogate_id', 'created_at', 'published_at', 'closed_at','notif_viewed_ontime', 'reaction_time','description','area_of_effect_coordinates_latitude','area_of_effect_coordinates_longitude','opened','opened_rate'],axis=1, inplace=True)
    X= basemodel_df.drop(["interesting_message"], axis=1)
    y= basemodel_df['interesting_message']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    return X_train, X_test, y_train, y_test
def __class_metrics(y_test:pd.Series, y_pred:pd.Series,prefix: str = "Train "):
    accuracy = balanced_accuracy_score(y_test, y_pred)
    report= classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred).round()
    logger.info(
        str(prefix) + "predicted values:\n {} \n" 
        + str(prefix) + "confusion matrix: \n {} \n"
        + str(prefix) + "balanced accuracy: \n {} \n"
        + str(prefix) + "report: \n {}".format(y_pred,cm,accuracy,report))
    mlflow.log_metric(prefix + "-" + "balanced accuracy", accuracy)
    logger.info(type(y_pred))
    sys.exit()
    mlflow.log_metric(prefix + "-" + "predicted values",y_pred)
    mlflow.log_metric(prefix + "-" + "confusion matrix",cm)
    mlflow.log_metric(prefix + "-" + "report",report)
    return cm, accuracy
    

def run_training():
    X_train, X_test, y_train, y_test = __get_data()
    logger.info("Training simple model and tracking with MLFlow")
    mlflow.set_tracking_uri(TRACKING_URI)
    mlflow.set_experiment(EXPERIMENT_NAME)
    # model
    with mlflow.start_run():
        model = DecisionTreeClassifier(class_weight="balanced")
        params = {'max_leaf_nodes':[10,50,100],
        'criterion': ['gini'],
        'max_depth': [2, 5, 10, 50],
        'min_samples_leaf':[50,200,500]
        }
        mlflow.log_params(params)
        mlflow.set_tag("Base_model", "True")
        cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=3, random_state=1)
        grid_tree = GridSearchCV(model, param_grid=params, cv=cv,scoring='balanced_accuracy', n_jobs=-1, verbose=10)
        start = time.time()
        grid_tree.fit(X_train, y_train)
        end = time.time()
        mlflow.log_metric("Training time",time)
        best_model_tree = grid_tree.best_estimator_
        y_train_pred = best_model_tree.predict(X_train)
        __class_metrics(y_train, y_train_pred)
        y_test_pred = best_model_tree.predict(X_test)
        __class_metrics(y_test, y_test_pred, "test")
        path = "../models/base_decision_tree"
        save_model(sk_model=best_model_tree, path=path)
        # logging the model to mlflow will not work without a AWS Connection setup.. too complex for now

if __name__ == "__main__":
    import logging

    logger = logging.getLogger()
    logging.basicConfig(format="%(asctime)s: %(message)s")
    logging.getLogger("pyhive").setLevel(logging.CRITICAL)  # avoid excessive logs
    logger.setLevel(logging.INFO)

    run_training()
