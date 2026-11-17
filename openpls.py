import streamlit as st
import pandas as pd
import time

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="OpenPLS Analytics",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. استدعاء خطوط جديدة كلياً وتصميم CSS متقدم
st.markdown("""
    <style>
        /* استدعاء خط عربي أنيق جداً */
        @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@500;700;900&display=swap');
        
        /* تطبيق الخط على كامل المنصة */
        html, body, [class*="css"] {
            font-family: 'Tajawal', sans-serif !important;
        }
        
        /* البانر العلوي المتدرج (برتقالي وأخضر) */
        .premium-banner {
            background: linear-gradient(135deg, #FF8C00, #4CAF50);
            padding: 30px;
            border-radius: 15px;
            text-align: center;
            color: white;
            box-shadow: 0 10px 20px rgba(0,0,0,0.1);
            margin-bottom: 10px;
            border: 2px solid #fff;
        }
        
        .banner-title {
            font-size: 50px;
            font-weight: 900;
            margin: 0;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            letter-spacing: 2px;
        }
        
        .banner-subtitle {
            font-size: 24px;
            font-weight: 500;
            margin-top: 10px;
            opacity: 0.9;
        }
        
        /* قسم اسم المطور */
        .author-badge {
            text-align: center;
            font-size: 18px;
            color: #FF8C00;
            font-weight: 700;
            margin-bottom: 30px;
            padding: 5px;
            background-color: #fff3e0;
            border-radius: 50px;
            display: inline-block;
            padding: 10px 20px;
            border: 1px solid #FF8C00;
        }
        
        /* تنسيق صندوق الرسائل */
        .stAlert {
            border-radius: 10px !important;
        }
    </style>
""", unsafe_allow_html=True)

# 3. عرض البانر العلوي واسمكِ
st.markdown("""
    <div class="premium-banner">
        <h1 class="banner-title">✨ OpenPLS Analytics ✨</h1>
        <p class="banner-subtitle">البديل المفتوح والذكي لنمذجة المعادلات الهيكلية (PLS-SEM)</p>
    </div>
    <div style="text-align: center;">
        <div class="author-badge">👩‍💻 تطوير وهندسة: الباحثة أسماء 🇩🇿</div>
    </div>
""", unsafe_allow_html=True)

# 4. قاموس الترجمة
translations = {
    "AR": {
        "sidebar_title": "⚙️ غرفة التحكم والبيانات",
        "upload_data": "📂 ارفعي ملف استبيانك هنا (Excel/CSV/SAV)",
        "tab1": "📊 استكشاف البيانات",
        "tab2": "📐 النموذج القياسي (Outer Model)",
        "tab3": "🔗 النموذج الهيكلي (Inner Model)",
        "welcome": "👋 أهلاً بكِ أستاذة! منصة OpenPLS جاهزة لتحليل بياناتك. انطلقي وارفعي الملف من القائمة الجانبية...",
        "success_msg": "🎉 عمل رائع! تم رفع البيانات بنجاح وبسرعة فائقة. عدد العينات الصالحة للتحليل:",
        "motivate": "💡 نصيحة بحثية: تأكدي دائماً أن بياناتك نظيفة من القيم المفقودة قبل بدء تشغيل خوارزميات PLS!"
    },
    "EN": {
        "sidebar_title": "⚙️ Control Room & Data",
        "upload_data": "📂 Upload your dataset here (Excel/CSV/SAV)",
        "tab1": "📊 Data Exploration",
        "tab2": "📐 Measurement Model",
        "tab3": "🔗 Structural Model",
        "welcome": "👋 Welcome Researcher! OpenPLS is ready. Upload your file from the sidebar to start...",
        "success_msg": "🎉 Outstanding! Data uploaded successfully. Valid sample size:",
        "motivate": "💡 Pro Tip: Ensure your data is free of missing values before running the PLS algorithms!"
    }
}

# 5. اللوحة الجانبية مع لمسات تفاعلية
with st.sidebar:
    # صورة تعبيرية في الجانب
    st.image("https://img.icons8.com/color/150/000000/data-configuration.png", use_container_width=True)
    
    lang_choice = st.radio("🌍 اختر لغة الواجهة / Select Language", ["AR", "EN"], horizontal=True)
    t = translations[lang_choice]
    
    st.markdown("---")
    st.subheader(t["sidebar_title"])
    
    # واجهة الرفع
    uploaded_file = st.file_uploader(t["upload_data"], type=['csv', 'xlsx', 'sav'])
    
    if uploaded_file is None:
        st.info("⏳ بانتظار ملف البيانات...")

# 6. نظام التبويبات الفخم
tab1, tab2, tab3 = st.tabs([t["tab1"], t["tab2"], t["tab3"]])

# 7. التفاعل وبرمجة الرفع
if uploaded_file is not None:
    # قراءة الملف 
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            
        with tab1:
            # تفاعل البالونات عند الرفع الناجح
            st.balloons()
            
            # رسالة نجاح مع إيموجي وإحصائية
            st.success(f'{t["success_msg"]} **{len(df)}** مشاركاً.')
            
            # عرض البيانات بتنسيق احترافي
            st.write("### 📋 نظرة عامة على البيانات الخام:")
            st.dataframe(df.style.highlight_null(color='#FF8C00'), use_container_width=True, height=300)
            
            # رسالة تحفيزية سفلية
            st.warning(t["motivate"])
            
        with tab2:
            st.header("📐 مرحلة تقييم النموذج القياسي")
            st.info("🚀 جاري بناء خوارزميات حساب الصدق التقاربي والتمايزي (قريباً)...")
            
        with tab3:
            st.header("🔗 مرحلة اختبار الفرضيات")
            st.info("🚀 جاري تجهيز تقارير APA 7 الخاصة بالمسارات (قريباً)...")
            
    except Exception as e:
        st.error(f"🚨 عذراً، حدث خطأ أثناء قراءة الملف: {e}")
else:
    with tab1:
        st.write(" ")
        st.write(" ")
        # صندوق ترحيبي ملون
        st.info(t["welcome"], icon="💡")
