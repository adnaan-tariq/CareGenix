import asyncio
from typing import Annotated, Dict, Any
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
import requests

AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIwNWMxZTA4Ni02Mzc4LTRhYTUtYmI4Yi1kNWYwYjZlNDM5Y2EiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjFiYTVmMzAzLTA0M2YtNDA1My1iMWIwLWFkYmJlNzhhOGZiNSJ9.89T3hOi83turP40ughVs_-JxPR_PCJWPiaauURUA0UQ" # noqa: E501
session = GenAISession(jwt_token=AGENT_JWT)


@session.bind(
    name="patient_intake_agent",
    description="Handles initial patient registration and triage"
)
async def patient_intake_agent(
    agent_context: GenAIContext,
    patient_name: Annotated[str, "Patient's full name"],
    symptoms: Annotated[str, "Patient's reported symptoms"],
    age: Annotated[int, "Patient's age"],
    emergency_contact: Annotated[str, "Emergency contact information"],
    email: Annotated[str, "Patient's email address"]
) -> Dict[str, Any]:
    """Handles initial patient registration and triage"""
    agent_context.logger.info(f"Processing intake for patient: {patient_name}")
    
    # Generate patient ID
    patient_id = f"P{hash(patient_name) % 10000:04d}"
    
    # Triage logic
    triage_level = "low"
    urgency_notes = ""
    
    # Check for high-priority symptoms
    high_priority_symptoms = ["chest pain", "shortness of breath", "unconscious", "severe bleeding", "stroke"]
    if any(symptom in symptoms.lower() for symptom in high_priority_symptoms):
        triage_level = "high"
        urgency_notes = "Immediate medical attention required"
    
    # Check for medium-priority symptoms
    elif any(symptom in symptoms.lower() for symptom in ["fever", "severe pain", "dizziness", "nausea"]):
        triage_level = "medium"
        urgency_notes = "Should be seen within 2-4 hours"
    
    # Age-based adjustments
    if age > 65 and triage_level == "low":
        triage_level = "medium"
        urgency_notes = "Elderly patient - increased monitoring recommended"
    
    # Pediatric considerations
    if age < 18 and "fever" in symptoms.lower():
        triage_level = "medium"
        urgency_notes = "Pediatric fever - requires prompt evaluation"

    # Send notification email via n8n webhook
    n8n_webhook_url = "https://inboxwatcher.app.n8n.cloud/webhook/a9449eba-ae6b-4591-8df0-416b27a79ecb"
    payload = {
        "email": email,
        "patient_name": patient_name,
        "symptoms": symptoms,
        "triage_level": triage_level,
        "emergency_contact": emergency_contact
    }
    try:
        requests.post(n8n_webhook_url, json=payload, timeout=10)
        agent_context.logger.info(f"Notification sent to n8n webhook for {email}")
    except Exception as e:
        agent_context.logger.error(f"Failed to notify via n8n: {e}")
    
    return {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "age": age,
        "symptoms": symptoms,
        "triage_level": triage_level,
        "urgency_notes": urgency_notes,
        "emergency_contact": emergency_contact,
        "email": email,
        "recommended_action": f"Priority {triage_level.upper()} - {urgency_notes}" if urgency_notes else f"Priority {triage_level.upper()} - routine care",
        "timestamp": asyncio.get_event_loop().time()
    }


async def main():
    print(f"Patient Intake Agent started with token '{AGENT_JWT}'")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
