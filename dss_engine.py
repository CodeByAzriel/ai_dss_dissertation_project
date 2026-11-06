import time

class DecisionSupportSystem:
    def __init__(self):
        self.mitigation_playbooks = {
            "DDoS": [
                "1. Apply rate-limiting rules on Edge Firewall for source subnet.",
                "2. Reroute anomalous traffic flow through scrubbing center.",
                "3. Scale up cloud gateway compute instances."
            ],
            "PortScan": [
                "1. Temporarily quarantine source IP address in access control list (ACL).",
                "2. Inspect SSH and RDP daemon logs on internal bastions.",
                "3. Enable strict SYN-flood port protection."
            ],
            "Default": [
                "1. Isolate compromised subnet node in Digital Twin sandbox.",
                "2. Capture memory dump for forensic analysis.",
                "3. Notify senior security operations engineer."
            ]
        }

    def generate_mitigation_directive(self, threat_type, confidence_score):
        start_generation = time.time()
        playbook = self.mitigation_playbooks.get(threat_type, self.mitigation_playbooks["Default"])
        
        directive = {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "threat_classification": threat_type,
            "confidence_rating": f"{confidence_score * 100:.2f}%",
            "priority_level": "CRITICAL" if confidence_score > 0.90 else "MODERATE",
            "recommended_actions": playbook
        }
        
        generation_latency = (time.time() - start_generation) * 1000
        directive["decision_latency_ms"] = round(generation_latency, 2)
        return directive