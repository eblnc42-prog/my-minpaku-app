import streamlit as st
import datetime

# --- ページ設定 ---
st.set_page_config(page_title="Jin Concierge Tablet", layout="wide")

# --- デザイン修正 (不要な記号を排除し、視認性を最大化) ---
st.markdown('<style>.main{background-color:#001a40;color:white;font-family:"Arial",sans-serif;}</style>', unsafe_allow_html=True)
st.markdown('<style>.monitor-frame{background:rgba(255,255,255,0.08);padding:20px;border-radius:10px;border:1px solid #00aaff;margin-bottom:15px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.accent{color:#00aaff;font-weight:bold;letter-spacing:1px;}</style>', unsafe_allow_html=True)

# --- 1. 最優先 Wi-Fi インフォメーション ---
st.markdown('<div style="background:linear-gradient(90deg, #0044cc, #0088ff);padding:10px;border-radius:50px;text-align:center;font-weight:bold;box-shadow:0 4px 10px rgba(0,0,0,0.3);">📶 Guest Wi-Fi : SSID: Deco_C884 / PW: Q99srAe5</div>', unsafe_allow_html=True)

# --- 2. プレミアム・ヘッダー ---
c_h1, c_h2 = st.columns([3, 1])
with c_h1:
    st.markdown('<h1 style="letter-spacing:3px;margin:0;font-weight:800;">Jin Concierge Tablet</h1>', unsafe_allow_html=True)
    st.markdown('<p style="color:#00aaff;margin:0;">Premium Hospitality Support</p>', unsafe_allow_html=True)
with c_h2:
    jst = datetime.timezone(datetime.timedelta(hours=9))
    time_now = datetime.datetime.now(jst).strftime("%H:%M")
    st.markdown(f'<div style="text-align:right;"><span style="font-size:28px;color:#00aaff;font-weight:bold;">{time_now}</span></div>', unsafe_allow_html=True)

# --- 3. メインメニュー ---
tab1, tab2, tab3, tab4 = st.tabs(["✈︎ HOME", "🛳 GUIDE", "📍 TREK & SIGHTS", "🆘 CALL"])

with tab1:
    st.markdown('<div class="monitor-frame">', unsafe_allow_html=True)
    col_s1, col_s2 = st.columns(2)
    with col_s1:
        st.markdown('<p class="accent">HITOSHI</p>', unsafe_allow_html=True)
        st.write("元鉄道運転士・整備士。旅のプロフェッショナル。")
    with col_s2:
        st.markdown('<p class="accent">NISACHOL</p>', unsafe_allow_html=True)
        st.write("タイ出身の元英語教師。知的なホスピタリティ。")
    
    st.write("---")
    st.markdown('<p class="accent">EXCLUSIVE SERVICES</p>', unsafe_allow_html=True)
    st.write("・**愛車無料点検**: 整備士によるプロフェッショナルケア。")
    st.write("・**ルートコンシェルジュ**: 元運転士が提案する、最適な「旅の航路」。")
    st.write("・**タイ式リフレッシュティー**: NISACHOLが淹れる、タイ直伝のウェルカムハーブティー。")
    
    st.write("---")
    col_st1, col_st2 = st.columns(2)
    with col_st1:
        st.write("CHECK-OUT")
        st.markdown('<span style="color:#00aaff;font-size:24px;font-weight:bold;">10:00 AM</span>', unsafe_allow_html=True)
    with col_st2:
        st.write("LOCATION")
        st.write("大淀町 桧垣本 1332")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<p class="accent">DESTINATION GUIDE (桧垣本エリア)</p>', unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="monitor-frame">', unsafe_allow_html=True)
        st.write("🛒 **SHOPPING / DINING (徒歩)**")
        st.write("- **和光 (寿司・割烹)**: 徒歩約3分")
        st.write("- **赤影 (焼き鳥)**: 徒歩約3分")
        st.write("- **キリン堂 大淀桧垣本店**: 徒歩約5分")
        st.write("- **鳥欽 (焼き鳥)**: 徒歩約8分")
        st.markdown('</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="monitor-frame">', unsafe_allow_html=True)
        st.write("🛒 **SHOPPING (徒歩・車)**")
        st.write("- **ライフ 大淀店**: 徒歩約8分")
        st.write("- **ローソン 桧垣本店**: 徒歩約10分")
        st.write("- **ファミリーマート 大淀東店**: 徒歩約10分")
        st.markdown('</div>', unsafe_allow_html=True)

    st.write("---")
    st.markdown('<p class="accent">RAILWAY TIMETABLE (近鉄時刻表PDF)</p>', unsafe_allow_html=True)
    st.write("※大阪阿部野橋まで特急で約1時間。")
    st.link_button("🚉 越部駅 時刻表 (徒歩4分)", "https://www.kintetsu.co.jp/railway/Dia/pdf/260314/801601.pdf")
    st.link_button("🚉 下市口駅 時刻表 (車4分)", "https://www.kintetsu.co.jp/railway/Dia/pdf/260314/801501.pdf")
    
    st.write("---")
    st.write("・22時以降は、吉野の静寂を愉しむため少しだけお静かにお過ごしください。")

with tab3:
    st.markdown('<p class="accent">TREKKING & SIGHTSEEING</p>', unsafe_allow_html=True)
    
    with st.expander("⛰ 登山・ハイキング"):
        st.write("・大峰山系・大台ヶ原へのベースキャンプとして最適です。")
        st.write("・オーナーHITOSHIによる登山ルート相談も承ります。")

    with st.expander("🚗 広域観光 (和歌山・高野山方面)"):
        st.write("・**高野山**: 車で約1時間半。")
        st.write("・世界遺産を巡る極上のドライブルートをご案内します。")
    
    st.write("---")
    st.link_button("⛩ 吉野神宮", "https://yoshinoyama-kankou.com/temples/%E5%90%89%E9%87%8E%E7%A5%9E%E5%AE%AE/")
    st.link_button("🌸 金峯山寺 (吉野山)", "https://www.kinpusen.or.jp/")
    st.link_button("🐎 丹生川上神社 下社", "https://niukawakami-jinja.jp/")
    st.link_button("🌲 道の駅 吉野路大淀iセンター", "https://yoshinoji-oyodo.com/")

with tab4:
    st.markdown('<p class="accent">SUPPORT & CALL</p>', unsafe_allow_html=True)
    st.write("何かお困りの際は、お電話または対面にていつでも**オーナーをお呼び出しください**。")
    
    # 電話番号の視認性を改善（濃紺背景に白文字でハッキリ）
    st.markdown('<div style="background-color:#002266; padding:25px; border-radius:15px; border:2px solid #00aaff; text-align:center;"><span style="color:#ffffff; font-size:36px; font-weight:bold; letter-spacing:2px;">☎︎ 080-9419-6063</span></div>', unsafe_allow_html=True)
    
    st.write("---")
    st.markdown('<p class="accent">TAXI (配車センター)</p>', unsafe_allow_html=True)
    st.write("・**中和近鉄タクシー**: 0745-77-2101")
    
    st.markdown('<p class="accent">MEDICAL</p>', unsafe_allow_html=True)
    st.write("・南奈良総合医療センター: 0747-54-5000")
    st.write("・中辻医院: 0747-52-2115")

st.write("---")
st.caption("Jin Concierge Tablet | Premium Hospitality Edition")
