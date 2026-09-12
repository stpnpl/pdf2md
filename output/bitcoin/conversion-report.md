# Conversion report — bitcoin.pdf

- job_id: 00a07c9a-b434-454c-a9cc-acb5b14c9b78
- status: assembling
- pages: 9
- wall-clock: not started
- tokens: prompt=123650 completion=7031
- pipeline_version: 073654be6c457b411ab24a51dcfff4bdea2968daf6252a3e996dc1f6b48c7d48
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 72

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 100 | 0 | 200 | 12878 | 684 | False |
| 2 | verified | 98 | 0 | 200 | 13148 | 782 | False |
| 3 | verified | 100 | 0 | 200 | 13518 | 805 | False |
| 4 | verified | 96 | 0 | 200 | 13876 | 944 | False |
| 5 | verified | 100 | 0 | 200 | 14297 | 733 | False |
| 6 | verified | 98 | 0 | 200 | 13925 | 842 | False |
| 7 | verified | 99 | 0 | 200 | 14035 | 835 | False |
| 8 | verified | 98 | 0 | 200 | 14382 | 922 | False |
| 9 | verified | 100 | 0 | 200 | 13591 | 484 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 7
- converted to Mermaid: 4 (57%)
- data-table fallbacks: 0
- image fallbacks: 3

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 2 | 41 | flowchart | image | 90 |
| 2 | 42 | flowchart | mermaid | 95 |
| 3 | 43 | flowchart | mermaid | 95 |
| 4 | 44 | flowchart | mermaid | 92 |
| 5 | 45 | flowchart | mermaid | 90 |
| 5 | 46 | flowchart | image | 68 |
| 6 | 47 | flowchart | image | 95 |

## Omissions log

