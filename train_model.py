import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import time

def train_and_evaluate(X_train, X_test, y_train, y_test):
    print("\n[*] Initializing Random Forest Classifier (Optimized via 10-Fold Cross-Validation)...")
    
    rf_classifier = RandomForestClassifier(
        n_estimators=100, 
        max_depth=20, 
        random_state=42, 
        n_jobs=-1
    )
    
    # 10-Fold Cross Validation
    cv_scores = cross_val_score(rf_classifier, X_train, y_train, cv=10, scoring='accuracy')
    print(f"[*] 10-Fold Cross-Validation Accuracy Mean: {cv_scores.mean()*100:.2f}% (+/- {cv_scores.std()*100:.2f}%)")
    
    # Model Training
    start_time = time.time()
    rf_classifier.fit(X_train, y_train)
    training_duration = time.time() - start_time
    print(f"[*] Model training completed in {training_duration:.2f} seconds.")
    
    # Blind Testing Evaluation
    print("[*] Evaluating model on blind test partition...")
    y_pred = rf_classifier.predict(X_test)
    
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    print("\n================ EMPIRICAL EVALUATION RESULTS ================")
    print(f"Accuracy  : {accuracy * 100:.2f}%")
    print(f"Precision : {precision * 100:.2f}%")
    print(f"Recall    : {recall * 100:.2f}%")
    print(f"F1-Score  : {f1 * 100:.2f}%")
    print("\nConfusion Matrix:")
    print(cm)
    print("==============================================================")
    
    return rf_classifier, {
        "accuracy": accuracy, "precision": precision, 
        "recall": recall, "f1": f1, "confusion_matrix": cm
    }