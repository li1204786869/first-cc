# Bi/MXene 钠离子电池快充负极论文 — 实施计划

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 从实验数据出发，完成一篇 Bi/MXene 钠离子电池快充负极的英文全文，目标投稿 Energy Storage Materials / Nano Energy / Small 梯队期刊。

**Architecture:** 采用 PaperSpine 动机驱动写作流程。先分类材料来源、确认 Motivation → 研究目标期刊 → 学习范文结构与修辞 → 建立段落功能模板 → 构建 Evidence Bank → 创建章节蓝图 → 逐节写作 → 语言润色与审计。输出为 LaTeX 源码 + 编译后的 PDF。

**Tech Stack:** PaperSpine (写作流程), LaTeX (排版), nature-polishing (语言润色), nature-citation (参考文献), nature-figure (图表制作)

---

## 文件结构

```
新建文件夹/
├── paper_rewriting_output/          # PaperSpine 写作产物
│   ├── source_map.md                # 材料来源分类
│   ├── confirmed_motivation.md      # 经确认的 motivation
│   ├── target_journal_research.md   # 目标期刊研究
│   ├── exemplar_learning_dossier.md # 范文学习档案
│   ├── style_profile.md             # 风格配置文件
│   ├── paragraph_function_templates.md  # 段落功能模板
│   ├── result_narrative_templates.md    # 结果叙述模板
│   ├── motivation_thread_model.md    # Motivation 线索模型
│   ├── motivation_surface_map.md     # Motivation 表层对齐
│   ├── evidence_bank.md             # 实验证据库
│   └── section_blueprints.md        # 章节蓝图
├── manuscript/                       # LaTeX 稿件
│   ├── main.tex                      # 主文件
│   ├── sections/                     # 各章节 .tex
│   │   ├── introduction.tex
│   │   ├── results_discussion.tex
│   │   ├── conclusion.tex
│   │   └── methods.tex
│   ├── figures/                      # 图片文件
│   ├── references.bib                # 参考文献
│   └── supporting_info.tex           # Supporting Information
└── docs/superpowers/
    ├── specs/2026-05-25-bi-mxene-paper-design.md
    └── plans/2026-05-25-bi-mxene-paper-plan.md
```

---

## Phase 1: 基础搭建

### Task 1: 创建材料来源地图

**Files:**
- Create: `paper_rewriting_output/source_map.md`

- [ ] **Step 1: 与用户确认所有数据来源**

用户需提供以下内容（请用户将相关文件放入工作目录或说明位置）：
- 实验原始数据和汇总表格 (Excel/CSV 等)
- 材料表征图片 (SEM, TEM, XRD, XPS)
- 电化学测试数据 (GCD, CV, EIS, 循环, 倍率等)
- 已有的草稿/笔记/大纲（如有）
- 参考文献列表或 .bib 文件
- 同领域优秀范文（3-6 篇，用于后续学习）

- [ ] **Step 2: 创建 source_map.md**

向用户确认后，创建以下分类文件：

```markdown
# Source Map — Bi/MXene SIB Fast-Charging Paper

## 1. Primary Data
- [ ] Electrochemical data (GCD, rate, cycling, CV, EIS)
  - Source: <user provides file path>
- [ ] Materials characterization images (SEM, TEM, XRD, XPS)
  - Source: <user provides file path>

## 2. Drafts & Notes
- [ ] Any existing draft text or notes
  - Source: <TBD>

## 3. Figures (to be created)
- [ ] Scheme 1: Synthesis process of Bi/MXene composite
- [ ] Figure 1: Morphology (SEM/TEM of MXene, Bi/MXene)
- [ ] Figure 2: Structure (XRD, XPS)
- [ ] Figure 3: Electrochemical performance (GCD, rate, cycling)
- [ ] Figure 4: Kinetics analysis (CV at various scan rates, EIS, GITT)
- [ ] Figure 5: Mechanism discussion (ex-situ XRD/XPS after cycling)
- [ ] Figure 6: Comparison table with literature

## 4. References
- [ ] .bib file or reference list
  - Source: <TBD>

## 5. Exemplar Papers (for style learning)
- [ ] Exemplar 1: <publication info>
- [ ] Exemplar 2: <publication info>
- [ ] Exemplar 3: <publication info>
- [ ] Exemplar 4-6: <publication info>
```

