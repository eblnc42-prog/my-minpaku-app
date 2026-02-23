import streamlit as st
import datetime

# ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 言語選択
sel_lang = st.selectbox("🌐 Language / 言語選択", ["日本語", "English"])

# ヘッダー
col_t, col_s = st.columns([3, 2])
with col_t:
    st.title("✈︎ Jin")
with col_s:
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    st.write(f"### {now.strftime('%H:%M')} | Oyodo, Nara")

# タブ
tab1, tab2, tab3, tab4 = st.tabs(["🏠 HOME", "ℹ️ INFO", "🗺️ GUIDE", "🆘 HELP"])

with tab1:
    if sel_lang == "日本語":
        st.subheader("Welcome to Jin")
        st.info("40の資格を持つオーナーと、タイ出身の元教師の妻が営む、吉野の隠れ家へようこそ。")
        st.metric(label="Check-out / チェックアウト", value="10:00 AM")
        st.write("---")
        st.subheader("👨‍✈️ Staff Information")
        st.write("**Hitoshi Kobayashi:** 元鉄道運転士・元タクシー運転手・整備士")
        st.write("**Nisachol:** タイ出身の元英語教師 (English/Thai/Lao OK)")
    else:
        st.subheader("Welcome to Jin")
        st.info("A cozy hideaway in Yoshino, run by a multi-talented owner and his Thai wife.")
        st.metric(label="Check-out", value="10:00 AM")

with tab2:
    st.subheader("📶 Wi-Fi Info")
    st.success("SSID: Deco_C884 / PW: Q99srAe5")
    
    st.write("---")
    st.subheader("📜 House Rules")
    rules = [
        "室内は完全禁煙です (Smoking outside only)",
        "夜22:00以降はお静かにお願いします (Quiet after 10PM)",
        "✨ **無料の愛車点検・洗車**をご希望の方はオーナーまで！"
    ]
    for rule in rules:
        st.write(f"- {rule}")

with tab3:
    st.subheader("🛒 Shopping & 🍽 Dining")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**キリン堂 大淀桧垣本店** (Drugstore)")
        st.link_button("📍 Google Map", "https://www.google.com/maps/search/?api=1&query=キリン堂+大淀桧垣本店")
        st.write("**ライフ 大淀店** (Supermarket)")
        st.link_button("📍 Google Map", "https://www.google.com/maps/search/?api=1&query=ライフ+大淀店")
    with c2:
        st.write("**赤影 / 鳥欽** (Yakitori)")
        st.link_button("📍 Google Map", "https://www.google.com/maps/search/?api=1&query=赤影+鳥欽")
        st.write("**和光** (Sushi)")
        st.link_button("📍 Google Map", "
