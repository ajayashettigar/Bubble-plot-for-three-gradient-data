# HPV Bubble Plot Visualization

This script generates a **bubble plot** to visualize **HPV measurement values** across multiple time points for different **sample IDs**. It utilizes **bubble sizes and colors** to represent data values while distinguishing small values using triangles.

## Features
✅ **Time Point Order Preserved**: Ensures the exact column order from the Excel file.  
✅ **Bubble Size & Color Mapping**: Uses square-root scaling for better visibility.  
✅ **Jittering (Optional)**: Prevents overlapping points for clarity.  
✅ **Colormap**: Uses a reversed 'plasma' colormap for high contrast.  
✅ **Custom Axis Labels**: Provides clear x-axis and y-axis labels.  
✅ **High-Resolution Output**: Saves the plot as **SVG (vector)** and **JPG (600 DPI)**.

---

## Installation & Requirements
This script requires **Python 3.x** and the following dependencies:

Usage
1️⃣ Place Your Data File
Ensure your Excel file (Treatment_monitoring.xlsx) is in the correct location.

2️⃣ Modify File Path
Open the script and update the file path:
```
file_path = "/path/to/Treatment_monitoring.xlsx"
```

3️⃣ Run the Script
Execute the Python script:
```
python bubble_plot.py
```

4️⃣ Check Output Files
The generated figures will be saved as:

bubble_plot.svg (Scalable Vector Format)
bubble_plot.jpg (High-Resolution 600 DPI)
Plot Details
🔹 Bubble Size & Color Mapping

Larger values → Larger circles
Smaller values (< 1) → Represented as triangles
Color gradient: Darker colors for higher values
📌 Custom Time Points (Y-Axis) The y-axis represents time points:
Pre, PRT, PBT, 1 Month, 3 Months, 6 Months, 12 Months, 24 Months, 30 Months
🎨 Colormap & Color Bar Uses a plasma colormap (reversed) for better contrast.

A color bar is included to indicate measurement values.

Example Output 📊
[Include an example image here]

Future Enhancements 🚀
✅ Add interactive visualization using plotly
✅ Allow user-defined jittering for better separation
✅ Improve colormap customization for user preferences

License 📜
This project is licensed under the MIT License. You are free to modify and distribute it.
