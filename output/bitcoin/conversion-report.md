# Conversion report — bitcoin.pdf

- job_id: 4b5c8418-babe-4873-82ea-65b23ad63404
- status: assembling
- pages: 9
- wall-clock: not started
- tokens: prompt=123660 completion=7011
- pipeline_version: 073654be6c457b411ab24a51dcfff4bdea2968daf6252a3e996dc1f6b48c7d48
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 67

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 98 | 0 | 200 | 12878 | 762 | False |
| 2 | verified | 100 | 0 | 200 | 13147 | 785 | False |
| 3 | verified | 98 | 0 | 200 | 13516 | 866 | False |
| 4 | verified | 95 | 0 | 200 | 13877 | 908 | False |
| 5 | verified | 98 | 0 | 200 | 14297 | 750 | False |
| 6 | verified | 100 | 0 | 200 | 13926 | 797 | False |
| 7 | verified | 100 | 0 | 200 | 14037 | 766 | False |
| 8 | verified | 99 | 0 | 200 | 14386 | 868 | False |
| 9 | verified | 98 | 0 | 200 | 13596 | 509 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 7
- converted to Mermaid: 3 (43%)
- data-table fallbacks: 0
- image fallbacks: 4

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 2 | 1 | flowchart | mermaid | 92 |
| 2 | 2 | flowchart | mermaid | 90 |
| 3 | 3 | flowchart | image | 92 |
| 4 | 4 | flowchart | mermaid | 95 |
| 5 | 5 | flowchart | image | 85 |
| 5 | 6 | flowchart | image | 70 |
| 6 | 7 | flowchart | image | 90 |

## Omissions log

