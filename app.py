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
     "DEM01": "DEM/fluidization.md",
     "DEM02": "DEM/geldart.md",
     "DEM03": "DEM/install.md",
     "DEM04": "DEM/parallel.md",
     "DEM05": "DEM/pour_drum.md",
     "DEM06": "DEM/stl_format.md",
     "FP01": "fundamentals/fokker_planck.md",
     "MDPD01": "MDPD/mdpd_fundamental.md",
     "MDPD02": "MDPD/other_dpds.md", 
     "MDPD03": "MDPD/refs.md",
     "MESH2LAMMPS01": "MESH2LAMMPS/mesh2lammps.md",
     "MESH2LAMMPS02": "MESH2LAMMPS/trimesh.md",
     "MESH2LAMMPS03": "MESH2LAMMPS/trimesh_cylinder.md",
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
