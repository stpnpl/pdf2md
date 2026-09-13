# Conversion report — scanned_fixture.pdf

- job_id: 17e9905a-1b84-4586-8b6b-b65b11675a42
- status: assembling
- pages: 3
- wall-clock: not started
- tokens: prompt=34406 completion=2142
- pipeline_version: 9c215872aa0b575aade8ae9fb73a81b65c9fb7d96e9934b244133c2636e44bc0
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 34

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 100 | 0 | 200 | 10926 | 540 | False |
| 2 | verified | 99 | 0 | 200 | 11463 | 723 | False |
| 3 | verified | 95 | 0 | 200 | 12017 | 879 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 2
- converted to Mermaid: 2 (100%)
- data-table fallbacks: 0
- image fallbacks: 0

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 1 | 38 | classDiagram | mermaid | 95 |
| 3 | 39 | classDiagram | mermaid | 95 |

## Omissions log

- page 1: No typo corrections needed. Sidebar diagram rendered as figure placeholder; diagram labels listed in alt text. Page number excluded from body.
- page 2: - Corrected "make is safer" — left as-is per source (possible typo, uncorrected to preserve meaning) — actually retained verbatim.
- Liskov quote reproduced as blockquote with italics and subscripted o1/o2.
- Footnote rule rendered as horizontal rule; footnote text preserved at end of page.
- page 3: - Figure 1 shows a UML inheritance diagram: Rectangle box at top, generalization arrow pointing to it from Square box below.
- Source typo left verbatim: `SetHeight(double h) {itsHeight=w;}` (should be `h`).
- Source typo left verbatim: "identical\"." (stray quote and period).
- Source grammar left verbatim: "Generally these problem are not foreseen".
- Page ends mid-sentence; continues on next page.

## Running furniture stripped

- '# The Liskov Substitution Principle' (on 2 pages)

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 235465B model=glm-5.3-flash effort=low transcribe_ms=4020.4 verify_ms=2684.1 ocr_ms=424.5 retries=0 verification_score=100 floor=n/a hashes=eabe5f8204e7221509640203a1c0b3ec2bfc7d67216b1bfdb3f54e84da6debf2/e993b9f4270e0b367b753633561d62701b3331eb706d7d4efe88dc8972d616be/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855/4e4862382655afb0b74447dc2739a2a7b2d16297c0cbccc18ec301d2c5cffc81
- page 2: dpi=200 image=1700x2200 283840B model=glm-5.3-flash effort=low transcribe_ms=6674.8 verify_ms=3425.9 ocr_ms=424.7 retries=0 verification_score=99 floor=n/a hashes=eabe5f8204e7221509640203a1c0b3ec2bfc7d67216b1bfdb3f54e84da6debf2/eeb0c00b3313ca8d080bca5b25f722dc75af6723dfee7b855a3a71998e378048/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855/82f6ba5939d25a8dd4445ba75f04f6da2ce97441647594edfc8c7d61d103ef9f
- page 3: dpi=200 image=1700x2200 311095B model=glm-5.3-flash effort=low transcribe_ms=7888.0 verify_ms=5572.1 ocr_ms=437.4 retries=0 verification_score=95 floor=n/a hashes=eabe5f8204e7221509640203a1c0b3ec2bfc7d67216b1bfdb3f54e84da6debf2/835b3e81ef192ddcab2cf3412b752f70f058aca8920299980fcbfa86b38aed37/e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855/5a3b9f43e130386e43626d0b7399c105dbb88c293c934892ed033a093ac83c75

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:1: [Expected: 80, Actual: 510]
- MD041:1:
- MD013:19: [Expected: 80, Actual: 220]
- MD033:21: [Element: details]
- MD013:24: [Expected: 80, Actual: 156]
- MD036:26:
- MD033:28: [Element: details]
- MD013:31: [Expected: 80, Actual: 152]
- MD013:38: [Expected: 80, Actual: 349]
- MD013:40: [Expected: 80, Actual: 388]
- MD013:42: [Expected: 80, Actual: 305]
- MD013:44: [Expected: 80, Actual: 130]
- MD013:46: [Expected: 80, Actual: 142]
- MD033:46: [Element: sup]
- MD013:48: [Expected: 80, Actual: 333]
- MD033:48: [Element: sub]
- MD033:48: [Element: sub]
- MD033:48: [Element: sub]
- MD033:48: [Element: sub]
- MD013:50: [Expected: 80, Actual: 419]
- MD013:54: [Expected: 80, Actual: 164]
- MD013:66: [Expected: 80, Actual: 294]
- MD013:68: [Expected: 80, Actual: 276]
- MD013:72: [Expected: 80, Actual: 89]
- MD026:74:
- MD013:76: [Expected: 80, Actual: 146]
- MD013:92: [Expected: 80, Actual: 271]
- MD013:99: [Expected: 80, Actual: 134]
- MD033:101: [Element: details]
- MD013:110: [Expected: 80, Actual: 264]
- MD013:112: [Expected: 80, Actual: 196]
- MD013:114: [Expected: 80, Actual: 390]
- MD013:116: [Expected: 80, Actual: 398]
- MD013:118: [Expected: 80, Actual: 346]
