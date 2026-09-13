# Conversion report — Interface_Segration_Principle.pdf

- job_id: cb9a1b2a-92ec-4b12-8d69-2fa96d9a4e93
- status: assembling
- pages: 13
- wall-clock: not started
- tokens: prompt=337526 completion=15075
- pipeline_version: 77ca3a05b80cc24b9f872d6b9b7d3a5a3e45d53f35b87e62d9835656f30dcc5e
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 93

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 95 | 0 | 200 | 11829 | 730 | False |
| 2 | verified | 98 | 0 | 200 | 12147 | 636 | False |
| 3 | verified | 97 | 1 | 300 | 32046 | 1670 | False |
| 4 | verified | 96 | 0 | 200 | 13334 | 714 | False |
| 5 | verified | 96 | 1 | 300 | 33324 | 1504 | False |
| 6 | needs_review | 90 | 2 | 400 | 52073 | 2337 | True |
| 7 | verified | 98 | 0 | 200 | 12927 | 627 | False |
| 8 | verified | 95 | 0 | 200 | 13252 | 771 | False |
| 9 | needs_review | 85 | 2 | 400 | 49070 | 1665 | True |
| 10 | needs_review | 92 | 2 | 400 | 49653 | 1828 | True |
| 11 | verified | 95 | 0 | 200 | 12676 | 595 | False |
| 12 | verified | 95 | 0 | 200 | 12944 | 741 | False |
| 13 | verified | 97 | 1 | 300 | 32251 | 1257 | False |

## needs_review pages

[6, 9, 10]

## Diagram → Mermaid conversion

- figures: 7
- converted to Mermaid: 7 (100%)
- data-table fallbacks: 0
- image fallbacks: 0

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 1 | 59 | classDiagram | mermaid | 92 |
| 3 | 60 | classDiagram | mermaid | 100 |
| 6 | 61 | classDiagram | mermaid | 92 |
| 7 | 62 | classDiagram | mermaid | 97 |
| 8 | 63 | classDiagram | mermaid | 95 |
| 9 | 64 | classDiagram | mermaid | 95 |
| 9 | 65 | classDiagram | mermaid | 95 |

## Omissions log

