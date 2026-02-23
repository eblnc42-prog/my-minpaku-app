import streamlit as st
import datetime

# --- ページ設定 ---
st.set_page_config(page_title="Jin In-Flight Premium", layout="wide")

# --- デザイン (ANA機内モニター・アルティメット 2.5) ---
st.markdown('<style>.main{background-color:#000d1a;color:white;font-family:"Arial",sans-serif;}</style>', unsafe_allow_html=True)
st.markdown('<style>.monitor-frame{background:linear-gradient(180deg, #001a33 0%, #000d1a 100%);padding:25px;border-radius:15px;border:1px solid #334d66;box-shadow: 0 10px 30px rgba(0,0,0,0.7);margin-bottom:20px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.wifi-banner{background:linear-gradient(90deg, #0044cc, #00aaff);padding:12px;border-radius:50px;text-align:center;font-weight:bold;margin-bottom:25px;box-shadow:0 0 15px rgba(0,170,255,0.4);}</style>', unsafe_allow_html=True)
st.markdown('<style>.accent{color:#00aaff;font-weight:bold;text-transform:uppercase;letter-spacing:1.5px;}</style>', unsafe_allow_html=True)

# --- 1. 最優先 Wi-Fi インフォメーション (TOP) ---
st.markdown('<div class="wifi-banner">📶 IN-FLIGHT Wi-Fi : SSID: Deco_C884 / PASS: Q99srAe5</div>', unsafe_allow_html=True)

# --- 2. ヘッダー (機内モニター風) ---
c_head1, c_head2 = st.columns([3, 1])
with c_head1:
    st.markdown('<p style="color:#00aaff;margin:0;letter-spacing:2px;">ENTERTAINMENT SYSTEM</p>', unsafe_allow_html=True)
    st.markdown('<h1 style="margin-top:0;font-size:3rem;font-weight:800;">JIN PREMIUM</h1>', unsafe_allow_html=True)
with c_head2:
    jst = datetime.timezone(datetime.timedelta(hours=9))
    time_now = datetime.datetime.now(jst).strftime("%H:%M")
    st.markdown(f'<div style="text-align:right;"><p style="margin:0;">JST</p><p style="font-size:32px;color:#00aaff;font-weight:bold;margin:0;">{time_now}</p></div>', unsafe_allow_html=True)

# --- 3. メインメニュー（機内モニターメニュー風） ---
tab1, tab2, tab3, tab4 = st.tabs(["✈︎ MY FLIGHT", "🛳 GUIDE", "📍 SIGHTS", "🆘 CALL"])

with tab1:
    st.markdown('<div class="monitor-frame">', unsafe_allow_html=True)
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.markdown('<p class="accent">Chief Purser</p>', unsafe_allow_html=True)
        st.write("**HITOSHI**")
        st.caption("元鉄道運転士・整備士。安全と信頼の旅路を支えるプロフェッショナル。")
    with col_s2:
        st.markdown('<p class="accent">Cabin Attendant</p>', unsafe_allow_html=True)
        st.write("**NISACHOL**")
        st.caption("タイ出身の元英語教師。知性と多言語での温かなおもてなし。")
    
    st.write("---")
    st.markdown('<p class="accent">Flight Data (Higakimoto)</p>', unsafe_allow_html=True)
    col_m1, col_m2, col_m3 = st.columns(3)
    with col_m1:
        st.write("DESTINATION")
        st.markdown('<span style="color:#00aaff;">Oyodo, Nara</span>', unsafe_allow_html=True)
    with col_m2:
        st.write("CHECK-OUT")
        st.markdown('<span style="color:#00aaff;">10:00 AM</span>', unsafe_allow_html=True)
    with col_m3:
        st.write("ALTITUDE")
        st.markdown('<span style="color:#00aaff;">172 m</span>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown('<p class="accent">Exclusive Service</p>', unsafe_allow_html=True)
    st.write("・**愛車の無料点検・洗車**：一級整備士の眼によるプロフェッショナル・ケア。")
    st.write("・**ルート・コンシェルジュ**：元運転士が提案する、最適な「旅の航路」。")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<p class="accent">Destination Guide (Based on Area Center)</p>', unsafe_allow_html=True)
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown('<div class="monitor-frame">', unsafe_allow_html=True)
        st.write("🛒 **SHOPPING**")
        st.write("- **キリン堂 大淀桧垣本店**: 徒歩約2分")
        st.write("- **ライフ 大淀店**: 車で約2分 / 徒歩約10分")
        st.write("- **ローソン 桧垣本店**: 徒歩約5分")
        st.markdown('</div>', unsafe_allow_html=True)
    with col_g2:
        st.markdown('<div class="monitor-frame">', unsafe_allow_html=True)
        st.write("🍽 **DINING**")
        st.write("- **和光 (寿司・割烹)**: 徒歩約1分 (至近)")
        st.write("- **赤影 / 鳥欽 (焼き鳥)**: 徒歩約3分")
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    st.markdown('<p class="accent">Railway Connection</p>', unsafe_allow_html=True)
    st.link_button("🚉 近鉄 越部駅 時刻表 (徒歩約4分)", "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E52")
    st.link_button("🚉 近鉄 下市口駅 時刻表 (車約4分)", "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E54")
    
    st.write("---")
    st.markdown('<p class="accent">In-Flight Etiquette</p>', unsafe_allow_html=True)
    st.write("吉野の静寂な夜を愉しむため、22時以降は少しだけお静かにお過ごしください。")

with tab3:
    st.markdown('<p class="accent">Entertainment (Sightseeing)</p>', unsafe_allow_html=True)
    st.link_button("🌲 道の駅 吉野路大淀iセンター", "https://yoshinoji-oyodo.com/")
    st.link_button("🌸 金峯山寺 (蔵王権現 拝観)", "https://www.kinpusen.or.jp/")
    st.link_button("⛩ 吉野神宮 (公式リンク修正済)", "https://yoshinojingu.jp/")
    st.link_button("🐎 丹生川上神社 下社", "https://niukawakami-jinja.jp/")
    st.link_button("🚠 吉野山ロープウェイ", "https://www.yoshino-ropeway.jp/")

with tab4:
    st.markdown('<div class="monitor-frame" style="border: 2px solid #ff4444;">', unsafe_allow_html=True)
    st.markdown('<p style="color:#ff4444;font-weight:bold;">🆘 ASSISTANCE / CALL BUTTON</p>', unsafe_allow_html=True)
    st.write("何かお困りの際は、お電話または対面にていつでも**オーナーをお呼び出しください**。")
    st.markdown('<h2 style="color:white;margin:10px 0;">080-9419-6063</h2>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.markdown('<p class="accent">Taxi (近鉄配車センター)</p>', unsafe_allow_html=True)
        st.write("☎︎ **0745-77-2101**")
        st.caption("中和近鉄タクシー (大淀エリア)")
    with col_t2:
        st.markdown('<p class="accent">Medical Support</p>', unsafe_allow_html=True)
        st.write("南奈良医療センター: 0747-54-5000")
        st.write("中辻医院: 0747-52-2115")

st.write("---")
st.caption("Jin Premium In-Flight Entertainment System | Developed for Owners Excellence")
