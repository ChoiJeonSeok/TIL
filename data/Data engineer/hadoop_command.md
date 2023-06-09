# 하둡(Hadoop) 파일시스템 (HDFS) 명령어 10가지

1. `hdfs dfs -cat FILE [FILE ...]`
   <br> 
   - 파일의 내용을 나타낸다.
2. `hdfs dfs -chgrp [-R] GROUP PATH [PATH ...]` 
   - 파일과 디렉토리에 대한 그룹을 변경한다.
3. `hdfs dfs -chmod [-R] MODE [, MODE ...] PATH [PATH ...]`
   - 파일과 디렉토리의 권한을 변경한다.
4. `hdfs dfs -chown [-R] [OWNER] [ : [GROUP]] PATH [PATH ...]`
   - 파일과 디렉토리의 소유자를 변경한다.
5. `hdfs dfs -copyFromLocal LOCALSRC [ LOCALSRC ...] DST`
   - 로컬 파일 시스템으로부터 파일들을 복사한다.
6. `hdfs dfs -copyToLocal [-ignorecrc] [-crc] SRC [SRC ...] LOCALDST`
   - 파일들을 로컬 파일 시스템으로 복사한다.
7. `hdfs dfs -count [-q] PATH [PATH ...]`
   - PATH에 있는 모든 파일과 디렉토리에 대한 이름, 사용된 바이트 수, 파일 개수, 하위 디렉토리 개수를 출력한다.
8. `hdfs dfs -cp SRC [SRC ...] DST`
   - 소스에 있는 파일들을 목적지로 복사한다.
9.  `hdfs dfs -du PATH [PATH ...]`
    - 파일 크기를 나타낸다.
10. `hdfs dfs -dus PATH [PATH ...]`
    - du와 비슷하게 파일 크기를 나타낸다.