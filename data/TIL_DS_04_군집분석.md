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