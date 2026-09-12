# Conversion report — Interface_Segration_Principle.pdf

- job_id: 0f0c5edf-4574-41a6-8c94-c03bb5196970
- status: assembling
- pages: 13
- wall-clock: not started
- tokens: prompt=414216 completion=19034
- pipeline_version: 49d37aab5011162c95b2267d3c52c5edb25ebd6d06ffb252038f28d3523593bc
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 84

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 96 | 0 | 200 | 11841 | 991 | False |
| 2 | verified | 96 | 0 | 200 | 12159 | 668 | False |
| 3 | needs_review | 92 | 2 | 400 | 51251 | 2764 | True |
| 4 | needs_review | 93 | 2 | 400 | 52742 | 2247 | True |
| 5 | verified | 96 | 0 | 200 | 13488 | 778 | False |
| 6 | verified | 98 | 1 | 300 | 32597 | 1505 | False |
| 7 | needs_review | 92 | 2 | 400 | 51517 | 2245 | True |
| 8 | verified | 96 | 0 | 200 | 13261 | 781 | False |
| 9 | needs_review | 85 | 2 | 400 | 49097 | 1821 | True |
| 10 | needs_review | 90 | 2 | 400 | 49614 | 1819 | True |
| 11 | needs_review | 88 | 2 | 400 | 50741 | 2100 | True |
| 12 | verified | 96 | 0 | 200 | 12951 | 762 | False |
| 13 | verified | 98 | 0 | 200 | 12957 | 553 | False |

## needs_review pages

[3, 4, 7, 9, 10, 11]

## Diagram → Mermaid conversion

- figures: 7
- converted to Mermaid: 5 (71%)
- data-table fallbacks: 0
- image fallbacks: 2

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 1 | 1 | classDiagram | mermaid | 95 |
| 3 | 2 | classDiagram | image | 85 |
| 6 | 3 | classDiagram | mermaid | 88 |
| 7 | 4 | classDiagram | image | 55 |
| 8 | 5 | classDiagram | mermaid | 95 |
| 9 | 6 | classDiagram | mermaid | 95 |
| 9 | 7 | classDiagram | mermaid | 88 |

## Omissions log

