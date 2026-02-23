import streamlit as st
import datetime

# ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 言語データの定義
LANG_DICT = {
    "日本語": {
        "welcome": "ご滞在ありがとうございます",
        "desc": "大淀町の宿「Jin」へようこそ。お客様の旅が快適なものになるようお手伝いいたします。",
        "checkout_label": "チェックアウト時間",
        "wifi_label": "Wi-Fi接続情報",
        "rules": "ハウスルール",
        "rule_list": ["・室内は完全禁煙です", "・喫煙は敷地内の指定場所でお願いします", "・夜22:00以降はお静かにお願いします"],
        "guide": "周辺ガイド",
        "shops": "🛒 買い出し",
        "dining": "🍽 お食事（徒歩圏内）",
        "support": "緊急・サポート",
        "medical": "医療機関"
    },
    "English": {
        "welcome": "Welcome to Jin",
        "desc": "Welcome to Jin. We are delighted to have you stay with us in Oyodo.",
        "checkout_label": "Check-out Time",
        "wifi_label": "Wi-Fi Information",
        "rules": "House Rules",
        "rule_list": ["- No smoking inside", "- Smoking allowed only in designated outdoor areas", "- Please be quiet after 10 PM"],
        "guide": "Local Guide",
        "shops": "🛒 Shopping",
        "dining": "🍽 Dining (Walking distance)",
        "support": "Support",
        "medical": "Medical Info"
    },
    "Français": {
        "welcome": "Bienvenue chez Jin",
        "desc": "Bienvenue chez Jin. Nous sommes ravis de vous accueillir à Oyodo.",
        "checkout_label": "Heure de départ",
        "wifi_label": "Informations Wi-Fi",
        "rules": "Règlement intérieur",
        "rule_list": ["- Interdiction de fumer à l'intérieur", "- Fumer est autorisé uniquement à l'extérieur", "- Merci de ne pas faire de bruit après 22h"],
        "guide": "Guide Local",
        "shops": "🛒 Shopping",
        "dining": "🍽 Restaurants (À pied)",
        "support": "Assistance",
        "medical": "Infos Médicales"
    },
    "简体中文": {
        "welcome": "欢迎光临 Jin",
        "desc": "欢迎来到 Jin。祝您在大淀町度过愉快的时光。",
        "checkout_label": "退房时间",
        "wifi_label": "Wi-Fi 信息",
        "rules": "住宿规则",
        "rule_list": ["- 室内禁止吸烟", "- 仅限在室外指定区域吸烟", "- 晚上22点后请保持安静"],
        "guide": "周边指南",
        "shops": "🛒 购物",
        "dining": "🍽 餐厅 (步行范围)",
        "support": "紧急联络",
        "medical": "医疗信息"
    },
    "ไทย": {
        "welcome": "ยินดีต้อนรับสู่ Jin",
        "desc": "ยินดีต้อนรับสู่ Jin เราหวังว่าคุณจะมีความสุขในการพักผ่อนที่โอยาโดะ",
        "checkout_label": "เวลาเช็คเอาท์",
        "wifi_label": "ข้อมูล Wi-Fi",
        "rules": "กฎระเบียบของที่พัก",
        "rule_list": ["- ห้ามสูบบุหรี่ภายในห้องพัก", "- อนุญาตให้สูบบุหรี่ในพื้นที่กลางแจ้งที่กำหนดไว้เท่านั้น", "- กรุณางดใช้เสียงดังหลัง 22:00 น."],
        "guide": "คำแนะนำสถานที่ใกล้เคียง",
        "shops": "🛒 แหล่งช้อปปิ้ง",
        "dining": "🍽 ร้านอาหาร (ระยะเดิน)",
        "support": "ติดต่อฉุกเฉิน",
        "medical": "ข้อมูลการแพทย์"
    }
}

