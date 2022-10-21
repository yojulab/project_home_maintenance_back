# 국토교통부 실거래가 정보 조회 서비스
## setup pip : https://pypi.org/project/PublicDataReader/
# 1. 라이브러리 임포트하기
import PublicDataReader as pdr
print(pdr.__version__)

# 2. 공공 데이터 포털 OpenAPI 서비스 인증키 입력하기
serviceKey = ""

# 3. 국토교통부 실거래가 정보 조회 OpenAPI 세션 정의하기
# debug: True이면 모든 메시지 출력, False이면 오류 메시지만 출력 (기본값: False)
ts = pdr.Transaction(serviceKey, debug=True)

# 4. 지역코드(시군구코드) 검색하기
sigunguName = "분당구"                              # 시군구코드: 41135
sigunguName = "심곡본동"                            # 시군구코드: 4119011100
code = pdr.code_bdong()
code.loc[(code['시군구명'].str.contains(sigunguName, na=False)) &
         (code['읍면동명'].isna())]

# 5. 지역, 월 별 데이터 프레임 만들기
prod="아파트"                                           # 부동산 상품 종류 (ex. 아파트, 오피스텔, 단독다가구 등)
trans="매매"                                            # 부동산 거래 유형 (ex. 매매, 전월세)
sigunguCode="41135"
sigunguCode="41190"
yearMonth="202101"

df = ts.read_data(prod, trans, sigunguCode, yearMonth)
print(df)
pass

# 6. 지역, 기간 별 데이터 프레임 만들기
prod="아파트"                                           # 부동산 상품 종류 (ex. 아파트, 오피스텔, 단독다가구 등)
trans="매매"                                            # 부동산 거래 유형 (ex. 매매, 전월세)
sigunguCode="41135"
sigunguCode="41190"
startYearMonth="202101"
endYearMonth="202111"

df = ts.collect_data(prod, trans, sigunguCode, startYearMonth, endYearMonth)
pass