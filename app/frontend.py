import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime
import json
import requests

st.set_page_config(
        page_title="С ветерком",
        page_icon="🌬️",
        layout="wide"
    )

def main():

    st.markdown("# С ветерком 🌬️")
    st.sidebar.markdown("# Главная страница")

    col1, col2, col3 = st.columns(3, gap="small")
    with col1:
        dep_city = st.selectbox(
        'Город вылета',
        ('Kolkata','Banglore', 'Delhi', 'Chennai', 'Mumbai'))

    with col2:
        dest_city = st.selectbox(
            "Город прилета:",
            ('New Delhi', 'Banglore', 'Cochin', 'Kolkata', 'Delhi', 'Hyderabad')
        )
    
    cont = st.container()
    with col1:
        departure_d = st.date_input("Дата вылета:", value=None, format="YYYY.MM.DD")
        
        
    if st.button("Найти рейсы"):
        button_click(dep_city, dest_city, departure_d, cont)



def create_cost_info_field(index, field, date):

    prim_col1, prim_col2 = st.columns(2, gap="small")

    with prim_col1:
        with st.form(f"Окно с билетом: {index}"):
            
            col1, col2 = st.columns(2, gap="medium")
            with col1:
                st.write(f"Дата вылета: {date}")

                airline = field["airline"]
                st.write(f"Авиакомпания: {airline}")
                
                cost = field['cost'] * 1.08
                st.write(f"Цена: {cost} ₽")
            
            with col2:
                st.form_submit_button(f"Купить билет с позицией: {index}")

def button_click(city1, city2, date, cont):
    
    url = f'https://airfare-predictor-production-856d.up.railway.app/v1/api/data?departure={city1}&destination={city2}&depdate={date}&info=no-info'
    response = requests.get(url)
    data = response.json()
    with cont:
        counter = 1
        for field in data['prices']:
            create_cost_info_field(counter, field, date)
            counter += 1

if __name__ == "__main__":
    main()

