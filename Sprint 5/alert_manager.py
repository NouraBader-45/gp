"""
Sprint 5 - Alert Management and Notification

Preliminary Proof of Concept

This module demonstrates basic local alert-management functionality
using SQLite.

It provides initial functions for:
- creating the alert database,
- storing security alerts,
- retrieving alerts,
- retrieving a specific alert,
- acknowledging an alert.

This is not the final Sprint 5 implementation.
"""

import sqlite3
from datetime import datetime


DATABASE_FILE = "assas_alerts.db"


def get_connection():
    """
    Create and return a connection to the local SQLite database.
    """
    connection = sqlite3.connect(DATABASE_FILE)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    """
    Create the alerts table if it does not already exist.
    """

    connection = get_connection()

    connection.execute(
        """
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
        )
        """
    )

    connection.commit()
    connection.close()


def add_alert(
    alert_source,
    description,
    device_id=None,
    alert_type=None,
    severity=None,
    risk_score=None
):
    """
    Store a new security alert in the local database.
    """

    connection = get_connection()

    timestamp = datetime.now().isoformat()

    cursor = connection.execute(
        """
        INSERT INTO alerts (
            device_id,
            timestamp,
            alert_source,
            alert_type,
            severity,
            description,
            risk_score,
            status
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, 'New')
        """,
        (
            device_id,
            timestamp,
            alert_source,
            alert_type,
            severity,
            description,
            risk_score
        )
    )

    connection.commit()

    alert_id = cursor.lastrowid

    connection.close()

    return alert_id


def get_all_alerts():
    """
    Retrieve all stored alerts, newest first.
    """

    connection = get_connection()

    rows = connection.execute(
        """
        SELECT *
        FROM alerts
        ORDER BY id DESC
        """
    ).fetchall()

    connection.close()

    return [dict(row) for row in rows]


def get_alert(alert_id):
    """
    Retrieve one alert by its ID.
    """

    connection = get_connection()

    row = connection.execute(
        """
        SELECT *
        FROM alerts
        WHERE id = ?
        """,
        (alert_id,)
    ).fetchone()

    connection.close()

    if row is None:
        return None

    return dict(row)


def acknowledge_alert(alert_id):
    """
    Change an alert status to Acknowledged.
    """

    connection = get_connection()

    cursor = connection.execute(
        """
        UPDATE alerts
        SET status = 'Acknowledged'
        WHERE id = ?
        """,
        (alert_id,)
    )

    connection.commit()

    updated = cursor.rowcount > 0

    connection.close()

    return updated


if __name__ == "__main__":

    initialize_database()

    sample_alert_id = add_alert(
        alert_source="Suricata",
        alert_type="Signature-Based Detection",
        severity=2,
        description="Example security alert generated for feasibility testing."
    )

    print(f"Created sample alert with ID: {sample_alert_id}")

    print("Stored alerts:")

    for alert in get_all_alerts():
        print(alert)
