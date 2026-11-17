import streamlit as st
import pandas as pd

# 1. إعدادات الصفحة الأساسية
st.set_page_config(
    page_title="OpenPLS Analytics",
    page_icon="🟢",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. تصميم الشعار والهوية البصرية (أخضر وبرتقالي) عبر CSS
st.markdown("""
<style>
    /* تصميم الشعار المتدرج */
    .openpls-logo {
        font-size: 45px;
        font-weight: 900;
        background: -webkit-linear-gradient(45deg, #FF8C00, #4CAF50);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0px;
        font-family: 'Arial', sans-serif;
    }
    .sub-logo {
        text-align: center;
        color: #666;
        font-size: 18px;
        margin-top: -10px;
        margin-bottom: 30px;
        font-weight: bold;
    }
    /* ألوان الأزرار */
    .stButton>button {
        background-color: #FF8C00;
        color: white;
        border-radius: 8px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #4CAF50;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# 3. قاموس الترجمة (عربي - إنجليزي)
translations = {
    "AR": {
        "subtitle": "البديل المفتوح لنمذجة المعادلات الهيكلية (PLS-SEM)",
        "sidebar_title": "⚙️ إعدادات التحليل",
        "lang_select": "🌐 لغة الواجهة / Language",
        "upload_data": "📂 رفع ملف البيانات (Excel/CSV/SAV)",
        "tab1": "📊 عرض البيانات",
        "tab2": "📐 النموذج القياسي (Outer Model)",
        "tab3": "🔗 النموذج الهيكلي (Inner Model)",
        "welcome": "مرحباً بك في OpenPLS! يرجى رفع بياناتك من القائمة الجانبية للبدء.",
        "success_upload": "تم رفع البيانات بنجاح! عدد العينات: "
    },
    "EN": {
        "subtitle": "The Open-Source Alternative for PLS-SEM",
        "sidebar_title": "⚙️ Analysis Settings",
        "lang_select": "🌐 Language / لغة الواجهة",
        "upload_data": "📂 Upload Data File (Excel/CSV/SAV)",
        "tab1": "📊 Data View",
        "tab2": "📐 Measurement Model (Outer Model)",
        "tab3": "🔗 Structural Model (Inner Model)",
        "welcome": "Welcome to OpenPLS! Please upload your data from the sidebar to begin.",
        "success_upload": "Data uploaded successfully! Sample size: "
    }
}

# عرض الشعار في منتصف الصفحة
st.markdown('<p class="openpls-logo">OpenPLS Analytics</p>', unsafe_allow_html=True)

# 4. اللوحة الجانبية (Sidebar)
with st.sidebar:
    st.header("⚙️ OpenPLS Setup")
    # اختيار اللغة
    lang_choice = st.radio("Language", ["AR", "EN"], horizontal=True, label_visibility="collapsed")
    t = translations[lang_choice] # المتغير t سيحمل نصوص اللغة المختارة
    
    st.markdown("---")
    st.subheader(t["sidebar_title"])
    
    # رفع الملف
    uploaded_file = st.file_uploader(t["upload_data"], type=['csv', 'xlsx', 'sav'])

# عرض الشعار الفرعي حسب اللغة
st.markdown(f'<p class="sub-logo">{t["subtitle"]}</p>', unsafe_allow_html=True)

# 5. نظام التبويبات (لتختلف عن المنصة السابقة)
tab1, tab2, tab3 = st.tabs([t["tab1"], t["tab2"], t["tab3"]])

# محتوى التبويبات
if uploaded_file is not None:
    # قراءة الملف (مبدئياً لملفات CSV و Excel)
    try:
        if uploaded_file.name.endswith('.csv'):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)
            
        with tab1:
            st.success(f'{t["success_upload"]} {len(df)}')
            st.dataframe(df.head(10), use_container_width=True)
            
        with tab2:
            st.info("سيتم برمجة خوارزميات PLS للنموذج القياسي (الصدق والثبات) هنا قريباً.")
            
        with tab3:
            st.info("سيتم برمجة اختبار الفرضيات والمسارات هنا قريباً.")
            
    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    with tab1:
        st.info(t["welcome"])
