# Conversion report — Interface_Segration_Principle.pdf

- job_id: 1d223786-45ae-411f-8b55-02132e49028e
- status: assembling
- pages: 13
- wall-clock: not started
- tokens: prompt=356033 completion=17450
- pipeline_version: 9c215872aa0b575aade8ae9fb73a81b65c9fb7d96e9934b244133c2636e44bc0
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 99

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 95 | 2 | 400 | 48185 | 2166 | False |
| 2 | verified | 97 | 0 | 200 | 12146 | 625 | False |
| 3 | needs_review | 90 | 2 | 400 | 51864 | 3565 | True |
| 4 | verified | 95 | 1 | 300 | 32998 | 1556 | False |
| 5 | verified | 95 | 0 | 200 | 13478 | 746 | False |
| 6 | needs_review | 82 | 2 | 400 | 52042 | 2411 | True |
| 7 | verified | 95 | 0 | 200 | 12911 | 756 | False |
| 8 | verified | 95 | 0 | 200 | 13233 | 797 | False |
| 9 | needs_review | 85 | 2 | 400 | 49019 | 1741 | True |
| 10 | verified | 95 | 0 | 200 | 12294 | 476 | False |
| 11 | verified | 95 | 0 | 200 | 12675 | 616 | False |
| 12 | verified | 97 | 0 | 200 | 12944 | 745 | False |
| 13 | verified | 95 | 1 | 300 | 32244 | 1250 | False |

## needs_review pages

[3, 6, 9]

## Diagram → Mermaid conversion

- figures: 7
- converted to Mermaid: 7 (100%)
- data-table fallbacks: 0
- image fallbacks: 0

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 1 | 99 | classDiagram | mermaid | 95 |
| 3 | 100 | classDiagram | mermaid | 100 |
| 6 | 101 | classDiagram | mermaid | 95 |
| 7 | 102 | classDiagram | mermaid | 100 |
| 8 | 103 | classDiagram | mermaid | 95 |
| 9 | 104 | classDiagram | mermaid | 95 |
| 9 | 105 | classDiagram | mermaid | 95 |

## Omissions log

