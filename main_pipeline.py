from preprocessing import load_and_preprocess_data
from train_model import train_and_evaluate
from digital_twin_sim import NetworkDigitalTwin
from dss_engine import DecisionSupportSystem

if __name__ == "__main__":
    # Corrected path pointing into your datasets/ folder
    dataset_file = "datasets/Friday-WorkingHours-Afternoon-DDos.pcap_ISCX.csv"
    
    # 1. Preprocess data
    X_train, X_test, y_train, y_test = load_and_preprocess_data(dataset_file)
    
    # 2. Train model and evaluate performance metrics & confusion matrix
    model, metrics = train_and_evaluate(X_train, X_test, y_train, y_test)
    
    # 3. Simulate Digital Twin environment synchronization & attack propagation
    dt = NetworkDigitalTwin()
    sync_status = dt.synchronize_telemetry(X_test)
    print(f"\n[Digital Twin Status]: {sync_status}")
    propagation_path = dt.simulate_attack_propagation("Web_Server_01", "DDoS")
    
    # 4. Generate AI-DSS Mitigations and calculate MTTR proxy
    dss = DecisionSupportSystem()
    directive = dss.generate_mitigation_directive("DDoS", metrics['precision'])
    print("\n[AI-DSS Actionable Directives Successfully Compiled]")
    for key, val in directive.items():
        print(f"  {key}: {val}")