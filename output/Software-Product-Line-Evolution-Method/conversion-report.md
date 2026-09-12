# Conversion report — Software-Product-Line-Evolution-Method.pdf

- job_id: c4dc362a-006f-429b-b497-9c73c4b871ba
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=134347 completion=13935
- pipeline_version: 073654be6c457b411ab24a51dcfff4bdea2968daf6252a3e996dc1f6b48c7d48
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 173

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 98 | 0 | 200 | 13387 | 1259 | False |
| 2 | verified | 99 | 0 | 200 | 15194 | 1367 | False |
| 3 | verified | 98 | 0 | 200 | 16311 | 1365 | False |
| 4 | verified | 98 | 0 | 200 | 17601 | 1738 | False |
| 5 | verified | 98 | 0 | 200 | 16579 | 1523 | False |
| 6 | verified | 95 | 0 | 200 | 17953 | 1911 | False |
| 7 | verified | 99 | 0 | 200 | 18222 | 2973 | False |
| 8 | verified | 97 | 0 | 200 | 19100 | 1799 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 4
- converted to Mermaid: 1 (25%)
- data-table fallbacks: 0
- image fallbacks: 3

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 9 | flowchart | image | 68 |
| 6 | 10 | flowchart | image | 72 |
| 6 | 11 | xychart-beta | mermaid | 95 |
| 7 | 12 |  | image | 90 |

## Omissions log