- page 1: - Corrected "uniﬁed" ligature to "unified"; source typo "Langage" left as-is (verbatim).
- Small-caps "TEMPLATE METHOD" rendered as regular caps.
- Footnote 1 kept in body at page bottom.
- Sidebar diagram replaced with figure placeholder; its text (Base Class, Derived 1, Derived 2, Had by Reference, Had By Value, Used) is contained in the figure.
- page 2: - Corrected "interfacse" to "interfaces" (source typo).
- Kept source typos per DEC-009 where not obviously OCR-introduced: "the a 'fat' interface", "Regsiter" (source typo in code, left verbatim).
- "Interface Pollution" running header and page number "2" excluded from body.
- No figures on this page (previous page's figure belongs to page 1).
- page 3: verification cap reached
- page 4: Page continues prior page's "Interface Pollution" section. Body ends mid-sentence ("chills customers") continuing onto next page. Source typo "complely" left as-is per verbatim transcription of OCR; "Regsiter" left as-is (matches source listing from prior page). No figures on this page.
- page 5: - Page continues the previous paragraph ("...chills customers" → "and managers to the bone.") from page 4.
- Corrected "unerlated" → "unrelated" (OCR typo).
- Corrected "couplings" (OCR shows "couplings"; kept as printed since it matches rolling context usage).
- Running header "5 : The Interface Segregation Principle" and page number excluded from body.
- Block quote is a styled pull-quote of the ISP principle in the original.
- page 6: verification cap reached
- page 7: - Page begins with the tail of the Listing 4 code block continued from previous page.
- ADAPTER rendered in small caps in source; transcribed as plain text.
- "class form" is italic in source.
- Figure 3 caption ("Figure 3 / Multiply Inherited Timed Door") included as figure caption, not body text.
- page 8: - Header "The ATM User Interface Example" and page number 8 excluded from body.
- Typos preserved per DEC-009 where ambiguous; source spellings retained: "encasulated" (encapsulated), "Withdrawl" (Withdrawal), "precicely" (precisely), "coresponding" (corresponding), "induvidual" (individual), "language" (languages). Logged, not corrected, to preserve verbatim source.
- Figure 4 diagram rendered as figure placeholder; caption kept in body text.
- page 9: coverage floor failed: judge score alone is insufficient
- page 10: - Continuation of Listing 6 from page 9; code block continues onto next page (ends mid-declaration "class UI : public DepositUI,").
- "class class" and "Transation" typos left as in source per DEC-009 (verbatim code); "Withdrawl" spelling left as in source.
- No figures on this page.
- page 11: - Continues Listing 6 from previous page (opening of UI class, "class UI : public DepositUI," on page 10).
- "Seperate Global Pointers" (Listing 8 title): source typo retained per DEC-009.
- "class class WithdrawlTransation" and "WithdrawlUI/GwithdrawlUI" spellings retained from source; "idom" corrected to "idiom" in body text.
- Code blocks are set in a monospace font in the source; body text regular.
- page 12: - Continuing code block from Listing 8 (previous page); first lines are the tail of the WithdrawlTransaction class.
- Source header "The Polyad vs. the Monad." ends with a period; retained.
- Missing semicolon after "static TransferUI& transfer" retained as in source.
- OCR curly quotes in #include lines normalized to straight quotes.
- Page ends mid-sentence, continues on page 13.
- page 13: - Corrected "beween" -> "between" (DEC-009).
- Page begins mid-sentence, continuing the "Polyad vs. Monad" section from page 12.
- Running header "13 : The Interface Segregation Principle" excluded from body per rules; recorded in FURNITURE.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=400 image=3400x4400 501700B model=glm-5.3-flash effort=low transcribe_ms=25590.8 verify_ms=12304.0 ocr_ms=1778.6 retries=2 verification_score=95 floor=88% hashes=b6eb389b264461b7f7d787aa91982b9e960c14e764c87235d0704707eac08e9c/b07aa574ea193d04e481c9cb11c32ba312aa1b0cd098d75deb2b7be790cff3cf/5796a7dae011a39d7ac56c1346aef508be73c11e4cde13b7647626f6d38da90c/bc4704555366f91d3db02c63621ada7fd5bb5bb32721e978b82369b931b9b848
- page 2: dpi=200 image=1700x2200 220419B model=glm-5.3-flash effort=low transcribe_ms=7593.9 verify_ms=3641.7 ocr_ms=313.5 retries=0 verification_score=97 floor=98% hashes=aa962e1f20cb76bbdc8c73d8ac80e490a289e983750773057222fc72be44878b/1c72812c2089d9d243fe3d65de4d9cd4fb1a31d6c123af11b9501198cce407d5/3c3ad49ae4f217d4bfd47acb582f48961a8e2e8189a6d002bc3a7a4869345b82/4ec50117c568a41a0351d0d9c107aece75756c79bb0ad7adb1c6b5ef4677dbf8
- page 3: dpi=400 image=3400x4400 492228B model=glm-5.3-flash effort=low transcribe_ms=33383.7 verify_ms=14474.3 ocr_ms=1941.8 retries=2 verification_score=90 floor=95% hashes=13a8b8dd7bc4b0681fad4b130213a25af4fe886f3f345f035ae533c8bd4c952a/85e15199b8328b516f2fee9f621c9b80e2ea4ad2e4a827bf21fdd869d1c0f2db/c43ba2a46738e04540c71c3c1673a76a55f642fa5b730bc65206031d932bba43/3565b7cdf6584c813a0b62647e14739f065b8358b7a78c76ddd5c69f7c368947
- page 4: dpi=300 image=2550x3300 434370B model=glm-5.3-flash effort=low transcribe_ms=12955.2 verify_ms=9920.2 ocr_ms=969.0 retries=1 verification_score=95 floor=98% hashes=5138fea3d81fb0ebadbe795fc0f4936b368ccae9d0abac5e5811fd38cc6fe3cc/9202f37c187649d9890fc7bfdfdfd57e48c624da2f9deb9613f9c052f969e112/0eee0b505484e4f8f3b351c0b7a9d096f43108b474809bc6a6e4cf9d2db8200d/bcf9c80a92c0a4c15b10c50583fc72c1bc6f7f60af81eb6cee097df64130b131
- page 5: dpi=200 image=1700x2200 268374B model=glm-5.3-flash effort=low transcribe_ms=6198.5 verify_ms=3294.7 ocr_ms=339.9 retries=0 verification_score=95 floor=95% hashes=7718a7b9512e369c156f5f538d8f78509a25d7e83ac8918d0fad600311ded967/d4ffe70e1cdfed5f6970bb252464ee8144c2d01027c16f0410afa76d88d149b6/b25061d33f8b3a1086bf5dffa743c27a1595ec6774f50e99a33f681749de1735/fe72d0598664c84e08295089a4e559814dfae9ffbc7f1d873115c6bc81095dd2
- page 6: dpi=400 image=3400x4400 405050B model=glm-5.3-flash effort=low transcribe_ms=21660.3 verify_ms=14728.1 ocr_ms=1977.2 retries=2 verification_score=82 floor=96% hashes=5bf8bf6c9b4419b3a7ae526057b0d1766cb190966530e13bc0bfb084456bcfe9/7adfc57e36ed75ada04027d760589f105a5a0047c8b4fbf4f832b458b5ee910d/21bfbe94bacbe0cf7a85573f94666b3cfee1ddd2c9ee999baa4ecff99e199c7c/19ca1c826c56bec2c31e27f00877443ea2104bfde5c4dd53ade8612f4a4a07f5
- page 7: dpi=200 image=1700x2200 186617B model=glm-5.3-flash effort=low transcribe_ms=7141.8 verify_ms=5379.8 ocr_ms=295.1 retries=0 verification_score=95 floor=94% hashes=ce7df1de0cea6c9cd4a2aa1b82b7c76de044a8db83752b43ba31c385c07d86ec/e25f5994d42b1cb4328f2cd879e4a2bd9c30949006158cfe17feaa5ce6ee8847/1d3a170c26d76351c7a9bc007cfa64c1929d9ce7511812c2d0ff71f253650f27/f1f5edfd9f4eb2222796e727638184dd3f96b352b7ea62ec5ae908655620c3b0
- page 8: dpi=200 image=1700x2200 271106B model=glm-5.3-flash effort=low transcribe_ms=8246.5 verify_ms=4340.6 ocr_ms=336.0 retries=0 verification_score=95 floor=95% hashes=bb87273df09fd0d312be1a282689880b9792747cc8ebcfef1400f7b48e1dacd0/400d7d5a6b16bf0da143f898d569cb858e5f2224bfe0c16eda020d049b67f8ed/84b4fc6f64b6cc1bf927f2301b1d4673a8a038911a27b50d510e389df4e3f56e/f96b110bd915e06f0b7f8e44d748b507c6529237e0c3d44de4196bdfbcd87aee
- page 9: dpi=400 image=3400x4400 219953B model=glm-5.3-flash effort=low transcribe_ms=21530.1 verify_ms=11153.9 ocr_ms=1791.3 retries=2 verification_score=85 floor=65% hashes=74eb3eab567879c24358f8865f2fda76ead213176ae8c590a0a4cf006fc15b4a/0741cb6c6c55bd3e10d54e05d988f7227f2883d07a27ade703ced8ec33cfcd03/9f409987cdb1ff3b46198f01651b5244b96a6ab17461a8495e8061e4f3c515f5/dc32049a3cef325cc7c89c12aa8b4ac71bb7a65d08c987be11aa9b1952b1e758
- page 10: dpi=200 image=1700x2200 154367B model=glm-5.3-flash effort=low transcribe_ms=5103.9 verify_ms=2524.2 ocr_ms=287.1 retries=0 verification_score=95 floor=93% hashes=2eab2383ad69292d86ead21ab0cae3ed46c3e1270db1777b5cf0ea22031e7e05/e78ac1f577e7809ad31423e1068d19a51dcbafe0fdd63a0c9a02c58ea15023cb/363e6070b6e85934e720251742009c984cff44f2ae193068940c78044d2cd200/bb06d7033d6ea5d05adabd4b08a46a1f69e1f9674291012fe1789b8ed8437be3
- page 11: dpi=200 image=1700x2200 229461B model=glm-5.3-flash effort=low transcribe_ms=7994.3 verify_ms=2854.7 ocr_ms=316.9 retries=0 verification_score=95 floor=98% hashes=a06a13eb12f0a9b16e68488f14d3042f1598d41306b05fc01cf3e369472a171d/61fdf5d60ca904dae251bf7e84b9a43cbe82b06bb2ad92cb03621d5ab442e958/dc8af4ca14d96b1dd0cb62ef4b2aab3267078021ae9d20cba162a14aa0f6fb6f/8a63cedde72527fb54af0673fea739b44afa7d1d6f51c9abbb318b6adc2315f0
- page 12: dpi=200 image=1700x2200 257385B model=glm-5.3-flash effort=low transcribe_ms=9309.3 verify_ms=3591.0 ocr_ms=350.3 retries=0 verification_score=97 floor=97% hashes=5421c2e6d32f163bc3d95029e7f8b668c34523de90c68cfbb049a46ffa5b18d6/9792fa1a5b79dfe242589c8c3829968314323245df5c5d3cc441c63f5997b09e/ff03a2817a8ca40d3a14edd0740c8807a38671e577151c9cc47ed8d2a34524ca/d8a074417b8409fa55bc0cca0426ec458d7028d30ed45c080081746b8d9c16b9
- page 13: dpi=300 image=2550x3300 331996B model=glm-5.3-flash effort=low transcribe_ms=13369.1 verify_ms=13608.0 ocr_ms=864.6 retries=1 verification_score=95 floor=94% hashes=4ba4522da77aa43b21879092b58161642b405c95b78826981986acd08fec0fad/5285936cc2920c05c7a2fef782bbfd9a599ee095787ee10bd77520d676ba7889/831fa43579c4a3f70d2e1eefae73b1fd5e00372cdd345bb71b07fc2d1c3a81a0/3deb1e4c397ea3bf9c49700b189fc74112aa06fb241e577259db44c538ef267d

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:18: [Expected: 80, Actual: 495]
- MD013:35: [Expected: 80, Actual: 188]
- MD033:37: [Element: details]
- MD013:40: [Expected: 80, Actual: 156]
- MD036:42:
- MD033:44: [Element: details]
- MD013:47: [Expected: 80, Actual: 222]
- MD013:54: [Expected: 80, Actual: 796]
- MD013:56: [Expected: 80, Actual: 264]
- MD013:60: [Expected: 80, Actual: 223]
- MD013:62: [Expected: 80, Actual: 346]
- MD013:64: [Expected: 80, Actual: 302]
- MD013:68: [Expected: 80, Actual: 163]
- MD036:70:
- MD013:84: [Expected: 80, Actual: 156]
- MD013:86: [Expected: 80, Actual: 230]
- MD036:88:
- MD013:105: [Expected: 80, Actual: 260]
- MD013:107: [Expected: 80, Actual: 375]
- MD013:115: [Expected: 80, Actual: 116]
- MD033:117: [Element: details]
- MD013:127: [Expected: 80, Actual: 525]
- MD013:129: [Expected: 80, Actual: 530]
- MD013:131: [Expected: 80, Actual: 535]
- MD025:133:
- MD026:133:
- MD013:135: [Expected: 80, Actual: 330]
- MD026:137:
- MD013:139: [Expected: 80, Actual: 391]
- MD013:141: [Expected: 80, Actual: 526]
- MD013:143: [Expected: 80, Actual: 295]
- MD036:145:
- MD013:164: [Expected: 80, Actual: 454]
- MD013:166: [Expected: 80, Actual: 247]
- MD026:168:
- MD013:170: [Expected: 80, Actual: 646]
- MD025:172:
- MD013:176: [Expected: 80, Actual: 547]
- MD025:178:
- MD013:180: [Expected: 80, Actual: 375]
- MD013:182: [Expected: 80, Actual: 209]
- MD025:184:
- MD013:186: [Expected: 80, Actual: 219]
- MD013:188: [Expected: 80, Actual: 265]
- MD013:208: [Expected: 80, Actual: 217]
- MD033:210: [Element: details]
- MD013:213: [Expected: 80, Actual: 156]
- MD036:215:
- MD033:217: [Element: details]
- MD013:220: [Expected: 80, Actual: 146]
- MD013:225: [Expected: 80, Actual: 433]
- MD036:227:
- MD029:249: [Expected: 1; Actual: 2; Style: 1/2/3]
- MD013:257: [Expected: 80, Actual: 375]
- MD025:259:
- MD013:261: [Expected: 80, Actual: 370]
- MD013:272: [Expected: 80, Actual: 144]
- MD033:274: [Element: details]
- MD036:279:
- MD036:283:
- MD013:295: [Expected: 80, Actual: 343]
- MD025:297:
- MD013:299: [Expected: 80, Actual: 514]
- MD013:314: [Expected: 80, Actual: 143]
- MD033:316: [Element: details]
- MD013:319: [Expected: 80, Actual: 118]
- MD036:321:
- MD013:328: [Expected: 80, Actual: 524]
- MD013:330: [Expected: 80, Actual: 399]
- MD013:332: [Expected: 80, Actual: 289]
- MD013:334: [Expected: 80, Actual: 424]
- MD013:364: [Expected: 80, Actual: 168]
- MD033:366: [Element: details]
- MD013:369: [Expected: 80, Actual: 156]
- MD036:371:
- MD033:373: [Element: details]
- MD013:376: [Expected: 80, Actual: 157]
- MD013:401: [Expected: 80, Actual: 200]
- MD033:403: [Element: details]
- MD013:406: [Expected: 80, Actual: 156]
- MD036:408:
- MD033:410: [Element: details]
- MD013:413: [Expected: 80, Actual: 196]
- MD036:420:
- MD013:510: [Expected: 80, Actual: 501]
- MD036:512:
- MD013:525: [Expected: 80, Actual: 549]
- MD036:527:
- MD013:557: [Expected: 80, Actual: 700]
- MD036:559:
- MD025:586:
- MD026:586:
- MD013:588: [Expected: 80, Actual: 281]
- MD013:590: [Expected: 80, Actual: 289]
- MD013:592: [Expected: 80, Actual: 166]
- MD013:594: [Expected: 80, Actual: 481]
- MD025:596:
- MD013:598: [Expected: 80, Actual: 454]
- MD013:600: [Expected: 80, Actual: 701]
