import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE
import os

def load_and_preprocess_data(file_path):
    print(f"[*] Loading dataset from {file_path}...")
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset file not found at {file_path}")
    
    # Load CSV file
    df = pd.read_csv(file_path)
    
    # Clean column names (strip whitespace)
    df.columns = df.columns.str.strip()
    
    print(f"[*] Initial dataset shape: {df.shape}")
    
    # Handle infinite and missing values
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)
    
    # Target label formatting (CIC-IDS2017 uses 'Label')
    if 'Label' in df.columns:
        df['Target'] = df['Label'].apply(lambda x: 0 if str(x).strip().upper() == 'BENIGN' else 1)
        X = df.drop(columns=['Label', 'Target'])
        y = df['Target']
    else:
        raise KeyError("Target 'Label' column missing from dataset structure.")
    
    # Select numeric features only for anomaly detection
    X_numeric = X.select_dtypes(include=[np.number])
    print(f"[*] Retained {X_numeric.shape[1]} numeric flow features.")
    
    # Feature Normalization (Min-Max Scaling)
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X_numeric)
    
    # Apply SMOTE to rectify class imbalance
    print("[*] Applying Synthetic Minority Over-sampling Technique (SMOTE)...")
    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_scaled, y)
    
    # 80/20 Data Partitioning
    X_train, X_test, y_train, y_test = train_test_split(
        X_resampled, y_resampled, test_size=0.2, random_state=42
    )
    
    print(f"[*] Training Set Shape: {X_train.shape}, Test Set Shape: {X_test.shape}")
    return X_train, X_test, y_train, y_test