### dataframe 합치기

- merge와 concat이 있다. merge는 공통된 데이터가 있을 때, concat은 그렇지 않을 때 사용한다.
concat: row나 column 기준으로 단순하게 이어 붙히기
merge: 특정 고유한 키(unique id) 값을 기준으로 병합하기
- merge는 두 개 이상의 dataframe을 공통된 column을 기준으로 병합한다.
    - 옵션은 다음과 같다.
    - inner join : 두 dataframe에 모두 키 값이 존재하는 경우만 병합.
    - outer join : 하나의 dataframe에 키 값이 존재하면 모두 병합하고 빈자리는 결측치 채움.
    - left join : 두 매개변수 중 왼쪽을 기준으로 병합. 오른쪽 dataframe에 없으면 결측치 채움.
    - right join : 두 매개변수 중 오른쪽을 기준으로 병합. 왼쪽 dataframe에 없으면 결측치 채움.
    - 기준이 된 dataframe이 보유 데이터가 기준이 아닌 dataframe보다 적으면 병합 이후 dataframe 사이즈는 줄어든다.
    - key column을 기준으로 병합. column명이 서로 다른 경우 
    `pd.merge(df, df_right, left_on='이름', right_on='성함', how='outer')` 
    left_on=”column_name_of_df” || right_on=”column_name_of_df_right”
    
    ```jsx
    import pandas as pd
    
    df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value': [1, 2, 3, 4]})
    df2 = pd.DataFrame({'key': ['B', 'D', 'E', 'F'], 'value': [5, 6, 7, 8]})
    
    merged_df = pd.merge(df1, df2, on='key', how='outer')
    
    print(merged_df)
    ```
    
    ![화면 캡처 2023-03-21 232745](https://user-images.githubusercontent.com/82266289/226641344-982529ae-dcf6-4dba-b3d9-7ce0e4edb48a.png)

    
- concat은 두 개 이상의 dataframe을 row(axis=0) 또는 column(axis=1) 방향으로 이어붙이는 작업을 말한다. row 이름이나 column index가 겹치지 않아야 한다.
    - 두 개의 dataframe을 column 방향으로 이어붙이는 예시.
    
    ```jsx
    import pandas as pd
    
    df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
    df2 = pd.DataFrame({'C': [7, 8, 9], 'D': [10, 11, 12]})
    
    concat_df = pd.concat([df1, df2], axis=1)
    
    print(concat_df)
    ```
    
    ![화면 캡처 2023-03-21 232739](https://user-images.githubusercontent.com/82266289/226641339-52967cf0-1ba3-44d9-b9f9-cedd0492a735.png)