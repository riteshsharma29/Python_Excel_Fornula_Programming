#!/usr/bin/python

import pandas as pd

df = pd.read_excel('sales-funnel.xlsx')

pvt_table = pd.pivot_table(df,index=["Name","Price"])

pvt_table.to_excel('result_pivot.xlsx')



