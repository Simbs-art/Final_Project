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
- **Target Variable**: Absenteeism time in hours
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

## Project Workflow

### 1. Data Preparation
- Converted `.xls` to `.csv`
- Cleaned and handled missing values
- Encoded categorical variables
- Scaled numerical features

### 2. Exploratory Data Analysis (EDA)
- Univariate & bivariate plots
- Correlation matrix
- Outlier detection
- Insights around seasonality, distance, health, workload

### 3. Feature Engineering
- Grouped absence reasons
- Created custom categories (e.g., absenteeism risk)
- Transformed skewed features

### 4. Modeling
- Regression Model:
  - XGBoost Regressor
- Classification Models:
  - Random Forest
  - Logistic Regression
  - XGBoost

### 5. Evaluation Metrics
- MAE, RMSE, R² Score for regression
- Confusion matrix, Precision, Recall, F1-Score for classification
- Feature importance

## Key Insights
- Health-related absences (e.g., medical visits), and Transportation expense are the most frequent.
- Distance to work and workload are positively correlated with absentee hours.
- Social drinkers and smokers tend to be absent longer than non-drinkers/smokers.
- Employees with disciplinary failures have above-average absence time.

## Tools & Technologies
- Python (Pandas, NumPy, Scikit-learn, Seaborn, Matplotlib)
- Jupyter Notebook
- Streamlit
- Tableau
- Git for version control

## Acknowledgements
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Absenteeism+at+work)
- Kaggle community contributors

## Contact
**Simbiat Titilope Musa**  
HR & Data Science and Machine Learning Enthusiast  
Lisbon, Portugal  
musasimbiat@gmail.com 
LinkedIn: https://www.linkedin.com/in/simbiat-adetokunbo-musa-acipm-hrpl-297487150?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=ios_app
