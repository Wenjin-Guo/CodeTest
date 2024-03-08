import pandas as pd
import matplotlib.pylab as plt


#reference workbook
fileName = "Import_COORD_CAN_-_5K_with_all_CTG_Special_Char.csv"
#headers = ["UniqueID","Postal Code","City","StoreCode","CustomerWeight","Dollars","Member Type","Some Text","Flag"]
df = pd.read_csv(fileName)
print(df.head())
table = pd.pivot_table(df[df.__PRIZM!='Not Coded'],values='Count',index='__PRIZM',aggfunc="sum")
print(table)
table.to_csv("pivot_table.csv")