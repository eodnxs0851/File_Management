import os
import random
import datetime

# =========================================================
# Project: Enterprise Data Simulation (8,000 Files)
# Author: Kim Daewon (Pusan National Univ.)
# Description: Generates unstructured dataset for Data Governance practice
# =========================================================

# 1. 환경 설정 (Environment Setup)
# ---------------------------------------------------------
# 바탕화면에 'Corporate_Data_Server' 폴더 생성
user_desktop = os.path.join(os.path.expanduser("~"), "Desktop")
base_path = os.path.join(user_desktop, "Corporate_Data_Server")

# 조직 구조 정의 (Organizational Structure)
departments = ["IUBA", "IWBA", "IMBA", "ISBA"] # 4 Business Units

# 데이터 카테고리 (Data Categories)
categories = {
    "01_Report": [".docx", ".pptx", ".pdf"],    # 문서
    "02_Media":  [".jpg", ".png", ".mp4"],      # 멀티미디어
    "03_Sales_DB": [".csv", ".xlsx"],           # [중요] 매출 데이터
    "04_Admin":  [".pdf", ".hwp"]               # 행정 문서
}

# 비정형 패턴 키워드 (Unstructured Keywords)
keywords = ["final", "draft", "meeting", "budget", "invoice", "contract", "ref", "temp", "copy"]
legacy_prefixes = ["New", "Untitled", "Backup", "Temp"]

# 시뮬레이션 기간 설정 (2021 ~ 2026)
end_date = datetime.date(2026, 3, 1)
start_date = end_date - datetime.timedelta(days=365 * 5)

# =========================================================
# 2. 메인 로직 (Main Logic)
# =========================================================
if not os.path.exists(base_path):
    os.makedirs(base_path)

print(f"🚀 [System] 데이터 서버 구축을 시작합니다... (Target: 8,000 files)")

total_target = 8000
count = 0

for i in range(total_target):
    
    # [Step 1] 랜덤 날짜 및 메타데이터 생성
    days_range = (end_date - start_date).days
    random_days = random.randrange(days_range)
    file_date = start_date + datetime.timedelta(days=random_days)
    
    date_str_short = file_date.strftime("%y%m%d")   # 260301 (파일명용)
    date_str_long = file_date.strftime("%Y-%m-%d")  # 2026-03-01 (데이터 내부용)
    
    # [Step 2] 부서 및 파일 타입 랜덤 배정
    dept = random.choice(departments)
    cat_name = random.choice(list(categories.keys())) # 카테고리 키 선택
    ext_list = categories[cat_name]                   # 해당 카테고리의 확장자 목록
    ext = random.choice(ext_list)
    
    # [Step 3] 디렉토리 계층 구조 생성 (Directory Hierarchy)
    # 구조: Server / 부서명 / 카테고리 / 파일
    final_path = os.path.join(base_path, dept, cat_name)
    if not os.path.exists(final_path):
        os.makedirs(final_path)
    
    # [Step 4] 난수 발생을 통한 3가지 유형의 '지저분한 파일명' 생성
    rand_val = random.random()
    
    if rand_val > 0.7:
        # Type A: 날짜_키워드_부서_번호 (순서 섞임)
        filename = f"{date_str_short}_{random.choice(keywords)}_{dept}_{random.randint(1,999)}"
        
    elif rand_val > 0.4:
        # Type B: 메신저 다운로드 파일 (KakaoTalk 등)
        filename = f"KakaoTalk_{date_str_short}_{random.randint(10000,99999)}"
        
    else:
        # Type C: 레거시/임시 파일 (Untitled, New 등 날짜 누락)
        filename = f"{random.choice(legacy_prefixes)}_{dept}_{random.randint(1,5000)}"
        
    full_path_with_ext = os.path.join(final_path, f"{filename}{ext}")
    
    # [Step 5] 더미 데이터 페이로드 주입 (Dummy Data Injection)
    # 매출 분석(Skill 2)을 위해 CSV 파일에는 '실제 분석 가능한 데이터'를 주입
    try:
        with open(full_path_with_ext, "w", encoding='utf-8') as f:
            if cat_name == "03_Sales_DB" and ext == ".csv":
                # Header 작성
                f.write("Date,Department,Category,Revenue,Cost,Status\n")
                # Row Data 작성 (랜덤 매출 20건)
                for _ in range(20):
                    revenue = random.randint(100, 1000) * 10000 # 100만~1000만
                    cost = int(revenue * random.uniform(0.6, 0.9)) # 원가율 60~90%
                    biz_type = random.choice(['B2B', 'B2C', 'Gov'])
                    f.write(f"{date_str_long},{dept},{biz_type},{revenue},{cost},Confirmed\n")
            else:
                # 일반 문서는 텍스트만 채움
                f.write(f"[Security Level: 3] This document belongs to {dept} department.")
    except Exception as e:
        pass # 에러 무시하고 계속 진행

    count += 1
    if count % 1000 == 0:
        print(f"   ... Progress: {count} / {total_target} files generated.")

print("="*60)
print(f"✅ [Success] 8,000개의 기업 데이터 시뮬레이션 완료.")
print(f"📁 저장 경로: {base_path}")
print("="*60)