- [ ] **Step 3: 用户确认后再进入下一任务**

---

### Task 2: 确认核心 Motivation

**Files:**
- Create: `paper_rewriting_output/confirmed_motivation.md`

- [ ] **Step 1: 将设计文档中的 motivation 写入确认文件**

```markdown
# Confirmed Motivation — Bi/MXene SIB Fast-Charging Paper

## Core Motivation Statement
Sodium-ion battery fast-charging anodes face an inherent trade-off 
among rate capability, capacity, and cycling stability — achieving 
all three simultaneously remains a critical bottleneck.

## Problem → Solution → Claim Logic

1. **Problem**: SIB anode materials typically sacrifice one of: 
   high rate capability, high specific capacity, or long cycle life.

2. **Gap**: Bismuth offers high theoretical capacity (384 mAh/g for Na₃Bi) 
   but suffers from poor conductivity and severe volume expansion, 
   causing rate and cycling degradation.

3. **Solution**: MXene (Ti₃C₂Tₓ) serves as a 2D conductive scaffold that:
   - Enhances electronic conductivity
   - Buffers volume expansion of Bi during sodiation/desodiation
   - Provides additional active sites

4. **Claim**: The Bi/MXene composite anode simultaneously achieves 
   high rate capability, high specific capacity, and long cycling 
   stability — breaking the traditional trade-off.

## Key Evidence to Support the Claim
- Rate performance data showing capacity retention at high current densities
- Long-term cycling data with Coulombic efficiency
- First-cycle ICE demonstrating practical viability
- Comparative benchmarking against reported SIB anodes
```

- [ ] **Step 2: 请用户审核并确认 motivation，或在以下备选方案中选择**

如用户认为上述 motivation 需要调整，提供备选方向：
- **Variant A**: 强调 Bi/MXene 界面工程对快充的独特贡献
- **Variant B**: 强调 MXene 限域效应抑制 Bi 颗粒粉碎
- **Variant C**: 强调合成方法的通用性/可扩展性

---

### Task 3: 目标期刊调研

**Files:**
- Create: `paper_rewriting_output/target_journal_research.md`

- [ ] **Step 1: 调研 Energy Storage Materials 的投稿要求**

使用 WebSearch 检索：
- Energy Storage Materials Guide for Authors
- 近期发表的 SIB 快充方向论文 3 篇（了解风格和深度）
- 格式要求：字数限制、图表数量、参考文献格式

- [ ] **Step 2: 调研 Nano Energy 作为备选**

- Nano Energy Guide for Authors
- 近期 SIB 快充论文风格对比

- [ ] **Step 3: 确认最终目标期刊并记录调研结果**

```markdown
# Target Journal Research

## Primary Target: Energy Storage Materials
- **IF**: ~20.4 (2024)
- **Scope**: Energy storage materials and devices
- **Article Types**: Research Paper, Review, Short Communication
- **Key Requirements**:
  - Graphical abstract required
  - Highlights (3-5 bullet points, 85 char each)
  - No strict word limit but concise
  - Figures: typically 6-8 main figures
  - Supporting Information allowed

## Recent SIB Fast-Charging Papers in ESM
1. <Paper 1 details>
2. <Paper 2 details>
3. <Paper 3 details>

## Style Observations
- <Common patterns observed in these papers>
```

---

## Phase 2: 范文学习

### Task 4: 学习范文结构与修辞

**Files:**
- Create: `paper_rewriting_output/exemplar_learning_dossier.md`

- [ ] **Step 1: 选择 3-6 篇范文**

范文选择标准：
- 来自 Energy Storage Materials / Nano Energy / Small / ACS Energy Letters 等目标梯队期刊
- 主题：MXene 储能、Bi 基 SIB 负极、SIB 快充负极
- 时间：2022-2026 年
- 至少 2 篇与 MXene 相关，至少 2 篇与合金型 SIB 负极相关

- [ ] **Step 2: 对每篇范文做 deep reading 分析**

每篇范文分析以下维度（参考 PaperSpine `references/deep-reading.md`）：
```markdown
## Exemplar 1: <Title, Journal, Year>

### Motivation Analysis
- What problem does the paper claim to solve?
- How does it frame the gap?
- What is the explicit novelty claim?

### Section-Level Structure
- Introduction: How many paragraphs? What's each paragraph's job?
- Results: How are results grouped? What's the narrative flow?
- Discussion: How do they connect results to the bigger picture?

### Rhetorical Moves (Introduction, paragraph-by-paragraph)
| Para | Function | Key Sentences |
|------|----------|---------------|
| 1    | Broad context | "..."
| 2    | Specific problem | "..."
| 3    | Existing solutions + their limits | "..."
| 4    | This work | "Herein, we..."

### Data Presentation Patterns (Results)
- How are electrochemical data presented?
- What order: morphology → structure → performance → mechanism?
- How is benchmarking done?

### Language Features
- Sentence length typical range
- Active vs passive voice ratio
- Hedging strength (may, suggest, indicate, demonstrate, prove)
- Transition strategies between figures/results
```

- [ ] **Step 3: 汇总范文学习结论**

提取可复用的跨论文模式：
```markdown
## Cross-Exemplar Patterns

### Universal Introduction Structure
<Observed pattern>

### Common Performance Reporting Sequence
<Observed pattern>

### Mechanism Discussion Depth
<What level do these papers go to?>
```

---

### Task 5: 创建风格配置文件

**Files:**
- Create: `paper_rewriting_output/style_profile.md`

- [ ] **Step 1: 基于范文学习提取风格参数**

```markdown
# Style Profile — Bi/MXene Paper

## Target Venue Style (derived from ESM exemplars)

### Paragraph Structure
- Typical paragraph length: 120-180 words
- Topic sentence position: First sentence (deductive)
- Transition style: Logical flow, minimal explicit transition words

### Sentence Architecture
- Preferred: Subject-Verb-Object, active voice for claims
- Evidence sentences: passive voice acceptable
- Average sentence length: 18-25 words
- Mix: 60% complex sentences, 40% simple/compound

### Vocabulary Tier
- Claims: demonstrate, reveal, achieve, deliver, exhibit
- Comparisons: outperform, surpass, exceed, superior to
- Mechanism: facilitate, enable, promote, contribute to
- Avoid: show (too weak), prove (too strong for data), first time (cliché)

### Data Reporting Conventions
- "delivers a specific capacity of X mAh/g at Y C"
- "retains Z% after N cycles"
- "corresponds to a capacity decay of only X% per cycle"

### Figure Referencing
- "As shown in Figure Xa, ..."
- "Figure Xb reveals that ..."
- "The XPS spectrum (Figure Xc) confirms ..."
```

---

### Task 6: 创建段落功能模板

**Files:**
- Create: `paper_rewriting_output/paragraph_function_templates.md`

基于范文学习结果，为每种段落类型创建可复用模板：

```markdown
# Paragraph Function Templates

## P-BROAD: Broad Context Opening (Intro P1)
Function: Establish the importance of the field
Structure:
  1. Societal/technological need (1 sentence)
  2. Why this need matters for energy storage (1 sentence)
  3. Where SIBs fit in (1 sentence)
  4. The specific challenge within SIBs (1 sentence)

Template:
"The growing demand for [application] has spurred intensive research
into [technology class]. Among [technology options], [specific tech]
has emerged as [positioning] owing to [key advantage]. However,
[critical bottleneck] remains a significant hurdle for [practical goal]."

## P-PROBLEM: Problem Identification (Intro P2)
...

## P-GAP: Gap Statement (Intro P3)
...

## P-SOLUTION: Our Approach (Intro P4)
...

## R-MORPH: Morphology Reporting (Results)
...

## R-PERF: Performance Reporting (Results)
...

## R-MECH: Mechanism Discussion (Results/Discussion)
...
```

