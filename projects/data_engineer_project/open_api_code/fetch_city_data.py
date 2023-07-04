import requests
import xml.etree.ElementTree as ET
import pandas as pd

def fetch_city_data(fileDir, place="empty", mode="new", encoding="cp949"):
    # 매개변수 예외처리
    if fileDir is None:
        return print("fileDir을 입력해주세요.")
    elif place == "empty":
        return print("관광지를 place에 입력해주세요.")
    
    # API 엔드포인트와 KEY 값을 연결하여 URL 생성
    base_url = "http://openapi.seoul.go.kr:8088/"
    key = "write your api key"
    url = f"{base_url}{key}/xml/citydata/1/5/{place}"

    # API 요청 보내기
    response = requests.get(url)

    # 응답 결과 확인
    if response.status_code == 200:
        # API 요청 성공
        data = response.content
        
        # XML 파싱
        root = ET.fromstring(data)
        
        # 추출하고자 하는 태그들을 리스트로 저장
        tags = ['AREA_NM', 'AREA_CD', 'AREA_CONGEST_LVL', 'AREA_CONGEST_MSG', 
                'AREA_PPLTN_MIN', 'AREA_PPLTN_MAX', 'MALE_PPLTN_RATE', 
                'FEMALE_PPLTN_RATE', 'PPLTN_RATE_0', 'PPLTN_RATE_10', 
                'PPLTN_RATE_20', 'PPLTN_RATE_30', 'PPLTN_RATE_40', 
                'PPLTN_RATE_50', 'PPLTN_RATE_60', 'PPLTN_RATE_70', 
                'RESNT_PPLTN_RATE', 'NON_RESNT_PPLTN_RATE', 'PPLTN_TIME',
                'ACDNT_OCCR_DT', 'EXP_CLR_DT', 'ACDNT_TYPE', 'ACDNT_DTYPE',
                'ACDNT_INFO', 'ACDNT_X', 'ACDNT_Y', 'ACDNT_TIME',
                'TEMP', 'SENSIBLE_TEMP', 'MAX_TEMP', 'MIN_TEMP', 'HUMIDITY',
                'WIND_DIRCT', 'WIND_SPD', 'PRECIPITATION', 'PRECPT_TYPE', 'PCP_MSG',
                'UV_INDEX_LVL', 'UV_INDEX', 'UV_MSG', 'PM25_INDEX', 'PM25',
                'PM10_INDEX', 'PM10', 'AIR_MSG', 'WARN_MSG',
                'EVENT_NM','EVENT_PERIOD','EVENT_PLACE','EVENT_ETC_DETAIL']

        # 데이터를 저장할 리스트
        results = []

        # 전체 구간 추출 및 데이터 수집
        for citydata in root.findall(".//CITYDATA"):
            data_dict = {}

            # 각 태그별로 데이터 추출
            for tag in tags:
                sub_element = citydata.find(".//"+tag)
                if sub_element is not None:
                    data_dict[tag] = sub_element.text
                else:
                    data_dict[tag] = None

            # 딕셔너리를 리스트에 추가
            results.append(data_dict)

        # 데이터를 DataFrame으로 변환
        new_df = pd.DataFrame(results)

        if mode == "new":
            # 새로운 파일로 저장
            new_df.to_csv(fileDir, index=False, encoding=encoding)
            print("데이터를 새로운 CSV 파일로 저장했습니다.")
        elif mode == "append":
            try:
                # 기존 CSV 파일 로드
                existing_df = pd.read_csv(fileDir, encoding=encoding)

                # 데이터를 기존 파일에 추가
                merged_df = pd.concat([existing_df, new_df], ignore_index=True)

                # 추가된 데이터를 CSV 파일로 저장
                merged_df.to_csv(fileDir, index=False, encoding=encoding)
                print("데이터를 기존 CSV 파일에 추가했습니다.")
            except FileNotFoundError:
                # 기존 파일이 없을 경우, 새로운 파일로 저장
                new_df.to_csv(fileDir, index=False, encoding=encoding)
                print("기존 CSV 파일이 없어 데이터를 새로운 파일로 저장했습니다.")
        else:
            print("잘못된 모드입니다. 'new' 또는 'append'를 선택하세요.")
    else:
        # API 요청 실패
        print("API 요청에 실패했습니다.")