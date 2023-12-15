import datetime
import time
import numpy as np, pandas as pd, streamlit as st

# Configure page
st.set_page_config(
    page_title="Purchase ticket",
    page_icon="🎫",
    layout='wide'
)


def main():

    st.markdown("# Available tickets 🎫")
    st.sidebar.markdown("# Tickets section")

    with st.form("Окно с самым дешевым билетом"):
        
        col1, col2 = st.columns(2, gap="small")
        
        with col1:
            price = 4320
            st.write(f"{price} ₽")

            if st.form_submit_button("Купить"):
                buy_ticket()
        with col2:
            
            sub_col1, sub_col2 = st.columns(2, gap="medium")
            
            with sub_col1:
                dep_date = datetime.date.today()
                st.write(f"Дата вылета: {dep_date}")

            with sub_col2:
                arr_date = datetime.date.today()
                st.write(f"Дата прибытия: {arr_date}")
    

def buy_ticket():
    st.write("Билет куплен")

if __name__ == "__main__":
    main()