---

### Task 7: 创建结果叙述模板

**Files:**
- Create: `paper_rewriting_output/result_narrative_templates.md`

```markdown
# Result Narrative Templates

## Template R-NARR-1: From Synthesis to Structure
Scenario setup → Synthesis approach → Morphology observation → Structure confirmation → Implication for electrochemistry

Sentence sequence:
1. "The Bi/MXene composite was synthesized via [method] (Scheme 1)."
2. "SEM images (Figure 1a,b) reveal [morphology description]..."
3. "TEM analysis (Figure 1c,d) further confirms [structure detail]..."
4. "XRD patterns (Figure 2a) show [phase info]..."
5. "XPS spectra (Figure 2b-d) verify [chemical state]..."
6. "This [structure feature] is expected to [electrochemical benefit]..."

## Template R-NARR-2: Electrochemical Performance
...

## Template R-NARR-3: Kinetics and Mechanism
...
```

---

## Phase 3: 写作设计

### Task 8: 构建 Motivation 线索模型

**Files:**
- Create: `paper_rewriting_output/motivation_thread_model.md`

将 confirmed motivation 转化为论文各部分的线索分配：

```markdown
# Motivation Thread Model

## Key Terms (anchor words for the spine)
- Primary: simultaneous, trade-off, rate-capacity-stability
- Secondary: conductive scaffold, volume buffering, structural integrity

## Thread Distribution

| Section | Motivation Connection | Key Terms to Hit |
|---------|----------------------|------------------|
| Title | Implicit: "High-Rate and Stable" flags the claim | high-rate, stable, Bi/MXene |
| Abstract | Explicit: states the problem and the solution | trade-off, simultaneously achieves |
| Intro P1 | Broad: why fast-charging matters | fast-charging, grid storage |
| Intro P2 | Problem: the rate-capacity-stability conflict | trade-off, compromise |
| Intro P3 | Gap: existing solutions and their limits | however, still suffer |
| Intro P4 | Solution: Bi/MXene breaks the trade-off | herein, simultaneously delivers |
| Results 1 | Structural basis for the solution | conductive network, scaffold |
| Results 2 | Performance proving the claim | rate, cycling, ICE |
| Results 3 | Mechanism explaining why it works | facilitated Na⁺ diffusion, buffered |
| Discussion | Return to the spine | breaking the trade-off, synergy |
| Conclusion | Restate the claim with evidence | simultaneous achievement |
```

---

### Task 9: 创建 Motivation 表层对齐

**Files:**
- Create: `paper_rewriting_output/motivation_surface_map.md`

确保 motivation 在标题、小标题、主题句和过渡句中自然体现：

```markdown
# Motivation Surface Map

## Title Candidates
1. "Bi/MXene Composite Anodes Enabling Simultaneously High-Rate, 
   High-Capacity, and Stable Sodium-Ion Storage"
2. "Breaking the Rate-Capacity-Stability Trade-off: Bi Nanoparticles 
   Anchored on MXene Nanosheets for Fast-Charging Sodium-Ion Batteries"
3. "MXene Scaffold-Regulated Bi Anode for Synergistically Enhanced 
   Rate Capability and Cycling Stability in Sodium-Ion Batteries"

## Abstract Topic Sentences
1. State the trade-off problem
2. Introduce Bi/MXene design rationale
3. Present key performance metrics (rate, cycling, ICE)
4. Explain mechanism briefly
5. Conclude with significance

## Section Headings (Results)
- 2.1 Synthesis and Structural Characterization of Bi/MXene Composite
- 2.2 Electrochemical Sodium Storage Performance
- 2.3 Reaction Kinetics and Charge Storage Mechanism
- 2.4 Post-Cycling Analysis and Structural Stability

## Check: Naturalness
- How often does "trade-off" appear? (max ~4 times across whole paper)
- Are the headings specific and informative without being repetitive?
```

