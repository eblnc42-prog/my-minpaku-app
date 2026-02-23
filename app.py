import streamlit as st
import datetime
import urllib.parse

# 1. ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 2. リンク先URLの定義（ここで一括管理してエラーを防ぐ）
URL_TIMETABLE_KOSHIBE = "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E52"
URL_TIMETABLE_SHIMO = "https://www.kintetsu.co.jp/station/station_info/timetable.html?stcode=E54"
URL_MICHINOEKI = "https://yoshinoji-oyodo.com/"
URL_HAKUSUIEN = "https://hakusuien.com/"
URL_KINPUSENJI = "https://www.kinpusen.or.jp/"

# Googleマップリンクを生成する関数（リンク切れ・改行エラー防止）
def get_map_url(name):
    base = "https://www.google.com/maps/search/?api=1&query="
    return base + urllib.parse.quote(name)

# 3. 言語選択
sel_lang = st.selectbox("🌐 Language / 言語選択", ["日本語", "English"])

# 4. ヘッダー
st.title("✈︎ Jin")
jst_now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
st.write(f"{jst_now.strftime('%H:%M')} | Oyodo, Nara")

# 5. タブ構成
tab1, tab2, tab3, tab4 = st.tabs(["🏠 HOME", "📶 INFO", "🗺️ GUIDE", "🆘 HELP"])

with tab1:
    if sel_lang == "日本語":
        st.subheader("Welcome to Jin")
        st.info("40の資格を持つオーナーと、タイ出身の元教師の妻が営む、吉野の隠れ家へようこそ。")
        st.metric(label="Check-out / チェックアウト", value="10:00 AM")
        st.divider()
        st.write("👨‍✈️ **Hitoshi Kobayashi:** 元鉄道運転士・元タクシー運転手・整備士")
        st.write("👩‍🏫 **Nisachol:** タイ出身の元英語教師 (English/Thai/Lao OK)")
    else:
        st.subheader("Welcome to Jin")
        st.info("A cozy hideaway in Yoshino, run by a multi-talented owner and his Thai wife.")
        st.metric(label="Check-out", value="10:00 AM")

with tab2:
    st.subheader("📶 Wi-Fi Info")
    st.success("SSID: Deco_C884 / PW: Q99srAe5")
    st.divider()
    st.subheader("📜 House Rules")
    st.write("- 室内は完全禁煙です (No smoking inside)")
    st.write("- 夜22:00以降はお静かに (Quiet after 10PM)")
    st.write("- ✨ **無料の愛車点検・洗車**はオーナーまで！")

with tab3:
    st.subheader("🛒 Shopping & 🍽 Dining")
    c1, c2 = st.columns(2)
    with c1:
        st.write("キリン堂 大淀桧垣本店")
        st.link_button("📍 Map", get_map_url("キリン堂 大淀桧垣本店"))
        st.write("ライフ 大淀店")
        st.link_button("📍 Map", get_map_url("ライフ 大淀店"))
    with c2:
        st.write("赤影 / 鳥欽 (焼き鳥)")
        st.link_button("📍 Map", get_map_url("大淀町 赤影"))
        st.write("和光 (寿司)")
        st.link_button("📍 Map", get_map_url("大淀町 和光 寿司"))

    st.divider()
    st.subheader("🚌 Transport")
    st.warning("吉野タクシー: 0746-32-2961")
    col_k1, col_k2 = st.columns(2)
    with col_k1:
        st.link_button("🚉 越部駅 時刻表", URL_TIMETABLE_KOSHIBE)
    with col_k2:
        st.link_button("🚉 下市口駅 時刻表", URL_TIMETABLE_SHIMO)

    st.divider()
    st.subheader("📍 Sightseeing")
    st.link_button("🌲 道の駅 吉野路大淀iセンター", URL_MICHINOEKI)
    st.link_button("🍐 博水園 (梨狩り)", URL_HAKUSUIEN)
    st.link_button("🌸 金峯山寺 (吉野山)", URL_KINPUSENJI)

with tab4:
    st.subheader("🆘 Support")
    st.error("Emergency: 080-9419-6063 (Owner: Kobayashi)")
    st.divider()
    st.subheader("🏥 Medical Info")
    st.write("南奈良総合医療センター: 0747-54-5000")
    st.write("中辻医院: 0
