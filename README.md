# Predict Vietnam House Price

An end-to-end **machine learning project** that predicts real estate prices in Vietnam from listing data (area, location, legal status, etc.), enriched with province-level population and regional statistics. The project covers the full pipeline — data collection, cleaning, exploratory data analysis (EDA), feature engineering, and model training — implemented in a single Jupyter notebook (`main.ipynb`).

> **Disclaimer:** This is an academic course project. Predictions are for learning/demonstration purposes and should not be used for real financial decisions.

## Overview

The goal is to estimate the selling price of a property based on its physical attributes and location. Raw listing data alone has weak predictive power for price, so the project augments it with external socio-economic data (population, population density, geographic region) to capture location-driven price effects.

Pipeline:

```text
Raw data (Kaggle)
       |
       v
Data cleaning
       |
       v
Enrichment: population + population density (population.py)
            province -> region mapping (region.py)
       |
       v
Exploratory Data Analysis
       |
       v
Feature Engineering
       |
       v
Model training & tuning (GridSearchCV)
(Linear Regression, Extra Trees Regressor)
       |
       v
Evaluation (R2, MSE, RMSE)
       |
       v
Flask API + web form
(deployed on AWS)
```

## Dataset

- **Source:** [Vietnam Housing Dataset 2024 (Kaggle)](https://www.kaggle.com/datasets/nguyentiennhan/vietnam-housing-dataset-2024)
- **Size:** 30,229 rows x 12 columns (original data)

| Column | Description |
|---|---|
| `Address` | Full listing address (parsed down to province) |
| `Area` | Property area (m²) |
| `Frontage` | Frontage width (m) |
| `Access Road` | Access road width (m) |
| `House direction` / `Balcony direction` | Orientation |
| `Floors` / `Bedrooms` / `Bathrooms` | Discrete counts |
| `Legal status` | Legal/ownership status |
| `Furniture state` | Furnishing level (`Full` / `Basic` / `No furniture`) |
| `Price` | Target variable (**billions of VND**) |

- **Population by province**: [danso.info](https://danso.info/dan-so-cac-tinh-cua-viet-nam/)

**External data added:**
- Population and population density per province (`population.py`)
- Region grouping, e.g. Red River Delta, Mekong Delta, etc. (`region.py`)
- Province boundaries (`diaphanhuyen.geojson`) for geographic visualization

## Exploratory Data Analysis

- Price is close to normally distributed (low skewness), which is favorable for regression.
- `Area`, `Frontage`, and `Access Road` are right-skewed; log transformation was applied to reduce skew.
- Correlation of individual numeric features with price is generally weak-to-moderate: `bathrooms`, `bedrooms`, and `floors` are the strongest positive correlates; `average_area_by_density` is the only negative one; `project` and `frontage` have the smallest-magnitude positive correlations.
- Mutual information (normalized) shows area scores highest, followed by frontage and access_road, despite area having only weak linear correlation with price. This supports a non-linear relationship between property size and price.
- **ANOVA test** on categorical variables showed `province` and `region_grouped` have the strongest statistical association with price.
- Average house area tends to be smaller in higher-density provinces. The floors-vs-density and price-vs-density plots are similarly noisy, no clean monotonic trend.
- Hanoi and Ho Chi Minh City appear as two extreme outliers in the population distribution, skewing it left relative to the other provinces.

## Feature Engineering

- **Column selection before modeling:** `province`, `region`, and `region_grouped` are dropped from the feature set entirely. These signal is instead carried by `average_price_by_region_grouped`, `average_floors_by_density` and `population`, `population_density`.
- **Outlier removal:** Apply IQR method on `area`, `frontage`, `access_road` before splitting the data.
- **Train/test split:** 80/20 (`random_state=42`).
- **Missing-value imputation:** with scikit-learn's `IterativeImputer` (MICE - multivariate imputation by chained equations). Discrete columns (`bathrooms`, `bedrooms`, `floors`) are imputed with a `LinearRegression` estimator; continuous columns (`area`, `frontage`, `access_road`) are imputed with a `DecisionTreeRegressor` estimator.
- **Encoding:** `OneHotEncoder` for nominal categories, `OrdinalEncoder` for `furniture_state`, `StandardScaler` for numerical columns.

## Modeling & Results

| Model | R² | MSE | RMSE |
|---|---|---|---|
| Linear Regression | 0.393 | 2.909 | 1.706 |
| **Extra Trees Regressor** | **0.516** | **2.318** | **1.522** |

Extra Trees (a non-linear ensemble model) outperformed Linear Regression. 
Best hyperparameters found: `etr__max_depth`: 20, `etr__min_samples_leaf`: 4, `etr__min_samples_split`: 10, `etr__n_estimators`: 300.

## Project Structure

```text
Predict-Viet-Nam-House-Price/
│
├── main.ipynb               # Full pipeline: EDA, feature engineering, modeling
├── api_data.py              # Builds the province-level lookup table for the API
├── population.py            # Province population & density data
├── region.py                # Province -> region mapping
├── diaphanhuyen.geojson     # Vietnam administrative boundaries (for maps)
├── data/
│   ├── original_data.csv          # Raw data (Kaggle)
│   ├── new_data.csv               # Cleaned/enriched dataset
│   ├── population.csv             # population data
│   ├── province_region.csv        # province_region data
│   └── data_for_api.csv           # Output of api_data.py
├── images/
│   ├── demo_api.png
│   └── vietnammap.png
├── requirements.txt
└── README.md
```

## Technologies

- **Python**, **Jupyter Notebook**
- **pandas / numpy** — data manipulation
- **matplotlib / seaborn / plotly** — visualization
- **scikit-learn** — pipelines, encoding, Linear Regression, Extra Trees, `GridSearchCV`, `IterativeImputer`, metrics
- **scipy** — ANOVA, statistical tests
- **Flask + gunicorn** — model serving API
- **AWS Elastic Beanstalk** — deployment

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/tritantran04/Predict-Viet-Nam-House-Price.git
cd Predict-Viet-Nam-House-Price
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the notebook

Open and run `main.ipynb` top to bottom to reproduce data preparation, EDA, and model training. This regenerates `etr_model.pkl`.

## Limitations

- Model performance (R² ≈ 0.52) is moderate, price in this dataset has a largely non-linear and noisy relationship with the available features, and unobserved factors (exact street, building quality, market timing) are not captured.
- `house_direction` and `balcony_direction` were dropped entirely due to heavy missingness, discarding potentially useful information.
- The dataset only covers listings available on the source site at the time of collection and may not generalize to other periods or platforms.
- This is a course project/prototype, not a production-grade valuation tool.


