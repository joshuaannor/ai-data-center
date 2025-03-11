import json
import time
import random
import logging

# Setup logging
LOG_FILE = "logs/monitoring_alerts.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(message)s")

# Load sample data
CONFIG_FILE = "configs/sample_metrics.json"

def load_metrics():
    """Loads server metrics from JSON file."""
    try:
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        logging.error("Error: Sample metrics file not found.")
        return {}

def simulate_data(metrics):
    """Randomly adjusts server metrics to simulate real-time changes."""
    for server, data in metrics.items():
        data["cpu_usage"] = max(0, min(100, data["cpu_usage"] + random.randint(-10, 10)))
        data["memory_usage"] = max(0, min(100, data["memory_usage"] + random.randint(-10, 10)))
        data["disk_usage"] = max(0, min(100, data["disk_usage"] + random.randint(-5, 5)))
    return metrics

def detect_anomalies(metrics):
    """Detects anomalies in CPU, memory, and disk usage."""
    for server, data in metrics.items():
        if data["cpu_usage"] > 85:
            alert = f"⚠ High CPU usage detected on {server}: {data['cpu_usage']}%"
            print(alert)
            logging.warning(alert)
        if data["memory_usage"] > 90:
            alert = f"⚠ High Memory usage detected on {server}: {data['memory_usage']}%"
            print(alert)
            logging.warning(alert)
        if data["disk_usage"] > 80:
            alert = f"⚠ High Disk usage detected on {server}: {data['disk_usage']}%"
            print(alert)
            logging.warning(alert)

if __name__ == "__main__":
    print(" AI Data Center Monitoring Started...")
    
    for _ in range(5):  # Simulate 5 monitoring cycles
        metrics = load_metrics()
        if metrics:
            updated_metrics = simulate_data(metrics)
            detect_anomalies(updated_metrics)
            time.sleep(2)  # Pause to simulate real-time monitoring
