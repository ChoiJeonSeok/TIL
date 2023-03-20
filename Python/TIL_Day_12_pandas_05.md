### 결측 값 다루기

- `df.isna()` ⇒ 데이터 프레임 전체에서 결측치가 있는지 확인
- `df[’특정column명’].isnull()` ⇒ 결측치이면 True 값 반환됨.
ex) 인덱스 반환하기 
`df['그룹'][df['그룹'].isnull()]` or `df['그룹'][df['그룹'].isna()]` 
⇒ column ‘그룹’에서 결측치인 행.
- 결측치가 아닌값 ⇒ df[’column’].notnull()
ex) df.loc[ df['그룹'].notnull(), ['키', '혈액형'] ]
- `df.fillna(값)` ⇒ 값으로 NaN 값을 채워주는 함수
- `df.dropna()` ⇒ 결측치가 있는 row 삭제
옵션 : axis=0 ⇒ row // axis=1 ⇒ column (결측치가 하나라도 있는 열 전체 삭제)
: how=’any’ ⇒ default. 하나라도 nan값이면 삭제. // how=’all’ ⇒ 모두 NaN이면 삭제
- 결측치를 삭제하거나 정렬을 시키면 index가 변경이 된다. 
그때는 index값을 다시 부여하여 초기화한다.
`df.reset_index(drop=True)` ⇒ drop=True 옵션은 기존 index를 삭제하는 기능이다.
- `df[’column명’].drop_duplicates()` ⇒ 해당 column에 첫번째 데이터만 남기고 중복값은 삭제
옵션 : keep[’first’] ⇒ default. 첫번째 데이터만 남김. // keep[’last’] ⇒ 마지막 데이터만 남김

### column/row 제거하기

- `df.drop(’column명’, axis=1)` ⇒ column명의 열을 제거
df.drop([’column1’, ‘column2’], axis=1) ⇒ 복수의 column 제거는 list로
- `df.drop(indexNum, axis=0)` ⇒ 해당 index의 row를 제거
df.drop([index1, index2], axis=0) ⇒ 복수의 row 제거는 list로

### 원본 데이터를 보존해야 할 때.

- `변수 = df.copy()` 
변수에 df의 복사본이 담기게 된다. 복사본이므로 변형해도 된다.