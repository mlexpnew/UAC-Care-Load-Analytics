def validate_data(df):

    results = {}

    # Missing Values
    results["missing_values"] = (
        df.isnull().sum().sum()
    )

    # Duplicate Dates
    results["duplicate_dates"] = (
        df["Date"].duplicated().sum()
    )

    # Transfer Validation
    invalid_transfer = df[
        df["Children transferred out of CBP custody"]
        >
        df["Children in CBP custody"]
    ]

    results["invalid_transfers"] = (
        len(invalid_transfer)
    )

    # Discharge Validation
    invalid_discharge = df[
        df["Children discharged from HHS Care"]
        >
        df["Children in HHS Care"]
    ]

    results["invalid_discharges"] = (
        len(invalid_discharge)
    )

    return results