import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from pathlib import Path


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="AMAZON SALES DASHBOARD",
    page_icon="",
    layout="wide"
)


# =========================================================
# BASE DIRECTORY
# =========================================================

BASE_DIR = Path(__file__).resolve().parent


# =========================================================
# MAIN DASHBOARD CSS
# =========================================================

st.markdown("""
<style>

/* =====================================================
   MAIN APP
===================================================== */

.stApp {
    background-color: #101820;
    color: white;
}


/* =====================================================
   DASHBOARD TITLE
===================================================== */

.dashboard-title {
    text-align: center;
    color: #FFFFFF;
    font-size: 38px;
    font-weight: 900;
    margin-top: 5px;
    margin-bottom: 5px;
    letter-spacing: 1px;
}

.dashboard-subtitle {
    text-align: center;
    color: #AAB4C3;
    font-size: 15px;
    margin-bottom: 25px;
}


/* =====================================================
   SECTION TITLE
===================================================== */

.section-title {
    color: #FFFFFF;
    font-size: 23px;
    font-weight: 800;
    margin-top: 28px;
    margin-bottom: 15px;
}


/* =====================================================
   FILTER TITLE
===================================================== */

.filter-title {
    color: #FF9900;
    font-size: 20px;
    font-weight: 800;
    margin-top: 10px;
    margin-bottom: 10px;
}


/* =====================================================
   SELECT BOX
===================================================== */

div[data-baseweb="select"] > div {
    background-color: #1F2937 !important;
    border: 1px solid #374151 !important;
    color: white !important;
    border-radius: 10px !important;
}

div[data-baseweb="select"] span {
    color: white !important;
}


/* =====================================================
   ALL KPI CARDS
===================================================== */

[data-testid="stMetric"] {

    position: relative !important;

    overflow: hidden !important;

    border-radius: 20px !important;

    padding: 20px !important;

    min-height: 125px !important;

    border: 1px solid rgba(255,255,255,0.12) !important;

    box-shadow:
        0 8px 25px rgba(0,0,0,0.35),
        inset 0 1px 0 rgba(255,255,255,0.08) !important;

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease !important;
}


/* =====================================================
   KPI HOVER
===================================================== */

[data-testid="stMetric"]:hover {

    transform: translateY(-5px) !important;

    box-shadow:
        0 14px 35px rgba(0,0,0,0.50),
        inset 0 1px 0 rgba(255,255,255,0.15) !important;
}


/* =====================================================
   KPI LABEL
===================================================== */

[data-testid="stMetricLabel"] {

    color: #FFFFFF !important;

    font-size: 13px !important;

    font-weight: 800 !important;

    letter-spacing: 0.5px !important;
}


/* =====================================================
   KPI VALUE
===================================================== */

[data-testid="stMetricValue"] {

    color: #FFFFFF !important;

    font-size: 27px !important;

    font-weight: 900 !important;

    margin-top: 8px !important;
}


/* =====================================================
   KPI GRADIENT CARDS
===================================================== */

/* SALES */
[data-testid="stMetric"]:nth-of-type(1) {

    background:
        linear-gradient(
            135deg,
            #0066FF 0%,
            #00C6FF 100%
        ) !important;
}


/* PROFIT */
[data-testid="stMetric"]:nth-of-type(2) {

    background:
        linear-gradient(
            135deg,
            #00A86B 0%,
            #00E676 100%
        ) !important;
}


/* QUANTITY */
[data-testid="stMetric"]:nth-of-type(3) {

    background:
        linear-gradient(
            135deg,
            #FF6A00 0%,
            #FFB300 100%
        ) !important;
}


/* ORDERS */
[data-testid="stMetric"]:nth-of-type(4) {

    background:
        linear-gradient(
            135deg,
            #6A11CB 0%,
            #B721FF 100%
        ) !important;
}


/* =====================================================
   SECOND ROW GRADIENTS
===================================================== */

/* AVERAGE SALES */
.kpi-average-sales [data-testid="stMetric"] {

    background:
        linear-gradient(
            135deg,
            #EC008C,
            #FC6767
        ) !important;
}


/* AVERAGE PROFIT */
.kpi-average-profit [data-testid="stMetric"] {

    background:
        linear-gradient(
            135deg,
            #0083B0,
            #00B4DB
        ) !important;
}


/* PRODUCTS */
.kpi-products [data-testid="stMetric"] {

    background:
        linear-gradient(
            135deg,
            #FF416C,
            #FF4B2B
        ) !important;
}


/* CUSTOMERS */
.kpi-customers [data-testid="stMetric"] {

    background:
        linear-gradient(
            135deg,
            #396AFC,
            #2948FF
        ) !important;
}


/* =====================================================
   PROGRESS BAR
===================================================== */

.stProgress > div > div > div > div {

    background:
        linear-gradient(
            90deg,
            #00C6FF,
            #0072FF,
            #7B2FFF,
            #FF00CC
        ) !important;
}


/* =====================================================
   DOWNLOAD BUTTON
===================================================== */

.stDownloadButton > button {

    background:
        linear-gradient(
            135deg,
            #FF9900,
            #FFB700
        ) !important;

    color: #000000 !important;

    font-weight: 800 !important;

    border: none !important;

    border-radius: 10px !important;

    padding: 10px 20px !important;
}

.stDownloadButton > button:hover {

    background:
        linear-gradient(
            135deg,
            #FFB700,
            #FFD000
        ) !important;

    color: #000000 !important;
}


/* =====================================================
   FOOTER
===================================================== */

.footer {

    text-align: center;

    color: #7F8A9A;

    padding: 30px 0 10px 0;

    font-size: 13px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FIND LOGO
# =========================================================

logo_file = None

logo_names = [
    "logo.png",
    "logo.jpg",
    "logo.jpeg",
    "logo.webp",
    "amazon_logo.png",
    "amazon_logo.jpg",
    "amazon_logo.jpeg",
    "amazon_logo.webp"
]

for logo_name in logo_names:

    logo_path = BASE_DIR / logo_name

    if logo_path.exists():

        logo_file = logo_path

        break


# =========================================================
# DISPLAY LOGO
# =========================================================

if logo_file:

    logo_left, logo_center, logo_right = st.columns(
        [1, 2, 1]
    )

    with logo_center:

        st.image(
            str(logo_file),
            width=180
        )

else:

    st.markdown(
        """
        <div style="
            text-align:center;
            color:#FF9900;
            font-size:42px;
            font-weight:900;
            margin-bottom:10px;
        ">
            AMAZON
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# TITLE
# =========================================================

st.markdown(
    """
    <div class="dashboard-title">
         AMAZON SALES DASHBOARD
    </div>

    <div class="dashboard-subtitle">
        Sales • Profit • Products • Customers • Performance Analytics
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FIND CSV
# =========================================================

possible_csv_files = [
    "amazon_data.csv",
    "amazon.csv",
    "Amazon.csv",
    "AMAZON.csv",
    "amazon_sales.csv",
    "Amazon_Sales.csv"
]

csv_file = None


for file_name in possible_csv_files:

    file_path = BASE_DIR / file_name

    if file_path.exists():

        csv_file = file_path

        break


# =========================================================
# FIND ANY CSV
# =========================================================

if csv_file is None:

    csv_files = list(
        BASE_DIR.glob("*.csv")
    )

    if csv_files:

        csv_file = csv_files[0]


# =========================================================
# CHECK CSV
# =========================================================

if csv_file is None:

    st.error(
        "❌ No CSV file found."
    )

    st.info(
        f"Place your CSV file inside:\n\n{BASE_DIR}"
    )

    st.stop()


# =========================================================
# READ CSV
# =========================================================

df = None

last_error = None

encodings = [
    "utf-8",
    "utf-8-sig",
    "cp1252",
    "latin1"
]


for encoding in encodings:

    try:

        df = pd.read_csv(
            csv_file,
            encoding=encoding
        )

        break

    except UnicodeDecodeError as error:

        last_error = error


if df is None:

    st.error(
        f"❌ Unable to read CSV.\n\n{last_error}"
    )

    st.stop()


# =========================================================
# CLEAN COLUMN NAMES
# =========================================================

df.columns = (
    df.columns
    .astype(str)
    .str.strip()
    .str.lower()
    .str.replace(" ", "_", regex=False)
    .str.replace("-", "_", regex=False)
)


# =========================================================
# REQUIRED COLUMNS
# =========================================================

required_columns = [
    "order_date",
    "ship_date",
    "email_id",
    "geography",
    "category",
    "product_name",
    "sales",
    "quantity",
    "profit"
]


missing_columns = [
    column
    for column in required_columns
    if column not in df.columns
]


if missing_columns:

    st.error(
        "❌ Required columns are missing."
    )

    st.write(
        "### Missing Columns"
    )

    st.write(
        missing_columns
    )

    st.write(
        "### Columns Found"
    )

    st.write(
        list(df.columns)
    )

    st.stop()


# =========================================================
# CLEAN TEXT COLUMNS
# =========================================================

text_columns = [
    "email_id",
    "geography",
    "category",
    "product_name"
]


for column in text_columns:

    df[column] = (
        df[column]
        .astype(str)
        .str.strip()
    )


# =========================================================
# CLEAN NUMERIC COLUMNS
# =========================================================

numeric_columns = [
    "sales",
    "quantity",
    "profit"
]


for column in numeric_columns:

    df[column] = (
        df[column]
        .astype(str)
        .str.replace("₹", "", regex=False)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.replace("\xa0", "", regex=False)
        .str.strip()
    )

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


# =========================================================
# DATE COLUMNS
# =========================================================

df["order_date"] = pd.to_datetime(
    df["order_date"],
    errors="coerce"
)

df["ship_date"] = pd.to_datetime(
    df["ship_date"],
    errors="coerce"
)


# =========================================================
# REMOVE INVALID NUMERIC ROWS
# =========================================================

df = df.dropna(
    subset=[
        "sales",
        "quantity",
        "profit"
    ]
).copy()


# =========================================================
# FILTER TITLE
# =========================================================

st.markdown(
    """
    <div class="filter-title">
        🔎 DASHBOARD FILTERS
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FILTER COLUMNS
# =========================================================

filter_col1, filter_col2 = st.columns(2)


# =========================================================
# CATEGORY FILTER
# =========================================================

with filter_col1:

    categories = sorted(
        df["category"]
        .dropna()
        .unique()
        .tolist()
    )

    category_options = [
        "All Categories"
    ] + categories

    selected_category = st.selectbox(
        "📁 Category",
        category_options
    )


# =========================================================
# CATEGORY FILTER DATA
# =========================================================

if selected_category == "All Categories":

    category_filtered = df.copy()

else:

    category_filtered = df[
        df["category"] == selected_category
    ].copy()


# =========================================================
# GEOGRAPHY FILTER
# =========================================================

with filter_col2:

    geographies = sorted(
        category_filtered["geography"]
        .dropna()
        .unique()
        .tolist()
    )

    geography_options = [
        "All Geographies"
    ] + geographies

    selected_geography = st.selectbox(
        "🌍 Geography",
        geography_options
    )


# =========================================================
# FINAL FILTER
# =========================================================

filtered = category_filtered.copy()


if selected_geography != "All Geographies":

    filtered = filtered[
        filtered["geography"] == selected_geography
    ].copy()


# =========================================================
# FILTER INFORMATION
# =========================================================




# =========================================================
# KPI CALCULATIONS
# =========================================================

total_sales = filtered["sales"].sum()

total_profit = filtered["profit"].sum()

total_quantity = filtered["quantity"].sum()

total_orders = len(filtered)

average_sales = filtered["sales"].mean()

average_profit = filtered["profit"].mean()

total_products = filtered["product_name"].nunique()

total_customers = filtered["email_id"].nunique()


if pd.isna(average_sales):

    average_sales = 0


if pd.isna(average_profit):

    average_profit = 0


if total_sales != 0:

    profit_margin = (
        total_profit /
        total_sales
    ) * 100

else:

    profit_margin = 0


# =========================================================
# KPI TITLE
# =========================================================

st.markdown(
    """
    <div class="section-title">
        📌 KEY PERFORMANCE INDICATORS
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# KPI ROW 1
# =========================================================

kpi1, kpi2, kpi3, kpi4 = st.columns(4)


with kpi1:

    st.metric(
        label="💰 TOTAL SALES",
        value=f"${total_sales:,.2f}"
    )


with kpi2:

    st.metric(
        label="📈 TOTAL PROFIT",
        value=f"${total_profit:,.2f}"
    )


with kpi3:

    st.metric(
        label="📦 TOTAL QUANTITY",
        value=f"{total_quantity:,.0f}"
    )


with kpi4:

    st.metric(
        label="🛒 TOTAL ORDERS",
        value=f"{total_orders:,}"
    )


# =========================================================
# SECOND KPI ROW
# =========================================================

st.write("")


kpi5, kpi6, kpi7, kpi8 = st.columns(4)


with kpi5:

    st.metric(
        label="💵 AVERAGE SALES",
        value=f"${average_sales:,.2f}"
    )


with kpi6:

    st.metric(
        label="💹 AVERAGE PROFIT",
        value=f"${average_profit:,.2f}"
    )


with kpi7:

    st.metric(
        label="🏷️ TOTAL PRODUCTS",
        value=f"{total_products:,}"
    )


with kpi8:

    st.metric(
        label="👥 CUSTOMERS",
        value=f"{total_customers:,}"
    )


# =========================================================
# EXTRA GRADIENT OVERLAY
# =========================================================

st.markdown("""
<style>

/* Make every metric card visually richer */

[data-testid="stMetric"] {
    background-size: 200% 200% !important;
}


/* Different visual glow for cards */

[data-testid="stMetric"]::before {

    content: "";

    position: absolute;

    top: 0;
    left: 0;

    width: 100%;
    height: 5px;

    background:
        linear-gradient(
            90deg,
            #FFFFFF,
            rgba(255,255,255,0.2),
            #FFFFFF
        );

    opacity: 0.65;

}


/* Shine */

[data-testid="stMetric"]::after {

    content: "";

    position: absolute;

    width: 150px;
    height: 150px;

    top: -80px;
    right: -60px;

    border-radius: 50%;

    background:
        rgba(255,255,255,0.12);

    pointer-events: none;

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# PROFIT MARGIN
# =========================================================

st.markdown(
    """
    <div class="section-title">
        📊 OVERALL PROFIT MARGIN
    </div>
    """,
    unsafe_allow_html=True
)


margin_col1, margin_col2 = st.columns(
    [1, 3]
)


with margin_col1:

    st.metric(
        "Profit Margin",
        f"{profit_margin:.2f}%"
    )


with margin_col2:

    progress_value = max(
        0,
        min(
            100,
            profit_margin
        )
    )

    st.progress(
        progress_value / 100
    )


# =========================================================
# PERFORMANCE GAUGES
# =========================================================

st.markdown(
    """
    <div class="section-title">
        🎯 PERFORMANCE OVERVIEW
    </div>
    """,
    unsafe_allow_html=True
)


gauge1, gauge2, gauge3 = st.columns(3)


# =========================================================
# SALES GAUGE
# =========================================================

with gauge1:

    max_sales = max(
        abs(total_sales) * 1.2,
        1
    )

    fig_sales = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=total_sales,
            title={
                "text": "Total Sales"
            },
            number={
                "prefix": "$",
                "valueformat": ",.0f"
            },
            gauge={
                "axis": {
                    "range": [
                        0,
                        max_sales
                    ]
                },
                "bar": {
                    "color": "#00C6FF"
                },
                "bgcolor": "#1F2937",
                "borderwidth": 1,
                "bordercolor": "#374151"
            }
        )
    )

    fig_sales.update_layout(
        paper_bgcolor="#161A23",
        font_color="white",
        height=300
    )

    st.plotly_chart(
        fig_sales,
        use_container_width=True
    )


# =========================================================
# PROFIT GAUGE
# =========================================================

with gauge2:

    max_profit = max(
        abs(total_profit) * 1.2,
        1
    )

    fig_profit = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=total_profit,
            title={
                "text": "Total Profit"
            },
            number={
                "prefix": "$",
                "valueformat": ",.0f"
            },
            gauge={
                "axis": {
                    "range": [
                        0,
                        max_profit
                    ]
                },
                "bar": {
                    "color": "#00E676"
                },
                "bgcolor": "#1F2937",
                "borderwidth": 1,
                "bordercolor": "#374151"
            }
        )
    )

    fig_profit.update_layout(
        paper_bgcolor="#161A23",
        font_color="white",
        height=300
    )

    st.plotly_chart(
        fig_profit,
        use_container_width=True
    )


