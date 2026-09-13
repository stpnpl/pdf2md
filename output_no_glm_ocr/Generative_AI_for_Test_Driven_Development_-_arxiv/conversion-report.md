# Conversion report — Generative AI for Test Driven Development - arxiv.pdf

- job_id: 3b420f35-abd2-4e02-8d65-ac8cc0e853b4
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=112238 completion=7444
- pipeline_version: 9c215872aa0b575aade8ae9fb73a81b65c9fb7d96e9934b244133c2636e44bc0
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 70

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 98 | 0 | 200 | 12377 | 795 | False |
| 2 | verified | 98 | 0 | 200 | 13247 | 851 | False |
| 3 | verified | 98 | 0 | 200 | 13893 | 925 | False |
| 4 | verified | 95 | 0 | 200 | 14045 | 837 | False |
| 5 | verified | 95 | 0 | 200 | 14505 | 968 | False |
| 6 | verified | 95 | 0 | 200 | 14435 | 1035 | False |
| 7 | verified | 97 | 0 | 200 | 14479 | 930 | False |
| 8 | verified | 98 | 0 | 200 | 15257 | 1103 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 1
- converted to Mermaid: 1 (100%)
- data-table fallbacks: 0
- image fallbacks: 0

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 98 | flowchart | mermaid | 90 |

## Omissions log

