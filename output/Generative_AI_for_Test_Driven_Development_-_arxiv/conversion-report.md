# Conversion report — Generative AI for Test Driven Development - arxiv.pdf

- job_id: b678c5e8-68ef-4d54-9e63-aa82fca4ee04
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=111538 completion=7340
- pipeline_version: 073654be6c457b411ab24a51dcfff4bdea2968daf6252a3e996dc1f6b48c7d48
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 75

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 98 | 0 | 200 | 12330 | 828 | False |
| 2 | verified | 97 | 0 | 200 | 13158 | 987 | False |
| 3 | verified | 96 | 0 | 200 | 13810 | 958 | False |
| 4 | verified | 96 | 0 | 200 | 13930 | 823 | False |
| 5 | verified | 97 | 0 | 200 | 14564 | 964 | False |
| 6 | verified | 95 | 0 | 200 | 14340 | 872 | False |
| 7 | verified | 96 | 0 | 200 | 14300 | 829 | False |
| 8 | verified | 97 | 0 | 200 | 15106 | 1079 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 1
- converted to Mermaid: 1 (100%)
- data-table fallbacks: 0
- image fallbacks: 0

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 8 | flowchart | mermaid | 90 |

## Omissions log

- page 1: Left-margin rotated arXiv watermark treated as furniture, excluded from body. Superscript footnote markers 1 and 2 rendered as $^1$/$^2$ LaTeX. No figures on page. No typos corrected.
- page 2: Continuation from page 1 (paragraph of Section 1). Page number "2" appears in running header, excluded from body. Inline math placeholders rendered as $\langle ... \rangle$ per OCR. No uncertain characters.
- page 3: The final-iteration bullet is a continuation of the prompt list from page 2. The exercise text was rendered as a block quote (italic in source). Fig. 1 is referenced but appears on a later page; no figure region on this page. No [?] uncertainties; no typo corrections made.
- page 4: Fig. 1 is a workflow diagram (Feature/Test case → Specify prompt → Develop failing test → Develop code → Execute tests → Pass/fail?; Fail → Choose prompt → loop; note boxes: Prompt, Test/Prompt, Error Trace (red)/Code/Test/Prompt). Circled numbers ①–⑤ mark activities. Placeholder token only; graphical details not transcribed. Text continues mid-sentence from page 3 and to page 5. No typo corrections made.
- page 5: Table 2 continues the results table from page 4 context (caption reiterates participants). Code block rendered as monospaced chat output; line wrapping adjusted for block format. No figures on this page. No uncertain characters.
- page 6: - Continuation of the ChatGPT code block from page 5: items 2 and 3 rendered here as a fenced continuation; merged into the previous page's code block when assembling the document.
- No figures on this page.
- No typo corrections made.
- page 7: - No figures on this page.
- Page ends mid-sentence, continuing onto page 8 ("...for our experiment and settings, ...").
- No typo corrections made; text reproduced verbatim from OCR reference.
- page 8: Continuation paragraph from Section 5 Conclusions (page 7); heading levels adjusted to match document outline. No figures on this page.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 314126B model=glm-5.3-flash effort=low transcribe_ms=4691.2 verify_ms=2652.9 ocr_ms=34070.9 retries=0 verification_score=98 floor=99% hashes=1964c7cade1db971a180794d5a9f107e14ee1f9ac7b029611b05c613e32099ba/649897b2f7db240c132fe92c9c0649ab608ae7a2b7c57e11d3d304a52c920655/7c370e103d63562bc1b82edf8a63e16c7401f64cbe0232f78fbc9a83ee783bdc/d9a7df6146e41702a2bbe6fcaaa39cdfac065354341050b1de68fbc7e681a537
- page 2: dpi=200 image=1700x2200 375495B model=glm-5.3-flash effort=low transcribe_ms=4697.9 verify_ms=3106.0 ocr_ms=22038.3 retries=0 verification_score=97 floor=100% hashes=3c648d8a8ad82d73cb3ad8682164e9dd6d1eff4634e3d208ce3528912bb2cdf2/2097b825ff6e6ae62164cb5147145d318ebc4976006ff4c1f75e9a842aa3cd22/88b02b75cb86ca2ff13849bea728c5aa021ea6c39ec8293139908f606ec2f3b7/efcef4af9681eeab9110065ba4d8b68e89600ea0b983a6f9f33bd6525d6fe13f
- page 3: dpi=200 image=1700x2200 377854B model=glm-5.3-flash effort=low transcribe_ms=4965.8 verify_ms=3359.0 ocr_ms=22235.8 retries=0 verification_score=96 floor=100% hashes=6d8946229ce606afd2d87696403caf0101d9e89a904d19116b0dd0fe97abe035/aff78325cb55fa51fec9b9392070b4e6ef96d9d90df8b6ba912b1b8cae5133d9/f0de9a4c9fba4c44efc930bdea4f0dd0261a0318732513d439e97c1d0bdf8933/7bae0591536a645d6b42452eb59baac5eb52c73626cd76f67929207dfaaaa7c7
- page 4: dpi=200 image=1700x2200 271130B model=glm-5.3-flash effort=low transcribe_ms=4460.0 verify_ms=3253.0 ocr_ms=17893.9 retries=0 verification_score=96 floor=100% hashes=32e24aa9bee2ee11f48a382710253abb427086a93cb7db1ecb5e0af6504dea45/e8eba92ee8548bf5889de49b9ab7b0b45a8e0de04008758cb997656f2e848014/6ab9752babea71f9ddb8861e24a90c1189e6a6c69939ed16336c949617842aa2/0b725a8e293c2c5f29348ce2d8edfcfb24aaf500c99e3e374ea38508519a4bb0
- page 5: dpi=200 image=1700x2200 340524B model=glm-5.3-flash effort=low transcribe_ms=4859.9 verify_ms=2803.8 ocr_ms=25179.2 retries=0 verification_score=97 floor=100% hashes=44deedf3162db13b3c4bb6e3a72ac287bbda44100286431ad4562a2bce10698b/04e32695178e626fd0f301944013f9806cc08a7cfaa42b0d1d1bdfb74dfea6d2/7bbdaa390b2f3fbc5be92b53b938af997b7883fd2857a0f0e85dd1b51053dc79/72263f8aea419c47e111023f393190b033025733fd06e9b98e99624c3bf84350
- page 6: dpi=200 image=1700x2200 343544B model=glm-5.3-flash effort=low transcribe_ms=4716.1 verify_ms=2539.9 ocr_ms=22020.6 retries=0 verification_score=95 floor=100% hashes=8cfd0be1b76af5ca8574a616f35d45b0d001350825be92b20291ad67e28f045e/5187b870b93b25e34f6475f857dd9f2e45c1cbe1c234673f06901d6951b78e8c/4afe8dadbdcca2cc2adb3bd055ab1f564ee4e5238dc107ecf8907e56ebbfbbd8/97427bc47d42466b1cde633416de80cb577e7090a9cd3589eb554c5a2258ed64
- page 7: dpi=200 image=1700x2200 370883B model=glm-5.3-flash effort=low transcribe_ms=4559.0 verify_ms=2864.3 ocr_ms=22544.4 retries=0 verification_score=96 floor=100% hashes=a0785837b1858dda78f6e96da32f0e32a949627f5aebe1fec56e1bd021f630b0/698739cc078a2ed4fb950d766b43327b237c7be93c1221028c4f34080c29bc04/4d96ea8f32b087dec64b681b8ce7a0bc1084f0fb7d307217b7de9d3fa3db8734/2a931c5a0a6d01cace4832bfa8de0595a256903d1f4cde955e5088ee44b83fed
- page 8: dpi=200 image=1700x2200 388311B model=glm-5.3-flash effort=low transcribe_ms=5216.8 verify_ms=2734.2 ocr_ms=32463.6 retries=0 verification_score=97 floor=100% hashes=139af2dfceaa712a4219f2d96163cb24fdeda73a739de7814c5dec1941d53072/7bd35a4831ba08e0f631bd9be6e5ec288eef541b8ad48cbb7fcaed3b7088f151/2765b8ec85bd4e919b9538cb567ac94cbf1a67ff2c37a9f1338ebeda77e297bf/16a8774998859aad0450fb117c69a6d272e6d810c6ec6da3a3f3b007adf28d86

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
- MD013:37: [Expected: 80, Actual: 313]
- MD013:38: [Expected: 80, Actual: 138]
- MD013:42: [Expected: 80, Actual: 942]
- MD013:44: [Expected: 80, Actual: 551]
- MD013:46: [Expected: 80, Actual: 616]
- MD034:46:
- MD013:50: [Expected: 80, Actual: 1018]
- MD013:70: [Expected: 80, Actual: 229]
- MD033:72: [Element: details]
- MD036:77:
- MD013:83: [Expected: 80, Actual: 187]
- MD013:85: [Expected: 80, Actual: 337]
- MD013:87: [Expected: 80, Actual: 290]
- MD013:89: [Expected: 80, Actual: 640]
- MD013:93: [Expected: 80, Actual: 98]
- MD013:94: [Expected: 80, Actual: 98]
- MD013:95: [Expected: 80, Actual: 98]
- MD013:96: [Expected: 80, Actual: 98]
- MD013:97: [Expected: 80, Actual: 98]
- MD013:98: [Expected: 80, Actual: 98]
- MD013:99: [Expected: 80, Actual: 98]
- MD013:101: [Expected: 80, Actual: 145]
- MD013:103: [Expected: 80, Actual: 97]
- MD013:104: [Expected: 80, Actual: 97]
- MD013:105: [Expected: 80, Actual: 97]
- MD013:106: [Expected: 80, Actual: 97]
- MD013:107: [Expected: 80, Actual: 97]
- MD013:108: [Expected: 80, Actual: 97]
- MD013:109: [Expected: 80, Actual: 97]
- MD013:110: [Expected: 80, Actual: 97]
- MD013:112: [Expected: 80, Actual: 154]
- MD013:114: [Expected: 80, Actual: 1628]
- MD013:116: [Expected: 80, Actual: 510]
- MD040:118:
- MD013:125: [Expected: 80, Actual: 120]
- MD029:125: [Expected: 1; Actual: 2; Style: 1/2/3]
- MD013:126: [Expected: 80, Actual: 100]
- MD013:128: [Expected: 80, Actual: 248]
- MD013:130: [Expected: 80, Actual: 1657]
- MD013:134: [Expected: 80, Actual: 312]
- MD013:135: [Expected: 80, Actual: 312]
- MD013:136: [Expected: 80, Actual: 312]
- MD013:137: [Expected: 80, Actual: 312]
- MD013:138: [Expected: 80, Actual: 312]
- MD013:139: [Expected: 80, Actual: 312]
- MD013:140: [Expected: 80, Actual: 312]
- MD013:142: [Expected: 80, Actual: 318]
- MD013:146: [Expected: 80, Actual: 2403]
- MD013:150: [Expected: 80, Actual: 305]
- MD013:152: [Expected: 80, Actual: 545]
- MD013:156: [Expected: 80, Actual: 229]
- MD013:161: [Expected: 80, Actual: 155]
- MD013:162: [Expected: 80, Actual: 220]
- MD013:163: [Expected: 80, Actual: 132]
- MD013:164: [Expected: 80, Actual: 117]
- MD013:165: [Expected: 80, Actual: 195]
- MD013:166: [Expected: 80, Actual: 130]
- MD013:167: [Expected: 80, Actual: 141]
- MD013:168: [Expected: 80, Actual: 119]
- MD013:169: [Expected: 80, Actual: 101]
- MD013:170: [Expected: 80, Actual: 161]
- MD013:171: [Expected: 80, Actual: 151]
- MD013:172: [Expected: 80, Actual: 164]
- MD034:172:
- MD013:173: [Expected: 80, Actual: 226]
- MD013:174: [Expected: 80, Actual: 167]
- MD034:174:
