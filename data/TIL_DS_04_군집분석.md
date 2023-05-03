# 군집분석
### 군집분석이란
- 어떤 개체나 대상들을 밀접한 유사성(similarity) 또는 비유사성(dissimilarity)에 의하여 유사한 특성을 지닌 개체들을 몇 개의 군집으로 집단화하는 비지도학습법
- 각 군집의 특성, 군집간의 차이 등에 대한 탐색대상으로, 집단에 대한 심화된 이해가 목적.
- 특이 군집의 발견, 결측값의 보정 등에도 사용될 수 있음.

### 군집의 조건
- 동일 군집에 속한 개체끼리는 유사한 속성이 매우 많음.
- 다른 군집에 속하는 개체끼리는 유사한 속성이 매우 적음.

# 계층적 군집분석(Hierarchical Clustering)
## 계측정 군집분석 개요
### 병합적(agglomerative) vs 분할적(divisive)
- 병합적: 개체 간 거리가 가까운 개체끼리 차례로 묶어주는 방법으로 군집을 정의.
- 분할적: 개체 간 거리가 먼 개체끼리 나누어 가는 방법으로 군집을 정의.
- 계층적 군집분석에서는 병합적 방법이 주로 사용됨.

![image](https://user-images.githubusercontent.com/82266289/235697891-77f29f43-4603-40f2-99f6-8d99b2eae449.png)

## 개체 간 거리 및 군집 간 거리의 정의
### 개체 간 거리
- 유클리디안 거리
- 맨해튼 거리
- 민코오스키 거리

### 군집 간 거리
- 단일 연결법(최단 연결법, single linkage)
  - 두 군집 $C_1$과 $C_2$의 거리는 $d_{c_1c_2} = \min \{d(x,y)|x \in C_1, y \in C_2\}$
![image](https://user-images.githubusercontent.com/82266289/235699980-97ae1944-ee90-47f5-a2bb-d19abdbedbbb.png)

- 완전 연결법(최장 연결법, complete linkage)
  - 두 군집 $C_1$과 $C_2$의 거리는 $d_{c_1c_2} = \max \{d(x,y)|x \in C_1, y \in C_2\}$
![image](https://user-images.githubusercontent.com/82266289/235700613-c40d12fd-067a-4aa8-aa58-6bd4541c210f.png)

- 평균 연결법(average linkage)
  - 두 군집 $C_1$과 $C_2$의 거리는 두 군집의 모든 개체간 거리들의 평균으로 정의.
![image](https://user-images.githubusercontent.com/82266289/235700845-1bed8822-0bd8-48d2-bfed-4428345d6428.png)

- 중심 연결법(centroid linkage)
  - 두 군집 $C_1$과 $C_2$의 거리는 두 군집의 중심 사이의 거리로 정의.
![image](https://user-images.githubusercontent.com/82266289/235700988-ef113bf2-16ac-4d41-ab75-5bfa3df32e62.png)

- ward 연결방법(ward linkage)
  - $SSE_k$를 군집 $k$의 중심으로부터 해당 군집 각 개체 간의 거리 제곱 합으로 정의한 뒤, 총 $K$의 군집이 있다면 $SSE = \sum^k_{k=1}SSE_k$로 정의.
  - $K$개 중 2개의 군집을 하나의 군집으로 묶었을 때 오차제곱합이 증가하는 정도를 두 군집 간의 거리로 정의.
![image](https://user-images.githubusercontent.com/82266289/235701556-fdddb0d0-b5c5-498d-8edc-ae39a79b8f71.png)

### 병합적 방법에서 단일연결법 사용 군집분석 예시
![image](https://user-images.githubusercontent.com/82266289/235928899-eccd2f1d-22a5-41a4-ae7c-7d365f763b19.png)
![image](https://user-images.githubusercontent.com/82266289/235928981-9d450ee6-3ab3-4601-98bf-0b05f0c3cf3f.png)
![image](https://user-images.githubusercontent.com/82266289/235929050-82f2e545-90a2-4c5d-8400-6e8fc6c93576.png)

- 군집분석의 결과를 Dendrogram으로 시각화
- 군집 간 거리가 멀고, 군집 내 거리가 가까워지도록 적절한 지점에서 절단하여 군집 수 결정

![image](https://user-images.githubusercontent.com/82266289/235929224-c4c1a20e-2e8c-46a0-af4a-140b9aec93cc.png)

# 비계층적 군집분석(K-means Clustering)
## K-means 군집분석 개요
- 사전에 결정된 군집 수 k에 기초하여, 전체 데이터를 상대적으로 유사한 k개의 군집으로 구분.
- 계층적 방식에 비하여 계산량이 적고, 대용량 데이터를 빠르게 처리함.
- 사전에 적절한 군집 수 k에 대한 예상이 필요.
- 초기에 군집 중심이 어디로 지정되는지에 따라 최종 결과가 영향을 많이 받음.
- 잡음이나 이상치의 영향을 많이 받음.

### k_means 군집분석 알고리즘
- 개체를 k개의 초기 군집으로 나눈다.
- 각 군집의 중심(centroid)을 계산한 뒤 모든 개체들을 각 군집의 중심에 가장 가까운 군집에 할당시킨다.
- 새로운 개체를 받아들이거나 잃은 군집의 중심을 다시 계산한다.
- 위 과정을 더 이상의 재배치가 생기지 않을 떄까지 반복한다.

![image](https://user-images.githubusercontent.com/82266289/235930354-4ff35b41-41f7-40ef-b65d-40ccca22b77f.png)

### k-means 군집분석 예시(k-menas clustering method)
![image](https://user-images.githubusercontent.com/82266289/235930563-3b1c6ed2-c138-493e-9edc-81c57e628a06.png)
![image](https://user-images.githubusercontent.com/82266289/235931660-07323889-36f3-4585-a11d-cb73d2ddef34.png)
![image](https://user-images.githubusercontent.com/82266289/235931805-5c81ab32-40a2-4331-9fe2-d826cdffee4c.png)
![image](https://user-images.githubusercontent.com/82266289/235931854-1df8e4e2-d18c-4367-b791-4d4c010bbfac.png)
![image](https://user-images.githubusercontent.com/82266289/235931903-014c1bce-bf20-49a8-b32f-e4e354ba9d95.png)

## k-means 군집분석에서 적절한 군집 수의 결정
- 오차제곱합(SSE, sum of squared error)
  - 각 군집 내 개체들과 해당 군집 중심점과의 거리를 제곱한 값들의 함.
  - 오차제곱합이 작을수록 군집 내 유사성이 높아 잘 응집된 것임.
- 군집수 k에 따른 SSE의 변화르 Elbow 차트로 시각화한 뒤, SSE가 급격히 감소하다가 완만해지기 시작하는 시점의 k를 적정 군집수로 판단함.

![image](https://user-images.githubusercontent.com/82266289/235933783-9b48dbca-062f-412b-aa96-64fc483c55ab.png)