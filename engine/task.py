from crewai import Task

def create_master_task(user_request: str):
    """Generates the overarching objective for the Citadel."""
    return Task(
        description=f"Execute the following master project: '{user_request}'. The Chief must coordinate all 9 Department Heads to architect, research, build, test, secure, and document the final deliverable.",
        expected_output="A flawless, multi-departmental final product, ready for deployment.",
        # The Chief dynamically assigns sub-tasks to the Heads
    )
