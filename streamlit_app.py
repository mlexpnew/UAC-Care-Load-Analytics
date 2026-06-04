import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from src.feature_engineering import create_features
from src.kpi_calculator import calculate_kpis
from src.anomaly_detection import validate_data

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="UAC Care Load Analytics",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_csv(
    "data/uac_analytics_dataset.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

df = create_features(df)

kpis = calculate_kpis(df)

validation = validate_data(df)
# ==================================================
# SIDEBAR
# ==================================================

st.sidebar.title("📅 Filters")

start_date = st.sidebar.date_input(
    "Start Date",
    df["Date"].min()
)

end_date = st.sidebar.date_input(
    "End Date",
    df["Date"].max()
)

df = df[
    (df["Date"] >= pd.to_datetime(start_date))
    &
    (df["Date"] <= pd.to_datetime(end_date))
]

# ==================================================
# KPI CALCULATIONS
# ==================================================

latest_load = int(df["Total_System_Load"].iloc[-1])

avg_pressure = round(
    df["Net_Daily_Intake"].mean(),
    2
)

volatility = round(
    df["Total_System_Load"].std(),
    2
)

peak_load = int(
    df["Total_System_Load"].max()
)

current_backlog = int(
    abs(df["Backlog"].iloc[-1])
)

stress_pct = (
    latest_load / peak_load
) * 100

if stress_pct > 80:
    system_status = "🔴 High Stress"
elif stress_pct > 50:
    system_status = "🟡 Moderate Stress"
else:
    system_status = "🟢 Stable"

# ==================================================
# TITLE
# ==================================================

st.title(
    "📊 System Capacity & Care Load Analytics for Unaccompanied Children"
)

st.caption(
    "Healthcare Capacity Monitoring | U.S. Department of Health & Human Services"
)

st.divider()

# ==================================================
# KPI ROW
# ==================================================

c1, c2, c3, c4, c5 = st.columns(5)

c1.metric(
    "Children Under Care",
    f"{latest_load:,}"
)

c2.metric(
    "Net Intake Pressure",
    avg_pressure
)

c3.metric(
    "Volatility Index",
    volatility
)

c4.metric(
    "Peak Load",
    f"{peak_load:,}"
)

c5.metric(
    "System Status",
    system_status
)

st.divider()

# ==================================================
# TABS
# ==================================================

tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Overview",
    "🏥 CBP vs HHS",
    "⚠️ Pressure Analysis",
    "📋 Executive Summary"
])

# ==================================================
# TAB 1
# ==================================================

with tab1:

    st.subheader("Total System Load Trend")

    fig = px.line(
        df,
        x="Date",
        y="Total_System_Load",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Monthly Average Load")

    monthly = (
        df.set_index("Date")
          .resample("ME")
          .agg({
              "Total_System_Load":"mean"
          })
          .reset_index()
    )

    fig = px.bar(
        monthly,
        x="Date",
        y="Total_System_Load",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==================================================
# TAB 2
# ==================================================

with tab2:

    st.subheader("CBP vs HHS Care Load")

    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["Children in CBP custody"],
            name="CBP Custody"
        )
    )

    fig.add_trace(
        go.Scatter(
            x=df["Date"],
            y=df["Children in HHS Care"],
            name="HHS Care"
        )
    )

    fig.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==================================================
# TAB 3
# ==================================================

with tab3:

    st.subheader("Net Intake Pressure")

    fig = px.line(
        df,
        x="Date",
        y="Net_Daily_Intake",
        template="plotly_dark"
    )

    fig.add_hline(
        y=0,
        line_dash="dash"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.subheader("Backlog Trend")

    df["Backlog_Pressure"] = (
        df["Backlog"]
        -
        df["Backlog"].min()
    )

    fig = px.area(
        df,
        x="Date",
        y="Backlog_Pressure",
        template="plotly_dark"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==================================================
# TAB 4
# ==================================================

with tab4:

    st.subheader("Executive Summary")

    peak_date = df.loc[
        df["Total_System_Load"].idxmax(),
        "Date"
    ]

    st.success(
        f"""
        Peak care load occurred on
        {peak_date.strftime('%d %b %Y')}
        with {peak_load:,} children
        under care.
        """
    )

    st.info(
        f"""
        Current system load is {latest_load:,}
        children.

        Average net intake pressure is
        {avg_pressure} children per day.

        System volatility index is
        {volatility}, indicating variability
        in care demand over time.
        """
    )

    st.subheader("Policy Recommendations")

    st.markdown("""
    ### 1. Increase Staffing During Peak Demand
    Monitor recurring high-load periods and
    allocate additional healthcare resources.

    ### 2. Improve Sponsor Processing
    Faster reunification reduces care burden
    and shelter congestion.

    ### 3. Monitor Intake–Discharge Balance
    Persistent positive net intake may indicate
    growing pressure on the care system.

    ### 4. Expand Capacity Planning
    Use forecasting models to anticipate future
    surges and avoid overcrowding.
    """)
csv = df.to_csv(index=False)

st.download_button(
    label="📥 Download Analytics Dataset",
    data=csv,
    file_name="uac_analytics_dataset.csv",
    mime="text/csv"
)
# ==================================================
# FOOTER
# ==================================================

st.divider()

st.caption(
    "Unified Mentor Project | System Capacity & Care Load Analytics for Unaccompanied Children"
)
