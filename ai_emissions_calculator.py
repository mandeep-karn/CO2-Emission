import streamlit as st
import plotly.graph_objects as plt
import plotly.express as px
import pandas as pd

def calculate_emissions(queries, model):
    # Emission factors (estimates based on current research)
    EMISSION_FACTORS = {
        'ChatGPT-3.5': 0.0028,  # kg CO2 per query
        'ChatGPT-4': 0.0045,    # kg CO2 per query
        'Claude': 0.0032,       # kg CO2 per query
        'Gemini': 0.0037,       # kg CO2 per query
    }
    
    # Calculate emissions
    emission_factor = EMISSION_FACTORS[model]
    total_emissions = queries * emission_factor
    
    return total_emissions

def get_comparative_context(emissions):
    # Comparative emissions contexts
    contexts = [
        f"Equivalent to driving a car for approximately {emissions / 0.192:.2f} kilometers.",
        f"About the same CO2 as charging {emissions / 0.075:.2f} smartphones.",
        f"Roughly {emissions / 0.5 * 100:.2f}% of the carbon footprint of a typical coffee."
    ]
    return contexts

def create_emissions_chart(queries, total_emissions):
    # Create data for pie chart
    data = {
        'Category': ['AI Query Emissions', 'Remaining Carbon Budget'],
        'Value': [total_emissions, max(0, 1 - total_emissions)]
    }
    df = pd.DataFrame(data)
    
    # Create pie chart using Plotly
    fig = px.pie(
        df, 
        values='Value', 
        names='Category', 
        title=f'CO2 Emissions for {queries} Queries',
        color_discrete_sequence=['#FF6384', '#36A2EB']
    )
    
    return fig

def main():
    # Set page configuration
    st.set_page_config(
        page_title="AI Sustainability Calculator", 
        page_icon="🌍", 
        layout="centered"
    )

    # Title and description
    st.title("🌍 AI Query CO2 Emissions Calculator")
    st.markdown("""
    ### Understanding the Environmental Impact of AI Queries

    This tool helps you estimate the carbon footprint of AI interactions. 
    Select an AI model and input the number of queries to see the environmental impact.
    """)

    # Sidebar for inputs
    st.sidebar.header("Calculation Inputs")
    
    # Model selection
    models = [
        'ChatGPT-3.5', 
        'ChatGPT-4', 
        'Claude', 
        'Gemini'
    ]
    selected_model = st.sidebar.selectbox(
        "Select AI Model", 
        models, 
        index=0
    )

    # Query input
    queries = st.sidebar.number_input(
        "Number of Queries", 
        min_value=1, 
        max_value=10000, 
        value=10, 
        step=1
    )

    # Calculate emissions
    if st.sidebar.button("Calculate Emissions"):
        # Perform calculations
        total_emissions = calculate_emissions(queries, selected_model)
        
        # Results section
        st.header("Results")
        
        # Emissions value
        st.metric(
            label=f"Estimated CO2 Emissions for {queries} {selected_model} Queries", 
            value=f"{total_emissions:.4f} kg CO2"
        )
        
        # Comparative context
        st.subheader("Comparative Context")
        contexts = get_comparative_context(total_emissions)
        for context in contexts:
            st.write(f"• {context}")
        
        # Emissions Chart
        st.subheader("Emissions Breakdown")
        emissions_chart = create_emissions_chart(queries, total_emissions)
        st.plotly_chart(emissions_chart)

    # Additional information
    st.markdown("""
    ### About This Calculator
    - Emission factors are estimates based on current research
    - Values may vary depending on specific AI model and computational resources
    - Aims to raise awareness about the environmental impact of AI technologies
    """)

    # Footer
    st.markdown("""
    ---
    *Created for AI Sustainability Awareness*
    """)

if __name__ == "__main__":
    main()
