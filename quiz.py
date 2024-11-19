import pandas as pd
df_csv = pd.read_csv('pop_kor.csv')

# Quiz 1번
df_excel = pd.read_excel("관서별 5대범죄 발생 및 검거.xlsx")    # 엑셀 파일을 불러온다.
print(df_excel) # 데이터프레임을 출력한다.

# Quiz 2번
# '관서명'의 데이터 글자 중 '서'를 '구'로 바꾸고 새로운 '구별'이라는 컬럼에 저장한다.
df_excel["구별"] = df_excel['관서명'].str.replace("서$", "구", regex=True)
gu_name = df_csv['구별']    # '구별'이라는 새로운 column 추가
# csv 파일과 비교해서 매칭되는 구 데이터가 없으면 '구 없음'으로 값을 적는다.
df_excel["구별"] = df_excel["구별"].where(df_excel['구별'].isin(gu_name), '구 없음')
print(df_excel) # 데이터프레임을 출력한다.

# Quiz 3번
df_excel.set_index('관서명', inplace=True)  # 인덱스를 '관서명'으로 바꾼 결과를 원본에 그대로 저장한다.
# 인덱스를 '구별'로 바꾸고, 집계연산 중 sum을 사용해 같은 구의 경우 더해준다.
pivot = pd.pivot_table(df_excel, index='구별', aggfunc='sum')

# Quiz 4번
# '구 없음' 행을 drop으로 삭제한다.
pivot = pivot.drop(['구 없음'])

# Quiz 5번
# 각 범죄 별로 검거율을 계산한다. 그리고 각 검거율 데이터 column을 데이터프레임에 추가한다.
pivot['강간검거율'] = pivot['강간(검거)'] / pivot['강간(발생)'] * 100
pivot['강도검거율'] = pivot['강도(검거)'] / pivot['강도(발생)'] * 100
pivot['살인검거율'] = pivot['살인(검거)'] / pivot['살인(발생)'] * 100
pivot['절도검거율'] = pivot['절도(검거)'] / pivot['절도(발생)'] * 100
pivot['폭력검거율'] = pivot['폭력(검거)'] / pivot['폭력(발생)'] * 100
pivot['검거율'] = pivot['소계(검거)'] / pivot['소계(발생)'] * 100

# Quiz 6번
# 필요없는 column을 del을 사용해 삭제한다.
del pivot['강간(검거)']
del pivot['강도(검거)']
del pivot['살인(검거)']
del pivot['절도(검거)']
del pivot['폭력(검거)']
del pivot['소계(발생)']
del pivot['소계(검거)']

# Quiz 7번
# 데이터프레임의 컬럼명을 rename을 사용해 변경한다.
pivot = pivot.rename(columns={
    '강간(발생)':'강간',
    '강도(발생)':'강도',
    '살인(발생)':'살인',
    '절도(발생)':'절도',
    '폭력(발생)':'폭력'
})
print(pivot)