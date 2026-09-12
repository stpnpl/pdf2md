# Conversion report — bitcoin.pdf

- job_id: b9b47ac2-e05f-4aba-836e-a01e3a0252d5
- status: assembling
- pages: 9
- wall-clock: not started
- tokens: prompt=123555 completion=6999
- pipeline_version: 073654be6c457b411ab24a51dcfff4bdea2968daf6252a3e996dc1f6b48c7d48
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 69

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 98 | 0 | 200 | 12878 | 749 | False |
| 2 | verified | 98 | 0 | 200 | 13149 | 803 | False |
| 3 | verified | 99 | 0 | 200 | 13516 | 820 | False |
| 4 | verified | 98 | 0 | 200 | 13873 | 895 | False |
| 5 | verified | 97 | 0 | 200 | 14293 | 720 | False |
| 6 | verified | 98 | 0 | 200 | 13902 | 786 | False |
| 7 | verified | 98 | 0 | 200 | 14014 | 754 | False |
| 8 | verified | 98 | 0 | 200 | 14364 | 958 | False |
| 9 | verified | 97 | 0 | 200 | 13566 | 514 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 7
- converted to Mermaid: 4 (57%)
- data-table fallbacks: 0
- image fallbacks: 3

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 2 | 75 | flowchart | mermaid | 88 |
| 2 | 76 | flowchart | mermaid | 85 |
| 3 | 77 | flowchart | mermaid | 95 |
| 4 | 78 | flowchart | mermaid | 95 |
| 5 | 79 | flowchart | image | 85 |
| 5 | 80 | flowchart | image | 85 |
| 6 | 81 | flowchart | image | 85 |

## Omissions log

