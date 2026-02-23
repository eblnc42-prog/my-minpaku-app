import streamlit as st
import datetime

# ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 言語データの定義
LANG_DICT = {
    "日本語": {
        "welcome": "ご滞在ありがとうございます",
        "desc": "大淀町の宿「Jin」へようこそ。お客様の旅が快適なものになるようお手伝いいたします。",
        "wifi_label": "Wi-Fi接続情報",
        "rules": "ハウスルール",
        "rule_list": ["・室内は完全禁煙です", "・夜22:00以降はお静かにお願いします", "・ゴミは分別にご協力をお願いします"],
        "guide": "周辺ガイド",
        "shops": "🛒 買い出し",
        "dining": "🍽 お食事（徒歩圏内）",
        "support": "緊急・サポート",
        "medical": "医療機関"
    },
    "English": {
        "welcome": "Welcome Aboard",
        "desc": "Welcome to Jin. We are delighted to have you stay with us in Oyodo.",
        "wifi_label": "Wi-Fi Information",
        "rules": "House Rules",
        "rule_list": ["- No smoking inside", "- Please be quiet after 10 PM", "- Please separate your trash"],
        "guide": "Local Guide",
        "shops": "🛒 Shopping",
        "dining": "🍽 Dining (Walking distance)",
        "support": "Support",
        "medical": "Medical Info"
    },
    "Français": {
        "welcome": "Bienvenue à bord",
        "desc": "Bienvenue chez Jin. Nous sommes ravis de vous accueillir à Oyodo.",
        "wifi_label": "Informations Wi-Fi",
        "rules": "Règlement intérieur",
        "rule_list": ["- Interdiction de fumer à l'intérieur", "- Merci de ne pas faire de bruit après 22h", "- Merci de trier vos déchets"],
        "guide": "Guide Local",
        "shops": "🛒 Shopping",
        "dining": "🍽 Restaurants (À pied)",
        "support": "Assistance",
        "medical": "Infos Médicales"
    },
    "简体中文": {
        "welcome": "欢迎光临",
        "desc": "欢迎来到 Jin。祝您在大淀町度过愉快的时光。",
        "wifi_label": "Wi-Fi 信息",
        "rules": "住宿规则",
        "rule_list": ["- 室内禁止吸烟", "- 晚上22点后请保持安静", "- 请协助进行垃圾分类"],
        "guide": "周边指南",
        "shops": "🛒 购物",
        "dining": "🍽 餐厅 (步行范围)",
        "support": "紧急联络",
        "medical": "医疗信息"
    },
    "ไทย": {
        "welcome": "ยินดีต้อนรับ",
        "desc": "ยินดีต้อนรับสู่ Jin เราหวังว่าคุณจะมีความสุขในการพักผ่อนที่โอยาโดะ",
        "wifi_label": "ข้อมูล Wi-Fi",
        "rules": "กฎระเบียบของที่พัก",
        "rule_list": ["- ห้ามสูบบุหรี่ภายในห้องพัก", "- กรุณางดใช้เสียงดังหลัง 22:00 น.", "- กรุณาแยกขยะก่อนทิ้ง"],
        "guide": "คำแนะนำสถานที่ใกล้เคียง",
        "shops": "🛒 แหล่งช้อปปิ้ง",
        "dining": "🍽 ร้านอาหาร (ระยะเดิน)",
        "support": "ติดต่อฉุกเฉิน",
        "medical": "ข้อมูลการแพทย์"
    }
}

# デザイン設定
st.markdown("""
    <style>
    .main { background-color: #002255; color: white; }
    .stTabs [data-baseweb="tab-list"] { gap: 8px; }
    .stTabs [data-baseweb="tab"] { background-color: rgba(255, 255, 255, 0.05); border-radius: 4px; color: #ccddee !important; }
    .stTabs [aria-selected="true"] { background-color: #004488 !important; }
    .info-card { background: rgba(255, 255, 255, 0.08); padding: 20px; border-radius: 12px; border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 10px; }
    .accent-text { color: #00aaff; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 言語選択（機内モニターのようにトップに配置）
sel_lang = st.selectbox("🌐 Language / 言語選択", list(LANG_DICT.keys()))
L = LANG_DICT[sel_lang]

# ヘッダー
col_title, col_status = st.columns([3, 2])
with col_title:
    st.markdown("## ✈︎ Jin Concierge")
with col_status:
    now = datetime.datetime.now()
    st.markdown(f"<div style='text-align: right; opacity: 0.8;'>{now.strftime('%H:%M')} | Checkout: 10:00 AM</div>", unsafe_allow_html=True)

# メインタブ
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "📶 Info", "🍽 Guide", "🆘 Help"])

with tab1:
    st.subheader(L["welcome"])
    st.markdown(f"""<div class="info-card"><h4>{L['welcome']}</h4><p>{L['desc']}</p><hr style="opacity:0.2"><p>Check-out: <span class="accent-text">10:00 AM</span></p></div>""", unsafe_allow_html=True)
    if st.button("Celebration 🎈"): st.balloons()

with tab2:
    st.subheader(L["wifi_label"] + " & " + L["rules"])
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class="info-card"><p class="accent-text">{L['wifi_label']}</p><p style="font-size: 0.8rem;">SSID: <b>Deco_C884</b></p><p style="font-size: 0.8rem;">Pass: <b>Q99srAe5</b></p></div>""", unsafe_allow_html=True)
    with c2:
        rules_html = "".join([f"<li>{r}</li>" for r in L["rule_list"]])
        st.markdown(f"""<div class="info-card"><p class="accent-text">{L['rules']}</p><ul style="font-size:0.9rem; padding-left:15px;">{rules_html}</ul></div>""", unsafe_allow_html=True)

with tab3:
    st.subheader(L["guide"])
    c_a, c_b = st.columns(2)
    with c_a:
        st.markdown(f"""<div class="info-card"><p class="accent-text">{L['shops']}</p><p><b>Life Oyodo (ライフ)</b><br>2 min by car</p><p><b>FamlyMart</b><br>2 min by car</p></div>""", unsafe_allow_html=True)
    with c_b:
        st.markdown(f"""<div class="info-card"><p class="accent-text">{L['dining']}</p><p><b>Akakage (赤影)</b> - Yakitori</p><p><b>Torikin (鳥欽)</b> - Yakitori</p><p><b>Wako (和光)</b> - Sushi</p></div>""", unsafe_allow_html=True)
    st.link_button("Google Maps", "https://www.google.com/maps")

with tab4:
    st.subheader(L["support"])
    st.markdown(f"""<div class="info-card" style="border-left: 4px solid #ff4444;"><p class="accent-text">Owner Contact</p><p style="font-size: 1.5rem;">📞 080-9419-6063</p></div>""", unsafe_allow_html=True)
    st.markdown(f"""<div class="info-card"><p class="accent-text">{L['medical']}</p><p><b>Minami-Nara Medical Center</b><br>0747-54-5000</p><p><b>Nakatsuji Clinic</b><br>0747-52-2115</p></div>""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; opacity: 0.5;'>Jin In-flight Concierge</p>", unsafe_allow_html=True)
