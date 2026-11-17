import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة
st.set_page_config(
    page_title="OpenPLS Analytics",
    page_icon="🌟",
    layout="wide"
)

# 2. تصميم الهوية البصرية (الخطوط والألوان)
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Tajawal', sans-serif !important;
    }
    
    .hero-banner {
        background: linear-gradient(135deg, #FF8C00, #4CAF50);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        color: white;
        margin-bottom: 25px;
        box-shadow: 0px 5px 15px rgba(0,0,0,0.1);
    }
    
    .hero-title {
        font-size: 45px;
        font-weight: 900;
        margin: 0;
    }
    
    .author-badge {
        background-color: white;
        color: #FF8C00;
        padding: 8px 25px;
        border-radius: 20px;
        font-weight: 900;
        font-size: 18px;
        margin-top: 15px;
        display: inline-block;
        border: 2px solid #4CAF50;
    }
    
    /* تكبير وتجميل التبويبات (Tabs) */
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        font-size: 20px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# 3. قاموس اللغات (تم إصلاحه ليعمل بشكل سليم)
texts = {
    "العربية": {
        "title": "🌟 OpenPLS Analytics",
        "subtitle": "المنصة الذكية لنمذجة المعادلات الهيكلية (PLS-SEM)",
        "author": "👑 تصميم وهندسة: الباحثة أسماء 🇩🇿",
        "lang_title": "🌍 لغة الواجهة",
        "upload_title": "📂 منطقة إدخال البيانات",
        "upload_desc": "ارفعي ملف الاستبيان هنا (Excel/CSV/SAV):",
        "welcome": "👋 مرحباً بكِ أستاذة أسماء! مساحة العمل جاهزة. ارفعي بياناتك لتبدأ خوارزميات الـ PLS بالعمل! 🚀",
        "success": "🎉 رائع جداً! تم استلام وقراءة البيانات بنجاح.",
        "tabs": ["📊 1. استكشاف البيانات", "📐 2. تقييم النموذج القياسي (Outer)", "🔗 3. اختبار الفرضيات (Inner)"],
        "sample_size": "حجم العينة الحالي:",
    },
    "English": {
        "title": "🌟 OpenPLS Analytics",
        "subtitle": "The Smart Platform for PLS-SEM",
        "author": "👑 Developed by: Researcher Asmaa 🇩🇿",
        "lang_title": "🌍 Language",
        "upload_title": "📂 Data Input Area",
        "upload_desc": "Upload your questionnaire file here (Excel/CSV/SAV):",
        "welcome": "👋 Welcome Asmaa! The workspace is ready. Upload your data to start the PLS algorithms! 🚀",
        "success": "🎉 Excellent! Data received and read successfully.",
        "tabs": ["📊 1. Data Exploration", "📐 2. Measurement Model", "🔗 3. Structural Model"],
        "sample_size": "Current Sample Size:",
    }
}

# 4. القائمة الجانبية للغة
st.sidebar.markdown(f"### {texts['العربية']['lang_title']}")
lang = st.sidebar.radio("", ["العربية", "English"], horizontal=True, label_visibility="collapsed")
t = texts[lang]

# 5. عرض البانر العلوي
st.markdown(f"""
    <div class="hero-banner">
        <h1 class="hero-title">{t['title']}</h1>
        <p style="font-size: 22px; font-weight: 700; margin-top: 10px;">{t['subtitle']}</p>
        <div class="author-badge">{t['author']}</div>
    </div>
""", unsafe_allow_html=True)

# 6. الرفع من الواجهة الرئيسية
st.markdown(f"### {t['upload_title']}")
uploaded_file = st.file_uploader(t['upload_desc'], type=["csv", "xlsx", "sav"])
st.markdown("---")

# 7. معالجة البيانات والتبويبات
if uploaded_file is None:
    st.info(t["welcome"])
else:
    st.success(t["success"]) # بدون بالونات
    
    # قراءة الملف
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)
    else:
        df = pd.read_excel(uploaded_file)
        
    # إعادة التبويبات (Tabs)
    tab1, tab2, tab3 = st.tabs(t["tabs"])
    
    with tab1:
        st.write(f"**{t['sample_size']} {len(df)}**")
        st.dataframe(df.head(15), use_container_width=True)
        
    with tab2:
        st.subheader("📐 جدول معايير الصدق والثبات (Measurement Model)")
        st.warning("💡 (مخرجات توضيحية - Mockup) - هكذا سيظهر جدول النتائج بتنسيق APA 7 بعد ربط خوارزمية PLS.")
        
        # إنشاء جدول نتائج وهمي ومحترف لملء الفراغ
        mock_outer = pd.DataFrame({
            "المتغير (Construct)": ["القيادة الإدارية", "الرضا الوظيفي", "الأداء العام"],
            "Cronbach's Alpha (α)": [0.852, 0.814, 0.910],
            "Composite Reliability (CR)": [0.885, 0.856, 0.932],
            "AVE (الصدق التقاربي)": [0.654, 0.589, 0.721]
        })
        st.dataframe(mock_outer, use_container_width=True)
        
    with tab3:
        st.subheader("🔗 جدول اختبار الفرضيات والمسارات (Structural Model)")
        st.warning("💡 (مخرجات توضيحية - Mockup) - هكذا ستظهر القرارات الإحصائية النهائية.")
        
        # جدول مسارات وهمي
        mock_inner = pd.DataFrame({
            "المسار (Path)": ["القيادة -> الأداء", "الرضا -> الأداء", "القيادة -> الرضا"],
            "Beta (β)": [0.451, 0.320, 0.560],
            "T-Value": [4.215, 3.150, 6.890],
            "P-Value": ["0.000 ***", "0.002 **", "0.000 ***"],
            "القرار": ["مدعومة ✅", "مدعومة ✅", "مدعومة ✅"]
        })
        st.dataframe(mock_inner, use_container_width=True)
