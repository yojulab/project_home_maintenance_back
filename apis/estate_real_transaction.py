# 국토교통부 실거래가 정보 조회 서비스
## setup pip : https://pypi.org/project/PublicDataReader/
# 1. 라이브러리 임포트하기
import PublicDataReader as pdr
# print(pdr.__version__)

# 2. 공공 데이터 포털 OpenAPI 서비스 인증키 입력하기
serviceKey = "BoygPZjC27pxm92hSposjnSob2u36vziS1rzIzxkrL9QxmlhB0SMARwLfNlBE3wrE7nnw34zLmmv0a6amvW4xg%3D%3D"

# 3. 국토교통부 실거래가 정보 조회 OpenAPI 세션 정의하기
# debug: True이면 모든 메시지 출력, False이면 오류 메시지만 출력 (기본값: False)
ts = pdr.Transaction(serviceKey, debug=True)

import sqlite3
database = "./db.sqlite3"
engine = sqlite3.connect(database)
import pandas as pd
df_commons = pd.read_sql('select * from common_codes order by serviceName', con=engine)

# 4. 지역코드(시군구코드) 검색하기
sigunguName = "심곡본동"                            # 시군구코드: 41190
code = pdr.code_bdong()
code.loc[(code['시군구명'].str.contains(sigunguName, na=False)) &
         (code['읍면동명'].isna())]

# 6. 지역, 기간 별 데이터 프레임 만들기
sigunguCode="41190"
startYearMonth="202101"
endYearMonth="202102"

for index, row in df_commons.iterrows():
    prod =row['categoryName']       # 부동산 상품 종류 (ex. 아파트, 오피스텔, 단독다가구 등)
    trans = row['itemName']        # 부동산 거래 유형 (ex. 매매, 전월세)
    df = ts.collect_data(prod, trans, sigunguCode, startYearMonth, endYearMonth)
    if not isinstance(df, str) and not df.empty:
        try:
            df.to_sql('estate_real_transaction', con=engine, if_exists='append')
        except :
            # df.to_sql('estate_real_transaction', con=engine, if_exists='replace')
            pass

pass