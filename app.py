import streamlit as st
import datetime

# --- ページ設定 ---
st.set_page_config(page_title="Jin Premium Concierge", layout="wide")

# --- デザイン（ANA風プレミアムブルー） ---
# エラー防止のため、CSSを短い文字列で分割して読み込みます
st.markdown('<style>.main{background-color:#002255;color:white;font-family:"Arial",sans-serif;}</style>', unsafe_allow_html=True)
st.markdown('<style>.stTabs [data-baseweb="tab-list"]{background-color:#001a40;}</style>', unsafe_allow_html=True)
st.markdown('<style>.info-card{background:rgba(255,255,255,0.05);padding:25px;border-radius:5px;border-left:5px solid #00aaff;margin-bottom:20px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.premium-button{background-color:#00aaff;color:white;padding:10px;border-radius:3px;text-align:center;font-weight:bold;}</style>', unsafe_allow_html=True)

# --- 言語選択 ---
lang = st.sidebar.selectbox("🌐 Language Select", ["日本語", "English"])

# --- ヘッダー（航空機のキャビンイメージ） ---
col1, col2 = st.columns([3, 1])
with col1:
    st.markdown('<h1 style="color:#ffffff;letter-spacing:3px;">✈︎ JIN PREMIUM CONCIERGE</h1>', unsafe_allow_html=True)
with col2:
    jst = datetime.timezone(datetime.timedelta(hours=9))
    now = datetime.datetime.now(jst)
    st.markdown(f'<p style="text-align:right;color:#00aaff;">Local Time: {now.strftime("%H:%M")}</p>', unsafe_allow_html=True)

# --- メインコンテンツ ---
tab1, tab2, tab3, tab4 = st.tabs(["BOARDING", "IN-FLIGHT INFO", "DESTINATION", "CONTACT"])

with tab1:
    if lang == "日本語":
        st.markdown('### Welcome to Jin')
        st.markdown('<div class="info-card"><h4>吉野の隠れ家へ、ようこそ</h4><p>40の資格を持つプロフェッショナルなオーナーと、タイ出身の元英語教師の妻が、真心を込めてお迎えいたします。</p></div>', unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown('<div class="info-card"><b style="color:#00aaff;">CHECK-OUT</b><br><span style="font-size:30px;font-weight:bold;">10:00 AM</span></div>', unsafe_allow_html=True)
        with c2:
            st.markdown('<div class="info-card"><b style="color:#00aaff;">SPECIAL SERVICE</b><br>無料の愛車点検・洗車をご希望の方は、オーナーまでお申し付けください。</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="info-card"><b>STAFF</b><br>👨‍✈️ 小林 斉（元鉄道運転士・元タクシー運転手・一級整備士等、40資格保持）<br>👩‍🏫 Nisachol（タイ出身・元英語教師 / Thai & English OK）</div>', unsafe_allow_html=True)
    else:
        st.markdown('### Welcome to Jin')
        st.markdown('<div class="info-card"><h4>A High-Quality Hideaway in Yoshino</h4><p>Run by an owner with 40 professional qualifications and his Thai wife, a former English teacher.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="info-card"><b style="color:#00aaff;">CHECK-OUT</b><br><span style="font-size:30px;font-weight:bold;">10:00 AM</span></div>', unsafe_allow_html=True)

with tab2:
    st.markdown('### Wi-Fi & House Rules')
    st.success("📶 SSID: Deco_C884  |  Pass: Q99srAe5")
    
    st.markdown('<div class="info-card"><b>HOUSE RULES</b><br>1. 室内は完全禁煙です (No smoking inside)<br>2. 22時以降はお静かに (Quiet hours after 10PM)<br>3. お困りごとは24時間オーナーまで</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('### Local Guide')
    st.markdown('<p style="color:#00aaff;">Shopping & Dining</p>', unsafe_allow_html=True)
    st.write("🛒 **キリン堂 大淀桧垣本店** / **ライフ 大淀店**")
    st.write("🍽 **赤影** (焼き鳥) / **鳥欽** (焼き鳥) / **和光** (寿司)")
    
    st.write("---")
    st.markdown('<p style="color:#00aaff;">Timetable (Kintetsu Railway)</p>', unsafe_allow_html=True)
    col_k1, col_k2 = st.columns(2)
    with col_k1:
        st.link_button("🚉 越部駅 (Kos