# =========================================================
# QUANTITY GAUGE
# =========================================================

with gauge3:

    max_quantity = max(
        abs(total_quantity) * 1.2,
        1
    )

    fig_quantity = go.Figure(
        go.Indicator(
            mode="gauge+number",
            value=total_quantity,
            title={
                "text": "Total Quantity"
            },
            number={
                "valueformat": ",.0f"
            },
            gauge={
                "axis": {
                    "range": [
                        0,
                        max_quantity
                    ]
                },
                "bar": {
                    "color": "#FFB300"
                },
                "bgcolor": "#1F2937",
                "borderwidth": 1,
                "bordercolor": "#374151"
            }
        )
    )

    fig_quantity.update_layout(
        paper_bgcolor="#161A23",
        font_color="white",
        height=300
    )

    st.plotly_chart(
        fig_quantity,
        use_container_width=True
    )


# =========================================================
# TOP 5 GEOGRAPHIES
# =========================================================

st.markdown(
    """
    <div class="section-title">
        🌍 TOP 5 GEOGRAPHIES BY SALES
    </div>
    """,
    unsafe_allow_html=True
)


if not filtered.empty:

    geography_sales = (
        filtered
        .groupby(
            "geography",
            as_index=False
        )["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
        .head(5)
    )


    fig_geo = px.pie(
        geography_sales,
        names="geography",
        values="sales",
        hole=0.45,
        title="Top 5 Geography Sales"
    )


    fig_geo.update_traces(
        textinfo="label+percent",
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Sales: $%{value:,.2f}<br>"
            "Share: %{percent}"
            "<extra></extra>"
        )
    )


    fig_geo.update_layout(
        paper_bgcolor="#161A23",
        plot_bgcolor="#161A23",
        font_color="white",
        title_font_color="white",
        legend_font_color="white"
    )


    st.plotly_chart(
        fig_geo,
        use_container_width=True
    )