---

### Task 10: 构建实验证据库

**Files:**
- Create: `paper_rewriting_output/evidence_bank.md`

**重要：此任务需要用户提供实验数据。**

- [ ] **Step 1: 请用户提供实验数据文件**

向用户请求以下数据：
1. SEM/TEM 图片文件
2. XRD 谱图（原始数据或图片）
3. XPS 谱图
4. 电化学数据（倍率、循环、CV、EIS 等作为 Excel/CSV 或图片）
5. 任何已整理的对比表格

- [ ] **Step 2: 录入证据到证据库**

```markdown
# Evidence Bank

## E1: Morphology
- **Claim to support**: MXene provides 2D conductive scaffold; Bi is well-dispersed
- **Evidence**: SEM (Figure X), TEM (Figure Y)
- **Data file**: <path>
- **Status**: [ ] Ready / [ ] Needs replotting / [ ] Needs new measurement

## E2: Crystal Structure
- **Claim to support**: Bi/MXene composite crystallinity and phase
- **Evidence**: XRD (Figure X)
- **Data file**: <path>
- **Status**: [ ] Ready / [ ] Needs replotting

## E3: Chemical State
- **Claim to support**: Successful synthesis, Bi-MXene interaction
- **Evidence**: XPS (Figure X)
- **Data file**: <path>
- **Status**: [ ] Ready

## E4: Rate Performance
- **Claim to support**: High capacity at high rates
- **Evidence**: Rate capability data (Figure X)
- **Data file**: <path>
- **Key numbers**: <e.g., X mAh/g at 0.1C, Y mAh/g at 50C>
- **Status**: [ ] Ready

## E5: Cycling Stability
- **Claim to support**: Long cycle life
- **Evidence**: Long-term cycling data (Figure X)
- **Data file**: <path>
- **Key numbers**: <e.g., Z% retention after N cycles at X C>
- **Status**: [ ] Ready

## E6: First-Cycle ICE
- **Claim to support**: High ICE for practical viability
- **Evidence**: GCD curves (Figure X), ICE values
- **Data file**: <path>
- **Key numbers**: ICE = X%
- **Status**: [ ] Ready

## E7: Kinetics
- **Claim to support**: Fast Na⁺ diffusion, capacitive contribution
- **Evidence**: CV at various scan rates, EIS, GITT (Figures X)
- **Data file**: <path>
- **Key numbers**: D_Na⁺ = X cm²/s, capacitive contribution = Y%
- **Status**: [ ] Ready

## E8: Post-Cycling Structure
- **Claim to support**: Structural stability, volume buffering
- **Evidence**: Post-cycling SEM/TEM/XRD (Figure X)
- **Data file**: <path>
- **Status**: [ ] Ready

## E9: Literature Benchmarking
- **Claim to support**: Competitive performance vs state-of-the-art
- **Evidence**: Comparison table (Table X)
- **Data source**: Literature survey
- **Status**: [ ] To be compiled
```

---

### Task 11: 创建章节蓝图

**Files:**
- Create: `paper_rewriting_output/section_blueprints.md`

