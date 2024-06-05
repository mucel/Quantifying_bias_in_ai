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

data = read_jsonl("output/exp_eng.jsonl")

# Single category counts
single_counts = defaultdict(lambda: defaultdict(int))
for item in data:
    age_str = str(item["age"])
    single_counts["age_" + age_str][item["bool"]] += 1
    single_counts["race_" + item["race"]][item["bool"]] += 1
    single_counts["gender_" + item["gender"]][item["bool"]] += 1

# Combination counts
combo_counts = defaultdict(lambda: defaultdict(int))
for item in data:
    combo_counts[(item["age"], item["race"], item["gender"])][item["bool"]] += 1

# Calculate statistics
def calculate_statistics(single_counts):
    statistics = {}
    for category, counts in single_counts.items():
        total = sum(counts.values())
        percentages = {k: (v / total) * 100 for k, v in counts.items()}
        mean = np.mean(list(counts.values()))
        std_dev = np.std(list(counts.values()))
        statistics[category] = {
            "total": total,
            "percentages": percentages,
            "mean": mean,
            "std_dev": std_dev
        }
    return statistics

single_stats = calculate_statistics(single_counts)

# Plot single category counts
def plot_single_counts(single_counts):
    categories = ["age", "race", "gender"]
    fig, axes = plt.subplots(1, 3, figsize=(18, 6))
    
    for ax, category in zip(axes, categories):
        counts = {k: v for k, v in single_counts.items() if k.startswith(category)}
        labels = sorted(counts.keys())
        values_0 = [counts[label][0] for label in labels]
        values_1 = [counts[label][1] for label in labels]
        values_2 = [counts[label][2] for label in labels]

        ax.bar(labels, values_0, color='blue', label='no', alpha=0.6)
        ax.bar(labels, values_1, bottom=values_0, color='green', label='yes', alpha=0.6)
        ax.bar(labels, values_2, bottom=[i+j for i,j in zip(values_0, values_1)], color='red', label='no answer', alpha=0.6)

        ax.set_title(f"{category.capitalize()} Counts")
        ax.set_xticks(range(len(labels)))  # Set the positions of the ticks
        ax.set_xticklabels(labels, rotation=45, ha="right")  # Use FixedLocator with FixedFormatter
        ax.legend()

    plt.tight_layout()
    plt.show()

# Plot combination counts
def plot_combo_counts(combo_counts):
    age_labels = age_categories
    race_labels = race_categories
    gender_labels = gender_categories

    # Create a 4D array to store the counts for 0, 1, and 2
    heatmap_data = np.zeros((len(age_labels), len(race_labels), len(gender_labels), 3), dtype=int)

    for (age, race, gender), count_dict in combo_counts.items():
        if str(age) in age_labels and race in race_labels and gender in gender_labels:
            age_idx = age_labels.index(str(age))
            race_idx = race_labels.index(race)
            gender_idx = gender_labels.index(gender)
            for bool_value, count in count_dict.items():
                heatmap_data[age_idx, race_idx, gender_idx, bool_value] = count

    # Plot heatmaps for each gender
    fig, axes = plt.subplots(3, len(gender_labels), figsize=(18, 18))

    for bool_value, bool_label in zip(range(3), ['no', 'yes', 'no answer']):
        for ax, gender, gender_idx in zip(axes[bool_value], gender_labels, range(len(gender_labels))):
            sns.heatmap(heatmap_data[:, :, gender_idx, bool_value], ax=ax, xticklabels=race_labels, yticklabels=age_labels, annot=True, fmt="d", annot_kws={"size": 10})
            ax.set_title(f"Counts for {gender} ({bool_label})")
            ax.set_xlabel("Race")
            ax.set_ylabel("Age")

    plt.tight_layout()
    plt.show()

# Display results
print("Single Category Counts:")
for category, count_dict in single_counts.items():
    print(f"{category}: {dict(count_dict)}")

print("\nCombination Counts:")
for combo, count_dict in combo_counts.items():
    print(f"{combo}: {dict(count_dict)}")

# Display statistics
print("\nStatistics:")
for category, stats in single_stats.items():
    print(f"{category}:")
    print(f"  Total: {stats['total']}")
    print(f"  Percentages: {stats['percentages']}")
    print(f"  Mean: {stats['mean']:.2f}")
    print(f"  Std Dev: {stats['std_dev']:.2f}")

# Plot the counts
#plot_single_counts(single_counts)
#plot_combo_counts(combo_counts)

