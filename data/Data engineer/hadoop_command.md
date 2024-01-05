# 하둡(Hadoop) 파일시스템 (HDFS) 사용자 명령어

### 파일 및 디렉토리 조회 및 정보 확인
- `hdfs dfs -ls [PATH]`: 지정된 경로의 파일 및 디렉토리 목록을 표시한다.
- `hdfs dfs -du PATH [PATH ...]`: 파일 크기를 나타낸다.
- `hdfs dfs -dus PATH [PATH ...]`: du와 비슷하게 파일 크기를 나타낸다.
- `hdfs dfs -stat FORMAT PATH`: 지정된 파일이나 디렉토리에 대한 통계 정보를 보여준다.
- `hdfs dfs -tail FILE`: 지정된 파일의 마지막 부분을 출력한다.

### 파일 및 디렉토리 관리
- `hdfs dfs -mkdir [PATH]`: 새 디렉토리를 생성한다.
- `hdfs dfs -rm [-r] PATH`: 파일 또는 디렉토리를 삭제한다.
- `hdfs dfs -mv SRC DST`: 파일 또는 디렉토리를 새 위치로 이동한다.
- `hdfs dfs -touchz FILE`: 새로운 파일을 생성하거나, 이미 존재하는 파일의 타임스탬프를 현재 시간으로 갱신한다.

### 파일 및 디렉토리 권한 및 소유권 관리
- `hdfs dfs -chgrp [-R] GROUP PATH [PATH ...]`: 파일과 디렉토리에 대한 그룹을 변경한다.
- `hdfs dfs -chmod [-R] MODE [, MODE ...] PATH [PATH ...]`: 파일과 디렉토리의 권한을 변경한다.
- `hdfs dfs -chown [-R] [OWNER] [: [GROUP]] PATH [PATH ...]`: 파일과 디렉토리의 소유자를 변경한다.

### 파일 복사 및 이동
- `hdfs dfs -copyFromLocal LOCALSRC [ LOCALSRC ...] DST`: 로컬 파일 시스템으로부터 파일들을 복사한다.
- `hdfs dfs -copyToLocal [-ignorecrc] [-crc] SRC [SRC ...] LOCALDST`: 파일들을 로컬 파일 시스템으로 복사한다.
- `hdfs dfs -cp SRC [SRC ...] DST`: 소스에 있는 파일들을 목적지로 복사한다.
- `hdfs dfs -getmerge SRC DST`: 여러 파일을 하나의 파일로 병합하여 로컬 파일 시스템으로 복사한다.

### 검색 및 카운트
- `hdfs dfs -find PATH -name PATTERN`: 주어진 패턴과 일치하는 파일 또는 디렉토리를 검색한다.
- `hdfs dfs -count [-q] PATH [PATH ...]`: PATH에 있는 모든 파일과 디렉토리에 대한 이름, 사용된 바이트 수, 파일 개수, 하위 디렉토리 개수를 출력한다.
- `hdfs dfs -df [-h] [PATH]`: HDFS의 사용 가능한 공간과 사용 중인 공간을 보여준다.

### 파일 내용 보기
- `hdfs dfs -cat FILE [FILE ...]`: 파일의 내용을 나타낸다.