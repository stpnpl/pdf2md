# Conversion report — Generative AI for Test Driven Development - arxiv.pdf

- job_id: 9a0199c8-7066-4c0c-8559-1dda7fe7ec40
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=112204 completion=7551
- pipeline_version: 49d37aab5011162c95b2267d3c52c5edb25ebd6d06ffb252038f28d3523593bc
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 71

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 98 | 0 | 200 | 12369 | 846 | False |
| 2 | verified | 98 | 0 | 200 | 13240 | 828 | False |
| 3 | verified | 97 | 0 | 200 | 13885 | 942 | False |
| 4 | verified | 95 | 0 | 200 | 14036 | 877 | False |
| 5 | verified | 97 | 0 | 200 | 14502 | 990 | False |
| 6 | verified | 97 | 0 | 200 | 14430 | 865 | False |
| 7 | verified | 95 | 0 | 200 | 14475 | 1117 | False |
| 8 | verified | 96 | 0 | 200 | 15267 | 1086 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 1
- converted to Mermaid: 1 (100%)
- data-table fallbacks: 0
- image fallbacks: 0

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 23 | flowchart | mermaid | 95 |

## Omissions log

- page 1: No figures on this page. The arXiv stamp on the left margin is a running identifier, excluded from body and listed as furniture. "automatize" kept as in source (not a clear typo). Footnote markers rendered as GFM footnotes.
- page 2: Page continues paragraph from page 1 ("can speed up testing. ..."). No figures on this page. Running header excluded from body. No typo corrections needed.
- page 3: Page continues Section 2 (Methodology) bullet list from page 2 with "– Final iteration: Refactor the code." Fig. 1 referenced in text but the figure itself appears on a later page; no figure region on this page. Circled numbers ① ② reproduced as Unicode characters. No typos corrected. Header and page number excluded from body.
- page 4: Continuation from previous page: the sentence "In the collaborative pattern, the workflow is the same but different in its execution. Firstly, activities ① and ② are executed by the developer. Secondly, the developer can modify the input passed to the AI in activity ③." spans the page break; page 4 begins at "activity ③". Table 1 caption "Demographics of the developers" continues from previous page ("Table 1. Demographics of the developers"). No corrections made. Figure region is estimated; the caption was placed as body text below the placeholder per source layout.
- page 5: - Code block reproduces the ChatGPT output verbatim, including the line-broken quote before 'textFormatter'.
- Table 2 caption corrected from "P1, P2, and P3" (source says P1, P2, and P3 though table includes P4, P5) — kept verbatim.
- No figures on this page.
- page 6: Continuation of the numbered code block from previous page (items 2–3 of ChatGPT's recommended changes); rendered as a fenced code block on prior page context. Page ends mid-sentence "but without replacing", continuing on next page. Header (page number + authors) excluded from body.
- page 7: Page 7 is the continuation of Section 3 (Conclusions section is new heading). The rolling-context content (Fig. 1 caption, Tables 1–3, Sections 3 text) belongs to prior pages and is not re-emitted. Section headings "4 Related work" and "5 Conclusions" promoted to ## per outline. Hyphenation from line breaks (e.g., "program-ming", "gener-ated") joined per standard dehyphenation. No figures on this page. Continuation: Section 5 sentence continues on next page.
- page 8: Conclusions paragraph continues from previous page ("practitioners to evaluate the feasibility..."). No figures, tables, or code blocks on this page. Reference 13 source URL contains duplicated "doi.org/doi.org/" — kept verbatim as in source.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 314126B model=glm-5.3-flash effort=low transcribe_ms=6103.9 verify_ms=3204.9 ocr_ms=372.5 retries=0 verification_score=98 floor=94% hashes=1964c7cade1db971a180794d5a9f107e14ee1f9ac7b029611b05c613e32099ba/649897b2f7db240c132fe92c9c0649ab608ae7a2b7c57e11d3d304a52c920655/688f57078d8ba5b9524782167cf287a243c58580d3c3a5f0b5dd9d38798e5a06/9821abcf5fb2f6983fadc87183475edd24dc93cb0aff3970c67f1e98f8b59166
- page 2: dpi=200 image=1700x2200 375495B model=glm-5.3-flash effort=low transcribe_ms=6476.2 verify_ms=2417.8 ocr_ms=367.2 retries=0 verification_score=98 floor=97% hashes=3c648d8a8ad82d73cb3ad8682164e9dd6d1eff4634e3d208ce3528912bb2cdf2/2097b825ff6e6ae62164cb5147145d318ebc4976006ff4c1f75e9a842aa3cd22/2bcc31d6bd6e2807a8240f6979f8ad6d00fafcf1396a7d4216d81c387226a632/fe04bad2b7187c5b29167c5b759d1cb7c7a88b3e508f771fe6177c0732b33428
- page 3: dpi=200 image=1700x2200 377854B model=glm-5.3-flash effort=low transcribe_ms=6789.8 verify_ms=3427.0 ocr_ms=365.6 retries=0 verification_score=97 floor=99% hashes=6d8946229ce606afd2d87696403caf0101d9e89a904d19116b0dd0fe97abe035/aff78325cb55fa51fec9b9392070b4e6ef96d9d90df8b6ba912b1b8cae5133d9/198bfe0dcf17096dc90d003535c2d91b7fbd7b7b74a45e9e920bce162a4f28f8/50ed7fa5242a76c4a63eab560fe406cc336b7e6230a2cfe90100040824d690e3
- page 4: dpi=200 image=1700x2200 271130B model=glm-5.3-flash effort=low transcribe_ms=6108.2 verify_ms=2930.3 ocr_ms=732.7 retries=0 verification_score=95 floor=90% hashes=32e24aa9bee2ee11f48a382710253abb427086a93cb7db1ecb5e0af6504dea45/e8eba92ee8548bf5889de49b9ab7b0b45a8e0de04008758cb997656f2e848014/5bc3597a624462d594fe69910a9ca61946fd2c4c3f1f1ed51e177a7de40a82b1/e412f24ad4cb812908f502e16aae33345438d57c6e338dbc5c1da4ee7b2af33b
- page 5: dpi=200 image=1700x2200 340524B model=glm-5.3-flash effort=low transcribe_ms=6450.3 verify_ms=2657.2 ocr_ms=396.5 retries=0 verification_score=97 floor=99% hashes=44deedf3162db13b3c4bb6e3a72ac287bbda44100286431ad4562a2bce10698b/04e32695178e626fd0f301944013f9806cc08a7cfaa42b0d1d1bdfb74dfea6d2/3c736a84688fc4a3d47bb532f9d06b011e828fcd1a93ee3045fda6eebb06b9c2/a1160bd5c502a196d3e9cb95d3e26a7d89e172610e642c6ae3d06d5ad59f1da0
- page 6: dpi=200 image=1700x2200 343544B model=glm-5.3-flash effort=low transcribe_ms=5695.2 verify_ms=3002.7 ocr_ms=402.5 retries=0 verification_score=97 floor=98% hashes=8cfd0be1b76af5ca8574a616f35d45b0d001350825be92b20291ad67e28f045e/5187b870b93b25e34f6475f857dd9f2e45c1cbe1c234673f06901d6951b78e8c/0319b9bbde5142f0aae776a75e79120d534b36a19c143b16e8c653a6775a51b1/8f4997d209b8dfd417ff58960c4e435c77d4e25a0c938095eb7d92f7cc5ee5b8
- page 7: dpi=200 image=1700x2200 370883B model=glm-5.3-flash effort=low transcribe_ms=6144.9 verify_ms=3737.8 ocr_ms=303.6 retries=0 verification_score=95 floor=99% hashes=a0785837b1858dda78f6e96da32f0e32a949627f5aebe1fec56e1bd021f630b0/698739cc078a2ed4fb950d766b43327b237c7be93c1221028c4f34080c29bc04/b7cbe7efa4db4c4f44679a19665adbf7f3dac47c4fb450d8f03a635c998277d5/d0f7eefe96ab7cb14eaa9802bfb99fb1d568db459bf5fda35986822025b3f956
- page 8: dpi=200 image=1700x2200 388311B model=glm-5.3-flash effort=low transcribe_ms=7606.8 verify_ms=3542.2 ocr_ms=115.3 retries=0 verification_score=96 floor=97% hashes=139af2dfceaa712a4219f2d96163cb24fdeda73a739de7814c5dec1941d53072/7bd35a4831ba08e0f631bd9be6e5ec288eef541b8ad48cbb7fcaed3b7088f151/dfc5e5e711a91494c1b28a54cf1898a89e9c09e489ed944716ad4839a0f150dd/028192546d2b3efc3a9fabe61780aa9cea6a4922e32236d5d09d9b86eb2b8720

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:13: [Expected: 80, Actual: 109]
- MD013:18: [Expected: 80, Actual: 1109]
- MD013:24: [Expected: 80, Actual: 884]
- MD013:26: [Expected: 80, Actual: 138]
- MD013:28: [Expected: 80, Actual: 238]
- MD013:32: [Expected: 80, Actual: 2333]
- MD013:34: [Expected: 80, Actual: 247]
- MD013:35: [Expected: 80, Actual: 138]
- MD013:39: [Expected: 80, Actual: 942]
- MD013:41: [Expected: 80, Actual: 549]
- MD013:43: [Expected: 80, Actual: 616]
- MD034:43:
- MD013:47: [Expected: 80, Actual: 1018]
- MD013:76: [Expected: 80, Actual: 184]
- MD033:78: [Element: details]
- MD013:81: [Expected: 80, Actual: 156]
- MD036:83:
- MD033:85: [Element: details]
- MD013:88: [Expected: 80, Actual: 195]
- MD013:95: [Expected: 80, Actual: 187]
- MD013:97: [Expected: 80, Actual: 337]
- MD013:99: [Expected: 80, Actual: 290]
- MD013:101: [Expected: 80, Actual: 640]
- MD013:105: [Expected: 80, Actual: 98]
- MD013:106: [Expected: 80, Actual: 98]
- MD013:107: [Expected: 80, Actual: 98]
- MD013:108: [Expected: 80, Actual: 98]
- MD013:109: [Expected: 80, Actual: 98]
- MD013:110: [Expected: 80, Actual: 98]
- MD013:111: [Expected: 80, Actual: 98]
- MD013:113: [Expected: 80, Actual: 145]
- MD013:115: [Expected: 80, Actual: 97]
- MD013:116: [Expected: 80, Actual: 97]
- MD013:117: [Expected: 80, Actual: 97]
- MD013:118: [Expected: 80, Actual: 97]
- MD013:119: [Expected: 80, Actual: 97]
- MD013:120: [Expected: 80, Actual: 97]
- MD013:121: [Expected: 80, Actual: 97]
- MD013:122: [Expected: 80, Actual: 97]
- MD013:124: [Expected: 80, Actual: 154]
- MD013:126: [Expected: 80, Actual: 1628]
- MD013:128: [Expected: 80, Actual: 510]
- MD040:130:
- MD013:137: [Expected: 80, Actual: 120]
- MD029:137: [Expected: 1; Actual: 2; Style: 1/2/3]
- MD013:138: [Expected: 80, Actual: 100]
- MD013:140: [Expected: 80, Actual: 248]
- MD013:142: [Expected: 80, Actual: 1657]
- MD013:146: [Expected: 80, Actual: 318]
- MD013:147: [Expected: 80, Actual: 318]
- MD013:148: [Expected: 80, Actual: 318]
- MD013:149: [Expected: 80, Actual: 318]
- MD013:150: [Expected: 80, Actual: 318]
- MD013:151: [Expected: 80, Actual: 318]
- MD013:152: [Expected: 80, Actual: 318]
- MD013:217: [Expected: 80, Actual: 155]
- MD013:218: [Expected: 80, Actual: 220]
- MD013:219: [Expected: 80, Actual: 132]
- MD013:220: [Expected: 80, Actual: 117]
- MD013:221: [Expected: 80, Actual: 195]
- MD013:222: [Expected: 80, Actual: 130]
- MD013:223: [Expected: 80, Actual: 141]
- MD013:224: [Expected: 80, Actual: 119]
- MD013:225: [Expected: 80, Actual: 101]
- MD013:226: [Expected: 80, Actual: 161]
- MD013:227: [Expected: 80, Actual: 151]
- MD013:228: [Expected: 80, Actual: 164]
- MD034:228:
- MD013:229: [Expected: 80, Actual: 226]
- MD013:230: [Expected: 80, Actual: 167]
- MD034:230:
