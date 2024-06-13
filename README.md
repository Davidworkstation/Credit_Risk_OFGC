# Credit Risk: One Factor Guassian Copula Approach
![Alt Text](Dashboard_Preview.png)

Vasicek's one-factor Gaussian copula is a statistical model used in the Basel III framework for calculating the Conditional Value at Risk (CVaR) of a portfolio of financial assets. It combines the Vasicek interest rate model, which describes the dynamics of interest rates over time, with a Gaussian copula, which captures the dependence structure between the different assets in the portfolio.

In this model, the Vasicek interest rate model is employed to simulate the movement of interest rates, while the Gaussian copula is used to model the correlation between the individual asset returns. By integrating these two components, the model can estimate the joint distribution of asset returns and hence quantify the risk associated with the portfolio.

This comes with the assumption of a 'homogenous' portfolio, or that a portfolio 1. contains similar assets (for example, with similar credit scores) and 2. have assets with the same default probability. 

CVaR, also known as expected shortfall, measures the potential losses of a portfolio beyond a certain threshold, and it's a key metric for assessing the risk of a portfolio under extreme market conditions. The Vasicek's one-factor Gaussian copula approach helps financial institutions comply with regulatory requirements by providing a coherent framework for estimating CVaR and managing their risk exposure effectively.

## Installation
To install the project dependencies, run:
pip install -r requirements.txt

## Usage
Basic instructions on how to use the project:

On your computer, navigate to the repository's folder and type the following in the terminal:
streamlit run polyregress.py

note: depending on your python setup, you may have to include 'python' or 'python3' in front of the command.

## Project Structure
Overview of the project's structure:

project-root/

├── py/ - OFGC_Dashboard - main model, contains one factor gaussian copula for credit risk in a python streamlit dashboard.

├── requirements.txt - Project dependencies.

├── .gitatributes - Text handling.

└── README.md - This file.

## References
"Probability of Loss on Loan Portfolio" Oldrich Vasicek, 1987
Basel iii https://www.bis.org/bcbs/basel3.htm
"The One Factor Gaussian Copula Model - Too Simplistic?" Gunter Meissner, 2019 https://www.risk.net/correlation-risk-modelling-and-management-2nd-edition/6446341/the-one-factor-gaussian-copula-model-too-simplistic


## Contact Information
For questions, please contact David Bannister at (https://www.linkedin.com/in/david-bannister-230a67191/).
