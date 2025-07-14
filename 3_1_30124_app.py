import streamlit as st

st.title("식품 폐기물 절감을 위한 동적 가격 시스템")

item_name = st.text_input("품목명 입력")
purchase_date = st.date_input("구매 날짜 입력")
expiration_date = st.date_input("소비기한 입력")
original_price = st.number_input("제품 가격 입력", min_value=0)

if st.button("할인 가격 계산"):
    # 예시 계산: 소비기한이 가까울수록 할인율 증가
    days_left = (expiration_date - purchase_date).days
    discount_rate = max(0, 30 - days_left) * 0.03  # 최대 30% 할인
    discount_price = original_price * (1 - discount_rate)
    st.write(f"할인 적용가: {discount_price:.2f}원")
    st.write(f"예상 할인률: {discount_rate*100:.1f}%")
