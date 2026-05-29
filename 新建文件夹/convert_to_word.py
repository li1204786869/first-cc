import re
import os
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH

# --- Read source files ---
base = 'd:/cc 内容/新建文件夹/manuscript'

with open(os.path.join(base, 'sections/introduction.tex'), 'r', encoding='utf-8') as f:
    intro_tex = f.read()
with open(os.path.join(base, 'sections/results_discussion.tex'), 'r', encoding='utf-8') as f:
    rd_tex = f.read()
with open(os.path.join(base, 'references.bib'), 'r', encoding='utf-8') as f:
    ref_text = f.read()

def latex_to_text(tex):
    """Strip LaTeX commands, keep readable text."""
    # Remove \section{}, \subsection{} — keep title text
    tex = re.sub(r'\\section\{([^}]*)\}', r'\1', tex)
    tex = re.sub(r'\\subsection\{([^}]*)\}', r'\1', tex)
    # Remove \cite{...}
    tex = re.sub(r'\\cite\{[^}]*\}', '', tex)
    # Remove math mode delimiters
    tex = tex.replace('$', '')
    # Remove LaTeX specials
    tex = tex.replace('~', ' ')
    tex = tex.replace('{', '')
    tex = tex.replace('}', '')
    tex = tex.replace('\\#', '#')
    tex = tex.replace('\\cdot', '·')
    tex = tex.replace('\\degree', '°')
    tex = tex.replace('\\textsubscript', '')
    # Remove leftover backslashes
    tex = re.sub(r'\\[a-zA-Z]+', '', tex)
    # Clean up extra spaces
    tex = re.sub(r'  +', ' ', tex)
    tex = re.sub(r'\n\s*\n', '\n\n', tex)
    return tex.strip()

# --- Create document ---
doc = Document()

# Style setup
style = doc.styles['Normal']
font = style.font
font.name = 'Times New Roman'
font.size = Pt(11)

# === TITLE ===
title = doc.add_paragraph()
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = title.add_run('Bi/MXene Composite Anode with Sandwich Architecture for\nSimultaneously High-Rate and Stable Sodium-Ion Storage')
run.bold = True
run.font.size = Pt(15)
run.font.name = 'Times New Roman'

# Authors placeholder
author = doc.add_paragraph()
author.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = author.add_run('[Authors and Affiliations — to be added]')
run.font.size = Pt(10)
run.font.color.rgb = RGBColor(150, 150, 150)
run.font.name = 'Times New Roman'

# === ABSTRACT ===
doc.add_paragraph()
abs_h = doc.add_paragraph()
run = abs_h.add_run('Abstract')
run.bold = True
run.font.size = Pt(13)
run.font.name = 'Times New Roman'

abs_p = doc.add_paragraph('[To be written after completing the full manuscript]')
abs_p.paragraph_format.first_line_indent = Inches(0.3)

# === INTRODUCTION ===
doc.add_paragraph()
intro_h = doc.add_paragraph()
run = intro_h.add_run('1. Introduction')
run.bold = True
run.font.size = Pt(13)
run.font.name = 'Times New Roman'

intro_text = latex_to_text(intro_tex)
for p in intro_text.split('\n\n'):
    p = p.strip()
    if not p or p == 'Introduction':
        continue
    para = doc.add_paragraph()
    para.paragraph_format.first_line_indent = Inches(0.3)
    para.paragraph_format.space_after = Pt(6)
    para.paragraph_format.line_spacing = 1.5
    run = para.add_run(p)
    run.font.size = Pt(11)
    run.font.name = 'Times New Roman'

# === RESULTS & DISCUSSION ===
doc.add_paragraph()
rd_h = doc.add_paragraph()
run = rd_h.add_run('2. Results and Discussion')
run.bold = True
run.font.size = Pt(13)
run.font.name = 'Times New Roman'

sub_h = doc.add_paragraph()
run = sub_h.add_run('2.1 Synthesis and Structural Characterization of Bi/MXene Composite')
run.bold = True
run.font.size = Pt(12)
run.font.name = 'Times New Roman'

rd_text = latex_to_text(rd_tex)
for p in rd_text.split('\n\n'):
    p = p.strip()
    if not p:
        continue
    # Skip section headings already handled
    if p in ('Results and Discussion', 'Synthesis and Structural Characterization of Bi/MXene Composite'):
        continue
    para = doc.add_paragraph()
    para.paragraph_format.first_line_indent = Inches(0.3)
    para.paragraph_format.space_after = Pt(6)
    para.paragraph_format.line_spacing = 1.5
    run = para.add_run(p)
    run.font.size = Pt(11)
    run.font.name = 'Times New Roman'

# === REFERENCES ===
doc.add_paragraph()
ref_h = doc.add_paragraph()
run = ref_h.add_run('References')
run.bold = True
run.font.size = Pt(13)
run.font.name = 'Times New Roman'

for line in ref_text.strip().split('\n'):
    line = line.strip()
    if line:
        para = doc.add_paragraph()
        para.paragraph_format.space_after = Pt(2)
        para.paragraph_format.line_spacing = 1.15
        run = para.add_run(line)
        run.font.size = Pt(10)
        run.font.name = 'Times New Roman'

# === SAVE ===
output_path = os.path.join(base, 'Bi-MXene_SIB_paper_draft.docx')
doc.save(output_path)
print(f'Done: {output_path}')
