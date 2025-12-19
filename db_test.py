from db import Database

if __name__ == "__main__":
    db = Database()

    try:
        # 1) 연결 확인용
        if db.connection is None:
            print("❌ DB 연결 실패")
        else:
            print("✅ DB 연결 성공")

            # 2) 버전 확인 (딱 테스트에 좋음)
            with db.connection.cursor() as cursor:
                cursor.execute("SELECT VERSION() AS version")
                print(cursor.fetchone())

            # 3) 테이블 조회 테스트(테이블 존재 여부 확인)
            with db.connection.cursor() as cursor:
                cursor.execute("SHOW TABLES")
                print(cursor.fetchall())

            # 4) BMI 데이터 가져오기 테스트
            records = db.get_bmi_records(limit=3)
            print("최근 BMI 기록 3개:", records)

    finally:
        db.close()
