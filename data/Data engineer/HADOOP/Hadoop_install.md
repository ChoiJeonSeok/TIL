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
### 기본 설정(master)
1. ```sudo apt update && sudo apt -y upgrade && sudo apt install -y vim && sudo apt install -y ssh && sudo service ssh start```
2. host name을 변경한다. 
   1. ip addr show를 통해 ip 주소를 확인하고 메모한다. 
   2. /etc/hostname과 /etc/hosts의 hosts 이름을 변경한다.
      1. sudo hostnamectl set-hostname 새로운_호스트이름
      2. 위 명령어는 hostname과 hosts 모두 변경한다.
   3. sudo reboot 또는 sudo systemctl restart systemd-hostnamed을 사용하여 호스트 이름 변경 사항을 적용한다.
3. 사용자를 생성한다. 보안상 sudo를 사용할 수 없는 사용자로 작업을 하는 것이 옳다고 생각한다.
4. sudo apt install -y openjdk-8-jdk<br>sudo vim /etc/environment
5. 환경변수 설정을 해준다. 
   1. /usr/lib/jvm/java-8-openjdk-amd64를 PATH에 추가한다.
   2. JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"
   3. echo 'export JAVA_HOME="/usr/lib/jvm/java-8-openjdk-amd64"' >> ~/.bashrc
   4. echo 'export HADOOP_HOME="/usr/local/hadoop"' >> ~/.bashrc
   5. source ~/.bashrc
6. hadoop을 다운받는다. (버전은 예시임)
   1. wget https://dlcdn.apache.org/hadoop/common/hadoop-3.3.5/hadoop-3.3.5.tar.gz
   . tar -xf hadoop-3.3.5.tar.gz
   . sudo mv hadoop-3.3.5 /usr/local/hadoop
   6. $HADOOP_HOME/etc/hadoop/hadoop-env.sh 파일에 환경변수를 추가한다.
      1. export JAVA_HOME=/usr/lib/jvm/gjava-8-openjdk-amd64
      2. export HADOOP_HOME=/usr/local/hadoop
      3. export HADOOP_PID_DIR=/usr/local/hadoop/pids
7. core-site.xml 파일 수정
   1. sudo vim $HADOOP_HOME/etc/hadoop/core-site.xm
   ```
   <configuration>
      <property>
         <name>fs.defaultFS</name>
         <value>hdfs://master:9000</value>
      </property>
      <property>
         <name>hadoop.tmp.dir</name>
         <value>/usr/local/hadoop/hadoop-data</value>
      </property>
   </configuration>
   ```
8. hdfs-site.xml 파일 수정
   1. sudo vim $HADOOP_HOME/etc/hadoop/hdfs-site.xml
   ```
   <configuration>
      <property>
         <name>dfs.replication</name>
         <value>1</value>
      </property>
      <property>
         <name>dfs.namenode.name.dir</name>
         <value>file:/usr/local/hadoop/data/dfs/namenode</value>
      </property>
      <property>
         <name>dfs.namenode.http-address</name>
         <value>master:9870</value>
      </property>
      <property>
         <name>dfs.namenode.secondary.http-address</name>
         <value>worker01:9868</value>
      </property>
      <property>
         <name>dfs.namenode.checkpoint.dir</name>
         <value>file:/usr/local/hadoop/hdfs/namesecondary</value>
      </property>
      <property>
         <name>dfs.datanode.data.dir</name>
         <value>file:/usr/local/hadoop/data/dfs/datanode</value>
      </property>
   </configuration>
   ```
9. yarn-stie.xml 파일 수정
   1.  sudo vim $HADOOP_HOME/etc/hadoop/yarn-site.xml
   ```
   <configuration>
      <property>
         <name>yarn.resourcemanager.hostname</name>
         <value>master</value>
      </property>
      <property>
         <name>yarn.nodemanager.aux-services</name>
         <value>mapreduce_shuffle</value>
      </property>
      <property>
         <name>yarn.nodemanager.aux-services.mapreduce.shuffle.class</name>
         <value>org.apache.hadoop.mapred.ShuffleHandler</value>
      </property>
   <!-- Site specific YARN configuration properties -->

   </configuration>
   ```
10. mapred-site.xml 파일 수정
    1.  sudo vim $HADOOP_HOME/etc/hadoop/mapred-site.xml
   ```
   <configuration>
      <property>
         <name>mapreduce.framework.name</name>
         <value>yarn</value>
      </property>
      <property>
         <name>mapreduce.jobhistory.address</name>
         <value>master:10020</value>
      </property>
      <property>
         <name>mapreduce.jobhistory.webapp.address</name>
         <value>master:19888</value>
      </property>
   </configuration>
   ```
11. worker 파일 수정
    1.  sudo vim $HADOOP_HOME/etc/hadoop/workers
    2.  worker01
    3.  worker02
    4.  worker03
12. 설정 완료. 파일 전송 과정 시작.
### hadoop 파일 전송(master)

1. cd /usr/local
2. sudo tar -czf hadoop.tar.gz hadoop
3. sudo chown -R ubuntu:ubuntu /usr/local/hadoop.tar.gz
4. sudo chmod -R 750 /usr/local/hadoop.tar.gz
5. ls -l /usr/local/hadoop.tar.gz -> 권한 확인
6. scp hadoop.tar.gz ubuntu@{호스트명}:/home/ubuntu/  
7. ssh ubuntu@{호스트명} "cd /home/ubuntu; tar xfz hadoop.tar.gz; rm hadoop.tar.gz"

### hadoop 그룹 및 사용자 권한 설정(master, worker 모두)
1. sudo chown -R ubuntu:ubuntu /usr/local/hadoop
2. sudo chmod -R 700 /usr/local/hadoop
3. reboot
4. ssh-copy-id는 master, worker 모두를 대상으로 실행.
   1. master 역시 자기 자신에 대해 인증 절차 없이 접속할 수 있어야 한다.

### hadoop 실행
1. (최초) $HADOOP_HOME/bin/hdfs namenode -format
2. $HADOOP_HOME/sbin/start-dfs.sh
3. $HADOOP_HOME/sbin/start-yarn.sh
4. $HADOOP_HOME/bin/mapred --daemon start historyserver

### hadoop 종료
1. $HADOOP_HOME/sbin/stop-dfs.sh
2. $HADOOP_HOME/sbin/stop-yarn.sh
3. $HADOOP_HOME/bin/mapred --daemon stop historyserver

### hadoop 일괄 실행 / 종료
1. $HADOOP_HOME/sbin/start-all.sh
2. $HADOOP_HOME/sbin/stop-all.sh
- 같이 실행되길 바라는 프로그램이 있다면 start-all.sh와 stop-all.sh에 실행/종료 명령어를 추가한다.

### hadoop test
- hadoop만 입력해도 실행될 수 있게 환경변수 설정
1. $HADOOP_HOME/bin/hadoop fs -ls /
2. echo 'export PATH=\$PATH:\$HADOOP_HOME/bin' >> ~/.bashrc
3. echo 'export PATH=\$PATH:\$HADOOP_HOME/sbin' >> ~/.bashrc
4. source ~/.bashrc
5. hadoop fs -ls /
6. touch file.txt && echo "Hello, world!" > file.txt
7. hadoop fs -put file.txt /file.txt
8. hadoop fs -ls /
9. hadoop fs -get /file.txt file2.txt
10. hadoop fs -cp /file.txt /file3.txt
11. hadoop fs -ls /
12. hadoop fs -rm /file3.txt
13. hadoop fs -ls /
14. 이외에도 chmod, chown 등의 명령어로 권한과 소유권을 변경할수도 있다.