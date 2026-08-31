-- Sprint 5 - Alert Management
-- Preliminary SQLite schema for storing security alerts.
-- The schema will be refined after integration with previous sprints.

CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,

    device_id TEXT,

    timestamp TEXT NOT NULL,

    alert_source TEXT NOT NULL,

    alert_type TEXT,

    severity INTEGER,

    description TEXT,

    risk_score REAL,

    status TEXT NOT NULL DEFAULT 'New'
        CHECK (status IN ('New', 'Viewed', 'Acknowledged')),

    created_at TEXT DEFAULT CURRENT_TIMESTAMP
);
