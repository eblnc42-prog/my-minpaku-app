import streamlit as st
import datetime

# ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 言語データ（元のリッチな説明文を復元）
LANG_DICT = {
    "日本語": {
        "welcome": "Welcome to Jin",
        "desc": "40の資格を持つオーナーと、タイ出身の元教師の妻が営む、吉野の隠れ家へようこそ。無料の愛車点検や洗車サービスも承っております。",
        "checkout_label": "Check-out / チェックアウト",
        "wifi_label": "Wi-Fi 情報",
        "rules": "ハウスルール",
        "rule_list": [
            "室内は完全禁煙です（屋外の指定場所をご利用ください）",
            "夜22:00以降はお静かにお願いいたします",
            "愛車点検・洗車をご希望の方は、お気軽にオーナーまで！"
        ],
        "shops": "🛒 お買い物",
        "dining": "🍽 お食事",
        "transport": "🚌 交通・時刻表",
        "sightseeing": "🌸 観光情報",
        "support": "緊急連絡・サポート"
    },
    "English": {
        "welcome": "Welcome to Jin",
        "desc": "A cozy hideaway in Yoshino, run by a multi-talented owner (holding 40 certifications) and his Thai wife, a former teacher.",
        "checkout_label": "Check-out",
        "wifi_label": "Wi-Fi Information",
        "rules": "House Rules",
        "rule_list": [
            "No smoking inside (Please use the designated outdoor area)",
            "Please be quiet after 10 PM",
            "Free car inspection or wash available! Please ask the owner."
        ],
        "shops": "🛒 Shopping",
        "dining": "🍽 Dining",
        "transport": "🚌 Transport",
        "sightseeing": "🌸 Sightseeing",
        "support": "Support"
    }
}

# デザインCSS
st.markdown("""
<style>
    .main { background-color: #002255; color: white; }
    .stTabs [data-baseweb="tab"] { color: #ccddee !important; font-size: 1.2rem !important; }
    .info-card { 
        background: rgba(255, 255, 255, 0.08); padding: 25px; border-radius: 15px; 
        border: 1px solid rgba(255, 255, 255, 0.1); margin-bottom: 20px;
    }
    .accent-blue { color: #00aaff; font-weight: bold; font-size: 1.3rem; margin-bottom: 10px; }
    .checkout-highlight {
        background: linear-gradient(90deg, #004488, #002255);
        padding: 20px; border-radius: 12px; border-left: 8px solid #00aaff;
        text-align: center; margin: 15px 0;
    }
    .staff-box { 
        background: rgba(0, 170, 255, 0.1); padding: 15px; border-radius: 1
