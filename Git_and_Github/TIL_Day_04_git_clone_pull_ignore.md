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
- 장소와 기기가 바뀌는 환경이라면 자주 쓸 기능이다.
- 두 곳 이상의 장소에서 파일을 수정한 경우 발생할 수 있는 상황.
> 1. 내 컴퓨터와 외부 컴퓨터에서 서로 다른 파일을 수정한 경우 
> 2. 같은 파일을 수정했지만, 수정한 라인이 다른 경우
> 3. 같은 파일의 같은 라인을 수정한 경우,
> - 1, 2는 문제 없다. 3은 어느 내용을 반영할지 직접 보고 선택해야 한다.
> - pull 이전에 push하는 경우 원격 저장소의 내용을 먼저 받아오지 않고, 로컬 저장소에서 새로운 commit을 생성했기 때문에 서로의 commit 내역이 달라지게 된다. 충돌이 발생하여 git push가 실패하게 된다. git pull을 통해 원격과 로컬 저장소의 동기화를 시킨 후 새로운 커밋을 쌓아야 한다.

```
 git pull → git add → git commit → git push
 ```

 ## [2] .gitignore
 > 특정 파일 또는 폴더에 대해 Git이 버전 관리를 하지 못하도록 지정하는 리스트가 담긴 문서.

### (1) .gitignore에 작성하는 목록 예시
- 민감한 개인 정보가 담긴 파일
- OS에서 활용되는 파일
- IDE(통합 개발 환경 -pycharm 등) 혹은 Text editor(vscode) 등에서 활용되는 파일

  - <details>
    <summary>예시: pycharm -> .idea/</summary>
    <div markdown="1">

    프로젝트 정보를 포함하는 .idea/ 디렉토리. 이 디렉토리에는 프로젝트 구성 파일이 저장되어 있어, 프로젝트 정보를 보존하고 관리하는 역할을 한다. 예를 들어 pycharm 프로젝트를 다른 컴퓨터로 이전하거나, 혹은 프로젝트를 공유하거나 백업하기 위해서는 .idea/ 디렉토리를 포함하여 전체 프로젝트 디렉토리를 복사하면 된다. 이 방법을 통해 프로젝트 구성 정보를 보존하고, 다른 컴퓨터에서 프로젝트를 동일하게 구성할 수 있다.
- 개발 언어(python) 혹은 프레임워크(django)에서 사용되는 파일
  - 가상 환경 : venv/
  - &#95;&#95;pycache&#95;&#95;/

### (2) .gitignore 작성 시 주의사항.
- 반드시 이름을 .gitignore로 작성할 것.
- .git 파일이 있는 폴더에 생성할 것.
- git add 전에 .gitignore에 작성할 것. git add를 먼저 하면 계속 버전 관리 대상으로 인식된다.

### (3) 유용한 사이트
> [gitignore.io :<br> 개발환경에 맞는 기본적인 .gitignore를 작성해준다.](https://www.toptal.com/developers/gitignore/)

### (4) 패턴 및 예시
### (1) .gitignore 패턴 규칙

1. 아무것도 없는 라인이나, `#`로 시작하는 라인은 무시한다.
2. `슬래시(/)`로 시작하면 하위 디렉터리에 재귀적으로 적용되지 않는다.
3. 디렉터리는 `슬래시(/)`를 끝에 사용하는 것으로 표현한다.
4. `느낌표(!)`로 시작하는 패턴의 파일은 ignore(무시)하지 않는다.
5. **표준 Glob 패턴을 사용한다.**
    - `*(asterisk)`는 문자가 하나도 없거나 하나 이상을 의미한다.
    - `[abc]`는 중괄호 안에 있는 문자 중 하나를 의미한다.
    - `물음표(?)`는 문자 하나를 의미한다.
    - `[0-9]`처럼 중괄호 안에 하이픈(-)이 있는 경우 0에서 9사이의 문자 중 하나를 의미한다.
    - `**(2개의 asterisk)`는 디렉터리 내부의 디렉터리까지 지정할 수 있다.
    (`a/**/z`라고 작성하면 `a/z`, `a/b/z`, `a/b/c/z` 까지 모두 영향을 끼친다.)
> **패턴 예시**<br># .gitignore <br><br># 확장자가 txt인 파일 무시<br>*.txt<br><br># 현재 확장자가 txt인 파일이 무시되지만, 느낌표를 사용하여 test.txt는 무시하지 않음<br>!test.txt<br><br># 현재 디렉터리에 있는 TODO 파일은 무시하고, folder/TODO 처럼 하위 디렉터리에 있는 파일은 무시하지 않음<br>/TODO<br><br># build/ 디렉터리에 있는 모든 파일은 무시<br>build/<br><br># folder/notes.txt 파일은 무시하고 folder/child/arch.txt 파일은 무시하지 않음
<br>folder/*.txt<br><br># folder 디렉터리 아래의 모든 .pdf 파일을 무시<br>folder/**/*.pdf