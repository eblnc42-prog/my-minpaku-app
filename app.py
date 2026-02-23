import streamlit as st
import datetime

# ページ設定
st.set_page_config(page_title="Jin Guest Concierge", layout="wide")

# 言語設定
sel_lang = st.selectbox("🌐 Language / 言語選択", ["日本語", "English"])

# デザイン（CSS）
common_style = """
<style>
    .main { background-color: #002255; color: white; }
    .info-card { 
        background: rgba(255,255,255,0.1); 
        padding: 20px; 
        border-radius: 15px; 
        margin-bottom: 15px; 
        border: 1px solid rgba(255,255,255,0.2); 
    }
    .accent { color: #00aaff; font-weight: bold; font-size: 1.2rem; margin-bottom: 5px; }
    .map-link { color: #00aaff !important; text-decoration: none; font-weight: bold; }
    .checkout-box { background: #004488; padding: 15px; border-radius: 10px; text-align: center; margin: 10px 0; }
</style>
"""
st.markdown(common_style, unsafe_allow_html=True)

# ヘッダー
col_t, col_s = st.columns([3, 2])
with col_t:
    st.header("✈︎ Jin")
with col_s:
    now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
    st.write(now.strftime('%H:%M') + " | Oyodo, Nara")

# タブ
tab1, tab2, tab3, tab4 = st.tabs(["HOME", "INFO", "GUIDE", "HELP"])

with tab1:
    if sel_lang == "日本語":
        home_html = """
        <div class="info-card">
            <p>40の資格を持つオーナーと、タイ出身の元教師の妻が営む、吉野の隠れ家へようこそ。</p>
            <div class="checkout-box">
                <div style="font-size: 1.2rem;">Check-out / チェックアウト</div>
                <div style="font-size: 2.5rem; font-weight: bold;">10:00 AM</div>
            </div>
        </div>
        <div class="info-card">
            <div class="accent">Staff Information</div>
            <p>👨‍✈️ <b>Hitoshi Kobayashi</b><br>元鉄道運転士・元タクシー運転手・自動車整備士</p>
            <p>👩‍🏫 <b>Nisachol</b><br>タイ出身の元英語教師 (English / Thai / Lao OK)</p>
        </div>
        """
    else:
        home_html = """
        <div class="info-card">
            <p>A cozy hideaway in Yoshino, run by a multi-talented owner and his Thai wife.</p>
            <div class="checkout-box">
                <div style="font-size: 1.2rem;">Check-out</div>
                <div style="font-size: 2.5rem; font-weight: bold;">10:00 AM</div>
            </div>
        </div>
        """
    st.markdown(home_html, unsafe_allow_html=True)

with tab2:
    info_html = """
    <div class="info-card">
        <div class="accent">Wi-Fi Info</div>
        <p>SSID: <b>Deco_C884</b><br>Password: <b>Q99srAe5</b></p>
    </div>
    <div class="info-card">
        <div class="accent">House Rules</div>
        <ul>
            <li>室内は完全禁煙です</li>
            <li>夜22:00以降はお静かにお願いします</li>
            <li><b>無料の愛車点検・洗車</b>をご希望の方はオーナーまで！</li>
        </ul>
    </div>
    """
    st.markdown(info_html, unsafe_allow_html=True)

with tab3:
    c1, c2 = st.columns(2)
    with c1:
        shop_html = """
        <div class="info-card">
            <div class="accent">🛒 Shopping</div>
            <p><b>キリン堂 大淀桧垣本店</b><br>
            <a href="https://www.google.com/maps/search/?api=1&query=キリン堂+大淀桧垣本店" target="_blank" class="map-link">📍 Google Map</a></p>
            <p><b>ライフ 大淀店</b><br>
            <a href="https://www.google.com/maps/search/?api=1&query=ライフ+大淀店" target="_blank" class="map-link">📍 Google Map</a></p>
        </div>
        """
        st.markdown(shop_html, unsafe_allow_html=True)
    with c2:
        food_html = """
        <div class="info-card">
            <div class="accent">🍽 Dining</div>
            <p><b>赤影 / 鳥欽 (焼き鳥)</b><br>
            <a href="https://www.google.com/maps/search/?api=1&query=赤影+大淀町" target="_blank" class="map-link">📍 Google Map</a></p>
            <p><b>和光 (寿司)</b><br>
            <a href="https://www.google.com/maps/search/?api=1&query=和光+大淀町+寿司" target="_blank" class="map-link">📍 Google Map</a></p>
        </div>
        """
        st.markdown(food_html, unsafe_allow_html=True)
    
    trans_html = """
    <div class="info-card">
