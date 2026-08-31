"""
Sprint 5 - FastAPI Alert Interface

Preliminary Proof of Concept

This module demonstrates how locally stored alert information can be
made available through RESTful FastAPI endpoints.

The final API will include additional endpoints for devices,
traffic statistics, risk information, and other dashboard data.

This is not the final backend implementation.
"""

from fastapi import FastAPI, HTTPException

from alert_manager import (
    initialize_database,
    get_all_alerts,
    get_alert,
    acknowledge_alert
)


app = FastAPI(
    title="Assas Sprint 5 Preliminary API",
    description="Preliminary REST API for Sprint 5 alert management.",
    version="0.1"
)


@app.on_event("startup")
def startup_event():
    """
    Initialize the local alert database when the API starts.
    """
    initialize_database()


@app.get("/")
def root():
    """
    Basic API status endpoint.
    """

    return {
        "message": "Assas Sprint 5 preliminary API is running."
    }


@app.get("/alerts")
def read_alerts():
    """
    Return all stored security alerts.
    """

    return {
        "alerts": get_all_alerts()
    }


@app.get("/alerts/{alert_id}")
def read_alert(alert_id: int):
    """
    Return one security alert.
    """

    alert = get_alert(alert_id)

    if alert is None:
        raise HTTPException(
            status_code=404,
            detail="Alert not found."
        )

    return alert


@app.patch("/alerts/{alert_id}/acknowledge")
def acknowledge(alert_id: int):
    """
    Acknowledge a security alert.
    """

    updated = acknowledge_alert(alert_id)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Alert not found."
        )

    return {
        "alert_id": alert_id,
        "status": "Acknowledged"
    }
