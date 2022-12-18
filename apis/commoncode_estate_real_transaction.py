import pandas as pd

# 국토교통부 실거래가 정보 조회 서비스
# from https://pypi.org/project/PublicDataReader/ > 1) 국토교통부 실거래가 정보 조회 서비스
df = pd.read_csv('./apis/commoncode_estate_real_transaction.csv')
# rename 서비스명, 상품유형, 거래유형
df.columns=['serviceName', 'categoryName', 'itemName']
pass

import sqlite3
database = "./db.sqlite3"
engine = sqlite3.connect(database)
df.to_sql('commoncode_estate_real_transaction', con=engine, if_exists='replace')
pass

df_commons = pd.read_sql('select * from commoncode_estate_real_transaction', con=engine)
pass