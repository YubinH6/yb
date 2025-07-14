import streamlit as st
from datetime import date

st.title("품목별 남은 소비기간 할인 계산기")

item_name = st.selectbox("품목 선택", ["고기", "생선", "과일", "도시락", "빵"])
purchase_date = st.date_input("구매 날짜", date.today())
expiration_date = st.date_input("소비기한", date.today())
original_price = st.number_input("제품 가격 입력", min_value=0)

def dicount_rate_calculation(item_name, days_left):
    if item_name in ["고기", "생선","과일", "도시락", "빵"]:
        if 0 < days_left <= 1:
            return 40+30*(24-days_left)/24
        elif 2 <= days_left <= 3:
            return 20+20*(24-days_left)/24
        elif days_left == 0 :
            return 100 #판매 중지 상품(소비 기한 0)

    elif item_name in ["유제품"]:
        if 0 < days_left <= 3 :
            return 30+30*(24-days_left)/24
        elif 4 <= days_left <= 7 :
            return 10+20*(24-days_left)/24
        elif days_left == 0:
            return 100

    elif item_name in ["가공 식품"]:
        if 7 < days_left <=14:
            return 30+20*(24-days_left)/24
        elif 14 <= days_left <= 28 :
            return 10+20*(24-days_left)/24
        elif days_left == 0:
            return 100

    elif item_name in ["건강 기능 식품"]:
        if 84 <= days_left <= 168 :
            return 30+20*(24-days_left)/24
        elif 28 <= days_left <= 84:
            return 50+20*(24-dyas_left)/24
        elif days_left == 0:
            return 100

남은_일수 = (소비기한 - date.today()).days
if 남은_일수 < 0:
    st.write("이미 소비기한이 지났습니다.")
else:
    할인률 = 할인률_계산(품목, 남은_일수)
    할인가 = 제품_가격 * (1 - 할인률)
    st.write(f"남은 소비기간: {남은_일수}일")
    st.write(f"할인 적용가: {할인가:.2f}원")
    st.write(f"예상 할인률: {할인률*100:.0f}%")
