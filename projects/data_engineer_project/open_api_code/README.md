# fetch_city_data

- `fetch_city_data`는 서울시 실시간 도시데이터를 API로 가져와서 CSV 파일에 저장하는 Python 함수입니다.

- 서울시 실시간 도시데이터는 서울시의 주요 113장소에 대한 실시간 인구현황, 도로소통현황, 주차장 현황, 지하철 실시간 도착 현황, 버스정류소 현황, 사고통제현황, 따릉이 현황, 날씨 현황, 전기차충전소 현황, 문화행사 현황 정보를 제공합니다.
- 이 함수에서는 장소, 실시간 인구현황, 장소 혼잡도 지표, 실시간 인구 비율, 실시간 사고 및 사건 상황, 날씨, 대기 상황, 주변 문화행사를 서울시 실시간 도시데이터로부터 추출할 수 있습니다. 
- 추가 또는 제외하고 싶은 항목이 있으시다면 tags 리스트를 [서울시 실시간 도시데이터](https://data.seoul.go.kr/dataList/OA-21285/A/1/datasetView.do#)의 출력값 부분을 참고하시어 바꾸시면 됩니다.

## 사용법

```python
fetch_city_data(fileDir, place="empty", mode="new")
```

### 매개변수

- `fileDir`: 데이터를 저장할 CSV 파일의 `경로와 파일명`을 지정합니다. 반드시 확장자 `.csv`를 포함해야 합니다.
- `place` : 관광지를 지정합니다. 기본값은 `"empty"`이며, 반드시 `"seoul_113_places.xlsx"` 문서에 기록된 실제 `관광지 이름 또는 코드`를 입력해야 합니다.

- `mode` : 데이터 저장 모드를 지정합니다. `"new"` 또는 `"append"` 중 하나를 선택할 수 있습니다. 기본값은 `"new"`입니다.
  - `"new"`: 새로운 `.csv` 파일로 저장합니다. 기존 파일이 있으면 덮어씁니다.
  - `"append"`: 기존 `.csv `파일에 데이터를 추가합니다. 기존 파일이 없으면 새로운 파일로 저장합니다.

- `encoding` : 인코딩 형식을 지정합니다. 기본값은 `"cp949"`입니다.

### 사용 예시

```python
from fetch_city_data import fetch_city_data

# 새로운 파일로 데이터 저장
fetch_city_data("output.csv", place="광화문·덕수궁", mode="new")

# 기존 파일에 데이터 추가
fetch_city_data("output.csv", place="광화문·덕수궁", mode="append")
