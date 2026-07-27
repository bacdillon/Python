# Simple Linear Regression – Ice Cream Revenue Prediction
A beginner Machine Learning project that demonstrates how Simple Linear Regression can be used to predict ice cream revenue based on temperature using Python and Scikit-learn.

# Project Overview
This project builds a Simple Linear Regression model to predict the daily revenue of an ice cream stand using historical temperature data.
The notebook demonstrates the complete machine learning workflow, including:<br>
•	Data loading<br>
•	Exploratory Data Analysis (EDA)<br>
•	Data visualization<br>
•	Data preprocessing<br>
•	Model training<br>
•	Model prediction<br>
•	Regression visualization<br>
•	Future revenue prediction
<br><br>
The project illustrates how machine learning can help businesses forecast sales and support data-driven decision making.

# Business Problem
An ice cream shop owner wants to estimate daily revenue based on weather forecasts.
Questions include:<br>
•	How much revenue can be expected when the temperature reaches 30°C?<br>
•	Does temperature significantly influence sales?<br>
•	Can future weather forecasts improve inventory planning?<br>
•	How should staffing levels be adjusted during hot weather?<br><br>
Instead of relying on intuition, historical sales data is used to build a predictive machine learning model.

# Project Objectives
•	Learn the fundamentals of Simple Linear Regression<br>
•	Explore the relationship between temperature and revenue<br>
•	Visualize the dataset using statistical plots<br>
•	Train a regression model using Scikit-learn<br>
•	Interpret regression coefficients<br>
•	Predict future revenue<br>
•	Evaluate the regression model visually<br>

# Dataset
The dataset contains two variables.<br>
Temperature (°C) - Daily outdoor temperature<br>
Revenue ($) -	Ice cream stand daily revenue<br>

The objective is to predict Revenue from Temperature.

# Technologies Used
•	Python 3
•	Pandas
•	NumPy
•	Matplotlib
•	Seaborn
•	Scikit-learn
•	Jupyter Notebook

# Exploratory Data Analysis (EDA)
The notebook explores the dataset using:<br>
•	head()
•	tail()
•	describe()
•	info()

Visualization techniques include:
•	Scatter Plot
•	Joint Plot
•	Pair Plot
•	Linear Regression Plot

These visualizations reveal a strong positive linear relationship between temperature and revenue.

# Machine Learning Workflow
The notebook follows the standard supervised learning workflow.
1.	Import required libraries
2.	Load the dataset
3.	Explore and visualize the data
4.	Define feature (X) and target (y)
5.	Split the dataset into training and testing sets
6.	Train a Simple Linear Regression model
7.	Display the learned regression coefficients
8.	Predict revenue using the testing dataset
9.	Visualize the regression line
10.	Predict revenue for new temperature values

# Regression Model
The Linear Regression model learns the equation:<br>
Revenue = (Slope × Temperature) + Intercept <br><br>
Where:<br>
•	Slope (m) represents the increase in revenue for every 1°C rise in temperature.<br>
•	Intercept (b) represents the estimated revenue when the temperature is 0°C.

# Model Prediction
Example prediction for a new temperature:
import pandas as pd

new_temperature = pd.DataFrame({
    'Temperature': [30]
})

predicted_revenue = regressor.predict(new_temperature)

print(predicted_revenue)
Example Output
Predicted Revenue: $685.32
(Actual value depends on the trained model.)

# Key Concepts Covered <br>
•	Machine Learning <br>
•	Supervised Learning <br>
•	Regression Analysis <br>
•	Simple Linear Regression <br>
•	Exploratory Data Analysis (EDA) <br>
•	Data Visualization <br>
•	Feature Selection <br>
•	Train-Test Split <br>
•	Model Training <br>
•	Prediction <br>
•	Regression Coefficients <br>
•	Business Forecasting <br>

# Learning Outcomes
•	Load datasets with Pandas<br>
•	Perform exploratory data analysis<br>
•	Visualize relationships between variables<br>
•	Build a Simple Linear Regression model<br>
•	Train a machine learning model using Scikit-learn<br>
•	Interpret model coefficients<br>
•	Predict new values<br>
•	Visualize regression results<br>
•	Apply machine learning to solve business problems<br>

# Business Value
This project demonstrates how machine learning can support business decisions by:
•	Forecasting daily sales
•	Planning inventory
•	Optimizing staffing levels
•	Understanding customer purchasing behavior
•	Supporting data-driven decision making

# Future Enhancements
Possible improvements include:
•	Calculate MAE, MSE, RMSE, and R² Score
•	Add model evaluation metrics
•	Perform residual analysis
•	Compare multiple regression algorithms
•	Extend to Multiple Linear Regression
•	Build a Streamlit web application
•	Deploy the model using Flask or FastAPI

# Acknowledgements
This project was developed as part of learning Machine Learning with Python and Scikit-learn, demonstrating the end-to-end workflow of building a predictive regression model using business data.
