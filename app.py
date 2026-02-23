import streamlit as st
import datetime

# --- ページ設定 ---
st.set_page_config(page_title="Jin Concierge Tablet", layout="wide")

# --- デザイン設定 (ルールブックの内容を反映しつつ視認性を向上) ---
st.markdown('<style>.main{background-color:#001a40;color:white;font-family:"Arial",sans-serif;}</style>', unsafe_allow_html=True)
st.markdown('<style>.monitor-frame{background:rgba(255,255,255,0.08);padding:20px;border-radius:10px;border:1px solid #00aaff;margin-bottom:15px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.wifi-card{background:linear-gradient(90deg, #ffcc00, #ffaa00);color:#000000;padding:20px;border-radius:10px;text-align:center;font-weight:bold;margin-bottom:20px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.checkout-box{background-color:rgba(0,170,255,0.2);padding:15px;border-radius:10px;border:2px solid #00aaff;text-align:center;margin-top:10px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.emergency-alert{background-color:#ff4444;color:white;padding:15px;border-radius:10px;text-align:center;font-weight:bold;margin-bottom:15px;}</style>', unsafe_allow_html=True)
st.markdown('<style>.accent{color:#00aaff;font-weight:bold;letter-spacing:1px;}</style>', unsafe_allow_html=True)

# --- 1. 言語選択 ---
lang = st.radio("🌐 Language / 言語選択", ["日本語", "English"], horizontal=True)

# --- 2. Wi-Fi インフォメーション (TOP) ---
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
tab1, tab2, tab3, tab4, tab5 = st.tabs(["🏠 HOME", "🗺️ GUIDE", "🏔️ SIGHTS", "📜 RULES", "🆘 CALL"])

with tab1:
    st.markdown('<div class="monitor-frame">', unsafe_allow_html=True)
    if lang == "日本語":
        st.markdown('<p class="accent">スタッフ紹介</p>', unsafe_allow_html=True)
        st.write("**HITOSHI**: 元鉄道運転士・整備士 [cite: 53]。旅のプロフェッショナル。")
        st.write("**NISACHOL**: タイ出身の元英語教師。知的なホスピタリティ。")
        st.write("---")
        st.markdown('<p class="accent">特別サービス</p>', unsafe_allow_html=True)
        st.write("・**愛車無料点検**: 整備士によるプロフェッショナルケア。")
        st.write("・**ルートコンシェルジュ**: 旅の目的地や広域観光の相談を承ります。")
        st.write("---")
        st.markdown('<div class="checkout-box"><span style="font-size:1.2rem;">🕚 チェックアウト時間</span><br><span style="font-size:2.5rem;font-weight:bold;color:#ffffff;">10:00 AM</span></div>', unsafe_allow_html=True)
        st.caption("※10時以降は1名1時間につき2,000円を申し受けます [cite: 9]。")
    else:
        st.markdown('<p class="accent">CREW INTRODUCTION</p>', unsafe_allow_html=True)
        st.write("**HITOSHI**: Former Train Driver & Mechanic[cite: 53].")
        st.write("**NISACHOL**: Former English Teacher from Thailand.")
        st.write("---")
        st.markdown('<div class="checkout-box"><span style="font-size:1.2rem;">🕚 CHECK-OUT TIME</span><br><span style="font-size:2.5rem;font-weight:bold;color:#ffffff;">10:00 AM</span></div>', unsafe_allow_html=True)
        st.caption("Late check-out fee: 2,000 JPY per person/hour[cite: 9].")
    st.markdown('</div>', unsafe_allow_html=True)

    # Google 口コミへの誘導
    st.markdown('<div class="monitor-frame" style="text-align:center; border:2px solid #ffcc00;">', unsafe_allow_html=True)
    st.markdown('<p style="color:#ffcc00; font-weight:bold;">🌟 Google Review / 口コミのお願い</p>', unsafe_allow_html=True)
    st.write("皆様の感想が励みになります。口コミ投稿にご協力をお願いします。")
    # ここにオーナー様の実際のGoogle Review URLを入れてください
    st.link_button("Write a Review / 口コミを書く", "https://g.page/r/ChIJ-VIthN_PBmARAsigFfrgZMI/review")
    # QRコードの代わりの案内（実際のQR画像がある場合はst.imageで表示可能）
    st.caption("QRコードは客室のルールブックにもございます。")
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
        st.markdown('<p class="accent">近鉄電車 時刻表 (PDF)</p>', unsafe_allow_html=True)
        st.link_button("🚉 越部駅 (徒歩 約18分)", "https://www.kintetsu.co.jp/railway/Dia/pdf/260314/801601.pdf")
        st.link_button("🚉 下市口駅 (車 約4分)", "https://www.kintetsu.co.jp/railway/Dia/pdf/260314/801501.pdf")
        st.caption("バス停は徒歩1分の場所にございます [cite: 29]。")
    else:
        st.markdown('<p class="accent">LOCAL GUIDE (Walk Time)</p>', unsafe_allow_html=True)
        st.write("- Restaurants & Shops (3-10min walk)")
        st.write("---")
        st.markdown('<p class="accent">TRAIN TIMETABLE (PDF)</p>', unsafe_allow_html=True)
        st.link_button("🚉 Koshibe Station (18min walk)", "https://www.kintetsu.co.jp/railway/Dia/pdf/260314/801601.pdf")
        st.link_button("🚉 Shimoichiguchi Station (4min drive)", "https://www.kintetsu.co.jp/railway/Dia/pdf/260314/801501.pdf")

