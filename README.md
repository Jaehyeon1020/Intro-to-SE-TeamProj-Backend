# Intro-to-SE-TeamProj-Backend

소프트웨어공학개론 팀프로젝트 백엔드

## API 명세서

### 로그인 / 회원가입 관련 api

- POST /users/login
  - 로그인 기능
  - {"id": id, "password": pw} 형식으로 폼데이터 날려주세요
- GET /users/logout
  - 로그아웃 기능
- POST /users/signup
  - 회원가입 기능
  - {"id": id, "password": pw} 형식으로 폼데이터 날려주세요

### 식당 정보 관련 api

- GET /stores
  - 모든 가게 정보 보여주기
- GET /stores/:가게id
  - 가게 상세 정보 보여주기
  - {"name":가게이름, "address":가게주소, "phone":가게전화번호, "primaryTag":대표태그}로 받아서 작업해주세요
- GET /stores/:가게id/reviews
  - id에 맞는 가게 리뷰 가져오기
- POST /stores/:가게id/reviews
  - 리뷰 작성
  - {"tags": [태그1, 태그2, 태그3 ... ]} 형식으로 폼데이터 날려주세요
- GET /stores/:세부카테고리
  - 세부카테고리에 맞는 가게 정보 모아서 가져오기
  - {"name": 가게이름, "address": 가게주소, "imageUrl": 이미지주소}
- GET /stores/:태그
  - 태그에 맞는 가게 정보 모아서 가져오기
  - {"name": 가게이름, "address": 가게주소, "imageUrl": 이미지주소}[]
