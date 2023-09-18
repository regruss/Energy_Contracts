# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 20:38:01 2023

@author: regru
"""
import os
import json
import numpy as np
import pandas as pd
import glob
import re
import io
import streamlit as st



# https://streamlit.io/gallery
# Find emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
def main():
    st.set_page_config(page_title="Contract Data Extraction",page_icon=":house:")
    st.header("Extract Data From Your Contracts")
    pdf_files = st.file_uploader("Upload Files", accept_multiple_files=True, type="pdf")
    # Extract Data
    if bool(pdf_files):
        st.header('Contract Data Preview')
        # Insert into DF
        contract_df = pd.read_csv(r'energy_contract_dash_df.csv')
        st.write(contract_df)
if __name__== '__main__':
    main()