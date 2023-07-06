import subprocess
import time
import signal
import datetime

is_running = True  # 작업을 계속 실행할지 여부를 저장하는 변수

# Signal 핸들러 함수 정의
def signal_handler(sig, frame):
    global is_running
    print("Received signal to stop the program")
    is_running = False

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

# 작업 실행 함수 정의
def run_job():
    # 작업 시작 시간 기록
    start_time = time.time()

    # 작업 실행 및 작동 시간 출력
    while is_running:
        run_spark_submit()
        move_csv_to_hadoop()
        time.sleep(3600)

    # 작업 종료 시간 기록
    end_time = time.time()

    # 작동 시간 계산
    duration = end_time - start_time
    hours = int(duration // 3600)
    minutes = int((duration % 3600) // 60)
    seconds = int(duration % 60)
    duration_str = f"{hours} hours, {minutes} minutes, {seconds} seconds"

    # 작동 시간 출력
    print(f"Program executed for {duration_str}")

    # 로그 파일에 기록
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{current_time} - Program executed for {duration_str}\n"
    with open("log.txt", "a") as log_file:
        log_file.write(log_message)
# Signal 핸들러 등록
signal.signal(signal.SIGINT, signal_handler)

# 작업 실행
run_job()