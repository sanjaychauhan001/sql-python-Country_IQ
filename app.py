import streamlit as st
from dbhelper import DB
import plotly.express as px
db = DB()

st.title("COUNTRY IQ ANALYSIS")

btn1 = st.button("Show analysis")

if btn1:
    country, iq = db.show_country_map()
    fig = px.choropleth(locations=country,locationmode='country names',
                    color=iq,
                    title='Average IQ by Country')
    st.plotly_chart(fig)    


    Avg_schooling, Average_IQ, Country = db.show_schooling()
    fig2 = px.scatter(x=Avg_schooling, y=Average_IQ, color=Country,
                      title="Relation between schooling and IQ")
    fig2.update_layout(xaxis_title="Average schooling", yaxis_title="Avegare IQ")
    st.plotly_chart(fig2)


    literacy_rate, avg_iq, country_name = db.show_literacy_rate()
    fig3 = px.scatter(x=literacy_rate, y=avg_iq, color=country_name,
                      title="Relation between literacy_rate and IQ")
    fig3.update_layout(xaxis_title="Literacy_Rate", yaxis_title="Avegare IQ")
    st.plotly_chart(fig3)


    Country_Name, Nobel_Prices = db.show_nobel_prices()
    fig4 = px.bar(x=Country_Name, y=Nobel_Prices,
                  title="Top 5 country with highest nobel prices")
    fig4.update_layout(xaxis_title="country name", yaxis_title="nobel prices")
    st.plotly_chart(fig4)