- page 1: Two-column layout linearized: left column (abstract through section 1.1 start) then copyright block, then right column. No figures on page. Running page number "1207" excluded from body. No typos detected.
- page 2: Page continues section 1.3 bullet list and body text from page 1. No figures on this page. Table 1 referenced but appears on a later page. No uncertain characters. No typo corrections needed.
- page 3: Two-column layout linearized: left column completed through Section 3.1 and Table 1/2, then right column. Table 1 rendered as GFM table with row headers; source uses a diagonal-split header cell (decorative diagonal omitted, logged). "The core assets are consistent each other" left as-is per OCR (possible source typo of "consistent with each other"). Page number 1209 excluded from body.
- page 4: OCR reference for Table 3 contained "Mixture of Chain and Grain" — corrected to "Chaff" per page 3 ground truth (Table 1) and image. Blue arrow overlay (scenarios 1, 2, 3) rendered as figure placeholder since it cannot be represented in GFM. Note text on this page states "Type B's level of coverage is low" (source reads "Type B's level of coverage is low" — image says "coverage is low"? actually image says "Type B's level of coverage is low" — kept verbatim; note: contextually this refers to consistency ambiguity, kept as source).
- page 5: - Page contains Table 4 (transcribed as a GFM pipe table) and no figures. Figure 1 is referenced but appears on a later page.
- Running footer/page number "1211" excluded from body.
- Table 4 continuation from previous page: Table 4 begins on this page as a full-width table.
- Scenario entries rendered with <br> line breaks within table cells to preserve layout.
- page 6: Page 6 continues from page 5; section 5 body text appears on page 5, page 6 begins with Figure 1 caption and Section 6. Reading order: two-column, left column first. Corrections: none beyond standard formatting. Figure 2 axis values approximate; chart legend/table values (s12: -4.00, -6.50, -5.00, -2.75, -0.50, 1.75; s13: -3.00, -5.00, -3.40, -1.00, 1.40, 3.80) preserved in figure only. Equation typography rendered as LaTeX per source layout (equation block appears at top of right column on the printed page; placed inline in reading flow).
- page 7: - Table 5's three sub-tables contain hand-drawn blue circled annotations labeled (a)–(e); the annotations are represented via the figure placeholder and inline labels, the drawing itself omitted.
- Labels (d) and (e) point to cells: (d) = Total 12.25 in sub-table (1); (e) = Total 12.5 in sub-table (3); rendered inline as "(e)" next to the Modification row total and "(d)" below sub-table (1) as in the source layout.
- "advantageous of" retained as in source (possible source typo for "advantages").
- Continuation: page begins mid-sentence after the equation "(c) = (a) * (b)" from previous page; ends mid-sentence "into" continuing to next page.
- Equation "(c) = (a) * (b)" italicized in source.
- page 8: - Page continues Section 8 (Related Work) from previous page ("previous core assets" continues the sentence "(b) involves integrating another option, which is obtained through product development, into").
- OCR source rendered "n1" as italic subscript; rendered as $n_1$ [?]. Possibly "n" only.
- Reference [8]: "CUM/SEI-2003-TR-005" kept as printed (likely typo for CMU/SEI-2003-TR-005, DEC-009 allowance: left verbatim, noted).
- Reference [6]: "Gamma, E. Helms, R." kept as printed (likely missing comma after E.).
- Running footer page number "1214" excluded from body.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 562756B model=glm-5.3-flash effort=low transcribe_ms=6110.4 verify_ms=3168.3 ocr_ms=30689.8 retries=0 verification_score=98 floor=100% hashes=391aa4cf3b97b9d62aaa448de10642f7d87d3cae025ce59696d1c16ebf04ac1f/1c80001f10bc630667e4897c393cd9b39d7fb8c8add9fe13f358149d3db20470/971e4e0f69575d27810b4f1a2bc3ac16ef2efbe99eed21301dfd401198117919/228680fa308affd395dde9b954ecd2858935b785f6cd0a458f5642f52dc1c4e1
- page 2: dpi=200 image=1700x2200 647180B model=glm-5.3-flash effort=low transcribe_ms=6255.7 verify_ms=2946.2 ocr_ms=38587.6 retries=0 verification_score=99 floor=100% hashes=0aa803bb25678cca60bb1d57dfbd1d1a754085ea874dfd4ddfca526b01e49c8a/7931e2595fd2ae6f92735b4a03238e00f58dcbc1f6fa8dc94cc58376884f5cab/a1acfb6d6cb2f7a80de49b617d8c4a3eddebf446893a8806ed1362ec6100deab/8bf0ea1ee24edb80ffc5924686a65f546c3545412c38dcea26a74c804f07b13e
- page 3: dpi=200 image=1700x2200 607029B model=glm-5.3-flash effort=low transcribe_ms=7434.0 verify_ms=3162.4 ocr_ms=38517.9 retries=0 verification_score=98 floor=100% hashes=8dbae235d59eb195204cd9fa576093f34fcb378f4c91d99f999de32b083a361b/2de92b5f21157644475575363dc56b812584427dbc97e9931cff10f9974c74fc/10e18ea253f841116c66addf9e76e587e93d680f393d109e205088dfedfbcb2e/d9efaf4faba94687806ef9e57f3549c842266d4d74b78197e848a835cf112f57
- page 4: dpi=200 image=1700x2200 623396B model=glm-5.3-flash effort=low transcribe_ms=7880.4 verify_ms=3707.9 ocr_ms=38271.6 retries=0 verification_score=98 floor=100% hashes=b3075efd981a37d4be934876ab90227c69ba563282111d00e02f5982967f8d9e/260a030976afafda190615593c57904d96a92ac936bb46241decd7938cf8b1cb/6f1126412d607eb470652a33ca804a8506cdac9b878ef23344f63011b089bf1a/822ba822e43d4f43ba2dd15b0fad7438d8a36117b403f0345ac13073bce4ff36
- page 5: dpi=200 image=1700x2200 508625B model=glm-5.3-flash effort=low transcribe_ms=7034.0 verify_ms=3277.3 ocr_ms=18719.5 retries=0 verification_score=98 floor=100% hashes=5db4ed8d189827e7873145d244c59826c0aa5a22fc8630d1c25a70dcfc256ce0/6a483bc45c09b3213eb9e48f8688d76118cf9d1cc1ac173febc6ec24e7619883/f6c8d3c76fbaf321db92c63510173e9fc21f67cee031c8de4c4afe0acf1016ae/df1afd47072f74425def6c8a2dd94fc95292b5cf9b86fc40d7ce5ab4133fb996
- page 6: dpi=200 image=1700x2200 612054B model=glm-5.3-flash effort=low transcribe_ms=8070.0 verify_ms=3637.4 ocr_ms=38431.0 retries=0 verification_score=95 floor=100% hashes=d6967d7dc4c02401b861c1e7e9c5f5dbe44e3c5d6db28747fd2c44fdcc30f061/36673e9e179bf33417bbaedd603143f2467fdfe263433f4442ba1697b214f431/a8d6994e54c9bbc27f9e5997c860f8b2d253c2d157c49b8fdf47014d383401fe/91d662d9680d40d90662473e7bedb89632d1298a3e6a340d9d5cdbdd85e770d1
- page 7: dpi=200 image=1700x2200 634905B model=glm-5.3-flash effort=low transcribe_ms=11026.8 verify_ms=4148.5 ocr_ms=35048.7 retries=0 verification_score=99 floor=100% hashes=657b76fbcc18f9b4e359ce6d75edb0cfdfb6bc3393200a455d61cd93ee8c4876/1a448d204b230e02a8df63863f0af61fa27784c098a9be8fb8e0daf6cfe2b2ea/bc5495fb5bf4898ebfb96689e443729e03c4a28e4d9b1b5aa49fe39bfd28d24a/b1e4839b73af477f951615faea7367b5d3283d6d33fb67c400c01566da20a2d0
- page 8: dpi=200 image=1700x2200 636013B model=glm-5.3-flash effort=low transcribe_ms=8061.7 verify_ms=3368.6 ocr_ms=49613.6 retries=0 verification_score=97 floor=100% hashes=f6f68320cdfa89b14bf4b455e53e0f1325ad0a54f4c7353fbda4ccfa71361731/04ef84ffec47c2afd7a2b1a6fe91719101e7bc65981b5075ab0e7bb75d92901a/fa0f24d0b88cbaf7241ec2f2d1b3ac3a753e2b252a917124668642a60f2a3959/643bf1bc5832e8f212c8efd093291c909f72d167e8137660bba57877bb9a921e

