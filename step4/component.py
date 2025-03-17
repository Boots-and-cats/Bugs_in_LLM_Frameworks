import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import matplotlib.font_manager as fm

# Data from the table (excluding total row)
root_causes = [
    "API Misuse", 
    "Incompatibility", 
    "Assignment Issue", 
    "Parameter/Argument Issue",
    "Code Logic Issue", 
    "Import Error", 
    "Type",
    "Incorrect Exception Handling",
    "Incorrect Numerical Computation"
]

# Include Total column
components = ["Data Preprocess", "Core Schema", "Agent Construction", "Featured Module", "Total"]

# Updated data matrix with corrected values and total column
raw_data = np.array([
    [103, 59, 22, 70, 254],
    [15, 22, 16, 3, 56],
    [24, 7, 4, 6, 41],
    [63, 51, 15, 31, 160],
    [150, 82, 27, 131, 390],
    [14, 9, 2, 11, 36],
    [17, 9, 8, 14, 48],
    [16, 6, 6, 3, 31],
    [6, 2, 0, 2, 10]
])

# Calculate column sums for normalization (excluding total column)
column_sums = raw_data[:, :-1].sum(axis=0)

# Create normalized data for the first 4 columns
normalized_data = np.zeros((len(root_causes), len(components)))
for j in range(4):  # First 4 columns (components)
    normalized_data[:, j] = raw_data[:, j] / column_sums[j] * 100

# Normalize the total column separately
total_sum = raw_data[:, 4].sum()
normalized_data[:, 4] = raw_data[:, 4] / total_sum * 100

# Create the figure and set its size
plt.figure(figsize=(14, 10))

# Create a blank heatmap without annotations first
ax = sns.heatmap(normalized_data, annot=False, fmt=".1f", cmap="Blues", 
                 xticklabels=components, 
                 yticklabels=root_causes,
                 vmin=0, vmax=40,  # Set fixed range for better contrast
                 cbar_kws={'label': 'Percentage within Component (%)'})

# Add custom annotations with both percentage and raw count
for i in range(len(root_causes)):
    for j in range(len(components)):
        # Determine text color based on cell intensity for better readability
        cell_value = normalized_data[i, j]
        if cell_value > 20:  # Threshold for switching text color
            text_color = 'white'
        else:
            text_color = 'black'
            
        text = f"{cell_value:.1f} ({raw_data[i, j]})"
        plt.text(j + 0.5, i + 0.5, text, 
                ha='center', va='center', color=text_color, 
                fontsize=16, fontweight='bold')

# Remove title and axis labels
plt.title('')
plt.xlabel('')
plt.ylabel('')

# Make tick labels bold and larger
plt.xticks(rotation=30, ha='right', fontweight='bold', fontsize=21)
plt.yticks(fontweight='bold', fontsize=21)

# Make colorbar label and ticks bold and larger
cbar = ax.collections[0].colorbar
cbar.ax.set_ylabel('Percentage within Component (%)', fontweight='bold', fontsize=21)
cbar.ax.tick_params(labelsize=14)
for l in cbar.ax.yaxis.get_ticklabels():
    l.set_weight('bold')
    l.set_fontsize(18)

# Add a border around each cell for better delineation
for _, spine in ax.spines.items():
    spine.set_visible(True)
    spine.set_linewidth(1.5)

# Adjust layout to make sure everything fits
plt.tight_layout()

# Save and show the plot
plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# import seaborn as sns

# # Data from the table (excluding total row)
# symptoms = [
#     "Crash",
#     "Incorrect Functionality", 
#     "Unexpected Output",
#     "Hang",
#     "External Connection Failure",
#     "Unidentified"
# ]

# # Include Total column
# components = ["Data Preprocess", "Core Schema", "Agent Construction", "Featured Module", "Total"]

# # Data from the table
# raw_data = np.array([
#     [110, 82, 29, 105, 326],
#     [160, 67, 24, 64, 315],
#     [50, 40, 13, 66, 169],
#     [4, 5, 5, 15, 29],
#     [50, 24, 4, 25, 103],
#     [31, 23, 9, 21, 84]
# ])

# # Calculate column sums for normalization (excluding total column)
# column_sums = raw_data[:, :-1].sum(axis=0)

# # Create normalized data for the first 4 columns
# normalized_data = np.zeros((len(symptoms), len(components)))
# for j in range(4):  # First 4 columns (components)
#     normalized_data[:, j] = raw_data[:, j] / column_sums[j] * 100

# # Normalize the total column separately
# total_sum = raw_data[:, 4].sum()
# normalized_data[:, 4] = raw_data[:, 4] / total_sum * 100

# # Create the figure and set its size
# plt.figure(figsize=(14, 10))

# # Create a blank heatmap without annotations first
# ax = sns.heatmap(normalized_data, annot=False, fmt=".1f", cmap="Blues", 
#                  xticklabels=components, 
#                  yticklabels=symptoms,
#                  vmin=0, vmax=40,  # Set fixed range for better contrast
#                  cbar_kws={'label': 'Percentage within Component (%)'})

# # Add custom annotations with both percentage and raw count
# for i in range(len(symptoms)):
#     for j in range(len(components)):
#         # Determine text color based on cell intensity for better readability
#         cell_value = normalized_data[i, j]
#         if cell_value > 20:  # Threshold for switching text color
#             text_color = 'white'
#         else:
#             text_color = 'black'
            
#         text = f"{cell_value:.1f} ({raw_data[i, j]})"
#         plt.text(j + 0.5, i + 0.5, text, 
#                 ha='center', va='center', color=text_color, 
#                 fontsize=18, fontweight='bold')

# # Remove title and axis labels
# plt.title('')
# plt.xlabel('')
# plt.ylabel('')

# # Make tick labels bold and larger
# plt.xticks(rotation=30, ha='right', fontweight='bold', fontsize=21)
# plt.yticks(fontweight='bold', fontsize=21)

# # Make colorbar label and ticks bold and larger
# cbar = ax.collections[0].colorbar
# cbar.ax.set_ylabel('Percentage within Component (%)', fontweight='bold', fontsize=21)
# cbar.ax.tick_params(labelsize=14)
# for l in cbar.ax.yaxis.get_ticklabels():
#     l.set_weight('bold')
#     l.set_fontsize(18)

# # Add a border around each cell for better delineation
# for _, spine in ax.spines.items():
#     spine.set_visible(True)
#     spine.set_linewidth(1.5)

# # Adjust layout to make sure everything fits
# plt.tight_layout()

# # Save and show the plot
# plt.savefig('normalized_symptoms_component_distribution.png', dpi=300, bbox_inches='tight')
# plt.show()