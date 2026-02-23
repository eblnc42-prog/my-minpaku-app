import streamlit as st
import datetime

# 設定
st.set_page_config(page_title="Jin", layout="wide")

# CSS（エラー回避のため1行ずつ短く記述）
st.markdown('<style>.main{background-color:#002255;color:white;}</style>', unsafe_allow_html=True)
st.markdown('<style>.card{background:rgba(255,255,255,0.1);padding:20px;border-radius:15px;margin-bottom:20px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.blue{color:#00aaff;font-weight:bold;font-size:1.3rem;}</style>', unsafe_allow_html=True)

# 言語
sel_lang = st.selectbox("🌐 Language", ["日本語", "English"])

# ヘッダー
st.title("✈︎ Jin")
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
st.write(now.strftime('%H:%M'))

# タブ
t1, t2, t3, t4, t5 = st.tabs(["HOME", "INFO", "GUIDE", "SIGHT", "HELP"])

with t1:
    if sel_lang == "日本語":
        st.subheader("Welcome to Jin")
        st.write("40の資格を持つオーナーと、タイ出身の妻が営む吉野の隠れ家へようこそ。")
        st.write("無料の愛車点検・洗車も承ります。")
        st.info("Check-out: 10:00 AM")
        st.markdown('<div class="card"><div class="blue">Staff</div><p>小林 斉 (元運転士・整備士)<br>Nisachol (元英語教師)</p></div>', unsafe_allow_html=True)
    else:
        st.subheader("Welcome to Jin")
        st.write("Run by a multi-talented owner and his Thai wife.")
        st.info("Check-out: 10:00 AM")

with t2:
    st.subheader("Wi-Fi & Rules")
    st.success("SSID: Deco_C884 / PW: Q99srAe5")
    st.write("---")
    st.write("・室内禁煙")
    st.write("・22時以降はお静かに")
    st.write("・洗車サービスあり")

with t3:
    st.subheader("Guide")
    st.write("**🛒 お買い物**")
    st.write("キリン堂 大淀桧垣本店 / ライフ 大淀店")
    st.write("**🍽 お食事**")
    st.write("赤影 / 鳥欽 (焼き鳥) / 和光 (寿司)")
    st.write("---")
    st.warning("吉野タクシー: 0746-32-2961")
    # 時刻表（長いURLを短く表示）
    st.link_button("🚉 越部駅 時刻表", "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E52")
    st.link_button("🚉 下市口駅 時刻表", "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E54")

with t4:
    st.subheader("Sightseeing")
    st.link_button("道の駅 吉野路大淀iセンター", "https://yoshinoji-oyodo.com/")
    st.link_button("博水園 (梨狩り)", "https://hakusuien.com/")
