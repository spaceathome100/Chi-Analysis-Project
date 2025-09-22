import pandas as pd
from scipy.stats import chi2_contingency
from pandasgui import show

# ---------------- 1️⃣ Load CSV ----------------
file_path = "square-analysis.csv"  # Replace with your CSV file path
df = pd.read_csv(file_path)

# ---------------- 2️⃣ Clean column names ----------------
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('[^a-z0-9_]', '', regex=True)

# ---------------- 3️⃣ Define the selected question pairs ----------------
selected_pairs = [
    ('1_in_your_opinion_what_is_the_primary_reason_companies_pursue_mergers_or_acquisitions',
     '2_how_often_do_you_think_promised_synergies_are_fully_realized_postmerger'),

    ('6what_in_your_opinion_is_the_biggest_risk_to_achieving_postmerger_synergies',
     '7do_you_think_integration_costs_are_usually_underreported_in_investor_presentations'),

    ('5__which_valuation_method_do_you_consider_most_prone_to_manipulation_during_ma',
     '12__have_you_ever_seen_an_acquisition_fail_primarily_due_to_valuation_overreach'),

    ('16_would_a_colorcoded_risk_assessment_model_rag_be_useful_for_identifying_postmerger_synergy_shortfalls',
     '20_lastly_do_you_feel_that_this_research_topic_is_practically_useful_for_investors_analysts_and_deal_teams'),

    ('4how_many_years_postmerger_do_you_believe_are_needed_to_fairly_assess_synergy_realization',
     '18__whats_your_view_on_using_a_3year_performance_window_to_assess_actual_synergy_realization')
]

# ---------------- 4️⃣ Chi-Square test function ----------------
def chi_square_test(col1, col2):
    try:
        table = pd.crosstab(df[col1], df[col2])
        chi2, p, dof, expected = chi2_contingency(table)
        return chi2, p
    except Exception as e:
        print(f"Error for {col1} vs {col2}: {e}")
        return None, None

# ---------------- 5️⃣ Compute Chi-Square for each pair ----------------
results = []
for col1, col2 in selected_pairs:
    chi2, p = chi_square_test(col1, col2)
    results.append({
        'Question 1': col1,
        'Question 2': col2,
        'Chi2': chi2,
        'p-value': p,
        'Significant (p<0.05)': 'Yes' if p is not None and p < 0.05 else 'No'
    })

results_df = pd.DataFrame(results)

# ---------------- 6️⃣ Optional: Save to CSV ----------------
results_df.to_csv("chi_square_selected_pairs.csv", index=False)
print("Chi-Square results saved to 'chi_square_selected_pairs.csv'")

# ---------------- 7️⃣ Show results in a beautiful interactive GUI ----------------
show(results_df)
