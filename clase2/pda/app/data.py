import pandas as pd
from pda import constants

df=pd.DataFrame([('a',1),('b',None)],
             columns=constants.COLUMNS)


print(df)