- page 1: No figures on this page. Page number "1" at bottom center excluded from body. No uncertain characters; no typo corrections needed.
- page 2: No typo corrections made. Figures are uncaptioned diagrams in the source. Page number "2" excluded from body.
- page 3: No figure numbering/captions in source; figure index assigned sequentially across document (pages 1–2 had figures 1–2, so this page's diagram is index 3 in the document, but rendered as page-local index 1 per token format). Page number "3" at bottom center excluded from body. No typo corrections needed.
- page 4: Source typo "a constant of amount of new coins" left as-is (typo allowance logged). Figure 1 contains two block diagrams with captions "Transactions Hashed in a Merkle Tree" and "After Pruning Tx0-2 from the Block".
- page 5: No typo corrections needed. Figure captions ("Longest Proof-of-Work Chain", "Merkle Branch for Tx3", "Transaction") are labels within the diagrams, included in figure alt text/captions. No [?] uncertainties.
- page 6: The figure region includes the two privacy-model diagrams (Traditional Privacy Model and New Privacy Model). Math blocks rendered as LaTeX from the OCR reference; original page renders the cases equation with italic "if" and q/p as (q/p)^z. Page number 6 at bottom excluded from body.
- page 7: Continuation of Section 11 (Calculations) from previous page. No figures on this page. No typo corrections made.
- page 8: Continuation of Section 11 (Calculations) code results from previous page. Result blocks rendered as LaTeX arrays. "12. Conclusion" heading numbered "12." in source, kept as-is under "##".
- page 9: This page (9) contains only the References section; no figures. Page number "9" in footer excluded from body. No typo corrections needed; no uncertain characters.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 336238B model=glm-5.3-flash effort=low transcribe_ms=4511.0 verify_ms=2885.5 ocr_ms=35040.9 retries=0 verification_score=98 floor=100% hashes=d6e2f38823c869115faac4f01ab7dea1d398a0e83fd8453ac2d9aa9f7fbb7bd5/8e1a0c8d3947469c7bec09ffa1d18caf80d52cdfca164bd9627b10c4c51f54a3/c2b40556312eaf64d33a8992032f61b80d73e3f6d034f9e83a7cd8007ce0dd2c/a8ab02851b92c00ad722b2830978dc5d6b9def13ce54d4a344bd84c3de15cb64
- page 2: dpi=200 image=1700x2200 284373B model=glm-5.3-flash effort=low transcribe_ms=4514.0 verify_ms=3468.1 ocr_ms=25010.3 retries=0 verification_score=100 floor=100% hashes=f9948c67dd4011aebc6d452e3bdf683fa2697c17f41612143f7f1784db4e97ee/48be9cc639d62eee69acb2e0fbcfd7e028367fc95c8e0bc425c98e1c9c1e769f/4b899146d4de306b7574990cfdcc51a1b9d29f19aabb159ec4d438d7c83c85b0/aafe94c7726bee14c1c17720c72f230716d7b696c8366eb8460a79b04c7e3d33
- page 3: dpi=200 image=1700x2200 353335B model=glm-5.3-flash effort=low transcribe_ms=5262.0 verify_ms=2755.5 ocr_ms=21584.2 retries=0 verification_score=98 floor=100% hashes=64134eaee44d2964aa5c52def2708d287e1764395ab39b37194d358ceb875eaa/1096044ea6a81876dc6d57fc3698a37cfa68ef4ae343d3c9dcea6c4ad3a069c8/3a6860d239cc8499b7ac7a5e2b251b65a5798abb3a2bf6ea5481df8b021fc215/6055ad516954a1e96a20e954b7ccda7b95095f6d6cbc6e6fb25aba8cefe20812
- page 4: dpi=200 image=1700x2200 327622B model=glm-5.3-flash effort=low transcribe_ms=4574.3 verify_ms=2986.4 ocr_ms=19457.5 retries=0 verification_score=95 floor=100% hashes=0daecae88b85d3ad7f07a7131e17f6d2ac1ccad790939fc265315689cf987113/a9a27b534a89a68a48b894f112c1ef13021d63d4f6db4c37059d09e1e63c4784/65a8862037a421ebd120cbb9571370eb8d5efc056c0633708dc8047bcfc0cf3c/dbeb31f09686fc65d46c579899c1e88fbc867b1c92acf48f3e32670717b873e7
- page 5: dpi=200 image=1700x2200 276070B model=glm-5.3-flash effort=low transcribe_ms=4018.4 verify_ms=2033.7 ocr_ms=27241.0 retries=0 verification_score=98 floor=100% hashes=a908726d2917ae3575783217d25d4f8f2473c24cd0b4c52f4fca8271084ba1d6/0dd85db1997be6ad65e391b7b3c359a3c1ffde7f61f463cc76cb73d37ccb8f8e/009d1eef2783085a998e73888f3d7017de1d1c9ace7f753226bd89413ac1aa79/e2ddb968eb2d6d73f23f76d39bdbbc393c05a85bf73e32eb773f906a1ac54004
- page 6: dpi=200 image=1700x2200 304207B model=glm-5.3-flash effort=low transcribe_ms=4789.7 verify_ms=2066.5 ocr_ms=19800.1 retries=0 verification_score=100 floor=100% hashes=176d0b231f889a838467a690c661536b3f7c68986ed117a1f5272e39d5efded8/115700d6733d38e34435d533d1496906654556ddb622197221d39dcebb12d416/13d7ee96a0b79c5bc1747d3622ea73daaf637b02f579355f348c0ecde914979d/eeae13f3087fbf51127644ef149e8644aae2f0e470da749299007229d35a0cf4
- page 7: dpi=200 image=1700x2200 259411B model=glm-5.3-flash effort=low transcribe_ms=4379.1 verify_ms=2341.5 ocr_ms=21262.2 retries=0 verification_score=100 floor=100% hashes=78205fb552a99f2a9c17a59576c503b2d63af63f98e7853eb399b4d8c450689c/0b289e586b9bb0c7121faa95ed010cb2cf67ad91b642ca865232225ecefbd160/bae736eff6877910d52391b21168fe3b4113363876e013b311a3537fe8f6303e/25acb6defe63c12caf8bd650c0ba6a810114ff44d8e62f08fbbe747eb7238296
- page 8: dpi=200 image=1700x2200 215528B model=glm-5.3-flash effort=low transcribe_ms=4584.1 verify_ms=2130.1 ocr_ms=27597.1 retries=0 verification_score=99 floor=100% hashes=17110863cb1558037f3dd2c179eed093f5711e47ac95240cdf70955a0c354dfb/41aae7856b28dba5cbcf9aa73495f95a062d991f48d7e2bd2ee52e3a491c2f38/081a5340df5e42a88595607215c647af7ece2741c597dc392f222f58c61f1516/9b215189381a988151efcab9926b4b2e014a17a458e986717c7ac46e2477a064
- page 9: dpi=200 image=1700x2200 155714B model=glm-5.3-flash effort=low transcribe_ms=3477.7 verify_ms=1818.3 ocr_ms=15752.2 retries=0 verification_score=98 floor=99% hashes=7b09e8df46f536b0f860a0c3c4e882660b499598f3374f6ce5815a81a175dc5d/382bbb0cf72bfa12e9f1b234f5fa4f087a4c591399fd401ee14cb6fe7e580ffc/43cd8833b5c490235bf58d852d8e3b2773833b23c4659925a81a54ddd178d77d/5b75b0de543fbaebb64903d26806e52cb0c4cd5e14dd0f16587ab1267aabc4d1

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:23: [Expected: 80, Actual: 1134]
- MD013:27: [Expected: 80, Actual: 1098]
- MD013:29: [Expected: 80, Actual: 700]
- MD013:33: [Expected: 80, Actual: 306]
- MD013:66: [Expected: 80, Actual: 246]
- MD033:68: [Element: details]
- MD013:71: [Expected: 80, Actual: 155]
- MD033:73: [Element: details]
- MD013:76: [Expected: 80, Actual: 156]
- MD013:81: [Expected: 80, Actual: 572]
- MD013:83: [Expected: 80, Actual: 721]
- MD013:87: [Expected: 80, Actual: 460]
- MD013:98: [Expected: 80, Actual: 150]
- MD033:100: [Element: details]
- MD013:109: [Expected: 80, Actual: 444]
- MD013:111: [Expected: 80, Actual: 413]
- MD013:115: [Expected: 80, Actual: 816]
- MD013:117: [Expected: 80, Actual: 260]
- MD013:127: [Expected: 80, Actual: 89]
- MD013:128: [Expected: 80, Actual: 157]
- MD013:130: [Expected: 80, Actual: 507]
- MD013:132: [Expected: 80, Actual: 315]
- MD013:136: [Expected: 80, Actual: 500]
- MD013:138: [Expected: 80, Actual: 391]
- MD013:140: [Expected: 80, Actual: 461]
- MD013:144: [Expected: 80, Actual: 410]
- MD013:179: [Expected: 80, Actual: 156]
- MD033:181: [Element: details]
- MD036:186:
- MD013:190: [Expected: 80, Actual: 366]
- MD037:190:
- MD037:190:
- MD013:194: [Expected: 80, Actual: 543]
- MD013:196: [Expected: 80, Actual: 156]
- MD036:198:
- MD033:200: [Element: details]
- MD013:203: [Expected: 80, Actual: 184]
- MD013:207: [Expected: 80, Actual: 730]
- MD013:211: [Expected: 80, Actual: 462]
- MD013:213: [Expected: 80, Actual: 120]
- MD036:215:
- MD013:217: [Expected: 80, Actual: 242]
- MD013:221: [Expected: 80, Actual: 661]
- MD013:223: [Expected: 80, Actual: 155]
- MD033:225: [Element: details]
- MD013:228: [Expected: 80, Actual: 193]
- MD013:232: [Expected: 80, Actual: 390]
- MD013:236: [Expected: 80, Actual: 511]
- MD013:238: [Expected: 80, Actual: 296]
- MD013:240: [Expected: 80, Actual: 380]
- MD013:244: [Expected: 80, Actual: 92]
- MD013:251: [Expected: 80, Actual: 282]
- MD013:253: [Expected: 80, Actual: 405]
- MD013:255: [Expected: 80, Actual: 447]
- MD013:257: [Expected: 80, Actual: 336]
- MD013:261: [Expected: 80, Actual: 194]
- MD013:263: [Expected: 80, Actual: 161]
- MD013:345: [Expected: 80, Actual: 1113]
- MD025:347:
- MD034:349:
- MD013:351: [Expected: 80, Actual: 192]
- MD013:353: [Expected: 80, Actual: 130]
- MD013:355: [Expected: 80, Actual: 205]
- MD013:357: [Expected: 80, Actual: 170]
- MD013:359: [Expected: 80, Actual: 113]
- MD034:359:
- MD013:361: [Expected: 80, Actual: 159]
