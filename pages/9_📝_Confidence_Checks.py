import streamlit as st
from load_css import local_css


st.set_page_config(
    page_title='Pre and Post-Bootcamp Confidence Checks',
    page_icon="📚"
)

local_css("css/style.css")

st.markdown(
    """
## 📋 Confidence Checks

These surveys help us assess whether this bootcamp improves your Python skills. Please complete both surveys at the appropriate times.
"""
)

st.divider()

# Pre-bootcamp section
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("### 📝")
with col2:
    st.markdown("### Pre-Bootcamp Survey")

st.info("⏰ **Complete this BEFORE the bootcamp starts**")

st.markdown(
    """
Record your current confidence level with the topics and techniques that will be covered in the bootcamp.

[📋 Open Pre-Bootcamp Survey](https://forms.office.com/e/1qrBP8s8Ri)
"""
)

st.divider()

# Post-bootcamp section
col1, col2 = st.columns([1, 5])
with col1:
    st.markdown("### ✅")
with col2:
    st.markdown("### Post-Bootcamp Survey")

st.success("⏰ **Complete this AFTER the bootcamp ends**")

st.markdown(
    """
Record your confidence level with the topics and techniques after completing the bootcamp.

[📊 Open Post-Bootcamp Survey](https://forms.office.com/e/yBgUpbnypX)
"""
)