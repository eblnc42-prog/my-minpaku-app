import streamlit as st
import datetime

# 画面設定
st.set_page_config(page_title="Jin In-flight Entertainment", layout="wide")

# ANA風の濃紺と白を基調としたスタイル
st.markdown("""
    <style>
    .main {
        background-color: #002255;
        color: white;
    }
    .stButton>button {
        width: 100%;
        border-radius: 5px;
        background-color: #0055aa;
        color: white;
        border: none;
        height: 80px;
        font-size: 20px;
    }
    .info-box {
        background-color: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #00aaff;
    }
    h1, h2, h3, p {
        color: white !important;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 10px;
        background-color: #002255;
    }
    .stTabs [data-baseweb="tab"] {
        height: 60px;
        background-color: #003377;
        border-radius: 5px 5px 0px 0px;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# ヘッダー部分
col_logo, col_info = st.columns([1, 4])
with col_logo:
    st.title("💺 Jin")
with col_info:
    st.write(f"**Destination:** OYODO, NARA / **Date:** {datetime.date.today().strftime('%Y/%m/%d')}")

st.divider()

# 機内モニター風のメインメニュー（タブ）
tab1, tab2, tab3, tab4 = st.tabs(["🏠 HOME", "📶 WiFi & RULES", "🗺 LOCAL MAP", "🛎 SERVICE"])

with tab1:
    st.header("Welcome to our Hospitality")
    st.markdown("""
    <div class="info-box">
        <h3>ご搭乗ありがとうございます</h3>
        <p>宿「Jin」へようこそ。大淀町での滞在が素晴らしいものになりますよう、
        この機内モニター風ガイドでサポートいたします。</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    if st.button("祝賀バルーンを飛ばす（着陸セレモニー） 🎈"):
        st.balloons()

with tab2:
    st.header("Flight Information")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"""
        <div class="info-box">
            <h4>📶 Wi-Fi Connection</h4>
            <p>Network: Jin_Guest_WiFi</p>
            <p>Password: <b>Q99srAe5</b></p>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        <div class="info-box">
            <h4>⏰ Checkout Time</h4>
            <p>10:00 AM</p>
            <p>※延長をご希望の場合はお知らせください。</p>
        </div>
        """, unsafe_allow_html=True)

    st.subheader("⚠️ Cabin Rules")
    st.write("・全館禁煙 / No Smoking")
    st.write("・夜22時以降の静粛 / Quiet Hours from 22:00")

with tab3:
    st.header("Destination Guide")
    st.write("大淀町・吉野エリアのおすすめスポットをご案内します。")
    
    st.markdown("""
    <div class="info-box">
        <h4>📍 Recommended Areas</h4>
        <ul>
            <li>吉野川の散策路 (Walking Trail)</li>
            <li>大淀町の梨園 (Local Pear Farm)</li>
            <li>道の駅 吉野路大淀ｉセンター</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.write("")
    st.link_button("MAPを開く (Open Navigation)", "https://www.google.com/maps")

with tab4:
    st.header("Service & Support")
    st.write("快適な滞在のために何か必要ですか？")
    
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.button("アメニティのリクエスト")
    with col_s2:
        st.button("オーナーを呼び出す")
    
    st.divider()
    st.write("緊急連絡先 / Emergency: 090-XXXX-XXXX")

# フッター
st.markdown("<p style='text-align: center;'>Enjoy your stay with Jin</p>", unsafe_allow_html=True)
