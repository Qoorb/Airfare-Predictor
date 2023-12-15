import streamlit as st
import numpy as np
import pandas as pd
import time
import datetime

#Configure page
st.set_page_config(
        page_title="Tomsk airlines",
        page_icon="🛫",
        layout="wide"
    )

def main():
    '''Здесь задается конфигурация страницы, необходимые поля, 
    небольшая логика, которая обеспечивает, чтобы переданные данные о
    времени вылета и прилета будут адекватны, то есть не получится такого,
    что сотрудник выберит дату прилета, который будет проходить раньше вылета.'''

    # Отображаем заголовок странице в секции вкладок
    st.markdown("# Tomsk airlines 🛫")
    st.sidebar.markdown("# Главная страница")

    # Поля, для ввода информации будут распределяться по трем колонкам, 
    # с небольшим интервалом между друг другом
    col1, col2, col3 = st.columns(3, gap="small")
    # Первая колонка, в которой выбирается город вылета
    with col1:
        dep_city = st.selectbox(
        'Укажите свой город отправления',
        ('Томск', 'Новосибирск'))

        st.write('Город отправления:', dep_city)
    # Вторая колонка, в которой выбирается город назначения
    with col2:
        dest_city = st.selectbox(
            "Укажите город назначения:",
            ("Санкт-Петербург", "Москва", "Хабаровск", 
            "Иркутск", "Благовещенск", "Нерюнгри", "Мирный",
            "Южно-Сахалинск", "Петропавловск-Камчатский")
        )
        st.write('Город отправления:', dest_city)

    
    # Массив c датой отправления и датой вылета обратно
    dates = []

    with col3:
        
        sub_col1, sub_col2 = st.columns(2, gap="small")
        
        with sub_col1:
            departure_d = st.date_input("Дата вылета:", value=None, format="DD.MM.YYYY")
            dates.append(departure_d)
        
        with sub_col2:
            arrival_d = st.date_input("Дата прилета:",value=None, min_value=departure_d, format="DD.MM.YYYY")
            dates.append(arrival_d)

            # После нажатия на кнопку, все необходимые данные отправляются в метод button_click,
            # Откуда они будут отправлены куда надо
            if st.button("Найти"):
                with col1:
                    button_click(dep_city, dest_city, dates)

    # Отображаем графики
    display_charts()


def display_charts():
    '''Функция вызывается для последовательно отображения двух графиков.
       Графики отображаются независимо от выбранных данных, 
       сразу после создания полей и кнопки, необходимых, для заполнения данных. '''
    
    with st.container():
        st.write("График изменения цен на авиабилеты для каждой авиакомпании")
        chart_data = pd.DataFrame(
            np.random.randn(20, 2),
            columns=['S7', 'Аэрофлот'])  
        
        st.line_chart(chart_data)

    with st.container():
        chart_data = pd.DataFrame(np.random.randn(20, 2), columns=["s7", "Аэрофлот"])

        st.bar_chart(chart_data)

def button_click(city1, city2, dates):
    '''Кнопка нужна для того, чтобы отправлять информацию 
    о выбранном времени вылета/прилета в базу данных.'''
    if (dates[0] != None and dates[1] != None):
        st.write(city1, city2, *dates)


if __name__ == "__main__":
    '''Запуск программы'''
    main()