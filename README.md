# Intro-to-SE-TeamProj-Backend

소프트웨어공학개론 팀프로젝트 백엔드

**배포 완료되었습니다**

API 서버 주소:
https://port-0-intro-to-se-teamproj-backend-7hqac2alhil3qhz.sel4.cloudtype.app

요청 예시:
GET https://port-0-intro-to-se-teamproj-backend-7hqac2alhil3qhz.sel4.cloudtype.app/stores (모든 가게 정보 불러오기)

## API 명세서

### 로그인 / 회원가입 관련 api

- POST /users/login
  - 로그인 기능
  - {"id": id, "password": pw} 형식으로 폼데이터 날려주세요
  - 로그인 성공 시 access_token 쿠키에 토큰이 저장됩니다. 200 OK
  - 로그인 실패 시 404 NOT FOUND 에러가 발생합니다.
- GET /users/logout
  - 로그아웃 기능
  - access_token 쿠키의 내용을 삭제합니다.
  - 성공 시 200 OK
- POST /users/signup
  - 회원가입 기능
  - {"id": id, "password": pw} 형식으로 폼데이터 날려주세요
  - 회원가입 성공 시 200 OK
  - 회원가입 실패 시 400 BAD REQUEST 에러가 발생합니다.
- GET /users/logincheck
  - 로그인 상태를 체크합니다. (로그인해야 접속 가능한 페이지 구현용)
  - 토큰이 만료되지 않은 경우(로그인 상태인 경우) 200 OK
  - 토큰이 만료되었거나 로그인 상태가 아닌 경우 401 UNAUTHORIZED 에러가 발생합니다.

### 식당 정보 관련 api

- GET /stores

  - 모든 가게 정보 보여주기
  - 반환 예시:
    ```
    [
      {
      "restaurant_name": "수해복마라탕",
      "address": "경기 수원시 장안구 서부로",
      "image_url": "url",
      "category": "중식",
      "id": 1
      },
      {
      "restaurant_name": "미가라멘",
      "address": "수원시 장안구 화산로221",
      "image_url": "url",
      "category": "일식",
      "id": 2
      }
    ]
    ```

- GET /stores/:가게id

  - 가게 상세 정보 보여주기
  - {"name": 가게이름, "address": 가게주소, "image_url": 이미지 url, "primary_tags": 대표태그번호} 반환
  - 반환 예시:

  ```
  {
    "name": "마왕족발",
    "address": "수원시 장안구 화산로221",
    "image_url": "url",
    "primary_tags": ["4","5"]
  } // primary_tags는 리스트입니다.(값이 여러개인 경우가 있기 때문에)
  ```

  - tag 1: 밥약
  - tag 2: 오늘은 거하게
  - tag 3: 동아리 회식
  - tag 4: 데이트 맛집
  - tag 5: 어른들과 약속
  - tag 6: 가성비최고
  - tag 7: 비싸도 맛있어

- GET /stores/categories/:세부카테고리

  - 세부카테고리에 맞는 가게 정보 모아서 가져오기
  - 세부카테고리: 공유 문서에 있는 세부카테고리 그대로 써 주시되, "족발&보쌈", "탕&찌개"와 같이 특수문자 있는경우 "족발보쌈", "탕찌개" 로 붙여서 쓰는것으로 해 주세요
  - 반환 예시(모든 카테고리 가져오기와 동일한데 카테고리 같은거만 분류돼서 반환):

  ```
    [
      {
      "restaurant_name": "바른스시",
      "address": "경기 수원시 장안구 서부로",
      "image_url": "url",
      "category": "일식",
      "id": 1
      },
      {
      "restaurant_name": "미가라멘",
      "address": "수원시 장안구 화산로221",
      "image_url": "url",
      "category": "일식",
      "id": 2
      }
    ]
  ```

- GET /stores/tags/:태그번호

  - 태그 번호에 맞는 가게 정보 모아서 가져오기 - 해당 태그를 많이 받은 순서대로
  - {"name": 가게이름, "address": 가게주소, "image_url": 이미지주소}[]

- GET /stores/:가게id/reviews

  - id에 맞는 가게 리뷰(Tag 목록 - 어떤 태그가 몇개 추천받았는지) 가져오기

- POST /stores/:가게id/reviews

  - 리뷰 작성(태그 추가)
  - 유저가 선택한 태그에 대해서는 1, 선택하지 않은 태그에 대해서는 0으로 폼데이터 보내주세요(tag1 ~ tag7이 모두 와야합니다)
  - 예시(유저가 tag1과 tag4를 선택한 경우):

  ```
  {"tag1": 1, "tag2": 0, "tag3": 0, "tag4": 1, "tag5": 0, "tag6": 0, "tag7": 0}
  ```

  - tag 1: 밥약
  - tag 2: 오늘은 거하게
  - tag 3: 동아리 회식
  - tag 4: 데이트 맛집
  - tag 5: 어른들과 약속
  - tag 6: 가성비최고
  - tag 7: 비싸도 맛있어
