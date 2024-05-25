[![Build App](https://github.com/aryansingla45/ML-Pipelines-StudentModel/actions/workflows/main.yml/badge.svg)](https://github.com/aryansingla45/ML-Pipelines-StudentModel/actions/workflows/main.yml)

# ML-Pipelines-StudentModel

This project is used for hosting a web app using flask to predict a student math score using different details.
The project also has different pipelines for data ingestion, transformation, model training and predicting which help in seamless predicting the data.

### Running the project 
1. Setting up the Virtual Environment
 To run these commands first set a virtual environment so there is no environment related errors.
```conda create -p venv```
```conda activate venv/```

2. Install all the dependencies and requirements:
   Run this command to install all the requirements that are used in this code.
   ```pip install -r requirements.txt```

3. Data Ingestion :
    ```python src/components/data_ingestion.py```
4. Data Transformation:
  `python src/components/data_transformation.py`
5. Model Training:
     `python src/components/model_training.py`
   If you want to run all the pipelines together then run the data ingestion pipeline if not then you can edit the code and comment it out.

6. Running the Flask App
   `python app.py`

7. Running the Streamlit App
   `streamlit run application.py`


