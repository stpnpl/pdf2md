# Conversion report — Software-Product-Line-Evolution-Method.pdf

- job_id: e8880fb0-dfd8-4e2e-9ce6-0f911e86b7e4
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=134441 completion=12820
- pipeline_version: 073654be6c457b411ab24a51dcfff4bdea2968daf6252a3e996dc1f6b48c7d48
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 178

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 98 | 0 | 200 | 13393 | 1336 | False |
| 2 | verified | 99 | 0 | 200 | 15200 | 1469 | False |
| 3 | verified | 95 | 0 | 200 | 16323 | 1465 | False |
| 4 | verified | 98 | 0 | 200 | 17613 | 1683 | False |
| 5 | verified | 98 | 0 | 200 | 16588 | 1561 | False |
| 6 | verified | 97 | 0 | 200 | 17971 | 1610 | False |
| 7 | verified | 98 | 0 | 200 | 18233 | 1935 | False |
| 8 | verified | 98 | 0 | 200 | 19120 | 1761 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 4
- converted to Mermaid: 0 (0%)
- data-table fallbacks: 0
- image fallbacks: 4

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 48 | flowchart | image | 72 |
| 5 | 49 |  | image | 90 |
| 6 | 50 | flowchart | image | 80 |
| 6 | 51 |  | image | 0 |

## Omissions log

