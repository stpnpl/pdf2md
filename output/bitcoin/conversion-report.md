# Conversion report — bitcoin.pdf

- job_id: 10386f7f-e5cb-4a32-ae93-982b6eb172ac
- status: assembling
- pages: 9
- wall-clock: not started
- tokens: prompt=122221 completion=6882
- pipeline_version: 49d37aab5011162c95b2267d3c52c5edb25ebd6d06ffb252038f28d3523593bc
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 68

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 99 | 0 | 200 | 12358 | 688 | False |
| 2 | verified | 95 | 0 | 200 | 12768 | 801 | False |
| 3 | verified | 98 | 0 | 200 | 13647 | 826 | False |
| 4 | verified | 98 | 0 | 200 | 14138 | 895 | False |
| 5 | verified | 98 | 0 | 200 | 13726 | 746 | False |
| 6 | verified | 98 | 0 | 200 | 13956 | 809 | False |
| 7 | verified | 98 | 0 | 200 | 13992 | 826 | False |
| 8 | verified | 98 | 0 | 200 | 14151 | 798 | False |
| 9 | verified | 100 | 0 | 200 | 13485 | 493 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 7
- converted to Mermaid: 2 (29%)
- data-table fallbacks: 0
- image fallbacks: 5

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 2 | 16 | flowchart | image | 93 |
| 2 | 17 | flowchart | image | 80 |
| 3 | 18 | flowchart | image | 90 |
| 4 | 19 | flowchart | image | 95 |
| 5 | 20 | flowchart | image | 92 |
| 5 | 21 | flowchart | mermaid | 95 |
| 6 | 22 | flowchart | mermaid | 95 |

## Omissions log

