import streamlit as st
import sys
import io

# Import your existing Citadel engine
from main import assemble_citadel

# Set up the Web Page
st.set_page_config(page_title="Treasure Box AI", page_icon="📦", layout="wide")

st.title("📦 Treasure Box AI Citadel")
st.markdown("**The 28-Node Multi-Agent Enterprise Engine**")
st.markdown("---")

# The User Input Box
user_prompt = st.text_area("Enter your enterprise project request for the Chief:", height=100)

if st.button("🚀 Ignite the Citadel"):
    if not user_prompt:
        st.warning("Please enter a request for the Chief.")
    else:
        st.info("Unlocking the Citadel... Booting 28 AI Agents. Please wait.")
        
        # Create a spinner while the AI works
        with st.spinner("The Departments are currently executing your request..."):
            
            # Capture the terminal output to display in the UI (Optional but cool)
            old_stdout = sys.stdout
            new_stdout = io.StringIO()
            sys.stdout = new_stdout
            
            try:
                # 1. Boot up your exact engine from main.py
                citadel = assemble_citadel(user_prompt)
                
                # 2. Run the AI
                result = citadel.kickoff()
                
                # Restore terminal printing
                sys.stdout = old_stdout
                
                st.success("Task Completed!")
                
                # Display the Final Output elegantly
                st.markdown("### 👑 Final Output From The Chief")
                st.write(result)
                
                # Show the raw logs in an expandable box for nerds
                with st.expander("View Raw Agent Communication Logs"):
                    st.text(new_stdout.getvalue())
                    
            except Exception as e:
                sys.stdout = old_stdout
                st.error(f"An error occurred in the Citadel: {e}")
