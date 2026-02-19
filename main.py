from crewai import Crew, Process

# FIXED BUG 1: Changed 'engine.tasks' to 'engine.task' to match your actual file name
from engine.task import create_master_task

# Import all 28 personalities from the engine
from engine.agents import (
    chief_agent, 
    head_architect, head_recon, head_quant, head_engineering, 
    head_mechanic, head_solver, head_red_team, head_lawyer, head_wordsmith,
    junior_ui_ux, junior_logic, junior_scraper, junior_api,
    junior_statistician, junior_cleanser, junior_frontend, junior_backend,
    junior_docker, junior_deps, junior_tester, junior_edge,
    junior_pen, junior_static, junior_copyright, junior_privacy,
    junior_tech_writer, junior_copywriter
)

def assemble_citadel(user_request: str):
    # 1. Generate the dynamic master objective
    master_task = create_master_task(user_request)

    # ==========================================
    # 2. ASSEMBLE THE MASTER CITADEL 
    # In CrewAI's hierarchical process, ALL agents must exist in the master array.
    # The Chief will dynamically delegate to the Heads, who will delegate to the Helpers.
    # ==========================================
    
    master_citadel = Crew(
        agents=[
            # Tier 2: The Department Heads (Middle Managers)
            head_architect, head_recon, head_quant, head_engineering, 
            head_mechanic, head_solver, head_red_team, head_lawyer, head_wordsmith,
            
            # Tier 3: The Junior Helpers (The Laborers)
            junior_ui_ux, junior_logic, junior_scraper, junior_api,
            junior_statistician, junior_cleanser, junior_frontend, junior_backend,
            junior_docker, junior_deps, junior_tester, junior_edge,
            junior_pen, junior_static, junior_copyright, junior_privacy,
            junior_tech_writer, junior_copywriter
        ],
        tasks=[master_task],
        manager_agent=chief_agent,
        process=Process.hierarchical,
        verbose=True
    )

    return master_citadel

if __name__ == "__main__":
    print("\n=== TREASURE BOX AI CITADEL ONLINE ===")
    user_prompt = input("\nEnter your enterprise project request: ")
    
    print("\nUnlocking the Citadel... Booting 28 AI Agents.")
    citadel = assemble_citadel(user_prompt)
    
    # Ignition
    result = citadel.kickoff()
    
    print("\n\n=== FINAL OUTPUT FROM THE CHIEF ===")
    print(result)
