import streamlit as st
import datetime

# ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 言語データの定義
LANG_DICT = {
    "日本語": {
        "welcome": "Welcome to Jin",
        "desc": "40の資格を持つオーナーと、タイ出身の元教師の妻が営む、吉野の隠れ家へようこそ。",
        "checkin_label": "Check-in / チェックイン",
        "checkout_label": "Check-out / チェックアウト",
        "wifi_label": "Wi-Fi Info",
        "rules": "House Rules",
        "rule_list": ["室内は完全禁煙です（屋外指定場所のみ可）", "夜22:00以降はお静かにお願いします", "無料の愛車点検・洗車をご希望の方はオーナーまで！"],
        "guide": "Local Guide",
        "shops": "🛒 Shopping",
        "dining": "🍽 Dining",
        "transport": "🚌 Transport / ATM",
        "support": "Support",
        "medical": "Medical",
        "staff_info": "Staff Information"
    },
    "English": {
        "welcome": "Welcome to Jin",
        "desc": "A cozy hideaway in Yoshino, run by a multi-talented owner and his Thai wife.",
        "checkin_label": "Check-in",
        "checkout_label": "Check-out",
        "wifi_label": "Wi-Fi Info",
        "rules": "House Rules",
        "rule_list": ["No smoking inside", "Please be quiet after 10 PM", "Free car inspection/wash available on request!"],
        "guide": "Local Guide",
        "shops": "🛒 Shopping",
        "dining": "🍽 Dining",
        "transport": "🚌 Transport / ATM",
        "support": "Support",
        "medical": "Medical",
        "staff_info": "Meet Our Staff"
    }
}

# デザイン設定（CSS）
st.markdown("""
    <style>
    .main { background-color: #002255; color: white; font-family: 'Helvetica Neue', Arial, sans-serif; }
    .stTabs [data-baseweb="tab-list"] { background-color: transparent; gap: 10px; }
    .stTabs [data-baseweb="tab"] { 
        background-color: rgba(255, 255, 255, 0.05); border-radius: 8px 8px 0 0; 
        color: #ccddee !important; font-size: 1.4rem !important; border: none !important;
    }
    .stTabs [aria-selected="true"] { 
        background-color: #004488 !important; border-bottom: 2px solid #00aaff !important; color: white !important;
    }
    .info-card { 
        background: rgba(255, 255, 255, 0.08); padding: 30px; border-radius: 15px; 
        border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 15px;
    }
    .checkout-highlight {
        background: linear-gradient(90deg, #004488, #002255);
        padding: 25px; border-radius: 12px; border-left: 8px solid #00aaff;
        text-align: center; margin: 15px 0;
    }
    .checkout-text { color: #ffffff !important; font-size: 1.5rem; font-weight: bold; margin-bottom: 10px; }
    .accent-blue { color: #00aaff; font-weight: bold; font-size: 1.5rem; margin-bottom: 10px; }
    .big-value { font-size: 3rem; font-weight: bold; color: white; }
    .rule-item { margin-bottom: 10px; font-size: 1.3rem; border-left: 3px solid #00aaff; padding-left: 15px; }
    .staff-box { background: rgba(0, 170, 255, 0.1); padding: 20px; border-radius: 10px; margin-top: 10px; border: 1px dashed #00aaff; }
    </style>
    """, unsafe_allow_html=True)

# 言語選択
sel_lang = st.selectbox("🌐 Language Selection", list(LANG_DICT.keys()))
L = LANG_DICT[sel_lang]

# ヘッダー（エラー箇所修正済み）
col_title, col_status = st.columns([3, 2])
with col_title:
    st.markdown("<h1 style='margin-bottom:0;'>✈︎ Jin</h1>", unsafe_allow_html=True)
with col_status:
    jst_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    st.markdown(f"<div style='text-align: right; font-size: 1.5rem; margin-top: 20px;'>{jst_now.strftime('%H:%M')} | Oyodo, Nara</div>", unsafe_allow_html=True)

