import streamlit as st
import datetime

# 画面設定
st.set_page_config(page_title="Jin In-flight Concierge", layout="wide")

# スタイル定義
st.markdown("""
    <style>
    .main { background-color: #002255; color: white; }
    .stButton>button {
        border-radius: 8px; background-color: #004488; color: white;
        height: 60px; font-weight: bold; border: 1px solid #00aaff;
    }
    .info-card {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px; border-radius: 15px;
        margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.1);
    }
    h1, h2, h3 { color: #00aaff !important; }
    .status-text { font-size: 1.2rem; font-weight: bold; color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# 1. ヘッダー（現在の状況）
col_logo, col_time, col_weather = st.columns([2, 2, 2])
with col_logo:
    st.title("✈️ Jin")
with col_time:
    now = datetime.datetime.now()
    st.markdown(f"**Current Time** \n<span class='status-text'>{now.strftime('%H:%M')}</span>", unsafe_allow_html=True)
with col_weather:
    st.markdown("**Destination: OYODO** \n<span class='status-text'>Fine / 22°C</span>", unsafe_allow_html=True)

st.divider()

# 2. メイン機能タブ（実用性重視の5項目）
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 HOME", "📶 WiFi/RULE", "🚿 HOW TO USE", "🍽 EAT/SHOP", "🆘 HELP"])

with tab1:
    st.subheader("Welcome Aboard")
    st.markdown("""
    <div class="info-card">
        <h4>快適なご滞在のために</h4>
        <p>宿「Jin」の設備案内や周辺情報は、上のタブからご覧いただけます。<br>
        チェックアウト時間は <b>10:00 AM</b> です。</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("祝賀バルーンを飛ばす 🎈"):
        st.balloons()

with tab2:
    st.subheader("Flight Connection & Rules")
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Wi-Fi Network**")
        st.code("SSID: Jin_Guest_WiFi\nPASS: Q99srAe5", language="")
    with col2:
        st.warning("**Cabin Rules**")
        st.write("🚭 全館禁煙 / No Smoking")
        st.write("🌙 22時以降はお静かに / Quiet Hours")

with tab3:
    st.subheader("Equipment Guide (設備の使いかた)")
    exp1 = st.expander("♨️ お風呂・給湯器")
    exp1.write("1. 壁のリモコンの「優先」ボタンを押す  \n2. 40〜42度に設定  \n3. 「自動」または「おいだき」を押してください。")
    
    exp2 = st.expander("❄️ エアコン・暖房")
    exp2.write("リモコンの「運転」で開始。大淀の冬は冷え込むため、入室後は早めの暖房をお勧めします。")
    
    exp3 = st.expander("🗑 ゴミの分別")
    exp3.write("キッチン下のゴミ箱へ。「燃えるゴミ」「プラスチック」「ペットボトル・缶」に分けてください。")

with tab4:
    st.subheader("Local Amenities")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("**🛒 買い出し**")
        st.write("・**オークワ 大淀西店** (車で3分)")
        st.write("・**ローソン/セブンイレブン** (車で2分)")
    with c2:
        st.markdown("**🍺 お食事**")
        st.write("・**地元の居酒屋** (徒歩圏内)")
        st.write("・**道の駅 吉野路大淀ｉセンター** (車で5分)")
    
    st.write("")
    st.link_button("👉 周辺のグルメマップを開く (Google Map)", "https://www.google.com/maps/search/%E5%A4%A7%E6%B7%80%E7%94%BA+%E3%82%B0%E3%83%AB%E3%83%A1")

with tab5:
    st.subheader("Service & Safety")
    st.error("緊急時は以下のボタンからオーナーへご連絡ください")
    st.write("オーナー直通電話： 090-XXXX-XXXX")
    
    st.divider()
    st.markdown("**🏥 医療機関 (Emergency Medical)**")
    st.write("大淀町立大淀病院: 0747-52-3081")

# フッター
st.markdown("<br><p style='text-align: center; opacity: 0.5;'>Jin In-flight Concierge Service</p>", unsafe_allow_html=True)
