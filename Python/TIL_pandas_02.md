### 특정 column의 행 데이터 선택

- df.loc[행 번호 이상:행 번호 미만 , ‘column명’] or df.loc[:, [‘column명1’, ‘column명2’, …]
column에 대해 단수 선택과 복수 선택이 모두 가능하다.
- `df.iloc[범위, 범위]`
행과 열을 범위로 접근할 수 있다.
ex) df.iloc[1:5, [0, 2]] ⇒ 행 1번부터 4번까지. 열 0번과 2번.
ex) df.iloc[:4, 1:4] ⇒ 행 처음부터 3번까지. 열 1번부터 3번까지.

### Boolean Indexing - 조건을 활용한 색인

- `df[’키’] > 100`
’키’ 열의 데이터에 >100 조건을 적용하여 True와 False를 반환하게 한다.
- df[’키’]>100 자체가 검색조건이 된다.
- 사용법: `df[검색조건(Boolean type)]`
ex) df[df[’키’]>180]  : df 데이터베이스에서 ‘키’열의 데이터가 180초과이면 출력.
- 특정 column과 같이 색인하고 싶을 때.
1. 맨 뒤에 출력할 column 붙이기
ex) df[ df['키'] > 180]['이름']
ex) df[ df['키'] > 180 ][['이름', '키']] ⇒ 찾을 열이 여러개인 경우 2차원 리스트 형태로 사용.
2. loc를 활용
ex) df.loc[ df['키'] > 180, '이름'] ⇒ 키 180초과의 이름.
ex) df.loc[ df['키'] > 180, '이름': '성별'] ⇒ 키 180 초과의 이름부터 성별까지 데이터.
ex) df.loc[ df['키'] > 180, ['이름', '키']] ⇒ 키 180 초과의 이름과 키 열

### isin을 활용한 색인

- isin을 활용한 색인은 조건을 걸고자 하는 값이 내가 정의한 list에 있을 때만 색인하려는 경우에 사용한다.

```jsx
my_condition = ['플레디스', 'SM']

# 검색조건 -> 소속사중에 플레디스 or SM이 있는지
df['소속사'].isin(my_condition) => 이게 검색 조건이 된다.
ex) 
df.loc[df['소속사'].isin(my_condition)] => 소속사 중에 플레디스 or SM이 있는 데이터
df.loc[df['소속사'].isin(my_condition),'이름'] => 소속사 중에 플레디스 or SM이 있는 이름
df.loc[df['소속사'].isin(my_condition), '소속사'] => 소속사 중에 플레디스 or SM 인 소속사
```

### 결측 값 다루기

- `df.isna()` ⇒ 데이터 프레임 전체에서 결측치가 있는지 확인
- `df[’특정column명’].isnull()` ⇒ 결측치이면 True 값 반환됨.
ex) 인덱스 반환하기 
`df['그룹'][df['그룹'].isnull()]` or `df['그룹'][df['그룹'].isna()]` 
⇒ column ‘그룹’에서 결측치인 행.
- 결측치가 아닌값 ⇒ df[’column’].notnull()
ex) df.loc[ df['그룹'].notnull(), ['키', '혈액형'] ]