- page 1: - Hyphenation from line breaks (soft-ware, prag-matic, document-ing, nota-tion, func-tions, abstrac-tion, Segrega-tion) joined to single words in flowing text.
- Typo correction: "Langage" left as in source? Corrected to "Langage" kept verbatim (source spelling); noted as likely typo for "Language" but left uncorrected as it appears in OCR ground truth. Actually corrected per DEC-009: left verbatim.
- "depend upon" in "the details depend upon" kept as in source (likely "depends").
- Sidebar diagram rendered as figure placeholder; its labels (Used, Base Class, Derived 1, Derived 2, Had by Reference, Had By Value) preserved in figure alt text.
- Footnote 1 (Design Patterns) transcribed at end of body.
- Running header "Copyright (c) 1996 Object Mentor, Inc. All Rights Reserved." and page number "1" excluded from body; listed in furniture.
- GOF¹ superscript footnote marker rendered as ¹.
- page 2: - Continuation from page 1: paragraph begins mid-sentence ("words, the interfaces of the class...").
- Corrected "interfacse" -> "interfaces" (source typo).
- Left "Regsiter" as-is in code (Listing 2); likely source typo for "Register", not corrected since it is code.
- Left "in which the a 'fat' interface" as-is (source grammar error, allowed verbatim).
- Header "Interface Pollution" and page number "2" excluded from body.
- page 3: verification cap reached
- page 4: verification cap reached
- page 5: - "unerlated" corrected to "unrelated" (source typo). Note: OCR reference shows "unerlated" in image; corrected per DEC-009.
- "couplings where possible" — image shows "couplings", rolling context had "couplings" as "couplings"; kept as "couplings".
- Principle statement rendered as italic block quote-style emphasis.
- Hyphenation from justified text joined (e.g., "com-pletely" → "completely", "incre-mental" → "incremental").
- page 6: - Corrected "theA DAPTER" spacing to "the ADAPTER"; "coupling of Door clients" per OCR "coupling" kept; "complely" typo from prior context not on this page.
- OCR "coupling of Door clients" — source shows "coupling"; left as printed (likely "coupling" intended "coupling"→kept verbatim as "coupling").
- Small caps "object form" rendered italic; "ADAPTER" with footnote superscript 2 rendered as footnote reference [^2].
- Listing 4 code shown on-page is a declaration fragment (no closing brace for DoorTimerAdapter shown before footnote rule); closed brace added for valid fenced code block.
- Figure 2 diagram bbox estimated from figure region between caption text and following paragraph.
- page 7: verification cap reached
- page 8: Source typos preserved per DEC-009 where intentional ("encasulated", "WithdrawlTransaction", "precicely", "coresponding", "induvidual", "many different language"); corrected only hyphenation across line breaks (e.g., "pre-sented" → "presented", "mes-sage" → "message", "possibil-ity" → "possibility"). Figure 4 diagram region converted to placeholder; diagram content transcribed in caption/alt from OCR reference.
- page 9: coverage floor failed: judge score alone is insufficient
- page 10: verification cap reached
- page 11: verification cap reached
- page 12: - Continuation of Listing 8 code from previous page ("GwithdrawlUI.RequestWithdrawlAmount(); ...").
- Source uses curly quotes in #include statements (“depositUI.h”); preserved as printed.
- "withdrawlUI.h"/"withdrawl" spellings preserved per DEC-009 (source typo allowance); "transfer" declaration missing semicolon in source, preserved.
- Text ends mid-sentence, continues on next page ("when WithdrawUI...").
- page 13: - Corrected source typos: "beween" → "between", "couplings beween cli-ents" hyphenation joined. (DEC-009 logged.)
- Continuing paragraph from previous page ("changed, 'g' and all clients...").
- "ADAPTER" rendered in small caps in source; uppercase preserved.
- No figures on this page.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 253832B model=glm-5.3-flash effort=low transcribe_ms=4685.3 verify_ms=2837.4 ocr_ms=334.4 retries=0 verification_score=96 floor=92% hashes=b6eb389b264461b7f7d787aa91982b9e960c14e764c87235d0704707eac08e9c/c38751119d34babbcbe94a1d5bd5524a96a496f56dfde7926181c5f9de16ea22/5796a7dae011a39d7ac56c1346aef508be73c11e4cde13b7647626f6d38da90c/ccdb7dea1b2793586621a588649a84160d8e3b1e530b478579dcf6e11af70695
- page 2: dpi=200 image=1700x2200 220419B model=glm-5.3-flash effort=low transcribe_ms=3873.0 verify_ms=2926.7 ocr_ms=316.7 retries=0 verification_score=96 floor=98% hashes=aa962e1f20cb76bbdc8c73d8ac80e490a289e983750773057222fc72be44878b/1c72812c2089d9d243fe3d65de4d9cd4fb1a31d6c123af11b9501198cce407d5/3c3ad49ae4f217d4bfd47acb582f48961a8e2e8189a6d002bc3a7a4869345b82/bf358842eb03fe51344c79c297eb96273a59a4fe7cd0c67fc7587d654b24d7e0
- page 3: dpi=400 image=3400x4400 492228B model=glm-5.3-flash effort=low transcribe_ms=23329.5 verify_ms=11316.5 ocr_ms=1978.4 retries=2 verification_score=92 floor=95% hashes=13a8b8dd7bc4b0681fad4b130213a25af4fe886f3f345f035ae533c8bd4c952a/85e15199b8328b516f2fee9f621c9b80e2ea4ad2e4a827bf21fdd869d1c0f2db/c43ba2a46738e04540c71c3c1673a76a55f642fa5b730bc65206031d932bba43/8a8647fedf1f3007ac550c4b4e933c7bc8d64029a22631da36a2c464f0f94689
- page 4: dpi=400 image=3400x4400 514811B model=glm-5.3-flash effort=low transcribe_ms=15677.4 verify_ms=9590.5 ocr_ms=1969.9 retries=2 verification_score=93 floor=98% hashes=5138fea3d81fb0ebadbe795fc0f4936b368ccae9d0abac5e5811fd38cc6fe3cc/620e54d8c9a154ed2120b5cf98e1bf28dd8025631c6acb0be6576ae468b4cdfc/0eee0b505484e4f8f3b351c0b7a9d096f43108b474809bc6a6e4cf9d2db8200d/ea2c77b68610f92dc329eeb01135c41d3cda9ad3609edd0b721c76a77a663f6e
- page 5: dpi=200 image=1700x2200 268374B model=glm-5.3-flash effort=low transcribe_ms=4763.0 verify_ms=2913.3 ocr_ms=293.8 retries=0 verification_score=96 floor=96% hashes=7718a7b9512e369c156f5f538d8f78509a25d7e83ac8918d0fad600311ded967/d4ffe70e1cdfed5f6970bb252464ee8144c2d01027c16f0410afa76d88d149b6/b25061d33f8b3a1086bf5dffa743c27a1595ec6774f50e99a33f681749de1735/0df70d47f9cb67085528b1b4139bddffaf5253ca8d3537c7bd486bfe35613ed1
- page 6: dpi=300 image=2550x3300 329408B model=glm-5.3-flash effort=low transcribe_ms=12651.4 verify_ms=6937.7 ocr_ms=489.0 retries=1 verification_score=98 floor=97% hashes=5bf8bf6c9b4419b3a7ae526057b0d1766cb190966530e13bc0bfb084456bcfe9/d8b3cee09c3667fc8612b9cb44ec986697945a3ff5d2d82070b84238f6932631/21bfbe94bacbe0cf7a85573f94666b3cfee1ddd2c9ee999baa4ecff99e199c7c/8a5e6414a34356a1aa1774c96f7e725808697893306e8e687acf7baed7532afe
- page 7: dpi=400 image=3400x4400 366922B model=glm-5.3-flash effort=low transcribe_ms=15612.0 verify_ms=10949.1 ocr_ms=1857.8 retries=2 verification_score=92 floor=94% hashes=ce7df1de0cea6c9cd4a2aa1b82b7c76de044a8db83752b43ba31c385c07d86ec/2a47a6a54de94bc0496264f7d2a7dad88aedbff666fce071036c8571c7c957b4/1d3a170c26d76351c7a9bc007cfa64c1929d9ce7511812c2d0ff71f253650f27/d4e5274cec377e51489adbf895aa735763cd6876d8e2fd2fc8a03f66fcb1ebab
- page 8: dpi=200 image=1700x2200 271106B model=glm-5.3-flash effort=low transcribe_ms=5164.9 verify_ms=2715.3 ocr_ms=328.9 retries=0 verification_score=96 floor=95% hashes=bb87273df09fd0d312be1a282689880b9792747cc8ebcfef1400f7b48e1dacd0/400d7d5a6b16bf0da143f898d569cb858e5f2224bfe0c16eda020d049b67f8ed/84b4fc6f64b6cc1bf927f2301b1d4673a8a038911a27b50d510e389df4e3f56e/b51f8e9b4e9f7b0806885e0da538f5f39f9c961cdeb50ceb88cfd7ccfcebf278
- page 9: dpi=400 image=3400x4400 219953B model=glm-5.3-flash effort=low transcribe_ms=14362.0 verify_ms=10414.9 ocr_ms=1601.8 retries=2 verification_score=85 floor=65% hashes=74eb3eab567879c24358f8865f2fda76ead213176ae8c590a0a4cf006fc15b4a/0741cb6c6c55bd3e10d54e05d988f7227f2883d07a27ade703ced8ec33cfcd03/9f409987cdb1ff3b46198f01651b5244b96a6ab17461a8495e8061e4f3c515f5/286199fc38ef44c43bee88acd9e88d98d2b167ef34e3137ba5bbabde15d51a38
- page 10: dpi=400 image=3400x4400 307353B model=glm-5.3-flash effort=low transcribe_ms=16113.8 verify_ms=9818.7 ocr_ms=1732.6 retries=2 verification_score=90 floor=93% hashes=2eab2383ad69292d86ead21ab0cae3ed46c3e1270db1777b5cf0ea22031e7e05/60a26bebe0442d2748a72165f7ecafd8799db8e13a388cc066f66c853efc084c/363e6070b6e85934e720251742009c984cff44f2ae193068940c78044d2cd200/c0169286d9b3ed30c57d16a64f814baf405b0faf7199b6789a0470545344e949
- page 11: dpi=400 image=3400x4400 444931B model=glm-5.3-flash effort=low transcribe_ms=14720.8 verify_ms=10629.2 ocr_ms=1852.8 retries=2 verification_score=88 floor=98% hashes=a06a13eb12f0a9b16e68488f14d3042f1598d41306b05fc01cf3e369472a171d/20197cdccacde4ebb363b639cc4b48f5a77492d53dbea91e901145e24cf42ce3/dc8af4ca14d96b1dd0cb62ef4b2aab3267078021ae9d20cba162a14aa0f6fb6f/4503d0a706169fcbdc4bccaac56c4f52753391f9f305b13a5b129cbf37281fec
- page 12: dpi=200 image=1700x2200 257385B model=glm-5.3-flash effort=low transcribe_ms=5445.5 verify_ms=2195.5 ocr_ms=320.1 retries=0 verification_score=96 floor=97% hashes=5421c2e6d32f163bc3d95029e7f8b668c34523de90c68cfbb049a46ffa5b18d6/9792fa1a5b79dfe242589c8c3829968314323245df5c5d3cc441c63f5997b09e/ff03a2817a8ca40d3a14edd0740c8807a38671e577151c9cc47ed8d2a34524ca/8075296da31787bd82d77cbfc4fa70e8bd5a346aa0b48e7ffb783c7de9e0c5a2
- page 13: dpi=200 image=1700x2200 201962B model=glm-5.3-flash effort=low transcribe_ms=4220.6 verify_ms=2549.0 ocr_ms=290.1 retries=0 verification_score=98 floor=94% hashes=4ba4522da77aa43b21879092b58161642b405c95b78826981986acd08fec0fad/57618f4a291b0fa90aa75253babf3c91721ccd2c927e3a202bbbe244c86d3753/831fa43579c4a3f70d2e1eefae73b1fd5e00372cdd345bb71b07fc2d1c3a81a0/3deb1e4c397ea3bf9c49700b189fc74112aa06fb241e577259db44c538ef267d

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:19: [Expected: 80, Actual: 499]
- MD013:37: [Expected: 80, Actual: 230]
- MD033:39: [Element: details]
- MD013:42: [Expected: 80, Actual: 156]
- MD036:44:
- MD033:46: [Element: details]
- MD013:49: [Expected: 80, Actual: 183]
- MD013:56: [Expected: 80, Actual: 797]
- MD013:58: [Expected: 80, Actual: 265]
- MD013:62: [Expected: 80, Actual: 223]
- MD013:64: [Expected: 80, Actual: 346]
- MD013:66: [Expected: 80, Actual: 302]
- MD013:70: [Expected: 80, Actual: 163]
- MD013:85: [Expected: 80, Actual: 156]
- MD013:87: [Expected: 80, Actual: 230]
- MD013:105: [Expected: 80, Actual: 260]
- MD013:107: [Expected: 80, Actual: 375]
- MD013:112: [Expected: 80, Actual: 124]
- MD036:114:
- MD013:116: [Expected: 80, Actual: 525]
- MD013:118: [Expected: 80, Actual: 530]
- MD013:120: [Expected: 80, Actual: 535]
- MD026:122:
- MD013:124: [Expected: 80, Actual: 330]
- MD026:126:
- MD013:128: [Expected: 80, Actual: 391]
- MD013:130: [Expected: 80, Actual: 526]
- MD013:132: [Expected: 80, Actual: 295]
- MD013:153: [Expected: 80, Actual: 454]
- MD013:155: [Expected: 80, Actual: 247]
- MD026:157:
- MD013:159: [Expected: 80, Actual: 646]
- MD025:161:
- MD013:165: [Expected: 80, Actual: 547]
- MD013:169: [Expected: 80, Actual: 375]
- MD013:171: [Expected: 80, Actual: 209]
- MD024:173:
- MD025:173:
- MD013:177: [Expected: 80, Actual: 220]
- MD013:179: [Expected: 80, Actual: 265]
- MD013:198: [Expected: 80, Actual: 318]
- MD033:198: [Element: Abstract]
- MD033:200: [Element: details]
- MD013:203: [Expected: 80, Actual: 156]
- MD036:205:
- MD033:207: [Element: details]
- MD013:210: [Expected: 80, Actual: 131]
- MD013:215: [Expected: 80, Actual: 433]
- MD013:247: [Expected: 80, Actual: 375]
- MD013:251: [Expected: 80, Actual: 370]
- MD013:269: [Expected: 80, Actual: 343]
- MD025:271:
- MD013:273: [Expected: 80, Actual: 514]
- MD013:291: [Expected: 80, Actual: 131]
- MD033:293: [Element: details]
- MD036:298:
- MD013:302: [Expected: 80, Actual: 524]
- MD013:304: [Expected: 80, Actual: 399]
- MD013:306: [Expected: 80, Actual: 289]
- MD013:308: [Expected: 80, Actual: 424]
- MD013:338: [Expected: 80, Actual: 205]
- MD033:340: [Element: details]
- MD013:343: [Expected: 80, Actual: 156]
- MD036:345:
- MD033:347: [Element: details]
- MD013:350: [Expected: 80, Actual: 203]
- MD013:377: [Expected: 80, Actual: 175]
- MD033:379: [Element: details]
- MD013:382: [Expected: 80, Actual: 156]
- MD036:384:
- MD033:386: [Element: details]
- MD013:389: [Expected: 80, Actual: 230]
- MD013:475: [Expected: 80, Actual: 501]
- MD013:489: [Expected: 80, Actual: 549]
- MD013:519: [Expected: 80, Actual: 706]
- MD025:547:
- MD026:547:
- MD013:549: [Expected: 80, Actual: 281]
- MD013:551: [Expected: 80, Actual: 289]
- MD013:553: [Expected: 80, Actual: 166]
- MD013:555: [Expected: 80, Actual: 481]
- MD025:557:
- MD013:559: [Expected: 80, Actual: 454]
- MD013:561: [Expected: 80, Actual: 701]
