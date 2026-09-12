# Conversion report — Interface_Segration_Principle.pdf

- job_id: 9f3eb920-19ce-449d-af90-36c50428a2f4
- status: assembling
- pages: 13
- wall-clock: not started
- tokens: prompt=309270 completion=15473
- pipeline_version: 073654be6c457b411ab24a51dcfff4bdea2968daf6252a3e996dc1f6b48c7d48
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 92

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 95 | 0 | 200 | 11648 | 873 | False |
| 2 | verified | 98 | 0 | 200 | 12082 | 692 | False |
| 3 | verified | 95 | 2 | 400 | 50827 | 2461 | False |
| 4 | verified | 97 | 0 | 200 | 13255 | 857 | False |
| 5 | verified | 95 | 1 | 300 | 32969 | 1561 | False |
| 6 | verified | 98 | 0 | 72 | 4676 | 1042 | False |
| 7 | verified | 95 | 0 | 200 | 12825 | 655 | False |
| 8 | verified | 95 | 0 | 200 | 13921 | 744 | False |
| 9 | needs_review | 90 | 2 | 400 | 48923 | 1351 | True |
| 10 | verified | 95 | 1 | 300 | 30881 | 1406 | False |
| 11 | verified | 95 | 1 | 300 | 31679 | 1590 | False |
| 12 | verified | 97 | 1 | 300 | 32054 | 1710 | False |
| 13 | verified | 97 | 0 | 200 | 13530 | 531 | False |

## needs_review pages

[9]

## Diagram → Mermaid conversion

- figures: 7
- converted to Mermaid: 7 (100%)
- data-table fallbacks: 0
- image fallbacks: 0

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 1 | 13 | classDiagram | mermaid | 95 |
| 3 | 14 | classDiagram | mermaid | 100 |
| 6 | 15 | classDiagram | mermaid | 92 |
| 7 | 16 | classDiagram | mermaid | 97 |
| 8 | 17 | classDiagram | mermaid | 95 |
| 9 | 18 | classDiagram | mermaid | 92 |
| 9 | 19 | classDiagram | mermaid | 95 |

## Omissions log

- page 1: - Corrected source typo "Modeling Langage" → "Modeling Language".
- The sidebar (boxed diagram "Unified Notation 0.8") is rendered as a figure placeholder inline at its wrap point in the paragraph text.
- Footnote 1 appears twice in OCR reference; single footnote emitted.
- Footnote continues onto next page ("In other...").
- Page number and copyright footer excluded from body.
- page 2: - Continuing paragraph from page 1 ("words, the interfaces...").
- Corrected source typo "interfase" to "interfaces" in "the disadvantages of 'fat' or 'polluted' interfaces".
- "the a 'fat' interface" retained as in source (article's own grammatical slip, per DEC-009 logged but left verbatim in body? — corrected reading kept as source).
- Source code typo "Regsiter" retained verbatim (code identifier).
- Running header "Interface Pollution" and page number "2" excluded from body.
- page 3: Continuation of article from page 2 (body text of "Interface Pollution" section). Figure caption "Figure 1 / TimerClient at top of hierarchy" rendered as text above the figure placeholder; the diagram region is the UML inheritance diagram (TimerClient → Door → TimedDoor). *nil* italicized as in source.
- page 4: - Header "Interface Pollution" and page number 4 are running header/footer furniture, excluded from body.
- Corrected "complely" → "completly" is still present in source; left as-is? Actually corrected "complely" → "completly" would be a guess; kept source spelling "completly" and logged it as an apparent source typo for "completely".
- Listing 3 code fence marked cpp despite earlier OCR reference labeling it java; the source is C++.
- Final sentence lacks a terminal period in source; preserved verbatim.
- No figures on this page.
- page 5: - Corrected source typo "unerlated" to "unrelated".
- Code typos "Regsiter" (Listings 2 and 3) left verbatim to preserve source listings.
- Continuation from page 4: page begins mid-sentence "and managers to the bone."
- page 6: - Figure 2 shows a UML class diagram (Door, TimerClient, TimedDoor, DoorTimerAdapter with inheritance and delegation relationships); replaced with placeholder token.
- OCR of "some of the use of Door would be affected" reads awkwardly; image shows "none of the users of Door would be affected" — corrected per image.
- Listing 4 code block language inferred as C++ despite the listing title mentioning the Adapter pattern (example code is C++); OCR context shows "class ... : public ..." syntax.
- Footnote "2. Another GOF pattern. ibid." retained as body text footnote marker at end of page.
- [?] none.
- page 7: Continuation: code block at top completes Listing 4 from previous page. Listing 5 source was labeled "java" in OCR reference but is C++ (public inheritance syntax); emitted as cpp. Figure 3 caption placed after figure placeholder per source layout.
- page 8: - Typos left as in source per DEC-009 allowance or corrected minimally: "encasulated" (source), "WithdrawlTransaction" (source), "different language" (source), "spoken out" (source). "coresponding" and "induvidual" appear in source; corrected to "corresponding"/"individual" per DEC-009 typo allowance. No [?] marks.
- Figure 4 diagram contains class labels ATM UI (Abstract), Braille UI, Screen UI, Speech UI.
- Running header and page number excluded from body.
- page 9: coverage floor failed: judge score alone is insufficient
- page 10: - Continuation of Listing 6 from page 9; code block remains open (ends with "class UI : public DepositUI," which continues on the next page).
- Corrected duplicated "class class" to "class" (3 occurrences, per DEC-009 typo allowance).
- Retained source spellings "Withdrawl", "RequestWithdrawlAmount", "itsWithdrawlUI" (source-consistent naming, not corrected).
- No figures on this page.
- page 11: - Page begins with continuation of the Listing 6 code block started on the previous page ("class UI : public DepositUI," on page 10); leading ", public WithdrawlUI," lines are verbatim continuation.
- "Seperate Global Pointers" is a source typo (Seperate → Separate); left verbatim per DEC-009, logged here.
- "class class WithdrawlTransation" — doubled "class" and "Transation" are source typos; left verbatim, logged.
- "Withdrawl" spellings (e.g., WithdrawlUI, GwithdrawlUI) are verbatim from source.
- "idom" in body text corrected to "idiom" (source typo).
- Listing 8 appears to be truncated/aborted at the bottom of the page in the source (listing ends with "}" and code block closes); no further text on the page.
- No figures on this page.
- page 12: - Code block at top continues Listing 8 from previous page (ends WithdrawlTransaction::Execute).
- Heading "The Polyad vs. the Monad." rendered as ## for outline continuity.
- Inline code in body set in code spans where bold monospace in source.
- "transfer" declaration in Listing 9 lacks trailing semicolon in source; preserved verbatim.
- OCR reference read "withdrawUI.h"; image shows "withdrawlUI.h" — preserved image spelling.
- No figures on this page.
- page 13: Page continues the polyadic vs. monadic discussion from page 12; only the tail of the article appears on this page. No figures. No typo corrections needed; OCR reference text was duplicated in the prompt and matched.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 253832B model=glm-5.3-flash effort=low transcribe_ms=4821.2 verify_ms=3083.3 ocr_ms=16384.6 retries=0 verification_score=95 floor=97% hashes=b6eb389b264461b7f7d787aa91982b9e960c14e764c87235d0704707eac08e9c/c38751119d34babbcbe94a1d5bd5524a96a496f56dfde7926181c5f9de16ea22/404e34c659898a92c3d6a203dac5f638cb8651b5b04e0a6328cdb8237ee5403a/58a289ecd6ca10d95ab4a7a7d5c28b1061f86c98fd831cd8da3c9b4fcf155c2c
- page 2: dpi=200 image=1700x2200 220419B model=glm-5.3-flash effort=low transcribe_ms=4013.1 verify_ms=2505.0 ocr_ms=15634.4 retries=0 verification_score=98 floor=100% hashes=aa962e1f20cb76bbdc8c73d8ac80e490a289e983750773057222fc72be44878b/1c72812c2089d9d243fe3d65de4d9cd4fb1a31d6c123af11b9501198cce407d5/7bbd1136980ec0a760844adc59ef402073cadc4d5e80f9cc827c37d02e4eeb6d/b935895fd3503f15a938912c67c837e400aecd4876cdc91fc85acc81c8dc716f
- page 3: dpi=400 image=3400x4400 492228B model=glm-5.3-flash effort=low transcribe_ms=15517.6 verify_ms=10882.9 ocr_ms=53715.3 retries=2 verification_score=95 floor=100% hashes=13a8b8dd7bc4b0681fad4b130213a25af4fe886f3f345f035ae533c8bd4c952a/85e15199b8328b516f2fee9f621c9b80e2ea4ad2e4a827bf21fdd869d1c0f2db/b0de294a2ef1e127dc990e828f07f0541d8b40f4468b5086719bce7826d8d8ac/e41596832002561297be83cd1b0de89de17859f4860ad49926d8a7aa15af6d09
- page 4: dpi=200 image=1700x2200 270889B model=glm-5.3-flash effort=low transcribe_ms=4473.1 verify_ms=4319.0 ocr_ms=18234.5 retries=0 verification_score=97 floor=100% hashes=5138fea3d81fb0ebadbe795fc0f4936b368ccae9d0abac5e5811fd38cc6fe3cc/ac6ab4604fc3e84a193594b1946a96c59564f734c04b72c9cd9a13a31e732dad/8fadc2a88cece7ff6d6b208197119525f7d847bc47f514043a251a27766fb774/def973ad8c87499d51d0e2149f65a6f65cbce1207a06c6245d4d01a614ffbba3
- page 5: dpi=300 image=2550x3300 433927B model=glm-5.3-flash effort=low transcribe_ms=11331.8 verify_ms=6292.6 ocr_ms=35284.1 retries=1 verification_score=95 floor=100% hashes=7718a7b9512e369c156f5f538d8f78509a25d7e83ac8918d0fad600311ded967/bc57726fcd9b2a182219967750ab6754ce5f62a1448765b7c35fa978b02e1079/cbbef71f3eeb51bf388b490ef226839961f87836e1e2f59b93d7722edba7f465/7e5fbb40b6527e5edf4dbf3a880a2809156dbf386de666b45339a48a10547ed1
- page 6: dpi=72 image=612x792 51225B model=glm-5.3-flash effort=low transcribe_ms=7234.1 verify_ms=3902.3 ocr_ms=1570025.2 retries=0 verification_score=98 floor=98% hashes=5bf8bf6c9b4419b3a7ae526057b0d1766cb190966530e13bc0bfb084456bcfe9/b398da3be1adea1ba40b14d4e23f64781e6f25d0d05335b183e0dd4abdeecee1/ff6a0cb1be683c9669fe14112afc3d7ebacc95d5926f0cb0a27cd92c8f2d4c7d/7ff1ce960be8dd2ad1db9f3de97cc3dede51935199713d5f22e79491e5938d4b
- page 7: dpi=200 image=1700x2200 186617B model=glm-5.3-flash effort=low transcribe_ms=20805.3 verify_ms=3590.3 ocr_ms=13948.3 retries=0 verification_score=95 floor=100% hashes=ce7df1de0cea6c9cd4a2aa1b82b7c76de044a8db83752b43ba31c385c07d86ec/e25f5994d42b1cb4328f2cd879e4a2bd9c30949006158cfe17feaa5ce6ee8847/d9e5676a7b791eaf74443f95aaa0b9c16ae1755914fd9335ae99ea358fbdd457/cca3c65fb7922b7cf5c486b4756889b84b4d00a63aa019ae04d9ca9e4ad7b47c
- page 8: dpi=200 image=1700x2200 271106B model=glm-5.3-flash effort=low transcribe_ms=9189.9 verify_ms=2617.6 ocr_ms=30182.3 retries=0 verification_score=95 floor=100% hashes=bb87273df09fd0d312be1a282689880b9792747cc8ebcfef1400f7b48e1dacd0/400d7d5a6b16bf0da143f898d569cb858e5f2224bfe0c16eda020d049b67f8ed/1b65f1b3aec99f29ad55629c44930b9b77b5ae6dd3d3b46e62b99ac5294680be/630554f6f4627b373d0ce8cf957e09b5a9306cc1adf27e0efc037bcd2ef510b4
- page 9: dpi=400 image=3400x4400 219953B model=glm-5.3-flash effort=low transcribe_ms=18294.9 verify_ms=9631.3 ocr_ms=27172.9 retries=2 verification_score=90 floor=69% hashes=74eb3eab567879c24358f8865f2fda76ead213176ae8c590a0a4cf006fc15b4a/0741cb6c6c55bd3e10d54e05d988f7227f2883d07a27ade703ced8ec33cfcd03/bdf6b77935be07490a5144862c6008a1f1d7225c243257536215cff04c2b2730/59cf5c9e4c6c0590c74909f697f7d5833a022778b5a91331cd2039b88d8107eb
- page 10: dpi=300 image=2550x3300 245326B model=glm-5.3-flash effort=low transcribe_ms=11083.6 verify_ms=9049.7 ocr_ms=24657.6 retries=1 verification_score=95 floor=100% hashes=2eab2383ad69292d86ead21ab0cae3ed46c3e1270db1777b5cf0ea22031e7e05/7cd087fcc872f1fb4d96e19164437de4b911f2dc78d633b69c50fb43836012c0/bba0de74a16470abba73c7f128ff060da755851369eb965be6ecb97b74b72516/6445017592ec76cc65d9439f01702805e9adf6e8bda4002cb3d3236aa475a620
- page 11: dpi=300 image=2550x3300 368927B model=glm-5.3-flash effort=low transcribe_ms=13481.4 verify_ms=8176.9 ocr_ms=33793.5 retries=1 verification_score=95 floor=99% hashes=a06a13eb12f0a9b16e68488f14d3042f1598d41306b05fc01cf3e369472a171d/cd0418fcfa0fd1cde51b19609e8d232baad12d2ab9b8c32da779ec8b978064a8/a5c6dac49ba0ff9ca1dd6b978aba46567d5fa7c3238f400596d0999bfd9fc84e/5ed7d685b21bccf94d52ed7b3718e496cd900da3cffea1436d9b055c72c51c1b
- page 12: dpi=300 image=2550x3300 418194B model=glm-5.3-flash effort=low transcribe_ms=17011.9 verify_ms=10426.8 ocr_ms=37615.4 retries=1 verification_score=97 floor=100% hashes=5421c2e6d32f163bc3d95029e7f8b668c34523de90c68cfbb049a46ffa5b18d6/006c8275fb695bbba07e8faf121f32c0b8d0915edee98fc8df24e3d734f9beb1/50c9eb0083f6e0c247f253ea4665caacafe401c450e9c91af08530623c733211/614a027c4f836477271ecc8acb6f8a5f73dc5e61327d568cab3074f58db3fd47
- page 13: dpi=200 image=1700x2200 201962B model=glm-5.3-flash effort=low transcribe_ms=5003.2 verify_ms=2420.4 ocr_ms=24433.4 retries=0 verification_score=97 floor=99% hashes=4ba4522da77aa43b21879092b58161642b405c95b78826981986acd08fec0fad/57618f4a291b0fa90aa75253babf3c91721ccd2c927e3a202bbbe244c86d3753/00bfa90d2a032f9c1be8bc899489adfbc90e163895ff6ea40cb1dde43b69f22a/3deb1e4c397ea3bf9c49700b189fc74112aa06fb241e577259db44c538ef267d

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:17: [Expected: 80, Actual: 496]
- MD013:34: [Expected: 80, Actual: 196]
- MD033:36: [Element: details]
- MD013:39: [Expected: 80, Actual: 156]
- MD036:41:
- MD033:43: [Element: details]
- MD013:46: [Expected: 80, Actual: 220]
- MD013:53: [Expected: 80, Actual: 795]
- MD013:55: [Expected: 80, Actual: 264]
- MD013:59: [Expected: 80, Actual: 223]
- MD013:61: [Expected: 80, Actual: 346]
- MD013:63: [Expected: 80, Actual: 302]
- MD025:65:
- MD013:67: [Expected: 80, Actual: 163]
- MD013:82: [Expected: 80, Actual: 156]
- MD013:84: [Expected: 80, Actual: 230]
- MD013:103: [Expected: 80, Actual: 260]
- MD013:105: [Expected: 80, Actual: 375]
- MD013:116: [Expected: 80, Actual: 152]
- MD033:118: [Element: details]
- MD013:121: [Expected: 80, Actual: 134]
- MD036:123:
- MD013:127: [Expected: 80, Actual: 525]
- MD013:129: [Expected: 80, Actual: 530]
- MD013:131: [Expected: 80, Actual: 535]
- MD025:133:
- MD026:133:
- MD013:135: [Expected: 80, Actual: 331]
- MD025:137:
- MD026:137:
- MD013:139: [Expected: 80, Actual: 391]
- MD013:141: [Expected: 80, Actual: 526]
- MD013:143: [Expected: 80, Actual: 295]
- MD013:164: [Expected: 80, Actual: 454]
- MD013:166: [Expected: 80, Actual: 247]
- MD013:170: [Expected: 80, Actual: 646]
- MD025:172:
- MD013:176: [Expected: 80, Actual: 547]
- MD025:178:
- MD013:180: [Expected: 80, Actual: 375]
- MD013:182: [Expected: 80, Actual: 209]
- MD025:184:
- MD013:186: [Expected: 80, Actual: 221]
- MD013:188: [Expected: 80, Actual: 265]
- MD013:209: [Expected: 80, Actual: 223]
- MD033:211: [Element: details]
- MD013:214: [Expected: 80, Actual: 156]
- MD036:216:
- MD033:218: [Element: details]
- MD013:221: [Expected: 80, Actual: 176]
- MD013:226: [Expected: 80, Actual: 433]
- MD029:249: [Expected: 1; Actual: 2; Style: 1/2/3]
- MD013:257: [Expected: 80, Actual: 375]
- MD025:259:
- MD013:261: [Expected: 80, Actual: 370]
- MD013:272: [Expected: 80, Actual: 131]
- MD033:274: [Element: details]
- MD036:279:
- MD013:296: [Expected: 80, Actual: 343]
- MD025:298:
- MD013:300: [Expected: 80, Actual: 514]
- MD013:318: [Expected: 80, Actual: 159]
- MD033:320: [Element: details]
- MD013:323: [Expected: 80, Actual: 125]
- MD036:325:
- MD013:329: [Expected: 80, Actual: 524]
- MD013:331: [Expected: 80, Actual: 399]
- MD013:333: [Expected: 80, Actual: 289]
- MD013:335: [Expected: 80, Actual: 425]
- MD013:365: [Expected: 80, Actual: 195]
- MD033:367: [Element: details]
- MD013:370: [Expected: 80, Actual: 156]
- MD036:372:
- MD033:374: [Element: details]
- MD013:377: [Expected: 80, Actual: 171]
- MD013:416: [Expected: 80, Actual: 221]
- MD033:418: [Element: details]
- MD013:421: [Expected: 80, Actual: 155]
- MD036:423:
- MD033:425: [Element: details]
- MD013:428: [Expected: 80, Actual: 194]
- MD013:520: [Expected: 80, Actual: 501]
- MD013:534: [Expected: 80, Actual: 549]
- MD013:568: [Expected: 80, Actual: 706]
- MD026:596:
- MD013:598: [Expected: 80, Actual: 281]
- MD013:600: [Expected: 80, Actual: 289]
- MD013:602: [Expected: 80, Actual: 166]
- MD013:604: [Expected: 80, Actual: 481]
- MD025:606:
- MD013:608: [Expected: 80, Actual: 454]
- MD013:610: [Expected: 80, Actual: 701]
