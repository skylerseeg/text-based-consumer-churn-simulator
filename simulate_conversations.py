from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("models/llama_3.2_1B")
model = AutoModelForCausalLM.from_pretrained("models/llama_3.2_1B")
import mlflow

def train_model(...):
    # Example: start an MLflow run
    with mlflow.start_run(run_name="Churn_Simulator_Experiment"):
        # Log parameters
        mlflow.log_param("model_type", "llama_3.2_1B")
        mlflow.log_param("epochs", 3)
        
        # Suppose you have some training loop here
        # ...
        
        # Log metrics
        mlflow.log_metric("loss", 0.35)
        mlflow.log_metric("accuracy", 0.91)
        
        # Save artifacts (like a trained model or config files)
        mlflow.log_artifact("config/settings.json")
        
        # (Optional) If you have a model to save, you can do:
        # mlflow.pytorch.log_model(...)
        # mlflow.pyfunc.log_model(...)
        # depending on your library. 
