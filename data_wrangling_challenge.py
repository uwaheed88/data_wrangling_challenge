import pandas as pd

daily_price = pd.read_excel("https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDd.xls",  sheet_name='Data 1', skiprows=[0, 1, 2])

daily_price.to_csv('daily/data/daily_gas_price.csv', encoding='utf-8', index=False, header=['date', 'price'])

weekly_price = pd.read_excel("https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDw.xls",  sheet_name='Data 1', skiprows=[0, 1, 2])
weekly_price.to_csv('weekly/data/weekly_gas_price.csv',encoding='utf-8', index=False, header=['date', 'price'])

monthly_price = pd.read_excel("https://www.eia.gov/dnav/ng/hist_xls/RNGWHHDm.xls",  sheet_name='Data 1', skiprows=[0, 1, 2])
monthly_price.to_csv('monthly/data/monthly_gas_price.csv',encoding='utf-8', index=False, header=['date', 'price'])
