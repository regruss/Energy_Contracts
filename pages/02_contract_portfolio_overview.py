# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 13:58:25 2023

@author: regru
"""


import pandas as pd
import streamlit as st
import plotly.express as px


# https://streamlit.io/gallery
# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="Contract Portfolio Overview",layout="wide",page_icon=":bar_chart:")
# Insert into DF
contract_df = pd.read_csv(r'energy_contract_dash_df.csv')[['Effective_Date','Acres','Term_Length','Royalty','Pooling','Pooling_Favorability','Lessor_Name','Lessor_Address','Lessee_Name','Lessee_Address','File_Name']]
# Title
st.title(":bar_chart: Contract Language Portfolio Overview")

# Sidebar filtering
st.sidebar.header("Filters:")
fn = st.sidebar.multiselect("Search by File Name",options=contract_df['File_Name'].unique(),default=contract_df['File_Name'].iloc[0])
df_selection = contract_df.query("File_Name == @fn")
st.dataframe(df_selection)

# Sort DF
col = st.sidebar.multiselect("Select a Column",options=['Term_Length','Royalty','Pooling','Pooling_Favorability'],default='Pooling')
val = st.sidebar.multiselect("Select Columns to Filter On",options=list(contract_df['Pooling'].unique()),default=list(contract_df['Pooling'].unique())[0])
search_df = contract_df[contract_df[col[0]].isin(val[:])]
st.dataframe(search_df)
contract_df['Term_Length'].unique()
##################### Statistics ############################################
########## Indemnity
# Royalty
indem1 = len(contract_df[contract_df['Royalty'] == '30%'].values)/len(contract_df)
indem2 = len(contract_df[contract_df['Royalty'] == '1/8'].values)/len(contract_df)
indem3 = len(contract_df[contract_df['Royalty'] == '1/4'].values)/len(contract_df)
########## Patents
# Term Length %
pat1 = len(contract_df[contract_df['Term_Length'] == '3 years'].values)/len(contract_df)
pat2 = len(contract_df[contract_df['Term_Length'] == '1 year'].values)/len(contract_df)
pat3 = len(contract_df[contract_df['Term_Length'] == '180 days'].values)/len(contract_df)
########## Subject Injury
# Pooling %
sub1 = len(contract_df[contract_df['Pooling_Favorability'] == 'Lessor'].values)/len(contract_df)
sub2 = len(contract_df[contract_df['Pooling_Favorability'] == 'Neutral'].values)/len(contract_df)
sub3 = len(contract_df[contract_df['Pooling_Favorability'] == 'Lessee'].values)/len(contract_df)

st.header('Portfolio Overview')
# Plot
fig1 = px.pie(values=[indem1,indem2,indem3],names=['30%','1/8','1/4'],title='<b>Royalty</b>',color_discrete_sequence=["green", "red", "blue"],hole=0.3)
fig2 = px.pie(values=[pat1,pat2,pat3],names=['3 Years','1 Year','180 Days'],title='<b>Term Length</b>',color_discrete_sequence=["green", "red", "blue"],hole=0.3)
fig3 = px.pie(values=[sub1,sub2,sub3],names=['Lessor','Neutral','Lessee'],title='<b>Pooling Favorability</b>',color_discrete_sequence=["green", "red", "blue"],hole=0.3)
st.plotly_chart(fig1)
st.plotly_chart(fig2)
st.plotly_chart(fig3)











































































