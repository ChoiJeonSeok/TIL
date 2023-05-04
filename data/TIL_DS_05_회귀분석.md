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