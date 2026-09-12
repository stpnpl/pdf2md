# Conversion report — Generative AI for Test Driven Development - arxiv.pdf

- job_id: be15e0c9-3062-47f7-bec4-08c579eeb164
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=235923 completion=13472
- pipeline_version: 073654be6c457b411ab24a51dcfff4bdea2968daf6252a3e996dc1f6b48c7d48
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 74

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 97 | 0 | 200 | 12331 | 942 | False |
| 2 | verified | 95 | 0 | 200 | 13158 | 890 | False |
| 3 | verified | 100 | 1 | 300 | 33967 | 1684 | False |
| 4 | needs_review | 95 | 2 | 400 | 54521 | 2639 | True |
| 5 | verified | 95 | 0 | 200 | 14567 | 982 | False |
| 6 | verified | 98 | 1 | 300 | 35050 | 1816 | False |
| 7 | verified | 98 | 0 | 200 | 14305 | 979 | False |
| 8 | verified | 96 | 2 | 400 | 58024 | 3540 | False |

## needs_review pages

[4]

## Diagram → Mermaid conversion

- figures: 1
- converted to Mermaid: 1 (100%)
- data-table fallbacks: 0
- image fallbacks: 0

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 82 | flowchart | mermaid | 88 |

## Omissions log

- page 1: - Running vertical arXiv sidebar ("arXiv:2405.10849v1 [cs.SE] 17 May 2024") excluded from body; listed as furniture.
- Footnotes transcribed at bottom of body with superscript markers; footnote 1-2 URLs preserved.
- Email line rendered with monospace for local part to reflect typewriter font in source.
- "automatize" kept as in source (DEC-009 allows typo correction, but this is valid/idiomatic variant usage; no change logged).
- "et al." italic per source.
- page 2: Page continues the paragraph from page 1 ("...can speed up testing"). No figures on this page. Math angle-bracket placeholders rendered as LaTeX $\langle...\rangle$ per source. No typos corrected.
- page 3: Page continues the bulleted list from previous page ("Final iteration: Refactor the code."). No figures on this page. No typo corrections needed.
- page 4: verification cap reached
- page 5: No figures on this page (Fig. 1 and Table 1 were on page 4 per rolling context). Code block reproduced verbatim from OCR, including the odd line break before "textFormatter'". No typo corrections made beyond rendering curly quotes as straight quotes in the code block.
- page 6: - Page 6 continues the code block from page 5 (items 2–3 of ChatGPT-recommended changes); rendered here as plain numbered text, merging into the preceding fenced code block from page 5.
- Curly quotes in code block normalized to backticks (verbatim code text per source style).
- No figures on this page.
- page 7: Page 7 continues Section 3 conclusions sentence ("Overall, we found that for our experiment and settings,") carried over from rolling context; sentence completes on next page. "Open AI's Codex" kept as in source (line break artifact; standard form "OpenAI's"). No figures on this page.
- page 8: - Running header "8    Moritz Mock, Jorge Melegati, and Barbara Russo" excluded from body per rules; listed in FURNITURE.
- Continuation: opening paragraph completes the sentence begun at end of Section 5 Conclusions on page 7 ("Overall, we found that for our experiment and settings,").
- No figures or decorative elements on this page.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 314126B model=glm-5.3-flash effort=low transcribe_ms=4714.7 verify_ms=2366.6 ocr_ms=22905.1 retries=0 verification_score=97 floor=99% hashes=1964c7cade1db971a180794d5a9f107e14ee1f9ac7b029611b05c613e32099ba/649897b2f7db240c132fe92c9c0649ab608ae7a2b7c57e11d3d304a52c920655/7c370e103d63562bc1b82edf8a63e16c7401f64cbe0232f78fbc9a83ee783bdc/eec89b0feda03f545b9d17765b68090ac2c65b7d7fc0eb3fd118d67fe97ca134
- page 2: dpi=200 image=1700x2200 375495B model=glm-5.3-flash effort=low transcribe_ms=4928.2 verify_ms=2375.0 ocr_ms=23141.8 retries=0 verification_score=95 floor=100% hashes=3c648d8a8ad82d73cb3ad8682164e9dd6d1eff4634e3d208ce3528912bb2cdf2/2097b825ff6e6ae62164cb5147145d318ebc4976006ff4c1f75e9a842aa3cd22/88b02b75cb86ca2ff13849bea728c5aa021ea6c39ec8293139908f606ec2f3b7/afb8de71f3c75c4c05e9cbae0d2769de981780707ae1099a22fb71e3311ffaf0
- page 3: dpi=300 image=2550x3300 636398B model=glm-5.3-flash effort=low transcribe_ms=9587.9 verify_ms=5983.8 ocr_ms=45660.4 retries=1 verification_score=100 floor=100% hashes=6d8946229ce606afd2d87696403caf0101d9e89a904d19116b0dd0fe97abe035/0783022a0acb9cab17ce2556ccee1d488bd4e8e5a616ee5f9fd38e0d1b97b63c/f0de9a4c9fba4c44efc930bdea4f0dd0261a0318732513d439e97c1d0bdf8933/50ed7fa5242a76c4a63eab560fe406cc336b7e6230a2cfe90100040824d690e3
- page 4: dpi=400 image=3400x4400 541097B model=glm-5.3-flash effort=low transcribe_ms=15249.4 verify_ms=10227.2 ocr_ms=55420.2 retries=2 verification_score=95 floor=100% hashes=32e24aa9bee2ee11f48a382710253abb427086a93cb7db1ecb5e0af6504dea45/a8691b26e7985e3658b6074648518c0dfc1016a070b0bbb817a2e8f1c1cda56d/6ab9752babea71f9ddb8861e24a90c1189e6a6c69939ed16336c949617842aa2/ec0b4cc9b0b1bf2b7d09f65ea344f3e3798f668402c8a052b192d44994671b43
- page 5: dpi=200 image=1700x2200 340524B model=glm-5.3-flash effort=low transcribe_ms=5753.8 verify_ms=3265.1 ocr_ms=25139.6 retries=0 verification_score=95 floor=100% hashes=44deedf3162db13b3c4bb6e3a72ac287bbda44100286431ad4562a2bce10698b/04e32695178e626fd0f301944013f9806cc08a7cfaa42b0d1d1bdfb74dfea6d2/7bbdaa390b2f3fbc5be92b53b938af997b7883fd2857a0f0e85dd1b51053dc79/72a1b5b5a49334346775573c6cc15c95c5f3bf0f4f8b7b96ff432bccf2ef8546
- page 6: dpi=300 image=2550x3300 581163B model=glm-5.3-flash effort=low transcribe_ms=11528.9 verify_ms=6640.0 ocr_ms=46187.8 retries=1 verification_score=98 floor=100% hashes=8cfd0be1b76af5ca8574a616f35d45b0d001350825be92b20291ad67e28f045e/fc9429a49154d9985bdc4c4a18e757acd69bc579023f38bd6994625e16e21704/4afe8dadbdcca2cc2adb3bd055ab1f564ee4e5238dc107ecf8907e56ebbfbbd8/8aaf7ff1996ca0b8c73b99060a4e6f881dc4856e96a7ba5fe19d49f9176310f0
- page 7: dpi=200 image=1700x2200 370883B model=glm-5.3-flash effort=low transcribe_ms=5154.1 verify_ms=2875.5 ocr_ms=24019.7 retries=0 verification_score=98 floor=100% hashes=a0785837b1858dda78f6e96da32f0e32a949627f5aebe1fec56e1bd021f630b0/698739cc078a2ed4fb950d766b43327b237c7be93c1221028c4f34080c29bc04/4d96ea8f32b087dec64b681b8ce7a0bc1084f0fb7d307217b7de9d3fa3db8734/561a534e4bcb2e5dfc797e01081be5e2194ab9cf0a252934dcb54278e82e36d5
- page 8: dpi=400 image=3400x4400 775947B model=glm-5.3-flash effort=low transcribe_ms=21174.5 verify_ms=11892.1 ocr_ms=103873.1 retries=2 verification_score=96 floor=100% hashes=139af2dfceaa712a4219f2d96163cb24fdeda73a739de7814c5dec1941d53072/06223d25ad5149642b7b0c9036299ca3aca1df20c4b091603bd106113d336da9/2765b8ec85bd4e919b9538cb567ac94cbf1a67ff2c37a9f1338ebeda77e297bf/16a8774998859aad0450fb117c69a6d272e6d810c6ec6da3a3f3b007adf28d86

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:13: [Expected: 80, Actual: 124]
- MD013:18: [Expected: 80, Actual: 1109]
- MD013:24: [Expected: 80, Actual: 884]
- MD034:26:
- MD034:27:
- MD013:29: [Expected: 80, Actual: 138]
- MD013:31: [Expected: 80, Actual: 238]
- MD013:35: [Expected: 80, Actual: 2333]
- MD013:37: [Expected: 80, Actual: 304]
- MD013:38: [Expected: 80, Actual: 138]
- MD013:42: [Expected: 80, Actual: 942]
- MD013:44: [Expected: 80, Actual: 549]
- MD013:46: [Expected: 80, Actual: 616]
- MD034:46:
- MD013:50: [Expected: 80, Actual: 1018]
- MD013:66: [Expected: 80, Actual: 330]
- MD033:68: [Element: details]
- MD036:73:
- MD013:79: [Expected: 80, Actual: 187]
- MD013:81: [Expected: 80, Actual: 337]
- MD013:83: [Expected: 80, Actual: 290]
- MD013:85: [Expected: 80, Actual: 640]
- MD013:89: [Expected: 80, Actual: 98]
- MD013:90: [Expected: 80, Actual: 98]
- MD013:91: [Expected: 80, Actual: 98]
- MD013:92: [Expected: 80, Actual: 98]
- MD013:93: [Expected: 80, Actual: 98]
- MD013:94: [Expected: 80, Actual: 98]
- MD013:95: [Expected: 80, Actual: 98]
- MD013:97: [Expected: 80, Actual: 145]
- MD013:99: [Expected: 80, Actual: 97]
- MD013:100: [Expected: 80, Actual: 97]
- MD013:101: [Expected: 80, Actual: 97]
- MD013:102: [Expected: 80, Actual: 97]
- MD013:103: [Expected: 80, Actual: 97]
- MD013:104: [Expected: 80, Actual: 97]
- MD013:105: [Expected: 80, Actual: 97]
- MD013:106: [Expected: 80, Actual: 97]
- MD013:108: [Expected: 80, Actual: 154]
- MD013:110: [Expected: 80, Actual: 1626]
- MD013:112: [Expected: 80, Actual: 510]
- MD013:121: [Expected: 80, Actual: 120]
- MD029:121: [Expected: 1; Actual: 2; Style: 1/2/3]
- MD013:123: [Expected: 80, Actual: 100]
- MD013:125: [Expected: 80, Actual: 248]
- MD013:127: [Expected: 80, Actual: 1657]
- MD013:131: [Expected: 80, Actual: 312]
- MD013:132: [Expected: 80, Actual: 312]
- MD013:133: [Expected: 80, Actual: 312]
- MD013:134: [Expected: 80, Actual: 312]
- MD013:135: [Expected: 80, Actual: 312]
- MD013:136: [Expected: 80, Actual: 312]
- MD013:137: [Expected: 80, Actual: 312]
- MD013:139: [Expected: 80, Actual: 318]
- MD013:143: [Expected: 80, Actual: 2403]
- MD013:147: [Expected: 80, Actual: 305]
- MD013:149: [Expected: 80, Actual: 545]
- MD013:153: [Expected: 80, Actual: 229]
- MD013:158: [Expected: 80, Actual: 155]
- MD013:159: [Expected: 80, Actual: 220]
- MD013:160: [Expected: 80, Actual: 132]
- MD013:161: [Expected: 80, Actual: 117]
- MD013:162: [Expected: 80, Actual: 195]
- MD013:163: [Expected: 80, Actual: 130]
- MD013:164: [Expected: 80, Actual: 141]
- MD013:165: [Expected: 80, Actual: 119]
- MD013:166: [Expected: 80, Actual: 101]
- MD013:167: [Expected: 80, Actual: 161]
- MD013:168: [Expected: 80, Actual: 151]
- MD013:169: [Expected: 80, Actual: 164]
- MD034:169:
- MD013:170: [Expected: 80, Actual: 226]
- MD013:171: [Expected: 80, Actual: 167]
- MD034:171:
