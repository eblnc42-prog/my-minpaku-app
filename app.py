import streamlit as st
import datetime

# --- ページ設定 ---
st.set_page_config(page_title="Jin Premium", layout="wide")

# --- デザイン (ANA Premium Concept) ---
st.markdown('<style>.main{background-color:#002255;color:white;}</style>', unsafe_allow_html=True)
st.markdown('<style>.card{background:rgba(255,255,255,0.05);padding:20px;border-left:5px solid #00aaff;margin-bottom:20px;border-radius:0 10px 10px 0;}</style>', unsafe_allow_html=True)
st.markdown('<style>.accent{color:#00aaff;font-weight:bold;font-size:1.1rem;}</style>', unsafe_allow_html=True)

# --- 言語・時刻 ---
lang = st.sidebar.selectbox("Language", ["日本語", "English"])
jst = datetime.timezone(datetime.timedelta(hours=9))
time_now = datetime.datetime.now(jst).strftime("%H:%M")

# --- ヘッダー ---
st.markdown('<h1 style="letter-spacing:5px;">✈︎ JIN PREMIUM CONCIERGE</h1>', unsafe_allow_html=True)
st.markdown(f'<p style="color:#00aaff;letter-spacing:2px;">Local Time: {time_now} | Nara Oyodo</p>', unsafe_allow_html=True)

# --- メインコンテンツ ---
t1, t2, t3, t4 = st.tabs(["BOARDING", "IN-FLIGHT", "DESTINATION", "SUPPORT"])

with t1:
    st.markdown('### Welcome to Jin')
    st.markdown('<div class="card">40の資格を持つプロフェッショナルと、タイの知性が織りなす極上の休日。</div>', unsafe_allow_html=True)
    
    col_st1, col_st2 = st.columns(2)
    with col_st1:
        st.markdown('<div class="card"><p class="accent">STAFF: HITOSHI</p>元鉄道運転士・整備士。40の資格を操る旅のプロ。</div>', unsafe_allow_html=True)
    with col_st2:
        st.markdown('<div class="card"><p class="accent">STAFF: NISACHOL</p>タイ出身の元英語教師。多言語でゲストを支えます。</div>', unsafe_allow_html=True)

    st.markdown('<div class="card"><p class="accent">EXCLUSIVE SERVICES</p>・<b>愛車の無料点検・洗車</b>：プロの整備士の眼で愛車をケア。<br>・<b>旅のルート・コンシェルジュ</b>：元運転士が次なる目的地への最適な路をご提案します。</div>', unsafe_allow_html=True)
    st.info("Check-out Time: 10:00 AM")

with t2:
    st.markdown('### In-Flight Info')
    st.success("📶 Wi-Fi: Deco_C884 / Pass: Q99srAe5")
    st.markdown('<div class="card"><p class="accent">HOUSE RULES</p>・<b>室内禁煙</b>：お煙草は指定の場所にて。<br>・<b>静寂を愉しむ</b>：22時以降は、吉野の静かな夜を愉しむため、少しだけお静かにお過ごしください。</div>', unsafe_allow_html=True)

with t3:
    st.markdown('### Destination Guide')
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<p class="accent">🛒 Shopping</p>', unsafe_allow_html=True)
        st.write("・**キリン堂** (ドラッグストア/徒歩15分)")
        st.write("・**ライフ 大淀店** (スーパー/車5分)")
    with c2:
        st.markdown('<p class="accent">🍽 Dining</p>', unsafe_allow_html=True)
        st.write("・**赤影 / 鳥欽** (焼き鳥/徒歩12分)")
        st.write("・**和光** (寿司・割烹/徒歩10分)")

    st.write("---")
    st.markdown('<p class="accent">🚉 Railway Timetable (近鉄電車)</p>', unsafe_allow_html=True)
    # 正確な近鉄時刻表URL
    u_koshibe = "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E52"
    u_shimo = "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E54"
    st.link_button("越部駅 (Koshibe) 時刻表", u_koshibe)
    st.link_button("下市口駅 (Shimoichiguchi) 時刻表", u_shimo)

    st.write("---")
    st.markdown('<p class="accent">🌸 Sightseeing</p>', unsafe_allow_html=True)
    st.link_button("道の駅 吉野路大淀iセンター", "https://yoshinoji-oyodo.com/")
    st.link_button("金峯山寺 (世界遺産)", "https://www.kinpusen.or.jp/")
    st.link_button("吉野神宮 (格式高い祈り)", "https://yoshinojingu.jp/")
    st.link_button("丹生川上神社 下社", "https://niukawakami-jinja.jp/")

with t4:
    st.markdown('### Support & Medical')
    st.error("☎︎ OWNER CALL: 080-9419-6063")
    st.markdown('<div class="card">何かお困りの際は、お電話または対面にていつでもHITOSHIをお呼び出しください。</div>', unsafe_allow_html=True)
    
    st.markdown('<p class="accent">🚕 Taxi</p>', unsafe_allow_html=True)
    st.write("・**近鉄タクシー**: 0745-77-2101")
    
    st.markdown('<p class="accent">🏥 Medical</p>', unsafe_allow_html=True)
    st.write("・南奈良総合医療センター: 0747-54-5000")
    st.write("・中辻医院: 0747-52-2115")

st.write("---")
st.caption("Jin Premium Concierge | Designed for Excellence")
