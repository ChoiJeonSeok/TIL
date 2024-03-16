import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def load_csv_auto_encoding(filepath):
    """
    자동 인코딩 감지를 시도하여 CSV 파일을 로드하는 함수입니다.
    일반적으로 사용되는 인코딩 몇 가지를 시도해보고, 그 중 하나로 파일을 성공적으로 열 수 있다면 해당 데이터프레임을 반환합니다.
    """
    encodings = ['cp949', 'utf-8', 'ISO-8859-1', 'cp1252']  # 시도할 인코딩 리스트
    for enc in encodings:
        try:
            df = pd.read_csv(filepath, encoding=enc)
            return df
        except UnicodeDecodeError:
            pass
    raise ValueError(f"All tried encodings failed. Check the file encoding: {filepath}")


def clean_data(df, method='median', fill_value=None, columns=None):
    """
    데이터 클리닝을 수행하는 함수입니다.
    결측치 처리 방법을 선택할 수 있습니다.
    method: 'mean', 'median', 'mode', 'constant' 중 하나를 선택합니다.
    fill_value: 'constant' 방법을 사용할 때 채울 값입니다.
    columns: 결측치를 처리할 특정 열(들)을 지정합니다. None일 경우 모든 열에 적용됩니다.
    """
    if columns is None:
        columns = df.columns

    if method == 'mean':
        # 평균으로 채우기
        df[columns].fillna(df[columns].mean(), inplace=True)
    elif method == 'median':
        # 중앙값으로 채우기
        df[columns].fillna(df[columns].median(), inplace=True)
    elif method == 'mode':
        # 최빈값으로 채우기 (범주형 데이터에 적합)
        for col in columns:
            df[col].fillna(df[col].mode()[0], inplace=True)
    elif method == 'constant':
        # 지정된 상수값으로 채우기
        if fill_value is not None:
            df[columns].fillna(fill_value, inplace=True)
        else:
            raise ValueError("fill_value must be provided for method='constant'")
    else:
        raise ValueError("Invalid method. Choose from 'mean', 'median', 'mode', 'constant'.")

    # 숫자가 아닌 데이터를 NaN으로 변환
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    return df

def basic_statistics(df):
    """
    데이터프레임의 기본 통계 정보를 제공하는 함수입니다.
    이 함수는 데이터프레임의 각 수치형 열에 대한 기본적인 통계적 요약을 반환합니다.
    반환되는 통계 정보에는 평균, 표준편차, 최소값, 25/50/75 백분위수, 최대값이 포함됩니다.
    """
    return df.describe()

def correlation_analysis(df):
    """
    데이터프레임 내 변수들 간의 상관관계를 분석하는 함수입니다.
    이 함수는 각 수치형 변수 간의 피어슨 상관계수를 계산하여 반환합니다.
    상관계수는 -1부터 1사이의 값을 가지며, 이는 변수 간의 선형 관계의 강도를 나타냅니다.
    """
    return df.corr()

def plot_distribution(df, column, title="Distribution Plot", bins=None, color=None):
    """
    주어진 데이터프레임의 특정 열에 대한 분포를 시각화하는 함수입니다.
    title: 그래프의 제목을 설정합니다.
    bins: 히스토그램의 빈(bin) 수를 설정합니다.
    color: 그래프의 색상을 설정합니다.
    """
    sns.histplot(df[column], kde=True, bins=bins, color=color)
    plt.title(title)
    plt.show()

def plot_correlation_matrix(df, title="Correlation Matrix", cmap='coolwarm', annot=True):
    """
    데이터프레임 내의 변수들 간 상관관계 매트릭스를 시각화하는 함수입니다.
    title: 히트맵의 제목을 설정합니다.
    cmap: 색상 팔레트를 설정합니다.
    annot: 각 셀에 상관계수 값을 표시할지 여부를 결정합니다.
    """
    plt.figure(figsize=(10, 8))  # 그래프 크기 설정
    sns.heatmap(df.corr(), annot=annot, fmt=".2f", cmap=cmap)
    plt.title(title)
    plt.show()



# 사용예시
# CSV 파일 로드
#filepath = 'path_to_your_csv.csv'
#df = load_csv_auto_encoding(filepath)

# 모든 열에 대해 결측치를 중앙값으로 처리
#df = clean_data(df, method='median')

# 'column1'과 'column2' 열의 결측치를 최빈값으로 처리
#df = clean_data(df, method='mode', columns=['column1', 'column2'])

# 모든 열에 대해 결측치를 상수 0으로 처리
#df = clean_data(df, method='constant', fill_value=0)

# 데이터의 기본 통계 정보를 출력
#print(basic_statistics(df))

# 변수들 간의 상관 계수를 출력
#print(correlation_analysis(df))

# 지정한 열의 데이터 분포를 시각화
# 제목, 히스토그램 빈(bin) 수, 색상을 사용자 정의 매개변수로 설정할 수 있다
#plot_distribution(df, 'decideCnt', title="Distribution of decideCnt", bins=30, color='blue')

# 데이터프레임 내의 변수들 간 상관관계 매트릭스를 히트맵으로 시각화
# 제목, 색상 팔레트(cmap), 상관계수 값 표시 여부(annot)를 사용자 정의 매개변수로 설정할 수 있다
#plot_correlation_matrix(df, title="Correlation Matrix of DataFrame", cmap='viridis', annot=False)
