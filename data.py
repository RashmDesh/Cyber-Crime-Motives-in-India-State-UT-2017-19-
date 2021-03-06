'''@Author : Rashmi Deshmukh'''
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


html_temp=""" <div style="background-color:tomato;padding:10px"> """
st.markdown(html_temp,unsafe_allow_html=True)
#st.title("Cyber Crime Motives In India(State/UT)")
new_title = '<p style="font-family:sans-serif; color:Green; font-size: 42px;">Cyber Crime Motives In India(State/UT)</p>'
st.markdown(new_title, unsafe_allow_html=True)
st.markdown(html_temp,unsafe_allow_html=True)

Motives_data= pd.read_csv('Motives.csv')
st.title("From 2017-2019 State/UT wise Cyber Crime Motives Count Rate :")
three_year_total=Motives_data.groupby(['State/UT'])['Total'].sum()
st.bar_chart(three_year_total,use_container_width=True)
st.markdown("* State/UT having maximum cyber crime accoring to Motives (2017-2019) is :")
three_year_total=three_year_total.to_frame(name="Total").reset_index()
#State/UT having maximum and mimimum cyber crime motives total
st.table(three_year_total[three_year_total["Total"]==(three_year_total["Total"].max())])
st.markdown("* State/UT having minimum cyber crime according to Motives (2017-2019) is :")
st.table(three_year_total[three_year_total["Total"]==(three_year_total["Total"].min())])

st.markdown(html_temp,unsafe_allow_html=True)

st.title("* Cyber Crime Motives")
data=Motives_data.drop(["S. No","Category","State/UT","Total","Year","Unnamed: 0"],axis=1)
motives_total=data.sum(axis=0,skipna=True)
st.bar_chart(motives_total,use_container_width=True)
st.table(motives_total)
st.markdown("* Fraud  which having maximum crime motives in year 2017 to 2019.")
st.markdown("* Terrorist Activities - Terrorist Funding which having minimum crime motives in year 2017 to 2019")
st.markdown(html_temp,unsafe_allow_html=True)

st.title("Indian State/UT details by your selected cyber crime motive :")
option=st.selectbox("Select Motive from following drop down list?",(
"Personal Revenge",	"Anger","Fraud","Extortion","Causing Disrepute","Prank","Sexual Exploitation","Political Motives","Terrorist Activities (Total))","Inciting Hate against Country","Disrupt Public Service",	"Sale purchase Illegal drugs","Developing own business","Spreading Piracy","Psycho or Pervert","Steal Information","Abetment to Suicide","Others"))
st.write('State/UT wise graph for your selected Motives : :', option)
#from 2017-2019 Fraud Motives satae/UT wise
motives_value=Motives_data.groupby(['State/UT'])[option].sum().to_frame(name="Total")
st.bar_chart(motives_value,use_container_width=True)

st.markdown(html_temp,unsafe_allow_html=True)

st.title("Cyber Crime Motives In India For Your Selected State/UT and year:")

State_option=st.selectbox("Select State/UT?",("Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh",
"Goa","Gujarat","Haryana","Himachal Pradesh","Jammu & Kashmir","Jharkhand",
"Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya",
 "Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu",
 "Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal","A&N Islands",
 "Chandigarh","D&N Haveli","Daman & Diu","Delhi","Lakshadweep","Puducherry"))

Year_option=st.selectbox("Select Year?",(2017,2018,2019))
#cyber crime motives details for specified State/UT and year
state_year=Motives_data[(Motives_data["State/UT"]==State_option) & (Motives_data["Year"]==Year_option)]
state_year=state_year.drop(['Unnamed: 0','S. No'], axis=1)
st.write('Your Selected State/UT:', State_option)
st.write('Your Selected Year:', Year_option)
st.write('Cyber Crime Motives Details:-')
state_year
state_year=state_year.drop(['Total','Year','Category','State/UT'], axis=1)
state_year=state_year.T
st.bar_chart(state_year)
st.markdown("***")

st.subheader("Thank You!")
