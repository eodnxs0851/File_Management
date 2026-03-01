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
    <td align="center"><b>Before</b></td>
    <td align="center"><b>After</b></td>
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
    <th width="50%">- Before:</th>
    <th width="50%">- Result:</th>
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
    <td align="center"><b>전체 파일 Before</b></td>
    <td align="center"><b>전체 파일 Result</b></td>
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





# 🏢 Corporate Data Management Standardization Project
### (데이터 관리 표준화 시스템 구축)

> **📌 Project Summary**  
> 4개 사업부의 5년 치 비정형 데이터 **8,000건을 표준화**하여 업무 효율을 획기적으로 개선한 프로젝트입니다.

---

## 1. 프로젝트 개요 (Project Overview)

### ✔️ Background (배경)
* **대상 조직:** 4개 사업부 (IUBA, IWBA, IMBA, ISBA)
* **데이터 규모:** 2021년부터 2026년까지 생성된 **8,000건**의 비정형 문서 및 데이터

### ✔️ Problem (문제점)
* 통일되지 않은 부서별 폴더 구조로 인한 자료 검색 시간 소요
* 비표준화된 파일명으로 데이터 자산화 불가능

### ✔️ Goal (목표)
1. **데이터 구조화:** 4개 부서의 폴더 트리 구조(MECE) 통일
2. **정규화 (Normalization):** 정규식(Regex) 기반의 표준 네이밍 규칙 적용
3. **자동화 (Automation):** Python 스크립트를 활용해 대규모 파일 관리 환경 시뮬레이션 및 검증

---

## 2. 해결 과정 (Solution Process)

### 📂 Phase 1. 데이터 시뮬레이션 환경 구축 (Data Generation)
실무와 동일한 환경을 구현하고자 **Python**을 활용하여 4개 부서, 5년 치, **8,000개의 비정형 더미 데이터(Dummy Data)**를 생성했습니다.

* **부서:** IUBA, IWBA, IMBA, ISBA
* **기간:** 2021 ~ 2026
* **총 파일 수:** 8,000개

<br>

**[▼ Python 시뮬레이션 결과 화면]**
<img width="80%" alt="Data Generation" src="https://github.com/user-attachments/assets/6047ce55-9066-4965-ae16-aa03664896ab" />

---

### 📂 Phase 2. 폴더 구조화 및 분류 (Restructuring)
MECE 원칙에 따라 각 본부 내 하위 폴더 구조를 통일하여 데이터 접근성을 높였습니다.

* **Before:** `새 폴더`, `자료모음`, `Temp` 등 불규칙한 구조
* **After:**
    * `01_Report` (기획안/보고서)
    * `02_Media` (사진/영상)
    * `03_Data` (수치자료)
    * `04_Admin` (관리자)

<br>

**[▼ 구조화 전/후 비교]**
<img width="45%" alt="Before Structure" src="https://github.com/user-attachments/assets/76547d51-5d56-4738-a5b8-5f5449477cb3" /> 
<img width="45%" alt="After Structure" src="https://github.com/user-attachments/assets/32205b6b-b308-40c1-98b6-e31e25e71023" />

---

### 📂 Phase 3. 네이밍 표준화 (Standardization)
**PowerToys PowerRename** 툴과 **정규식(Regular Expression)**을 활용하여 파일명을 표준화했습니다.

> **✅ Standard Rule:** `[YYMMDD]_[Dept]_[Category]_[Description]_[Ver]`

#### 1️⃣ Before: 비정형 파일명 (문제 상황)
* `Backup_IMBA_64.pptx` (날짜 누락)
* `Untitled_IMBA_4161.pdf` (무의미한 이름)
* `KakaoTalk_260114_65826.pptx` (메신저 다운로드 파일)
* `220326_meeting_IMBA_748.pptx` (순서 오류)

<img width="60%" alt="Before Files" src="https://github.com/user-attachments/assets/9adbfaf4-5820-4ee8-8e94-3c21a409c4ef" />

<br>

#### 2️⃣ Result: 표준화 완료 (개선 결과)
* `260301_IMBA_Backup_No64_v01.pptx` (날짜 강제 부여 및 포맷 통일)
* `260301_IMBA_Draft_No4161_v01.pdf` ('Untitled' → 'Draft'로 용어 변경)
* `260114_IMBA_Received_File65826_v01.pptx` ('KakaoTalk' 제거 후 'Received'로 변경)
* `220326_IMBA_meeting_No748_v01.pptx` (부서명/카테고리 순서 재배치)

<img width="60%" alt="Result Files" src="https://github.com/user-attachments/assets/b534433e-eba1-42f5-912d-bc7a7493fd0d" />

<br>

**[▼ 전체 표준화 적용 결과 (Before & After)]**
<img width="48%" alt="Final Before" src="https://github.com/user-attachments/assets/5735dfec-e128-473f-9bf0-218f9c7b0bce" />
<img width="48%" alt="Final After" src="https://github.com/user-attachments/assets/d1c7233d-1240-421f-ac3e-f6893e0d505a" />

---