# =========================================================
# SALES TREND
# =========================================================

st.markdown(
    """
    <div class="section-title">
        📅 SALES TREND
    </div>
    """,
    unsafe_allow_html=True
)


if not filtered.empty:

    trend_data = (
        filtered
        .dropna(
            subset=["order_date"]
        )
        .groupby(
            "order_date",
            as_index=False
        )["sales"]
        .sum()
        .sort_values(
            "order_date"
        )
    )


    if not trend_data.empty:

        fig_trend = px.line(
            trend_data,
            x="order_date",
            y="sales",
            markers=True,
            title="Sales Over Time"
        )


        fig_trend.update_traces(
            line={
                "width": 3
            },
            marker={
                "size": 7
            }
        )


        fig_trend.update_layout(
            paper_bgcolor="#161A23",
            plot_bgcolor="#161A23",
            font_color="white",
            title_font_color="white",
            xaxis={
                "gridcolor": "#303746"
            },
            yaxis={
                "gridcolor": "#303746",
                "tickprefix": "$"
            }
        )


        st.plotly_chart(
            fig_trend,
            use_container_width=True
        )


# =========================================================
# CATEGORY ANALYSIS
# =========================================================

st.markdown(
    """
    <div class="section-title">
        📦 CATEGORY ANALYSIS
    </div>
    """,
    unsafe_allow_html=True
)


