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
        st
