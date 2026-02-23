import streamlit as st
import datetime

# --- 1. ページ基本設定 ---
st.set_page_config(page_title="Jin Premium", layout="wide")

# --- 2. ANAプレミアム・デザイン (CSS) ---
# エラー防止のため極限まで短く分割
st.markdown('<style>.main{background-color:#002255;color:white;}</style>', unsafe_allow_html=True)
st.markdown('<style>.card{background:rgba(255,255,255,0.05);padding:20px;border-left:5px solid #00aaff;margin-bottom:20px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.accent{color:#00aaff;font-weight:bold;}</style>', unsafe_allow_html=True)

# --- 3. 言語と時計 ---
lang = st.sidebar.selectbox("Language", ["日本語", "English"])
jst = datetime.timezone(datetime.timedelta(hours=9))
time_str = datetime.datetime.now(jst).strftime("%H:%M")

# --- 4. ヘッダー ---
st.markdown('<h2 style="letter-spacing:4px;">✈︎ JIN PREMIUM</h2>', unsafe_allow_html=True)
st.markdown(f'<p style="color:#00aaff;">Local Time: {time_str}</p>', unsafe_allow_html=True)

# --- 5. メインメニュー ---
t1, t2, t3, t4 = st.tabs(["BOARDING", "INFO", "GUIDE", "HELP"])

with t1:
    if lang == "日本語":
        st.markdown('### Welcome to Jin')
        st.markdown('<div class="card"><b>吉野の隠れ家へ、ようこそ</b><br>40の資格を持つプロオーナーと、タイ出身の元教師の妻が営む宿です。</div>', unsafe_allow_html=True)
        col_a, col_b = st.columns(2)
        with col_a:
            st.markdown('<div class="card"><p class="accent">CHECK-OUT</p><h3>10:00 AM</h3></div>', unsafe_allow_html=True)
        with col_b:
            st.markdown('<div class="card"><p class="accent">SERVICE</p>愛車の無料点検・洗車承ります</div>', unsafe_allow_html=True)
        st.markdown('<div class="card"><p class="accent">STAFF</p>👨‍✈️ 斉 (元運転士・整備士)<br>👩‍🏫 Nisachol (Thai/English OK)</div>', unsafe_allow_html=True)
    else:
        st.markdown('### Welcome to Jin')
        st.markdown('<div class="card">Run by an owner with 40 licenses and his Thai wife.</div>', unsafe_allow_html=True)
        st.info("Check-out: 10:00 AM")

with t2:
    st.markdown('### In-Flight Info')
    st.success("📶 SSID: Deco_C884 / PW: Q99srAe5")
    st.markdown('<div class="card"><b>Rules</b><br>・禁煙 (No Smoking)<br>・22時以降消音 (Quiet after 10PM)</div>', unsafe_allow_html=True)

with t3:
    st.markdown('### Destination Guide')
    st.markdown('<p class="accent">Shopping & Dining</p>', unsafe_allow_html=True)
    st.write("🛒 キリン堂 / ライフ")
    st.write("🍽 赤影 / 鳥欽 / 和光")
    
    st.markdown('<p class="accent">Timetable</p>', unsafe_allow_html=True)
    # URLを直接書かずに短縮
    url_k = "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E52"
    url_s = "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E54"
    st.link_button("🚉 越部駅", url_k)
    st.link_button("🚉 下市口駅", url_s)
    
    st.markdown('<p class="accent">Sightseeing</p>', unsafe_allow_html=True)
    st.link_button("🌲 道の駅", "https://yoshinoji-oyodo.com/")
    st.link_button("🌸 金峯山寺", "https://www.kinpusen.or.jp/")

with t4:
    st.markdown('### Support')
    st.error("☎︎ Owner: 080-9419-6063")
    st.markdown('<div class="card"><b>Medical</b><br>南奈良総合医療センター<br>中辻医院</div>', unsafe_allow_html=True)
    st.write("吉野タクシー: 0746-32-2961")

st.write("---")
st.caption("Jin Premium Concierge")
