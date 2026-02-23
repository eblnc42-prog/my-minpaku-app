import streamlit as st
import datetime

# ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 言語データの定義
LANG_DICT = {
    "日本語": {
        "welcome": "Welcome to Jin",
        "desc": "吉野の入り口、大淀町でのひとときを。宿「Jin」は、お客様の快適な旅をサポートします。",
        "checkout_label": "Check-out / チェックアウト",
        "wifi_label": "Wi-Fi Info",
        "rules": "House Rules",
        "rule_list": ["室内は完全禁煙です（喫煙は屋外の指定場所でお願いします）", "夜22:00以降はお静かにお願いします"],
        "guide": "Local Guide",
        "shops": "🛒 Shopping",
        "dining": "🍽 Dining",
        "transport": "🚌 Transport / ATM",
        "support": "Support",
        "medical": "Medical"
    },
    "English": {
        "welcome": "Welcome to Jin",
        "desc": "Enjoy your stay in Oyodo, Nara. We are here to support your journey.",
        "checkout_label": "Check-out Time",
        "wifi_label": "Wi-Fi Info",
        "rules": "House Rules",
        "rule_list": ["No smoking inside (Designated outdoor areas only)", "Please be quiet after 10 PM"],
        "guide": "Local Guide",
        "shops": "🛒 Shopping",
        "dining": "🍽 Dining",
        "transport": "🚌 Transport / ATM",
        "support": "Support",
        "medical": "Medical"
    },
    "Français": {
        "welcome": "Bienvenue chez Jin",
        "desc": "Profitez de votre séjour à Oyodo. Nous sommes là pour vous aider.",
        "checkout_label": "Heure de départ",
        "wifi_label": "Wi-Fi Info",
        "rules": "Règlement",
        "rule_list": ["Interdiction de fumer à l'intérieur (Espaces extérieurs uniquement)", "Pas de bruit après 22h"],
        "guide": "Guide Local",
        "shops": "🛒 Shopping",
        "dining": "🍽 Restaurants",
        "transport": "🚌 Transport / ATM",
        "support": "Assistance",
        "medical": "Médical"
    },
    "简体中文": {
        "welcome": "欢迎光临 Jin",
        "desc": "欢迎来到大淀町。祝您在这里度过美好的时光。",
        "checkout_label": "退房时间",
        "wifi_label": "Wi-Fi 信息",
        "rules": "住宿规则",
        "rule_list": ["室内禁止吸烟（仅限在室外指定区域吸烟）", "晚上22点后请保持安静"],
        "guide": "周边指南",
        "shops": "🛒 购物",
        "dining": "🍽 餐厅",
        "transport": "🚌 交通 / ATM",
        "support": "紧急联络",
        "medical": "医疗"
    },
    "ไทย": {
        "welcome": "ยินดีต้อนรับสู่ Jin",
        "desc": "ขอให้มีความสุขกับการพักผ่อนที่โอยาโดะ นารา เราพร้อมดูแลคุณ",
        "checkout_label": "เวลาเช็คเอาท์",
        "wifi_label": "ข้อมูล Wi-Fi",
        "rules": "กฎระเบียบ",
        "rule_list": ["ห้ามสูบบุหรี่ภายในห้องพัก (อนุญาตเฉพาะพื้นที่กลางแจ้งที่กำหนด)", "งดใช้เสียงดังหลัง 22:00 น."],
        "guide": "คำแนะนำ",
        "shops": "🛒 แหล่งช้อปปิ้ง",
        "dining": "🍽 ร้านอาหาร",
        "transport": "🚌 การเดินทาง / ATM",
        "support": "ช่วยเหลือ",
        "medical": "การแพทย์"
    }
}

