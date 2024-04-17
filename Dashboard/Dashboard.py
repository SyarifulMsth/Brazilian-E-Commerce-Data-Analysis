import pandas as pd
import seaborn as sns
import streamlit as st
import matplotlib.pyplot as plt
from babel.numbers import format_currency

st.set_page_config(page_title='Brazillian E-Commerce Data Analysis',page_icon='./icons/icons.png')
st.markdown("<h1 style='text-align: center;'>Brazillian E-Commerce <br>Data Analysis 🛒 </h1>", unsafe_allow_html=True)

# read dataset
all_df = pd.read_csv("./Dashboard/dataset/All_Data_Brazilian_ECommerce.csv")

# Market Segmentation by Customers
# Market Segmentation by Customers
# Market Segmentation by Customers

def create_segmentation_customer_city_df(df):
    segmentation_customer_city_df = all_df.groupby(by="customer_city").agg({"customer_id": "nunique"}).sort_values(by="customer_id", ascending=False)
    segmentation_customer_city_df = segmentation_customer_city_df.reset_index()
    segmentation_customer_city_df.head()

    return segmentation_customer_city_df

def create_segmentation_customer_state_df(df):
    segmentation_customer_state_df = all_df.groupby(by="customer_state").agg({"customer_id": "nunique"}).sort_values(by="customer_id", ascending=False)
    segmentation_customer_state_df = segmentation_customer_state_df.reset_index()
    segmentation_customer_state_df.head()

    return segmentation_customer_state_df

# Market Segmentation by Sellers
# Market Segmentation by Sellers
# Market Segmentation by Sellers
def create_segmentation_seller_city_df(df):
    segmentation_seller_city_df = all_df.groupby(by="seller_city").agg({"seller_id": "nunique"}).sort_values(by="seller_id", ascending=False)
    segmentation_seller_city_df = segmentation_seller_city_df.reset_index()
    segmentation_seller_city_df.head()

    return segmentation_seller_city_df

def create_segmentation_seller_state_df(df):
    segmentation_seller_state_df = all_df.groupby(by="seller_state").agg({"seller_id": "nunique"}).sort_values(by="seller_id", ascending=False)
    segmentation_seller_state_df = segmentation_seller_state_df.reset_index()
    segmentation_seller_state_df.head()

    return segmentation_seller_state_df

segmentation_customer_city_df = create_segmentation_customer_city_df(all_df)
segmentation_customer_state_df = create_segmentation_customer_state_df(all_df)
segmentation_seller_city_df = create_segmentation_seller_city_df(all_df)
segmentation_seller_state_df = create_segmentation_seller_state_df(all_df)

# Data visualization
# Data visualization
# Data visualization
st.subheader("Market Segmentation📊")

# Market Segmentation by Customers
# Market Segmentation by Customers
# Market Segmentation by Customers
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

colors = ["#06D6A0", "#118AB2", "#118AB2", "#118AB2", "#118AB2"]

