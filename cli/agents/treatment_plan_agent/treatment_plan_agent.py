import asyncio
from typing import Annotated, Dict, Any, List
from genai_session.session import GenAISession
from genai_session.utils.context import GenAIContext

AGENT_JWT = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiI1OTdkZGI0Mi02NTJkLTQyMGYtYjgwNy02YWE5MzBlODJiODEiLCJleHAiOjI1MzQwMjMwMDc5OSwidXNlcl9pZCI6IjFiYTVmMzAzLTA0M2YtNDA1My1iMWIwLWFkYmJlNzhhOGZiNSJ9.abc123..."  # Use your actual JWT
session = GenAISession(jwt_token=AGENT_JWT)

@session.bind(
    name="treatment_plan_agent",
    description="Creates personalized treatment plans and monitors progress"
)
async def treatment_plan_agent(
    agent_context: GenAIContext,
    diagnosis: Annotated[str, "Primary diagnosis for the patient"],
    patient_id: Annotated[str, "Patient ID for the treatment plan"],
    age: Annotated[int, "Patient's age"],
    recommended_tests: Annotated[List[str], "Tests recommended for the patient"]
) -> Dict[str, Any]:
    """Creates personalized treatment plans and monitors progress"""
    agent_context.logger.info(f"Creating treatment plan for patient: {patient_id}")
    # Example logic
    return {
        "patient_id": patient_id,
        "diagnosis": diagnosis,
        "age": age,
        "recommended_tests": recommended_tests,
        "treatment_plan": [
            "Start oxygen therapy immediately.",
            "Administer aspirin 325mg orally.",
            "Prepare for possible cardiac intervention.",
            "Monitor vital signs continuously."
        ],
        "follow_up_instructions": "Repeat ECG and troponin in 1 hour. Consult cardiology if no improvement."
    }

async def main():
    print(f"Treatment Plan Agent started with token '{AGENT_JWT}'")
    await session.process_events()

if __name__ == "__main__":
    asyncio.run(main())
