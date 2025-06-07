from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

# Initialize connection to data sources
connect()

# Load the sports data
df = get_df("sports.csv")

# Create a title for the dashboard
text("Sports Data Analysis Dashboard")

# Create a filtered view for Sports Datasets
sql = "SELECT * FROM sports"
queens_df = query(sql, "sports")

fig = px.scatter(queens_df, y="DIMENSIONS", x="COMMUNITYBOARD", title="Handball Analysis Board")
fig.update_traces(textposition='top center', marker=dict(size=12, color='lightblue'))

plotly(fig)

# Display the full dataset
table(queens_df, title="Queens Sports Attendance")