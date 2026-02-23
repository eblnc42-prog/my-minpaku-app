import streamlit as st

# iPadの画面幅に合わせる設定
st.set_page_config(layout="wide", page_title="大淀・宿コンシェルジュ")

# サイドメニュー
st.sidebar.title("🏨 Guest Guide")
menu = st.sidebar.radio(
    "メニューを選んでください",
    ["Welcome", "Wi-Fi & Rules", "How to Use", "Local Map", "Contact"]
)

# 各ページの内容
if menu == "Welcome":
    st.header("ようこそ、大淀町の我が家へ")
    st.image("https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e", caption="吉野の風景") # サンプル画像
    st.write("吉野の玄関口、大淀町での滞在をごゆっくりお楽しみください。")
    st.info("チェックアウト時間は 10:00 AM です。")

elif menu == "Wi-Fi & Rules":
    st.header("📶 Wi-Fi & 📝 ルール")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Wi-Fi")
        st.code("SSID: Oyodo_Guest_WiFi\nPASS: yoshino2024", language="")
    with col2:
        st.subheader("基本ルール")
        st.write("・室内は完全禁煙です\n・夜22時以降はお静かに\n・ゴミは分別してキッチン横へ")

elif menu == "How to Use":
    st.header("♨ 設備の使い方")
    device = st.selectbox("設備を選択", ["お風呂・給湯器", "エアコン", "キッチン・IH"])
    st.write(f"{device} の使い方はこちらです。")
    # ここに画像や動画のリンクを貼ることができます

elif menu == "Local Map":
    st.header("📍 周辺案内（大淀・吉野）")
    st.write("オーナーが実際に通うおすすめスポットです。")
    # Google Mapの埋め込みなどが可能です

elif menu == "Contact":
    st.header("📞 お困りですか？")
    st.button("オーナーのLINEを開く")
    st.write("緊急時は 090-XXXX-XXXX までお電話ください。")
