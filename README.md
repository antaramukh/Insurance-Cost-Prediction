# Insurance-Cost-Prediction

Heroku Link: https://insurance-cost-pred-heroku.herokuapp.com/

## Do you know what is Health Insurance?
Health insurance is a type of insurance product that specifically guarantees the health costs or care of the insurance members if they fall ill or have an accident.

In this project, we create a linear regression machine learning model to predict insurance charges using information such as beneficiary’s age, sex, BMI, no. of children, residential area and smoking habit. This kind of model is useful for insurance companies to determine the yearly insurance premium for a person. We will conduct an analysis of a health insurance data in the US. The dataset used can be found on [Kaggle](https://www.kaggle.com/mirichoi0218/insurance?select=insurance.csv). This dataset contains 1338 rows.

## Multiple Linear Regression

Multiple linear regression analysis is a linear relationship between two or more independent variables (X1, X2, X3, …, Xn) with the dependent variable (Y). This analysis is to determine the direction of the relationship between the independent variable and the dependent variable, whether each independent variable is positively or negatively related and to predict the value of the dependent variable if the value of the independent variable increases or decreases.

## Columns

**1. age:** age of primary beneficiary

**2. sex:** insurance contractor gender, female, male

**3. bmi:** Body mass index

**4. children:** Number of children covered by health insurance / Number of dependents

**5. smoker:** Smoking

**6.region:** the beneficiary's residential area in the US, northeast, southeast, southwest, northwest.

**7. charges:** Individual medical costs billed by health insurance

The aim of this project is to evaluate and investigate the feasibility. The machine learning algorithm used for predicting insurance cost is multiple linear regression and inference is provided on the features on which the insurance costs rely the most and which factors affect the insurance costs using concepts such as data visualization, data preprocessing, statistical learning, train-test split for model evaluation and making predictions using the trained model.

## Deployment

By using the Python package flask, we have created an interactive application where you can enter the values of your age, sex, BMI, no. of children, residential area and smoking habit to predict your insurance cost. The web application is written in **Python** using **Flask** along with model deployment on **Heroku.**