# デザイン修正
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
        padding: 30px; border-radius: 12px; border-left: 8px solid #00aaff;
        text-align: center; margin: 20px 0;
    }
    .accent-blue { color: #00aaff; font-weight: bold; font-size: 1.5rem; margin-bottom: 10px; }
    .big-value { font-size: 3rem; font-weight: bold; color: white; }
    .rule-item { margin-bottom: 15px; font-size: 1.4rem; border-left: 3px solid #00aaff; padding-left: 15px; }
    </style>
    """, unsafe_allow_html=True)

# 言語選択
sel_lang = st.selectbox("🌐 Language Selection / 言語選択", list(LANG_DICT.keys()))
L = LANG_DICT[sel_lang]

# ヘッダー
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
    st.markdown(f'<div class="info-card"><p style="font-size: 1.5rem; line-height: 1.6;">{L["desc"]}</p><div class="checkout-highlight"><div style="font-size: 1.4rem; opacity: 0.9; margin-bottom:5px;">{L["checkout_label"]}</div><div class="big-value">10:00 AM</div></div></div>', unsafe_allow_html=True)

with tab2:
    st.markdown(f"### {L['wifi_label']} & Rules")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f'<div class="info-card"><div class="accent-blue">{L["wifi_label"]}</div><p style="opacity: 0.7; margin-bottom:0;">SSID</p><p style="font-size: 2rem; font-weight: bold; margin-bottom:15px;">Deco_C884</p><p style="opacity: 0.7; margin-bottom:0;">Password</p><p style="font-size: 2rem; font-weight: bold;">Q99srAe5</p></div>', unsafe_allow_html=True)
    with c2:
        rules_html = "".join([f'<div class="rule-item">{r}</div>' for r in L["rule_list"]])
        st.markdown(f'<div class="info-card"><div class="accent-blue">{L["rules"]}</div>{rules_html}</div>', unsafe_allow_html=True)

with tab3:
    st.markdown(f"### {L['guide']}")
    c_a, c_b = st.columns(2)
    with c_a:
        st.markdown(f'<div class="info-card"><div class="accent-blue">{L["shops"]}</div><p><b>ライフ 大淀店 (Life)</b><br><small>Supermarket | 9:00-21:00</small></p><p><b>ファミリーマート (FamilyMart)</b><br><small>Convenience Store (ATM inside)</small></p></div>', unsafe_allow_html=True)
    with c_b:
        st.markdown(f'<div class="info-card"><div class="accent-blue">{L["dining"]}</div><p><b>赤影 / 鳥欽 (Akakage/Torikin)</b><br><small>Yakitori (Grilled Chicken)</small></p><p><b>和光 (Wako)</b><br><small>Traditional Sushi</small></p></div>', unsafe_allow_html=True)
    
    st.markdown(f'<div class="info-card"><div class="accent-blue">{L["transport"]}</div><p>🚕 <b>近鉄タクシー (Kintetsu Taxi):</b><br><span style="font-size:1.8rem; font-weight:bold;">0747-53-2331</span></p><hr style="opacity:0.2"><p>🚉 <b>越部駅 (Koshibe Station)</b><br><a href="https://www.kintetsu.co.jp/rakuraku/t_koshibe.html" target="_blank" style="color:#00aaff;">→ 時刻表 / Timetable</a></p><p>🚉 <b>下市口駅 (Shimoichiguchi Station)</b><br><small>※特急停車駅 / Limited Express Stop</small><br><a href="https://www.kintetsu.co.jp/rakuraku/t_shimoichiguchi.html" target="_blank" style="color:#00aaff;">→ 時刻表 / Timetable</a></p></div>', unsafe_allow_html=True)

with tab4:
    st.markdown(f"### {L['support']}")
    st.markdown(f'<div class="info-card" style="border-left: 8px solid #ff4444;"><div class="accent-blue" style="color:#ff4444 !important;">Direct Contact</div><p style="font-size: 2.5rem; letter-spacing: 2px; font-weight: bold; margin: 10px 0;">080-9419-6063</p><p style="opacity: 0.8;">Owner: Jin</p></div>', unsafe_allow_html=True)
    st.markdown(f'<div class="info-card"><div class="accent-blue">{L["medical"]}</div><p><b>南奈良総合医療センター</b><br>0747-54-5000</p><p style="margin-top:15px;"><b>中辻医院 (Clinic)</b><br>0747-52-2115</p></div>', unsafe_allow_html=True)

st.markdown("<p style='text-align: center; opacity: 0.3; margin-top: 50px;'>Jin Guest Concierge Service</p>", unsafe_allow_html=True)