- page 1: - Source typo "Langage" preserved verbatim (DEC-009 allowance); correction would be "Language".
- Footnote 1 appears at bottom of page as a footnote tied to "GOF" superscript reference in Introduction.
- Sidebar diagram (Unified Notation 0.8) wrapped as figure placeholder; its text (Base Class, Derived 1, Derived 2, Had by Reference, Had By Value, Used) is contained in the figure.
- No uncertain characters.
- page 2: - Corrected "interfacse" to "interfaces" in the second paragraph under Introduction continuation.
- Kept source typos per DEC-009: "Regsiter" (Listing 2, should be "Register") and "the a 'fat' interface" in the following paragraph. "Regsiter" appears verbatim in both image and OCR reference.
- "whethere" in the image ("know whethere they are open") — OCR reference reads "whether"; corrected to "whether".
- Running header "Interface Pollution" and page number "2" excluded from body.
- page 3: - Corrected "lan- guates" to "languages"; "noti ed" to "notified" (ligature fi).
- Figure 1 caption was printed above the diagram in the source; transcribed as caption below the figure placeholder.
- Figure coordinates are approximate based on rendered page layout.
- "nil" rendered as italic in source.
- page 4: - Typo "complely" left as in source per DEC-009? Corrected? No — retained verbatim; log only corrections made. "Regsiter" (Listing 3) retained as in source, matching Listing 2 spelling. No figures on this page. Page continues mid-sentence into next page ("chills customers...").
- page 5: - Corrected source typo "unerlated" → "unerlated" kept? Left as in source; flagging: "unerlated" appears in source, likely "unrelated" [?]. Per DEC-009 allowance it was left verbatim; log as candidate correction.
- Small-caps rendering of "Clients should not be forced..." normalized to uppercase italic blockquote as in source emphasis.
- No figures on this page. Continuation paragraph at top ("and managers to the bone...") continues from page 4.
- "significant" rendered with fi ligature in source, transcribed as standard "significant".
- page 6: verification cap reached
- page 7: - Code block at top of page is a continuation of Listing 4 from previous page.
- OCR source shows "class form" as "class form" (sic); normalized spacing of small-caps "ADAPTER".
- Figure caption "Figure 3 / Multiply Inherited Timed Door" appears above the diagram in the source; rendered as caption below placeholder. No typos requiring correction on this page.
- page 8: Verbatim typos retained per DEC-009: "encasulated", "WithdrawlTransaction", "precicely", "coresponding", "induvidual", "many different language". Figure 4 diagram rendered as placeholder; its caption "Figure 4 / ATM UI Hierarchy" appears above the diagram in source. Figure number indexing restarts at 1 for this page.
- page 9: coverage floor failed: judge score alone is insufficient
- page 10: verification cap reached
- page 11: - Continuing Listing 6/8 code across page boundaries; first block is the tail of Listing 6 (UI class), final block is the tail of Listing 8.
- "Seperate Global Pointers" and "WithdrawlTransation"/"class class" left as in source (DEC-009 typo allowance).
- No figures on this page.
- page 12: - Page continues Listing 8 code from previous page (opening code block).
- Source typo "transfer" missing semicolon in Listing 9 left verbatim per DEC-009.
- "Withdrawl" spellings preserved as in source.
- Inline code in prototype sentences rendered as code spans for readability; text verbatim.
- page 13: - Page continues from previous page (mid-paragraph "changed, ..."); paragraph continues under the heading "The Polyad vs. the Monad." from page 12.
- Kept source typo "beween" (for "between") per verbatim rule; flagged here as an observed typo.
- "ADAPTER" rendered in small caps in source; transcribed as ADAPTER.
- Running header "13 : The Interface Segregation Principle" and page number 13 excluded from body.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 253832B model=glm-5.3-flash effort=low transcribe_ms=7254.2 verify_ms=2668.3 ocr_ms=90.2 retries=0 verification_score=95 floor=88% hashes=b6eb389b264461b7f7d787aa91982b9e960c14e764c87235d0704707eac08e9c/c38751119d34babbcbe94a1d5bd5524a96a496f56dfde7926181c5f9de16ea22/5796a7dae011a39d7ac56c1346aef508be73c11e4cde13b7647626f6d38da90c/2d5d577c303686ec5cbee35a13a66b3755da11c114a6642fe3db821c44ac9273
- page 2: dpi=200 image=1700x2200 220419B model=glm-5.3-flash effort=low transcribe_ms=5655.6 verify_ms=2880.5 ocr_ms=90.2 retries=0 verification_score=98 floor=98% hashes=aa962e1f20cb76bbdc8c73d8ac80e490a289e983750773057222fc72be44878b/1c72812c2089d9d243fe3d65de4d9cd4fb1a31d6c123af11b9501198cce407d5/3c3ad49ae4f217d4bfd47acb582f48961a8e2e8189a6d002bc3a7a4869345b82/bf358842eb03fe51344c79c297eb96273a59a4fe7cd0c67fc7587d654b24d7e0
- page 3: dpi=300 image=2550x3300 423825B model=glm-5.3-flash effort=low transcribe_ms=23847.3 verify_ms=6722.6 ocr_ms=701.2 retries=1 verification_score=97 floor=95% hashes=13a8b8dd7bc4b0681fad4b130213a25af4fe886f3f345f035ae533c8bd4c952a/894eb63718018cc1369763c3dafd54b5dbd70929c89801e7d516dab7abfb671d/c43ba2a46738e04540c71c3c1673a76a55f642fa5b730bc65206031d932bba43/dc1091ba184a78b1c574534ff8c893d8e3eaf26ebb69a7aa7546391e8c8c3a24
- page 4: dpi=200 image=1700x2200 270889B model=glm-5.3-flash effort=low transcribe_ms=4825.4 verify_ms=3700.5 ocr_ms=352.7 retries=0 verification_score=96 floor=98% hashes=5138fea3d81fb0ebadbe795fc0f4936b368ccae9d0abac5e5811fd38cc6fe3cc/ac6ab4604fc3e84a193594b1946a96c59564f734c04b72c9cd9a13a31e732dad/0eee0b505484e4f8f3b351c0b7a9d096f43108b474809bc6a6e4cf9d2db8200d/89ec5a4e3923eb45f706079e5cffa1723fe38a319d404dba8b4b7c97092e26e4
- page 5: dpi=300 image=2550x3300 433927B model=glm-5.3-flash effort=low transcribe_ms=17200.7 verify_ms=7606.7 ocr_ms=922.7 retries=1 verification_score=96 floor=96% hashes=7718a7b9512e369c156f5f538d8f78509a25d7e83ac8918d0fad600311ded967/bc57726fcd9b2a182219967750ab6754ce5f62a1448765b7c35fa978b02e1079/b25061d33f8b3a1086bf5dffa743c27a1595ec6774f50e99a33f681749de1735/ae56602cdb6ff1035e98f8264097c6e9213b9071ec273577e06e21afc8478314
- page 6: dpi=400 image=3400x4400 405050B model=glm-5.3-flash effort=low transcribe_ms=20156.3 verify_ms=14181.4 ocr_ms=2034.1 retries=2 verification_score=90 floor=96% hashes=5bf8bf6c9b4419b3a7ae526057b0d1766cb190966530e13bc0bfb084456bcfe9/7adfc57e36ed75ada04027d760589f105a5a0047c8b4fbf4f832b458b5ee910d/21bfbe94bacbe0cf7a85573f94666b3cfee1ddd2c9ee999baa4ecff99e199c7c/384a8ae9fb6770dc8ade9e96638136453ebfb0529df53c4c731497a4b7c4dee6
- page 7: dpi=200 image=1700x2200 186617B model=glm-5.3-flash effort=low transcribe_ms=7567.7 verify_ms=3239.8 ocr_ms=320.5 retries=0 verification_score=98 floor=96% hashes=ce7df1de0cea6c9cd4a2aa1b82b7c76de044a8db83752b43ba31c385c07d86ec/e25f5994d42b1cb4328f2cd879e4a2bd9c30949006158cfe17feaa5ce6ee8847/1d3a170c26d76351c7a9bc007cfa64c1929d9ce7511812c2d0ff71f253650f27/e70bc7cbb0dce891420bf134b91470ccc4e3379461a7a8513aee32a034c1ef8c
- page 8: dpi=200 image=1700x2200 271106B model=glm-5.3-flash effort=low transcribe_ms=8786.6 verify_ms=3978.2 ocr_ms=313.5 retries=0 verification_score=95 floor=95% hashes=bb87273df09fd0d312be1a282689880b9792747cc8ebcfef1400f7b48e1dacd0/400d7d5a6b16bf0da143f898d569cb858e5f2224bfe0c16eda020d049b67f8ed/84b4fc6f64b6cc1bf927f2301b1d4673a8a038911a27b50d510e389df4e3f56e/a32feca94e3b9d2b493170ac84c2c15c4b99b990073c33c6119b30514f7b3edb
- page 9: dpi=400 image=3400x4400 219953B model=glm-5.3-flash effort=low transcribe_ms=22825.0 verify_ms=11768.1 ocr_ms=1801.3 retries=2 verification_score=85 floor=65% hashes=74eb3eab567879c24358f8865f2fda76ead213176ae8c590a0a4cf006fc15b4a/0741cb6c6c55bd3e10d54e05d988f7227f2883d07a27ade703ced8ec33cfcd03/9f409987cdb1ff3b46198f01651b5244b96a6ab17461a8495e8061e4f3c515f5/4d0b7fd058406c6843629fe5d6f6f3a9b29d3c059774196f52806dc4d58a01a6
- page 10: dpi=400 image=3400x4400 307353B model=glm-5.3-flash effort=low transcribe_ms=30325.6 verify_ms=18042.4 ocr_ms=1641.1 retries=2 verification_score=92 floor=93% hashes=2eab2383ad69292d86ead21ab0cae3ed46c3e1270db1777b5cf0ea22031e7e05/60a26bebe0442d2748a72165f7ecafd8799db8e13a388cc066f66c853efc084c/363e6070b6e85934e720251742009c984cff44f2ae193068940c78044d2cd200/bb06d7033d6ea5d05adabd4b08a46a1f69e1f9674291012fe1789b8ed8437be3
- page 11: dpi=200 image=1700x2200 229461B model=glm-5.3-flash effort=low transcribe_ms=6924.0 verify_ms=3711.5 ocr_ms=326.6 retries=0 verification_score=95 floor=98% hashes=a06a13eb12f0a9b16e68488f14d3042f1598d41306b05fc01cf3e369472a171d/61fdf5d60ca904dae251bf7e84b9a43cbe82b06bb2ad92cb03621d5ab442e958/dc8af4ca14d96b1dd0cb62ef4b2aab3267078021ae9d20cba162a14aa0f6fb6f/4503d0a706169fcbdc4bccaac56c4f52753391f9f305b13a5b129cbf37281fec
- page 12: dpi=200 image=1700x2200 257385B model=glm-5.3-flash effort=low transcribe_ms=7860.3 verify_ms=3475.5 ocr_ms=339.5 retries=0 verification_score=95 floor=97% hashes=5421c2e6d32f163bc3d95029e7f8b668c34523de90c68cfbb049a46ffa5b18d6/9792fa1a5b79dfe242589c8c3829968314323245df5c5d3cc441c63f5997b09e/ff03a2817a8ca40d3a14edd0740c8807a38671e577151c9cc47ed8d2a34524ca/3ff1ef28a49bc7a191a6c4294cf13d30053a34f82a3b39962975d5cdf4c78a93
- page 13: dpi=300 image=2550x3300 331996B model=glm-5.3-flash effort=low transcribe_ms=17226.6 verify_ms=6561.0 ocr_ms=952.3 retries=1 verification_score=97 floor=95% hashes=4ba4522da77aa43b21879092b58161642b405c95b78826981986acd08fec0fad/5285936cc2920c05c7a2fef782bbfd9a599ee095787ee10bd77520d676ba7889/831fa43579c4a3f70d2e1eefae73b1fd5e00372cdd345bb71b07fc2d1c3a81a0/ef9914c6b371e8ad99739d640eb072788fcab25f5216716f165104c394acf47e

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:18: [Expected: 80, Actual: 495]
- MD013:29: [Expected: 80, Actual: 201]
- MD033:31: [Element: details]
- MD013:34: [Expected: 80, Actual: 156]
- MD036:36:
- MD033:38: [Element: details]
- MD013:41: [Expected: 80, Actual: 236]
- MD013:48: [Expected: 80, Actual: 798]
- MD013:50: [Expected: 80, Actual: 264]
- MD013:54: [Expected: 80, Actual: 223]
- MD013:56: [Expected: 80, Actual: 346]
- MD013:58: [Expected: 80, Actual: 302]
- MD013:62: [Expected: 80, Actual: 163]
- MD013:77: [Expected: 80, Actual: 156]
- MD013:79: [Expected: 80, Actual: 230]
- MD013:97: [Expected: 80, Actual: 260]
- MD013:99: [Expected: 80, Actual: 375]
- MD013:108: [Expected: 80, Actual: 147]
- MD033:110: [Element: details]
- MD036:115:
- MD036:119:
- MD013:121: [Expected: 80, Actual: 525]
- MD013:123: [Expected: 80, Actual: 530]
- MD013:125: [Expected: 80, Actual: 535]
- MD025:127:
- MD026:127:
- MD013:129: [Expected: 80, Actual: 330]
- MD026:131:
- MD013:133: [Expected: 80, Actual: 391]
- MD013:135: [Expected: 80, Actual: 526]
- MD013:137: [Expected: 80, Actual: 295]
- MD013:158: [Expected: 80, Actual: 454]
- MD013:160: [Expected: 80, Actual: 247]
- MD026:162:
- MD013:164: [Expected: 80, Actual: 646]
- MD025:166:
- MD013:170: [Expected: 80, Actual: 547]
- MD025:172:
- MD013:174: [Expected: 80, Actual: 375]
- MD013:176: [Expected: 80, Actual: 209]
- MD025:178:
- MD013:180: [Expected: 80, Actual: 217]
- MD013:182: [Expected: 80, Actual: 265]
- MD013:201: [Expected: 80, Actual: 195]
- MD033:203: [Element: details]
- MD013:206: [Expected: 80, Actual: 156]
- MD036:208:
- MD033:210: [Element: details]
- MD013:213: [Expected: 80, Actual: 146]
- MD036:218:
- MD013:220: [Expected: 80, Actual: 433]
- MD029:243: [Expected: 1; Actual: 2; Style: 1/2/3]
- MD013:251: [Expected: 80, Actual: 375]
- MD025:253:
- MD013:255: [Expected: 80, Actual: 370]
- MD013:267: [Expected: 80, Actual: 160]
- MD033:269: [Element: details]
- MD036:274:
- MD013:291: [Expected: 80, Actual: 343]
- MD025:293:
- MD013:295: [Expected: 80, Actual: 514]
- MD013:310: [Expected: 80, Actual: 139]
- MD033:312: [Element: details]
- MD013:315: [Expected: 80, Actual: 112]
- MD036:317:
- MD013:324: [Expected: 80, Actual: 524]
- MD013:326: [Expected: 80, Actual: 399]
- MD013:328: [Expected: 80, Actual: 289]
- MD013:330: [Expected: 80, Actual: 424]
- MD013:357: [Expected: 80, Actual: 194]
- MD033:359: [Element: details]
- MD013:362: [Expected: 80, Actual: 156]
- MD036:364:
- MD033:366: [Element: details]
- MD013:369: [Expected: 80, Actual: 137]
- MD013:396: [Expected: 80, Actual: 134]
- MD033:398: [Element: details]
- MD013:401: [Expected: 80, Actual: 156]
- MD036:403:
- MD033:405: [Element: details]
- MD013:408: [Expected: 80, Actual: 178]
- MD013:505: [Expected: 80, Actual: 501]
- MD013:519: [Expected: 80, Actual: 549]
- MD013:551: [Expected: 80, Actual: 700]
- MD025:578:
- MD026:578:
- MD013:580: [Expected: 80, Actual: 281]
- MD013:582: [Expected: 80, Actual: 289]
- MD013:584: [Expected: 80, Actual: 166]
- MD013:586: [Expected: 80, Actual: 481]
- MD025:588:
- MD013:590: [Expected: 80, Actual: 453]
- MD013:592: [Expected: 80, Actual: 701]
