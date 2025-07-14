import asyncio
from typing import Annotated, Dict, Any, List
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext

AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJlM2Q3OWIyOS1mZDM3LTRjZmMtYTQ3MS1jM2I5M2M4ZmVkZGQiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjFiYTVmMzAzLTA0M2YtNDA1My1iMWIwLWFkYmJlNzhhOGZiNSJ9.abc123..."  # Use your actual JWT
session = GenAISession(jwt_token=AGENT_JWT)

@session.bind(
    name="diagnostic_assistant_agent",
    description="Analyzes symptoms and suggests possible diagnoses"
)
async def diagnostic_assistant_agent(
    agent_context: GenAIContext,
    symptoms: Annotated[str, "Patient's symptoms"],
    age: Annotated[int, "Patient's age"],
    medical_history: Annotated[List[str], "Patient's medical history"],
    triage_level: Annotated[str, "Triage level from intake agent"]
) -> Dict[str, Any]:
    """Advanced diagnostic assistant with clinical reasoning"""
    agent_context.logger.info(f"Analyzing symptoms: {symptoms}")
    # Example logic
    return {
        "symptoms": symptoms,
        "age": age,
        "medical_history": medical_history,
        "triage_level": triage_level,
        "possible_diagnoses": [
            {"condition": "Acute Coronary Syndrome", "probability": "high", "reasoning": "Chest pain radiating to left arm"},
            {"condition": "Myocardial Infarction", "probability": "medium", "reasoning": "History of hypertension and diabetes"}
        ],
        "recommended_tests": ["ECG", "Troponin", "Chest X-ray"],
        "red_flags": ["Chest pain with radiation", "Shortness of breath"],
        "clinical_notes": "Immediate cardiac evaluation recommended."
    }

async def main():
    print(f"Diagnostic Assistant Agent started with token '{AGENT_JWT}'")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
