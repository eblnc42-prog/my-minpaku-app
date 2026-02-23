import streamlit as st
import datetime

# 1. ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 2. CSSデザイン（1行ずつ読み込むことでトリプルクォートを回避）
st.markdown('<style>.main { background-color: #002255; color: white; }</style>', unsafe_allow_html=True)
st.markdown('<style>.info-card { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; margin-bottom: 15px; border: 1px solid rgba(255,255,255,0.2); }</style>', unsafe_allow_html=True)
st.markdown('<style>.accent { color: #00aaff; font-weight: bold; font-size: 1.2rem; }</style>', unsafe_allow_html=True)
st.markdown('<style>.map-link { color: #00aaff !important; text-decoration: none; font-weight: bold; }</style>', unsafe_allow_html=True)
st.markdown('<style>.checkout-box { background: #004488; padding: 15px; border-radius: 10px; text-align: center; margin: 10px 0; }</style>', unsafe_allow_html=True)

# 3. 言語選択
sel_lang = st.selectbox("🌐 Language / 言語選択", ["日本語", "English"])

# 4. ヘッダー
col_t, col_s = st.columns([3, 2])
with col_t:
    st.header("✈︎ Jin")
with col_s:
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    st.write(now.strftime('%H:%M') + " | Oyodo, Nara")

# 5. タブ構成
tab1, tab2, tab3, tab4 = st.tabs(["HOME", "INFO", "GUIDE", "HELP"])

with tab1:
    if sel_lang == "日本語":
        st.subheader("Welcome to Jin")
        st.markdown('<div class="info-card"><p>40の資格を持つオーナーと、タイ出身の元教師の妻が営む、吉野の隠れ家へようこそ。</p><div class="checkout-box"><div style="font-size: 1.2rem;">Check-out / チェックアウト</div><div style="font-size: 2.5rem; font-weight: bold;">10:00 AM</div></div></div>', unsafe_allow_html=True)
        st.markdown('<div class="info-card"><div class="accent">Staff Information</div><p>👨‍✈️ <b>Hitoshi Kobayashi</b><br>元鉄道運転士・元タクシー運転手・整備士保持</p><p>👩‍🏫 <b>Nisachol</b><br>タイ出身の元英語教師 (English/Thai OK)</p></div>', unsafe_allow_html=True)
    else:
        st.subheader("Welcome to Jin")
        st.markdown('<div class="info-card"><p>A cozy hideaway in Yoshino, run by a multi-talented owner and his Thai wife.</p><div class="checkout-box"><div style="font-size: 1.2rem;">Check-out</div><div style="font-size: 2.5rem; font-weight: bold;">10:00 AM</div></div></div>', unsafe_allow_html=True)

with tab2:
    st.subheader("Wi-Fi & Rules")
    st.markdown('<div class="info-card"><div class="accent">Wi-Fi Info</div><p>SSID: <b>Deco_C884</b><br>PW: <b>Q99srAe5</b></p></div>', unsafe