sns.barplot(x="customer_id", y="customer_city", data=segmentation_customer_city_df.sort_values(by="customer_id", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Market Segmentation by City Location", loc="center", fontsize=15)
ax[0].tick_params(axis ='x', labelsize=15)
ax[0].tick_params(axis ='y', labelsize=15)

sns.barplot(x="customer_id", y="customer_state", data=segmentation_customer_state_df.sort_values(by="customer_id", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=15)
ax[1].tick_params(axis='x', labelsize=15)
ax[1].tick_params(axis='y', labelsize=15)

plt.suptitle("Market Segmentation by Customers", fontsize=20)
plt.show()

st.pyplot(fig)

# Market Segmentation by Sellers
# Market Segmentation by Sellers
# Market Segmentation by Sellers
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(24, 6))

sns.barplot(x="seller_id", y="seller_city", data=segmentation_seller_city_df.sort_values(by="seller_id", ascending=False).head(5), palette=colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("Market Segmentation by City Location", loc="center", fontsize=15)
ax[0].tick_params(axis ='x', labelsize=15)
ax[0].tick_params(axis ='y', labelsize=15)

sns.barplot(x="seller_id", y="seller_state", data=segmentation_seller_state_df.sort_values(by="seller_id", ascending=False).head(5), palette=colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].invert_xaxis()
ax[1].yaxis.set_label_position("right")
ax[1].yaxis.tick_right()
ax[1].set_title("Worst Performing Product", loc="center", fontsize=15)
ax[1].tick_params(axis='x', labelsize=15)
ax[1].tick_params(axis='y', labelsize=15)

plt.suptitle("Market Segmentation by Sellers", fontsize=20)
st.pyplot(fig)


# Order Status Performance
# Order Status Performance
# Order Status Performance
def create_order_status_performance_df(df):
    order_status_performance_df = all_df.groupby('order_status').agg({"order_id": "nunique"}).sort_values(by="order_id",ascending=False)
    order_status_performance_df = order_status_performance_df.reset_index()
    order_status_performance_df.head()

    return order_status_performance_df

order_status_performance_df = create_order_status_performance_df(all_df)

# Data visualization
# Data visualization
# Data visualization
st.subheader("Order Status Performance📊")
colors = ["#06D6A0", "#118AB2", "#118AB2", "#118AB2", "#118AB2"]
plt.figure(figsize=(10, 5))
sns.barplot(
    x="order_id",
    y="order_status",
    data=order_status_performance_df.sort_values(by="order_id", ascending=False),
    palette=colors
)
plt.title("Order Status Performance", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
st.pyplot(plt)


# Payment Type Trend
# Payment Type Trend
# Payment Type Trend
def create_order_payments_trends_df(df):
    order_payments_trends_df = all_df.groupby('payment_type').agg({"order_id": "nunique"}).sort_values(by="order_id",ascending=False)
    order_payments_trends_df = order_payments_trends_df.reset_index()
    order_payments_trends_df.head()

    return order_payments_trends_df

order_payments_trends_df = create_order_payments_trends_df(all_df)

# Data visualization
# Data visualization
# Data visualization
st.subheader("Payment Types Trend📊")
colors = ["#06D6A0", "#118AB2", "#118AB2", "#118AB2", "#118AB2"]

plt.figure(figsize=(10, 5))
sns.barplot(
    x="order_id",
    y="payment_type",
    data=order_payments_trends_df.sort_values(by="order_id", ascending=False),
    palette=colors
)
plt.title("Payments Type Trend", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
st.pyplot(plt)


# Customer Satisfaction
# Customer Satisfaction
# Customer Satisfaction
def create_customers_rating_df(df):
    customers_rating_df = all_df.groupby(by=['review_score'])['customer_id'].size().reset_index().sort_values(ascending=False, by='customer_id')

    return customers_rating_df

customers_rating_df = create_customers_rating_df(all_df)

# Data visualization
# Data visualization
# Data visualization
st.subheader("Customers Satisfaction📊")
colors2 = ["#118AB2", "#118AB2", "#118AB2", "#118AB2", "#06D6A0"]
plt.figure(figsize=(10, 5))
sns.barplot(
    y="customer_id",
    x="review_score",
    data=customers_rating_df.sort_values(by="customer_id", ascending=False),
    palette=colors2
)
plt.title("Customer Satisfaction", loc="center", fontsize=15)
plt.ylabel(None)
plt.xlabel(None)
plt.tick_params(axis='y', labelsize=12)
st.pyplot(plt)

datetime_columns = ["order_purchase_timestamp"]
all_df.sort_values(by="order_purchase_timestamp", inplace=True)
all_df.reset_index(inplace=True)

for column in datetime_columns:
    all_df[column] = pd.to_datetime(all_df[column])

# Filter data
min_date = all_df["order_purchase_timestamp"].min()
max_date = all_df["order_purchase_timestamp"].max()

# RFM Analysis
# RFM Analysis
# RFM Analysis
def create_rfm_df(df):
    rfm_df = all_df.groupby(by="customer_id", as_index=False).agg({
        "order_purchase_timestamp": "max",  # mengambil tanggal order terakhir
    })
    rfm_df.columns = ["customer_id", "max_order_timestamp"]

    # frequency
    frequency = all_df.groupby('customer_id')['order_id'].count()

    # monetary
    monetary = all_df.groupby('customer_id')['price'].sum()

    # menghitung kapan terakhir pelanggan melakukan transaksi (hari)
    rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
    recent_date = all_df["order_purchase_timestamp"].dt.date.max()
    recency = rfm_df["max_order_timestamp"].apply(lambda x: (recent_date - x).days)
    rfm_df.drop("max_order_timestamp", axis=1, inplace=True)

    rfm_df = pd.DataFrame({
        'customer_id': recency.index,
        'recency': recency.values,
        'frequency': frequency.values,
        'monetary': monetary.values
    })

    return rfm_df

rfm_df = create_rfm_df(all_df)

# Data visualization
# Data visualization
# Data visualization
st.subheader("RFM Analysis📊")
fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 6))

recency_colors = ["#06D6A0", "#118AB2", "#118AB2", "#118AB2", "#118AB2"]
frequency_colors = ["#118AB2", "#06D6A0", "#118AB2", "#118AB2", "#118AB2"]
monetary_colors = ["#06D6A0", "#118AB2", "#118AB2", "#118AB2", "#118AB2"]

sns.barplot(y="recency", x="customer_id", data=rfm_df.sort_values(by="recency", ascending=True).head(5), palette=recency_colors, ax=ax[0])
ax[0].set_ylabel(None)
ax[0].set_xlabel(None)
ax[0].set_title("By Recency (days)", loc="center", fontsize=18)
ax[0].tick_params(axis ='x', labelsize=15)
ax[0].tick_params(axis='y', labelsize=15)

sns.barplot(y="frequency", x="customer_id", data=rfm_df.sort_values(by="frequency", ascending=False).head(5), palette=frequency_colors, ax=ax[1])
ax[1].set_ylabel(None)
ax[1].set_xlabel(None)
ax[1].set_title("By Frequency", loc="center", fontsize=18)
ax[1].tick_params(axis='x', labelsize=15)
ax[1].tick_params(axis='y', labelsize=15)

sns.barplot(y="monetary", x="customer_id", data=rfm_df.sort_values(by="monetary", ascending=False).head(5), palette=monetary_colors, ax=ax[2])
ax[2].set_ylabel(None)
ax[2].set_xlabel(None)
ax[2].set_title("By Monetary", loc="center", fontsize=18)
ax[2].tick_params(axis='x', labelsize=15)
ax[2].tick_params(axis='y', labelsize=15)

plt.suptitle("Best Customer Based on RFM Parameters (customer_id)", fontsize=25)
st.pyplot(plt)

# Footer
st.caption('Copyright © Syariful Musthofa 2023⚡')
