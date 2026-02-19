from crewai import Crew, Process
from engine.tasks import create_master_task

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
    # 2. ASSEMBLE THE DEPARTMENTS (Binding Tier 2 to Tier 3)
    # This is where the helpers learn who their boss is.
    # ==========================================
    
    strategy_dept = Crew(
        agents=[junior_ui_ux, junior_logic],
        manager_agent=head_architect,
        process=Process.hierarchical, verbose=True
    )
    
    recon_dept = Crew(
        agents=[junior_scraper, junior_api],
        manager_agent=head_recon,
        process=Process.hierarchical, verbose=True
    )
    
    quant_dept = Crew(
        agents=[junior_statistician, junior_cleanser],
        manager_agent=head_quant,
        process=Process.hierarchical, verbose=True
    )
    
    engineering_dept = Crew(
        agents=[junior_frontend, junior_backend],
        manager_agent=head_engineering,
        process=Process.hierarchical, verbose=True
    )
    
    infrastructure_dept = Crew(
        agents=[junior_docker, junior_deps],
        manager_agent=head_mechanic,
        process=Process.hierarchical, verbose=True
    )
    
    qa_dept = Crew(
        agents=[junior_tester, junior_edge],
        manager_agent=head_solver,
        process=Process.hierarchical, verbose=True
    )
    
    security_dept = Crew(
        agents=[junior_pen, junior_static],
        manager_agent=head_red_team,
        process=Process.hierarchical, verbose=True
    )
    
    compliance_dept = Crew(
        agents=[junior_copyright, junior_privacy],
        manager_agent=head_lawyer,
        process=Process.hierarchical, verbose=True
    )
    
    marketing_dept = Crew(
        agents=[junior_tech_writer, junior_copywriter],
        manager_agent=head_wordsmith,
        process=Process.hierarchical, verbose=True
    )

    # ==========================================
    # 3. ASSEMBLE THE MASTER CITADEL (Binding Tier 1 to Tier 2)
    # The Chief manages the Department Heads.
    # ==========================================
    
    master_citadel = Crew(
        # We put the Department Heads in the main room with the Chief
        agents=[
            head_architect, head_recon, head_quant, head_engineering, 
            head_mechanic, head_solver, head_red_team, head_lawyer, head_wordsmith
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