- page 1: The OCR reference duplicated the "1. Introduction" section; the page image contains it only once, so it is transcribed once. No figures on this page. No text corrections were needed.
- page 2: No typo corrections needed. Figures are line diagrams (transaction ownership chain; timestamp server block chain) rendered as placeholders. Page number "2" excluded from body.
- page 3: No typo corrections needed. Block diagram (Block / Prev Hash / Nonce / Tx ... chain) rendered as figure placeholder.
- page 4: Source contains typo "a constant of amount of new coins" — kept verbatim per OCR ground truth (could be corrected to "a constant amount of new coins"). Figures on this page rendered as single combined figure (two side-by-side diagrams with captions). Page number 4 excluded from body.
- page 5: No text corrections needed. Figure regions approximate the diagram bounds; page number 5 excluded from body.
- page 6: Privacy diagram region transcribed as a single figure placeholder covering both Traditional Privacy Model and New Privacy Model rows. Math block rendered from OCR as LaTeX cases. No typo corrections needed.
- page 7: Continuation of Section 11 (Calculations) from page 6. No figures on this page. No corrections needed.
- page 8: Continuation of section 11 (Calculations) from page 7: the result listings and "Solving for P less than 0.1%..." block belong to that section. Result listings are monospaced in source; rendered as LaTeX arrays per OCR reference. "12. Conclusion" transcribed as a GFM heading (## 12. Conclusion) consistent with document outline. No figures on this page. Page number 8 excluded from body.
- page 9: Final page of document; only the References section appears. References rendered as an ordered list. Page number "9" at footer excluded from body. No figures on this page.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 336238B model=glm-5.3-flash effort=low transcribe_ms=4250.0 verify_ms=2849.9 ocr_ms=36157.6 retries=0 verification_score=98 floor=100% hashes=d6e2f38823c869115faac4f01ab7dea1d398a0e83fd8453ac2d9aa9f7fbb7bd5/8e1a0c8d3947469c7bec09ffa1d18caf80d52cdfca164bd9627b10c4c51f54a3/c2b40556312eaf64d33a8992032f61b80d73e3f6d034f9e83a7cd8007ce0dd2c/a8ab02851b92c00ad722b2830978dc5d6b9def13ce54d4a344bd84c3de15cb64
- page 2: dpi=200 image=1700x2200 284373B model=glm-5.3-flash effort=low transcribe_ms=4284.3 verify_ms=2649.6 ocr_ms=25425.2 retries=0 verification_score=98 floor=100% hashes=f9948c67dd4011aebc6d452e3bdf683fa2697c17f41612143f7f1784db4e97ee/48be9cc639d62eee69acb2e0fbcfd7e028367fc95c8e0bc425c98e1c9c1e769f/4b899146d4de306b7574990cfdcc51a1b9d29f19aabb159ec4d438d7c83c85b0/5d7e03ab34a91a5d2db94be4c87d14150eb6356a4150396bb621a40b93db4756
- page 3: dpi=200 image=1700x2200 353335B model=glm-5.3-flash effort=low transcribe_ms=5503.6 verify_ms=2278.4 ocr_ms=22229.3 retries=0 verification_score=99 floor=100% hashes=64134eaee44d2964aa5c52def2708d287e1764395ab39b37194d358ceb875eaa/1096044ea6a81876dc6d57fc3698a37cfa68ef4ae343d3c9dcea6c4ad3a069c8/3a6860d239cc8499b7ac7a5e2b251b65a5798abb3a2bf6ea5481df8b021fc215/f6747231640f28246875225d4131e16d6fd659b0d16b675ddcab90f8a4ffd692
- page 4: dpi=200 image=1700x2200 327622B model=glm-5.3-flash effort=low transcribe_ms=6649.1 verify_ms=2887.3 ocr_ms=19503.6 retries=0 verification_score=98 floor=100% hashes=0daecae88b85d3ad7f07a7131e17f6d2ac1ccad790939fc265315689cf987113/a9a27b534a89a68a48b894f112c1ef13021d63d4f6db4c37059d09e1e63c4784/65a8862037a421ebd120cbb9571370eb8d5efc056c0633708dc8047bcfc0cf3c/e529ce98a88d557656965fdb1e954afd48dad71e1e651e9102e5a1db7e0ef5fd
- page 5: dpi=200 image=1700x2200 276070B model=glm-5.3-flash effort=low transcribe_ms=4483.4 verify_ms=2956.9 ocr_ms=27113.2 retries=0 verification_score=97 floor=100% hashes=a908726d2917ae3575783217d25d4f8f2473c24cd0b4c52f4fca8271084ba1d6/0dd85db1997be6ad65e391b7b3c359a3c1ffde7f61f463cc76cb73d37ccb8f8e/009d1eef2783085a998e73888f3d7017de1d1c9ace7f753226bd89413ac1aa79/431e8b397c29b8df3051a6ad60c81a3aa3d4671fa3476d24531eb2cd33120845
- page 6: dpi=200 image=1700x2200 304207B model=glm-5.3-flash effort=low transcribe_ms=4701.2 verify_ms=2438.1 ocr_ms=19644.5 retries=0 verification_score=98 floor=100% hashes=176d0b231f889a838467a690c661536b3f7c68986ed117a1f5272e39d5efded8/115700d6733d38e34435d533d1496906654556ddb622197221d39dcebb12d416/13d7ee96a0b79c5bc1747d3622ea73daaf637b02f579355f348c0ecde914979d/f704b7e0dff4041cf94c735cda2da52c410e2d8ed5e529618b20b7561d60d7ad
- page 7: dpi=200 image=1700x2200 259411B model=glm-5.3-flash effort=low transcribe_ms=4830.5 verify_ms=2890.5 ocr_ms=21388.6 retries=0 verification_score=98 floor=100% hashes=78205fb552a99f2a9c17a59576c503b2d63af63f98e7853eb399b4d8c450689c/0b289e586b9bb0c7121faa95ed010cb2cf67ad91b642ca865232225ecefbd160/bae736eff6877910d52391b21168fe3b4113363876e013b311a3537fe8f6303e/b842fcfb42120c9073e8c9cca9e36a61c2c37e7029b9936276376a7bf80a8650
- page 8: dpi=200 image=1700x2200 215528B model=glm-5.3-flash effort=low transcribe_ms=4915.5 verify_ms=2516.6 ocr_ms=27049.1 retries=0 verification_score=98 floor=100% hashes=17110863cb1558037f3dd2c179eed093f5711e47ac95240cdf70955a0c354dfb/41aae7856b28dba5cbcf9aa73495f95a062d991f48d7e2bd2ee52e3a491c2f38/081a5340df5e42a88595607215c647af7ece2741c597dc392f222f58c61f1516/38e5dfb329fe4191d997f1757a211f4f3b3177b954d17b4e3aa49e8524608455
- page 9: dpi=200 image=1700x2200 155714B model=glm-5.3-flash effort=low transcribe_ms=3004.8 verify_ms=2540.8 ocr_ms=16245.3 retries=0 verification_score=97 floor=99% hashes=7b09e8df46f536b0f860a0c3c4e882660b499598f3374f6ce5815a81a175dc5d/382bbb0cf72bfa12e9f1b234f5fa4f087a4c591399fd401ee14cb6fe7e580ffc/43cd8833b5c490235bf58d852d8e3b2773833b23c4659925a81a54ddd178d77d/6fd97ddb96e1713cb8a0c1a2d5b77176baa1c32e78e713241244c57db34e847a

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:23: [Expected: 80, Actual: 1134]
- MD013:27: [Expected: 80, Actual: 1098]
- MD013:29: [Expected: 80, Actual: 700]
- MD013:33: [Expected: 80, Actual: 306]
- MD013:61: [Expected: 80, Actual: 217]
- MD033:63: [Element: details]
- MD013:68: [Expected: 80, Actual: 100]
- MD036:68:
- MD013:72: [Expected: 80, Actual: 572]
- MD013:74: [Expected: 80, Actual: 721]
- MD013:78: [Expected: 80, Actual: 460]
- MD013:89: [Expected: 80, Actual: 161]
- MD033:91: [Element: details]
- MD036:96:
- MD013:102: [Expected: 80, Actual: 444]
- MD013:104: [Expected: 80, Actual: 413]
- MD013:122: [Expected: 80, Actual: 146]
- MD033:124: [Element: details]
- MD013:131: [Expected: 80, Actual: 816]
- MD013:133: [Expected: 80, Actual: 260]
- MD013:143: [Expected: 80, Actual: 89]
- MD013:144: [Expected: 80, Actual: 157]
- MD013:146: [Expected: 80, Actual: 507]
- MD013:148: [Expected: 80, Actual: 315]
- MD013:152: [Expected: 80, Actual: 500]
- MD013:154: [Expected: 80, Actual: 391]
- MD013:156: [Expected: 80, Actual: 461]
- MD013:160: [Expected: 80, Actual: 410]
- MD013:211: [Expected: 80, Actual: 233]
- MD033:213: [Element: details]
- MD013:216: [Expected: 80, Actual: 117]
- MD036:218:
- MD013:222: [Expected: 80, Actual: 366]
- MD037:222:
- MD037:222:
- MD013:226: [Expected: 80, Actual: 543]
- MD013:228: [Expected: 80, Actual: 155]
- MD036:230:
- MD033:232: [Element: details]
- MD013:235: [Expected: 80, Actual: 164]
- MD013:239: [Expected: 80, Actual: 730]
- MD013:243: [Expected: 80, Actual: 462]
- MD036:247:
- MD013:249: [Expected: 80, Actual: 242]
- MD013:253: [Expected: 80, Actual: 661]
- MD013:255: [Expected: 80, Actual: 156]
- MD036:257:
- MD033:259: [Element: details]
- MD013:262: [Expected: 80, Actual: 144]
- MD013:266: [Expected: 80, Actual: 390]
- MD013:270: [Expected: 80, Actual: 511]
- MD013:272: [Expected: 80, Actual: 296]
- MD013:274: [Expected: 80, Actual: 380]
- MD013:282: [Expected: 80, Actual: 282]
- MD013:284: [Expected: 80, Actual: 405]
- MD013:286: [Expected: 80, Actual: 447]
- MD013:288: [Expected: 80, Actual: 336]
- MD013:292: [Expected: 80, Actual: 194]
- MD013:294: [Expected: 80, Actual: 149]
- MD013:370: [Expected: 80, Actual: 1113]
- MD025:372:
- MD034:374:
- MD013:375: [Expected: 80, Actual: 191]
- MD013:376: [Expected: 80, Actual: 129]
- MD013:377: [Expected: 80, Actual: 204]
- MD013:378: [Expected: 80, Actual: 169]
- MD013:379: [Expected: 80, Actual: 112]
- MD034:379:
- MD013:380: [Expected: 80, Actual: 158]
