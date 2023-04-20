## column 정보
- survived : 생존여부(1:생존, 0: 사망)
- pclass : 승선권 클래스(1: 1st, 2:2nd, 3:3rd)
- name : 승객 이름
- sex : 승객 성별
- age : 승객 나이
- sibsp : 동반한 형제자매, 배우자 수
- parch : 동반한 부모, 자식 수
- ticket : 티켓의 고유 넘버
- fare : 티켓의 요금
- cabin : 객실 번호
- embarked : 승선한 항구명 (C:Cherbourg, Q:Queenstown, S:Southampton)
- boat
- body
- home.dest

# 결측치 및 중복 처리
![dd](https://user-images.githubusercontent.com/82266289/233369529-dd53c5b5-f256-4633-bed8-5c525f4caeac.png)

- titanic.shape => (1309, 14)
  
### 중복 확인
- titanic[titanic.duplicated()].sum()
- 

<table>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/82266289/233369909-f5a9822b-68c6-42a3-aff8-0220783b57a2.png" alt="Image 1"></td>
    <td><img src="https://user-images.githubusercontent.com/82266289/233370108-097b47dc-45f1-4f8d-8fff-f4e4ee1eb95b.png" alt="Image 2"></td>
  </tr>
  <tr>
    <td><img src="https://user-images.githubusercontent.com/82266289/233370156-223efa1e-34bd-4897-a317-c97332b3479f.png" alt="Image 3"></td>
    <td><img src="https://user-images.githubusercontent.com/82266289/233370182-e3066f98-9fc5-40a6-b790-5d5e7284e3f6.png" alt="Image 4"></td>
  </tr>
</table>

