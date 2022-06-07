import streamlit as st
import pandas as pd
import os

st.markdown("# Trades")
st.sidebar.markdown("## Trades")

if os.path.isfile("data/orders.csv"):
  df = pd.read_csv("data/orders.csv")
else:
  d = { "ticker": [], "quantity": [], "order_date": [], "price": [], "order_type": [] }
  df = pd.DataFrame(data=d)

with st.form("my_form"):
  st.write("Nova ordem")
  ticker = st.text_input("Ticker")
  quantity = st.number_input("Quantidade", 0)
  order_date = st.date_input("Data da ordem")
  price = st.number_input("Preço")
  order_type = st.selectbox("Tipo da ordem", ("Compra", "Venda"))

  submitted = st.form_submit_button("Submit")
  if submitted:
    st.write(ticker, quantity, order_date, price, order_type)
    d = { "ticker": [ticker], "quantity": [quantity], "order_date": [order_date], "price": [price], "order_type": [order_type] }
    df_new = pd.DataFrame(data=d)
    df = pd.concat([df, df_new])
    
    df.to_csv("data/orders.csv", index=False)


st.dataframe(df.astype(str))
