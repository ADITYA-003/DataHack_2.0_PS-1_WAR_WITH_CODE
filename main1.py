import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np
from streamlit_echarts import st_echarts
import pydeck as pdk
st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")
@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="Ai_companies1.xlsx",
        engine="openpyxl",
        sheet_name="sheet1",
        # skiprows=3,
        usecols="A:J",
        nrows=15,
    )
    return df
df = get_data_from_excel()
# st.write(df)
st.markdown(
    """
    <style>
        section[data-testid="stSidebar"] {
            width: 1200px !important; # Set the width to your desired value
        }
    </style>
    """,
    unsafe_allow_html=True,
)

def bar_Reliance():
    reliance_data = df[df['Name'] == 'Reliance Industries Ltd.']
    years = [2019, 2020, 2021, 2022, 2023]
    income_values = reliance_data.iloc[0, 3:8].tolist()
    X = years
    Y = income_values
    data = {
    'Year': X,
    'Income (in CR)': Y,
}
    df2 = pd.DataFrame(data)

    # Create a Streamlit bar chart
    st.title("Reliance ")
    st.bar_chart(df2, use_container_width=True)
#     # Filter the data for "Reliance Industries Ltd."


# Select the relevant columns for the last five years
    # reliance_data = reliance_data[['Income Year', 'Income of 5 Years']]

# Create a Streamlit bar chart
    # st.bar_chart(reliance_data.set_index('Income Year'))

with st.sidebar.header("Please Filter Here:"):
    location = st.sidebar.multiselect(
        "Select the Location:",
        options=df["Location"].unique(),
        default=df["Location"].unique()
    )
    st.header(' :blue[DASHBOARD] :trophy:',divider="rainbow")
    st.button("TOP_COMAPANY",on_click=bar_Reliance,type="primary")
    
    # uploaded_file = st.file_uploader("Choose a file")
    # if uploaded_file is not None:
    #     dd = pd.read_csv(uploaded_file)
    #     st.write(dd)


sector = st.sidebar.multiselect(
    "Select the Sector Type:",
    options=df["Sector"].unique(),
    default=df["Sector"].unique(),
)

df_selection = df.query(
    "Location == @location & Sector == @sector"
)
print(df)
total_revenue = int(df_selection['Total_Income'].sum())
average_income_2023 = round(df_selection["Income in 2023(in CR)"].mean(), 2)
column1,column2,column3 = st.columns(3)
with column1:
    # st.subheader("total income")
    st.subheader(f"Total_Income {total_revenue}")
with column2:
    st.subheader("Average Income In 2023:")
    st.subheader(average_income_2023)
# ---- MAINPAGE ----
st.title(":bar_chart: Sales Dashboard")
st.markdown("##")


tab1, tab2, tab3, tab4,tab5  = st.tabs(["2023","2022","2021","2020","2019"])
with tab1:
    top_10_companies = df.sort_values(by="Income in 2023(in CR)",ascending=False).head(10)
    st.write(top_10_companies[["Name","Income in 2023(in CR)"]])
    
with tab2:
    top_10_companies = df.sort_values(by="Income in 2022(in CR)",ascending=False).head(10)
    st.write(top_10_companies[["Name","Income in 2022(in CR)"]])
with tab3:
    top_10_companies = df.sort_values(by="Income in 2021(in CR)",ascending=False).head(10)
    st.write(top_10_companies[["Name","Income in 2021(in CR)"]])
with tab4:
    top_10_companies = df.sort_values(by="Income in 2020(in CR)",ascending=False).head(10)
    st.write(top_10_companies[["Name","Income in 2020(in CR)"]])
with tab5:
    top_10_companies = df.sort_values(by="Income in 2019(in CR)",ascending=False).head(10)
    st.write(top_10_companies[["Name","Income in 2019(in CR)"]])


sales_by_sector = df_selection.groupby(by=["Sector"])[["Total_Income"]].sum().sort_values(by="Total_Income")
product_sales = px.bar(
    sales_by_sector,
    x="Total_Income",
    y=sales_by_sector.index,
    orientation="h",
    title="<b>Sales by sector</b>",
    color_discrete_sequence=["#275BBB"] * len(sales_by_sector),
    template="plotly_white",
)
product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
fig_avg_income_2023 = px.bar(
    sales_by_sector,
    x="Total_Income",
    y=sales_by_sector.index,
    orientation="h",
    title="<b>Sales by sector</b>",
    color_discrete_sequence=["#275BBB"] * len(sales_by_sector),
    template="plotly_white",
)
product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
#visvalization
column1,column2,column3 = st.columns(3)
column1.plotly_chart(product_sales,use_container_width=True)
df5 = pd.DataFrame(
    np.random.randn[(21,78, 2)/50],
    columns=['lat', 'lon'])

st.map(df5)
# gender = st.sidebar.multiselect(
#     "Select the Gender:",
#     options=df["Gender"].unique(),
#     default=df["Gender"].unique()
# )
# payment = st.sidebar.multiselect(
#     "Select the Payment",
#     options=df["Payment"].unique(),
#     default=df["Payment"].unique()
# )
# branch = st.sidebar.multiselect(
#     "Select the Branch",
#     options=df["Branch"].unique(),
#     default=df["Branch"].unique()
# )

df_selection = df.query(
    "Location == @location & Sector==@sector "
)

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop() # This will halt the app from further execution.


