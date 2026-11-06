import time
import random

class NetworkDigitalTwin:
    def __init__(self):
        self.topology = {
            "Subnet_DMZ": ["Firewall_Edge", "Web_Server_01"],
            "Subnet_Internal": ["Database_Core", "Employee_Workstations"],
            "Subnet_Cloud": ["AWS_S3_Gateway", "Auth_Microservice"]
        }
        self.active_state = "STABLE"

    def synchronize_telemetry(self, packet_stream_batch):
        start_sync = time.time()
        active_nodes = sum(len(nodes) for nodes in self.topology.values())
        sync_latency = (len(packet_stream_batch) / 1000.0) * 0.015 + random.uniform(0.005, 0.020)
        time.sleep(min(sync_latency, 0.05))
        
        return {
            "status": "SYNCHRONIZED",
            "nodes_monitored": active_nodes,
            "sync_latency_ms": round(sync_latency * 1000, 2)
        }

    def simulate_attack_propagation(self, entry_node, attack_type):
        print(f"\n[DIGITAL TWIN SANDBOX] Initiating simulation for [{attack_type}] starting at {entry_node}...")
        if entry_node in self.topology["Subnet_DMZ"]:
            propagation_path = ["Subnet_DMZ -> Firewall_Edge", "Subnet_Internal -> Database_Core"]
        else:
            propagation_path = [f"{entry_node} -> Internal Routing", "Subnet_Cloud -> Auth_Microservice"]
            
        print(f"[DIGITAL TWIN SANDBOX] Simulated Threat Propagation Path: {' ==> '.join(propagation_path)}")
        return propagation_path