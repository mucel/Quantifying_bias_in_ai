import json
from collections import Counter, defaultdict

# Categories
age_categories = ["20", "30", "40", "50", "60", "70", "80", "90", "100"]
race_categories = ["white", "hispanic", "asian", "native american", "black"]
gender_categories = ["male", "female", "non-binary"]


# Load data
def read_jsonl(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # Read the lines from the file
        return [json.loads(line) for line in lines]


data = read_jsonl("explicit.jsonl")

# Single category counts
single_counts = defaultdict(int)
for item in data:
    if item["decision"] == 1:
        age_str = str(item["age"])
        single_counts["age_" + age_str] += 1
        single_counts["race_" + item["race"]] += 1
        single_counts["gender_" + item["gender"]] += 1

# Combination counts
combo_counts = Counter()
for item in data:
    if item["decision"] == 1:
        combo_counts[(item["age"], item["race"], item["gender"])] += 1

# Display results
print("Single Category Counts:")
for category, count in single_counts.items():
    print(f"{category}: {count}")

print("\nCombination Counts:")
for combo, count in combo_counts.items():
    print(f"{combo}: {count}")