- page 1: No figures on this page. OCR reference contained a duplicated "1. Introduction" block; treated as duplicate and transcribed once. No typo corrections applied.
- page 2: No corrections needed; source text matched OCR reference. Figure regions are diagrams without captions in the source. Page number "2" at bottom excluded from body.
- page 3: No typo corrections needed. Figure 1 bbox estimated from block diagram region on the page.
- page 4: - Continues §5 Network paragraph at top of page.
- Figure contains captions "Transactions Hashed in a Merkle Tree" and "After Pruning Tx0-2 from the Block"; both captured in alt/caption.
- No typo corrections made. Source phrase "a constant of amount of new coins" (§6) is original wording, left verbatim per typo allowance policy — could be "constant amount" if normalized; kept as source.
- page 5: Continuation of the Bitcoin whitepaper; sections 8 and 9 begin on this page. Figures are diagrams (block header chain with Merkle branch; transaction In/Out block diagram) replaced with placeholder tokens. No typo corrections needed.
- page 6: - Privacy model diagram transcribed as a figure placeholder; contains "Traditional Privacy Model" and "New Privacy Model" flow diagrams.
- Probability definitions rendered as LaTeX math blocks; original used inline text with italicized variables.
- No typo corrections made.
- page 7: - Page continues Section 11 (Calculations) from previous page; math content ends mid-section (C code block continues).
- "Rearranging to avoid summing the infinite tail of the distribution..." ends with ellipsis as in source.
- No figures on this page; equations rendered as LaTeX math.
- page 8: Continues section 11 (Calculations) from previous page; result tables rendered as LaTeX arrays per source layout. No figures on this page. No typos corrected.
- page 9: Final page of the document; contains only the References section. Journal/conference titles italicized per source. No figures on this page.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 336238B model=glm-5.3-flash effort=low transcribe_ms=4963.9 verify_ms=2962.8 ocr_ms=35696.1 retries=0 verification_score=100 floor=100% hashes=d6e2f38823c869115faac4f01ab7dea1d398a0e83fd8453ac2d9aa9f7fbb7bd5/8e1a0c8d3947469c7bec09ffa1d18caf80d52cdfca164bd9627b10c4c51f54a3/c2b40556312eaf64d33a8992032f61b80d73e3f6d034f9e83a7cd8007ce0dd2c/a8ab02851b92c00ad722b2830978dc5d6b9def13ce54d4a344bd84c3de15cb64
- page 2: dpi=200 image=1700x2200 284373B model=glm-5.3-flash effort=low transcribe_ms=4922.6 verify_ms=2923.6 ocr_ms=25554.7 retries=0 verification_score=98 floor=100% hashes=f9948c67dd4011aebc6d452e3bdf683fa2697c17f41612143f7f1784db4e97ee/48be9cc639d62eee69acb2e0fbcfd7e028367fc95c8e0bc425c98e1c9c1e769f/4b899146d4de306b7574990cfdcc51a1b9d29f19aabb159ec4d438d7c83c85b0/6db9ca1a35023ca148f65b1814d33684f15577fc752f8bf8ad87b0d1286d0a4b
- page 3: dpi=200 image=1700x2200 353335B model=glm-5.3-flash effort=low transcribe_ms=5245.0 verify_ms=2897.8 ocr_ms=22216.6 retries=0 verification_score=100 floor=100% hashes=64134eaee44d2964aa5c52def2708d287e1764395ab39b37194d358ceb875eaa/1096044ea6a81876dc6d57fc3698a37cfa68ef4ae343d3c9dcea6c4ad3a069c8/3a6860d239cc8499b7ac7a5e2b251b65a5798abb3a2bf6ea5481df8b021fc215/2cfa7ea591e5fd1453ab5aaf6e3ff59a656dbeeaf4e1dc33bde618a579ea5539
- page 4: dpi=200 image=1700x2200 327622B model=glm-5.3-flash effort=low transcribe_ms=6149.2 verify_ms=3275.5 ocr_ms=19471.3 retries=0 verification_score=96 floor=100% hashes=0daecae88b85d3ad7f07a7131e17f6d2ac1ccad790939fc265315689cf987113/a9a27b534a89a68a48b894f112c1ef13021d63d4f6db4c37059d09e1e63c4784/65a8862037a421ebd120cbb9571370eb8d5efc056c0633708dc8047bcfc0cf3c/7cfec44fe12c439fcdee45024a1687169e515e83ad5abde1fcfecbd4c5828a0c
- page 5: dpi=200 image=1700x2200 276070B model=glm-5.3-flash effort=low transcribe_ms=5109.5 verify_ms=2809.3 ocr_ms=26497.0 retries=0 verification_score=100 floor=100% hashes=a908726d2917ae3575783217d25d4f8f2473c24cd0b4c52f4fca8271084ba1d6/0dd85db1997be6ad65e391b7b3c359a3c1ffde7f61f463cc76cb73d37ccb8f8e/009d1eef2783085a998e73888f3d7017de1d1c9ace7f753226bd89413ac1aa79/847462b6414526d460a0b6786ed3d0faacb0c67eb3ba18ca2f1384e7f3470d4c
- page 6: dpi=200 image=1700x2200 304207B model=glm-5.3-flash effort=low transcribe_ms=4738.5 verify_ms=2579.9 ocr_ms=20061.4 retries=0 verification_score=98 floor=100% hashes=176d0b231f889a838467a690c661536b3f7c68986ed117a1f5272e39d5efded8/115700d6733d38e34435d533d1496906654556ddb622197221d39dcebb12d416/13d7ee96a0b79c5bc1747d3622ea73daaf637b02f579355f348c0ecde914979d/dce75bae154b9527b4c71aee43a14191a39e6496903399a6573dd87656cad5c9
- page 7: dpi=200 image=1700x2200 259411B model=glm-5.3-flash effort=low transcribe_ms=4940.2 verify_ms=2461.7 ocr_ms=21385.5 retries=0 verification_score=99 floor=100% hashes=78205fb552a99f2a9c17a59576c503b2d63af63f98e7853eb399b4d8c450689c/0b289e586b9bb0c7121faa95ed010cb2cf67ad91b642ca865232225ecefbd160/bae736eff6877910d52391b21168fe3b4113363876e013b311a3537fe8f6303e/25acb6defe63c12caf8bd650c0ba6a810114ff44d8e62f08fbbe747eb7238296
- page 8: dpi=200 image=1700x2200 215528B model=glm-5.3-flash effort=low transcribe_ms=5350.8 verify_ms=2579.3 ocr_ms=27698.0 retries=0 verification_score=98 floor=100% hashes=17110863cb1558037f3dd2c179eed093f5711e47ac95240cdf70955a0c354dfb/41aae7856b28dba5cbcf9aa73495f95a062d991f48d7e2bd2ee52e3a491c2f38/081a5340df5e42a88595607215c647af7ece2741c597dc392f222f58c61f1516/0b8cc590ff8cd20ceac1988259961f8cc93c0e376294dce3e054a3afe1cfdc45
- page 9: dpi=200 image=1700x2200 155714B model=glm-5.3-flash effort=low transcribe_ms=3967.5 verify_ms=1946.1 ocr_ms=15958.4 retries=0 verification_score=100 floor=99% hashes=7b09e8df46f536b0f860a0c3c4e882660b499598f3374f6ce5815a81a175dc5d/382bbb0cf72bfa12e9f1b234f5fa4f087a4c591399fd401ee14cb6fe7e580ffc/43cd8833b5c490235bf58d852d8e3b2773833b23c4659925a81a54ddd178d77d/5b75b0de543fbaebb64903d26806e52cb0c4cd5e14dd0f16587ab1267aabc4d1

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:23: [Expected: 80, Actual: 1134]
- MD013:27: [Expected: 80, Actual: 1098]
- MD013:29: [Expected: 80, Actual: 700]
- MD013:33: [Expected: 80, Actual: 306]
- MD013:35: [Expected: 80, Actual: 156]
- MD033:37: [Element: details]
- MD013:40: [Expected: 80, Actual: 216]
- MD013:44: [Expected: 80, Actual: 572]
- MD013:46: [Expected: 80, Actual: 721]
- MD013:50: [Expected: 80, Actual: 460]
- MD013:73: [Expected: 80, Actual: 116]
- MD033:75: [Element: details]
- MD013:78: [Expected: 80, Actual: 156]
- MD033:80: [Element: details]
- MD013:83: [Expected: 80, Actual: 142]
- MD013:90: [Expected: 80, Actual: 444]
- MD013:92: [Expected: 80, Actual: 413]
- MD013:114: [Expected: 80, Actual: 160]
- MD033:116: [Element: details]
- MD013:123: [Expected: 80, Actual: 816]
- MD013:125: [Expected: 80, Actual: 260]
- MD013:135: [Expected: 80, Actual: 89]
- MD013:136: [Expected: 80, Actual: 157]
- MD013:138: [Expected: 80, Actual: 507]
- MD013:140: [Expected: 80, Actual: 315]
- MD013:144: [Expected: 80, Actual: 500]
- MD013:146: [Expected: 80, Actual: 391]
- MD013:148: [Expected: 80, Actual: 461]
- MD013:152: [Expected: 80, Actual: 410]
- MD013:187: [Expected: 80, Actual: 246]
- MD033:189: [Element: details]
- MD013:194: [Expected: 80, Actual: 87]
- MD036:194:
- MD013:198: [Expected: 80, Actual: 366]
- MD037:198:
- MD037:198:
- MD013:202: [Expected: 80, Actual: 543]
- MD013:235: [Expected: 80, Actual: 229]
- MD033:237: [Element: details]
- MD013:240: [Expected: 80, Actual: 155]
- MD036:242:
- MD033:244: [Element: details]
- MD013:247: [Expected: 80, Actual: 168]
- MD013:252: [Expected: 80, Actual: 730]
- MD013:256: [Expected: 80, Actual: 462]
- MD036:260:
- MD013:262: [Expected: 80, Actual: 242]
- MD013:266: [Expected: 80, Actual: 661]
- MD013:268: [Expected: 80, Actual: 156]
- MD033:270: [Element: details]
- MD013:273: [Expected: 80, Actual: 146]
- MD013:277: [Expected: 80, Actual: 390]
- MD013:281: [Expected: 80, Actual: 511]
- MD013:283: [Expected: 80, Actual: 296]
- MD013:285: [Expected: 80, Actual: 380]
- MD013:289: [Expected: 80, Actual: 92]
- MD013:296: [Expected: 80, Actual: 282]
- MD013:298: [Expected: 80, Actual: 405]
- MD013:300: [Expected: 80, Actual: 447]
- MD013:302: [Expected: 80, Actual: 336]
- MD013:306: [Expected: 80, Actual: 194]
- MD013:308: [Expected: 80, Actual: 161]
- MD013:383: [Expected: 80, Actual: 1113]
- MD025:385:
- MD034:387:
- MD013:389: [Expected: 80, Actual: 192]
- MD013:391: [Expected: 80, Actual: 130]
- MD013:393: [Expected: 80, Actual: 205]
- MD013:395: [Expected: 80, Actual: 170]
- MD013:397: [Expected: 80, Actual: 113]
- MD034:397:
- MD013:399: [Expected: 80, Actual: 159]
