# Heart Attack EDA & Prediction (90% Accuracy)

This project demonstrates exploratory data analysis (EDA) and prediction modeling on a heart attack dataset to identify risk factors and predict the likelihood of a heart attack with an impressive accuracy of 90%. The notebook is hosted on Kaggle and serves as a comprehensive guide to understanding the dataset and building machine learning models for medical predictions.

## Dataset Description

The dataset contains medical features and labels indicating whether a patient has experienced a heart attack. The features include:
- **Age**: Age of the patient
- **Sex**: Gender (1 = Male, 0 = Female)
- **Chest Pain Type (cp)**: 0-3 categories
- **Resting Blood Pressure (trestbps)**: Measured in mm Hg
- **Cholesterol Level (chol)**: Serum cholesterol in mg/dl
- **Fasting Blood Sugar (fbs)**: >120 mg/dl (1 = True, 0 = False)
- **Resting ECG Results (restecg)**: 0-2 categories
- **Max Heart Rate Achieved (thalach)**: Numerical value
- **Exercise-Induced Angina (exang)**: 1 = Yes, 0 = No
- **Old Peak (oldpeak)**: ST depression induced by exercise
- **Slope of ST Segment (slope)**: 0-2 categories
- **Number of Major Vessels Colored by Fluoroscopy (ca)**: 0-4
- **Thalassemia (thal)**: 1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect

## Exploratory Data Analysis (EDA)

The EDA involves:
1. **Feature Analysis**: Examining distributions and relationships with the target variable.
2. **Correlations**: Identifying significant features affecting the likelihood of a heart attack.
3. **Visualizations**: Using histograms, bar charts, and heatmaps to explore data trends.

## Prediction Models

Various machine learning models were used to predict heart attack risks:
- **Logistic Regression**
- **Decision Trees**
- **Random Forest**
- **Support Vector Machines (SVM)**

The workflow involves:
1. **Data Preprocessing**: Handling missing values, scaling numerical features, and encoding categorical data.
2. **Model Training**: Training models using 80% of the dataset.
3. **Model Evaluation**: Measuring performance using accuracy, precision, recall, and F1 score.

## Key Insights

- The logistic regression model achieved the highest accuracy of 90%.
- Features such as age, chest pain type, and maximum heart rate significantly impact predictions.
- The dataset is relatively balanced, ensuring fair model evaluation.

## Additional Features

We have extended the functionality by integrating a user-friendly interface with the following features:
1. **Heart Attack Risk Prediction**: The interface allows users to input medical data and predict the likelihood of a heart attack.
2. **Interactive Map and Hospital Listing**: A single button opens a map interface that:
   - Displays the user’s exact location.
   - Lists nearby hospitals within a 15 km radius.
   - Marks the locations of these hospitals on the map for easy navigation.

## How to Run

1. Access the notebook on Kaggle: [Heart Attack EDA & Prediction Notebook](https://www.kaggle.com/code/namanmanchanda/heart-attack-eda-prediction-90-accuracy/notebook).
2. Ensure dependencies like `pandas`, `numpy`, and `scikit-learn` are installed.
3. Download the dataset from Kaggle.
4. Execute cells sequentially to reproduce results.

## Applications

This project can serve as:
- A foundational guide for beginners in EDA and medical data analysis.
- A practical demonstration of machine learning's role in healthcare.
- A benchmark for building predictive models for heart disease.
- A user-friendly tool for individuals to assess risk and locate nearby hospitals in emergencies.

## Acknowledgments

Special thanks to the Kaggle community and contributors for making the dataset and resources available for public use. This project aligns with efforts to leverage AI and data analysis for improving healthcare outcomes.