## Figures placed without placeholder (appended at page end)

- page 7 index=1 alt='Table 5 with hand-drawn circled annotations (a), (b), (c), (d), (e)' reason=no placeholder token in markdown; appended at page end

## Lint warnings (non-fatal)

- MD013:50: [Expected: 80, Actual: 675]
- MD013:54: [Expected: 80, Actual: 156]
- MD013:68: [Expected: 80, Actual: 376]
- MD013:70: [Expected: 80, Actual: 761]
- MD013:74: [Expected: 80, Actual: 308]
- MD013:76: [Expected: 80, Actual: 372]
- MD013:78: [Expected: 80, Actual: 816]
- MD013:82: [Expected: 80, Actual: 269]
- MD013:84: [Expected: 80, Actual: 412]
- MD013:97: [Expected: 80, Actual: 813]
- MD013:99: [Expected: 80, Actual: 625]
- MD013:103: [Expected: 80, Actual: 343]
- MD013:105: [Expected: 80, Actual: 317]
- MD013:111: [Expected: 80, Actual: 424]
- MD013:113: [Expected: 80, Actual: 241]
- MD013:115: [Expected: 80, Actual: 435]
- MD013:119: [Expected: 80, Actual: 269]
- MD013:121: [Expected: 80, Actual: 206]
- MD013:125: [Expected: 80, Actual: 509]
- MD013:129: [Expected: 80, Actual: 296]
- MD013:131: [Expected: 80, Actual: 223]
- MD013:133: [Expected: 80, Actual: 188]
- MD013:135: [Expected: 80, Actual: 306]
- MD013:139: [Expected: 80, Actual: 154]
- MD013:141: [Expected: 80, Actual: 265]
- MD013:143: [Expected: 80, Actual: 106]
- MD013:145: [Expected: 80, Actual: 445]
- MD013:147: [Expected: 80, Actual: 220]
- MD013:149: [Expected: 80, Actual: 336]
- MD013:153: [Expected: 80, Actual: 102]
- MD013:154: [Expected: 80, Actual: 102]
- MD013:155: [Expected: 80, Actual: 102]
- MD013:156: [Expected: 80, Actual: 102]
- MD013:160: [Expected: 80, Actual: 501]
- MD013:173: [Expected: 80, Actual: 376]
- MD013:175: [Expected: 80, Actual: 428]
- MD013:177: [Expected: 80, Actual: 457]
- MD013:179: [Expected: 80, Actual: 214]
- MD013:181: [Expected: 80, Actual: 421]
- MD013:183: [Expected: 80, Actual: 142]
- MD013:185: [Expected: 80, Actual: 351]
- MD013:189: [Expected: 80, Actual: 184]
- MD013:191: [Expected: 80, Actual: 118]
- MD013:193: [Expected: 80, Actual: 323]
- MD013:195: [Expected: 80, Actual: 150]
- MD013:197: [Expected: 80, Actual: 343]
- MD013:199: [Expected: 80, Actual: 136]
- MD013:201: [Expected: 80, Actual: 149]
- MD013:205: [Expected: 80, Actual: 169]
- MD013:207: [Expected: 80, Actual: 160]
- MD013:209: [Expected: 80, Actual: 474]
- MD013:211: [Expected: 80, Actual: 557]
- MD013:213: [Expected: 80, Actual: 296]
- MD013:217: [Expected: 80, Actual: 270]
- MD013:221: [Expected: 80, Actual: 253]
- MD013:223: [Expected: 80, Actual: 172]
- MD013:225: [Expected: 80, Actual: 269]
- MD013:227: [Expected: 80, Actual: 98]
- MD013:229: [Expected: 80, Actual: 329]
- MD013:233: [Expected: 80, Actual: 195]
- MD013:237: [Expected: 80, Actual: 138]
- MD013:243: [Expected: 80, Actual: 408]
- MD013:247: [Expected: 80, Actual: 119]
- MD036:249:
- MD013:251: [Expected: 80, Actual: 107]
- MD013:252: [Expected: 80, Actual: 107]
- MD013:253: [Expected: 80, Actual: 107]
- MD013:254: [Expected: 80, Actual: 107]
- MD013:256: [Expected: 80, Actual: 374]
- MD013:260: [Expected: 80, Actual: 583]
- MD013:262: [Expected: 80, Actual: 167]
- MD013:266: [Expected: 80, Actual: 445]
- MD013:267: [Expected: 80, Actual: 445]
- MD013:268: [Expected: 80, Actual: 445]
- MD033:268: [Element: br]
- MD033:268: [Element: br]
- MD033:268: [Element: br]
- MD033:268: [Element: br]
- MD033:268: [Element: br]
- MD033:268: [Element: br]
- MD013:269: [Expected: 80, Actual: 445]
- MD033:269: [Element: br]
- MD013:270: [Expected: 80, Actual: 445]
- MD013:271: [Expected: 80, Actual: 445]
- MD013:272: [Expected: 80, Actual: 445]
- MD033:272: [Element: br]
- MD033:272: [Element: br]
- MD013:273: [Expected: 80, Actual: 445]
- MD033:273: [Element: br]
- MD013:274: [Expected: 80, Actual: 445]
- MD013:275: [Expected: 80, Actual: 445]
- MD013:276: [Expected: 80, Actual: 445]
- MD033:276: [Element: br]
- MD033:276: [Element: br]
- MD013:277: [Expected: 80, Actual: 445]
- MD013:278: [Expected: 80, Actual: 445]
- MD013:279: [Expected: 80, Actual: 445]
- MD033:279: [Element: br]
- MD033:279: [Element: br]
- MD033:279: [Element: br]
- MD033:279: [Element: br]
- MD033:279: [Element: br]
- MD033:279: [Element: br]
- MD013:281: [Expected: 80, Actual: 352]
- MD013:283: [Expected: 80, Actual: 355]
- MD013:287: [Expected: 80, Actual: 469]
- MD013:289: [Expected: 80, Actual: 303]
- MD013:296: [Expected: 80, Actual: 127]
- MD013:298: [Expected: 80, Actual: 124]
- MD013:300: [Expected: 80, Actual: 200]
- MD013:304: [Expected: 80, Actual: 102]
- MD013:306: [Expected: 80, Actual: 155]
- MD036:308:
- MD033:310: [Element: details]
- MD013:313: [Expected: 80, Actual: 269]
- MD013:323: [Expected: 80, Actual: 324]
- MD013:325: [Expected: 80, Actual: 413]
- MD013:327: [Expected: 80, Actual: 508]
- MD013:335: [Expected: 80, Actual: 318]
- MD013:337: [Expected: 80, Actual: 288]
- MD036:339:
- MD013:341: [Expected: 80, Actual: 127]
- MD013:343: [Expected: 80, Actual: 120]
- MD013:352: [Expected: 80, Actual: 334]
- MD013:354: [Expected: 80, Actual: 393]
- MD013:356: [Expected: 80, Actual: 481]
- MD013:367: [Expected: 80, Actual: 207]
- MD033:369: [Element: details]
- MD013:372: [Expected: 80, Actual: 156]
- MD036:374:
- MD033:376: [Element: details]
- MD013:379: [Expected: 80, Actual: 158]
- MD013:386: [Expected: 80, Actual: 440]
- MD013:388: [Expected: 80, Actual: 775]
- MD013:392: [Expected: 80, Actual: 146]
- MD013:396: [Expected: 80, Actual: 961]
- MD036:398:
- MD013:435: [Expected: 80, Actual: 201]
- MD013:437: [Expected: 80, Actual: 127]
- MD013:438: [Expected: 80, Actual: 98]
- MD013:439: [Expected: 80, Actual: 217]
- MD013:443: [Expected: 80, Actual: 145]
- MD013:445: [Expected: 80, Actual: 137]
- MD013:454: [Expected: 80, Actual: 402]
- MD013:456: [Expected: 80, Actual: 577]
- MD013:458: [Expected: 80, Actual: 253]
- MD013:460: [Expected: 80, Actual: 232]
- MD013:464: [Expected: 80, Actual: 420]
- MD013:466: [Expected: 80, Actual: 528]
- MD013:468: [Expected: 80, Actual: 378]
- MD036:472:
- MD013:474: [Expected: 80, Actual: 313]
- MD013:476: [Expected: 80, Actual: 916]
- MD013:478: [Expected: 80, Actual: 785]
- MD013:480: [Expected: 80, Actual: 243]
- MD013:482: [Expected: 80, Actual: 139]
- MD013:487: [Expected: 80, Actual: 96]
- MD013:492: [Expected: 80, Actual: 272]
- MD013:496: [Expected: 80, Actual: 281]
- MD013:498: [Expected: 80, Actual: 409]
- MD013:500: [Expected: 80, Actual: 356]
- MD013:504: [Expected: 80, Actual: 115]
- MD013:506: [Expected: 80, Actual: 190]
- MD013:508: [Expected: 80, Actual: 110]
- MD013:510: [Expected: 80, Actual: 86]
- MD013:512: [Expected: 80, Actual: 105]
- MD013:514: [Expected: 80, Actual: 148]
- MD013:516: [Expected: 80, Actual: 92]
- MD013:518: [Expected: 80, Actual: 134]
- MD013:520: [Expected: 80, Actual: 162]
- MD013:522: [Expected: 80, Actual: 170]
- MD013:524: [Expected: 80, Actual: 140]
- MD013:526: [Expected: 80, Actual: 173]
