# 2021.bootcamp
django project

## -project 일정
   2021.12.17 부트 캠프 시작, 직업 강의 </br>
   2022.1.1   1차 과제: 기획서 제출 </br>
   2022.1.8   2차 과제: 기본 가상환경 설정(PyCharm 사용), 메인화면 구성, django를 이용한 데이터 정리 </br>
   2022.1.15  3차 과제: navbar와 footer의 템플릿화, 로그인/로그아웃 서비스 </br>
   2022.1.22  4차 과제: 댓글 서비스, 회사 소개 페이지 등 구성 </br>

## -실제 구성 화면
    1. 메인화면 입니다. navbar와  footer 사이 회사의 정체성을 알 수 있는 메인 이미지를 넣고, 회사에 대한 설명은 적을 수 있도록 만들었습니다.
<img src="https://user-images.githubusercontent.com/93725108/153582224-085a3e7b-3cc7-44ff-bf96-28f07355316c.PNG">
    2. 회사 소개 페이지 입니다.
      우선 들어가자마자 나오는 메인 레이아웃에는 회사의 다짐 등을 적을 수 있습니다. 버튼은 각각 회사를 소개해 주는 레이아웃과 회사의 위치에 대해 설명해주는 지도 링크로 연결됩니다. 
      그 밑으로는 회사의 이벤트나 특징 등, 그리고 고객의 리뷰들이 적혀 있습니다. 이 두개의 리뷰는 가장 최근에 적힌 상품의 리뷰들이 올라갑니다.
<img src="https://user-images.githubusercontent.com/93725108/153582230-c5a1a6e9-b48e-43d6-af39-b0236b245baf.PNG">
    3. 가장 중심이 되는 제품 소개 페이지입니다. 메인레이아웃에는 신메뉴 소개란이, 밑에는 다른 제품 혹은 이벤트를 홍보하는 작은 배너들이 있습니다.
<img src="https://user-images.githubusercontent.com/93725108/153582237-93de12e6-91cb-4586-9606-295a5aba2328.PNG">
    4. 상품 소개페이지 메인 레이아웃의 'Detail Explanation' 버튼을 클릭하면 상품상세 설명란으로 넘어갑니다. 메인 레이아웃에서는 30자 내로만 보이던 설명이 모두 보입니다. 
       위 페이지는 댓글 기능을 만들었습니다. 각각 댓글을 달고, 해당 계정의 댓글에 관하여 수정 혹은 삭제가 가능합니다. 수정할 시 수정 날짜가 계정 아이디의 옆에 뜹니다.
<img src="https://user-images.githubusercontent.com/93725108/153582261-018bee30-edbd-41be-a9ce-f1909fb6a1b2.PNG">
    5. 로그인 페이지와 회원가입 페이지 입니다. django의 form을 가져와 생성되었습니다.
<img src="https://user-images.githubusercontent.com/93725108/153582276-e603aceb-9e8f-478f-945a-27e0f0313440.PNG">
<img src="https://user-images.githubusercontent.com/93725108/153582282-5cf9eacd-28f7-4e99-9e80-7a545c8e66e0.PNG">
    6. 백엔드는 django로 구현하였습니다. 로그인과 댓글, 제품의 데이터를 관할합니다.
<img src="https://user-images.githubusercontent.com/93725108/153582297-c248ac3f-fe87-413c-aff3-c8bbd665e363.PNG">
