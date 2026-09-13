# Conversion report — bitcoin.pdf

- job_id: 20fdf826-4f17-4b34-b5a1-8a2a0f40901a
- status: assembling
- pages: 9
- wall-clock: not started
- tokens: prompt=122317 completion=6772
- pipeline_version: 9c215872aa0b575aade8ae9fb73a81b65c9fb7d96e9934b244133c2636e44bc0
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 72

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 100 | 0 | 200 | 12358 | 668 | False |
| 2 | verified | 98 | 0 | 200 | 12771 | 828 | False |
| 3 | verified | 97 | 0 | 200 | 13650 | 832 | False |
| 4 | verified | 97 | 0 | 200 | 14144 | 903 | False |
| 5 | verified | 98 | 0 | 200 | 13733 | 718 | False |
| 6 | verified | 98 | 0 | 200 | 13965 | 766 | False |
| 7 | verified | 100 | 0 | 200 | 14017 | 770 | False |
| 8 | verified | 99 | 0 | 200 | 14173 | 790 | False |
| 9 | verified | 98 | 0 | 200 | 13506 | 497 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 7
- converted to Mermaid: 4 (57%)
- data-table fallbacks: 0
- image fallbacks: 3

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 2 | 78 | flowchart | mermaid | 92 |
| 2 | 79 | flowchart | mermaid | 95 |
| 3 | 80 | flowchart | mermaid | 95 |
| 4 | 81 | flowchart | image | 90 |
| 5 | 82 | flowchart | image | 92 |
| 5 | 83 | flowchart | mermaid | 92 |
| 6 | 84 | flowchart | image | 96 |

## Omissions log

