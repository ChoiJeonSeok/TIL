# Github
## [1] 원격 저장소(Remote Repository)
> 내가 소유하고 있는 컴퓨터는 로컬 저장소라고 한다. 이는 한정된 공간이며 컴퓨터가 없는 공간으로 가면 버전 관리를 진행할 수 없다. 이로 인해 원격 저장소의 필요성이 대두되었다. <br> Github는 원격 저장소를 이용해 버전 관리를 할 수 있으며, 내 로컨 저장소를 다른 사람과 공유할 수 있다. 즉, Github를 통하면 협업을 더욱 효율적으로 할 수 있다.
<br>

### (1) Github 원격 저장소 생성 및 연결
```
1. New repository를 생성한다.
2. 저장소의 이름, 설명, 공개 여부를 선택하고 Create repository 한다.
3. 원격 저장소가 생성되었으면 저장소의 주소를 복사한다. HTTPS와 SSH가 있으니 용도에 맞게 복사한다.
4. 원하는 dir로 가서 
4-1."git clone <주소> <폴더명>"
    폴더명을 작성하면 그 이름을 가진 폴더가 생성된다. 
4-2. git init
    해당 디렉토리에 .git 파일을 추가하여 git 저장소와 연결할 준비를 한다. 
    절대 home 디렉토리와 같이 하위 폴더 및 파일이 많은 곳에서는 실행해서는 안되는 명령어이다. 컴퓨터의 모든 파일을 git으로 관리할 필요는 없다.
5. git init으로 했다면 
    $ git remote add origin https://github.com/ChoiJeonSeok/TIL.git
    origin이라는 이름으로 링크의 원격 저장소를 연결했다.
- git remote -v : 조회
- git remote rm <이름> : 삭제 (rm 대신 remove 가능.)
```
<br>

### (2) 원격 저장소에 업로드
```
1. 로컬 저장소에서 커밋을 생성한 후 원격 저장소에 폴더 및 파일을 업로드 할 수 있다.
2. git status : 현재 git 업로드 관련 상태 조회
3. git add <해당파일이름 or . or --all>
    : 해당파일만 업로드 준비 or 생성되거나 변경된 모든 파일 업로드 준비
4. git commit -m "<commit message>"
5. git log --oneline : 한 줄로 로그 확인
- commit은 어떤 변화가 일어났는지 최대한 자세하게 작성하는 것이 올바르다.
6. git push origin master : origin이라는 이름의 원격 저장소의 master branch에 업로드
or
git push -u origin master
이후 해당 디렉토리에서는 git push만 입력 가능
```
<br>

### (3) 간단한 그림으로 보는 Github 사용 과정
![Untitled](https://user-images.githubusercontent.com/82266289/224491303-00ab586c-dac6-4dd3-9cc2-49489601e067.png)