import json
from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Categories
age_categories = ["20", "30", "40", "50", "60", "70", "80", "90", "100"]
race_categories = ["white", "hispanic", "asian", "native american", "black"]
gender_categories = ["male", "female", "non-binary"]

# Load data
def read_jsonl(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        lines = file.readlines()  # Read the lines from the file
        return [json.loads(line) for line in lines]

data = read_jsonl("output/exp_lv_full.jsonl")

# Single category counts
single_counts = defaultdict(int)
for item in data:
    if item["bool"] == 1:
        age_str = str(item["age"])
        single_counts["age_" + age_str] += 1
        single_counts["race_" + item["race"]] += 1
        single_counts["gender_" + item["gender"]] += 1

# Combination counts
combo_counts = Counter()
for item in data:
    if item["bool"] == 1:
        combo_counts[(item["age"], item["race"], item["gender"])] += 1

# Plot single category counts
def plot_single_counts(single_counts):
    categories = ["age", "race", "gender"]
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    for ax, category in zip(axes, categories):
        counts = {k: v for k, v in single_counts.items() if k.startswith(category)}
        labels, values = zip(*counts.items())
        
        ax.bar(labels, values)
        ax.set_title(f"{category.capitalize()} Counts")
        ax.set_xticks(range(len(labels)))  # Set the positions of the ticks
        ax.set_xticklabels(labels, rotation=45, ha="right")  # Use FixedLocator with FixedFormatter
    
    plt.tight_layout()
    plt.show()

# Plot combination counts
def plot_combo_counts(combo_counts):
    age_labels = age_categories
    race_labels = race_categories
    gender_labels = gender_categories

    # Create a 3D array to store the counts
    heatmap_data = np.zeros((len(age_labels), len(race_labels), len(gender_labels)), dtype=int)

    for (age, race, gender), count in combo_counts.items():
        if str(age) in age_labels and race in race_labels and gender in gender_labels:
            age_idx = age_labels.index(str(age))
            race_idx = race_labels.index(race)
            gender_idx = gender_labels.index(gender)
            heatmap_data[age_idx, race_idx, gender_idx] = count

    # Plot heatmaps for each gender
    fig, axes = plt.subplots(1, len(gender_labels), figsize=(18, 6))
    
    for ax, gender, gender_idx in zip(axes, gender_labels, range(len(gender_labels))):
        sns.heatmap(heatmap_data[:, :, gender_idx], ax=ax, xticklabels=race_labels, yticklabels=age_labels, annot=True, fmt="d", annot_kws={"size": 10})
        ax.set_title(f"Counts for {gender}")
        ax.set_xlabel("Race")
        ax.set_ylabel("Age")

    plt.tight_layout()
    plt.show()

# Display results
print("Single Category Counts:")
for category, count in single_counts.items():
    print(f"{category}: {count}")

print("\nCombination Counts:")
for combo, count in combo_counts.items():
    print(f"{combo}: {count}")

# Plot the counts
plot_single_counts(single_counts)
plot_combo_counts(combo_counts)

