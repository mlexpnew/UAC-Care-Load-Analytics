import pandas as pd

def create_features(df):

    df = df.copy()

    # Total System Load
    df["Total_System_Load"] = (
        df["Children in CBP custody"]
        + df["Children in HHS Care"]
    )

    # Net Daily Intake
    df["Net_Daily_Intake"] = (
        df["Children transferred out of CBP custody"]
        - df["Children discharged from HHS Care"]
    )

    # Growth Rate
    df["Load_Growth_Rate"] = (
        df["Total_System_Load"]
        .pct_change()
        * 100
    )

    # Backlog
    df["Backlog"] = (
        df["Net_Daily_Intake"]
        .cumsum()
    )

    # Rolling Averages
    df["Load_7D"] = (
        df["Total_System_Load"]
        .rolling(7)
        .mean()
    )

    df["Load_14D"] = (
        df["Total_System_Load"]
        .rolling(14)
        .mean()
    )

    return df