if not filtered.empty:

    category_data = (
        filtered
        .groupby(
            "category",
            as_index=False
        )
        .agg(
            Sales=("sales", "sum"),
            Profit=("profit", "sum"),
            Quantity=("quantity", "sum")
        )
    )


    category_col1, category_col2 = st.columns(2)


    # =====================================================
    # SALES BY CATEGORY
    # =====================================================

    with category_col1:

        fig_category_sales = px.bar(
            category_data,
            x="category",
            y="Sales",
            title="Sales by Category",
            text_auto=".2s"
        )


        fig_category_sales.update_layout(
            paper_bgcolor="#161A23",
            plot_bgcolor="#161A23",
            font_color="white",
            title_font_color="white",
            xaxis={
                "gridcolor": "#303746"
            },
            yaxis={
                "gridcolor": "#303746",
                "tickprefix": "$"
            }
        )


        st.plotly_chart(
            fig_category_sales,
            use_container_width=True
        )


    # =====================================================
    # PROFIT BY CATEGORY
    # =====================================================

    with category_col2:

        fig_category_profit = px.bar(
            category_data,
            x="category",
            y="Profit",
            title="Profit by Category",
            text_auto=".2s"
        )


        fig_category_profit.update_layout(
            paper_bgcolor="#161A23",
            plot_bgcolor="#161A23",
            font_color="white",
            title_font_color="white",
            xaxis={
                "gridcolor": "#303746"
            },
            yaxis={
                "gridcolor": "#303746",
                "tickprefix": "$"
            }
        )


        st.plotly_chart(
            fig_category_profit,
            use_container_width=True
        )


