// Lightweight React dashboard, loaded via CDN React/ReactDOM/Babel Standalone
// (see react-dashboard.html) — no build tooling required. This is an
// additional view alongside the original TypeScript-compiled dashboard,
// not a replacement for it.

const { useState, useEffect } = React;

const API_URL = "http://localhost:5000/metrics";

function UnitCard({ name, metrics }) {
    return (
        <div className="unit-card">
            <h3>🏥 {name}</h3>
            <p>Bed Occupancy Rate: {metrics.bed_occupancy_rate}%</p>
            <p>Avg Wait Time: {metrics.avg_wait_time_minutes} min</p>
            <p>Patient Backlog: {metrics.patient_backlog}</p>
        </div>
    );
}

function Dashboard() {
    const [metrics, setMetrics] = useState({});
    const [error, setError] = useState(null);

    useEffect(() => {
        async function fetchMetrics() {
            try {
                const response = await fetch(API_URL);
                const data = await response.json();
                setMetrics(data);
                setError(null);
            } catch (err) {
                setError("Unable to reach the metrics API. Is app.py running?");
            }
        }

        fetchMetrics();
        const interval = setInterval(fetchMetrics, 3000);
        return () => clearInterval(interval);
    }, []);

    if (error) {
        return <p className="error">{error}</p>;
    }

    return (
        <div id="metrics">
            {Object.entries(metrics).map(([name, unitMetrics]) => (
                <UnitCard key={name} name={name} metrics={unitMetrics} />
            ))}
        </div>
    );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<Dashboard />);
