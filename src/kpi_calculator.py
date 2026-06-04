def calculate_kpis(df):

    latest_load = int(
        df["Total_System_Load"].iloc[-1]
    )

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

    backlog = int(
        df["Backlog"].iloc[-1]
    )

    return {
        "latest_load": latest_load,
        "avg_pressure": avg_pressure,
        "volatility": volatility,
        "peak_load": peak_load,
        "backlog": backlog
    }