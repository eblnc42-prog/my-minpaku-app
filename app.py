import streamlit as st
import datetime

# 1. ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 2. 言語データの定義
LANG_DICT = {
    "日本語": {
        "welcome": "Welcome to Jin",
        "desc": "40の資格を持つオーナーと、タイ出身の元教師の妻が営む、吉野の隠れ家へようこそ。",
        "checkout_label": "Check-out / チェックアウト",
        "wifi_label": "Wi-Fi Info",
        "rules": "House Rules",
        "rule_list": ["室内は完全禁煙です", "夜22:00以降はお静かに", "無料の愛車点検・洗車はオーナーまで！"],
        "guide": "Guide",
        "sight": "Sightseeing",
        "support": "Support",
        "staff": "Staff Information"
    },
    "English": {
        "welcome": "Welcome to Jin",
        "desc": "A cozy hideaway in Yoshino, run by a talented owner and his Thai wife.",
        "checkout_label": "Check-out",
        "wifi_label": "Wi-Fi Info",
        "rules": "House Rules",
        "rule_list": ["No smoking inside", "Quiet after 10 PM", "Free car wash: Ask owner!"],
        "guide": "Guide",
        "sight": "Sightseeing",
        "support": "Support",
        "staff": "Staff Information"
    }
}

# 3. CSSデザイン（エラー回避のためシンプルに記述）
st.markdown("<style>.main { background-color: #002255; color: white; } .info-card { background: rgba(255,255,255,0.1); padding: 20px; border-radius: 15px; margin-bottom: 10px; border: 1px solid rgba(255,255,255,0.2); } .accent { color: #00aaff; font-weight: bold; font-size: 1.2rem; } .map-link { color: #00aaff !important; text-decoration: none; font-weight: bold; }</style>", unsafe_allow_html=True)

# 4. 言語選択
sel_lang = st.selectbox("🌐 Language", list(LANG_DICT.keys()))
L = LANG_DICT[sel_lang]

# 5. ヘッダー
col_t, col_s = st.columns([3, 2])
with col_t:
    st.header("✈︎ Jin")
with col_s:
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    st.write(f"{now.strftime('%H:%M')} | Oyodo, Nara")

# 6. タブ構成
tab1, tab2, tab3, tab4 = st.tabs(["HOME", "INFO", "GUIDE", "HELP"])

with tab1:
    st.subheader(L["welcome"])
    st.markdown(f'<div class="info-card"><p>{L["desc"]}</p><div style="background: #004488; padding: 15px; border-radius: 10px; text-align: center;"><div style="font-size: 1.2rem;">{L["checkout_label"]}</div><div style="font-size: 2.5rem; font-weight: bold;">10:00 AM</div></div></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-card"><div class="accent">{L["staff"]}</div><p>👨‍✈️ <b>Hitoshi Kobayashi</b><br>元鉄道運転士・元タクシー運転手<br>👩‍🏫 <b>Nisachol</b><br>Thai Teacher (English/Thai OK)</p></div>', unsafe_allow_html=True)

with tab2:
    st.subheader(L["wifi_label"])
    st.markdown(f'<div class="info-card"><div class="accent">Wi-Fi</div><p>SSID: <b>Deco_C884</b><br>PW: <b>Q99srAe5</b></p></div>', unsafe_allow_html=True)
    rules_html = "".join([f"<li>{r}</li>" for r in L["rule_list"]])
    st.markdown(f'<div class="info-card"><div class="accent">{L["rules"]}</div><ul>{rules_html}</ul></div>', unsafe_allow_html=True)

with tab3:
    st.subheader(L["guide"])
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'<div class="info-card"><div class="accent">🛒 Shopping</div><b>キリン堂 大淀桧垣本店</b><br><a href="https://www.google.com/maps/search/?api=1&query=キリン堂+大淀桧垣本店" class="map-link">📍 Map</a><br><br><b>ライフ 大淀店</b><br><a href="https://www.google.com/maps/search/?api=1&query=ライフ+大淀店" class="map-link">📍 Map</a></div>', unsafe_allow_html=True)
    with c2:
        st.markdown(f'<div class="info-card">
