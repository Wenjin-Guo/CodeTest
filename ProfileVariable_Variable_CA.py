import pandas as pd

#import file
file = pd.read_excel('C:\Users\simon guo\OneDrive - Environics Analytics\Documents\Presentation\Profile - Variable vs Variable(py).xlsx',sheet_name='Sheet1')






#Export to Excel file
file.to_excel('NewProfileVariable_Variable.xlsx',index=0)