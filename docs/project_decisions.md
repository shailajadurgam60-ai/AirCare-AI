# AirCare AI – Project Decision Log

This document records the important technical decisions made during the development of the project, along with the reasoning behind each choice.

---

## Decision 01 – Selected Dataset

**Decision**

Selected the "Air Quality Data in India (2015–2020)" dataset from Kaggle.

**Reason**

- Contains approximately 29,500 observations.
- Covers 26 Indian cities.
- Includes pollutant concentrations such as PM2.5, PM10, NO₂, SO₂, CO, O₃, NH₃, Benzene, Toluene, and Xylene.
- Provides both numerical AQI and categorical AQI Bucket.
- Covers over five years of historical observations.

**Impact**

- Suitable for supervised machine learning.
- Supports both regression (AQI prediction) and classification (AQI Bucket prediction).
- Can be integrated with live AQI APIs during deployment.

---

## Decision 02 – Target Variable

**Decision**

Use **AQI (Air Quality Index)** as the primary machine learning target.

**Reason**

- AQI is available directly in the dataset.
- Predicting AQI is based on real observations rather than an artificially created label.
- AQI can later be converted into health risk levels and personalized recommendations.

**Impact**

- Produces a technically sound machine learning model.
- Separates prediction from the recommendation engine.

---

## Decision 03 – Remove Xylene

**Decision**

Drop the `Xylene` column.

**Reason**

- Approximately 61.3% of the values are missing.
- Imputing more than half of the column would introduce a large amount of artificial data.
- Other pollutant features provide sufficient environmental information.

**Impact**

- Improves overall data quality.
- Reduces unnecessary complexity during preprocessing.

---

## Decision 04 – Remove Rows with Missing AQI

**Decision**

Remove observations where the `AQI` value is missing.

**Reason**

- AQI is the prediction target.
- Supervised learning requires known target values.
- These rows cannot contribute to model training.

**Impact**

- Ensures all training samples contain valid labels.
- Reduces dataset size while maintaining data integrity.

---

## Decision 05 – Delay Missing Value Imputation

**Decision**

Do not impute pollutant values immediately.

**Reason**

- Appropriate imputation depends on the underlying data distribution.
- Exploratory Data Analysis (EDA) will determine whether mean, median, or another strategy is most appropriate.
- Avoids making assumptions before understanding the data.

**Impact**

- Results in more informed preprocessing decisions.
- Maintains a transparent and reproducible workflow.

---
## Decision 06 – Missing Value Imputation Strategy

**Decision**

Use **median imputation** for numerical pollutant features.

**Reason**

Histogram analysis showed that the pollutant variables are heavily right-skewed and contain extreme values. The median is less sensitive to outliers than the mean and therefore provides a more robust estimate for missing values.

**Impact**

- Preserves the overall distribution of the data.
- Reduces the influence of extreme pollution events during imputation.
- Produces a more reliable dataset for machine learning.
## Decision 07 – Save Processed Dataset Separately

**Decision**

Save the cleaned dataset as `data/processed/clean_air_quality.csv`.

**Reason**

- Preserve the original raw dataset.
- Ensure preprocessing is reproducible.
- Provide a clean input for EDA and model training.

**Impact**

- Creates a clear separation between raw and processed data.
- Improves project organization and reproducibility.

## Decision 08 – Retain Correlated Pollutant Features

**Decision**

Retain all pollutant features despite high correlations between some variables.

**Reason**

- Correlation analysis identified strong relationships between NO and NOx, and between Benzene and Toluene.
- The planned baseline models (Random Forest and other tree-based algorithms) are generally robust to multicollinearity.
- Removing correlated features at this stage could discard useful predictive information.

**Impact**

- Preserves potentially valuable environmental information.
- Simplifies the initial modeling process while allowing future feature selection if needed.