import asyncio
from typing import Annotated, Dict, Any
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext
import datetime

AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyY2FkNzc5MC1jYmFkLTRkNDItYmZiZS1kZGM2MzgzNWNkYjUiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjFiYTVmMzAzLTA0M2YtNDA1My1iMWIwLWFkYmJlNzhhOGZiNSJ9.abc123..."  # Use your actual JWT
session = GenAISession(jwt_token=AGENT_JWT)

@session.bind(
    name="patient_communication_agent",
    description="Sends appointment reminders and handles patient queries"
)
async def patient_communication_agent(
    agent_context: GenAIContext,
    patient_id: Annotated[str, "Patient ID for communication"],
    message: Annotated[str, "Message to send to the patient or contact"],
    contact_info: Annotated[str, "Contact information for the patient or emergency contact"]
) -> Dict[str, Any]:
    """Sends appointment reminders and handles patient queries"""
    agent_context.logger.info(f"Sending message to patient: {patient_id}")
    # Example logic
    return {
        "patient_id": patient_id,
        "message": message,
        "contact_info": contact_info,
        "status": "Message sent",
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }

async def main():
    print(f"Patient Communication Agent started with token '{AGENT_JWT}'")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
