import math
import pandas as pd

# ---------- Settings ----------
input_file = "/content/drive/MyDrive/Colab Notebooks/bcd_survey/BC_Scopus_WOS.csv"
output_file = "/content/drive/MyDrive/Colab Notebooks/bcd_survey/independent_audit_sample.csv"

category_column = "status"  # Change if your column has a different name
passed_sample_size = 28
screening_out_fraction = 0.10
max_screening_out_per_category = 20
random_seed = 2026

# Categories to include in the screening-decision audit.
# D and IR are omitted because they concern preprocessing.
screening_out_categories = ["ST", "SA", "SF", "NA"]

# Accept either the codes or the labels shown in your table.
category_map = {
    "DUPLICATES": "D",
    "INVALID RECORD": "IR",
    "SCREENED OUT BY TITLE": "ST",
    "SCREENED OUT BY ABSTRACT": "SA",
    "SCREENED OUT BY FULL TEXT": "SF",
    "PASSED": "P",
    "NOT AVAILABLE": "NA",
}

# ---------- Load and prepare data ----------
df = pd.read_csv(input_file)

if category_column not in df.columns:
    raise ValueError(
        f"Column '{category_column}' was not found. "
        f"Available columns: {list(df.columns)}"
    )

def normalize_category(value):
    if pd.isna(value):
        return None

    value = str(value).strip().upper()
    return category_map.get(value, value)

df["_category_code"] = df[category_column].apply(normalize_category)
df = df[df["_category_code"].notna()].copy()

# ---------- Select records ----------
selections = []

# Select the passed studies for independent eligibility and data-extraction checks.
passed = df[df["_category_code"] == "P"]

if not passed.empty:
    n_passed = min(passed_sample_size, len(passed))
    selections.append(
        passed.sample(n=n_passed, random_state=random_seed)
    )

# Select records screened out at each stage for eligibility-decision checks.
for i, category in enumerate(screening_out_categories, start=1):
    category_records = df[df["_category_code"] == category]

    if category_records.empty:
        continue

    n_to_select = math.ceil(len(category_records) * screening_out_fraction)
    n_to_select = max(1, n_to_select)
    n_to_select = min(n_to_select, max_screening_out_per_category)
    n_to_select = min(n_to_select, len(category_records))

    selections.append(
        category_records.sample(
            n=n_to_select,
            random_state=random_seed + i
        )
    )

if not selections:
    raise ValueError("No records were selected. Check the category values.")

audit_sample = pd.concat(selections).drop_duplicates()

# Remove the helper column before saving.
audit_sample = audit_sample.drop(columns=["_category_code"])
audit_sample.to_csv(output_file, index=False)

print(f"Saved audit sample to: {output_file}")
print("\nSelected records by category:")
print(
    audit_sample[category_column]
    .value_counts(dropna=False)
    .to_string()
)