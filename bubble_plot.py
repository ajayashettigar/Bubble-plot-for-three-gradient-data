#HPV Bubble Plot

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import random
import matplotlib.cm as cm

# Load data from Excel file
file_path = "/content/Treatment_monitoring.xlsx"  # Change this to your file path
df = pd.read_excel(file_path)

# Preserve the exact column order from Excel
original_time_order = df.columns[1:].tolist()  # First column is 'Sample ID', rest are Time Points

# Reshaping data for plotting (NO reordering)
df_melted = df.melt(id_vars=["Sample ID"], var_name="Time Point", value_name="Value", ignore_index=True)
df_melted.dropna(inplace=True)  # Remove NaN values

# **Ensure 'Time Point' follows the exact order from the Excel file**
df_melted["Time Point"] = pd.Categorical(df_melted["Time Point"], categories=original_time_order, ordered=True)

# Apply jittering to spread out overlapping points
jitter_strength = 0  # Adjust for more or less separation
unique_time_points = {tp: i for i, tp in enumerate(original_time_order)}  # Use original order
df_melted["Jittered Time"] = df_melted["Time Point"].map(lambda x: unique_time_points[x] + random.uniform(-jitter_strength, jitter_strength))

# Normalize bubble sizes for colormap (Enhanced contrast)
norm = mcolors.PowerNorm(gamma=0.2, vmin=df_melted["Value"].min(), vmax=df_melted["Value"].max())
cmap = plt.cm.plasma.reversed()  # Reversed 'plasma' colormap (smallest = purple, largest = yellow-green)

# **Apply transformation to avoid tiny dots**
scale_factor = 5  # Adjust this for better visibility
df_melted["Scaled Size"] = np.sqrt(df_melted["Value"]) * scale_factor  # Square root scaling

# Separate data for circles and triangles
circle_data = df_melted[df_melted["Value"] >= 1]
triangle_data = df_melted[df_melted["Value"] < 1]

# **Custom Y-axis labels**
y_labels = [
    "Pre", "PRT", "PBT", "1 Month", "3 Months", "6 Months",
    "12 Months", "24 Months", "30 Months"
]  # Add more blank lines if needed
y_positions = np.arange(len(y_labels))  # Generate y positions for labels

# Bubble Plot
plt.figure(figsize=(22, 12))

# Plot circles (Value >= 1)
sc1 = plt.scatter(
    circle_data["Jittered Time"],
    circle_data["Sample ID"],
    s=circle_data["Scaled Size"],
    c=circle_data["Value"],
    cmap=cmap,
    norm=norm,
    alpha=0.75,
    marker="o",
    edgecolors="black"
)

# Plot triangles (Value < 1)
sc2 = plt.scatter(
    triangle_data["Jittered Time"],
    triangle_data["Sample ID"],
    s=50, # fixed triangle value
    c=triangle_data["Value"],
    cmap=cmap,
    norm=norm,
    alpha=0.75,
    marker="^",  # Triangle marker
    edgecolors="black"
)

# **Set Y-axis labels manually**
plt.yticks(ticks=y_positions, labels=y_labels)

# **Force the correct X-axis order**
plt.xticks(ticks=range(len(original_time_order)), labels=original_time_order, rotation=45)

# Labels and formatting
plt.xlabel("Sample IDs")
plt.ylabel("Time Points")
plt.title("Bubble Plot with Size-Based Color Mapping (Small Values as Triangles)")

# Add color bar (now correctly linked to scatter plot)
cbar = plt.colorbar(sc1)
cbar.set_label("Measurement Value")

plt.grid(True, linestyle="--", alpha=0.1)

# Save the figure in high resolution for publication
plt.savefig("bubble_plot.svg", format="svg")  # Vector format (scalable)
plt.savefig("bubble_plot.jpg", format="jpg", dpi=600)  # High-quality raster format

# Show the plot
plt.show()
