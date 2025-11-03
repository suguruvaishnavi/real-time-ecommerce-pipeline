import pandas as pd

data = {
    "Student Names" : ['Vaishnavi','Shravanthy','Madhavi','Suresh'],
    "Age": [30,36,60,65],
    "Grade": ["A","B","C","D"]
}
df = pd.DataFrame(data)
print(df)