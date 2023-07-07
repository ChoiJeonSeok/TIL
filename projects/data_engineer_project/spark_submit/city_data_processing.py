import subprocess
import time
import signal
import datetime
import csv
import sys

start_time = None

# Signal 핸들러 함수 정의
def signal_handler(sig, frame):
    print("Received signal to stop the program")

    global start_time
    if start_time is not None:
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

        # 프로그램이 얼마나 작동되었는지 로그 파일에 기록
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"{current_time} - Program executed for {duration_str}\n"
        with open("log.txt", "a") as log_file:
            log_file.write(log_message)

    sys.exit(0)

# Spark Submit 명령어 실행 함수 정의
def run_spark_submit(master_url, app_name, script_path):
    command = f"spark-submit --master {master_url} --name {app_name} {script_path}"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    # 확인 메시지 출력
    print("Spark Submit completed successfully")
    return output

# CSV 파일을 Hadoop에 이동하는 함수 정의
def move_csv_to_hadoop(csv_path, hdfs_path):
    move_output_to_hdfs = f"hadoop fs -put {csv_path} {hdfs_path}"
    subprocess.run(move_output_to_hdfs, shell=True)
    # 확인 메시지 출력
    print("Seoul city data CSV file moved to Hadoop successfully")

# 작업 실행 함수 정의
def run_job(duration_hours, url):
    # 전역 변수 start_time에 접근
    global start_time

    # 작업 시작 시간 기록
    start_time = time.time()

    # 작업 실행 및 작동 시간 계산
    while True:
        run_spark_submit(url["master_url"], url["app_name"], url["script_path"])
        move_csv_to_hadoop(url["csv_path"], url["hdfs_path"])
        time.sleep(3600)

        # 작동 시간 체크
        if duration_hours != 0:
            elapsed_time = time.time() - start_time
            if elapsed_time >= duration_hours * 3600:
                break

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

    # 프로그램이 얼마나 작동되었는지로그 파일에 기록
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{current_time} - Program executed for {duration_str}\n"
    with open("log.txt", "a") as log_file:
        log_file.write(log_message)

# Signal 핸들러 등록
signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) < 2:
    print("작동 시간을 입력하세요. 예: python your_program.py 3")
else:
    duration_hours = int(sys.argv[1])

    # CSV 파일에서 URL 행을 로드
    with open("url.csv", "r") as csv_file:
        reader = csv.DictReader(csv_file)
        url = next(reader)  # 첫 번째 행을 가져옴

    run_job(duration_hours, [url])  # 단일 URL을 리스트에 담아서 전달

    # # CSV 파일에서 URL들을 로드
    # urls = []
    # with open("urls.csv", "r") as csv_file:
    #     reader = csv.DictReader(csv_file)
    #     for row in reader:
    #         urls.append(row)
    
    # run_job(duration_hours, urls)