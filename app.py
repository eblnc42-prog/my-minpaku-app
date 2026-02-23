import streamlit as st
import datetime
import pandas as pd

# ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 言語データの定義
LANG_DICT = {
    "日本語": {
        "welcome": "ご滞在ありがとうございます",
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
        "checkout_label": "Check-out Time",
        "wifi_label": "Wi-Fi Information",
        "rules": "House Rules",
        "rule_list": ["- No smoking inside", "- Smoking is allowed only in designated outdoor areas", "- Please be quiet after 10 PM"],
        "guide": "Local Guide",
        "shops": "🛒 Shopping",
        "dining": "🍽 Dining (Walking distance)",
        "support": "Support",
        "medical": "Medical Info"
    },
    "Français": {
        "welcome": "Bienvenue chez Jin",
        "checkout_label": "Heure de départ",
        "wifi_label": "Informations Wi-Fi",
        "rules": "Règlement intérieur",
        "rule_list": ["- Interdiction de fumer à l'intérieur", "- Fumer est autorisé uniquement dans les zones extérieures désignées", "- Merci de ne pas faire de bruit après 22h"],
        "guide": "Guide Local",
        "shops": "🛒 Shopping",
        "dining": "🍽 Restaurants (À pied)",
        "support": "Assistance",
        "medical": "Infos Médicales"
    },
    "简体中文": {
        "welcome": "欢迎光临 Jin",
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

# デザイン設定（文字サイズを大幅にアップ）
st.markdown("""
    <style>
    .main { background-color: #002255; color: white; }
    html, body, [data-testid="stWidgetLabel"] { font-size: 1.2rem !important; }
    .stTabs [data-baseweb="tab-list"] { gap: 10px; }
    .stTabs [data-baseweb="tab"] { background-color: rgba(255, 255, 255, 0.05); border-radius: 4px; padding: 15px 25px; color: #ccddee !important; font-size: 1.3rem !important; }
    .stTabs [aria-selected="true"] { background-color: #004488 !important; border-bottom: 3px solid #00aaff !important; }
    .info-card { background: rgba(255, 255, 255, 0.08); padding: 30px; border-radius: 15px; border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 15px; }
    .checkout-box { background-color: #004488; padding: 20px; border-radius: 10px; border-left: 10px solid #00aaff; text-align: center; margin: 20px 0; }
    .accent-text { color: #00aaff; font-weight: bold; font-size: 1.5rem; }
    .big-text { font-size: 1.8rem; font-weight: bold; }
    h1 { font-size: 3rem !important; color: #00aaff !important; }
    h2 { font-size: 2.2rem !important; color: #00aaff !important; }
    h3 { font-size: 1.8rem !important; }
    </style>
    """, unsafe_allow_html=True)

# 言語選択
sel_lang = st.selectbox("🌐 Language / 言語選択", list(LANG_DICT.keys()))
L = LANG_DICT[sel_lang]

# ヘッダー（時刻修正：サーバー時刻ではなく日本時刻を表示）
col_title, col_status = st.columns([3, 2])
with col_title:
    st.markdown("# ✈︎ Jin")
with col_status:
    # 日本標準時を表示するための簡易的な調整
    jst_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    st.markdown(f"<div style='text-align: right; font-size: 1.5rem; opacity: 0.9;'>{jst_now.strftime('%H:%M')} | Oyodo, Nara</div>", unsafe_allow_html=True)

# メインタブ
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Home", "📶 Info", "🍽 Guide", "🆘 Help"])

with tab1:
    st.markdown(f"## {L['welcome']}")
    st.markdown(f"""
        <div class="info-card">
            <p style="font-size: 1.4rem;">{L['desc']}</p>
            <div class="checkout-box">
                <p style="font-size: 1.2rem; margin-bottom: 5px;">{L['checkout_label']}</p>
                <p class="big-text">10:00 AM</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown(f"## {L['wifi_label']} & {L['rules']}")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown(f"""
            <div class="info-card">
                <p class="accent-text">{L['wifi_label']}</p>
                <p style="font-size: 1.1rem; opacity: 0.8;">SSID</p>
                <p class="big-text">Deco_C884</p>
                <p style="font-size: 1.1rem; opacity: 0.8;">Password</p>
                <p class="big-text">Q99srAe5</p>
            </div>
        """, unsafe_allow_html=True)
    with c2:
        rules_html = "".join([f"<li style='margin-bottom:15px;'>{r}</li>" for r in L["rule_list"]])
        st.markdown(f"""
            <div class="info-card">
                <p class="accent-text">{L['rules']}</p>
                <ul style="font-size: 1.3rem; padding-left: 20px;">{rules_html}</ul>
            </div>
        """, unsafe_allow_html=True)

with tab3:
    st.markdown(f"## {L['guide']}")
    c_a, c_b = st.columns(2)
    with c_a:
        st.markdown(f"""
            <div class="info-card">
                <p class="accent-text">{L['shops']}</p>
                <p class="big-text">ライフ 大淀店</p>
                <p style="font-size: 1.1rem;">車で約2分 / 2 min by car</p>
                <br>
                <p class="big-text">ファミリーマート</p>
                <p style="font-size: 1.1rem;">車で約2分 / 2 min by car</p>
            </div>
        """, unsafe_allow_html=True)
    with c_b:
        st.markdown(f"""
            <div class="info-card">
                <p class="accent-text">{L['dining']}</p>
                <p class="big-text">赤影 / 鳥欽 (焼き鳥)</p>
                <p class="big-text">和光 (寿司)</p>
                <p style="font-size: 1.1rem;">徒歩圏内 / Walking distance</p>
            </div>
        """, unsafe_allow_html=True)
    st.link_button("🗺 Google Maps", "https://www.google.com/maps/search/?api=1&query=奈良県吉野郡大淀町", use_container_width=True)

with tab4:
    st.markdown(f"## {L['support']}")
    st.markdown(f"""
        <div class="info-card" style="border-left: 8px solid #ff4444;">
            <p class="accent-text" style="color:#ff4444 !important;">Direct Call</p>
            <p style="font-size: 1.2rem;">緊急時・オーナー直通</p>
            <p style="font-size: 2.5rem; letter-spacing: 2px; font-weight: bold;">080-9419-6063</p>
        </div>
        <div class="info-card">
            <p class="accent-text">Hospital / 医療機関</p>
            <p style="font-size: 1.3rem;"><b>南奈良総合医療センター</b><br>0747-54-5000</p>
            <p style="font-size: 1.3rem; margin-top: 15px;"><b>中辻医院</b> (近隣)<br>0747-52-2115</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<p style='text-align: center; opacity: 0.5; font-size: 1rem;'>Jin Guest Concierge Service</p>", unsafe_allow_html=True)
