import pandas as pd  # pip install pandas openpyxl
import plotly.express as px  # pip install plotly-express
import streamlit as st  # pip install streamlit
import numpy as np
from streamlit_echarts import st_echarts
import pydeck as pdk
from bokeh.plotting import figure
import matplotlib.pyplot as plt

st.set_page_config(page_title="Sales Dashboard", page_icon=":bar_chart:", layout="wide")


@st.cache_data
def get_data_from_excel():
    df = pd.read_excel(
        io="Ai_companies.xlsx",
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
px.defaults.width = 1000
px.defaults.height = 500


def bar_Reliance():
    reliance_data = df[df["Name"] == "Reliance Industries Ltd."]
    years = [2019, 2020, 2021, 2022, 2023]
    income_values = reliance_data.iloc[0, 3:8].tolist()
    X = years
    Y = income_values
    data = {
        "Year": X,
        "Income (in CR)": Y,
    }
    df2 = pd.DataFrame(data)

    # Create a Streamlit bar chart
    st.title("Reliance ")
    st.bar_chart(df2, use_container_width=True)


css = """
<style>
    [data-testid="stSidebar"]{
        min-width: 100px;
        max-width: 400px;
    }
</style>
"""
st.markdown(css, unsafe_allow_html=True)
css = """
<style>
    [data-testid="sttabs"]{
        max-width: 800px;
    }
</style>
"""
st.markdown(css, unsafe_allow_html=True)


#     # Filter the data for "Reliance Industries Ltd."
def covid():
    data = {
        "Company Name": [
            "Tata Elxsi",
            "Kellton Tech Solutions Limited",
            "Happiest Minds Technologies Ltd.",
            "Zensar Technologies Ltd.",
            "Persistent Systems",
            "Saksoft",
            "Cyient",
            "Affle (India) Limited",
            "Haptik",
            "Flutura",
            "Niki.ai",
            "Reliance Industries Ltd.",
            "TVS Motor Company",
            "Tata Motors",
            "Indian Oil Corporation",
            "Mahindra & Mahindra",
            "Hindalco Industries",
            "Exide Industries Ltd",
            "Aether Industries",
            "Ola Electric",
            "Yulu",
            "EMotorad",
            "Wipro",
            "Tata Consultancy Services Ltd",
            "Mindtree",
            "Infosys Ltd",
            "Tech Mahindra",
            "Subex Ltd",
            "Zoho",
            "Razorpay Software Pvt Ltd",
        ],
        "Total_Income": [
            10648.47,
            4137.5,
            4694.7,
            8089.69,
            15240.63,
            745.01,
            9262.4,
            1528.06,
            353.67,
            484.63,
            15.2,
            3272020,
            115054,
            1453594,
            2825231,
            471108,
            804860,
            57840.04,
            1265,
            3074.72,
            46.4,
            252.49,
            364947,
            904305,
            1516,
            555228,
            211991,
            1738,
            25346.05,
            2330.2,
        ],
    }
    df = pd.DataFrame(data)

    # Create a line chart using st.line_chart
    st.line_chart(
        df.set_index("Company Name")["Total_Income"], use_container_width=True
    )

    # X = df.iloc[:,9:]

    # Y = df.iloc[:,-1]

    # p = figure(
    # title='Effect of Covid19 On Indian Startups',
    # x_axis_label='x',
    # y_axis_label='y')

    # # p.line(x, y, legend_label='Trend', line_width=2)

    # st.line_chart(df, x=X,y=Y, use_container_width=True)


# Select the relevant columns for the last five years
# reliance_data = reliance_data[['Income Year', 'Income of 5 Years']]

# Create a Streamlit bar chart
# st.bar_chart(reliance_data.set_index('Income Year'))
st.header(" :blue[DASHBOARD] :trophy:", divider="rainbow")
with st.sidebar.header("Please Filter Here:"):
    location = st.sidebar.multiselect(
        "Select the Location:",
        options=df["Location"].unique(),
        default=df["Location"].unique(),
    )
    custom_css = """
    <style>
       .multiselect[data-testid="stMultiselect"] .st-eb{  
        background-color: #A352B0; /* Background color */
        color: #FFFFFF; /* Text color */
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)
    head1, head2 = st.columns(2)
    with head1:
        q1 = st.button("TOP_COMPANY", on_click=bar_Reliance, type="primary")
        m1 = st.markdown(
            """
            <style>
                button[data-testid="baseButton-secondary"]{  
                    background-color: #86CCEE;
                    color:#FFFFFF;
                }
            </style>""",
            unsafe_allow_html=True,
        )
    with head2:
        q2 = st.button("COVID19_STATITICS", on_click=covid, type="secondary")
        m = st.markdown(
            """
            <style>
                button[data-testid="baseButton-secondary"]{  
                    background-color: #A352B0;
                    color:#FFFFFF;
                }
            </style>""",
            unsafe_allow_html=True,
        )


sector = st.sidebar.multiselect(
    "Select the Sector Type:",
    options=df["Sector"].unique(),
    default=df["Sector"].unique(),
)
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    dd = pd.read_csv(uploaded_file, encoding="ISO-8859-1")
    st.write(dd)
    dd.to_csv("uploaded_file.csv", index=False)

    options = dd.columns.to_list()
    user_input = st.multiselect("Select an option: ", options)
    st.write("You selected: ", user_input)
    if user_input:
        plt.plot(dd[user_input[0]], dd[user_input[1]])
        st.pyplot(plt)
df_selection = df.query("Location == @location & Sector == @sector")

total_revenue = int(df_selection["Total_Income"].sum())
average_income_2023 = round(df_selection["Income in 2023(in CR)"].mean(), 2)
column1, column2 = st.columns(2)
with column1:
    # st.subheader("total income")
    st.subheader(f":blue[Total_Income] {total_revenue} :red[CR]")
with column2:
    st.subheader(f":blue[Average Income In 2023:] {average_income_2023} :red[CR]")
# ---- MAINPAGE ----
st.title(":bar_chart: INCOME TRENDS")
st.markdown("##")


tab1, tab2, tab3, tab4, tab5 = st.tabs(["2023", "2022", "2021", "2020", "2019"])
with tab1:
    top_10_companies = df.sort_values(by="Income in 2023(in CR)", ascending=False).head(
        10
    )
    st.write(top_10_companies[["Name", "Income in 2023(in CR)"]])
with tab2:
    top_10_companies = df.sort_values(by="Income in 2022(in CR)", ascending=False).head(
        10
    )
    st.write(top_10_companies[["Name", "Income in 2022(in CR)"]])
with tab3:
    top_10_companies = df.sort_values(by="Income in 2021(in CR)", ascending=False).head(
        10
    )
    st.write(top_10_companies[["Name", "Income in 2021(in CR)"]])
with tab4:
    top_10_companies = df.sort_values(by="Income in 2020(in CR)", ascending=False).head(
        10
    )
    st.write(top_10_companies[["Name", "Income in 2020(in CR)"]])
with tab5:
    top_10_companies = df.sort_values(by="Income in 2019(in CR)", ascending=False).head(
        10
    )
    st.write(top_10_companies[["Name", "Income in 2019(in CR)"]])


data = {
    "Sector": [
        "Natural Language Processing",
        "Conversational AI",
        "Machine Learning",
        "Big Data",
        "ERP Consulting",
        "Data Analytics",
        "Artificial Intelligence",
        "Custom Software Development",
        "Electrive Vehicle",
        "Electric Vehicle",
    ],
    "Total_Income": [
        15.20,
        353.67,
        4137.50,
        4694.70,
        8089.69,
        9262.40,
        13406.17,
        15240.63,
        3272020.00,
        4393879.00,
    ],
}

df10 = pd.DataFrame(data)
st.bar_chart(df10.set_index("Sector"), use_container_width=True)

sales_by_sector = (
    df_selection.groupby(by=["Sector"])[["Total_Income"]]
    .sum()
    .sort_values(by="Total_Income")
)
# print(sales_by_sector)

# Create a bar chart with Sector on the y-axis and Total_Income on the x-axis

product_sales = px.bar(
    sales_by_sector,
    x="Total_Income",
    y=sales_by_sector.index,
    orientation="h",
    title="<b>Sales by sector</b>",
    color_discrete_sequence=["#275BBB"] * len(sales_by_sector),
    template="plotly_white",
)
print(product_sales)
product_sales.update_layout(plot_bgcolor="rgba(0,0,0,0)", xaxis=(dict(showgrid=False)))
fig_avg_income_2023 = px.bar(
    sales_by_sector,
    x="Total_Income",
    y=sales_by_sector.index,
    orientation="h",
    title="<b>Sales by sector</b>",
    color_discrete_sequence=["#275BBB"] * len(sales_by_sector),
    template="plotly_white",
)
product_sales.update_layout(plot_bgcolor="rgba(0,0,0,0)", xaxis=(dict(showgrid=False)))
# visvalization
column1, column2, column3 = st.columns(3)
column1.plotly_chart(product_sales, use_container_width=True)
st.title("TOP 10 STARTUPS")
df5 = pd.DataFrame(
    {
        "col1": [
            28.6139,
            19.7515,
            26.8467,
            15.3173,
            11.1271,
            22.9868,
            27.0238,
            10.8505,
            22.2587,
            31.1471,
        ],
        "col2": [
            77.2090,
            75.7139,
            80.9462,
            75.7139,
            78.6569,
            87.8550,
            74.2179,
            76.2711,
            71.1924,
            75.3412,
        ],
        "col3": np.random.randn(10) * 10000,
        "col4": np.random.rand(10, 4).tolist(),
    }
)

st.map(df5, latitude="col1", longitude="col2", size="col3", color="col4")

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

df_selection = df.query("Location == @location & Sector==@sector ")

# Check if the dataframe is empty:
if df_selection.empty:
    st.warning("No data available based on the current filter settings!")
    st.stop()  # This will halt the app from further execution.
