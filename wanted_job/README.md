main_crawling.ipynb   ==> 메인 크롤링 노트북  
wanted.csv            ==> engineering 하기 전 raw data  
year_id_df.csv        ==> year_creat 함수로 크롤링한 데이터 year_mapping할때 사용   
result.csv            ==> 전처리 끝낸 최종 csv  

---------------------------------------------------  
개발일지
https://www.notion.so/71a54809c6cf43749e5b2a967105f4aa

------------------------------------------------------  
[프로젝트 개요]  
  
이번 프로젝트는 구인구직 플랫폼 크롤링을 통해 구인구직 정보를 수집하고 분석하는 것을 목적으로 진행되었습니다.  
  
[프로젝트 진행 과정]  
  
- 크롤링을 통한 데이터 수집  
BeautifulSoup을 이용하여 Wanted 사이트의 채용 정보 페이지를 크롤링하였습니다.  
  
- 데이터 전처리  
수집한 데이터는 정제되지 않은 상태였기 때문에, 전처리를 통해 데이터를 정제하였습니다.  
전처리 작업으로는 중복 제거, 결측치 처리, 새로운 컬럼 추가 등이 포함되었습니다.  
  
[데이터세트 개요]  
- shape  
933 rows × 23 columns  
- columns
  - id : 고유 id
  - due_time : 근무일
  - skill_tag : 기술스택
  - company_tags : 회사를 설명하는 키워드
  - position : 직무
  - category_tags : 업무
  - address.country : 국가
  - address.full_loaction : 회사 주소 (포맷이 일정하지 않음)
  - address.geo_location.n_location.lat : 회사 위도
  - address.geo_location.n_location.lng : 회사 경도
  - address.geo_location.location_type : 좌표 타입
  - address.location : 지역
  - address.country_code : 국가 코드
  - detail.requirements : 채용 요구사항
  - detail.main_tasks : 주요 업무
  - detail.preferred_points : 우대 사항
  - company.industry_name : 산업명
  - company.application_response_stats.avg_rate : 지원에 대한 평균 응답률
  - company.application_response_stats.avg_day : 하루 평균 지원 수
  - company.name : 회사명
  - logo_img.origin : 회사 로고
  - url : 채용 공고 게시물 주소
  - year : 요구 경력

  
[추후 과제]
- 통계분석을 통한 트렌드 분석  
- 직무별 선호하는 기술스택이 있는가
- 경력별 직무 분포도
- 사용자가 웹을 통해서 자신의 경험과 기술스택을 기반으로 공고 추천하는 서비스 제작

[활용 예시]
<br>
<img width="785" alt="example" src="https://user-images.githubusercontent.com/110758221/220267713-a50af7b9-b768-4810-a5e9-66c26770e47b.png">




