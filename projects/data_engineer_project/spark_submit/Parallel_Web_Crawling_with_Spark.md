## Spark를 이용한 웹 크롤링.

Apache spark에서 생성한 데이터를 Hadoop의 HDFS에 직접 저장할 수 있다.
Spark의 RDD나 DataFrame API를 사용하여 데이터를 처리한 후, saveAsTextFile 함수와 같은 함수를 사용하여 HDFS의 경로를 지정하여 저장하면 된다.
예시) rdd.saveAsTextFile("hdfs://namenode:8020/path/to/result.csv")
Spark에서 생성된 데이터가 HDFS의 지정된 경로에 result.csv 라는 이름으로 저장되게 된다. 이 경우, 데이터를 가상 머신의 로컬 파일 시스템에 저장되지 않고, 직업 HDFS에 저장된다.

## Spark를 이용한 웹 크롤링 병렬처리

Master와 각 Worker 노드에는 크롬 드라이버가 모두 설치되어 있어야 한다.
Spark Master는 작업을 스케줄링 하는 역할을 한다. 실제 작업은 Worker 노드에서 진행된다.
Spark Master는 전체 작업을 여러 개의 작업 단위로 분할하여 각 Worker 노드에 할당할 수 있다
이 경우, 각 Worker 노드는 할당받은 작업 단위에 해당하는 링크들에 대한 크롤링 작업을 진행한다. 
예) 100개의 링크에 대해 크롤링을 하는 경우, Spark Master가 전체 작업을 임의의 작업 단위로 분할합니다. 예를 들어 10개로 나눴다면 각 Worker 노드가 하나씩 가져가서 해당 10개의 링크에 대한 크롤링 작업을 진행합니다.
	
작업 단위를 분할하는 것은 Worker 노드의 수와 클러스터의 성능을 고려해야 한다. Worker 노드가 3개인데, 작업을 4개로 분할하면 결국 두 개의 Worker 노드는 사용되지 않는 시간이 생겨 비효율이 발생하기 때문이다.

#