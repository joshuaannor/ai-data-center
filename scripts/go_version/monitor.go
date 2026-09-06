package main

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"log"
)

// Define a struct for hospital unit metrics
type UnitMetrics struct {
	BedOccupancyRate   int `json:"bed_occupancy_rate"`
	AvgWaitTimeMinutes int `json:"avg_wait_time_minutes"`
	PatientBacklog     int `json:"patient_backlog"`
}

func loadMetrics(filename string) map[string]UnitMetrics {
	data, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatalf("Error loading metrics: %v", err)
	}

	var metrics map[string]UnitMetrics
	err = json.Unmarshal(data, &metrics)
	if err != nil {
		log.Fatalf("Error parsing JSON: %v", err)
	}

	return metrics
}

func main() {
	fmt.Println("🏥 Healthcare Facility Operations Monitoring (Go Version) Started...")
	metrics := loadMetrics("configs/sample_metrics.json")
	fmt.Printf("Loaded Metrics: %+v\n", metrics)
}
