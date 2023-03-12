### Github profile
- Github 사용자 이름으로 공개 repository를 만들면 profile 화면을 설정할 수 있다.
- 이 repository에는 README.md 파일이 있으며 이 곳에 어떻게 profile을 설정할 것인지 작성하게 된다. 
- 나는 github-readme-stats를 이용해서 간단하게 내 github을 표현했다.  
- [github-readme-stats](https://github.com/anuraghazra/github-readme-stats)

# 원격 저장소에서 로컬 저장소로.

## [1] 원격 저장소 가져오기

### (1) git clone
- 원격 저장소의 commit 내역을 모두 가져와서, 로컬 저장소를 생성하는 명령어.
- commit은 코드 변경 내역을 저장하는 것을 의미한다. 변경 사항을 저장했기 때문에 이를 이용해서 코드를 이전 버전으로 되돌릴 수 있다.
- git clone <원격 저장소 주소>
- git init과 git remote add는 자동으로 진행되어 있다.

### (2) git pull
- 원격 저장소의 변경 사항을 가져와서, 로컬 저장소를 업데이트하는 명령어.
- git pull <저장소 이름> <브랜치 이름>
- 브랜치가 master 하나만 있고 이미 연결되어 있다면, git pull만 해도 가능하다.