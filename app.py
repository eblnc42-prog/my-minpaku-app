import streamlit as st
import datetime

# --- ページ設定 ---
st.set_page_config(page_title="Jin Concierge Tablet", layout="wide")

# --- デザイン設定 ---
st.markdown('<style>.main{background-color:#001a40;color:white;font-family:"Arial",sans-serif;}</style>', unsafe_allow_html=True)
st.markdown('<style>.monitor-frame{background:rgba(255,255,255,0.08);padding:20px;border-radius:10px;border:1px solid #00aaff;margin-bottom:15px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.wifi-card{background:linear-gradient(90deg, #ffcc00, #ffaa00);color:#000000;padding:20px;border-radius:10px;text-align:center;font-weight:bold;margin-bottom:20px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.checkout-box{background-color:rgba(0,170,255,0.2);padding:15px;border-radius:10px;border:2px solid #00aaff;text-align:center;margin-top:10px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.accent{color:#00aaff;font-weight:bold;letter-spacing:1px;}</style>', unsafe_allow_html=True)

# --- 1. 言語選択 ---
lang = st.radio("🌐 Language / 言語選択", ["日本語", "English"], horizontal=True)

# --- 2. Wi-Fi インフォメーション ---
st.markdown(f"""
<div class="wifi-card">
    <div style="font-size:1.2rem;margin-bottom:5px;">📶 FREE Wi-Fi</div>
    <div style="font-size:1.8rem;letter-spacing:1px;">SSID: Deco_C884 / Password: Q99srAe5</div>
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
        st.markdown('<p class="accent">スタッフ紹介</p>', unsafe_allow_html=True)
        st.write("**HITOSHI**: 元鉄道運転士・整備士。旅のプロフェッショナル。")
        st.write("**NISACHOL**: タイ出身の元英語教師。知的なホスピタリティ。")
        st.write("---")
        st.markdown('<p class="accent">特別サービス</p>', unsafe_allow_html=True)
        st.write("・**愛車無料点検**: 整備士によるプロフェッショナルケア。")
        st.write("・**ルートコンシェルジュ**: 旅の目的地や広域観光の相談を承ります。")
        st.write("---")
        st.markdown('<div class="checkout-box"><span style="font-size:1.2rem;">🕚 チェックアウト時間</span><br><span style="font-size:2.5rem;font-weight:bold;color:#ffffff;">10:00 AM</span></div>', unsafe_allow_html=True)
    else:
        st.markdown('<p class="accent">CREW INTRODUCTION</p>', unsafe_allow_html=True)
        st.write("**HITOSHI**: Former Train Driver & Mechanic. Travel Professional.")
        st.write("**NISACHOL**: Former English Teacher from Thailand. Intellectual Hospitality.")
        st.write("---")
        st.markdown('<p class="accent">EXCLUSIVE SERVICES</p>', unsafe_allow_html=True)
        st.write("・**Free Car Check**: Professional care by an experienced mechanic.")
        st.write("・**Route Concierge**: Feel free to consult about your travel routes and local areas.")
        st.write("---")
        st.markdown('<div class="checkout-box"><span style="font-size:1.2rem;">🕚 CHECK-OUT TIME</span><br><span style="font-size:2.5rem;font-weight:bold;color:#ffffff;">10:00 AM</span></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    if lang == "日本語":
        st.markdown('<p class="accent">周辺ガイド (徒歩目安)</p>', unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            st.write("- **和光 (寿司・割烹)**: 約3分")
            st.write("- **赤影 (焼き鳥)**: 約3分")
            st.write("- **キリン堂**: 約5分")
            st.write("- **ライフ 大淀店**: 約8分")
        with c2:
            st.write("- **鳥欽 (焼き鳥)**: 約8分")
            st.write("- **ローソン 桧垣本店**: 約10分")
            st.write("- **ファミリーマート 大淀東店**: 約10分")
        st.write("---")
        st.markdown('<p class="accent">近鉄電車 時刻表</p>', unsafe_allow_html=True)
        st.link_button("🚉 越部駅 (徒歩 約18分)", "https://www.kintetsu.co.jp/railway/Dia/pdf/260314/801601.pdf")
        st.link_button("🚉 下市口駅 (車 約4分)", "https://www.kintetsu.co.jp/railway/Dia/pdf/260314/801501.pdf")
    else:
        st.markdown('<p class="accent">LOCAL GUIDE (Walk Time)</p>', unsafe_allow_html=True)
        st.write("- Wako Sushi: 3min / Akakage Yakitori: 3min / Kirindo: 5min")
        st.write("- Life Supermarket: 8min / Torikin Yakitori: 8min")
        st.write("- Lawson: 10min / FamilyMart: 10min")
        st.write("---")
        st.markdown('<p class="accent">TRAIN TIMETABLE (PDF)</p>', unsafe_allow_html=True)
        st.link_button("🚉 Koshibe Station (18min walk)", "https://www.kintetsu.co.jp/railway/Dia/pdf/260314/801601.pdf")
        st.link_button("🚉 Shimoichiguchi Station (4min by car)", "https://www.kintetsu.co.jp/railway/Dia/pdf/260314/801501.pdf")

with tab3:
    if lang == "日本語":
        st.markdown('<p class="accent">登山・広域観光ガイド</p>', unsafe_allow_html=True)
        with st.expander("⛰ 登山者の方へ (注意事項)"):
            st.write("・十分な装備（靴・雨具・防寒着）を確認してください。")
            st.write("・天候の急変に備え、無理のない計画を。")
            st.write("・登山届（コンパス等）の提出を推奨します。")
            st.write("・大峰山系は非常に険しいため、事前の下調べを徹底してください。")
        with st.expander("🚗 高野山・広域観光"):
            st.write("・高野山まで車で約1.5時間。世界遺産の旅路を楽しめます。")
            st.write("・広域観光のルートについてはオーナーまでお気軽にご相談ください。")
    else:
        st.markdown('<p class="accent">TREKKING & SIGHTSEEING</p>', unsafe_allow_html=True)
        with st.expander("⛰ For Trekkers (Safety Tips)"):
            st.write("- Please check your equipment (hiking boots, rain gear, warm clothes).")
            st.write("- Make a reasonable plan and be prepared for sudden weather changes.")
            st.write("- We recommend submitting a mountain climbing registration.")
        with st.expander("🚗 Koyasan & Area Guide"):
            st.write("- About 1.5 hours by car to Koyasan World Heritage site.")
            st.write("- Please feel free to consult the owner about wide-area travel routes.")
    
    st.write("---")
    st.link_button("⛩ 吉野神宮 / Yoshino Jingu", "https://yoshinoyama-kankou.com/temples/%E5%90%89%E9%87%8E%E7%A5%9E%E5%AE%AE/")
    st.link_button("🌸 金峯山寺 / Kinpusen-ji", "https://www.kinpusen.or.jp/")
    st.link_button("🐎 丹生川上神社 下社", "https://niukawakami-jinja.jp/")

with tab4:
    st.markdown('<p class="accent">SUPPORT & CALL</p>', unsafe_allow_html=True)
    if lang == "日本語":
        st.write("お困りの際は、お電話または対面にていつでも**オーナーをお呼び出しください**。")
        st.markdown('<div style="background-color:#002266; padding:25px; border-radius:15px; border:2px solid #00aaff; text-align:center;"><span style="color:#ffffff; font-size:36px; font-weight:bold;">☎︎ 080-9419-6063</span></div>', unsafe_allow_html=True)
        st.write("---")
        st.write("🚕 **近鉄タクシー (フリーダイヤル)**: 0120-202-961")
    else:
        st.write("Please call or visit the owner anytime for assistance.")
        st.markdown('<div style="background-color:#002266; padding:25px; border-radius:15px; border:2px solid #00aaff; text-align:center;"><span style="color:#ffffff; font-size:36px; font-weight:bold;">☎︎ 080-9419-6063</span></div>', unsafe_allow_html=True)
        st.write("---")
        st.write("🚕 **Kintetsu Taxi (Toll-free)**: 0120-202-961")
    
    st.write("---")
    st.write("🏥 南奈良医療センター (Medical Center): 0747-54-5000 / 中辻医院: 0747-52-2115")

st.write("---")
st.caption("Jin Concierge Tablet | Version 3.1")