```markdown
# Section Blueprints

## Introduction Blueprint (4 paragraphs)

### Intro-P1: Field Importance
- **Function**: Establish urgency of fast-charging energy storage
- **Move**: Broad need → role of SIBs → anode challenge
- **Key claim**: Anode dictates rate performance
- **Template ref**: P-BROAD

### Intro-P2: Existing Solutions
- **Function**: Review current SIB anode materials for fast-charging
- **Move**: Carbon-based anodes → alloy-type anodes → their limitations
- **Key claim**: Each material class has a rate-capacity-stability trade-off
- **Template ref**: P-PROBLEM

### Intro-P3: MXene + Bi Rationale
- **Function**: Introduce the proposed solution
- **Move**: MXene properties → Bi advantages → synergy concept
- **Key claim**: MXene scaffolds can resolve Bi's conductivity + volume issues
- **Template ref**: P-GAP

### Intro-P4: This Work
- **Function**: State what we did and what we achieved
- **Move**: Synthesis approach → characterization → key results → significance
- **Key claim**: Bi/MXene simultaneously achieves high rate, capacity, and stability
- **Template ref**: P-SOLUTION

## Results & Discussion Blueprint

### R&D-S1: Synthesis and Structure (2-3 paragraphs)
- **Para 1**: Synthesis route description + Scheme 1
  - Evidence: E1 (morphology), synthesis details from user's data
- **Para 2**: SEM/TEM morphology analysis
  - Evidence: E1 (SEM, TEM images)
- **Para 3**: XRD and XPS structural confirmation
  - Evidence: E2 (XRD), E3 (XPS)

### R&D-S2: Electrochemical Performance (3-4 paragraphs)
- **Para 1**: Basic electrochemical behavior (GCD, CV at low scan rate)
  - Evidence: E6 (GCD/ICE), E4 (basic CV)
- **Para 2**: Rate capability
  - Evidence: E4 (rate data)
- **Para 3**: Cycling stability
  - Evidence: E5 (cycling data)
- **Para 4**: Performance benchmarking table
  - Evidence: E9 (comparison table)

### R&D-S3: Kinetics and Mechanism (2-3 paragraphs)
- **Para 1**: CV kinetics analysis (capacitive vs diffusion)
  - Evidence: E7 (CV at multiple scan rates)
- **Para 2**: GITT and EIS for Na⁺ diffusion
  - Evidence: E7 (GITT/EIS data)
- **Para 3**: Post-cycling structural analysis
  - Evidence: E8 (post-cycling TEM/XRD)

## Conclusion Blueprint (1-2 paragraphs)
- **Para 1**: Restate the main achievements with key numbers
- **Para 2**: Broader significance and outlook

## Methods Blueprint
- Synthesis section
- Materials characterization section
- Electrochemical measurements section
```

---

## Phase 4: 写作

### Task 12: 撰写 Introduction

**Files:**
- Create: `manuscript/sections/introduction.tex`

- [ ] **Step 1: 按蓝图撰写 Introduction 4 段**

按照 Section Blueprints 中的 Introduction 蓝图书写，逐段执行：
1. 先写段落大纲（每句话的 claims）
2. 参照 paragraph_function_templates 的对应模板
3. 保持 motivation_surface_map 的一致性
4. 写完整草稿
5. 对照 style_profile 自查

- [ ] **Step 2: 提交用户审核 Introduction**

### Task 13: 撰写 Results & Discussion

**Files:**
- Create: `manuscript/sections/results_discussion.tex`

按 Section Blueprints 中三个子章节逐一撰写，每小节完成后请用户确认数据准确性。

### Task 14: 撰写 Conclusion + Methods

**Files:**
- Create: `manuscript/sections/conclusion.tex`
- Create: `manuscript/sections/methods.tex`

### Task 15: 组装完整稿件

**Files:**
- Create: `manuscript/main.tex`
- Create: `manuscript/references.bib`
- Modify: 整合所有 section 文件

---

## Phase 5: 润色与审计

### Task 16: 语言润色

**Files:**
- Modify: `manuscript/sections/*.tex` (全文)

使用 nature-polishing 技能对全文进行 Nature 级英文润色。

### Task 17: 参考文献与格式检查

使用 nature-citation 技能检查引用完整性和格式合规性。

### Task 18: 图表质量检查

使用 nature-figure 技能审计和优化所有图表。

### Task 19: 最终审计与投稿准备

- [ ] Motivation 一致性检查（对照 motivation_surface_map）
- [ ] Evidence 完整性检查（对照 evidence_bank）
- [ ] LaTeX 编译检查
- [ ] 投稿材料准备（Graphical Abstract, Highlights, Cover Letter）
