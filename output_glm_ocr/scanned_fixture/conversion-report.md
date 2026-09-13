# Conversion report — scanned_fixture.pdf

- job_id: a499f00d-d499-4512-95d5-6ddd1f3c00b0
- status: assembling
- pages: 3
- wall-clock: not started
- tokens: prompt=49235 completion=3198
- pipeline_version: 77ca3a05b80cc24b9f872d6b9b7d3a5a3e45d53f35b87e62d9835656f30dcc5e
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 30

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 100 | 0 | 200 | 11547 | 653 | False |
| 2 | verified | 100 | 0 | 80 | 5371 | 726 | False |
| 3 | verified | 97 | 1 | 300 | 32317 | 1819 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 2
- converted to Mermaid: 2 (100%)
- data-table fallbacks: 0
- image fallbacks: 0

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 1 | 36 | classDiagram | mermaid | 85 |
| 3 | 37 | classDiagram | mermaid | 95 |

## Omissions log

- page 1: Figure 1 is a sidebar diagram ("Sidebar: Unified Notation 0.8") that wraps the first column of body text; its internal labels (Used, Base Class, Had by Reference, Had By Value, Derived 1, Derived 2) are captured in the alt text and omitted from body text as figure content. No typo corrections were needed. No uncertain characters.
- page 2: - Footnote 1 continues at bottom of page.
- Subscripts in the Liskov quotation (o_S, o_T) rendered as plain $o$ per OCR; original reads "object o₁ of type S ... object o₂ of type T ... when o₂ is substituted for o₁".
- Inline code formatting (typeid, static_cast, DrawShape, Shape, DrawSquare, DrawCircle) added for readability; source uses monospace in code/identifiers.
- Running header and page number excluded from body.
- page 3: - Continuation from page 2: text flows from "This should be a significant clue that there is a problem" (page 3 ends mid-sentence, continues on page 4).
- Figure 1 caption label "Figure 1." appears inside the boxed diagram region; transcribed as figure caption rather than body text.
- Source typo preserved: code sets `{itsHeight=w;}` in SetHeight (should be =h; original source shows w — DEC-009, not corrected to avoid altering code semantics).
- Source typo preserved verbatim: "identical.”" (stray closing quote) and "Generally these problem are" (grammar error).

## Running furniture stripped

- '# The Liskov Substitution Principle' (on 2 pages)

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 235465B model=glm-5.3-flash effort=low transcribe_ms=6996.4 verify_ms=3167.1 ocr_ms=26176.4 retries=0 verification_score=100 floor=100% hashes=eabe5f8204e7221509640203a1c0b3ec2bfc7d67216b1bfdb3f54e84da6debf2/e993b9f4270e0b367b753633561d62701b3331eb706d7d4efe88dc8972d616be/6b8316edba738e978be55bbb5aa6d93667ebfd04716af246c90eb84e05dd6dc5/1ec444080a77d1802de663d7660eb76062ed1936ea4871d9b0288a958082c23f
- page 2: dpi=80 image=680x880 124073B model=glm-5.3-flash effort=low transcribe_ms=7867.4 verify_ms=2270.8 ocr_ms=962553.0 retries=0 verification_score=100 floor=100% hashes=eabe5f8204e7221509640203a1c0b3ec2bfc7d67216b1bfdb3f54e84da6debf2/7782c94ff8d66d5051910adec79fd8eb916d6622b14881631a8a567b5332ac10/b4d1358e4fcee3d8f4542b323b823a5990479dc1ea5286cbbbd85a57dd73a9fc/978f256169a73ba6ad7fdcd2ff35571c24a477108bd33ff97c3ff28e2dbbe41f
- page 3: dpi=300 image=2550x3300 1137709B model=glm-5.3-flash effort=low transcribe_ms=19661.9 verify_ms=9810.5 ocr_ms=45924.9 retries=1 verification_score=97 floor=100% hashes=eabe5f8204e7221509640203a1c0b3ec2bfc7d67216b1bfdb3f54e84da6debf2/909122f84ddb1471c727cd3f823d6488aca45cf808b447b625ab4752bf94c9b6/a88ad21d4ecda4e1e19e6928f14a93a9366a31694a835cf53edfc38fb3f0f2be/e39ee0315e00293c341f09f93f2d02d67fd506ada8724bf5d4fa226c366a8ad7

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:1: [Expected: 80, Actual: 510]
- MD041:1:
- MD013:12: [Expected: 80, Actual: 238]
- MD033:14: [Element: details]
- MD013:17: [Expected: 80, Actual: 156]
- MD036:19:
- MD033:21: [Element: details]
- MD013:24: [Expected: 80, Actual: 226]
- MD013:31: [Expected: 80, Actual: 349]
- MD013:33: [Expected: 80, Actual: 388]
- MD013:35: [Expected: 80, Actual: 305]
- MD013:37: [Expected: 80, Actual: 126]
- MD013:39: [Expected: 80, Actual: 130]
- MD013:41: [Expected: 80, Actual: 303]
- MD013:43: [Expected: 80, Actual: 419]
- MD013:47: [Expected: 80, Actual: 164]
- MD013:59: [Expected: 80, Actual: 293]
- MD013:61: [Expected: 80, Actual: 276]
- MD013:63: [Expected: 80, Actual: 89]
- MD026:65:
- MD013:67: [Expected: 80, Actual: 146]
- MD013:83: [Expected: 80, Actual: 271]
- MD013:90: [Expected: 80, Actual: 97]
- MD033:92: [Element: details]
- MD013:95: [Expected: 80, Actual: 153]
- MD013:101: [Expected: 80, Actual: 264]
- MD013:103: [Expected: 80, Actual: 196]
- MD013:105: [Expected: 80, Actual: 390]
- MD013:107: [Expected: 80, Actual: 398]
- MD013:109: [Expected: 80, Actual: 345]
