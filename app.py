# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components
import json
import os

st.set_page_config(layout="wide")
st.markdown("""
<style>
.block-container {
    max-width: 900px;
    margin-left: auto;
    margin-right: auto;
}
</style>
""", unsafe_allow_html=True)

markdown_contents = {}
note_paths = {
     "chapter001": "notes/chapter001.md",
     "chapter002": "notes/chapter002.md",
     "chapter003": "notes/chapter003.md",
     "topics004": "notes/topics004.md",
     "topics005": "notes/topics005.md",
     "sfgmd": "notes/sfgmd.md",
     "non_condon_effect": "notes/non_condon_effect.md",
     "rotation_matrix_01": "notes/rotation_matrix_01.md", 
     "rotation_matrix_02": "notes/rotation_matrix_02.md",
     "window": "notes/window.md",
     "artifact_in_3200": "notes/artifact_in_3200.md",
     "nma01": "notes/nma01.md",
     "nma02": "notes/nma02.md",
     "nma03": "notes/nma03.md",
     "nma04": "notes/nma04.md",
     "nma05": "notes/nma05.md",
     "nma06": "notes/nma06.md",
}

for key, path in note_paths.items():
    try:
        with open(path, "r", encoding="utf-8") as f:
            markdown_contents[key] = f.read()
    except FileNotFoundError:
        st.error(f"ZKANICS ERROR: note file not found: {path}")
        st.stop()

markdown_json = json.dumps(markdown_contents)

with open("index.html", encoding="utf-8") as f:
    html_template = f.read()

html_content = html_template.replace(
    "// MARKDOWN_DATA_PLACEHOLDER",
    f"const allMarkdownData = {markdown_json};"
)

components.html(html_content, height=2000, scrolling=True)
#components.html(html_content, height=800, width=None, scrolling=True)　最大化