- page 1: Footnote markers rendered as superscript characters ¹/²; original used \thanks-style footnotes. No figures on page. No typos corrected.
- page 2: Page continues the Introduction paragraph from page 1. No figures on this page. No typos corrected.
- page 3: Continues Section 2 list of prompts from previous page ("— Final iteration" bullet) and paragraph continues on next page. No figures on this page despite reference to Fig. 1. Circled numbers ① ② rendered as 1○/2○ in source; corrected to ① ②. No other corrections needed.
- page 4: Figure 1 is a workflow diagram with activities 1-5 (Specify prompt, Develop failing test, Develop code, Execute tests, Choose prompt), note boxes (Feature/Test case, Prompt, Test/Prompt, Error Trace/Code/Test/Prompt), a Pass/fail? decision, and Pass/Fail/Repeat branches.
Continuation from page 3: body text begins mid-sentence ("activity ③") completing "the developer can modify the input passed to the AI in activity ③." Page ends mid-sentence ("so we are") continuing on page 5.
"Error Trace" and "Code" text in note boxes of Fig. 1 appear in red in the original.
- page 5: - Page continues from previous page: paragraph starts mid-sentence ("able to log the activities of both.") and Table 2 belongs to the RQ2 discussion started on page 4.
- Code-style ChatGPT recommendation block reproduced as monospace fenced block; the original line breaks within the quoted identifiers were joined for readability.
- No figure regions on this page.
- page 6: - Continuation of a fenced code block ("ChatGPT recommended these changes...") started on the previous page; rendered as a complete fenced block including items 2 and 3 that appear on this page.
- Typo corrections: "textFormatter" quotes normalized; "1-3 years" style tables from prior context not repeated here. No other corrections made.
- No uncertain characters marked.
- page 7: No figures/tables on this page. Section headings "4 Related work" and "5 Conclusions" rendered as ## headings per outline. Text ends mid-sentence, continuing on next page.
- page 8: Page contains the continuation of Section 5 (Conclusions), Acknowledgments, and References. Table 2/Table 3 and earlier body text in the rolling context appear on prior pages, not on this image. No figures on this page. Inconsistent capitalization in references ("chatgpt", "Ai-driven", "ai programming assistants") preserved verbatim. Reference 13 retains doubled "doi.org/doi.org/" as in source.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 314126B model=glm-5.3-flash effort=low transcribe_ms=5251.2 verify_ms=3660.2 ocr_ms=404.7 retries=0 verification_score=98 floor=94% hashes=1964c7cade1db971a180794d5a9f107e14ee1f9ac7b029611b05c613e32099ba/649897b2f7db240c132fe92c9c0649ab608ae7a2b7c57e11d3d304a52c920655/688f57078d8ba5b9524782167cf287a243c58580d3c3a5f0b5dd9d38798e5a06/9f188ea9aa87c03fca46db7b1ecdf541a3197d9c1ffe5f086aa276ec330cac31
- page 2: dpi=200 image=1700x2200 375495B model=glm-5.3-flash effort=low transcribe_ms=5731.4 verify_ms=3355.3 ocr_ms=364.6 retries=0 verification_score=98 floor=97% hashes=3c648d8a8ad82d73cb3ad8682164e9dd6d1eff4634e3d208ce3528912bb2cdf2/2097b825ff6e6ae62164cb5147145d318ebc4976006ff4c1f75e9a842aa3cd22/2bcc31d6bd6e2807a8240f6979f8ad6d00fafcf1396a7d4216d81c387226a632/fe04bad2b7187c5b29167c5b759d1cb7c7a88b3e508f771fe6177c0732b33428
- page 3: dpi=200 image=1700x2200 377854B model=glm-5.3-flash effort=low transcribe_ms=6840.9 verify_ms=3420.2 ocr_ms=365.6 retries=0 verification_score=98 floor=99% hashes=6d8946229ce606afd2d87696403caf0101d9e89a904d19116b0dd0fe97abe035/aff78325cb55fa51fec9b9392070b4e6ef96d9d90df8b6ba912b1b8cae5133d9/198bfe0dcf17096dc90d003535c2d91b7fbd7b7b74a45e9e920bce162a4f28f8/7bae0591536a645d6b42452eb59baac5eb52c73626cd76f67929207dfaaaa7c7
- page 4: dpi=200 image=1700x2200 271130B model=glm-5.3-flash effort=low transcribe_ms=7527.4 verify_ms=2613.3 ocr_ms=756.4 retries=0 verification_score=95 floor=90% hashes=32e24aa9bee2ee11f48a382710253abb427086a93cb7db1ecb5e0af6504dea45/e8eba92ee8548bf5889de49b9ab7b0b45a8e0de04008758cb997656f2e848014/5bc3597a624462d594fe69910a9ca61946fd2c4c3f1f1ed51e177a7de40a82b1/2ff353876042de8fb7ff1f9da0c0ad12d38a930e42576bf37aeb288cfda3f447
- page 5: dpi=200 image=1700x2200 340524B model=glm-5.3-flash effort=low transcribe_ms=9293.2 verify_ms=2978.4 ocr_ms=357.6 retries=0 verification_score=95 floor=99% hashes=44deedf3162db13b3c4bb6e3a72ac287bbda44100286431ad4562a2bce10698b/04e32695178e626fd0f301944013f9806cc08a7cfaa42b0d1d1bdfb74dfea6d2/3c736a84688fc4a3d47bb532f9d06b011e828fcd1a93ee3045fda6eebb06b9c2/5cf1454fdd26457ec031952451e605feff5088c1fcbf46dc28ddd3b340f26075
- page 6: dpi=200 image=1700x2200 343544B model=glm-5.3-flash effort=low transcribe_ms=8761.8 verify_ms=5587.6 ocr_ms=365.4 retries=0 verification_score=95 floor=98% hashes=8cfd0be1b76af5ca8574a616f35d45b0d001350825be92b20291ad67e28f045e/5187b870b93b25e34f6475f857dd9f2e45c1cbe1c234673f06901d6951b78e8c/0319b9bbde5142f0aae776a75e79120d534b36a19c143b16e8c653a6775a51b1/3736e9661286e00104db491eb48df021e425395745989722dbfe9aaa3e595112
- page 7: dpi=200 image=1700x2200 370883B model=glm-5.3-flash effort=low transcribe_ms=9833.1 verify_ms=3529.0 ocr_ms=355.0 retries=0 verification_score=97 floor=99% hashes=a0785837b1858dda78f6e96da32f0e32a949627f5aebe1fec56e1bd021f630b0/698739cc078a2ed4fb950d766b43327b237c7be93c1221028c4f34080c29bc04/b7cbe7efa4db4c4f44679a19665adbf7f3dac47c4fb450d8f03a635c998277d5/d0f7eefe96ab7cb14eaa9802bfb99fb1d568db459bf5fda35986822025b3f956
- page 8: dpi=200 image=1700x2200 388311B model=glm-5.3-flash effort=low transcribe_ms=7152.1 verify_ms=2790.3 ocr_ms=370.2 retries=0 verification_score=98 floor=97% hashes=139af2dfceaa712a4219f2d96163cb24fdeda73a739de7814c5dec1941d53072/7bd35a4831ba08e0f631bd9be6e5ec288eef541b8ad48cbb7fcaed3b7088f151/dfc5e5e711a91494c1b28a54cf1898a89e9c09e489ed944716ad4839a0f150dd/16a8774998859aad0450fb117c69a6d272e6d810c6ec6da3a3f3b007adf28d86

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:13: [Expected: 80, Actual: 142]
- MD033:13: [Element: sup]
- MD033:13: [Element: sup]
- MD033:13: [Element: sup]
- MD013:19: [Expected: 80, Actual: 1109]
- MD013:25: [Expected: 80, Actual: 878]
- MD013:31: [Expected: 80, Actual: 138]
- MD013:33: [Expected: 80, Actual: 238]
- MD013:37: [Expected: 80, Actual: 2333]
- MD013:39: [Expected: 80, Actual: 247]
- MD013:40: [Expected: 80, Actual: 138]
- MD013:44: [Expected: 80, Actual: 942]
- MD013:46: [Expected: 80, Actual: 551]
- MD013:48: [Expected: 80, Actual: 616]
- MD034:48:
- MD013:52: [Expected: 80, Actual: 1018]
- MD013:83: [Expected: 80, Actual: 217]
- MD033:85: [Element: details]
- MD036:90:
- MD013:96: [Expected: 80, Actual: 187]
- MD013:98: [Expected: 80, Actual: 337]
- MD013:100: [Expected: 80, Actual: 290]
- MD013:102: [Expected: 80, Actual: 640]
- MD013:106: [Expected: 80, Actual: 98]
- MD013:107: [Expected: 80, Actual: 98]
- MD013:108: [Expected: 80, Actual: 98]
- MD013:109: [Expected: 80, Actual: 98]
- MD013:110: [Expected: 80, Actual: 98]
- MD013:111: [Expected: 80, Actual: 98]
- MD013:112: [Expected: 80, Actual: 98]
- MD013:114: [Expected: 80, Actual: 145]
- MD013:116: [Expected: 80, Actual: 97]
- MD013:117: [Expected: 80, Actual: 97]
- MD013:118: [Expected: 80, Actual: 97]
- MD013:119: [Expected: 80, Actual: 97]
- MD013:120: [Expected: 80, Actual: 97]
- MD013:121: [Expected: 80, Actual: 97]
- MD013:122: [Expected: 80, Actual: 97]
- MD013:123: [Expected: 80, Actual: 97]
- MD013:125: [Expected: 80, Actual: 154]
- MD013:127: [Expected: 80, Actual: 1628]
- MD013:129: [Expected: 80, Actual: 510]
- MD040:131:
- MD013:146: [Expected: 80, Actual: 248]
- MD013:148: [Expected: 80, Actual: 1657]
- MD013:152: [Expected: 80, Actual: 312]
- MD013:153: [Expected: 80, Actual: 312]
- MD013:154: [Expected: 80, Actual: 312]
- MD013:155: [Expected: 80, Actual: 312]
- MD013:156: [Expected: 80, Actual: 312]
- MD013:157: [Expected: 80, Actual: 312]
- MD013:158: [Expected: 80, Actual: 312]
- MD013:206: [Expected: 80, Actual: 545]
- MD013:210: [Expected: 80, Actual: 229]
- MD013:215: [Expected: 80, Actual: 155]
- MD013:216: [Expected: 80, Actual: 220]
- MD013:217: [Expected: 80, Actual: 132]
- MD013:218: [Expected: 80, Actual: 117]
- MD013:219: [Expected: 80, Actual: 195]
- MD013:220: [Expected: 80, Actual: 130]
- MD013:221: [Expected: 80, Actual: 141]
- MD013:222: [Expected: 80, Actual: 119]
- MD013:223: [Expected: 80, Actual: 101]
- MD013:224: [Expected: 80, Actual: 161]
- MD013:225: [Expected: 80, Actual: 151]
- MD013:226: [Expected: 80, Actual: 164]
- MD034:226:
- MD013:227: [Expected: 80, Actual: 226]
- MD013:228: [Expected: 80, Actual: 167]
- MD034:228:
