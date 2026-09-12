# Conversion report — Open-Closed_Principle.pdf

- job_id: d705771d-747b-4cc7-a913-43fb0c6c451d
- status: assembling
- pages: 14
- wall-clock: not started
- tokens: prompt=353591 completion=16299
- pipeline_version: 49d37aab5011162c95b2267d3c52c5edb25ebd6d06ffb252038f28d3523593bc
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 86

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 100 | 0 | 200 | 12167 | 683 | False |
| 2 | needs_review | 92 | 2 | 400 | 50403 | 2550 | True |
| 3 | needs_review | 92 | 2 | 400 | 49857 | 2097 | True |
| 4 | verified | 95 | 0 | 200 | 12992 | 665 | False |
| 5 | verified | 95 | 1 | 300 | 32408 | 1402 | False |
| 6 | verified | 98 | 0 | 200 | 13494 | 753 | False |
| 7 | verified | 95 | 0 | 200 | 13076 | 715 | False |
| 8 | verified | 100 | 2 | 400 | 51461 | 1534 | False |
| 9 | verified | 95 | 0 | 200 | 13278 | 749 | False |
| 10 | verified | 98 | 0 | 200 | 13239 | 726 | False |
| 11 | verified | 96 | 0 | 200 | 13825 | 911 | False |
| 12 | needs_review | 88 | 2 | 400 | 51430 | 1741 | True |
| 13 | verified | 95 | 0 | 200 | 13204 | 828 | False |
| 14 | verified | 95 | 0 | 200 | 12757 | 945 | False |

## needs_review pages

[2, 3, 12]

## Diagram → Mermaid conversion

- figures: 8
- converted to Mermaid: 4 (50%)
- data-table fallbacks: 0
- image fallbacks: 4

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 2 | 8 | flowchart | image | 45 |
| 3 | 9 | classDiagram | mermaid | 95 |
| 14 | 10 | classDiagram | image | 75 |
| 14 | 11 | classDiagram | mermaid | 95 |
| 14 | 12 | classDiagram | mermaid | 95 |
| 14 | 13 | classDiagram | mermaid | 95 |
| 14 | 14 | sequenceDiagram | image | 78 |
| 14 | 15 | classDiagram | image | 88 |

## Omissions log

