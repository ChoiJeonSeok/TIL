1. 가상 머신 설정
2. Java 설치
3. Hadoop 다운로드
4. Hadoop 설치
5. Hadoop 환경 설정
6. 호스트 파일 수정
7. Hadoop 분산 모드 설정
8. Hadoop 클러스터 실행


2023-06-17에 수업 과정의 설치 방법과, chat-gpt의 설치 방법을 비교하며, 무엇이 어떻게 다른지, 어떤 질문을 AI에게 던지면 수업 과정에서 배운 설치 방법을 답변하게 할 수 있는지 시도할 예정이다.

설치는 수업 과정에서 배운 방법으로 진행한다. 그러나 하던 도중 AI가 더 간결하고 똑같은 결과를 가져오는 방법을 발견하면, 정말 그런지 인터넷에 검색을 통해 알아보고, 시도해본다.

# quick 설치. 간략한 과정 소개
1. ```sudo apt update && sudo apt -y upgrade && sudo apt install -y vim && sudo apt install -y ssh && sudo service ssh start```
2. host name을 변경한다. 
   1. **ip addr show**를 통해 ip 주소를 확인하고 메모한다. 
   2. /etc/hostname과 /etc/hosts의 hosts 이름을 변경한다.
      1. **sudo hostnamectl set-hostname 새로운_호스트이름**으로 한 번에 바꿀 수 있다.
   3. **sudo reboot** 또는 **sudo systemctl restart systemd-hostnamed**을 사용하여 호스트 이름 변경 사항을 적용한다.