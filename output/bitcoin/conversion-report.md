# Conversion report — bitcoin.pdf

- job_id: da24d333-ccc1-4a70-9784-cac0ec015114
- status: assembling
- pages: 9
- wall-clock: not started
- tokens: prompt=123494 completion=7041
- pipeline_version: e0804123b115bceb6fe27a3fb5bbe5cb5c3757a3a32381593bed7112ec02ec58
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 72

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 99 | 0 | 200 | 12878 | 748 | False |
| 2 | verified | 98 | 0 | 200 | 13146 | 755 | False |
| 3 | verified | 100 | 0 | 200 | 13515 | 817 | False |
| 4 | verified | 98 | 0 | 200 | 13873 | 960 | False |
| 5 | verified | 97 | 0 | 200 | 14293 | 708 | False |
| 6 | verified | 97 | 0 | 200 | 13921 | 967 | False |
| 7 | verified | 98 | 0 | 200 | 14034 | 840 | False |
| 8 | verified | 98 | 0 | 200 | 14312 | 785 | False |
| 9 | verified | 100 | 0 | 200 | 13522 | 461 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 7
- converted to Mermaid: 5 (71%)
- data-table fallbacks: 0
- image fallbacks: 2

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 2 | 120 | flowchart | image | 88 |
| 2 | 121 | flowchart | mermaid | 95 |
| 3 | 122 | flowchart | mermaid | 95 |
| 4 | 123 | flowchart | mermaid | 95 |
| 5 | 124 | flowchart | mermaid | 90 |
| 5 | 125 | flowchart | mermaid | 88 |
| 6 | 126 | flowchart | image | 90 |

## Omissions log