## 3. 사용 툴 (Tools Used)
* **Python:** 대규모 파일 시스템 제어 및 시뮬레이션 데이터 생성 (Library: `os`, `random`)
* **PowerToys (PowerRename):** 정규식(Regex) 기반의 대량 파일명 일괄 변경
* **File System Management:** 윈도우 탐색기 기반 데이터 자산 관리

---

## 4. 결과 및 성과 (Results)
1. **검색 시간 단축:** 표준화된 네이밍 규칙 적용으로 키워드 검색 정확도 및 속도 향상
2. **확장성 확보:** 부서가 늘어나거나 데이터가 수만 개로 증가해도 즉시 적용 가능한 **표준 가이드라인(SOP)** 수립






Corporate Data Management Standardization Project (데이터 관리 표준화 시스템)
📌4개 사업부의 5년 치 비정형 데이터 8,000건을 표준화하여 업무효율 개선


-----
1. 프로젝트 개요
✔️ Background (배경)
(1) 4개 사업부(IUBA, IWBA, IMBA, ISBA)
(2) 2021년부터 2026년까지 생성된 8,000건의 관리되지 않은 문서와 데이터
✔️ Problem (문제점)
통일되지 않은 부서별 폴더 구조로 인한 자료 검색의 어려움
✔️ Goal (목표)
(1) 데이터 구조화: 4개 부서의 폴더 트리 구조 통일
(2) 정규화: 정규식(Regex) 기반으로 표준화된 네이밍 규칙을 적용
(2) Automation: Python 스크립트를 활용해 대규모 파일 관리 환경을 시뮬레이션하고 검증


-----
2. 해결 과정
📂 Phase 1. 데이터 시뮬레이션 환경 구축 (Data Generation)
실무와 동일한 환경을 구현하고자 Python을 활용하여 4개 부서, 5년 치, 8,000개의 비정형 더미 데이터(Dummy Data) 생성
- 부서: IUBA, IWBA, IMBA, ISBA
- 기간: 2021~2026
- 총 8,000개 파일
<img width="825" height="1143" alt="image" src="https://github.com/user-attachments/assets/6047ce55-9066-4965-ae16-aa03664896ab" />

📂 Phase 2. 폴더 구조화 및 분류 (Restructuring)
MECE 원칙에 따라 각 본부 내 하위 폴더 구조 통일
- Before: 새 폴더, 자료모음, Temp 등 불규칙한 구조
- After:
01_Report (기획안/보고서)
02_Media (사진/영상)
03_Data (수치자료)
04_Admin (관리자)
<img width="1310" height="339" alt="image" src="https://github.com/user-attachments/assets/76547d51-5d56-4738-a5b8-5f5449477cb3" />
<img width="1315" height="328" alt="image" src="https://github.com/user-attachments/assets/32205b6b-b308-40c1-98b6-e31e25e71023" />

📂 Phase 3. 네이밍 표준화 (Standardization)
PowerToys PowerRename 툴과 정규식(Regular Expression)을 활용하여 표준화
✔️ [YYMMDD]_[Dept]_[Category]_[Description]_[Ver]
- Before:
<img width="1622" height="1477" alt="image" src="https://github.com/user-attachments/assets/9adbfaf4-5820-4ee8-8e94-3c21a409c4ef" />
Backup_IMBA_64.pptx (날짜 누락)
Untitled_IMBA_4161.pdf (무의미한 이름)
KakaoTalk_260114_65826.pptx (메신저 다운로드 파일)
220326_meeting_IMBA_748.pptx (순서 꼬임: 카테고리가 먼저 옴)
- Result:
<img width="1581" height="1475" alt="image" src="https://github.com/user-attachments/assets/b534433e-eba1-42f5-912d-bc7a7493fd0d" />
260301_IMBA_Backup_No64_v01.pptx (날짜 강제 부여, 포맷 통일)
260301_IMBA_Draft_No4161_v01.pdf ('Untitled'를 'Draft'라는 용어로 변경)
260114_IMBA_Received_File65826_v01.pptx (파일명 속 날짜 추출, 'KakaoTalk' 제거 후 'Received'로 변경)
220326_IMBA_meeting_No748_v01.pptx (부서명과 카테고리 순서 재배치)

<img width="2506" height="1568" alt="image" src="https://github.com/user-attachments/assets/5735dfec-e128-473f-9bf0-218f9c7b0bce" />
<img width="2512" height="1558" alt="image" src="https://github.com/user-attachments/assets/d1c7233d-1240-421f-ac3e-f6893e0d505a" />


-----
3. 사용 툴
Python: 대규모 파일 시스템 제어 및 시뮬레이션 데이터 생성
PowerToys (PowerRename): 정규식 기반의 대량 파일명 일괄 변경
File System Management: 윈도우 탐색기 기반으로 파일 관리


-----
4. 결과
검색 시간 단축: 표준화된 네이밍 규칙으로 키워드 검색 시 정확도 향상
확장성 확보: 부서가 늘어나거나 데이터가 수만 개로 증가해도 즉시 적용 가능한 표준 가이드라인(SOP)을 수립