# =========================================================
# QUANTITY BY CATEGORY
# =========================================================

st.markdown(
    """
    <div class="section-title">
        📦 QUANTITY BY CATEGORY
    </div>
    """,
    unsafe_allow_html=True
)


if not filtered.empty:

    fig_quantity_category = px.bar(
        category_data,
        x="category",
        y="Quantity",
        title="Quantity Sold by Category",
        text_auto=".2s"
    )


    fig_quantity_category.update_layout(
        paper_bgcolor="#161A23",
        plot_bgcolor="#161A23",
        font_color="white",
        title_font_color="white",
        xaxis={
            "gridcolor": "#303746"
        },
        yaxis={
            "gridcolor": "#303746"
        }
    )


    st.plotly_chart(
        fig_quantity_category,
        use_container_width=True
    )


# =========================================================
# AVERAGE SALES BY CATEGORY
# =========================================================

st.markdown(
    """
    <div class="section-title">
        💵 AVERAGE SALES BY CATEGORY
    </div>
    """,
    unsafe_allow_html=True
)


if not filtered.empty:

    average_category = (
        filtered
        .groupby(
            "category",
            as_index=False
        )["sales"]
        .mean()
        .sort_values(
            "sales",
            ascending=False
        )
    )


    fig_average_category = px.bar(
        average_category,
        x="category",
        y="sales",
        title="Average Sales per Order by Category",
        text_auto=".2f"
    )


    fig_average_category.update_layout(
        paper_bgcolor="#161A23",
        plot_bgcolor="#161A23",
        font_color="white",
        title_font_color="white",
        xaxis={
            "gridcolor": "#303746"
        },
        yaxis={
            "gridcolor": "#303746",
            "tickprefix": "$"
        }
    )


    st.plotly_chart(
        fig_average_category,
        use_container_width=True
    )


