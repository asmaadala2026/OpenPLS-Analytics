import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="OpenPLS Analytics",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تصميم الهوية البصرية
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #FF8C00, #4CAF50);
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        color: white;
        box-shadow: 0px 10px 20px rgba(0,0,0,0.15);
        margin-bottom: 40px;
        border: 3px solid #f9f9f9;
    }
    
    .hero-title {
        font-size: 55px;
        font-weight: 900;
        margin: 0;
        text-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    
    .hero-subtitle {
        font-size: 22px;
        margin-top: 10px;
        font-weight: 700;
        color: #f1f1f1;
    }
    
    .author-badge {
        background-color: white;
        color: #FF8C00;
        padding: 10px 30px;
        border-radius: 30px;
        font-weight: 900;
        font-size: 20px;
        margin-top: 25px;
        display: inline-block;
        border: 2px solid #4CAF50;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }
    
    .stFileUploader {
        padding: 20px;
        background-color: #f9fbff;
        border-radius: 15px;
        border: 2px dashed #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# 3. عرض البانر
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">🌟 OpenPLS Analytics</h1>
        <p class="hero-subtitle">المنصة الذكية لنمذجة المعادلات الهيكلية (PLS-SEM)</p>
        <div class="author-badge">👑 تصميم وهندسة: الباحثة أسماء 🇩🇿</div>
    </div>
""", unsafe_allow_html=True)

# 4. لغة الواجهة
st.sidebar.markdown("### 🌍 لغة الواجهة / Language")
lang = st.sidebar.radio("", ["العربية", "English"], horizontal=True, label_visibility="collapsed")

# 5. رفع البيانات (بارز في الواجهة)
st.markdown("### 📂 منطقة إدخال البيانات")
uploaded_file = st.file_uploader("ارفعي ملف الاستبيان هنا (بصيغة Excel أو CSV أو SAV) للبدء:", type=["csv", "xlsx", "sav"])

st.markdown("---")

if uploaded_file is None:
    st.info("👋 **مرحباً بكِ أستاذة أسماء!** مساحة العمل جاهزة. ارفعي بياناتك لتبدأ خوارزميات الـ PLS بالعمل! 🚀")
else:
    # إظهار البالونات المتحركة عند الرفع
    st.balloons()
    st.success("🎉 **رائع جداً!** تم استلام البيانات بنجاح وأنتِ الآن جاهزة للتحليل.")
    
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)

    # عرض المراحل بشكل متسلسل في الواجهة الرئيسية
    st.markdown("### 📊 1. استكشاف وتنظيف البيانات")
    st.write(f"**حجم العينة الحالي:** {len(df)} مشاركاً.")
    st.dataframe(df.head(15), use_container_width=True)
    
    st.markdown("---")
    st.markdown("### 📐 2. تقييم النموذج القياسي (Outer Model)")
    st.info("⚙️ جاري برمجة حساب الصدق التقاربي (AVE) والثبات المركب (CR).")
    
    st.markdown("---")
    st.markdown("### 🔗 3. اختبار الفرضيات (Inner Model)")
    st.info("⚙️ جاري برمجة حسابات المسار (Path Coefficients).")
