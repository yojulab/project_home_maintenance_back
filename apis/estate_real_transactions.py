# 국토교통부 실거래가 정보 조회 서비스
## setup pip : https://pypi.org/project/PublicDataReader/
# [ERROR] 아파트 전월세 202101 조회 오류
# [ERROR] 아파트 전월세 조회 서비스 오류 - (99) SERVICE ACCESS DENIED ERROR.
# [ERROR] 오피스텔 전월세 조회 서비스 오류 - (99) SERVICE ACCESS DENIED ERROR.
# [ERROR] 단독다가구 전월세 조회 서비스 오류 - (99) DEADLINE HAS EXPIRED ERROR.
# [ERROR] 연립다세대 전월세 조회 서비스 오류 - (99) DEADLINE HAS EXPIRED ERROR.
# [ERROR] 공장창고등 매매 조회 서비스 오류 - (99) SERVICE ACCESS DENIED ERROR.


# ['지역코드', '법정동', '주택유형', '건축년도', '대지면적', '연면적', '년', '월', '일', '거래금액',
#        '거래유형', '중개사소재지', '해제사유발생일', '해제여부']

# ['지역코드', '시군구', '법정동', '유형', '용도지역', '건물주용도', '건축년도', '층', '대지면적',
#        '건물면적', '구분', '년', '월', '일', '거래금액', '거래유형', '중개사소재지', '해제사유발생일',
#        '해제여부']

# ['지역코드', '도로명', '법정동', '지번', '아파트', '건축년도', '층', '전용면적', '년', '월', '일',
#        '거래금액', '도로명건물본번호코드', '도로명건물부번호코드', '도로명시군구코드', '도로명일련번호코드',
#        '도로명지상지하코드', '도로명코드', '법정동본번코드', '법정동부번코드', '법정동시군구코드', '법정동읍면동코드',
#        '법정동지번코드', '일련번호', '거래유형', '중개사소재지', '해제사유발생일', '해제여부']

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
df_commons = pd.read_sql('select * from commoncode_estate_real_transaction order by serviceName', con=engine)

# 4. 지역코드(시군구코드) 검색하기
sigunguName = "심곡본동"                            # 시군구코드: 41190
code = pdr.code_bdong()
code.loc[(code['시군구명'].str.contains(sigunguName, na=False)) &
         (code['읍면동명'].isna())]

# 6. 지역, 기간 별 데이터 프레임 만들기
sigunguCode="41190"
startYearMonth="202101"
endYearMonth="202102"

# def add_column_and_samevalue():


for index, row in df_commons.iterrows():
    category = row['categoryName']       # 부동산 상품 종류 (ex. 아파트, 오피스텔, 단독다가구 등)
    item = row['itemName']        # 부동산 거래 유형 (ex. 매매, 전월세)
    df = ts.collect_data(category, item, sigunguCode, startYearMonth, endYearMonth)
    if not isinstance(df, str) and not df.empty:
        try:
            df['categoryName'] = category
            df['itemName'] = item

            df.to_sql('estate_real_transaction', con=engine, if_exists='append', index=False)
        except :
            data = pd.read_sql('SELECT * FROM estate_real_transaction', con=engine)
            df2 = pd.concat([data,df])
            df2.to_sql(name='estate_real_transaction', con=engine, if_exists = 'replace', index=False)
pass