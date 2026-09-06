interface UnitMetrics {
    bed_occupancy_rate: number;
    avg_wait_time_minutes: number;
    patient_backlog: number;
}

type FacilityMetrics = Record<string, UnitMetrics>;

const API_URL = "http://localhost:5000/metrics";

async function fetchMetrics(): Promise<void> {
    const response = await fetch(API_URL);
    const data: FacilityMetrics = await response.json();
    const metricsDiv = document.getElementById('metrics') as HTMLDivElement;

    metricsDiv.innerHTML = "";
    for (const unit in data) {
        const unitMetrics = data[unit];
        let html = `<h3>🏥 ${unit}</h3>`;
        html += `<p>Bed Occupancy Rate: ${unitMetrics.bed_occupancy_rate}%</p>`;
        html += `<p>Avg Wait Time: ${unitMetrics.avg_wait_time_minutes} min</p>`;
        html += `<p>Patient Backlog: ${unitMetrics.patient_backlog}</p>`;
        metricsDiv.innerHTML += html;
    }
}

setInterval(fetchMetrics, 3000);
fetchMetrics();