with tab3:
    if lang == "日本語":
        st.markdown('<p class="accent">登山・広域観光ガイド</p>', unsafe_allow_html=True)
        with st.expander("⛰ 登山者の方へ (注意事項)"):
            st.write("・十分な装備（靴・雨具・防寒着）を確認してください。")
            st.write("・天候の急変に備え、無理のない計画を。登山届の提出を推奨します。")
        with st.expander("🚗 高野山・広域観光"):
            st.write("・高野山まで車で約1.5時間。ルート相談はオーナーまでお気軽に。")
    else:
        st.markdown('<p class="accent">TREKKING & SIGHTSEEING</p>', unsafe_allow_html=True)
        st.write("- Mount Omine Basecamp info / Koyasan trip info available.")
    
    st.write("---")
    st.link_button("⛩ 吉野神宮 / Yoshino Jingu", "https://yoshinoyama-kankou.com/temples/%E5%90%89%E9%87%8E%E7%A5%9E%E5%AE%AE/")
    st.link_button("🌸 金峯山寺 / Kinpusen-ji", "https://www.kinpusen.or.jp/")

with tab4:
    st.markdown('<p class="accent">HOUSE RULES / 施設使用ルール</p>', unsafe_allow_html=True)
    if lang == "日本語":
        st.write("・**土足厳禁**: 室内（中庭除く）では靴を脱いでください [cite: 4]。")
        st.write("・**禁煙**: 室内は完全禁煙です。喫煙は中庭か駐車場でお願いします [cite: 18, 19]。")
        st.write("・**畳への配慮**: 居室での飲食は可能ですが、畳を汚された場合は実費を請求いたします [cite: 26]。")
        st.write("・**静粛に**: 周辺は住宅街です。騒音や大声での会話はお控えください [cite: 3, 34, 35]。")
        st.write("・**チェックアウト**: 鍵はテーブルの上に置いて退出してください [cite: 7]。")
    else:
        st.write("- **No Shoes Inside**: Please take off your shoes[cite: 4].")
        st.write("- **No Smoking**: Smoking only allowed in the courtyard or parking lot[cite: 18, 19].")
        st.write("- **Quiet Hours**: Please be mindful of neighbors[cite: 3, 34].")
        st.write("- **Check-out**: Please leave the key on the table[cite: 7].")

with tab5:
    st.markdown('<p class="accent">EMERGENCY / サポート</p>', unsafe_allow_html=True)
    if lang == "日本語":
        st.markdown(f'<div class="emergency-alert">📍 現在地：{st.secrets.get("ADDRESS", "奈良県吉野郡大淀町桧垣本1332")} [cite: 58]</div>', unsafe_allow_html=True)
        st.write("何かお困りの際は、お電話または対面にていつでも**オーナーをお呼び出しください**。")
        st.markdown('<div style="background-color:#002266; padding:20px; border-radius:15px; border:2px solid #00aaff; text-align:center;"><span style="color:#ffffff; font-size:32px; font-weight:bold;">☎︎ 080-9419-6063</span></div>', unsafe_allow_html=True)
        st.write("---")
        st.write("🚑 **火災・救急**: 119 / 🚓 **警察**: 110 [cite: 54, 55]")
        st.write("🚕 **近鉄タクシー**: 0120-202-961")
    else:
        st.markdown(f'<div class="emergency-alert">📍 Address: 1332 Higakimoto, Oyodo [cite: 58]</div>', unsafe_allow_html=True)
        st.write("Please call or visit the owner anytime for assistance.")
        st.markdown('<div style="background-color:#002266; padding:20px; border-radius:15px; border:2px solid #00aaff; text-align:center;"><span style="color:#ffffff; font-size:32px; font-weight:bold;">☎︎ 080-9419-6063</span></div>', unsafe_allow_html=True)
        st.write("---")
        st.write("Taxi (Toll-free): 0120-202-961")
    
    st.write("---")
    st.write("🏥 南奈良医療センター: 0747-54-5000 / 中辻医院: 0747-52-8586 [cite: 60, 61]")

st.write("---")
st.caption("Jin Concierge Tablet | Rules & Support Integrated")
