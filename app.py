import streamlit as st
import datetime

# ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 言語データの定義（すべての項目を全言語で完全に統一）
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

# デザイン設定（さらに文字を大きく）
st.markdown("""
    <style>
    .main { background-color: #002255; color: white; }