- page 1: No figures on this page. No text corrections needed. Page number "1" at bottom center excluded from body.
- page 2: - Page 2 continues the Bitcoin whitepaper; sections 2 and 3 follow section 1 from page 1.
- Figures are diagram regions (transaction chain diagram and timestamp server diagram); embedded diagram text (Transaction, Owner N's Public Key, Hash, Verify, Sign, Block, Item) is reproduced in the figure alt text and placeholder regions rather than as body text.
- No spelling or grammar corrections needed; no uncertain characters.
- Page number "2" at bottom center excluded from body output.
- page 3: No typo corrections. Figure region estimated from block diagram (Block/Prev Hash/Nonce/Tx) on the page.
- page 4: - Source text "a constant of amount of new coins" appears to be a typo; preserved verbatim (candidate correction: "a constant amount of new coins").
- Figure caption text embedded in the diagram ("Transactions Hashed in a Merkle Tree", "After Pruning Tx0-2 from the Block") is represented in the figure caption, not the body text.
- Figure bbox is approximate.
- page 5: No spelling or grammar corrections were needed. Figure 1 caption labels ("Longest Proof-of-Work Chain", "Merkle Branch for Tx3") appear inside the diagram region and are reproduced in the figure alt/caption. No uncertain characters.
- page 6: Page 6 of the Bitcoin whitepaper, continuing from section 9. The privacy model diagram rendered as a figure placeholder; its labels (Traditional Privacy Model: Identities → Transactions → Trusted Third Party → Counterparty | Public; New Privacy Model: Identities | Transactions → Public) are captured in alt text. Piecewise formula transcribed as LaTeX from OCR fragment.
- page 7: - Page continues Section 11 "Calculations" from previous page (section header was on prior page; not repeated).
- Math formulas rendered as LaTeX; source used rendered equations. The "if" conditions in the cases environments are italic text in the source, reproduced as "if".
- No figures on this page.
- page 8: Monospace result blocks rendered as fenced code blocks. "12. Conclusion" continues the section numbering from page 7 (Section 11). No figures on this page; no corrections needed.
- page 9: Page 9 contains only the References section (continuation of document); running content limited to page number "9" at bottom center. No figures on this page.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 336238B model=glm-5.3-flash effort=low transcribe_ms=5098.3 verify_ms=2976.4 ocr_ms=440.2 retries=0 verification_score=99 floor=100% hashes=d6e2f38823c869115faac4f01ab7dea1d398a0e83fd8453ac2d9aa9f7fbb7bd5/8e1a0c8d3947469c7bec09ffa1d18caf80d52cdfca164bd9627b10c4c51f54a3/427e85bed23ec53ebc591a19298b304fdb516fbb95eef92c70c8d3a66353fca5/a8ab02851b92c00ad722b2830978dc5d6b9def13ce54d4a344bd84c3de15cb64
- page 2: dpi=200 image=1700x2200 284373B model=glm-5.3-flash effort=low transcribe_ms=6051.0 verify_ms=2761.2 ocr_ms=347.0 retries=0 verification_score=95 floor=95% hashes=f9948c67dd4011aebc6d452e3bdf683fa2697c17f41612143f7f1784db4e97ee/48be9cc639d62eee69acb2e0fbcfd7e028367fc95c8e0bc425c98e1c9c1e769f/ce59cf4ceb97cdf0ff506f35112208c62e97adfbd8a6c6e58810068ebafa11b3/f69b17ffb7211f7138cdcaca171d3bded2a9fcdfe18892126f5d79996a7252a9
- page 3: dpi=200 image=1700x2200 353335B model=glm-5.3-flash effort=low transcribe_ms=5585.6 verify_ms=3233.0 ocr_ms=369.7 retries=0 verification_score=98 floor=99% hashes=64134eaee44d2964aa5c52def2708d287e1764395ab39b37194d358ceb875eaa/1096044ea6a81876dc6d57fc3698a37cfa68ef4ae343d3c9dcea6c4ad3a069c8/8226a28d8f4ee4ea47f2c7bc44a632e514679aaf386e6cc90c23493111d863dd/6055ad516954a1e96a20e954b7ccda7b95095f6d6cbc6e6fb25aba8cefe20812
- page 4: dpi=200 image=1700x2200 327622B model=glm-5.3-flash effort=low transcribe_ms=5153.2 verify_ms=3301.7 ocr_ms=365.5 retries=0 verification_score=98 floor=95% hashes=0daecae88b85d3ad7f07a7131e17f6d2ac1ccad790939fc265315689cf987113/a9a27b534a89a68a48b894f112c1ef13021d63d4f6db4c37059d09e1e63c4784/951e68d241b3c2ab020b9e9e9ca01f75485f02d5955f6e3f6caa725da57889fd/93e07fb42f8d0942d3969da429f0681460d90ea88bdc40c80ea0283b9e8ed547
- page 5: dpi=200 image=1700x2200 276070B model=glm-5.3-flash effort=low transcribe_ms=4753.5 verify_ms=3158.1 ocr_ms=347.1 retries=0 verification_score=98 floor=94% hashes=a908726d2917ae3575783217d25d4f8f2473c24cd0b4c52f4fca8271084ba1d6/0dd85db1997be6ad65e391b7b3c359a3c1ffde7f61f463cc76cb73d37ccb8f8e/7c2999520cfec635c2fb86bebca2150182a84b7bcaf087139e4a19c56ee00436/a63ecb650b9c503aa22f290eedeaa4df16ac40ee0f5f46714b1c08dcc889f900
- page 6: dpi=200 image=1700x2200 304207B model=glm-5.3-flash effort=low transcribe_ms=5869.6 verify_ms=2498.5 ocr_ms=352.4 retries=0 verification_score=98 floor=99% hashes=176d0b231f889a838467a690c661536b3f7c68986ed117a1f5272e39d5efded8/115700d6733d38e34435d533d1496906654556ddb622197221d39dcebb12d416/26b059aad12e1fc100a141d48d4da509675a70222ed375a11785761fe92af8d4/3465746a23c8b73e5209a831f697818a8daf4d773f0a4fabf696df7dd4eb1cec
- page 7: dpi=200 image=1700x2200 259411B model=glm-5.3-flash effort=low transcribe_ms=5865.1 verify_ms=2584.0 ocr_ms=331.6 retries=0 verification_score=98 floor=99% hashes=78205fb552a99f2a9c17a59576c503b2d63af63f98e7853eb399b4d8c450689c/0b289e586b9bb0c7121faa95ed010cb2cf67ad91b642ca865232225ecefbd160/e293e261f46b18ce7b4538dde42ea37530afa6f94691b4d63f2e15fc1928ec19/43c4b1becaf829ce05578e2d8f702e63efc2524d016e6567d2c1025d0a07f48a
- page 8: dpi=200 image=1700x2200 215528B model=glm-5.3-flash effort=low transcribe_ms=5390.9 verify_ms=2761.0 ocr_ms=213.3 retries=0 verification_score=98 floor=100% hashes=17110863cb1558037f3dd2c179eed093f5711e47ac95240cdf70955a0c354dfb/41aae7856b28dba5cbcf9aa73495f95a062d991f48d7e2bd2ee52e3a491c2f38/f5cddb1a04bc75aeff575033d24b4fcc85c01cda7cbb339e07a84d7f0b08d0c9/3a9aa6b8ac56125db5a75602ed8638850d754b0ef41ae9a7491359ab795696fa
- page 9: dpi=200 image=1700x2200 155714B model=glm-5.3-flash effort=low transcribe_ms=3858.1 verify_ms=2711.8 ocr_ms=304.5 retries=0 verification_score=100 floor=99% hashes=7b09e8df46f536b0f860a0c3c4e882660b499598f3374f6ce5815a81a175dc5d/382bbb0cf72bfa12e9f1b234f5fa4f087a4c591399fd401ee14cb6fe7e580ffc/7de2f62fcd9846bd0fb270435b35e876ec89ffc0cccbd5d68421de2ed905ef19/4ac7cdac4f6fec96e75708643ffc057baee98a0602b61704db1bc05a84f9569d

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:23: [Expected: 80, Actual: 1134]
- MD013:27: [Expected: 80, Actual: 1098]
- MD013:29: [Expected: 80, Actual: 700]
- MD013:33: [Expected: 80, Actual: 306]
- MD013:35: [Expected: 80, Actual: 156]
- MD033:37: [Element: details]
- MD013:40: [Expected: 80, Actual: 170]
- MD013:44: [Expected: 80, Actual: 572]
- MD013:46: [Expected: 80, Actual: 721]
- MD013:50: [Expected: 80, Actual: 460]
- MD013:52: [Expected: 80, Actual: 150]
- MD013:56: [Expected: 80, Actual: 444]
- MD013:58: [Expected: 80, Actual: 413]
- MD013:62: [Expected: 80, Actual: 816]
- MD013:64: [Expected: 80, Actual: 260]
- MD013:74: [Expected: 80, Actual: 89]
- MD013:75: [Expected: 80, Actual: 157]
- MD013:77: [Expected: 80, Actual: 507]
- MD013:79: [Expected: 80, Actual: 315]
- MD013:83: [Expected: 80, Actual: 500]
- MD013:85: [Expected: 80, Actual: 391]
- MD013:87: [Expected: 80, Actual: 461]
- MD013:91: [Expected: 80, Actual: 410]
- MD013:93: [Expected: 80, Actual: 156]
- MD036:95:
- MD033:97: [Element: details]
- MD013:100: [Expected: 80, Actual: 199]
- MD013:104: [Expected: 80, Actual: 366]
- MD037:104:
- MD037:104:
- MD013:108: [Expected: 80, Actual: 543]
- MD013:110: [Expected: 80, Actual: 155]
- MD036:112:
- MD033:114: [Element: details]
- MD013:117: [Expected: 80, Actual: 164]
- MD013:121: [Expected: 80, Actual: 730]
- MD013:125: [Expected: 80, Actual: 462]
- MD013:148: [Expected: 80, Actual: 146]
- MD033:150: [Element: details]
- MD036:155:
- MD013:159: [Expected: 80, Actual: 242]
- MD013:163: [Expected: 80, Actual: 661]
- MD013:171: [Expected: 80, Actual: 167]
- MD033:173: [Element: details]
- MD013:176: [Expected: 80, Actual: 156]
- MD033:178: [Element: details]
- MD013:181: [Expected: 80, Actual: 152]
- MD013:186: [Expected: 80, Actual: 390]
- MD013:190: [Expected: 80, Actual: 511]
- MD013:192: [Expected: 80, Actual: 296]
- MD013:194: [Expected: 80, Actual: 380]
- MD013:202: [Expected: 80, Actual: 282]
- MD013:204: [Expected: 80, Actual: 405]
- MD013:206: [Expected: 80, Actual: 447]
- MD013:208: [Expected: 80, Actual: 334]
- MD013:212: [Expected: 80, Actual: 194]
- MD013:214: [Expected: 80, Actual: 127]
- MD040:243:
- MD040:273:
- MD013:287: [Expected: 80, Actual: 1113]
- MD034:291:
- MD013:293: [Expected: 80, Actual: 192]
- MD013:295: [Expected: 80, Actual: 130]
- MD013:297: [Expected: 80, Actual: 205]
- MD013:299: [Expected: 80, Actual: 170]
- MD013:301: [Expected: 80, Actual: 113]
- MD034:301:
- MD013:303: [Expected: 80, Actual: 159]
