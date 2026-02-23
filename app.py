import streamlit as st
import datetime

# 1. ページ基本設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 2. CSSデザイン（1行ずつ読み込むことで構文エラーを物理的に回避）
st.markdown('<style>.main { background-color: #002255; color: white; }</style>', unsafe_allow_html=True)
st.markdown('<style>.info-card { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; margin-bottom: 20px; border: 1px solid rgba(255,255,255,0.2); }</style>', unsafe_allow_html=True)
st.markdown('<style>.accent-blue { color: #00aaff; font-weight: bold; font-size: 1.3rem; }</style>', unsafe_allow_html=True)
st.markdown('<style>.checkout-box { background: linear-gradient(90deg, #004488, #002255); padding: 20px; border-radius: 12px; border-left: 8px solid #00aaff; text-align: center; margin: 15px 0; }</style>', unsafe_allow_html=True)

# 3. 言語選択
sel_lang = st.selectbox("🌐 Language / 言語選択", ["日本語", "English"])

# 4. ヘッダー表示
col_title, col_time = st.columns([3, 1])
with col_title:
    st.markdown('# ✈︎ Jin')
with col_time:
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    st.markdown(f"### {now.strftime('%H:%M')}")

# 5. タブ構成
tab1, tab2, tab3, tab4, tab5 = st.tabs(["HOME", "INFO", "GUIDE", "SIGHTSEEING", "HELP"])

with tab1:
    if sel_lang == "日本語":
        st.markdown('### Welcome to Jin')
        st.markdown('<div class="info-card"><p style="font-size: 1.2rem;">40の資格を持つオーナーと、タイ出身の元教師の妻が営む、吉野の隠れ家へようこそ。無料の愛車点検や洗車サービスも承っております。</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="checkout-box"><div style="font-size: 1.2rem;">Check-out / チェックアウト</div><div style="font-size: 2.5rem; font-weight: bold;">10:00 AM</div></div>', unsafe_allow_html=True)
        st.markdown('<div class="info-card"><div class="accent-blue">Staff Information</div><p>👨‍✈️ <b>Hitoshi Kobayashi</b><br>元鉄道運転士・元タクシー運転手・自動車整備士（40資格保持のプロ）</p><p>👩‍🏫 <b>Nisachol</b><br>タイ出身の元英語教師 (English / Thai / Lao OK!)</p></div>', unsafe_allow_html=True)
    else:
        st.markdown('### Welcome to Jin')
        st.markdown('<div class="info-card"><p style="font-size: 1.2rem;">A cozy hideaway in Yoshino, run by a multi-talented owner (40 certifications) and his Thai wife, a former teacher.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="checkout-box"><div style="font-size: 1.2rem;">Check-out</div><div style="font-size: 2.5rem; font-weight: bold;">10:00 AM</div></div>', unsafe_allow_html=True)

with tab2:
    st.markdown(f"### Wi-Fi & Rules")
    st.markdown('<div class="info-card"><div class="accent-blue">Wi-Fi</div><p style="font-size: 1.3rem;">SSID: <b>Deco_C884</b><br>PW: <b>Q99srAe5</b></p></div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card"><div class="accent-blue">House Rules</div><ul><li>室内は完全禁煙です</li><li>夜22:00以降はお静かにお願いします</li><li>愛車点検・洗車はオーナーまでお気軽に！</li></ul></div>', unsafe_allow_html=True)

with tab3:
    st.markdown(f"### Shopping & Dining")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<div class="info-card"><div class="accent-blue">🛒 お買い物</div><p><b>キリン堂 大淀桧垣本店</b><br><b>ライフ 大淀店</b></p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="info-card"><div class="accent-blue">🍽 お食事</div><p><b>赤影 / 鳥欽 (焼き鳥)</b><br><b>和光 (寿司)</b></p></div>', unsafe_allow_html=True)
    
    st.markdown('<div class="info-card"><div class="accent-blue">🚌 交通情報</div><p>🚕 <b>吉野タクシー</b><br><span style="font-size: 1.8rem; font-weight: bold; color: #ffcc00;">0746-32-2961</span></p><hr><p>🚉 <b>時刻表リンク</b></p></div>', unsafe_allow_html=True)
    st.link_button("🚉 越部駅 時刻表 (Kintetsu Koshibe)", "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E52")
    st.link_button("🚉 下市口駅 時刻表 (Kintetsu Shimoichiguchi)", "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E54")

with tab4:
    st.markdown('### Sightseeing')
    st.markdown('<div class="info-card"><div class="accent-blue">📍 おすすめスポット</div><p>吉野の豊かな自然と歴史をお楽しみください。</p></div>', unsafe_allow_html=True)
    st.link_button("🌲 道の駅 吉野路大淀iセンター", "https://yoshinoji-oyodo.com/")
    st.link_button("🍐 博水園 (梨狩り)", "https://hakusuien.com/")
    st.link_button("🌸 金峯山寺 (吉野山)", "https://www.kinpusen.or.jp/")
    st.link_button("🚠 吉野山ロープウェイ", "https://www.yoshino-ropeway.jp/")

with tab5:
    st.markdown('### Support')
    st.markdown('<div class="info-card" style="border-left: 8px solid #ff4444;"><div class="accent-blue" style="color: #ff4444;">緊急連絡先</div><p style="font-size: 1.8rem; font-weight: bold;">080-9419-6063</p><p>オーナー：小林 斉 (Hitoshi Kobayashi)</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="info-card"><div class="accent-blue">医療機関</div><p>南奈良総合医療センター: 0747-54-5000<br>中辻医院: 0747-52-2115</p></div>', unsafe_allow_html=True)

st.write("---")
st.caption("Jin Guest Conc
