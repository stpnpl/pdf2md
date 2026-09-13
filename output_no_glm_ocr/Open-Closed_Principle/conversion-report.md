# Conversion report — Open-Closed_Principle.pdf

- job_id: f708ba59-0cad-4d58-b6f9-820b0d3a32e1
- status: assembling
- pages: 14
- wall-clock: not started
- tokens: prompt=277768 completion=13442
- pipeline_version: 9c215872aa0b575aade8ae9fb73a81b65c9fb7d96e9934b244133c2636e44bc0
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 91

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 100 | 0 | 200 | 12205 | 654 | False |
| 2 | needs_review | 93 | 2 | 400 | 50499 | 2572 | True |
| 3 | verified | 95 | 0 | 200 | 12427 | 649 | False |
| 4 | verified | 98 | 0 | 200 | 13031 | 568 | False |
| 5 | verified | 95 | 1 | 300 | 32420 | 1318 | False |
| 6 | verified | 98 | 0 | 200 | 13493 | 781 | False |
| 7 | verified | 95 | 0 | 200 | 13076 | 570 | False |
| 8 | verified | 95 | 0 | 200 | 12919 | 657 | False |
| 9 | verified | 95 | 0 | 200 | 13278 | 765 | False |
| 10 | verified | 100 | 0 | 200 | 13239 | 667 | False |
| 11 | verified | 95 | 0 | 200 | 13827 | 935 | False |
| 12 | needs_review | 90 | 2 | 400 | 51405 | 1582 | True |
| 13 | verified | 95 | 0 | 200 | 13202 | 696 | False |
| 14 | verified | 95 | 0 | 200 | 12747 | 1028 | False |

## needs_review pages

[2, 12]

## Diagram → Mermaid conversion

- figures: 8
- converted to Mermaid: 4 (50%)
- data-table fallbacks: 0
- image fallbacks: 4

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 2 | 106 | flowchart | image | 75 |
| 3 | 107 | classDiagram | image | 80 |
| 14 | 108 | classDiagram | mermaid | 92 |
| 14 | 109 | classDiagram | mermaid | 90 |
| 14 | 110 | classDiagram | mermaid | 85 |
| 14 | 111 | classDiagram | mermaid | 95 |
| 14 | 112 | sequenceDiagram | image | 70 |
| 14 | 113 | classDiagram | image | 85 |

## Omissions log