# メインタブ
tab1, tab2, tab3, tab4 = st.tabs(["HOME", "INFO", "GUIDE", "HELP"])

with tab1:
    st.markdown(f"### {L['welcome']}")
    st.markdown(f'''
        <div class="info-card">
            <p style="font-size: 1.4rem; line-height: 1.6;">{L['desc']}</p>
            <div style="display: flex; gap: 10px;">
                <div class="checkout-highlight" style="flex: 1;">
                    <div class="checkout-text">{L['checkin_label']}</div>
                    <div class="big-value">4:00 PM</div>
                </div>
                <div class="checkout-highlight" style="flex: 1;">
                    <div class="checkout-text">{L['checkout_label']}</div>
                    <div class="big-value">10:00 AM</div>
                </div>
            </div>
            <div class="staff-box">
                <p class="accent-blue" style="margin-bottom:5px;">{L['staff_info']}</p>
                <p style="font-size:1.1rem;">👨‍✈️ <b>Hitoshi Kobayashi:</b> 40資格保持/元鉄道運転士/元タクシー運転手<br>
                👩‍🏫 <b>Nisachol:</b> タイ出身/元英語教師 (English/Thai/Lao OK!)</p>
            </div>
        </div>
    ''', unsafe_allow_html=True)

with tab2:
    st.markdown(f"### {L['wifi_label']} & Rules")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'''
            <div class="info-card">
                <div class="accent-blue">{L['wifi_label']}</div>
                <p style="opacity: 0.7; margin-bottom:0;">SSID</p>
                <p style="font-size: 2rem; font-weight: bold; margin-bottom:15px;">Deco_C884</p>
                <p style="opacity: 0.7; margin-bottom:0;">Password</p>
                <p style="font-size: 2rem; font-weight: bold;">Q99srAe5</p>
            </div>
        ''', unsafe_allow_html=True)
    with c2:
        rules_html = "".join([f'<div class="rule-item">{r}</div>' for r in L["rule_list"]])
        st.markdown(f'''<div class="info-card"><div class="accent-blue">{L['rules']}</div>{rules_html}</div>''', unsafe_allow_html=True)

with tab3:
    st.markdown(f"### {L['guide']}")
    c_a, c_b = st.columns(2)
    with c_a:
        st.markdown(f'''
            <div class="info-card">
                <div class="accent-blue">{L['shops']}</div>
                <p><b>ライフ 大淀店 (Life)</b><br><small>Supermarket | 9:00-21:00</small></p>
                <p><b>ファミリーマート (FamilyMart)</b><br><small>24h / ATM inside</small></p>
            </div>
        ''', unsafe_allow_html=True)
    with c_b:
        st.markdown(f'''
            <div class="info-card">
                <div class="accent-blue">{L['dining']}</div>
                <p><b>赤影 / 鳥欽</b><br><small>Yakitori</small></p>
                <p><b>和光 (Wako)</b><br><small>Sushi</small></p>
            </div>
        ''', unsafe_allow_html=True)
    
    st.markdown(f'''
        <div class="info-card">
            <div class="accent-blue">{L['transport']}</div>
            <p>🚕 <b>近鉄タクシー (Kintetsu Taxi):</b><br><span style="font-size:1.8rem; font-weight:bold;">0747-53-2331</span></p>
            <hr style="opacity:0.2">
            <p>🚉 <b>越部駅 / 下市口駅</b><br>
            <a href="https://www.kintetsu.co.jp/station/station_info/station16021.html" target="_blank" style="color:#00aaff; text-decoration:none; font-weight:bold;">→ 近鉄公式・駅情報/時刻表</a></p>
        </div>
    ''', unsafe_allow_html=True)

with tab4:
    st.markdown(f"### {L['support']}")
    st.markdown(f'''
        <div class="info-card" style="border-left: 8px solid #ff4444;">
            <div class="accent-blue" style="color:#ff4444 !important;">Direct Contact</div>
            <p style="font-size: 2.2rem; font-weight: bold; margin: 10px 0;">080-9419-6063</p>
