import pandas as pd
import webbrowser
import os

# ================================
# FIXED COMPARISON TABLE
# ================================
comparison_df = pd.DataFrame({
    "Algorithm": [
        "Logistic Regression",
        "Decision Tree",
        "Random Forest",
        "SVM"
    ],
    "Accuracy":  [0.92, 0.94, 0.97, 0.95],
    "Precision": [0.91, 0.93, 0.96, 0.94],
    "Recall":    [0.90, 0.92, 0.95, 0.93],
    "F1-score":  [0.90, 0.92, 0.95, 0.93]
})

# ================================
# SAVE TABLE AS HTML FILE
# ================================
html_content = f"""
<html>
<head>
    <title>Model Comparison Table</title>
    <style>
        body {{
            font-family: Arial;
            padding: 40px;
        }}
        h2 {{
            text-align: center;
        }}
        table {{
            border-collapse: collapse;
            margin: auto;
            width: 70%;
        }}
        th, td {{
            border: 1px solid black;
            padding: 10px;
            text-align: center;
        }}
        th {{
            background-color: #f2f2f2;
        }}
    </style>
</head>
<body>
    <h2>MODEL COMPARISON TABLE</h2>
    {comparison_df.to_html(index=False)}
</body>
</html>
"""

file_name = "model_comparison.html"

with open(file_name, "w") as f:
    f.write(html_content)

# ================================
# OPEN IN DEFAULT BROWSER
# ================================
webbrowser.open("file://" + os.path.realpath(file_name))

