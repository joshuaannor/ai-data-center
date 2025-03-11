async function fetchMetrics() {
    const response = await fetch('https://musical-computing-machine-745pgxwjrjj2r479-5000.app.github.dev/metrics');
    const data = await response.json();
    const metricsDiv = document.getElementById('metrics');

    metricsDiv.innerHTML = "";
    for (let server in data) {
        let html = `<h3>📌 ${server}</h3>`;
        html += `<p>CPU Usage: ${data[server].cpu_usage}%</p>`;
        html += `<p>Memory Usage: ${data[server].memory_usage}%</p>`;
        html += `<p>Disk Usage: ${data[server].disk_usage}%</p>`;
        metricsDiv.innerHTML += html;
    }
}

setInterval(fetchMetrics, 3000);
fetchMetrics();
