import streamlit as st
import datetime

# --- ページ設定 ---
st.set_page_config(page_title="Jin Concierge Tablet", layout="wide")

# --- デザイン設定 (ANAブルーを基調とした高視認性デザイン) ---
st.markdown('<style>.main{background-color:#001a40;color:white;font-family:"Arial",sans-serif;}</style>', unsafe_allow_html=True)
st.markdown('<style>.monitor-frame{background:rgba(255,255,255,0.08);padding:20px;border-radius:10px;border:1px solid #00aaff;margin-bottom:15px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.wifi-card{background:linear-gradient(90deg, #ffcc00, #ffaa00);color:#000000;padding:20px;border-radius:10px;text-align:center;font-weight:bold;margin-bottom:20px;box-shadow:0 4px 15px rgba(255,204,0,0.4);}</style>', unsafe_allow_html=True)
st.markdown('<style>.accent{color:#00aaff;font-weight:bold;letter-spacing:1px;}</style>', unsafe_allow_html=True)

# --- 1. 言語選択 (サイドバーからメインへ移動し、切り替えやすく) ---
lang = st.radio("🌐 Language / 言語選択", ["日本語", "English"], horizontal=True)

# --- 2. Wi-Fi インフォメーション (視認性最大化) ---
st.markdown(f"""
<div class="wifi-card">
    <div style="font-size:1.2rem;margin-bottom:5px;">📶 FREE Wi-Fi</div>
    <div style="font-size:1.8rem;letter-spacing:1px;">SSID: Deco_C884</div>
    <div style="font-size:1.8rem;letter-spacing:1px;">Password: Q99srAe5</div>
</div>
""", unsafe_allow_html=True)

# --- 3. ヘッダー ---
c_h1, c_h2 = st.columns([3, 1])
with c_h1:
    st.markdown('<h1 style="letter-spacing:3px;margin:0;font-weight:800;">Jin Concierge Tablet</h1>', unsafe_allow_html=True)
with c_h2:
    jst = datetime.timezone(datetime.timedelta(hours=9))
    time_now = datetime.datetime.now(jst).strftime("%H:%M")
    st.markdown(f'<div style="text-align:right;"><span style="font-size:28px;color:#00aaff;font-weight:bold;">{time_now}</span></div>', unsafe_allow_html=True)

# --- 4. メインコンテンツ (タブ) ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 HOME", "🗺️ GUIDE", "🏔️ SIGHTS", "🆘 CALL"])

with tab1:
    st.markdown('<div class="monitor-frame">', unsafe_allow_html=True)
    if lang == "日本語":
        st.markdown('<p class="accent">CREW INTRODUCTION</p>', unsafe_allow_html=True)
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            st.write("**HITOSHI**")
            st.caption("元鉄道運転士・整備士。旅のプロフェッショナル。")
        with col_s2:
            st.write("**NISACHOL**")
            st.caption("タイ出身の元英語教師。知的なホスピタリティ。")
        
        st.write("---")
        st.markdown('<p class="accent">EXCLUSIVE SERVICES</p>', unsafe_allow_html=True)
        st.write("・**愛車無料点検**: 整備士によるプロフェッショナルケア。")
        st.write("・**ルートコンシェルジュ**: 元運転士が提案する、最適な「旅の航路」。")
        st.write("・**タイ式リフレッシュティー**: NISACHOLが淹れる、タイ直伝のウェルカムティー。")
        st.write("---")
        st.write("📍 **所在地**: 大淀町 桧垣本 1332")
        st.write("🕚 **チェックアウト**: 10:00 AM")
    else:
        st.markdown('<p class="accent">CREW INTRODUCTION</p>', unsafe_allow_html=True)
        st.write("**HITOSHI**: Former Train Driver & Mechanic. Travel Professional.")
        st.write("**NISACHOL**: Former English Teacher from Thailand. Intellectual Hospitality.")
        st.write("---")
        st.write("Check-out: 10:00 AM")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    if lang == "日本語":
        st.markdown('<p class="accent">周辺ガイド (徒歩目安)</p>', unsafe_allow_html=True)
        col_g1, col_g2 = st.columns(2)
        with col_g1:
            st.markdown('<div class="monitor-frame">', unsafe_allow_html=True)
            st.write("**飲食・買い物**")
            st.write("- 和光 (寿司・割烹): 3分")
            st.write("- 赤影 (焼き鳥): 3分")
            st.write("- キリン堂: 5分")
            st.write("- 鳥欽 (焼き鳥): 8分")
            st.markdown('</div>', unsafe_allow_html=True)
        with col_g2:
            st.markdown('<div class="monitor-frame">', unsafe_allow_html=True)
            st.write("**その他**")
            st.write("- ライフ 大淀店: 8分")
            st.write("- ローソン 桧垣本店: 10分")
            st.write("- ファミマ 大淀東店: 10分")
            st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.write("Local Guide: Wako Sushi (3min), Akakage Yakitori (3min), Kirindo Drugstore (5min), Life Supermarket (8min)")

    st.write("---")
    st.markdown('<p class="accent">RAILWAY TIMETABLE (近鉄時刻表PDF)</p>', unsafe_allow_html=True)
    st.link_button("🚉 越部駅 (徒歩4分)", "https://www.kintetsu.co.jp/railway/Dia/pdf/260314/801601.pdf")
    st.link_button("🚉 下市口駅 (車4分)", "https://www.kintetsu.co.jp/railway/Dia/pdf/260314/801501.pdf")

with tab3:
    st.markdown('<p class="accent">TREKKING & SIGHTSEEING</p>', unsafe_allow_html=True)
    
    with st.expander("⛰ 登山者の方へ / For Trekkers"):
        st.write("大峰山系・大台ヶ原のベースキャンプとして。ルート相談はHITOSHIまで。")

    with st.expander("🚗 広域観光 / High-Area Guide"):
        st.write("高野山まで車で約1.5時間。世界遺産の旅路をご案内します。")
    
    st.write("---")
    st.link_button("⛩ 吉野神宮", "https://yoshinoyama-kankou.com/temples/%E5%90%89%E9%87%8E%E7%A5%9E%E5%AE%AE/")
    st.link_button("🌸 金峯山寺 (吉野山)", "https://www.kinpusen.or.jp/")
    st.link_button("🐎 丹生川上神社 下社", "https://niukawakami-jinja.jp/")
    st.link_button("🌲 道の駅 吉野路大淀iセンター", "https://yoshinoji-oyodo.com/")

with tab4:
    st.markdown('<p class="accent">SUPPORT & CALL</p>', unsafe_allow_html=True)
    if lang == "日本語":
        st.write("お困りの際は、お電話または対面にていつでも**オーナーをお呼び出しください**。")
    else:
        st.write("Please call or visit the owner anytime for assistance.")
    
    # オーナー電話番号
    st.markdown('<div style="background-color:#002266; padding:25px; border-radius:15px; border:2px solid #00aaff; text-align:center;"><span style="color:#ffffff; font-size:36px; font-weight:bold; letter-spacing:2px;">☎︎ 080-9419-6063</span></div>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown('<p class="accent">TAXI (近鉄タクシー フリーダイヤル)</p>', unsafe_allow_html=True)
    st.markdown('<h2 style="color:#ffcc00;text-align:center;">0120-202-961</h2>', unsafe_allow_html=True)
    
    st.markdown('<p class="accent">MEDICAL</p>', unsafe_allow_html=True)
    st.write("南奈良医療センター: 0747-54-5000 / 中辻医院: 0747-52-2115")

st.write("---")
st.caption("Jin Concierge Tablet | Premium Hospitality Edition")
