# 머신러닝 기본 개념
## 머신러닝
- 컴퓨터 시스템에 명시적으로 프로그래밍 하지 않더라도 데이터를 스스로 학습하여 문제를 해결할 수 있게 하는 기술을 의미.
- 사람이 인지하기 어려운 복잡한 규칙과 패턴을 파악하여 의미있는 결과를 얻을 수 있음.

# 머신러닝 방법론의 분류
## 지도학습 (Supervised Learning)
- 라벨이 있는 훈련용 데이터에서, 여러 특성변수를 이용하여 목표변수인 라벨(label)을 예측하도록 모델을 학습함.
- 라벨의 데이터 타입에 따라 라벨이 연속형이면 회귀(regression) 알고리즘, 라벨이 범주형이면 분류(classification) 알고리즘으로 구분함.
- 예시.
  - Linear Regression
  - k-nearest Neighbors
  - Logistic Regression
  - Softmax Regression
  - Decision Tree
  - SVM
  - Random Forest
  - Boosting
  - Neural Network
  - Deep Learning

### 분류(classification) VS 회귀(regression)
![image](https://user-images.githubusercontent.com/82266289/235177964-86797833-017c-4f40-ae2b-1b466b332584.png)

## 비지도학습(Unsupervised Learning)
- 라벨이 없는 훈련용 데이터에서 특징 변수들 간의 관계나 유사성을 기반으로 의미있는 패턴을 추출.
- 자율학습이라고도 함.
- 군집화(clustering), 차원축소(dimension reduction), 추천시스템(recommendation) 등에 활용됨.
- 예시
  - k-means Clustering
  - Hierarchical Clustering
  - PCA
  - t-SNE
  - Apriori
  - Auto-Encoders

### 군집화(clustering)
![image](https://user-images.githubusercontent.com/82266289/235178485-61e91edc-a9e9-43a0-945f-f64a41500040.png)

### 차원축소(dimension reduction)
![image](https://user-images.githubusercontent.com/82266289/235178546-06f185e2-d670-4043-b202-4b450ad6c6d3.png)

### 추천시스템(recommendation)
![image](https://user-images.githubusercontent.com/82266289/235178755-74576b88-5535-4b86-9b11-3131e417266d.png)

## 강화학습(Reinforcement Learning)
- 행동하는 주체(agent)가 있고 행동을 했을 때의 상태(state)와 보상(reward)을 바꿔주는 환경(environment)으로 구성됨
- 주체가 매번 어떠한 행동(action)을 하면 환경에 의해 상태와 보상이 바뀌면서 주체는 보상이 가장 커지는 방향으로 계속 학습해 나가게 됨.
- 예시
  - SARSA, Q-Learning

# 머신러닝 모델의 분석 절차
## 모델 기반 지도학습 알고리즘의 일반적인 분석 절차
- 주어진 데이터 전처리 및 탐색
- 적절한 모델을 선택
- 주어진 데이터로 모델을 훈련시킴
- 훈련된 모델을 적용하여 새로운 데이터에 대한 예측을 수행

### 과대적합(overfitting)의 문제
- 주어진 자료는 거의 완벽한 예측이 가능하지만, 미래의 새로운 자료에 대한 예측력이 떨어지는 문제
- 복잡한 알고리즘을 사용하여 데이터를 훈련하는 경우 과대적합 문제를 항상 염두에 두어야 함.
![image](https://user-images.githubusercontent.com/82266289/235179603-552f45c9-3043-453f-8096-56e04535304d.png)

# 모델의 검증 및 평가
## 모델의 검증 및 평가 개요
### 모델 평가의 필요성
- 과대적합을 막고 일반화 오차를 줄이기 위해서는, 새로운 데이터에 얼마나 잘 일반화될지를 파악해야 함.
- 모델 적합에 사용된 자료를 평가를 위해 재활용하지 않고, 평가만을 위한 데이터를 확보할 필요가 있음.

## 모델 검증 및 평가를 위한 데이터의 구분
### Hold-out 방식
- 주어진 자료를 다음의 세 그룹으로 랜덤하게 분할한 뒤, 주어진 목적에 따라 각각 모델의 훈련, 검증, 평가에 활용함.
1. 훈련 데이터(Training data)
  - 모델의 학습을 위해 사용되는 자료
2. 검증 데이터(Validation data)
  - 훈련 자료로 적합한 모델을 최적의 성능으로 튜닝하기 위해 사용되는 자료.
  - 훈련에 필요한 하이퍼파라미터(hyperparameter)를 조정하거나, 변수선택(model selecting) 등에 이용.
3. 평가 데이터(Test data)
  - 훈련 및 검증 자료로 적합된 최종 모형이 미래에 주어질 새로운 자료에 대하여 얼마나 좋은 성과를 갖는지를 평가하는데 사용되는 자료.

### K-fold 교차검증(Cross-validation) 방식
- 자료의 수가 충분하지 않은 경우에는 훈련 데이터에서 너무 많은 양의 데이터를 검증 또는 평가 데이터에 뺏기지 않도록 교차 검정(cross-validation) 기법을 사용.
- 자료를 균등하게 k개의 그룹으로 분할한 뒤
- 각 j에 대하여, j번째 그룹을 제외한 나머지 k-1개 그룹의 자료를 이용하여 모델을 적합(fit).
- j번째 그룹의 자료에 적합된 모델을 적용한 뒤 예측오차를 구함.
- j=1, ..., k에 대하여 위의 과정을 반복한 뒤, k개의 예측오차의 평균을 구함.
- 예측오차의 평균값을 기준으로, 모델의 검증 또는 평가를 수행.

### 편향-분산 트레이드(Bias-Variance Trade off)
- 모델의 복잡한 정도에 따라 훈련 데이터와 평가 데이터의 예측오차는 일반적으로 다음과 같은 패턴을 보임.

![image](https://user-images.githubusercontent.com/82266289/235305758-4a278c12-9853-4955-9f68-5c2feaa879fc.png)

### 과대적합을 막기 위한 방법
- 훈련 데이터를 많이 확보한다.
- 모델의 복잡도를 낮춘다.
  - 특성 변수의 수를 줄이거나 차원축소.
  - 파라미터에 규제(regularization)을 적용.

# 머신러닝 모델의 평가지표
## 회귀(Regression) 모델의 평가 지표
![image](https://user-images.githubusercontent.com/82266289/235305958-24a3599a-dc00-4e14-8195-b094236a3358.png)

![image](https://user-images.githubusercontent.com/82266289/235305985-5d4d569d-a802-4488-95b8-a1f08dbfc1e6.png)

Accuracy = TP + TN / (TP + TN + FP + FN)
<table>
  <tr>
    <td></td>
    <th style="background-color:#f2f2f2">실제 양성 클래스</th>
    <th style="background-color:#f2f2f2">실제 음성 클래스</th>
  </tr>
  <tr>
    <th style="background-color:#f2f2f2">예측 양성 클래스</th>
    <td style="background-color:#b3ffb3; font-weight:bold">TP (True Positive)</td>
    <td style="background-color:#ff9999; font-weight:bold">FP (False Positive)</td>
  </tr>
  <tr>
    <th style="background-color:#f2f2f2">예측 음성 클래스</th>
    <td style="background-color:#ff9999; font-weight:bold">FN (False Negative)</td>
    <td style="background-color:#b3ffb3; font-weight:bold">TN (True Negative)</td>
  </tr>
</table>
