# 요약변수와 파생변수
### 요약변수
- 수집된 정보를 분석의 목적에 맞게 종합(aggregate)한 변수.
- 많은 모델에 공통으로 사용될 수 있어 재활용성이 높다.
  - 단어 빈도, 상품별 구매 금액, 상품별 구매량, 영화 매출액

### 파생변수
- 특정한 의미를 갖는 작위적 정의에 의한 변수
- 사용자가 특정 조건을 만족하거나 특정 함수에 의해 값을 만들어 의미를 부여한 변수.
- 주관적일 수 있으므로 논리적 타당성을 갖추어야 함.
  - 구매상품 다양성 변수, 가격 선호대 변수, 라이프 스타일 변수, 영화 인기도 변수

# 데이터 정제
## 결측값의 이해
- 기록누락, 미응답, 수집오류 등의 이유로 결측이 발생.
- 결측값이 포함된 자료라도 나머지 변수의 값들은 의미있는 정보이므로, 정보의 손실을 최소화 하도록 결측을 처리하는 것이 바람직함.

## 결측값 처리법
### 완전제거법(list-wise deletion)
- 결측값이 하나 이상 포함된 자료를 제거하는 방법.
- 정보의 손실로 분석 결과가 왜곡될 수 있음

### 평균대체법(mean value imputation)
- 결측값을 해당 변수의 나머지 값들의 평균으로 대체하는 방법.
- 추정량의 표준오차가 과소추정되는 문제가 있음.

### 핫덱대체법(hot deck imputation)
- 동일한 데이터 내에서 결측값이 발생한 관찰치와 유사한 특성을 가진 다른 관찰치의 정보를 이용하여 대체하는 방법.
- 정보의 손실로 분석 결과가 왜곡될 수 있음.

### 그밖의 결측값 처리법
- 대체: Regression imputation, kNN imputation
- 선형보간법(Linear Interpolation)
- 다중선형회귀(Multiple Linear Regression)
- KNN(K-Nearest Neighbors)
- EM(Expectation-Maximization) 알고리즘
- MICE(Multiple Imputation by Chained Equations)
- 결측값 예측 Deeplearning model
- Time Series Analysis(ARIMA, Prophet 등 모델)

# 이상값
### 이상값이란?
- 다른 데이터와 동떨어진 값
- 의미가 있을수도 있고, 오류에 의한 값이라 의미가 없을 수도 있다.

## 이상값의 탐지
###상자그림
- Q1 - 1.5 X IQR과 Q3 + 1.5 X IQR 의 범위를 넘어가는 자료를 이상값으로 진단.

![image](https://user-images.githubusercontent.com/82266289/234896652-392d0a7a-c0c6-4c62-be67-d836613f08aa.png)

### 표준화 점수(Z-score)
- 표준화 점수의 절대값이 2, 3보다 큰 경우 이상값으로 진단한다.

## 이상값 처리 방법
### 이상값 제외(trimming)
- 처리는 간단하지만, 정보 손실이 발생하고 추정량 왜곡이 생길 수 있음.
### 이상값 대체(winsorization)
- 이상값을 정상값 중 최대 또는 최소 등으로 대체하는 방식.
### 변수변환
- 자료값 전체에 로그변환, 제곱근 변환 등을 적용.

## 연속형 자료의 범주화
### 변수구간화(binning)
- 연속형 변수를 구간을 이용하여 범주화하는 과정. 
- 연령 구간 10이상 20미만을 10으로 범주화.
- 연봉 구간 범주화

### 변수구간화의 효과
- 이상치 문제를 완화
- 결측치 처리 방법이 될 수 있음
- 변수간 관계가 단순화 되어 분석 시 과적합을 방지할 수 있고 결과 해석이 용이해진다.
  
<br><br>

# 데이터 변환과 결합
## 데이터 변환
- 자료 변환을 통해 자료의 해석을 쉽고 풍부하게 하기 위한 과정
### 데이터 변환 목적
- 분포의 대칭화
- 산포를 비슷하게 하기 위하여
- 변수 간 관계를 단순하게 하기 위하여

### 제곱근 변환 vs 제곱 변환
![image](https://user-images.githubusercontent.com/82266289/234898587-ab671cf4-dff2-4d4e-bd45-c4c83091e6e4.png)

### 로그 변환 vs 지수 변환
![image](https://user-images.githubusercontent.com/82266289/234898719-deaeeec7-b62d-4ef8-b266-5f2675795c86.png)

### 박스콕스 변환(Box-Cox Transform)
![image](https://user-images.githubusercontent.com/82266289/234899085-c5efa704-fb86-4153-a4f7-ba79969670d4.png)

## 데이터 결합
![image](https://user-images.githubusercontent.com/82266289/234900130-569b6945-2f86-4036-9f4f-437b6e3d9082.png)
- X1: 키 변수

### 이너 조인(inner join)
- 두 테이블에 키(key)가 공통으로 존재하는 레코드(record)만 결합.
- (A, 1, T), (B, 2, f)

### 풀아우터조인(full outer join)
- 두 테이블 중 어느 한쪽이라도 존재하는 키에 대한 레코드를 모두 결합.
- (A, 1, T), (B, 2, F),(C, 3, NA),(D,NA,T)

### 레프트 조인(left join)
- 왼쪽 테이블에 존재하는 키에 대한 레코드를 결합
- (A, 1, T), (B, 2, F), (C, 3 NA)

### 라이트 조인(right join)
- 오른쪽 테이블에 존재하는 키에 대한 레크드를 결합
- (A, 1, T), (B, 2, F), (D, NA, T)
