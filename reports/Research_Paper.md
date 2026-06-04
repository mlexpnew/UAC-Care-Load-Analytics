# System Capacity & Care Load Analytics for Unaccompanied Children

## 1. Introduction

The Unaccompanied Alien Children (UAC) Program is a federally mandated initiative managed by the U.S. Department of Health and Human Services (HHS). The program provides shelter, medical care, psychological support, and reunification services for children transferred from U.S. Customs and Border Protection (CBP).

This study aims to develop a healthcare analytics framework for monitoring system capacity, evaluating care load trends, identifying capacity stress periods, and supporting data-driven decision-making.

---

## 2. Objectives

### Primary Objectives

* Quantify daily and cumulative care load.
* Evaluate balance between inflow and outflow.
* Identify capacity stress and relief periods.

### Secondary Objectives

* Support staffing and shelter planning.
* Improve situational awareness.
* Enable evidence-based policy evaluation.

---

## 3. Dataset Description

The dataset contains daily operational records from 2023–2025.

| Variable                                       | Description            |
| ---------------------------------------------- | ---------------------- |
| Date                                           | Reporting date         |
| Children apprehended and placed in CBP custody | Daily intake volume    |
| Children in CBP custody                        | Active CBP care load   |
| Children transferred out of CBP custody        | Transfers into HHS     |
| Children in HHS Care                           | Active HHS care load   |
| Children discharged from HHS Care              | Sponsor reunifications |

---

## 4. Data Quality Assessment

The following validation checks were performed:

* Missing value analysis
* Duplicate date detection
* Chronological ordering validation
* Transfer ≤ CBP custody validation
* Discharge ≤ HHS care validation

No critical data quality issues affecting analysis were identified.

---

## 5. Feature Engineering

Several healthcare analytics metrics were derived:

### Total System Load

Total System Load = CBP Custody + HHS Care

### Net Daily Intake

Net Daily Intake = Transfers − Discharges

### Care Load Growth Rate

Measures daily percentage change in system load.

### Backlog Indicator

Cumulative net intake over time.

### Discharge Offset Ratio

Discharges divided by transfers.

---

## 6. Exploratory Data Analysis

### System Load Trends

Analysis revealed fluctuations in total care responsibility throughout the study period. Periods of increasing load indicate growing resource demand, while declines suggest successful capacity relief.

### CBP vs HHS Load

Comparison of CBP and HHS populations highlighted the distribution of care responsibility across the pipeline.

### Net Intake Pressure

Positive net intake periods indicate more children entering care than exiting, creating additional pressure on available resources.

### Backlog Accumulation

Persistent positive intake pressure contributes to backlog growth and increased shelter utilization.

---

## 7. Capacity Stress Analysis

Rolling averages and trend analysis were used to identify prolonged periods of elevated system demand.

Stress periods were defined using high-percentile system load thresholds.

These periods indicate increased risk of:

* Shelter overcrowding
* Staffing shortages
* Delayed reunification processes
* Increased operational costs

---

## 8. Key Findings

* Peak care-load periods were successfully identified.
* System load exhibited measurable variability over time.
* Net intake pressure directly influenced backlog accumulation.
* HHS facilities absorbed the majority of long-term care responsibility.

---

## 9. Recommendations

### Recommendation 1

Increase staffing and healthcare resources during recurring peak periods.

### Recommendation 2

Improve sponsor verification and reunification processing efficiency.

### Recommendation 3

Implement continuous capacity monitoring dashboards.

### Recommendation 4

Utilize forecasting models to proactively plan resource allocation.

---

## 10. Conclusion

This project demonstrates how healthcare analytics can transform operational data into actionable capacity insights.

The resulting dashboard and analytical framework support proactive management of the UAC care system and provide policymakers with a data-driven approach to monitoring healthcare capacity, workload sustainability, and humanitarian response effectiveness.