# デザイン設定（文字サイズを大きくし、構文エラーを防ぐために正確に記述）
st.markdown("""
    <style>
    .main { background-color: #002255; color: white; }
    html, body, [data-testid="stWidgetLabel"] { font-size: 1.3rem !important; }
    .stTabs [data-baseweb="tab"] { font-size: 1.5rem !important; padding: 15px 30px !important; color: #ccddee !important; }
    .info-card { background: rgba(255, 255, 255, 0.08); padding: 30px; border-radius: 15px; border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 15px; }
    .checkout-box { background-color: #004488; padding: 25px; border-radius: 10px; border-left: 12px solid #00aaff; text-align: center; }
    .accent-text { color: #00aaff; font-weight: bold; font-size: 1.6rem; }
    .big-text { font-size: 2.2rem; font-weight: bold; }
    h1 { font-size: 3.5rem !important; color: #00aaff !important; }
    h2 { font-size: 2.5rem !important; color: #00aaff !important; }
    </style>
    """, unsafe_allow_html=True)

# 言語選択
sel_lang = st.selectbox("🌐 Language / 言語選択", list(LANG_DICT.keys()))
L = LANG_DICT[sel_lang]

# ヘッダー（日本時間 JST 調整）
col_title, col_status = st.columns([3, 2])
with col_title:
    st.markdown("# ✈︎ Jin")
with col_status:
    jst_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    st.markdown(f"<div style='text-align: right; font-size: 1.6rem; opacity: 0.9;'>{jst_now.strftime('%H:%M')} | Oyodo, Nara</div>", unsafe_allow_html=True)

# メインタブ
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "📶 Info", "🍽 Guide", "🆘 Help"])

with tab1:
    st.markdown(f"## {L['welcome']}")
    st.markdown(f"""<div class="info-card"><p style="font-size: 1.6rem; line-height: 1.6;">{L['desc']}</p><div class="checkout-box"><p style="font-size: 1.4rem; margin-bottom: 5px;">{L['checkout_label']}</p><p class="big-text">10:00 AM</p></div></div>""", unsafe_allow_html=True)

with tab2:
    st.markdown(f"## {L['wifi_label']} & {L['rules']}")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""<div class="info-card"><p class="accent-text">{L['wifi_label']}</p><p style="font-size: 1.2rem; opacity: 0.8;">SSID</p><p class="big-text">Deco_C884</p><p style="font-size: 1.2rem; opacity: 0.8;">Password</p><p class="big-text">Q99srAe5</p></div>""", unsafe_allow_html=True)
    with c2:
        rules_html = "".join([f"<li style='margin-bottom:20px;'>{r}</li>" for r in L["rule_list"]])
        st.markdown(f"""<div class="info-card"><p class="accent-text">{L['rules']}</p><ul style="font-size: 1.5rem; padding-left: 25px;">{rules_html}</ul></div>""", unsafe_allow_html=True)

with tab3:
    st.markdown(f"## {L['guide']}")
    c_a, c_b = st.columns(2)
    with c_a:
        st.markdown(f"""<div class="info-card"><p class="accent-text">{L['shops']}</p><p class="big-text">ライフ 大淀店</p><p style="font-size: 1.3rem;">車で約2分 / 2 min by car</p><br><p class="big-text">ファミリーマート</p><p style="font-size: 1.3rem;">車で約2分 / 2 min by car</p></div>""", unsafe_allow_html=True)
    with c_b:
        st.markdown(f"""<div class="info-card"><p class="accent-text">{L['dining']}</p><p class="big-text">赤影 / 鳥欽 (焼き鳥)</p><p class="big-text">和光 (寿司)</p><p style="font-size: 1.3rem;">徒歩圏内 / Walking distance</p></div>""", unsafe_allow_html=True)
    st.link_button("🗺 Google Maps", "https://www.google.com/maps", use_container_width=True)

with tab4:
    st.markdown(f"## {L['support']}")
    st.markdown(f"""<div class="info-card" style="border-left: 10px solid #ff4444;"><p class="accent-text" style="color:#ff4444 !important;">Direct Call</p><p style="font-size: 1.4rem;">緊急時・オーナー直通</p><p style="font-size: 3rem; letter-spacing: 2px; font-weight: bold;">080-9419-6063</p></div><div class="info-card"><p class="accent-text">{L['medical']}</p><p style="font-size: 1.5rem;"><b>南奈良総合医療センター</b><br>0747-54-5000</p><p style="font-size: 1.5rem; margin-top: 20px;"><b>中辻医院</b> (近隣)<br>0747-52-2115</p></div>""", unsafe_allow_html=True)

st.markdown("<p style='text-align: center; opacity: 0.5; font-size: 1.1rem;'>Jin Guest Concierge Service</p>", unsafe_allow_html=True)
