import time
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from xgboost import XGBClassifier
from preprocessing import load_and_preprocess_data

def evaluate_models():
    # 1. Load preprocessed data using Friday DDoS dataset file
    dataset_file = "datasets/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
    X_train, X_test, y_train, y_test = load_and_preprocess_data(dataset_file)
    
    models = {
        "Random Forest (Baseline/Ensemble)": RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
        "XGBoost Classifier (Advanced Ensemble)": XGBClassifier(n_estimators=100, random_state=42, n_jobs=-1, eval_metric='logloss')
    }
    
    results = {}
    
    for name, model in models.items():
        print(f"\n[*] Training {name}...")
        start_train = time.time()
        model.fit(X_train, y_train)
        train_time = time.time() - start_train
        
        print(f"[*] Evaluating {name} on blind test set...")
        start_pred = time.time()
        y_pred = model.predict(X_test)
        pred_time = (time.time() - start_pred) * 1000 # in ms
        
        acc = accuracy_score(y_test, y_pred)
        prec = precision_score(y_test, y_pred)
        rec = recall_score(y_test, y_pred)
        f1 = f1_score(y_test, y_pred)
        cm = confusion_matrix(y_test, y_pred)
        
        results[name] = {
            "accuracy": acc, "precision": prec, "recall": rec, "f1": f1,
            "train_time_sec": train_time, "latency_ms": pred_time, "confusion_matrix": cm
        }
        
    print("\n================ COMPARATIVE MODEL EVALUATION ================")
    for name, metrics in results.items():
        print(f"\nModel: {name}")
        print(f"  Accuracy  : {metrics['accuracy'] * 100:.2f}%")
        print(f"  Precision : {metrics['precision'] * 100:.2f}%")
        print(f"  Recall    : {metrics['recall'] * 100:.2f}%")
        print(f"  F1-Score  : {metrics['f1'] * 100:.2f}%")
        print(f"  Train Time: {metrics['train_time_sec']:.2f} seconds")
        print(f"  Inference Latency: {metrics['latency_ms']:.2f} ms")
        print(f"  Confusion Matrix:\n{metrics['confusion_matrix']}")
    print("==============================================================")

if __name__ == "__main__":
    evaluate_models()