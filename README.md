# Wine Quality Prediction – End-to-End ML Project

This project demonstrates an **end-to-end Machine Learning pipeline** for predicting the quality of wine using the [Wine Quality Dataset](https://www.kaggle.com/datasets/yasserh/wine-quality-dataset).  
It is designed using a **modular coding structure in Python** and follows **MLOps best practices** to ensure scalability, maintainability, and reproducibility.

---

## Project Details

### Workflow (ML Pipeline)

1. **Data Ingestion** – Load raw data from source.  
2. **Data Validation** – Validate schema and ensure data quality.  
3. **Data Transformation** – Clean and preprocess data for training.  
4. **Model Trainer** – Train ML model using ElasticNet regression.  
5. **Model Evaluation** – Evaluate model performance using metrics like RMSE, MAE, R².  

### Project Setup & Configuration

The project uses YAML-based configuration for modularity.

- `config.yaml` → High-level pipeline configuration.  
- `schema.yaml` → Data schema & validation rules.  
- `params.yaml` → Model hyperparameters.  
- `src/config` → Configuration manager for loading settings.  
- `src/components` → Contains modular components (ingestion, transformation, training, etc.).  
- `src/pipeline` → Orchestration of all components.  
- `main.py` → Entry point for running the pipeline.  

### Workflows

1. Update `config.yaml`  
2. Update `schema.yaml`  
3. Update `params.yaml`  
4. Update entity classes in `Entity`  
5. Update configuration manager in `src/config`  
6. Implement or update the required component in `src/components`  
7. Update the pipeline in `src/pipeline`  
8. Run `main.py` to execute the pipeline  

## Repository Management (Git + DagsHub)

This project supports both **GitHub** and **Dagshub** integration for version control and experiment tracking.

### GitHub Repository Setup

- Go to [GitHub](https://github.com/).
- Click on New.
- Enter:
  - Repository Name: e.g., `wine-quality-prediction`
  - Visibility: `Public` (recommended for showcasing) or `Private`.
  - Click `Create Repository`.
  - Clone it locally:
  ```
    git clone https://github.com/<your-username>/wine-quality-prediction.git
    cd wine-quality-prediction
  ```
### Creating and Connecting DagsHub Repository Setup

- Go to [DagsHub](https://dagshub.com) -> Create -> New Repository -> Connect a Repository -> Github(You can choose any other repository of choice) -> Connect 
- Authorise the Dags authentication to Github account.
- Enter the same repository name as GitHub (e.g., wine-quality-prediction).
- Under Repository source, select GitHub and link it to the GitHub repo you just created.
- Now, your GitHub repo is connected with DagsHub automatically.

### Authentication

MLflow requires authentication to push logs and models.

- Go to DagsHub -> Your Setting -> Tokens.
- Click Generate New Token or copy the Default Token.

```bash
export MLFLOW_TRACKING_PASSWORD=YOUR_TOKEN_FROM_DAGSHUB
export MLFLOW_TRACKING_URI=YOUR_TRACKING_URI
export MLFLOW_TRACKING_USERNAME=YOUR_USERNAME_FROM_DAGSHUB
```

## Environment Setup

Below examples are with respect to Github. If 

### Clone the repository

```bash
git clone <your-repo-url>
cd wine-quality-mlops
```

### Setup virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate 
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Access the UI at: http://127.0.0.1:8080

Endpoints
- Train model → http://127.0.0.1:8080/train
- Predict wine quality → http://127.0.0.1:8080/predict

## Model Performance

Metrics used:

- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- R² Score (Coefficient of Determination)
- Experiment tracking is managed via MLflow and DagsHub.