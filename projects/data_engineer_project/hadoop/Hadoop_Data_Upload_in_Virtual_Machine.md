## TIL: Hadoop 가상 머신 데이터 업로드와 공유

### 가상 머신에 Hadoop 설치 및 데이터 업로드

1. 가상 머신 생성: VMware를 사용하여 가상 머신 4개를 생성하고, Hadoop 클러스터를 설치한다.
![1_hadoop_실행](https://github.com/ChoiJeonSeok/TIL/assets/82266289/d07c33c6-85dc-4683-89ff-05ac48cc1a7d)<br><br><br>
2. Folder Sharing 설정: VMware에서 "CDATA"라는 이름으로 호스트 컴퓨터의 "C:\Users\art\Downloads\CDATA"와 가상 머신 간의 폴더 공유 설정을 한다.
![2_호스트_가상머신 간 공유폴더 설정](https://github.com/ChoiJeonSeok/TIL/assets/82266289/13e7add2-e5e1-4826-9131-2c4bd7b69ba5)<br><br><br>
3. 데이터 업로드: 호스트 컴퓨터의 "C:\Users\art\Downloads\CDATA" 폴더에 있는 데이터를 가상 머신의 "/mnt/hgfs/CDATA" 또는 "/media/sf_CDATA" 폴더로 복사한다. 
![3_공유폴더 이동 및 파일 확인](https://github.com/ChoiJeonSeok/TIL/assets/82266289/e94828cb-f165-4fc3-8363-a6c58d687b8a)<br><br><br>
4. Hadoop으로 데이터 업로드: 가상 머신 내에서 HDFS로 데이터를 업로드한다.
   ```bash
   hadoop fs -put /mnt/hgfs/CDATA/* ./DATA
   ```
![4_hadoop에 데이터 업로드 후 확인](https://github.com/ChoiJeonSeok/TIL/assets/82266289/ea312943-05c0-4272-a392-dd60f2300f76)