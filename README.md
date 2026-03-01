# Corporate Data Management Standardization Project (데이터 관리 표준화 시스템)
📌 4개 사업부의 5년 치 비정형 데이터 8,000건을 표준화하여 업무효율 개선

---

## 1. 프로젝트 개요

### ✔️ Background (배경)
(1) 4개 사업부(IUBA, IWBA, IMBA, ISBA)
<br>
(2) 2021년부터 2026년까지 생성된 8,000건의 관리되지 않은 문서와 데이터

### ✔️ Problem (문제점)
통일되지 않은 부서별 폴더 구조로 인한 자료 검색의 어려움

### ✔️ Goal (목표)
(1) 데이터 구조화: 4개 부서의 폴더 트리 구조 통일
<br>
(2) 정규화: 정규식(Regex) 기반으로 표준화된 네이밍 규칙을 적용
<br>
(2) Automation: Python 스크립트를 활용해 대규모 파일 관리 환경을 시뮬레이션하고 검증

---

## 2. 해결 과정

### 📂 Phase 1. 데이터 시뮬레이션 환경 구축 (Data Generation)
실무와 동일한 환경을 구현하고자 Python을 활용하여 4개 부서, 5년 치, 8,000개의 비정형 더미 데이터(Dummy Data) 생성
- 부서: IUBA, IWBA, IMBA, ISBA
- 기간: 2021~2026
- 총 8,000개 파일

<img src="https://github.com/user-attachments/assets/6047ce55-9066-4965-ae16-aa03664896ab" width="50%">

<br>

### 📂 Phase 2. 폴더 구조화 및 분류 (Restructuring)
MECE 원칙에 따라 각 본부 내 하위 폴더 구조 통일
- Before: 새 폴더, 자료모음, Temp 등 불규칙한 구조
- After:
    - 01_Report (기획안/보고서)
    - 02_Media (사진/영상)
    - 03_Data (수치자료)
    - 04_Admin (관리자)

<!-- 이미지 나란히 배치 -->
<table>
  <tr>
    <td align="center"><b>사업부</b></td>
    <td align="center"><b>하위 폴더</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/76547d51-5d56-4738-a5b8-5f5449477cb3" width="100%"></td>
    <td><img src="https://github.com/user-attachments/assets/32205b6b-b308-40c1-98b6-e31e25e71023" width="100%"></td>
  </tr>
</table>

<br>

### 📂 Phase 3. 네이밍 표준화 (Standardization)
PowerToys PowerRename 툴과 정규식(Regular Expression)을 활용하여 표준화
<br>
✔️ [YYMMDD]_[Dept]_[Category]_[Description]_[Ver]

<!-- 텍스트와 이미지 배치 -->
<table>
  <tr>
    <th width="50%">Before</th>
    <th width="50%">After</th>
  </tr>
  <tr>
    <td valign="top">
      <img src="https://github.com/user-attachments/assets/9adbfaf4-5820-4ee8-8e94-3c21a409c4ef" width="100%">
      <br><br>
      Backup_IMBA_64.pptx (날짜 누락)<br>
      Untitled_IMBA_4161.pdf (무의미한 이름)<br>
      KakaoTalk_260114_65826.pptx (메신저 다운로드 파일)<br>
      220326_meeting_IMBA_748.pptx (순서 꼬임: 카테고리가 먼저 옴)
    </td>
    <td valign="top">
      <img src="https://github.com/user-attachments/assets/b534433e-eba1-42f5-912d-bc7a7493fd0d" width="100%">
      <br><br>
      260301_IMBA_Backup_No64_v01.pptx (날짜 강제 부여, 포맷 통일)<br>
      260301_IMBA_Draft_No4161_v01.pdf ('Untitled'를 'Draft'라는 용어로 변경)<br>
      260114_IMBA_Received_File65826_v01.pptx (파일명 속 날짜 추출, 'KakaoTalk' 제거 후 'Received'로 변경)<br>
      220326_IMBA_meeting_No748_v01.pptx (부서명과 카테고리 순서 재배치)
    </td>
  </tr>
</table>

<br>

<!-- 전체 파일 비교 이미지 -->
<table>
  <tr>
    <td align="center"><b>Result_1</b></td>
    <td align="center"><b>Result_2</b></td>
  </tr>
  <tr>
    <td><img src="https://github.com/user-attachments/assets/5735dfec-e128-473f-9bf0-218f9c7b0bce" width="100%"></td>
    <td><img src="https://github.com/user-attachments/assets/d1c7233d-1240-421f-ac3e-f6893e0d505a" width="100%"></td>
  </tr>
</table>

---

## 3. 사용 툴
Python: 대규모 파일 시스템 제어 및 시뮬레이션 데이터 생성
<br>
PowerToys (PowerRename): 정규식 기반의 대량 파일명 일괄 변경
<br>
File System Management: 윈도우 탐색기 기반으로 파일 관리

---

## 4. 결과
검색 시간 단축: 표준화된 네이밍 규칙으로 키워드 검색 시 정확도 향상
<br>
확장성 확보: 부서가 늘어나거나 데이터가 수만 개로 증가해도 즉시 적용 가능한 표준 가이드라인(SOP)을 수립