- page 1: Two-column layout linearized column-aware. The ACM copyright/permission block (bottom of left column, read after section 1.1) is rendered as a block quote. No figures on this page. Page number "1207" is a running footer, excluded from body. No typos corrected; no uncertain characters.
- page 2: Two-column layout linearized left column then right column. Continuing list items (a)(b)(c) from "Our standard includes the following:" — rendered as plain paragraphs with hanging indent matching source. Continuation from page 1: "Kaizen activities include the following:" completes the sentence in section 1.3. Page continues mid-sentence ("An organization develops core") into next page. Source typo "thenselves" corrected to "themselves" per DEC-009. Page number 1208 appears at bottom center — listed as furniture, excluded from body.
- page 3: - Tables 1 and 2 rendered as GFM tables; source Table 1 uses a diagonal split header cell and shaded (green) cells, which cannot be represented in GFM (decorative styling omitted).
- Source heading "3. KAIZEN ACTIVITIES" italicizes Kaizen; rendered as "# 3. *KAIZEN* ACTIVITIES".
- Prior context: paragraph "(1) Harvesting core assets of existing feature" began on page 2 ("An organization develops core") and continues here from "assets of this type...".
- No figure placeholders: page contains only text and tables.
- No uncertain characters.
- page 4: - Table 3 region contains overlaid blue scenario arrows (1),(2),(3); rendered as figure placeholder with table reproduced in Markdown below it (header combined as "Level of Consistency / Level of Coverage" due to split diagonal header cell).
- OCR reference contains "Chain" for "Chaff" in Table 3 cell; corrected to "Chaff" per page 3 table (obvious OCR error, same table).
- Page number 1210 treated as footer furniture.
- page 5: - Table 4 spans the full page width at top; transcribed as a GFM pipe table but kept as figure placeholder for the original table region; table content reproduced verbatim in the markdown table.
- Two-column body linearized column by column (left column then right).
- Footer "1211" is a running page number, excluded from body.
- "s1. Harvesting-->Refactoring" arrows rendered as "-->" per source.
- No uncertain characters.
- page 6: - Page 6 begins mid-section 5 (Figure 1 diagram at top of left column belongs to Section 5, KAIZEN PROCESS, continued from previous page).
- Figure 2 placeholder covers the chart including the embedded data table beneath the plot area.
- No typos corrected; source text reproduced verbatim.
- page 7: - Table 5 sub-tables transcribed as GFM tables; annotation callouts (a)–(e) shown inline as text. Blue circle annotations in the source image omitted (decorative).
- "We have evaluated the advantageous of" — source typo retained per DEC-009 (should be "advantages").
- Page number "1213" appears at bottom center (footer).
- Reading order: left column then right column (two-column layout).
- page 8: - Two-column layout linearized column by column.
- Page number "1214" at bottom center excluded from body.
- Source reference [3] reads "Clements, P. and Northrop L." (missing period) — left as in source.
- Equation reproduced from source: subscript "n1" in "(Here, n₁ is the number of products...)" per source, though contextually the sum is over products; left verbatim.
- Reference [8] "CUM/SEI-2003-TR-005" is likely a typo for "CMU/SEI" but preserved verbatim as it appears in source.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 562756B model=glm-5.3-flash effort=low transcribe_ms=7531.9 verify_ms=3893.3 ocr_ms=30711.7 retries=0 verification_score=98 floor=100% hashes=391aa4cf3b97b9d62aaa448de10642f7d87d3cae025ce59696d1c16ebf04ac1f/1c80001f10bc630667e4897c393cd9b39d7fb8c8add9fe13f358149d3db20470/971e4e0f69575d27810b4f1a2bc3ac16ef2efbe99eed21301dfd401198117919/47d6acbc8b8b1ae9eccf4910c8d2bb3279c415f51da4b299b3e3a82734cf1cae
- page 2: dpi=200 image=1700x2200 647180B model=glm-5.3-flash effort=low transcribe_ms=8323.9 verify_ms=3221.8 ocr_ms=38146.2 retries=0 verification_score=99 floor=100% hashes=0aa803bb25678cca60bb1d57dfbd1d1a754085ea874dfd4ddfca526b01e49c8a/7931e2595fd2ae6f92735b4a03238e00f58dcbc1f6fa8dc94cc58376884f5cab/a1acfb6d6cb2f7a80de49b617d8c4a3eddebf446893a8806ed1362ec6100deab/11dd0a89115b8f55b5a0609c65108f50401f03c141293b45422db0190911a234
- page 3: dpi=200 image=1700x2200 607029B model=glm-5.3-flash effort=low transcribe_ms=8933.2 verify_ms=3149.3 ocr_ms=37639.1 retries=0 verification_score=95 floor=100% hashes=8dbae235d59eb195204cd9fa576093f34fcb378f4c91d99f999de32b083a361b/2de92b5f21157644475575363dc56b812584427dbc97e9931cff10f9974c74fc/10e18ea253f841116c66addf9e76e587e93d680f393d109e205088dfedfbcb2e/ec4a6717fe994dee0c5b7c7d9b5c28474f3b40e1c4bd1f765d036f76bbd28f3d
- page 4: dpi=200 image=1700x2200 623396B model=glm-5.3-flash effort=low transcribe_ms=8903.3 verify_ms=3432.4 ocr_ms=39848.3 retries=0 verification_score=98 floor=100% hashes=b3075efd981a37d4be934876ab90227c69ba563282111d00e02f5982967f8d9e/260a030976afafda190615593c57904d96a92ac936bb46241decd7938cf8b1cb/6f1126412d607eb470652a33ca804a8506cdac9b878ef23344f63011b089bf1a/c7ef7c48185e0e6e7a5f0a12efe807a96be10a80d8e2b115355ed13340145d4a
- page 5: dpi=200 image=1700x2200 508625B model=glm-5.3-flash effort=low transcribe_ms=8527.3 verify_ms=2794.2 ocr_ms=19482.4 retries=0 verification_score=98 floor=100% hashes=5db4ed8d189827e7873145d244c59826c0aa5a22fc8630d1c25a70dcfc256ce0/6a483bc45c09b3213eb9e48f8688d76118cf9d1cc1ac173febc6ec24e7619883/f6c8d3c76fbaf321db92c63510173e9fc21f67cee031c8de4c4afe0acf1016ae/9703b1919aff58e710e9198659962cbd0417048881d220d3e75493d57ceeead5
- page 6: dpi=200 image=1700x2200 612054B model=glm-5.3-flash effort=low transcribe_ms=8935.9 verify_ms=3560.0 ocr_ms=41348.2 retries=0 verification_score=97 floor=100% hashes=d6967d7dc4c02401b861c1e7e9c5f5dbe44e3c5d6db28747fd2c44fdcc30f061/36673e9e179bf33417bbaedd603143f2467fdfe263433f4442ba1697b214f431/a8d6994e54c9bbc27f9e5997c860f8b2d253c2d157c49b8fdf47014d383401fe/aba3310965add3ba345981921bf09354473607a8feffe7975e276fb58d25420c
- page 7: dpi=200 image=1700x2200 634905B model=glm-5.3-flash effort=low transcribe_ms=11052.1 verify_ms=3253.7 ocr_ms=37371.7 retries=0 verification_score=98 floor=100% hashes=657b76fbcc18f9b4e359ce6d75edb0cfdfb6bc3393200a455d61cd93ee8c4876/1a448d204b230e02a8df63863f0af61fa27784c098a9be8fb8e0daf6cfe2b2ea/bc5495fb5bf4898ebfb96689e443729e03c4a28e4d9b1b5aa49fe39bfd28d24a/0217de5877906a861043e7685bf66617db1921ae4250942259f412991f41f932
- page 8: dpi=200 image=1700x2200 636013B model=glm-5.3-flash effort=low transcribe_ms=8544.9 verify_ms=3036.9 ocr_ms=49851.1 retries=0 verification_score=98 floor=100% hashes=f6f68320cdfa89b14bf4b455e53e0f1325ad0a54f4c7353fbda4ccfa71361731/04ef84ffec47c2afd7a2b1a6fe91719101e7bc65981b5075ab0e7bb75d92901a/fa0f24d0b88cbaf7241ec2f2d1b3ac3a753e2b252a917124668642a60f2a3959/b0ad7d5e4beb87f50d0a390d4db0f80ea4fa65903488f13e034996f89e05fc58

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:53: [Expected: 80, Actual: 675]
- MD013:57: [Expected: 80, Actual: 156]
- MD025:67:
- MD013:71: [Expected: 80, Actual: 376]
- MD013:73: [Expected: 80, Actual: 761]
- MD013:75: [Expected: 80, Actual: 412]
- MD013:81: [Expected: 80, Actual: 308]
- MD013:83: [Expected: 80, Actual: 372]
- MD013:85: [Expected: 80, Actual: 816]
- MD013:89: [Expected: 80, Actual: 269]
- MD013:101: [Expected: 80, Actual: 813]
- MD013:103: [Expected: 80, Actual: 625]
- MD013:107: [Expected: 80, Actual: 343]
- MD013:109: [Expected: 80, Actual: 317]
- MD013:118: [Expected: 80, Actual: 424]
- MD013:120: [Expected: 80, Actual: 241]
- MD013:122: [Expected: 80, Actual: 435]
- MD025:124:
- MD013:126: [Expected: 80, Actual: 269]
- MD013:128: [Expected: 80, Actual: 206]
- MD013:132: [Expected: 80, Actual: 509]
- MD013:136: [Expected: 80, Actual: 296]
- MD013:138: [Expected: 80, Actual: 223]
- MD013:140: [Expected: 80, Actual: 188]
- MD013:142: [Expected: 80, Actual: 306]
- MD013:146: [Expected: 80, Actual: 154]
- MD013:148: [Expected: 80, Actual: 265]
- MD013:150: [Expected: 80, Actual: 106]
- MD013:152: [Expected: 80, Actual: 445]
- MD013:154: [Expected: 80, Actual: 220]
- MD013:156: [Expected: 80, Actual: 336]
- MD013:160: [Expected: 80, Actual: 98]
- MD013:161: [Expected: 80, Actual: 98]
- MD013:162: [Expected: 80, Actual: 98]
- MD013:163: [Expected: 80, Actual: 98]
- MD025:165:
- MD013:167: [Expected: 80, Actual: 501]
- MD013:180: [Expected: 80, Actual: 376]
- MD013:182: [Expected: 80, Actual: 428]
- MD013:184: [Expected: 80, Actual: 457]
- MD013:186: [Expected: 80, Actual: 214]
- MD013:188: [Expected: 80, Actual: 421]
- MD013:190: [Expected: 80, Actual: 142]
- MD013:192: [Expected: 80, Actual: 351]
- MD013:196: [Expected: 80, Actual: 184]
- MD013:198: [Expected: 80, Actual: 118]
- MD013:200: [Expected: 80, Actual: 323]
- MD013:202: [Expected: 80, Actual: 150]
- MD013:204: [Expected: 80, Actual: 343]
- MD013:206: [Expected: 80, Actual: 136]
- MD013:208: [Expected: 80, Actual: 149]
- MD013:212: [Expected: 80, Actual: 169]
- MD013:214: [Expected: 80, Actual: 160]
- MD013:216: [Expected: 80, Actual: 474]
- MD013:218: [Expected: 80, Actual: 557]
- MD013:220: [Expected: 80, Actual: 296]
- MD025:222:
- MD013:224: [Expected: 80, Actual: 270]
- MD013:228: [Expected: 80, Actual: 253]
- MD013:230: [Expected: 80, Actual: 172]
- MD013:232: [Expected: 80, Actual: 269]
- MD013:234: [Expected: 80, Actual: 98]
- MD013:236: [Expected: 80, Actual: 329]
- MD013:240: [Expected: 80, Actual: 195]
- MD013:244: [Expected: 80, Actual: 138]
- MD013:250: [Expected: 80, Actual: 408]
- MD013:254: [Expected: 80, Actual: 128]
- MD036:256:
- MD013:258: [Expected: 80, Actual: 106]
- MD013:259: [Expected: 80, Actual: 106]
- MD013:260: [Expected: 80, Actual: 106]
- MD013:261: [Expected: 80, Actual: 106]
- MD013:263: [Expected: 80, Actual: 374]
- MD013:267: [Expected: 80, Actual: 583]
- MD013:269: [Expected: 80, Actual: 167]
- MD013:273: [Expected: 80, Actual: 151]
- MD036:275:
- MD013:277: [Expected: 80, Actual: 445]
- MD013:278: [Expected: 80, Actual: 445]
- MD013:279: [Expected: 80, Actual: 445]
- MD033:279: [Element: br]
- MD033:279: [Element: br]
- MD033:279: [Element: br]
- MD033:279: [Element: br]
- MD033:279: [Element: br]
- MD033:279: [Element: br]
- MD013:280: [Expected: 80, Actual: 445]
- MD033:280: [Element: br]
- MD013:281: [Expected: 80, Actual: 445]
- MD013:282: [Expected: 80, Actual: 445]
- MD013:283: [Expected: 80, Actual: 445]
- MD033:283: [Element: br]
- MD033:283: [Element: br]
- MD013:284: [Expected: 80, Actual: 445]
- MD033:284: [Element: br]
- MD013:285: [Expected: 80, Actual: 445]
- MD013:286: [Expected: 80, Actual: 445]
- MD013:287: [Expected: 80, Actual: 445]
- MD033:287: [Element: br]
- MD033:287: [Element: br]
- MD013:288: [Expected: 80, Actual: 445]
- MD013:289: [Expected: 80, Actual: 445]
- MD013:290: [Expected: 80, Actual: 445]
- MD033:290: [Element: br]
- MD033:290: [Element: br]
- MD033:290: [Element: br]
- MD033:290: [Element: br]
- MD033:290: [Element: br]
- MD033:290: [Element: br]
- MD013:292: [Expected: 80, Actual: 352]
- MD013:294: [Expected: 80, Actual: 355]
- MD025:296:
- MD013:298: [Expected: 80, Actual: 469]
- MD013:300: [Expected: 80, Actual: 303]
- MD013:307: [Expected: 80, Actual: 125]
- MD013:309: [Expected: 80, Actual: 122]
- MD013:311: [Expected: 80, Actual: 200]
- MD013:315: [Expected: 80, Actual: 102]
- MD036:319:
- MD025:323:
- MD013:327: [Expected: 80, Actual: 324]
- MD013:329: [Expected: 80, Actual: 413]
- MD013:331: [Expected: 80, Actual: 508]
- MD013:339: [Expected: 80, Actual: 318]
- MD013:341: [Expected: 80, Actual: 288]
- MD036:343:
- MD013:345: [Expected: 80, Actual: 127]
- MD013:356: [Expected: 80, Actual: 334]
- MD013:358: [Expected: 80, Actual: 393]
- MD013:360: [Expected: 80, Actual: 481]
- MD036:364:
- MD013:368: [Expected: 80, Actual: 440]
- MD013:370: [Expected: 80, Actual: 775]
- MD013:374: [Expected: 80, Actual: 146]
- MD013:378: [Expected: 80, Actual: 961]
- MD036:380:
- MD036:382:
- MD036:392:
- MD036:401:
- MD013:415: [Expected: 80, Actual: 201]
- MD013:417: [Expected: 80, Actual: 127]
- MD013:418: [Expected: 80, Actual: 98]
- MD013:419: [Expected: 80, Actual: 217]
- MD025:421:
- MD013:423: [Expected: 80, Actual: 145]
- MD013:425: [Expected: 80, Actual: 137]
- MD013:434: [Expected: 80, Actual: 402]
- MD013:436: [Expected: 80, Actual: 577]
- MD013:438: [Expected: 80, Actual: 253]
- MD013:440: [Expected: 80, Actual: 232]
- MD025:442:
- MD013:444: [Expected: 80, Actual: 420]
- MD013:446: [Expected: 80, Actual: 528]
- MD013:448: [Expected: 80, Actual: 378]
- MD013:450: [Expected: 80, Actual: 313]
- MD013:452: [Expected: 80, Actual: 916]
- MD013:454: [Expected: 80, Actual: 785]
- MD013:456: [Expected: 80, Actual: 243]
- MD013:458: [Expected: 80, Actual: 139]
- MD013:463: [Expected: 80, Actual: 96]
- MD013:468: [Expected: 80, Actual: 294]
- MD025:470:
- MD013:472: [Expected: 80, Actual: 281]
- MD013:474: [Expected: 80, Actual: 409]
- MD013:476: [Expected: 80, Actual: 356]
- MD025:478:
- MD013:480: [Expected: 80, Actual: 115]
- MD013:482: [Expected: 80, Actual: 190]
- MD013:484: [Expected: 80, Actual: 110]
- MD013:486: [Expected: 80, Actual: 86]
- MD013:488: [Expected: 80, Actual: 105]
- MD013:490: [Expected: 80, Actual: 148]
- MD013:492: [Expected: 80, Actual: 92]
- MD013:494: [Expected: 80, Actual: 132]
- MD013:496: [Expected: 80, Actual: 162]
- MD013:498: [Expected: 80, Actual: 170]
- MD013:500: [Expected: 80, Actual: 140]
- MD013:502: [Expected: 80, Actual: 173]