- page 1: First page of document; no figures. OCR reference duplicated the Introduction text; transcribed only once as it appears once on the page image. Page number "1" excluded from body per rules.
- page 2: No typo corrections made. Page number "2" at bottom excluded from body. Figure bboxes are estimated from layout; no [?] uncertain characters.
- page 3: No text corrections needed; OCR matched source. Numbered list converted from "1)" style to GFM ordered list. Figure bbox estimated from rendered page.
- page 4: - Continuing Section 5 (Network) paragraph from previous page at top of body.
- OCR source reads "a constant of amount of new coins"; kept verbatim (source typo, per DEC-009 allowance; rolling context normalized it, original retained here). Logged, not corrected.
- Figure bbox estimates cover both Merkle tree diagrams and their captions.
- page 5: No typo corrections needed. Figure regions estimated from layout; no uncertain characters. Running page number "5" excluded from body.
- page 6: - Page begins section 10 (Privacy); headings numbered per source.
- Math definitions and piecewise equation rendered as LaTeX, matching source layout.
- No typo corrections needed; no uncertain characters.
- page 7: Continuation of Section 11 (Calculations) from page 6; body text ends mid-section, code block complete. No figures on this page. Math typeset in LaTeX to match source formulas; italic "if" in piecewise cases rendered with \textit as in source.
- page 8: Result tables and the P < 0.001 table rendered as fenced code blocks to preserve monospaced alignment. Continuation of Section 11 (Calculations) from previous page; Section 12 heading starts on this page.
- page 9: No figures on this page. No corrections required.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 336238B model=glm-5.3-flash effort=low transcribe_ms=5997.1 verify_ms=2997.7 ocr_ms=38143.9 retries=0 verification_score=99 floor=100% hashes=d6e2f38823c869115faac4f01ab7dea1d398a0e83fd8453ac2d9aa9f7fbb7bd5/8e1a0c8d3947469c7bec09ffa1d18caf80d52cdfca164bd9627b10c4c51f54a3/c2b40556312eaf64d33a8992032f61b80d73e3f6d034f9e83a7cd8007ce0dd2c/a8ab02851b92c00ad722b2830978dc5d6b9def13ce54d4a344bd84c3de15cb64
- page 2: dpi=200 image=1700x2200 284373B model=glm-5.3-flash effort=low transcribe_ms=6565.7 verify_ms=3151.9 ocr_ms=25623.7 retries=0 verification_score=98 floor=100% hashes=f9948c67dd4011aebc6d452e3bdf683fa2697c17f41612143f7f1784db4e97ee/48be9cc639d62eee69acb2e0fbcfd7e028367fc95c8e0bc425c98e1c9c1e769f/4b899146d4de306b7574990cfdcc51a1b9d29f19aabb159ec4d438d7c83c85b0/baed02affdbb95123f53f42de62d07ab567a69bcbe100a9cac32efb51ae84133
- page 3: dpi=200 image=1700x2200 353335B model=glm-5.3-flash effort=low transcribe_ms=6884.8 verify_ms=3175.6 ocr_ms=21931.0 retries=0 verification_score=100 floor=100% hashes=64134eaee44d2964aa5c52def2708d287e1764395ab39b37194d358ceb875eaa/1096044ea6a81876dc6d57fc3698a37cfa68ef4ae343d3c9dcea6c4ad3a069c8/3a6860d239cc8499b7ac7a5e2b251b65a5798abb3a2bf6ea5481df8b021fc215/e5562b6fd246a56ae9673336b0ca1281eca8aefa6e9be65c16718bb9f531a5a7
- page 4: dpi=200 image=1700x2200 327622B model=glm-5.3-flash effort=low transcribe_ms=7705.5 verify_ms=3264.5 ocr_ms=19207.4 retries=0 verification_score=98 floor=100% hashes=0daecae88b85d3ad7f07a7131e17f6d2ac1ccad790939fc265315689cf987113/a9a27b534a89a68a48b894f112c1ef13021d63d4f6db4c37059d09e1e63c4784/65a8862037a421ebd120cbb9571370eb8d5efc056c0633708dc8047bcfc0cf3c/b5b7b0ff31c12613b8d457453b376783110e45fb627e64b9b670c6f01f406656
- page 5: dpi=200 image=1700x2200 276070B model=glm-5.3-flash effort=low transcribe_ms=4358.1 verify_ms=2512.5 ocr_ms=26517.3 retries=0 verification_score=97 floor=100% hashes=a908726d2917ae3575783217d25d4f8f2473c24cd0b4c52f4fca8271084ba1d6/0dd85db1997be6ad65e391b7b3c359a3c1ffde7f61f463cc76cb73d37ccb8f8e/009d1eef2783085a998e73888f3d7017de1d1c9ace7f753226bd89413ac1aa79/c52cab8df0ef9d4207360fe4b876e0ac67e3a5770857defba99330775b1e54dc
- page 6: dpi=200 image=1700x2200 304207B model=glm-5.3-flash effort=low transcribe_ms=4424.3 verify_ms=3780.3 ocr_ms=19646.8 retries=0 verification_score=97 floor=100% hashes=176d0b231f889a838467a690c661536b3f7c68986ed117a1f5272e39d5efded8/115700d6733d38e34435d533d1496906654556ddb622197221d39dcebb12d416/13d7ee96a0b79c5bc1747d3622ea73daaf637b02f579355f348c0ecde914979d/7b4c59e9b98575158d48c0ac3c58ade5284377d7baa3f7d7710064b6f0799444
- page 7: dpi=200 image=1700x2200 259411B model=glm-5.3-flash effort=low transcribe_ms=4716.2 verify_ms=2794.2 ocr_ms=20720.6 retries=0 verification_score=98 floor=99% hashes=78205fb552a99f2a9c17a59576c503b2d63af63f98e7853eb399b4d8c450689c/0b289e586b9bb0c7121faa95ed010cb2cf67ad91b642ca865232225ecefbd160/bae736eff6877910d52391b21168fe3b4113363876e013b311a3537fe8f6303e/ecfc9ee81eb7a9687d86a135509654faf8b597eb087a124b24583139fa159f5b
- page 8: dpi=200 image=1700x2200 215528B model=glm-5.3-flash effort=low transcribe_ms=4508.4 verify_ms=1959.7 ocr_ms=26881.7 retries=0 verification_score=98 floor=89% hashes=17110863cb1558037f3dd2c179eed093f5711e47ac95240cdf70955a0c354dfb/41aae7856b28dba5cbcf9aa73495f95a062d991f48d7e2bd2ee52e3a491c2f38/081a5340df5e42a88595607215c647af7ece2741c597dc392f222f58c61f1516/139171cbc548825d82a77705bfb5c0da0d47e7521a73905c2ef0642d8ea29c7d
- page 9: dpi=200 image=1700x2200 155714B model=glm-5.3-flash effort=low transcribe_ms=3523.6 verify_ms=2504.7 ocr_ms=15392.5 retries=0 verification_score=100 floor=99% hashes=7b09e8df46f536b0f860a0c3c4e882660b499598f3374f6ce5815a81a175dc5d/382bbb0cf72bfa12e9f1b234f5fa4f087a4c591399fd401ee14cb6fe7e580ffc/43cd8833b5c490235bf58d852d8e3b2773833b23c4659925a81a54ddd178d77d/4ac7cdac4f6fec96e75708643ffc057baee98a0602b61704db1bc05a84f9569d

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:23: [Expected: 80, Actual: 1134]
- MD013:27: [Expected: 80, Actual: 1098]
- MD013:29: [Expected: 80, Actual: 700]
- MD013:33: [Expected: 80, Actual: 306]
- MD013:35: [Expected: 80, Actual: 153]
- MD013:37: [Expected: 80, Actual: 572]
- MD013:39: [Expected: 80, Actual: 721]
- MD013:43: [Expected: 80, Actual: 460]
- MD013:64: [Expected: 80, Actual: 188]
- MD033:66: [Element: details]
- MD013:69: [Expected: 80, Actual: 124]
- MD013:75: [Expected: 80, Actual: 444]
- MD013:77: [Expected: 80, Actual: 413]
- MD013:100: [Expected: 80, Actual: 172]
- MD033:102: [Element: details]
- MD013:109: [Expected: 80, Actual: 816]
- MD013:111: [Expected: 80, Actual: 260]
- MD013:121: [Expected: 80, Actual: 89]
- MD013:122: [Expected: 80, Actual: 157]
- MD013:124: [Expected: 80, Actual: 507]
- MD013:126: [Expected: 80, Actual: 315]
- MD013:130: [Expected: 80, Actual: 500]
- MD013:132: [Expected: 80, Actual: 391]
- MD013:134: [Expected: 80, Actual: 461]
- MD013:138: [Expected: 80, Actual: 410]
- MD013:199: [Expected: 80, Actual: 238]
- MD033:201: [Element: details]
- MD013:204: [Expected: 80, Actual: 156]
- MD036:206:
- MD033:208: [Element: details]
- MD013:211: [Expected: 80, Actual: 366]
- MD013:216: [Expected: 80, Actual: 366]
- MD037:216:
- MD037:216:
- MD013:220: [Expected: 80, Actual: 543]
- MD013:259: [Expected: 80, Actual: 230]
- MD033:261: [Element: details]
- MD013:264: [Expected: 80, Actual: 156]
- MD036:266:
- MD033:268: [Element: details]
- MD013:271: [Expected: 80, Actual: 222]
- MD013:276: [Expected: 80, Actual: 730]
- MD013:280: [Expected: 80, Actual: 462]
- MD013:299: [Expected: 80, Actual: 216]
- MD033:301: [Element: details]
- MD013:308: [Expected: 80, Actual: 242]
- MD013:312: [Expected: 80, Actual: 661]
- MD013:314: [Expected: 80, Actual: 156]
- MD033:316: [Element: details]
- MD013:319: [Expected: 80, Actual: 179]
- MD013:323: [Expected: 80, Actual: 390]
- MD013:327: [Expected: 80, Actual: 511]
- MD013:329: [Expected: 80, Actual: 296]
- MD013:331: [Expected: 80, Actual: 380]
- MD013:335: [Expected: 80, Actual: 90]
- MD013:342: [Expected: 80, Actual: 282]
- MD013:344: [Expected: 80, Actual: 405]
- MD013:346: [Expected: 80, Actual: 447]
- MD013:348: [Expected: 80, Actual: 336]
- MD013:352: [Expected: 80, Actual: 194]
- MD013:354: [Expected: 80, Actual: 153]
- MD040:383:
- MD040:413:
- MD013:427: [Expected: 80, Actual: 1113]
- MD034:431:
- MD013:433: [Expected: 80, Actual: 192]
- MD013:435: [Expected: 80, Actual: 130]
- MD013:437: [Expected: 80, Actual: 205]
- MD013:439: [Expected: 80, Actual: 170]
- MD013:441: [Expected: 80, Actual: 113]
- MD034:441:
- MD013:443: [Expected: 80, Actual: 159]
