# city_data_processing.py

`city_data_processing.py`는 Open API를 사용하여 데이터를 추출하고 CSV 파일로 저장한 뒤, Hadoop 시스템에 업로드하는 Python 스크립트입니다.

## 요구 사항

- Python 3.x 이상이 설치되어 있어야 합니다.
- Apache Spark가 설치되어 있어야 합니다.
- Hadoop 클러스터가 구성되어 있어야 합니다.

## 사용법

1. `url.csv`을 `city_data_processing.py` 파일 디렉토리에 준비합니다. 이 파일에는 spark submit을 위한 url과 app_name, csv 저장 및 hdfs에 저장할 경로가 입력되어 있어야 합니다.

| url                 | master_url           | app_name   | script_path           | csv_path               | hdfs_path                  |
|---------------------|----------------------|------------|-----------------------|------------------------|----------------------------|
| http://example.com  | spark://example-master  | example-app  | /path/to/script.py  | /path/to/output.csv  | /hdfs/path/to/output.csv  |

2. 터미널 또는 명령 프롬프트에서 다음 명령을 실행하여 스크립트를 실행합니다:

   ```python
   python city_data_processing.py [작동 시간]
   ```

   - `[작동 시간]`에는 스크립트가 작동할 총 시간(시간 단위)을 입력합니다. 예를 들어, `python city_data_processing.py 3`은 스크립트를 3시간 동안 실행합니다.
   
   - 작동 시간에 0을 입력하면, Ctrl + C 로 중지하지 않는 한, 무한히 작동합니다. 

   - 스크립트가 실행되면 Spark submit에 제출된 python script가 Open API를 통해 데이터를 추출하고, 추출된 데이터는 CSV 파일로 저장됩니다. 그 후, CSV 파일은 Hadoop 시스템으로 업로드됩니다.

   - 스크립트는 `Ctrl+C`를 눌러 수동으로 중지하거나, `[작동 시간]`이 지나면 자동으로 종료됩니다.

   - 스크립트 실행 중에는 작업 진행 상황과 관련된 메시지가 출력됩니다.

