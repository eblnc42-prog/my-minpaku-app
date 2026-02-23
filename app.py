import streamlit as st
import datetime

# --- 設定 ---
st.set_page_config(page_title="Jin", layout="wide")

# --- リンク定義（行を短く保つため） ---
U_K = "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E52"
U_S = "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E54"
U_M = "https://yoshinoji-oyodo.com/"
U_H = "https://hakusuien.com/"
U_Y = "https://www.kinpusen.or.jp/"

# --- 表示 ---
lang = st.selectbox("Language", ["日本語", "English"])

st.title("✈︎ Jin")
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
st.write(now.strftime("%H:%M") + " | Oyodo, Nara")

t1, t2, t3, t4 = st.tabs(["🏠", "📶", "🗺️", "🆘"])

with t1:
    if lang == "日本語":
        st.subheader("Welcome to Jin")
        st.info("資格40保持のオーナーとタイ人妻の宿へようこそ")
        st.metric("Check-out", "10:00 AM")
        st.write("---")
        st.write("👨‍✈️ 小林 斉 (元運転士/整備士)")
        st.write("👩‍🏫 Nisachol (元英語教師)")
    else:
        st.subheader("Welcome to Jin")
        st.info("Run by a multi-talented owner and his Thai wife.")
        st.metric("Check-out", "10:00 AM")

with t2:
    st.subheader("Wi-Fi & Rules")
    st.success("SSID: Deco_C884 / PW: Q99srAe5")
    st.write("---")
    st.write("- 禁煙 (No Smoking)")
    st.write("- 22時以降消音 (Quiet after 10PM)")
    st.write("- ✨洗車/点検はオーナーまで！")

with t3:
    st.subheader("Guide")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**キリン堂**")
        st.link_button("Map1", "https://maps.google.com/?q=Kirindo_Oyodo")
        st.write("**ライフ**")
        st.link_button("Map2", "https://maps.google.com/?q=Life_Oyodo")
    with c2:
        st.write("**赤影/鳥欽**")
        st.link_button("Map3", "https://maps.google.com/?q=Akakage_Oyodo")
        st.write("**和光**")
        st.link_button("Map4", "https://maps.google.com/?q=Wako_Sushi_Oyodo")

    st.write("---")
    st.warning("吉野タクシー: 0746-32-2961")
    st.link_button("越部駅時刻表", U_K)
    st.link_button("下市口駅時刻表", U_S)
    
    st.write("---")
    st.link_button("道の駅", U_M)
    st.link_button("梨狩り", U_H)
    st.link_button("吉野山", U_Y)

with t4:
    st.subheader("Support")
    st.error("Owner: 080-9419-6063")
    st.write("---")
    st.write("南奈良医療センター: 0747-54-5000")
    st.write("中辻医院: 0747-52-2115")

st.caption("Jin Guest Concierge")
