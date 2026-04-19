import arakawa as ar
import plotly.express as px
import pandas as pd

# 1. Create Sample Data
df = pd.DataFrame({
    "Category": ["A", "B", "C", "D"],
    "Values": [10, 20, 15, 25]
})

# 2. Create Plotly Chart
fig = px.bar(df, x="Category", y="Values", title="Sample Category Distribution")

# 3. Build the Blog with ar.Blocks
report = ar.Blocks(
    "# Arakawa Interactive Blog",
    "This is a sample blog generated with Arakawa and Plotly.",
    ar.Plot(fig),
    ar.DataTable(df)
)

# 4. Save to index.html
ar.save_report(report, path="index.html")
print("Blog successfully generated at index.html")
