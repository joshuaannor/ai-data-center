// This is an intentional second implementation of the /metrics endpoint,
// built to get hands-on familiarity with Node/Express alongside the
// primary Flask backend (app.py) — it is not meant to replace it.
// It serves the exact same data, read from the same config file.

const express = require('express');
const cors = require('cors');
const path = require('path');
const fs = require('fs');

const app = express();
app.use(cors());

const CONFIG_FILE = path.join(__dirname, '..', 'configs', 'sample_metrics.json');

function loadMetrics() {
    try {
        const raw = fs.readFileSync(CONFIG_FILE, 'utf8');
        return JSON.parse(raw);
    } catch (err) {
        return { error: 'Metrics file not found' };
    }
}

app.get('/metrics', (req, res) => {
    res.json(loadMetrics());
});

const PORT = process.env.PORT || 5001;
app.listen(PORT, '0.0.0.0', () => {
    console.log(`Express metrics server running at http://localhost:${PORT}/metrics`);
});
