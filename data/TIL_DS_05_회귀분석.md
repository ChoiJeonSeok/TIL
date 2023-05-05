# 회귀분석 개요
- 독립변수와 종속변수 간의 함수적인 관련성을 규명하기 위하여 어떤 수학적 모형을 가정하고, 이 모형을 측정된 자료로부터 통계적으로 추정하는 분석방법

### y=f(x)의 함수 관계가 있을 때, 
- x를 설명변수(explanatory variable) 또는 독립변수(independent variable)
  - 단순 회귀 : 독립변수가 1개
  - 다중 회귀 : 독립변수가 2개 이상
- y를 반응변수(response variable) 또는 종속변수(dependent variable)

![image](https://user-images.githubusercontent.com/82266289/236238891-cafc2057-4382-452b-86b6-ab0980862acb.png)

# 단순선형회귀모형
## 모형 정의 및 가정
### 자료($x_i, Y_i$), $i=1,...,n$에 다음의 관계식이 성립한다고 가정함.
- $Y_i = \alpha + \beta x_i +$ $\epsilon_i$, $i = 1,2,...,n$
- 오차항인 $\epsilon_1, \epsilon_2, \dots, \epsilon_n$ 는 서로 독립인 확률변수로, $\epsilon_i~N[0,\sigma^2]$
: 정규, 등분산, 독립 가정
- $\alpha, \beta$는 회귀계수라 부르며 $\alpha$는 절편, $\beta$는 기울기를 나타냄.
- $\alpha, \beta, \sigma^2$은 미지의 모수로, 상수임.

- $Y_i~N[\alpha + \beta x_i, \sigma^2] -> E[Y_i] = \alpha + \beta x_i$
![image](https://user-images.githubusercontent.com/82266289/236479068-3b19b44b-1767-4f47-befa-2e353cec84a6.png)

### 모수 추정
- 모형이 포함한 미지의 모수 $\alpha, \beta$를 추정하기 위하여 각 독립변수 $x_i$에 대응하는 종속변수 $y_i$로 짝지어진 n개의 표본인 관측치 (x_i, y_i)가 주어짐.

![image](https://user-images.githubusercontent.com/82266289/236479601-10be41c9-6f20-407f-9634-922d25932bc8.png)

### 최소제곱법
- 단순회귀모형 $Y_i = \alpha + \beta x_i + \epsilon_i$에서 자료점과 회귀선 간의 수직거리 제곱합 $SS(\alpha, \beta) = \sum^n_{i=1}(y_i - \alpha - \beta x_i)^2$이 최소가 되도록 $\alpha$와 $\beta$를 추정하는 방법.

![image](https://user-images.githubusercontent.com/82266289/236480284-8ce7944a-51f7-4192-9e76-782a9ac68b37.png)

- $\alpha$에 대한 최소제곱 추정량 : $\hat{\alpha} = y - \hat{\beta} x$
- $\beta$에 대한 최소제곱 추정량 : $\hat{\beta} = \frac{\sum^n_{i=1}x_i(y_i-\vec{y})}{\sum^n_{i=1}x_i(x_i-\vec{x})}$
  - 단, $\vec{x}$는 $x_i$의 평균, $\vec{y}$는 $y_i$의 평균
- $y_i$의 추정치 : $\hat{y_i} = \hat{\alpha} + \hat{\beta}x_i$  ,$i = 1,2,...,n$
- 잔차 : $e_i = y_i - \hat{y_i} = y_i - \hat{\alpha} - \hat{\beta}x_i$ ,$i = 1,2,...,n$

### 예시
- 자동차의 주행속도와 정지거리에 관한 50개의 표본 자료를 이용하여, 주행거리를 독립변수로, 정지거리를 종속변수로 두고 단순선형회귀모형을 적합하고자 함.

![image](https://user-images.githubusercontent.com/82266289/236485107-443917af-e776-4f59-b19c-bfc5f180ccdd.png)

- 회귀계수의 추정 $\vec{X} = 15.4, \vec{y} = 42.98$ 이므로, $\beta = \frac{\sum^n_{i=1}x_i(y_i - \vec{y})}{\sum^n_{i=1}x_i(x_i - \vec{x})} = 3.932$ <br> $\hat{\alpha} = \vec{y} - \hat{\beta}\vec{x} = -17.579$ 로 계산됨.
- 추정된 회귀선 $\hat{y} = -17.579 + 3.932x$
- 결정계수 $R^2 = \frac{SSR}{SST} = 0.6511$

## 단순선형회귀모형의 유의성 검정
### 모형의 유의성 t 검정
- 독립변수 $x$가 종속변수 $Y$를 설명하기에 유용한 변수인가에 대한 통계적 추론은 회귀계수 $\beta$에 대한 검정을 통해 파악할 수 있음.
- 가설
  - $H_0 : \beta = 0$
  - $H_1 : \beta \ne 0$ 