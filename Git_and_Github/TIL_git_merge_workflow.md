# Branch Merge
> branch를 통해 독립된 작업 공간을 마련했다. 작업이 끝난 후 그 내용을 master에 반영하려고 한다. 

## [1] git merge
- 분기된 branch들을 하나로 병합하는 명령어
- git merge <합칠 branch 이름>
- merge 하기 전에 합치려고 하는 main branch로 HEAD를 switch 해야 한다. 
- A를 B에 합치고 싶다면 B로 이동을 한 뒤 git merge A를 한다.
```
# 1. 현재 branch1과 branch2가 있고, HEAD가 가리키는 곳은 branch1 입니다.
$ git branch
* branch1
  branch2

# 2. branch2를 branch1에 합치려면?
$ git merge branch2

# 3. branch1을 branch2에 합치려면?
$ git switch branch2
$ git merge branch1
```
### (1) Merge의 세 종류
1. Fast-Forward
    - branch를 병합할 떄 마치 빨리감기처럼 branch가 가리키는 commit을 앞으로 이동시키는 것.
    1. 현재 master는 C2 commit을 hotfix는 C4 commit을 가리킨다.
![Untitled](https://user-images.githubusercontent.com/82266289/224902756-a30308ac-feab-49fe-9cea-25cea1535f73.png)
    2. master에 hotfix를 병합한다.
    3. hotfix가 가리키는 C4는 C2에 기반한 commit이므로, master가 C4에 이동하게 된다. 
    따로 merge의 과정 없이 branch의 포인터가 이동하는 것을 Fast-Forward라고 한다.
    ![Untitled](https://user-images.githubusercontent.com/82266289/224904018-3051ce0b-00b5-4708-8f42-2bf5a4587d1e.png)
    4. 병합이 완료된 hotfix는 더 이상 필요하지 않다. 따라서 삭제한다.<br>
    git branch -d hotfix
<br><br>
2. 3-Way Merge
    - branch를 병합할 때 각 branch의 commit 두 개와 공통 조상 하나를 사용하여 병합하는 것.
    - 두 branch에서 다른 파일 혹은 같은 파일의 다른 부분을 수정했을 때 가능하다.
    1. 현재 master는 C4 commit을, iss53는 C5 commit을 가리키고 있다. 이 경우 master와 iss53의 공통 조상은 C2 commit이다.
    ![Untitled](https://user-images.githubusercontent.com/82266289/224904514-cda5ca94-ae07-41b4-a8d7-68a5b558beb0.png)
    2. master에 iss53을 병합한다.
    3. master와 iss53은 갈래가 나누어져 있다. 따라서 Fast-Forward로 합쳐질 수 없다. 대신, 두 branch의 공통 조상인 C2와 각자가 가리키는 commit인 C4, C5를 비교하여 3-way merge를 진행한다.
    ![Untitled](https://user-images.githubusercontent.com/82266289/224904857-60af7fd0-1849-4383-9c24-d455ec2dbd7a.png)
    4. C6가 새로 생기게 되는데 이는 master와 iss53이 병합되면서 발생한 Merge Commit이다. 
    5. iss53은 필요없으므로 삭제한다.<br>git branch -d iss53
<br><br>
3. Merge Confilct
   - 병합하는 두 branch에서 같은 파일의 같은 부분을 수정하면, Git은 어느 branch의 내용으로 작성해야 하는지 알지 못하므로 충돌이 발생함.
   - 사용자가 직접 내용을 선택해서 Confilct를 해결해야 한다.
   - 해당 파일을 수정한 뒤 add, commit한다.
   - Vim 편집기를 이용해서 commit 내역을 수정할 수도 있다. 그 내역이 새로운 commit이 된다. 필요없어진 branch를 삭제하면 끝이다.

# Git 협업의 기초
- [Git workflow 개념](https://real-atom-0b1.notion.site/10-Git-workflow-3bf780f0c9464d809992a89fdb812777)