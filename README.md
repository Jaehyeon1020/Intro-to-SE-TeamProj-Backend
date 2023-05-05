# Intro-to-SE-TeamProj-Backend

소프트웨어공학개론 팀프로젝트 백엔드

## API 명세서

### 로그인 / 회원가입 관련 api

- POST /users/login
  - 로그인 기능
  - {"id": id, "password": pw} 형식으로 폼데이터 날려주세요
- GET /users/logout
  - 로그아웃 기능(회의 필요)
- POST /users/signup
  - 회원가입 기능
  - {"id": id, "password": pw} 형식으로 폼데이터 날려주세요

### 식당 정보 관련 api

- GET /stores

  - 모든 가게 정보 보여주기

- GET /stores/:가게id

  - 가게 상세 정보 보여주기
  - {"name": 가게이름, "address": 가게주소, "image_url": 이미지 url, "primary_tags": 대표태그번호} 반환
  - 반환 정보 예시: {
    "name": "마왕족발",
    "address": "수원시 장안구 화산로221",
    "image_url": "url",
    "primary_tags": ["4","5"]
    } // primary_tags는 리스트입니다.(값이 여러개인 경우가 있기 때문에)
  - tag 1: 밥약
  - tag 2: 오늘은 거하게
  - tag 3: 동아리 회식
  - tag 4: 데이트 맛집
  - tag 5: 어른들과 약속
  - tag 6: 가성비최고
  - tag 7: 비싸도 맛있어

- GET /stores/:가게id/reviews

  - id에 맞는 가게 리뷰 가져오기

- POST /stores/:가게id/reviews

  - 리뷰 작성
  - {"tags": [태그1, 태그2, 태그3 ... ]} 형식으로 폼데이터 날려주세요

- GET /stores/:세부카테고리

  - 세부카테고리에 맞는 가게 정보 모아서 가져오기
  - {"name": 가게이름, "address": 가게주소, "image_url": 이미지주소}
  - 세부카테고리: 공유 문서에 있는 세부카테고리 그대로 써 주시되, "족발&보쌈", "탕&찌개"와 같이 특수문자 있는경우 "족발보쌈", "탕찌개" 로 붙여서 쓰는것으로 해 주세요

- GET /stores/:태그

  - 태그에 맞는 가게 정보 모아서 가져오기
  - {"name": 가게이름, "address": 가게주소, "image_url": 이미지주소}[]
