import streamlit as st
from mlflow.tracking import MlflowClient

# Analyze MLflow runs to choose the best
def analyze_mlflow_runs():
    client = MlflowClient()
    experiment_name = "movie_recommendation"  # Update this to match your experiment name
    experiment = client.get_experiment_by_name(experiment_name)

    if experiment is None:
        st.error(f"Experiment '{experiment_name}' does not exist.")
        return None

    experiment_id = experiment.experiment_id
    runs = client.search_runs(
        experiment_ids=[experiment_id],
        filter_string="",
        order_by=["metrics.max_lift DESC"],
        max_results=50
    )

    # Display results
    st.write("### Best MLflow Runs:")
    for run in runs:
        st.write(f"- **Run ID**: {run.info.run_id}")
        st.write(f"  - Min Support: {run.data.params.get('min_support', 'N/A')}")
        st.write(f"  - Metric: {run.data.params.get('metric', 'N/A')}")
        st.write(f"  - Min Threshold: {run.data.params.get('min_threshold', 'N/A')}")
        st.write(f"  - Max Lift: {run.data.metrics.get('max_lift', 'N/A')}")
        st.write(f"  - Number of Rules: {run.data.metrics.get('num_rules', 'N/A')}")
        st.write("---")

# Streamlit UI setup
st.title("🎥 MLflow Runs Analysis")
st.write("Analyze the best runs from your MLflow experiments.")

# Add button to analyze MLflow runs
if st.button("Analyze MLflow Runs"):
    analyze_mlflow_runs()
