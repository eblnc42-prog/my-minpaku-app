import streamlit as st
import datetime

# ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 言語データの定義
LANG_DICT = {
    "日本語": {
        "welcome": "Welcome to Jin",
        "desc": "40の資格を持つオーナーと、タイ出身の元教師の妻が営む、吉野の隠れ家へようこそ。",
        "checkout_label": "Check-out / チェックアウト",
        "wifi_label": "Wi-Fi Info",
        "rules": "House Rules",
        "rule_list": ["室内は完全禁煙です（屋外指定場所のみ可）", "夜22:00以降はお静かにお願いします", "無料の愛車点検・洗車をご希望の方はオーナーまで！"],
        "guide": "Shopping / Dining",
        "sightseeing": "Sightseeing",
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
        "checkout_label": "Check-out",
        "wifi_label": "Wi-Fi Info",
        "rules": "House Rules",
        "rule_list": ["No smoking inside", "Please be quiet after 10 PM", "Free car inspection/wash available on request!"],
        "guide": "Shopping / Dining",
        "sightseeing": "Sightseeing",
        "shops": "🛒 Shopping",
        "dining": "🍽 Dining",
        "transport": "🚌 Transport / ATM",
        "support": "Support",
        "medical": "Medical",
        "staff_info": "Meet Our Staff"
    }
}

# CSSデザイン
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
    .accent-blue { color: #00aaff; font-weight: bold; font-size: 1.5rem; margin-bottom: 10px; }
    .big-value { font-size: 3rem; font-weight: bold; color: white; }
    .map-btn {
        display: inline-block; padding: 5px 12px; background: #00aaff; color: white !important;
        text-decoration: none; border-radius: 5px; font-size: 0.8rem; margin-top: 5px;
    }
    .rule-item { margin-bottom: 10px; font-size: 1.3rem; border-left: 3px solid #00aaff; padding-left: 15px; }
    .staff-box { background: rgba(0, 170, 255, 0.1); padding: 20px; border-radius: 10px; margin-top: 10px; border: 1px dashed
