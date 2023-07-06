import subprocess
import time
import signal
import datetime
import sys

is_running = True  # 작업을 계속 실행할지 여부를 저장하는 변수

# Signal 핸들러 함수 정의
def signal_handler(sig, frame):
    global is_running
    print("Received signal to stop the program")
    is_running = False

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
def run_job(duration_hours):
    # 작업 시작 시간 기록
    start_time = time.time()

    # 작업 실행 및 작동 시간 계산
    while is_running:
        run_spark_submit()
        move_csv_to_hadoop()
        time.sleep(3600)

        # 작동 시간 체크
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

    # 로그 파일에 기록
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{current_time} - Program executed for {duration_str}\n"
    with open("log.txt", "a") as log_file:
        log_file.write(log_message)

# Signal 핸들러 등록
signal.signal(signal.SIGINT, signal_handler)

if len(sys.argv) < 2:
    print("작동 시간을 입력하세요. 3시간 작동 예: python city_data_processing.py 3")
else:
    duration_hours = int(sys.argv[1])
    run_job(duration_hours)

# 작동 시간을 매개변수로 입력받아 작업을 실행하는 부분을 변경하였습니다. 
# `run_job()` 함수의 매개변수로 작동 시간을 시간 단위로 입력받습니다. 
# `elapsed_time` 변수를 사용하여 경과한 시간을 체크하고, 
# 입력받은 작동 시간(`duration_hours`)을 초과하면 작업을 종료합니다.

