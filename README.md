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
- GET /stores/:가게id/reviews
  - id에 맞는 가게 리뷰 가져오기
- POST /stores/:가게id/reviews
  - 리뷰 작성
  - {"tags": [태그1, 태그2, 태그3 ... ]} 형식으로 폼데이터 날려주세요
