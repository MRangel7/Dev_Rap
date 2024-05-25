import pandas as pd

df = pd.read_excel(
        io='empresas_combined.xlsx',
        engine='openpyxl',
        sheet_name='Sheet1',
        nrows=14375,
    )

print(df)