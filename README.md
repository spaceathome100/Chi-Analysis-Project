# Chi-Square Analysis of Survey Data

This repository contains a Python project to perform **Chi-Square tests** on selected survey question pairs. It helps identify statistical associations between different survey responses related to mergers and acquisitions.

---

## 📂 Project Structure
├── square-analysis.csv # Input survey CSV file
  
  ├── chi_square_analysis.py # Python script performing Chi-Square tests
  
  ├── chi_square_selected_pairs.csv # Output CSV with results
  
  └── README.md # Project documentation

---

## 📝 Overview

The project workflow includes:

1. **Loading the survey CSV file**.
2. **Cleaning the column names** for consistency.
3. **Defining selected question pairs** for Chi-Square testing.
4. **Performing Chi-Square tests** to check for statistical significance.
5. **Saving the results** into a CSV file.
6. **Interactive visualization** using `pandasgui`.

---

## ⚡ Key Features

- Clean and standardized survey data
- Automated Chi-Square testing for multiple question pairs
- Identification of significant associations (`p < 0.05`)
- Interactive GUI for exploring results
- CSV export for easy reporting

---

## 🛠️ How to Run

1. Install dependencies:
bash: ```pip install pandas scipy pandasgui!```

2. Place your CSV file in the project folder.

3. Run the Python script:
bash: ```python chi_square_analysis.py```

5. View results in an interactive GUI and/or check chi_square_selected_pairs.csv.

⚖️ Interpretation:
- Chi2: Test statistic measuring the association between two categorical variables.
- p-value: Probability of observing the data if the null hypothesis is true.
- Significant (p < 0.05): "Yes" indicates a statistically significant association between the question pair.

 Output:
 <img width="1453" height="315" alt="image" src="https://github.com/user-attachments/assets/88165e15-56e5-4f98-b75d-b8b862279749" />

