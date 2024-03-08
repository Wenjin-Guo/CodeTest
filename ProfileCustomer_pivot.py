import pandas as pd
import matplotlib.pylab as plt


#reference workbook
fileName = "Sample_Customer_File - 5K_W_All_Additional_Types.csv"
#headers = ["UniqueID","Postal Code","City","StoreCode","CustomerWeight","Dollars","Member Type","Some Text","Flag"]
df = pd.read_csv(fileName)
print(df.head())
#table = pd.pivot_table(df,)