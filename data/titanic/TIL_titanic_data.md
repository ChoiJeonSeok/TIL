## column 정보
- survived : 생존여부(1:생존, 0: 사망)
- pclass : 승선권 클래스(1: 1st, 2:2nd, 3:3rd)
- name : 승객 이름
- sex : 승객 성별
- age : 승객 나이
- sibsp : 동반한 형제자매, 배우자 수
- parch : 동반한 부모, 자식 수
- ticket : 티켓의 고유 넘버
- fare : 티켓의 요금
- cabin : 객실 번호
- embarked : 승선한 항구명 (C:Cherbourg, Q:Queenstown, S:Southampton)
- boat
- body
- home.dest

# 결측치 및 중복 처리
![dd](https://user-images.githubusercontent.com/82266289/233369529-dd53c5b5-f256-4633-bed8-5c525f4caeac.png)

- titanic.shape => (1309, 14)
  
### 중복 확인
- titanic[titanic.duplicated()].sum()
- 
![image](https://user-images.githubusercontent.com/82266289/233369909-f5a9822b-68c6-42a3-aff8-0220783b57a2.png)
<table>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/82266289/233374418-91eca645-bdac-42f8-b90f-d481ee0f5e4d.png" alt="Image 1"></td>
    <td><img src="https://user-images.githubusercontent.com/82266289/233370108-097b47dc-45f1-4f8d-8fff-f4e4ee1eb95b.png" alt="Image 2"></td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/82266289/233370156-223efa1e-34bd-4897-a317-c97332b3479f.png" alt="Image 3"></td>
    <td><img src="https://user-images.githubusercontent.com/82266289/233370182-e3066f98-9fc5-40a6-b790-5d5e7284e3f6.png" alt="Image 4"></td>
  </tr>
</table>

### age
- 평균 나이로 계산하여 채웠다.
  ```
  mean_Age = titanic[ 'age' ].mean(axis = 0 )
  titanic[ 'age' ].fillna( mean_Age, inplace = True )
  ```
### fare
- 빈 요금은 해당 객실의 평균 요금으로 채웠다.
  ```
  mean_fare_3rd_class = round(titanic[titanic['pclass'] == 3]['fare'].mean(), 4)
  ```

### embarked
- 승선지는 2명이 비어있었는데, 1등석이 요금이 80.0이었다.
- 가장 많이 탑승한 곳이 S이며, 탑승지 평균 fare 값을 분석한 결과 평균 72인 S가 가장 차이가 적었다. 
- 그래서 S로 채웠다.
![image](https://user-images.githubusercontent.com/82266289/233375596-c65154c0-1f01-40cd-a04a-c20303b0bbf8.png)

### 결측치 비율 계산
```
missing_ratio = titanic.isnull().mean()
```
![image](https://user-images.githubusercontent.com/82266289/233375754-2c264fae-e309-4224-a4fe-d50b0d4f3447.png)

## 데이터 가공
- 결측치가 40퍼센트가 넘는 column은 과감히 삭제했다.
- sibsp : 동반한 형제자매, 배우자 수
- parch : 동반한 부모, 자식 수
- 이 둘을 합쳐 family_size라는 변수에 담았다.
```
titanic_df = titanic.loc[:, missing_ratio < 0.4]
titanic_df['family_size'] = titanic_df['sibsp'] + titanic_df['parch'] + 1
```

### 요금 구간 라벨링
- 컴퓨터가 계산하기 쉽게 요금 구간을 0부터 6까지 7개의 구간으로 나눴다. 
```
fare_bins = [0, 10, 30, 50, 100, 200, 300]
fare_labels_meaning = ['0-10', '10-30', '30-50', '50-100', '100-200', '200-300', '300-600']
fare_labels = [0, 1, 2, 3, 4, 5, 6]
# fare column의 값에 따라 구간을 할당
titanic_df['fare_group'] = pd.cut(titanic_df['fare'], bins=fare_bins, labels=fare_labels[:-1], include_lowest=True)
```

### 특성 삭제
- 이름, 티켓 번호, sibsp, parch는 삭제했다.
- 이름을 삭제한 이유는 사망자 중에는 저명한 인사지만, 스스로 구명정 탑승을 거부한 사람이 있으며, 그들 중 대부분이 남성이고 1등실에 거주하였기 때문이다. 
- 따라서 Dr. Mr. 등으로 분류한다 해도 생존을 예측하는데 사용하기는 어렵다. Dr. 등의 마음까지 예측할 수는 없기 때문이다.

### one-hot encoding
- 요금 구간, 나이 구간, 가족 규모에 대해서 원 핫 인코딩을 하였다.
```
titanic_onehot = pd.get_dummies(titanic_df, columns=['fare_group'])
titanic_onehot = pd.get_dummies(titanic_onehot, columns=['age_group'])
titanic_onehot = pd.get_dummies(titanic_onehot, columns=['family_size'])
```
- 이미 수치형 데이터이지만, 계산의 효율성과 순서, 중요도 등을 제거하기 위해 하였다.
- 대략 이런 모습이 되었다.
![image](https://user-images.githubusercontent.com/82266289/233378405-b4babcff-6494-4927-9985-9b07a35ea4a8.png)

# 생존자 예측
```
X = titanic_onehot.drop('survived', axis=1)
y = titanic_onehot.iloc[:, 1]
```
```
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

X_train = X_train.astype('float32')
y_train = y_train.astype('float32')
X_test = X_test.astype('float32')
y_test = y_test.astype('float32')
```
```
model = keras.Sequential([
    layers.Dense(1024, activation="relu", input_shape=(26,), dtype='float32'),
    layers.Dropout(0.3),
    layers.Dense(512, activation="relu"),
    layers.Dropout(0.2),
    layers.Dense(256, activation="LeakyReLU"),
    layers.Dropout(0.1),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.1),
    layers.Dense(64, activation="LeakyReLU"),
    layers.Dense(10, activation="softmax")
])


model.compile(optimizer=keras.optimizers.RMSprop(lr=0.0005),
              loss="sparse_categorical_crossentropy",
              metrics=["accuracy"])

early_stopping = EarlyStopping(monitor='val_loss', patience=30)

history = model.fit(X_train, y_train, epochs=500, batch_size=128,
                    validation_split=0.2, callbacks=[early_stopping])
```
![image](https://user-images.githubusercontent.com/82266289/233379056-abc37fa6-beba-4ff4-9e89-a929b7041f7e.png)
```
y_pred = model.predict(X_test)

# 예측 결과 출력
import numpy as np
y_pred_classes = np.argmax(y_pred, axis=1)
print("Predicted classes:", y_pred_classes)

# 정확도 계산
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, y_pred_classes)
print("Accuracy:", accuracy)
```
![image](https://user-images.githubusercontent.com/82266289/233379170-1731dea0-43b1-4878-9e08-426675b0a6c4.png)

**Accuracy: 0.7913486005089059**