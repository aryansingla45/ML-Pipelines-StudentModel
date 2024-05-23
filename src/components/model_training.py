import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (RandomForestRegressor , 
                              GradientBoostingRegressor,
                              AdaBoostRegressor)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exceptions import CustomException
from src.logger import logging 
from src.utils import save_object , evaluate_model

@dataclass
class ModelTrainerConfig:
    trained_model_path = os.path.join('artifacts', "model.pkl")
     

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self , train_arr , test_arr):
        try:
            logging.info("Entered Model Trainer")
            X_train , y_train , X_test , y_test = (
                train_arr[:,:-1],
                train_arr[:,-1],
                test_arr[:,:-1],
                test_arr[:,-1]            
                )

            models={
                'RandomForest': RandomForestRegressor(),
                'DecisionTree': DecisionTreeRegressor(),
                'GradientBoosting': GradientBoostingRegressor(),
                'AdaBoost': AdaBoostRegressor(),
                'XGBoost': XGBRegressor(),
                'CatBoost': CatBoostRegressor(verbose = False),
                'KNN': KNeighborsRegressor(),
                'LinearRegression': LinearRegression()
            }

            model_report:dict=evaluate_model(X_train = X_train , y_train = y_train ,X_test = X_test ,y_test = y_test,models = models)

            best_model_score = max(sorted(model_report.values()))
            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model = models[best_model_name]

            if best_model_score < 0.7:
                raise CustomException("No best model found")
            logging.info(f"Best Model: {best_model_name} with score: {best_model_score} found both on training and testing data")

            save_object(
                file_path = self.model_trainer_config.trained_model_path,
                obj = best_model
            )

            x = best_model.predict(X_test)
            r2score = r2_score(y_test , x)
            return r2score

        except Exception as e:
            raise CustomException(e,sys)

        