# =========================================================
# TOP 20 PRODUCTS
# =========================================================

st.markdown(
    """
    <div class="section-title">
        🏆 TOP 20 PRODUCTS BY SALES
    </div>
    """,
    unsafe_allow_html=True
)


if not filtered.empty:

    top_products = (
        filtered
        .groupby(
            "product_name",
            as_index=False
        )["sales"]
        .sum()
        .sort_values(
            "sales",
            ascending=False
        )
        .head(20)
    )


    top_products = top_products.sort_values(
        "sales",
        ascending=True
    )


    fig_products = px.bar(
        top_products,
        x="sales",
        y="product_name",
        orientation="h",
        title="Top 20 Products",
        text_auto=".2s"
    )


    fig_products.update_layout(
        paper_bgcolor="#161A23",
        plot_bgcolor="#161A23",
        font_color="white",
        title_font_color="white",
        xaxis={
            "gridcolor": "#303746",
            "tickprefix": "$"
        },
        yaxis={
            "gridcolor": "#303746"
        },
        height=700
    )


    st.plotly_chart(
        fig_products,
        use_container_width=True
    )


# =========================================================
# PROFIT MARGIN BY CATEGORY
# =========================================================

st.markdown(
    """
    <div class="section-title">
        📈 PROFIT MARGIN BY CATEGORY
    </div>
    """,
    unsafe_allow_html=True
)


if not filtered.empty:

    margin_category = (
        filtered
        .groupby(
            "category",
            as_index=False
        )
        .agg(
            Sales=("sales", "sum"),
            Profit=("profit", "sum")
        )
    )


    margin_category["Profit Margin"] = (
        margin_category["Profit"]
        /
        margin_category["Sales"].replace(
            0,
            pd.NA
        )
    ) * 100


    margin_category = margin_category.dropna(
        subset=["Profit Margin"]
    )


    if not margin_category.empty:

        fig_margin = px.bar(
            margin_category,
            x="category",
            y="Profit Margin",
            title="Profit Margin by Category (%)",
            text_auto=".2f"
        )


        fig_margin.update_layout(
            paper_bgcolor="#161A23",
            plot_bgcolor="#161A23",
            font_color="white",
            title_font_color="white",
            xaxis={
                "gridcolor": "#303746"
            },
            yaxis={
                "gridcolor": "#303746",
                "ticksuffix": "%"
            }
        )


        st.plotly_chart(
            fig_margin,
            use_container_width=True
        )


# =========================================================
# FILTERED DATASET
# =========================================================

st.markdown(
    """
    <div class="section-title">
        📋 FILTERED DATASET
    </div>
    """,
    unsafe_allow_html=True
)


st.dataframe(
    filtered,
    use_container_width=True,
    height=450
)


# =========================================================
# DOWNLOAD
# =========================================================

csv_download = filtered.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    label="⬇️ Download Filtered CSV",
    data=csv_download,
    file_name="amazon_filtered_data.csv",
    mime="text/csv"
)


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Amazon Sales Dashboard • Built with Streamlit & Plotly <br> submitted by Melvin Prasad
    </div>
    """,
    unsafe_allow_html=True
)