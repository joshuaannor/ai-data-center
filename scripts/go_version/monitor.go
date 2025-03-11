package main

import (
    "encoding/json"
    "fmt"
    "io/ioutil"
    "log"
)

// Define a struct for server metrics
type ServerMetrics struct {
    CPUUsage    int `json:"cpu_usage"`
    MemoryUsage int `json:"memory_usage"`
    DiskUsage   int `json:"disk_usage"`
}

func loadMetrics(filename string) map[string]ServerMetrics {
    data, err := ioutil.ReadFile(filename)
    if err != nil {
        log.Fatalf("Error loading metrics: %v", err)
    }

    var metrics map[string]ServerMetrics
    err = json.Unmarshal(data, &metrics)
    if err != nil {
        log.Fatalf("Error parsing JSON: %v", err)
    }

    return metrics
}

func main() {
    fmt.Println("🔍 AI Data Center Monitoring (Go Version) Started...")
    metrics := loadMetrics("configs/sample_metrics.json")
    fmt.Printf("Loaded Metrics: %+v\n", metrics)
}