- page 1: Footnote references rendered as superscript Unicode (¹, ²). Small-caps pull quote rendered as bold italic with capitalized first letters, matching source styling. No figures on this page. No typos corrected.
- page 2: verification cap reached
- page 3: Figure 2 continues the figure sequence from the previous page (Figure 1). Listing 1 continues onto the next page; the code block is left unclosed contextually for continuation. Code indentation in the listing box normalized. No uncertain characters.
- page 4: Continuation from previous page: listing continues the `struct Square` definition; body text continues mid-sentence ("...the predicates of the if") onto the next page. Listing title "Listing 1 (Continued)" transcribed as bold text heading the code block. Running header and page number excluded from body.
- page 5: - Running header "5 : The Open-Closed Principle" excluded from body per rules and recorded here as furniture.
- Page continues prior page text (paragraph beginning "statements would be combined...").
- Listing 2 box drawn with border in source; rendered as fenced code block with listing caption.
- page 6: Footnote 3 rendered as body footnote text; running header "Strategic Closure" and page number "6" excluded from body. No figures on this page.
- page 7: Listings 3–5 rendered as code blocks with boxed list captions; boxes omitted as decorative. No figures on page. Footnote reference from previous page context not repeated here.
- page 8: - Page contains only Listing 6, enclosed in a boxed figure region (not replaced with a figure token since it is a code listing, transcribed verbatim).
- Corrected curly quotes in `"Circle"` and `"Square"` to straight quotes in code.
- Listing 6 continues on the next page (code cut off after `argOrd = i;`).
- [?] none.
- page 9: - Listing 6 (Continued) is a code box continuation from previous page; opening lines of the `Precedes` for-loop appear on prior page. The boxed listing is rendered as a fenced code block (no figure region needed).
- Corrected "begining" to "begining" left as-is per source? Corrected to "beginning" — typo correction logged (source: "at the begining of this article").
- Running header "9 : The Open-Closed Principle" and page number 9 excluded from body.
- page 10: No figures on page. Running header "Heuristics and Conventions" and page number "10" excluded from body. Italic emphasis (*do*, *are closed*, *encapsulation*) preserved from source typography. No typos corrected on this page.
- page 11: - Source typo "pubic member variables" corrected to "public member variables" (DEC-009).
- Page begins mid-sentence/mid-section continuing from previous page; continues onto next page ("How-" hyphenated).
- Typo "begining" and "proscrip-tion" appeared in rolling context, not on this page image; no further corrections needed.
- Inline code formatting applied to identifiers (minutes, hours, Time, public, private, etc.) consistent with prior pages.
- page 12: verification cap reached
- page 13: - Page begins mid-listing: Listing 10 code block is the continuation of the listing started on the previous page (function signature `void DrawSquaresOnly(Set<Shape*>& ss)` was on prior page).
- Paragraph begins mid-word ("ever," completing "How-ever" hyphenation from prior page).
- Retained source typos per DEC-009 allowance (verbatim policy for OCR ground truth): "yeilds" (yields), "strenghts" (strengths). Not corrected to preserve source text fidelity.
- Listing 10 caption/box is textual, not a figure region; no figure placeholders needed.
- No uncertain characters found.
- page 14: - Page is a figure page: six boxed diagram panels (Booch notation legend) arranged in two columns; reading order linearized left-to-right, top-to-bottom per column pair. Panel boxes retained as figure placeholders including their diagram region; caption text and code blocks transcribed.
- OCR reference order differed from visual reading order; re-ordered per layout.
- Code within panels uses monospaced text in source; rendered as fenced code blocks.
- No uncertain characters encountered.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 278930B model=glm-5.3-flash effort=low transcribe_ms=5879.2 verify_ms=3035.9 ocr_ms=335.7 retries=0 verification_score=100 floor=97% hashes=79e4031eb3438ba67cc61a92a04de98b205b3a245956cdff692d05d8a263bf20/a441ddc0949c244cf94fc5e644e0a502b4b95fc20cf1f9a2a9c7bda59fb8f868/2af3b1ea8a3f302b75863208ca3ae4670f48ed05c0ccf0b8add1e6e1d428fdc1/900db92bc74bc8f19394d51599da8a693d437a25d0c617e681c858cd03cf5c0c
- page 2: dpi=400 image=3400x4400 519735B model=glm-5.3-flash effort=low transcribe_ms=27758.9 verify_ms=11051.3 ocr_ms=2118.3 retries=2 verification_score=93 floor=95% hashes=0f7a6e0aea64fa7164bcc01c91cf50683af6ad989b336813f05bd97fb71c61f0/59965a1ec3baed5f40a8fa623c4245f6bcc4fa29d4822a14c1d93bc6d5f58725/72bb81595763517054b3bd69715f7fdc37f1d1ca226c510219f84a4f49ea6a00/8f84814d9a952fe0528ab650998de3a7076f4b04b76154768aba689a8afe3f53
- page 3: dpi=200 image=1700x2200 183589B model=glm-5.3-flash effort=low transcribe_ms=3987.4 verify_ms=3578.4 ocr_ms=336.2 retries=0 verification_score=95 floor=95% hashes=e4861ea62a4de7378298b00a570fb554a1cc40f278a3319799be0c82d5eb28c6/2f74db5f5589470dc3f7dbc36b11ac309a88d364a206e68658ac67e43f6aa6c1/2054f1e425ff3cb2207f94d683051c5c79fb042efd2c181e7d66196b59a72683/66bba783c2ce0118e75fe5e3aac345a6cb4a6aa09688c7131f50c0a735cfe6bb
- page 4: dpi=200 image=1700x2200 219943B model=glm-5.3-flash effort=low transcribe_ms=5476.5 verify_ms=2862.5 ocr_ms=322.0 retries=0 verification_score=98 floor=97% hashes=7061c8a51b4f5dc2402536f845a6e527fb2cb49921d4094bcd54a114622a4ad9/e9644c4b3abb5cdf038a5f13f39c74d680140aa6faec92f7202b436f6db293d1/d2b87de66fc20c7560ac0a7f587c39ca2de5af87a17fc4b42ebe5236425bd825/ff0567eccc907418822ff7276eac47bb498ce1f06c76beb2f3c6ee2b56b3a5fa
- page 5: dpi=300 image=2550x3300 395349B model=glm-5.3-flash effort=low transcribe_ms=13393.1 verify_ms=8215.0 ocr_ms=1005.1 retries=1 verification_score=95 floor=99% hashes=2c8b30f217530d6af59bc8e25baa681604393fe2fc044170f5f8021e9c63b5e4/ecac07b7b9aaeabcbcb364c57c40fb51fe55e1527fadd589cc30158a4deba64e/1f245def6e343243e70bbfcecbdef1701acb07052306a4fdf028eefe1367fbd6/d39551493ada7fa4922fe63ebfa53dac5c17d5b97f43d85cfd348bda68481317
- page 6: dpi=200 image=1700x2200 338554B model=glm-5.3-flash effort=low transcribe_ms=6735.4 verify_ms=4611.9 ocr_ms=362.3 retries=0 verification_score=98 floor=97% hashes=ee6beed23f81a06d97747ca9bf5b628d10ef9b24031c9256a4df782b2a5d9fbd/eaffc72fd8015bfa2009631217ca6d436cfab7c2d674dc4e845aba913397339d/6dab58cbfa2b323ccc1320ac4c63c3d99cc304ce302b5afcf62d38be48731547/4a25bbc1749a2a6de462a7f0e26efcabb7417f69a5ff2997eb7fb986aa261850
- page 7: dpi=200 image=1700x2200 218236B model=glm-5.3-flash effort=low transcribe_ms=5627.2 verify_ms=3763.8 ocr_ms=297.0 retries=0 verification_score=95 floor=97% hashes=7da7883d76e769f0d013ba71bf3cb1d064353f6605cef593efdfb939310b1a75/0d9ae4e7169ff86fb6873aa458b672c657c07f5448fc7b12a23f83a71dcd36f4/b8ec40934472826afbfa0373fa2a96faac514f4ef1c5ebb30c622f08f65743cc/54b1d5b08990da5ec5aa64ffe1008f93b388c06954f7ab13b39e3a97155f0825
- page 8: dpi=200 image=1700x2200 182693B model=glm-5.3-flash effort=low transcribe_ms=4415.7 verify_ms=5514.7 ocr_ms=295.5 retries=0 verification_score=95 floor=98% hashes=0aadaed0fd61a30c6b2be749eeb95b1593cfc1f183a3566d12b3dd8359a1e5c5/481d1cd5571fa5b46de962635bd43be5dbe2b6860345fa56485cd16e58ed89db/97ec79c6998b33069dd223be853a484b484198a0ad943732676439d72d348065/bce1b0f6d11f4f5307b3dedd50fa9af62564e924d3923b75ae6486236f54aba2
- page 9: dpi=200 image=1700x2200 262623B model=glm-5.3-flash effort=low transcribe_ms=16403.1 verify_ms=3655.3 ocr_ms=347.2 retries=0 verification_score=95 floor=99% hashes=0cae54be9a452566e151ce93a2aef19f7744bf387f48e00cb097e78fe518cf78/38aa27b0e794753bc6a1101567c02608ce536e99c611bd30cf9934bf4bb9e30a/0da9032f3044d374ee6f43f8c474289ec4c2b8f973b9967b4adee260b06b03e9/dcd517cf670e843dc090bd24ff1975b3a80ddb64e436e94f2e9dadcfd5fc48e5
- page 10: dpi=200 image=1700x2200 270245B model=glm-5.3-flash effort=low transcribe_ms=4962.0 verify_ms=3627.8 ocr_ms=339.8 retries=0 verification_score=100 floor=98% hashes=17ab3eafce1959bb937f674efc201ec6c758424ff178cc0c4d50266db0400968/e9d90d4b58232e813eb64443d8fba757cd93d4d8003d1504cde1e2d12e9ca5f9/d9654efa4a405290fdf447dec4c69a22f3b2b8bbc9ddc6de1ac65f5d111e3224/e7814dcea2101220db43e02b220721be4a3dc391fb82ab4acd54b5e02d5bf401
- page 11: dpi=200 image=1700x2200 337729B model=glm-5.3-flash effort=low transcribe_ms=7470.9 verify_ms=3981.5 ocr_ms=343.3 retries=0 verification_score=95 floor=96% hashes=7ff803bf88aaec7f503d7f1e5f1532138995b252403036b664ad23c9672f80cf/d038a4225ad1f625a4ab1ea75a9dea763e93c55c9c0e55eaf7170b437f6a153f/5dddc1989efbb268e576871732dc7b6e6f034baadc51716020b1486fe5b574e1/dabe3484cf405e8faad2f7aa123368b8427da47c52cb8f0e25ca47d461adcd16
- page 12: dpi=400 image=3400x4400 308360B model=glm-5.3-flash effort=low transcribe_ms=16339.4 verify_ms=10159.4 ocr_ms=1821.0 retries=2 verification_score=90 floor=96% hashes=dd274278986d57516625f3b55ce3da63aaa9788cbcf3812a8a7af8946a8b984d/0902d3873725706e71dec71e4095538233362b233998dd4c9fe93b861172674d/5e5801814b06e8fd1103ee3af30788b81dd60287ae5f7a85bc4a59fe3225914c/73504c7d22beb49694c8a1011d54012b8a08a2fab80a2226e452878f393b72db
- page 13: dpi=200 image=1700x2200 217078B model=glm-5.3-flash effort=low transcribe_ms=4751.5 verify_ms=3010.2 ocr_ms=94.6 retries=0 verification_score=95 floor=98% hashes=4bbeb90e5bce2beba6d748b059bc561b74f247eaa4cf70823ada8672e71dd8a2/e144e559c831b9dd2244a6180d3081b490956168c8d4501313dcae2cfcbad70e/9004661dbccb99e730722808eabadcc08f895d6585bfc19ec54ed838463aec84/b72f06f5da7c18d22f97bdc701839f2a7796f5e994552b30ba6837415ae11156
- page 14: dpi=200 image=1700x2200 176295B model=glm-5.3-flash effort=low transcribe_ms=6645.7 verify_ms=2630.5 ocr_ms=336.0 retries=0 verification_score=95 floor=98% hashes=1640911cec68049b1b808517c3079b0943349d4e59e79ccf351c1f480517f055/aebff8bdf0b4d26b146fd7e6596962b9de3eb8f726e31dfd3e78a7a54428eff0/9b9ce83da0e6db00588ba13ed6d5c438f1fa3181272535621cff70a5e210ec99/addbe0b690c5204941ab1f6da8d52bf7d4efcc361c8aded0948b48e9e75e9c44

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:19: [Expected: 80, Actual: 469]
- MD013:21: [Expected: 80, Actual: 416]
- MD013:23: [Expected: 80, Actual: 408]
- MD013:25: [Expected: 80, Actual: 176]
- MD013:27: [Expected: 80, Actual: 513]
- MD013:35: [Expected: 80, Actual: 110]
- MD013:36: [Expected: 80, Actual: 83]
- MD013:38: [Expected: 80, Actual: 212]
- MD013:40: [Expected: 80, Actual: 102]
- MD013:42: [Expected: 80, Actual: 282]
- MD025:44:
- MD026:44:
- MD013:46: [Expected: 80, Actual: 564]
- MD013:48: [Expected: 80, Actual: 401]
- MD013:58: [Expected: 80, Actual: 487]
- MD013:60: [Expected: 80, Actual: 126]
- MD036:62:
- MD025:67:
- MD013:69: [Expected: 80, Actual: 336]
- MD013:71: [Expected: 80, Actual: 531]
- MD024:92:
- MD025:92:
- MD013:133: [Expected: 80, Actual: 359]
- MD013:135: [Expected: 80, Actual: 611]
- MD013:137: [Expected: 80, Actual: 290]
- MD013:139: [Expected: 80, Actual: 298]
- MD013:170: [Expected: 80, Actual: 343]
- MD013:172: [Expected: 80, Actual: 318]
- MD013:174: [Expected: 80, Actual: 211]
- MD025:176:
- MD013:178: [Expected: 80, Actual: 416]
- MD013:180: [Expected: 80, Actual: 430]
- MD026:182:
- MD013:184: [Expected: 80, Actual: 356]
- MD013:186: [Expected: 80, Actual: 378]
- MD013:188: [Expected: 80, Actual: 171]
- MD013:190: [Expected: 80, Actual: 402]
- MD013:192: [Expected: 80, Actual: 423]
- MD013:194: [Expected: 80, Actual: 110]
- MD029:194: [Expected: 1; Actual: 3; Style: 1/2/3]
- MD013:238: [Expected: 80, Actual: 243]
- MD026:240:
- MD013:242: [Expected: 80, Actual: 171]
- MD013:244: [Expected: 80, Actual: 334]
- MD013:311: [Expected: 80, Actual: 242]
- MD026:313:
- MD013:315: [Expected: 80, Actual: 680]
- MD025:317:
- MD013:319: [Expected: 80, Actual: 240]
- MD026:321:
- MD013:323: [Expected: 80, Actual: 327]
- MD013:325: [Expected: 80, Actual: 291]
- MD013:327: [Expected: 80, Actual: 291]
- MD013:329: [Expected: 80, Actual: 339]
- MD013:342: [Expected: 80, Actual: 691]
- MD013:344: [Expected: 80, Actual: 459]
- MD036:346:
- MD013:362: [Expected: 80, Actual: 416]
- MD013:364: [Expected: 80, Actual: 526]
- MD013:366: [Expected: 80, Actual: 172]
- MD026:368:
- MD013:370: [Expected: 80, Actual: 417]
- MD013:372: [Expected: 80, Actual: 281]
- MD013:374: [Expected: 80, Actual: 500]
- MD026:376:
- MD013:378: [Expected: 80, Actual: 429]
- MD013:380: [Expected: 80, Actual: 178]
- MD013:450: [Expected: 80, Actual: 141]
- MD013:452: [Expected: 80, Actual: 100]
- MD025:454:
- MD013:456: [Expected: 80, Actual: 564]
- MD013:458: [Expected: 80, Actual: 681]
- MD013:468: [Expected: 80, Actual: 179]
- MD033:470: [Element: details]
- MD036:475:
- MD013:479: [Expected: 80, Actual: 120]
- MD013:498: [Expected: 80, Actual: 188]
- MD033:500: [Element: details]
- MD036:505:
- MD013:509: [Expected: 80, Actual: 88]
- MD013:528: [Expected: 80, Actual: 248]
- MD033:530: [Element: details]
- MD036:535:
- MD013:539: [Expected: 80, Actual: 106]
- MD013:556: [Expected: 80, Actual: 160]
- MD033:558: [Element: details]
- MD036:563:
- MD013:573: [Expected: 80, Actual: 123]
- MD036:575:
- MD013:587: [Expected: 80, Actual: 120]
- MD036:589:
