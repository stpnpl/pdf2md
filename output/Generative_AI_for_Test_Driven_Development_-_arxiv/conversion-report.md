# Conversion report — Generative AI for Test Driven Development - arxiv.pdf

- job_id: 07a86115-2281-4e39-9a42-48c0f258599f
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=150956 completion=9441
- pipeline_version: 073654be6c457b411ab24a51dcfff4bdea2968daf6252a3e996dc1f6b48c7d48
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 70

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 100 | 1 | 300 | 30996 | 1679 | False |
| 2 | verified | 98 | 0 | 200 | 13171 | 884 | False |
| 3 | verified | 98 | 0 | 200 | 13822 | 896 | False |
| 4 | verified | 98 | 0 | 200 | 13941 | 721 | False |
| 5 | verified | 96 | 0 | 200 | 14561 | 952 | False |
| 6 | verified | 96 | 1 | 300 | 35044 | 2195 | False |
| 7 | verified | 97 | 0 | 200 | 14307 | 1014 | False |
| 8 | verified | 98 | 0 | 200 | 15114 | 1100 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 1
- converted to Mermaid: 0 (0%)
- data-table fallbacks: 0
- image fallbacks: 1

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 52 | flowchart | image | 88 |

## Omissions log

- page 1: - Verification miss fixed: arXiv sidebar stamp "arXiv:2405.10849v1 [cs.SE] 17 May 2024" is reproduced as first line of Markdown body (it is rotated vertical text in the left margin, ~x=60-150, y=950-2450, so its position cannot be fully conveyed inline).
- Footnote markers rendered as ^1^/^2^ inline and GFM footnotes [^1]/[^2]; footnote text continues on next page potentially.
- Author ORCID iDs rendered as superscripts per source.
- No corrections to source text were needed; no figures on this page.
- page 2: Continues from page 1 ("...the use of GenAI / can speed up testing...") and Section 2 heading follows mid-page. No figures on this page. No typos corrected. Rendered italic placeholder tokens ⟨...⟩ as LaTeX math \langle...\rangle.
- page 3: Page continues the bullet list of prompts from Section 2 and the paragraph from Section 2; Section 3 heading is a continuation of the document. Text ends mid-sentence, continuing on page 4. No figures on this page. No typos corrected; "fulfils" and "actuate" are source verbatim.
- page 4: Page begins mid-paragraph continuing from previous page; first visible body line is "activity ③. The red text...". Figure 1 bbox estimated from diagram region. Table 1 has an empty extra row in the source (excluded). No uncertain characters.
- page 5: Table 2 caption and content transcribed per OCR ground truth. Monospaced ChatGPT output block rendered as fenced code block. No figures on this page. No corrections needed.
- page 6: - The fenced code block at the top continues the ChatGPT recommendation block started on the previous page (items 1 appeared there); kept as a single logical code block continuation.
- Header and page number excluded from body per rules; listed in FURNITURE.
- No figures on this page.
- page 7: - Continues sentence from previous page ("...without replacing developers in terms of creativity...") and ends mid-sentence ("for our experiment and settings,") continuing on next page.
- *et al.* in italics per source.
- No figures on this page; Fig. 1 placeholder in rolling context belongs to an earlier page.
- page 8: No figures on page. Running header "8 Moritz Mock, Jorge Melegati, and Barbara Russo" excluded from body. Reference 13's DOI "https://doi.org/doi.org/10.48550/arXiv.2312.04687" appears duplicated in the source; kept verbatim. No corrections needed.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=300 image=2550x3300 521533B model=glm-5.3-flash effort=low transcribe_ms=11948.6 verify_ms=6372.8 ocr_ms=45766.0 retries=1 verification_score=100 floor=100% hashes=1964c7cade1db971a180794d5a9f107e14ee1f9ac7b029611b05c613e32099ba/46faa41a8fad32c14ff7322ad5edb29f71c6e5f44ba7aa055a8515af133f0041/cda5e83b6d36ee39964f9d4650bcb41ba1a35777171c978d69360835bbe521ca/bf772dcd1efcfd57af3787ca65652aeeb8a17821953e073e4f423f711cef5cde
- page 2: dpi=200 image=1700x2200 375495B model=glm-5.3-flash effort=low transcribe_ms=6191.2 verify_ms=3107.4 ocr_ms=24852.2 retries=0 verification_score=98 floor=100% hashes=3c648d8a8ad82d73cb3ad8682164e9dd6d1eff4634e3d208ce3528912bb2cdf2/2097b825ff6e6ae62164cb5147145d318ebc4976006ff4c1f75e9a842aa3cd22/88b02b75cb86ca2ff13849bea728c5aa021ea6c39ec8293139908f606ec2f3b7/afb8de71f3c75c4c05e9cbae0d2769de981780707ae1099a22fb71e3311ffaf0
- page 3: dpi=200 image=1700x2200 377854B model=glm-5.3-flash effort=low transcribe_ms=5338.0 verify_ms=2965.3 ocr_ms=25218.4 retries=0 verification_score=98 floor=100% hashes=6d8946229ce606afd2d87696403caf0101d9e89a904d19116b0dd0fe97abe035/aff78325cb55fa51fec9b9392070b4e6ef96d9d90df8b6ba912b1b8cae5133d9/f0de9a4c9fba4c44efc930bdea4f0dd0261a0318732513d439e97c1d0bdf8933/928505a12e0c238a03b392d5f383b133d018b913592a731aef10c10d0106215c
- page 4: dpi=200 image=1700x2200 271130B model=glm-5.3-flash effort=low transcribe_ms=4794.8 verify_ms=2412.4 ocr_ms=19954.1 retries=0 verification_score=98 floor=100% hashes=32e24aa9bee2ee11f48a382710253abb427086a93cb7db1ecb5e0af6504dea45/e8eba92ee8548bf5889de49b9ab7b0b45a8e0de04008758cb997656f2e848014/6ab9752babea71f9ddb8861e24a90c1189e6a6c69939ed16336c949617842aa2/3a67a942572137e0c421aaa368c675a14204d273d4712d04980cde93ee8b939f
- page 5: dpi=200 image=1700x2200 340524B model=glm-5.3-flash effort=low transcribe_ms=5553.1 verify_ms=2861.2 ocr_ms=29071.1 retries=0 verification_score=96 floor=100% hashes=44deedf3162db13b3c4bb6e3a72ac287bbda44100286431ad4562a2bce10698b/04e32695178e626fd0f301944013f9806cc08a7cfaa42b0d1d1bdfb74dfea6d2/7bbdaa390b2f3fbc5be92b53b938af997b7883fd2857a0f0e85dd1b51053dc79/72263f8aea419c47e111023f393190b033025733fd06e9b98e99624c3bf84350
- page 6: dpi=300 image=2550x3300 581163B model=glm-5.3-flash effort=low transcribe_ms=13631.9 verify_ms=7258.9 ocr_ms=49451.4 retries=1 verification_score=96 floor=100% hashes=8cfd0be1b76af5ca8574a616f35d45b0d001350825be92b20291ad67e28f045e/fc9429a49154d9985bdc4c4a18e757acd69bc579023f38bd6994625e16e21704/4afe8dadbdcca2cc2adb3bd055ab1f564ee4e5238dc107ecf8907e56ebbfbbd8/694420bffaaead687d2899423216d35f475e6e0a8ebe433fc1e55292a1959d41
- page 7: dpi=200 image=1700x2200 370883B model=glm-5.3-flash effort=low transcribe_ms=6595.7 verify_ms=2918.2 ocr_ms=23881.6 retries=0 verification_score=97 floor=100% hashes=a0785837b1858dda78f6e96da32f0e32a949627f5aebe1fec56e1bd021f630b0/698739cc078a2ed4fb950d766b43327b237c7be93c1221028c4f34080c29bc04/4d96ea8f32b087dec64b681b8ce7a0bc1084f0fb7d307217b7de9d3fa3db8734/561a534e4bcb2e5dfc797e01081be5e2194ab9cf0a252934dcb54278e82e36d5
- page 8: dpi=200 image=1700x2200 388311B model=glm-5.3-flash effort=low transcribe_ms=6131.5 verify_ms=2769.4 ocr_ms=34844.2 retries=0 verification_score=98 floor=100% hashes=139af2dfceaa712a4219f2d96163cb24fdeda73a739de7814c5dec1941d53072/7bd35a4831ba08e0f631bd9be6e5ec288eef541b8ad48cbb7fcaed3b7088f151/2765b8ec85bd4e919b9538cb567ac94cbf1a67ff2c37a9f1338ebeda77e297bf/16a8774998859aad0450fb117c69a6d272e6d810c6ec6da3a3f3b007adf28d86

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD041:1:
- MD013:15: [Expected: 80, Actual: 115]
- MD013:20: [Expected: 80, Actual: 1109]
- MD013:26: [Expected: 80, Actual: 882]
- MD013:28: [Expected: 80, Actual: 138]
- MD013:30: [Expected: 80, Actual: 238]
- MD013:34: [Expected: 80, Actual: 2333]
- MD013:36: [Expected: 80, Actual: 313]
- MD013:37: [Expected: 80, Actual: 138]
- MD013:40: [Expected: 80, Actual: 942]
- MD013:42: [Expected: 80, Actual: 549]
- MD013:44: [Expected: 80, Actual: 616]
- MD034:44:
- MD013:48: [Expected: 80, Actual: 1018]
- MD036:52:
- MD013:56: [Expected: 80, Actual: 187]
- MD013:58: [Expected: 80, Actual: 337]
- MD013:60: [Expected: 80, Actual: 290]
- MD013:62: [Expected: 80, Actual: 640]
- MD013:66: [Expected: 80, Actual: 98]
- MD013:67: [Expected: 80, Actual: 98]
- MD013:68: [Expected: 80, Actual: 98]
- MD013:69: [Expected: 80, Actual: 98]
- MD013:70: [Expected: 80, Actual: 98]
- MD013:71: [Expected: 80, Actual: 98]
- MD013:72: [Expected: 80, Actual: 98]
- MD013:74: [Expected: 80, Actual: 145]
- MD013:76: [Expected: 80, Actual: 97]
- MD013:77: [Expected: 80, Actual: 97]
- MD013:78: [Expected: 80, Actual: 97]
- MD013:79: [Expected: 80, Actual: 97]
- MD013:80: [Expected: 80, Actual: 97]
- MD013:81: [Expected: 80, Actual: 97]
- MD013:82: [Expected: 80, Actual: 97]
- MD013:83: [Expected: 80, Actual: 97]
- MD013:85: [Expected: 80, Actual: 154]
- MD013:87: [Expected: 80, Actual: 1628]
- MD013:89: [Expected: 80, Actual: 510]
- MD040:91:
- MD040:98:
- MD013:106: [Expected: 80, Actual: 248]
- MD013:108: [Expected: 80, Actual: 1657]
- MD013:112: [Expected: 80, Actual: 312]
- MD013:113: [Expected: 80, Actual: 312]
- MD013:114: [Expected: 80, Actual: 312]
- MD013:115: [Expected: 80, Actual: 312]
- MD013:116: [Expected: 80, Actual: 312]
- MD013:117: [Expected: 80, Actual: 312]
- MD013:118: [Expected: 80, Actual: 312]
- MD013:120: [Expected: 80, Actual: 318]
- MD013:124: [Expected: 80, Actual: 2403]
- MD013:128: [Expected: 80, Actual: 305]
- MD013:130: [Expected: 80, Actual: 545]
- MD013:134: [Expected: 80, Actual: 229]
- MD013:139: [Expected: 80, Actual: 155]
- MD013:140: [Expected: 80, Actual: 220]
- MD013:141: [Expected: 80, Actual: 132]
- MD013:142: [Expected: 80, Actual: 117]
- MD013:143: [Expected: 80, Actual: 195]
- MD013:144: [Expected: 80, Actual: 130]
- MD013:145: [Expected: 80, Actual: 141]
- MD013:146: [Expected: 80, Actual: 119]
- MD013:147: [Expected: 80, Actual: 101]
- MD013:148: [Expected: 80, Actual: 161]
- MD013:149: [Expected: 80, Actual: 151]
- MD013:150: [Expected: 80, Actual: 164]
- MD034:150:
- MD013:151: [Expected: 80, Actual: 226]
- MD013:152: [Expected: 80, Actual: 167]
- MD034:152:
