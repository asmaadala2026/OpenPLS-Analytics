import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="OpenPLS Analytics",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تصميم الهوية البصرية (أخضر وبرتقالي + خط تجوّل الفخم)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
    }
    
    /* البانر العلوي الفخم */
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
    
    /* اسم الباحثة البارز */
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
    
    /* تكبير صندوق الرفع */
    .stFileUploader {
        padding: 20px;
        background-color: #f9fbff;
        border-radius: 15px;
        border: 2px dashed #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

# 3. عرض البانر والشعار واسمك في المنتصف
st.markdown("""
    <div class="hero-banner">
        <h1 class="hero-title">🌟 OpenPLS Analytics</h1>
        <p class="hero-subtitle">المنصة الذكية لنمذجة المعادلات الهيكلية (PLS-SEM)</p>
        <div class="author-badge">👑 تصميم وهندسة: الباحثة أسماء 🇩🇿</div>
    </div>
""", unsafe_allow_html=True)

# 4. اختيار اللغة في القائمة الجانبية
st.sidebar.markdown("### 🌍 لغة الواجهة / Language")
lang = st.sidebar.radio("", ["العربية", "English"], horizontal=True, label_visibility="collapsed")

# 5. منطقة رفع البيانات (بارزة في المنتصف وليست في الجانب)
st.markdown("### 📂 منطقة إدخال البيانات")
uploaded_file = st.file_uploader("ارفعي ملف الاستبيان هنا (بصيغة Excel أو CSV أو SAV) للبدء:", type=["csv", "xlsx", "sav"])

st.markdown("---")

# 6. التفاعلات ونظام التنقل الجديد (بديل التبويبات)
if uploaded_file is None:
    # رسالة ترحيبية وتحفيزية في المنتصف
    st.info("👋 **مرحباً بكِ أستاذة أسماء!** مساحة العمل والمحرك الإحصائي جاهزان. نحن بانتظار رفع بياناتك لتفجير طاقة خوارزميات الـ PLS! 🚀")
    
else:
    # احتفال عند رفع الملف
    st.balloons()
    st.success("🎉 **رائع جداً!** تم استلام وقراءة البيانات بنجاح وبسرعة فائقة. أنتِ الآن جاهزة للتحليل.")
    
    # قراءة البيانات
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
        
    # نظام التنقل الجديد (لوحة تحكم جانبية بدلاً من التبويبات العلوية)
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 🧭 لوحة التحكم (Navigation)")
    st.sidebar.info("اختاري مرحلة التحليل من هنا:")
    
    nav_choice = st.sidebar.radio("", [
        "📊 1. استكشاف وتنظيف البيانات", 
        "📐 2. تقييم النموذج القياسي (Outer)", 
        "🔗 3. اختبار الفرضيات (Inner)"
    ])
    
    # عرض المحتوى بناءً على اختيار القائمة الجانبية
    if nav_choice == "📊 1. استكشاف وتنظيف البيانات":
        st.markdown("#### 📊 نظرة عامة على قاعدة بياناتك:")
        st.warning("💡 **نصيحة بحثية:** تأكدي دائماً من عدم وجود قيم مفقودة (Missing Values) في هذه العينة قبل الانتقال للنموذج القياسي.")
        st.write(f"**حجم العينة الحالي:** {len(df)} مشاركاً.")
        st.dataframe(df.head(15), use_container_width=True)
        
    elif nav_choice == "📐 2. تقييم النموذج القياسي (Outer)":
        st.markdown("#### 📐 خوارزميات النموذج القياسي (Measurement Model)")
        st.info("⚙️ جاري برمجة مكتبات `plspm` لحساب الصدق التقاربي (AVE) والثبات المركب (CR). ستظهر الجداول هنا قريباً!")
        
    elif nav_choice == "🔗 3. اختبار الفرضيات (Inner)":
        st.markdown("#### 🔗 خوارزميات النموذج الهيكلي (Structural Model)")
        st.info("⚙️ جاري برمجة حسابات المسار (Path Coefficients) ومستوى الدلالة (P-value) بتنسيق APA 7. ستظهر قريباً!")
