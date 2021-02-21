import pandas as pd

cols = ['Arrestee' ,'Home City' ,'Home State' ,'Offense Date' ,'Arrest Date' ,'Code' ,'Case Type' ,'Class' ,'Charge' ,'Next Hearing Date' ,'Final Status']
data = pd.read_csv("ARRESTED PROTESTERS - Redacted.csv", skip_blank_lines=True)

print(data)
