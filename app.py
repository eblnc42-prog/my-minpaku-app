import streamlit as st

# アプリの設定
st.set_page_config(page_title="Jin Guest Guide", layout="wide")

# カスタムCSSでデザインを少し整える（文字を大きく、読みやすく）
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    .stTitle {
        color: #2e5077;
        font-family: 'Helvetica Neue', Arial, sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

# タイトル
st.title("🏡 Welcome to Jin")
st.write("大淀町でのご滞在をサポートするデジタルガイドです。")

# タブの作成（iPadでタップしやすい）
tab1, tab2, tab3 = st.tabs(["🏠 ホーム", "📶 Wi-Fi / 📝 ルール", "📍 周辺ガイド"])

with tab1:
    st.header("ようこそ、宿「Jin」へ")
    st.write("吉野の玄関口、大淀町へお越しいただきありがとうございます。")
    st.write("何かお困りのことがあれば、お気軽にオーナーまでお知らせください。")
    
    st.divider()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="チェックアウト時間", value="10:00 AM")
    with col2:
        if st.button("お祝いのバルーンを飛ばす 🎈"):
            st.balloons()

with tab2:
    st.header("📶 接続・滞在ルール")
    
    # Wi-Fi情報を目立つように表示
    st.success(f"""
    **Wi-Fi ネットワーク情報**
    - SSID: Jin_Guest_WiFi (※または現在のSSID)
    - Password: **Q99srAe5**
    """)
    
    st.divider()
    
    st.subheader("⚠️ 宿のルール")
    st.write("- **チェックアウト:** 10:00までにお願いします。")
    st.write("- **全館禁煙:** お煙草は指定の場所（あれば）でお願いします。")
    st.write("- **静穏時間:** 夜22時以降は近隣へのご配慮をお願いします。")

with tab3:
    st.header("📍 周辺のおすすめ")
    st.write("大淀町・吉野エリアのオーナー厳選スポットです。")
    
    # ここにGoogleマップへのリンクなどを作っていけます
    st.info("※現在、おすすめスポットを準備中です。")
    
    # リンクボタンの例
    st.link_button("Googleマップで周辺を見る", "https://www.google.com/maps/search/?api=1&query=奈良県吉野郡大淀町")

# フッター
st.sidebar.markdown("---")
st.sidebar.write("宿 Jin オーナー")
