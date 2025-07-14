import streamlit as st
from datetime import datetime

st.title("소비 기한 할인률 계산기")

item_name = st.selectbox("품목 선택", ["고기", "생선", "과일", "도시락", "빵", "유제품", "가공 식품", "건강 기능 식품"])

purchase_date = st.date_input("구매 날짜", datetime.today())
purchase_time = st.time_input("구매 시간", datetime.now().time())
purchase_datetime = datetime.combine(purchase_date, purchase_time)

expiration_date = st.date_input("소비 기한 날짜", datetime.today())
expiration_time = st.time_input("소비 기한 시간", datetime.now().time())
expiration_datetime = datetime.combine(expiration_date, expiration_time)

original_price = st.number_input("원래 가격", min_value=0.0)

time_left = (expiration_datetime - purchase_datetime).total_seconds() / 3600  # 남은 시간 계산(단위: 시간)

def calculate_discount_rate(item, hours_left):
    if hours_left <= 0:
        return 1.0  # 소비기한 지난 경우 100% 할인 (판매 중지)
    if item in ["고기", "생선", "과일", "도시락", "빵"]:
        if 0 < hours_left <= 24:
            return (40 + 30 * (24 - hours_left) / 24) / 100
        elif 48 >= hours_left > 24:
            return (20 + 20 * (48 - hours_left) / 24) / 100
        else:
            return 0.0
    elif item == "유제품":
        if 0 < hours_left <= 72:
            return (30 + 30 * (72 - hours_left) / 72) / 100
        elif 168 >= hours_left > 72:
            return (10 + 20 * (168 - hours_left) / 96) / 100
        else:
            return 0.0
    elif item == "가공 식품":
        if 168 < hours_left <= 336:
            return (30 + 20 * (336 - hours_left) / 168) / 100
        elif 672 >= hours_left > 336:
            return (10 + 20 * (672 - hours_left) / 336) / 100
        else:
            return 0.0
    elif item == "건강 기능 식품":
        if 2016 < hours_left <= 4032:
            return (30 + 20 * (4032 - hours_left) / 2016) / 100
        elif 2016 >= hours_left > 672:
            return (50 + 20 * (2016 - hours_left) / 1344) / 100
        else:
            return 0.0
