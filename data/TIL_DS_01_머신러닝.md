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


