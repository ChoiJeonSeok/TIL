import subprocess
import time

# Spark Submit 명령어 실행 함수 정의
def run_spark_submit():
    command = "spark-submit --master <master-url> --name <app-name> /path/to/script.py"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    # 확인 메시지 출력
    print("Spark Submit completed successfully")
    return output

# CSV 파일을 Hadoop에 이동하는 함수 정의
def move_csv_to_hadoop():
    move_output_to_hdfs = "hadoop fs -put /path/to/output.csv /hdfs/path/to/output.csv"
    subprocess.run(move_output_to_hdfs, shell=True)
    # 확인 메시지 출력
    print("Seoul city data CSV file moved to Hadoop successfully")

# 1시간마다 Spark Submit 실행하고 CSV 파일 이동
while True:
    run_spark_submit()
    move_csv_to_hadoop()
    time.sleep(3600)
