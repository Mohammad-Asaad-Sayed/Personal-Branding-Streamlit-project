
from pathlib import Path
import streamlit as st
from PIL import Image

clarity_code = """
<script type="text/javascript">
    (function(c,l,a,r,i,t,y){
        c[a]=c[a]||function(){(c[a].q=c[a].q||[]).push(arguments)};
        t=l.createElement(r);t.async=1;t.src="https://www.clarity.ms/tag/"+i;
        y=l.getElementsByTagName(r)[0];y.parentNode.insertBefore(t,y);
    })(window, document, "clarity", "script", "mj3lt3d807");
</script>
"""

# Add to your app (best placed in your main script)
st.components.v1.html(clarity_code, height=0, width=0)

THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"

# --- GENERAL SETTINGS ---

GUIDE_DOWNLOAD_LINK = "https://topmate.io/mohammad_asaad_abrar_sayed/1339373"
PRODUCT_NAME = "Personal Branding Guide"
PRODUCT_TAGLINE = "Build Your Powerful Personal Brand - Free Download! 🚀"
PRODUCT_DESCRIPTION = """
My FREE Personal Branding Guide will help you:

- Discover your unique professional identity
- Craft an authentic personal brand statement
- Optimize your LinkedIn and social media profiles
- Create content that showcases your expertise
- Build meaningful professional relationships
- Establish yourself as an industry thought leader

**Get instant access to this comprehensive guide - no strings attached!**
"""

# --- PAGE CONFIG ---
st.set_page_config(
    page_title=PRODUCT_NAME,
    page_icon=":star:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# --- MAIN SECTION ---
st.header(PRODUCT_NAME)
st.subheader(PRODUCT_TAGLINE)
left_col, right_col = st.columns((2, 1))
with left_col:
    st.text("")
    st.write(PRODUCT_DESCRIPTION)

    # Link button that redirects to your Topmate URL
    st.link_button(
        label="⬇️ Download Free Guide",
        url=GUIDE_DOWNLOAD_LINK,
        type="primary"  # Makes the button more prominent
    )

with right_col:
    img_url="guide-preview.png"
    st.image(img_url, width=450)

# --- GUIDE CONTENTS ---
st.subheader("📚 What's Inside The Guide")

with st.expander("🔍 Personal Brand Discovery", expanded=True):
    st.write(
        "Identify your unique strengths, values, and professional differentiators through our step-by-step self-assessment framework.")

with st.expander("🌐 Digital Presence Blueprint"):
    st.write(
        "Transform your LinkedIn profile into a powerful personal branding tool with our optimized profile formula.")

with st.expander("✍️ Content Strategy"):
    st.write(
        "Learn how to create engaging content that establishes your expertise and attracts the right opportunities.")

# --- TESTIMONIALS ---
st.markdown("---")
st.subheader("💬 What People Are Saying")

col1, col2 = st.columns(2)
with col1:
    with st.container(border=True):  # New container with border
        st.write('"Great 1"')
        st.markdown("**Isha O.**, *Career Consultant*")

with col2:
    with st.container(border=True):
        st.write('"The Personal Branding Guide is a lifesaver, a great resource for anyone starting out on their journey of personal branding. Thank you so much for this Mohd. Asaad!!"')
        st.markdown("**Usman P.**, *Freelancer*")

# --- FAQ ---
st.markdown("---")
st.subheader("❓ Frequently Asked Questions")

with st.expander("Is this really free?"):
    st.write("Absolutely! There's no catch - this is my gift to help professionals build their personal brands.")

with st.expander("Do I need any special software?"):
    st.write("No, the guide comes in PDF format that works on any device.")

with st.expander("Can I share this with others?"):
    st.write("Please do! Share the download link with anyone who might benefit.")

with st.expander("Will you follow up with sales pitches?"):
    st.write("No, this is completely free with no upsells or email sequences.")

# --- CONTACT ---
st.markdown("---")
st.subheader("📧 Want To Say Thanks Or Have Questions?")

# Beautiful Contact Form using Streamlit only
st.components.v1.iframe(
    src="https://docs.google.com/forms/d/e/1FAIpQLSfiv4Bba91g98lLMsuSbZ2XNC9xeZZtq8v92Opn977tLgPtfg/viewform?embedded=true",
height=800,
    scrolling=False
)