- page 1: Ligatures (ﬁ, ﬂ) corrected to standard characters. Footnote reference numbers rendered as superscripts (¹, ²). Small-caps paraphrase quote rendered as italic block quote. Page number "1" excluded from body and listed as furniture. No figures on this page.
- page 2: verification cap reached
- page 3: verification cap reached
- page 4: Listing box rendered as a fenced code block (bordered listing frame treated as code, not figure). The listing box title "Listing 1 (Continued) / Procedural Solution to the Square/Circle Problem" kept as text preceding the code block. Code block continues from previous page (Listing 1 began on page 3). Page ends mid-sentence ("...the predicates of the if"); continues on page 5. No figures on this page.
- page 5: Continuation from previous page: opening paragraph continues sentence about "if" statements. Listing 2 is presented in a boxed region in the source; transcribed as heading + fenced code block. No figures on this page. No typo corrections needed.
- page 6: No figures on this page. Footnote 3 reproduced as a GFM footnote. Header "Strategic Closure" and page number "6" excluded from body. No typos corrected.
- page 7: - Listing boxes rendered as fenced code blocks; heading lines "Listing 3/4/5" and captions preserved as bold/caption text. Heading "Using a "Data Driven" Approach to Achieve Closure." demoted to h2 to fit document outline pattern (previous section headings "Using Abstraction to Gain Explicit Closure." was h2).
- Continued from previous page: heading text "It should be very clear..." paragraph appears on this page below Listing 5 per image.
- No figures on page.
- page 8: Listing 6 code block continues on next page (cut off mid-function after "argOrd = i;"). Corrected curly quotes in "Circle" and "Square" string literals to straight quotes; log per DEC-009.
- page 9: - Corrected typo "begining" -> "beginning" (DEC-009 allowance).
- Listing 6 is a continuation from page 8; code block presented in reading order (boxed listing region transcribed as code, not treated as a figure).
- Inline code words (`Shape`, `DrawAllShapes`, etc.) rendered in code spans to reflect monospace emphasis in source.
- page 10: Listings 7 and 8 are boxed in the source (decorative borders omitted). Running header and page number excluded from body. Typo correction from rolling context not needed on this page; "begining" appears on prior page context only. No figures on this page.
- page 11: - Continuation: text ends mid-word ("How-") carrying to next page.
- Corrected source typo "pubic member variables" → "public member variables" (DEC-009 allowance).
- Inline code formatting applied to code identifiers (minutes, hours, public, private, etc.) consistent with prior pages.
- No figures on this page.
- page 12: verification cap reached
- page 13: - This page continues the code block started on the previous page (Listing 10); the `DrawSquaresOnly` function signature line appeared at the bottom of the prior page, so this page begins with the function body's opening brace.
- Paragraph "ever, nothing changes..." is a continuation of the hyphenated word "How-ever" from the previous page.
- Source typos left as-is per source fidelity vs. DEC-009: "yeilds" (yields), "strenghts" (strengths). Flagged but not corrected since they are in the OCR reference; noted for the log: yeilds→yields, strenghts→strengths.
- The boxed listing frame is rendered as a heading + fenced code block, not as a figure.
- Uncertain: none.
- page 14: This page is a full-page figure legend (Booch diagram notation key) that continues table-like boxed entries from the previous page; six boxed panels each contain a small diagram (rendered as FIG placeholders) plus descriptive text and code. Panel reading order: top-left, top-right, middle-left, middle-right, bottom-left, bottom-right. Page number "14" appears at bottom right and is excluded from body. Decorative script-style letters (A, B, D, P, V, M, "Set") inside diagrams are part of figure regions. No uncertain characters.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 278930B model=glm-5.3-flash effort=low transcribe_ms=4028.9 verify_ms=2839.8 ocr_ms=330.8 retries=0 verification_score=100 floor=98% hashes=79e4031eb3438ba67cc61a92a04de98b205b3a245956cdff692d05d8a263bf20/a441ddc0949c244cf94fc5e644e0a502b4b95fc20cf1f9a2a9c7bda59fb8f868/2af3b1ea8a3f302b75863208ca3ae4670f48ed05c0ccf0b8add1e6e1d428fdc1/abc7009a2f812d4915983bd08f0690ac41f268ee6b30ee5cc039173eec5082c6
- page 2: dpi=400 image=3400x4400 519735B model=glm-5.3-flash effort=low transcribe_ms=16141.1 verify_ms=10563.2 ocr_ms=1936.6 retries=2 verification_score=92 floor=95% hashes=0f7a6e0aea64fa7164bcc01c91cf50683af6ad989b336813f05bd97fb71c61f0/59965a1ec3baed5f40a8fa623c4245f6bcc4fa29d4822a14c1d93bc6d5f58725/72bb81595763517054b3bd69715f7fdc37f1d1ca226c510219f84a4f49ea6a00/0d25d9bb822811b277287a37130dd3540fa0e2009ce231d021547b63fca4b9cc
- page 3: dpi=400 image=3400x4400 370218B model=glm-5.3-flash effort=low transcribe_ms=13122.3 verify_ms=10895.2 ocr_ms=1693.4 retries=2 verification_score=92 floor=95% hashes=e4861ea62a4de7378298b00a570fb554a1cc40f278a3319799be0c82d5eb28c6/57af1306a841c04a142a832b90d7bb766e5d3e91c651aa87d3a1a87412663396/2054f1e425ff3cb2207f94d683051c5c79fb042efd2c181e7d66196b59a72683/feec3a1e186c3540af857058ed2219e59077cefe274949c4412ce1fa4c6c2124
- page 4: dpi=200 image=1700x2200 219943B model=glm-5.3-flash effort=low transcribe_ms=3961.5 verify_ms=2549.4 ocr_ms=340.6 retries=0 verification_score=95 floor=97% hashes=7061c8a51b4f5dc2402536f845a6e527fb2cb49921d4094bcd54a114622a4ad9/e9644c4b3abb5cdf038a5f13f39c74d680140aa6faec92f7202b436f6db293d1/d2b87de66fc20c7560ac0a7f587c39ca2de5af87a17fc4b42ebe5236425bd825/9b62dbe42adfe447db400046d453263a0b3413afbd08fa4794c6bb5a36ee1512
- page 5: dpi=300 image=2550x3300 395349B model=glm-5.3-flash effort=low transcribe_ms=9292.7 verify_ms=6171.7 ocr_ms=879.8 retries=1 verification_score=95 floor=99% hashes=2c8b30f217530d6af59bc8e25baa681604393fe2fc044170f5f8021e9c63b5e4/ecac07b7b9aaeabcbcb364c57c40fb51fe55e1527fadd589cc30158a4deba64e/1f245def6e343243e70bbfcecbdef1701acb07052306a4fdf028eefe1367fbd6/8c5835920ee0f4c08ecadec4166cc1be7f9b56954f55953ba38f9e0e69ebd683
- page 6: dpi=200 image=1700x2200 338554B model=glm-5.3-flash effort=low transcribe_ms=4465.4 verify_ms=2109.3 ocr_ms=358.3 retries=0 verification_score=98 floor=97% hashes=ee6beed23f81a06d97747ca9bf5b628d10ef9b24031c9256a4df782b2a5d9fbd/eaffc72fd8015bfa2009631217ca6d436cfab7c2d674dc4e845aba913397339d/6dab58cbfa2b323ccc1320ac4c63c3d99cc304ce302b5afcf62d38be48731547/7d11e32cf8affd9738414484b7cfa5c50e9bb2b5b87ed94cf3c51f8fa1d60998
- page 7: dpi=200 image=1700x2200 218236B model=glm-5.3-flash effort=low transcribe_ms=5466.6 verify_ms=3694.9 ocr_ms=300.2 retries=0 verification_score=95 floor=97% hashes=7da7883d76e769f0d013ba71bf3cb1d064353f6605cef593efdfb939310b1a75/0d9ae4e7169ff86fb6873aa458b672c657c07f5448fc7b12a23f83a71dcd36f4/b8ec40934472826afbfa0373fa2a96faac514f4ef1c5ebb30c622f08f65743cc/fb54accdadeba723d541a90ef792f0be82852b9b9e4b60145b67fc55b2c174a8
- page 8: dpi=400 image=3400x4400 371826B model=glm-5.3-flash effort=low transcribe_ms=14280.6 verify_ms=9739.7 ocr_ms=1758.6 retries=2 verification_score=100 floor=98% hashes=0aadaed0fd61a30c6b2be749eeb95b1593cfc1f183a3566d12b3dd8359a1e5c5/ec44e9ade76f33a390d868f6b5baf81654884ae6c4136e18b4a6a5e1ab18d29b/97ec79c6998b33069dd223be853a484b484198a0ad943732676439d72d348065/12ceeaca2aba8a36974b590886dcd2256c910e09d64bc3460c203a1c5bbbfa3b
- page 9: dpi=200 image=1700x2200 262623B model=glm-5.3-flash effort=low transcribe_ms=4528.2 verify_ms=3078.0 ocr_ms=363.6 retries=0 verification_score=95 floor=99% hashes=0cae54be9a452566e151ce93a2aef19f7744bf387f48e00cb097e78fe518cf78/38aa27b0e794753bc6a1101567c02608ce536e99c611bd30cf9934bf4bb9e30a/0da9032f3044d374ee6f43f8c474289ec4c2b8f973b9967b4adee260b06b03e9/8547f3855e9f217f1659664b4c7bb251e920c61140241c7fe28ff5c9f10f89dc
- page 10: dpi=200 image=1700x2200 270245B model=glm-5.3-flash effort=low transcribe_ms=4624.8 verify_ms=3030.8 ocr_ms=330.1 retries=0 verification_score=98 floor=98% hashes=17ab3eafce1959bb937f674efc201ec6c758424ff178cc0c4d50266db0400968/e9d90d4b58232e813eb64443d8fba757cd93d4d8003d1504cde1e2d12e9ca5f9/d9654efa4a405290fdf447dec4c69a22f3b2b8bbc9ddc6de1ac65f5d111e3224/4aa1a7f6a676cfc01de79fb2426fa204e49d2cd80cc6c148edfd6a15da598d61
- page 11: dpi=200 image=1700x2200 337729B model=glm-5.3-flash effort=low transcribe_ms=6171.6 verify_ms=2491.4 ocr_ms=333.1 retries=0 verification_score=96 floor=96% hashes=7ff803bf88aaec7f503d7f1e5f1532138995b252403036b664ad23c9672f80cf/d038a4225ad1f625a4ab1ea75a9dea763e93c55c9c0e55eaf7170b437f6a153f/5dddc1989efbb268e576871732dc7b6e6f034baadc51716020b1486fe5b574e1/4e8b04addcc614b92a59c8e6b462048d82c45d6fdcd2bb224cd5b64b35193fa3
- page 12: dpi=400 image=3400x4400 308360B model=glm-5.3-flash effort=low transcribe_ms=14628.0 verify_ms=10171.4 ocr_ms=1760.8 retries=2 verification_score=88 floor=96% hashes=dd274278986d57516625f3b55ce3da63aaa9788cbcf3812a8a7af8946a8b984d/0902d3873725706e71dec71e4095538233362b233998dd4c9fe93b861172674d/5e5801814b06e8fd1103ee3af30788b81dd60287ae5f7a85bc4a59fe3225914c/b10e112fdb62b14c0d339a8cdb7cb2b054d285caa5aa87c7c0bca78e6cf508f8
- page 13: dpi=200 image=1700x2200 217078B model=glm-5.3-flash effort=low transcribe_ms=6277.3 verify_ms=3457.1 ocr_ms=288.8 retries=0 verification_score=95 floor=98% hashes=4bbeb90e5bce2beba6d748b059bc561b74f247eaa4cf70823ada8672e71dd8a2/e144e559c831b9dd2244a6180d3081b490956168c8d4501313dcae2cfcbad70e/9004661dbccb99e730722808eabadcc08f895d6585bfc19ec54ed838463aec84/938f076448d9251ec2f7d59a3c5f70d51a47bb81172d34da5930bbe30c0948f5
- page 14: dpi=200 image=1700x2200 176295B model=glm-5.3-flash effort=low transcribe_ms=5741.8 verify_ms=3165.5 ocr_ms=328.8 retries=0 verification_score=95 floor=98% hashes=1640911cec68049b1b808517c3079b0943349d4e59e79ccf351c1f480517f055/aebff8bdf0b4d26b146fd7e6596962b9de3eb8f726e31dfd3e78a7a54428eff0/9b9ce83da0e6db00588ba13ed6d5c438f1fa3181272535621cff70a5e210ec99/a5764a61f2c393760f9aebfc73abc095a19fe2183f482f8ec823a09090794196

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:19: [Expected: 80, Actual: 469]
- MD013:21: [Expected: 80, Actual: 416]
- MD013:23: [Expected: 80, Actual: 408]
- MD013:25: [Expected: 80, Actual: 116]
- MD013:27: [Expected: 80, Actual: 513]
- MD025:29:
- MD013:35: [Expected: 80, Actual: 110]
- MD013:37: [Expected: 80, Actual: 83]
- MD013:41: [Expected: 80, Actual: 212]
- MD013:45: [Expected: 80, Actual: 102]
- MD013:47: [Expected: 80, Actual: 282]
- MD025:49:
- MD026:49:
- MD013:51: [Expected: 80, Actual: 564]
- MD013:53: [Expected: 80, Actual: 401]
- MD013:55: [Expected: 80, Actual: 125]
- MD036:57:
- MD013:62: [Expected: 80, Actual: 487]
- MD025:64:
- MD013:66: [Expected: 80, Actual: 336]
- MD013:68: [Expected: 80, Actual: 531]
- MD013:82: [Expected: 80, Actual: 172]
- MD033:84: [Element: details]
- MD013:87: [Expected: 80, Actual: 135]
- MD024:115:
- MD013:156: [Expected: 80, Actual: 359]
- MD013:158: [Expected: 80, Actual: 611]
- MD013:160: [Expected: 80, Actual: 290]
- MD013:162: [Expected: 80, Actual: 298]
- MD013:193: [Expected: 80, Actual: 343]
- MD013:195: [Expected: 80, Actual: 318]
- MD013:197: [Expected: 80, Actual: 211]
- MD025:199:
- MD013:201: [Expected: 80, Actual: 416]
- MD013:203: [Expected: 80, Actual: 430]
- MD026:205:
- MD013:207: [Expected: 80, Actual: 356]
- MD013:209: [Expected: 80, Actual: 378]
- MD013:211: [Expected: 80, Actual: 171]
- MD013:213: [Expected: 80, Actual: 404]
- MD013:215: [Expected: 80, Actual: 423]
- MD013:217: [Expected: 80, Actual: 115]
- MD013:261: [Expected: 80, Actual: 243]
- MD026:263:
- MD013:265: [Expected: 80, Actual: 171]
- MD013:267: [Expected: 80, Actual: 334]
- MD013:333: [Expected: 80, Actual: 242]
- MD026:335:
- MD013:337: [Expected: 80, Actual: 680]
- MD025:339:
- MD013:341: [Expected: 80, Actual: 240]
- MD026:343:
- MD013:345: [Expected: 80, Actual: 327]
- MD013:347: [Expected: 80, Actual: 291]
- MD013:349: [Expected: 80, Actual: 291]
- MD013:351: [Expected: 80, Actual: 341]
- MD013:364: [Expected: 80, Actual: 691]
- MD013:366: [Expected: 80, Actual: 459]
- MD036:368:
- MD013:384: [Expected: 80, Actual: 416]
- MD013:386: [Expected: 80, Actual: 526]
- MD013:388: [Expected: 80, Actual: 172]
- MD026:390:
- MD013:392: [Expected: 80, Actual: 415]
- MD013:394: [Expected: 80, Actual: 281]
- MD013:396: [Expected: 80, Actual: 500]
- MD026:398:
- MD013:400: [Expected: 80, Actual: 429]
- MD013:402: [Expected: 80, Actual: 178]
- MD013:472: [Expected: 80, Actual: 141]
- MD013:474: [Expected: 80, Actual: 100]
- MD025:476:
- MD013:478: [Expected: 80, Actual: 564]
- MD013:480: [Expected: 80, Actual: 681]
- MD013:484: [Expected: 80, Actual: 120]
- MD013:504: [Expected: 80, Actual: 148]
- MD033:506: [Element: details]
- MD013:513: [Expected: 80, Actual: 88]
- MD013:531: [Expected: 80, Actual: 165]
- MD033:533: [Element: details]
- MD013:540: [Expected: 80, Actual: 106]
- MD013:553: [Expected: 80, Actual: 100]
- MD013:556: [Expected: 80, Actual: 139]
- MD033:558: [Element: details]
- MD013:571: [Expected: 80, Actual: 116]
- MD013:583: [Expected: 80, Actual: 132]
