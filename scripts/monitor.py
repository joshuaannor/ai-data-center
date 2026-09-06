import json
import time
import random
import logging
import csv

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
    """Randomly adjusts unit metrics to simulate real-time changes."""
    for unit, data in metrics.items():
        data["bed_occupancy_rate"] = max(0, min(100, data["bed_occupancy_rate"] + random.randint(-10, 10)))
        data["avg_wait_time_minutes"] = max(0, data["avg_wait_time_minutes"] + random.randint(-10, 10))
        data["patient_backlog"] = max(0, data["patient_backlog"] + random.randint(-5, 5))
    return metrics

def detect_anomalies(metrics):
    """Detects anomalies in bed occupancy, wait time, and patient backlog and logs them."""
    with open("logs/monitoring_alerts.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Unit", "Metric", "Value", "Alert Type"])

        for unit, data in metrics.items():
            if data["bed_occupancy_rate"] > 90:
                alert = f"⚠ High bed occupancy detected on {unit}: {data['bed_occupancy_rate']}%"
                print(alert)
                logging.warning(alert)
                writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), unit, "Bed Occupancy Rate", data["bed_occupancy_rate"], "High Bed Occupancy"])

            if data["avg_wait_time_minutes"] > 60:
                alert = f"⚠ Long wait time detected on {unit}: {data['avg_wait_time_minutes']} min"
                print(alert)
                logging.warning(alert)
                writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), unit, "Avg Wait Time Minutes", data["avg_wait_time_minutes"], "Long Wait Time"])

            if data["patient_backlog"] > 15:
                alert = f"⚠ High patient backlog detected on {unit}: {data['patient_backlog']}"
                print(alert)
                logging.warning(alert)
                writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), unit, "Patient Backlog", data["patient_backlog"], "High Patient Backlog"])


if __name__ == "__main__":
    print(" AI Data Center Monitoring Started...")
    
    for _ in range(5):  # Simulate 5 monitoring cycles
        metrics = load_metrics()
        if metrics:
            updated_metrics = simulate_data(metrics)
            detect_anomalies(updated_metrics)
            time.sleep(2)  # Pause to simulate real-time monitoring