- page 1: No figures on page. No corrections needed; text matches source verbatim.
- page 2: No corrections needed; source text transcribed verbatim. Figure 1 text labels (Transaction, Owner X's Public Key, Hash, Verify, Sign, Owner X's Private Key, Owner X's Signature) are contained within the figure placeholder. Figure 2 labels (Block, Item, Item, ..., Hash) contained within figure placeholder.
- page 3: No figures dropped. Numbered list items converted from "1)" style to GFM ordered list; text verbatim otherwise. No typos corrected. Figure bbox estimated from rendered page image.
- page 4: - Page continues section 5 (Network) text from previous page before section 6 heading.
- Figure region includes both block diagrams and their captions ("Transactions Hashed in a Merkle Tree" and "After Pruning Tx0-2 from the Block").
- Asterisks in "80 bytes * 6 * 24 * 365" escaped for GFM.
- "constant of amount of new coins" kept verbatim per DEC-009 typo allowance (source reads "a constant of amount of new coins").
- No uncertain characters.
- page 5: No typo corrections needed. Figure 1 caption text ("Longest Proof-of-Work Chain", "Merkle Branch for Tx3") and block labels are contained within the figure region, so they are not duplicated as body text.
- page 6: No typo corrections needed. Math formula transcribed as LaTeX from the typeset piecewise equation; original used a brace structure equivalent to cases. Diagram region treated as a single figure placeholder.
- page 7: Page 7 continues Section 11 (Calculations) from page 6; the Poisson distribution discussion follows the gambler's ruin setup. No figures on this page; formulas rendered as LaTeX math from the source equations. No typo corrections needed.
- page 8: No figures on this page. Running results and solving-for-P blocks rendered as plain fenced code blocks (non-C). No typo corrections needed.
- page 9: Final page contains only the References section; body text of sections 10-12 appeared on prior pages. No figures on this page.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 336238B model=glm-5.3-flash effort=low transcribe_ms=7241.5 verify_ms=2607.2 ocr_ms=101.9 retries=0 verification_score=100 floor=100% hashes=d6e2f38823c869115faac4f01ab7dea1d398a0e83fd8453ac2d9aa9f7fbb7bd5/8e1a0c8d3947469c7bec09ffa1d18caf80d52cdfca164bd9627b10c4c51f54a3/427e85bed23ec53ebc591a19298b304fdb516fbb95eef92c70c8d3a66353fca5/a8ab02851b92c00ad722b2830978dc5d6b9def13ce54d4a344bd84c3de15cb64
- page 2: dpi=200 image=1700x2200 284373B model=glm-5.3-flash effort=low transcribe_ms=5228.8 verify_ms=3349.1 ocr_ms=359.3 retries=0 verification_score=98 floor=95% hashes=f9948c67dd4011aebc6d452e3bdf683fa2697c17f41612143f7f1784db4e97ee/48be9cc639d62eee69acb2e0fbcfd7e028367fc95c8e0bc425c98e1c9c1e769f/ce59cf4ceb97cdf0ff506f35112208c62e97adfbd8a6c6e58810068ebafa11b3/d9d500cd73369909515e37d01616a0a48a17d3c7f3be2e497488676c6d12be1b
- page 3: dpi=200 image=1700x2200 353335B model=glm-5.3-flash effort=low transcribe_ms=5827.9 verify_ms=2672.3 ocr_ms=382.1 retries=0 verification_score=97 floor=99% hashes=64134eaee44d2964aa5c52def2708d287e1764395ab39b37194d358ceb875eaa/1096044ea6a81876dc6d57fc3698a37cfa68ef4ae343d3c9dcea6c4ad3a069c8/8226a28d8f4ee4ea47f2c7bc44a632e514679aaf386e6cc90c23493111d863dd/ec559cecbad405481fc70fd2af47d4e93beb620a4777197b4be48f306adaeae6
- page 4: dpi=200 image=1700x2200 327622B model=glm-5.3-flash effort=low transcribe_ms=5769.1 verify_ms=3538.4 ocr_ms=375.8 retries=0 verification_score=97 floor=95% hashes=0daecae88b85d3ad7f07a7131e17f6d2ac1ccad790939fc265315689cf987113/a9a27b534a89a68a48b894f112c1ef13021d63d4f6db4c37059d09e1e63c4784/951e68d241b3c2ab020b9e9e9ca01f75485f02d5955f6e3f6caa725da57889fd/2b7e0de38a1c19b10bd9c3abe104075af241026a2d274ff6aae2aa87c2e5e9aa
- page 5: dpi=200 image=1700x2200 276070B model=glm-5.3-flash effort=low transcribe_ms=6129.9 verify_ms=3299.6 ocr_ms=381.7 retries=0 verification_score=98 floor=94% hashes=a908726d2917ae3575783217d25d4f8f2473c24cd0b4c52f4fca8271084ba1d6/0dd85db1997be6ad65e391b7b3c359a3c1ffde7f61f463cc76cb73d37ccb8f8e/7c2999520cfec635c2fb86bebca2150182a84b7bcaf087139e4a19c56ee00436/55e7e6a241b5f779f6bbacd69896eb187ac85269cb40c2a8e53054faafaef43f
- page 6: dpi=200 image=1700x2200 304207B model=glm-5.3-flash effort=low transcribe_ms=6011.0 verify_ms=2629.8 ocr_ms=368.2 retries=0 verification_score=98 floor=99% hashes=176d0b231f889a838467a690c661536b3f7c68986ed117a1f5272e39d5efded8/115700d6733d38e34435d533d1496906654556ddb622197221d39dcebb12d416/26b059aad12e1fc100a141d48d4da509675a70222ed375a11785761fe92af8d4/507a3cf10265633efb788f8f3423c94bbeb89ab86b1f3592c544112beca07080
- page 7: dpi=200 image=1700x2200 259411B model=glm-5.3-flash effort=low transcribe_ms=6458.8 verify_ms=3085.3 ocr_ms=368.7 retries=0 verification_score=100 floor=99% hashes=78205fb552a99f2a9c17a59576c503b2d63af63f98e7853eb399b4d8c450689c/0b289e586b9bb0c7121faa95ed010cb2cf67ad91b642ca865232225ecefbd160/e293e261f46b18ce7b4538dde42ea37530afa6f94691b4d63f2e15fc1928ec19/eba98f599bec545bdfec77d520f3fb7669947dc6111b98ac4ba5c7b958d2db3b
- page 8: dpi=200 image=1700x2200 215528B model=glm-5.3-flash effort=low transcribe_ms=5732.9 verify_ms=2827.9 ocr_ms=325.8 retries=0 verification_score=99 floor=100% hashes=17110863cb1558037f3dd2c179eed093f5711e47ac95240cdf70955a0c354dfb/41aae7856b28dba5cbcf9aa73495f95a062d991f48d7e2bd2ee52e3a491c2f38/f5cddb1a04bc75aeff575033d24b4fcc85c01cda7cbb339e07a84d7f0b08d0c9/3a9aa6b8ac56125db5a75602ed8638850d754b0ef41ae9a7491359ab795696fa
- page 9: dpi=200 image=1700x2200 155714B model=glm-5.3-flash effort=low transcribe_ms=4551.4 verify_ms=2788.6 ocr_ms=319.0 retries=0 verification_score=98 floor=99% hashes=7b09e8df46f536b0f860a0c3c4e882660b499598f3374f6ce5815a81a175dc5d/382bbb0cf72bfa12e9f1b234f5fa4f087a4c591399fd401ee14cb6fe7e580ffc/7de2f62fcd9846bd0fb270435b35e876ec89ffc0cccbd5d68421de2ed905ef19/5b75b0de543fbaebb64903d26806e52cb0c4cd5e14dd0f16587ab1267aabc4d1

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:23: [Expected: 80, Actual: 1134]
- MD013:27: [Expected: 80, Actual: 1098]
- MD013:29: [Expected: 80, Actual: 700]
- MD013:33: [Expected: 80, Actual: 306]
- MD013:54: [Expected: 80, Actual: 184]
- MD033:56: [Element: details]
- MD013:59: [Expected: 80, Actual: 156]
- MD033:61: [Element: details]
- MD013:64: [Expected: 80, Actual: 207]
- MD013:69: [Expected: 80, Actual: 572]
- MD013:71: [Expected: 80, Actual: 721]
- MD013:75: [Expected: 80, Actual: 460]
- MD013:98: [Expected: 80, Actual: 163]
- MD033:100: [Element: details]
- MD013:103: [Expected: 80, Actual: 148]
- MD013:109: [Expected: 80, Actual: 444]
- MD013:111: [Expected: 80, Actual: 413]
- MD013:129: [Expected: 80, Actual: 166]
- MD033:131: [Element: details]
- MD013:138: [Expected: 80, Actual: 816]
- MD013:140: [Expected: 80, Actual: 260]
- MD013:150: [Expected: 80, Actual: 89]
- MD013:151: [Expected: 80, Actual: 157]
- MD013:153: [Expected: 80, Actual: 507]
- MD013:155: [Expected: 80, Actual: 315]
- MD013:159: [Expected: 80, Actual: 500]
- MD013:161: [Expected: 80, Actual: 391]
- MD013:163: [Expected: 80, Actual: 461]
- MD013:167: [Expected: 80, Actual: 410]
- MD013:169: [Expected: 80, Actual: 156]
- MD036:171:
- MD033:173: [Element: details]
- MD013:176: [Expected: 80, Actual: 205]
- MD013:180: [Expected: 80, Actual: 366]
- MD037:180:
- MD037:180:
- MD013:184: [Expected: 80, Actual: 543]
- MD013:186: [Expected: 80, Actual: 117]
- MD036:188:
- MD013:190: [Expected: 80, Actual: 730]
- MD013:194: [Expected: 80, Actual: 462]
- MD013:211: [Expected: 80, Actual: 158]
- MD033:213: [Element: details]
- MD036:218:
- MD013:222: [Expected: 80, Actual: 242]
- MD013:226: [Expected: 80, Actual: 661]
- MD013:228: [Expected: 80, Actual: 156]
- MD036:230:
- MD033:232: [Element: details]
- MD013:235: [Expected: 80, Actual: 161]
- MD013:239: [Expected: 80, Actual: 390]
- MD013:243: [Expected: 80, Actual: 511]
- MD013:245: [Expected: 80, Actual: 296]
- MD013:247: [Expected: 80, Actual: 380]
- MD013:255: [Expected: 80, Actual: 282]
- MD013:257: [Expected: 80, Actual: 405]
- MD013:259: [Expected: 80, Actual: 447]
- MD013:261: [Expected: 80, Actual: 336]
- MD013:265: [Expected: 80, Actual: 194]
- MD013:267: [Expected: 80, Actual: 152]
- MD040:296:
- MD040:326:
- MD013:340: [Expected: 80, Actual: 1113]
- MD025:342:
- MD034:344:
- MD013:346: [Expected: 80, Actual: 192]
- MD013:348: [Expected: 80, Actual: 130]
- MD013:350: [Expected: 80, Actual: 205]
- MD013:352: [Expected: 80, Actual: 170]
- MD013:354: [Expected: 80, Actual: 113]
- MD034:354:
- MD013:356: [Expected: 80, Actual: 159]
