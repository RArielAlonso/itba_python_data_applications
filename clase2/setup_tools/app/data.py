import pandas as pd
import requests
from setup_tools import constants

response=requests.get(constants.URL).json()

df1=pd.DataFrame(response['countries'])

df1['country-capital']=df1['name']+'-'+df1['capital']

print('Generating Exce')
df1.to_excel('./setup_tools/country_capitals.xlsx')
print('Process Finished')