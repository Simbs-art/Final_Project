# Employee_Absenteeism_Prediction
Predicting and Understanding Employee Absenteeism Using Machine Learning.
## Overview
This project aims to analyze and predict employee absenteeism using a real-world HR dataset from a courier company. Through exploratory data analysis, feature engineering, and machine learning modeling, we identify key patterns and risk factors associated with absentee behavior. The goal is to support HR teams in proactive workforce planning, reducing productivity losses, and developing data-informed policies to manage absenteeism more effectively.

## Business Goal
To develop a predictive model that estimates the number of hours an employee is likely to be absent based on various personal, workplace, and health-related features.

This helps organizations:
- Forecast absentee-related disruptions
- Identify high-risk absenteeism profiles
- Improve HR policy and operational planning

## Key Business Questions
1. Can we predict how many hours an employee will be absent based on their work and health profile? (Regression)
2. Which factors most strongly influence employee absenteeism?
3. Are there patterns in absenteeism by day of week, season, or distance from work?
4. Do health-related reasons (e.g., diseases, accidents) explain most absences?
5. Can we classify employees into low, medium, and high absenteeism risk categories?
6. Does absenteeism vary significantly across departments, education levels, or job roles?
7. Are certain employees abusing the system (e.g., frequent short absences)?

## Dataset Overview
- **Source**: Kaggle
- **Records**: 740 rows × 21 columns
- **Target Variable**: `Absenteeism time in hours` (continuous)
- **Features**: Age, distance to work, education, workload, BMI, reason for absence, etc.

### Selected Columns:
| Column                     | Description                                            |
|----------------------------|--------------------------------------------------------|
| ID                         | Unique employee ID                                     |
| Reason for absence         | Coded reason (medical, personal, etc.)                |
| Month of absence           | Month number (1–12)                                   |
| Day of the week            | Workday (2 = Monday to 6 = Friday)                    |
| Distance from Residence    | Commute distance (km)                                 |
| Work load Average/day      | Average workload in minutes                           |
| Disciplinary failure       | 0 = No, 1 = Yes                                        |
| Education                  | 1 = HS, 2 = Graduate, 3 = PG, 4 = PhD                 |
| Social smoker/drinker      | Binary indicator                                      |
| BMI, Age, Service time     | Health and tenure indicators                          |
| **Absenteeism time in hours** | Target variable                                      |

