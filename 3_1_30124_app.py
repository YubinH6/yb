import streamlit as st
from datetime import datetime

st.title("소비 기한 할인율 계산기")

item_name = st.selectbox("Select Item", ["고기", "생선", "과일", "도시락", "빵", "유제품", "가공 식품", "건강 기능 식품"])
purchase_datetime = st.datetime_input("구매 날짜 및 시간", datetime.now())
expiration_datetime = st.datetime_input("소비 기한 날짜 및 시간", datetime.now())
original_price = st.number_input("원래 가격", min_value=0.0)

time_left = (expiration_datetime - purchase_datetime).total_seconds() / 3600  # 시간 단위 계산

def calculate_discount_rate(item, hours_left):
    if hours_left <= 0:
        return 1.0
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
    else:
        return 0.0

if original_price > 0:
    if time_left < 0:
        st.write("이미 소비기한이 지난 제품입니다.")
    else:
        discount_rate = calculate_discount_rate(item_name, time_left)
        discounted_price = original_price * (1 - discount_rate)
        st.write(f"남은 시간: {int(time_left)}시간")
        st.write(f"예상 할인률: {discount_rate * 100:.1f}%")
        st.write(f"할인 적용 가격: {discounted_price:.2f} 원")
else:
    st.write("제품 가격을 입력해주세요.")
