# -*- coding: utf-8 -*-
import streamlit as st
import streamlit.components.v1 as components
import json
import os

#st.set_page_config(layout="wide")　最大化

markdown_contents = {}
note_paths = {
    "topics0001": "notes/topics0001.md",
    "topics0002": "notes/topics0002.md",
    "topics0003": "notes/topics0003.md",
    "dem_topics0001": "DEM/topics0001.md",
    "mdpd_refs": "MDPD/refs.md",
    "ioz_topics0001": "IOZ/topics0001.md",
    "ioz_topics0002": "IOZ/topics0002.md",
    "ioz_topics0003": "IOZ/topics0003.md",
    "pfm_topics0001": "PFM/topics0001.md",
    "mlip_install": "MLIP/install.md",
    "deepmd_dplr": "DEEPMD/dplr.md",
    "aenet_install": "AENET/aenet_install.md",
    "aenet_lammps": "AENET/aenet_lammps.md",
    "reaxff_install": "LAMMPS/reaxff_install.md",
    "fix_bond_react": "LAMMPS/fix_bond_react.md",
    "fix_bond_react_key": "LAMMPS/fix_bond_react_key.md",
    "volume_fraction": "COLLOID/volume_fraction.md",
    "eff_volume_fraction": "COLLOID/eff_volume_fraction.md",
    "kd_viscosity": "COLLOID/kd_viscosity.md",
    "gel_intro": "COLLOID/gel_intro.md",
    "dpd_Pan2010": "COLLOID/dpd_Pan2010.md",
    "kapsel_install": "KAPSEL/kapsel_install.md",
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
