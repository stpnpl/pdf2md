# Conversion report — Software-Product-Line-Evolution-Method.pdf

- job_id: 71f614b6-d0b3-4066-ab1a-77986e0d32c3
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=204893 completion=18035
- pipeline_version: 073654be6c457b411ab24a51dcfff4bdea2968daf6252a3e996dc1f6b48c7d48
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 166

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 95 | 0 | 200 | 13388 | 1264 | False |
| 2 | verified | 98 | 0 | 200 | 15189 | 1512 | False |
| 3 | verified | 97 | 0 | 200 | 16302 | 1372 | False |
| 4 | verified | 96 | 1 | 300 | 41517 | 3407 | False |
| 5 | verified | 98 | 1 | 300 | 38822 | 2817 | False |
| 6 | verified | 96 | 1 | 300 | 42293 | 3874 | False |
| 7 | verified | 97 | 0 | 200 | 18241 | 2047 | False |
| 8 | verified | 98 | 0 | 200 | 19141 | 1742 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 4
- converted to Mermaid: 2 (50%)
- data-table fallbacks: 0
- image fallbacks: 2

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 83 | flowchart | mermaid | 88 |
| 6 | 84 | flowchart | image | 88 |
| 6 | 85 | xychart-beta | mermaid | 95 |
| 7 | 86 |  | image | 95 |

## Omissions log

- page 1: Two-column layout linearized column by column; copyright/permission block (left column bottom) placed after section 1.1 in reading order. Page number "1207" is a paper ID printed at bottom center, excluded from body. No figures on page. No typo corrections needed.
- page 2: Two-column layout linearized in reading order (left column completed, then right column). Page number 1208 in footer excluded from body. Section 1.4 heading continued from previous page context. No figures on this page. No typos requiring correction observed.
- page 3: Two-column layout linearized column by column; Table 1 header row rendered with empty leading cell (source has diagonal split cell). Section heading "3. KAIZEN ACTIVITIES" italicized as "*KAIZEN*" per source emphasis. No figures on page; page number 1209 excluded from body.
- page 4: - Table 3 rendered both as figure placeholder (diagram with scenario arrows (1),(2),(3) over the matrix) and as GFM pipe table per verification miss fix; table header uses "Consistent/Inconsistent Core Assets" with rows keyed by coverage.
- OCR ground truth for Table 3 read "Mixture of Chain and Grain" — corrected to "Chaff and Grain" for consistency with Table 1 on the prior page (logged as correction).
- Page number 1210 appears at page bottom center; excluded from body, listed in furniture.
- No uncertain characters.
- page 5: Table 4 rendered as GFM pipe table; multi-line Scenario cells joined with semicolons to preserve all s1–s30 entries. Caption "Table 4. Kaizen patterns" transcribed in bold. No figure regions on this page (Figure 1 referenced in text but appears on next page). Page number 1211 listed under furniture, excluded from body. Table header row has green background in source (decorative, omitted).
- page 6: - Two-column layout linearized: left column (Figure 1, sections 6.1–6.2 through "(2) Analyzing scenarios" intro) followed by right column (equation, Figure 2 discussion, Table 5 lead-in).
- Figure 2 chart embeds a data table (s12: −4.00, −6.50, −5.00, −2.75, −0.50, 1.75; s13: −3.00, −5.00, −3.40, −1.00, 1.40, 3.80 for 05a–07b), not transcribed as text; retained in figure placeholder.
- No text corrections made this page.
- page 7: - Page number on this page is "1213" (conference proceedings page numbering), listed as furniture, not body.
- Table 5 sub-tables (a), (b), (c) with circled markers (a)-(e) rendered as GFM tables; circled annotations kept as text labels.
- Continued from previous page: equation "(c) = (a) * (b)" begins this page (end of Table 5 description).
- Text ends mid-sentence "into" — continues on next page (section 8).
- "advantageous" left as in source (likely "advantages" typo, not corrected per source fidelity).
- OCR reference ground truth matched; no uncertain characters.
- page 8: Two-column layout linearized left column first, then right column. This page is a continuation of Section 8 (Related Work) from the previous page. Equation from image rendered as LaTeX; subscripts (evo, org, cab, unique, reuse) preserved. Reference [6]: "Gamma, E. Helms, R." lacks comma after "E." in source (typo allowed, kept as-is to stay verbatim). Reference [8] "CUM/SEI-2003-TR-005" likely a typo for "CMU/SEI" — kept as source per DEC-009. Equation continuation "Cost savings =" split across lines in source, merged into single display equation. Footer page number "1214" excluded from body.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 562756B model=glm-5.3-flash effort=low transcribe_ms=7078.4 verify_ms=3210.1 ocr_ms=31692.2 retries=0 verification_score=95 floor=100% hashes=391aa4cf3b97b9d62aaa448de10642f7d87d3cae025ce59696d1c16ebf04ac1f/1c80001f10bc630667e4897c393cd9b39d7fb8c8add9fe13f358149d3db20470/971e4e0f69575d27810b4f1a2bc3ac16ef2efbe99eed21301dfd401198117919/3082ce468f0998c5f24169da025356b1ee176fef1f0ff45d6e02fab02114607b
- page 2: dpi=200 image=1700x2200 647180B model=glm-5.3-flash effort=low transcribe_ms=8151.6 verify_ms=3607.3 ocr_ms=38670.1 retries=0 verification_score=98 floor=100% hashes=0aa803bb25678cca60bb1d57dfbd1d1a754085ea874dfd4ddfca526b01e49c8a/7931e2595fd2ae6f92735b4a03238e00f58dcbc1f6fa8dc94cc58376884f5cab/a1acfb6d6cb2f7a80de49b617d8c4a3eddebf446893a8806ed1362ec6100deab/17b5d9b5fe7eab64d4f9fd23303a8101ff4d25caa47a559280447d6e77f93790
- page 3: dpi=200 image=1700x2200 607029B model=glm-5.3-flash effort=low transcribe_ms=7496.4 verify_ms=3676.7 ocr_ms=39382.5 retries=0 verification_score=97 floor=100% hashes=8dbae235d59eb195204cd9fa576093f34fcb378f4c91d99f999de32b083a361b/2de92b5f21157644475575363dc56b812584427dbc97e9931cff10f9974c74fc/10e18ea253f841116c66addf9e76e587e93d680f393d109e205088dfedfbcb2e/019145f11d48e6258c6cad882a2b5bc70278082e1c97d1d2c2577f1443fb55f1
- page 4: dpi=300 image=2550x3300 882656B model=glm-5.3-flash effort=low transcribe_ms=18419.9 verify_ms=8639.2 ocr_ms=84309.7 retries=1 verification_score=96 floor=100% hashes=b3075efd981a37d4be934876ab90227c69ba563282111d00e02f5982967f8d9e/ed648696345f84ef70192f5827e777a4f5c16891a2b345ec8a829547be636de9/6f1126412d607eb470652a33ca804a8506cdac9b878ef23344f63011b089bf1a/ff812962c79dc3c345bfb50bf13d4d832fb8a1cad554182033cb8296f62540f8
- page 5: dpi=300 image=2550x3300 680321B model=glm-5.3-flash effort=low transcribe_ms=16854.9 verify_ms=8179.3 ocr_ms=43822.3 retries=1 verification_score=98 floor=100% hashes=5db4ed8d189827e7873145d244c59826c0aa5a22fc8630d1c25a70dcfc256ce0/342120b9cc91772e3bd9b5437a6fa9d8e5027d642dd38510e3300f2f45b77959/f6c8d3c76fbaf321db92c63510173e9fc21f67cee031c8de4c4afe0acf1016ae/d3768e8e521d454abcd5947eb41561e3eeaa21cb31b0f8d1c01fc43f0f2495e9
- page 6: dpi=300 image=2550x3300 808649B model=glm-5.3-flash effort=low transcribe_ms=17575.7 verify_ms=11584.7 ocr_ms=91022.2 retries=1 verification_score=96 floor=100% hashes=d6967d7dc4c02401b861c1e7e9c5f5dbe44e3c5d6db28747fd2c44fdcc30f061/35b90e3c59f7e170ed5b14afec6ba32869814174bdf3fb7fc67e1e6d478104c2/a8d6994e54c9bbc27f9e5997c860f8b2d253c2d157c49b8fdf47014d383401fe/7ccd4aa9fd07fb42e9de0867874c497e85f98b3c6522c80952368b9ac4c01829
- page 7: dpi=200 image=1700x2200 634905B model=glm-5.3-flash effort=low transcribe_ms=11672.9 verify_ms=3478.8 ocr_ms=39140.5 retries=0 verification_score=97 floor=100% hashes=657b76fbcc18f9b4e359ce6d75edb0cfdfb6bc3393200a455d61cd93ee8c4876/1a448d204b230e02a8df63863f0af61fa27784c098a9be8fb8e0daf6cfe2b2ea/bc5495fb5bf4898ebfb96689e443729e03c4a28e4d9b1b5aa49fe39bfd28d24a/c28f2889580d6d3283ca4db704572741e084597777c87c863992850934a3b656
- page 8: dpi=200 image=1700x2200 636013B model=glm-5.3-flash effort=low transcribe_ms=7790.0 verify_ms=3281.2 ocr_ms=51525.2 retries=0 verification_score=98 floor=100% hashes=f6f68320cdfa89b14bf4b455e53e0f1325ad0a54f4c7353fbda4ccfa71361731/04ef84ffec47c2afd7a2b1a6fe91719101e7bc65981b5075ab0e7bb75d92901a/fa0f24d0b88cbaf7241ec2f2d1b3ac3a753e2b252a917124668642a60f2a3959/e30b45d51accf8ee12c21507dfbd33c5dfbac46ed013e8298ad350d785e9330d

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:50: [Expected: 80, Actual: 675]
- MD013:54: [Expected: 80, Actual: 156]
- MD025:64:
- MD013:68: [Expected: 80, Actual: 376]
- MD013:70: [Expected: 80, Actual: 761]
- MD013:72: [Expected: 80, Actual: 412]
- MD013:78: [Expected: 80, Actual: 308]
- MD013:80: [Expected: 80, Actual: 372]
- MD013:82: [Expected: 80, Actual: 816]
- MD013:86: [Expected: 80, Actual: 269]
- MD013:97: [Expected: 80, Actual: 813]
- MD013:99: [Expected: 80, Actual: 625]
- MD013:103: [Expected: 80, Actual: 343]
- MD013:105: [Expected: 80, Actual: 317]
- MD013:113: [Expected: 80, Actual: 424]
- MD013:115: [Expected: 80, Actual: 241]
- MD013:117: [Expected: 80, Actual: 435]
- MD025:119:
- MD013:121: [Expected: 80, Actual: 269]
- MD013:123: [Expected: 80, Actual: 206]
- MD013:127: [Expected: 80, Actual: 509]
- MD013:131: [Expected: 80, Actual: 296]
- MD013:133: [Expected: 80, Actual: 223]
- MD013:135: [Expected: 80, Actual: 188]
- MD013:137: [Expected: 80, Actual: 306]
- MD013:141: [Expected: 80, Actual: 154]
- MD013:143: [Expected: 80, Actual: 265]
- MD013:145: [Expected: 80, Actual: 106]
- MD013:147: [Expected: 80, Actual: 445]
- MD013:149: [Expected: 80, Actual: 220]
- MD013:151: [Expected: 80, Actual: 336]
- MD013:155: [Expected: 80, Actual: 98]
- MD013:156: [Expected: 80, Actual: 98]
- MD013:157: [Expected: 80, Actual: 98]
- MD013:158: [Expected: 80, Actual: 98]
- MD025:160:
- MD013:162: [Expected: 80, Actual: 501]
- MD013:175: [Expected: 80, Actual: 376]
- MD013:177: [Expected: 80, Actual: 428]
- MD013:179: [Expected: 80, Actual: 457]
- MD013:181: [Expected: 80, Actual: 214]
- MD013:183: [Expected: 80, Actual: 421]
- MD013:185: [Expected: 80, Actual: 142]
- MD013:187: [Expected: 80, Actual: 351]
- MD013:191: [Expected: 80, Actual: 184]
- MD013:193: [Expected: 80, Actual: 118]
- MD013:195: [Expected: 80, Actual: 323]
- MD013:197: [Expected: 80, Actual: 150]
- MD013:199: [Expected: 80, Actual: 343]
- MD013:201: [Expected: 80, Actual: 136]
- MD013:203: [Expected: 80, Actual: 149]
- MD013:207: [Expected: 80, Actual: 169]
- MD013:209: [Expected: 80, Actual: 160]
- MD013:211: [Expected: 80, Actual: 474]
- MD013:213: [Expected: 80, Actual: 557]
- MD013:215: [Expected: 80, Actual: 296]
- MD025:217:
- MD013:219: [Expected: 80, Actual: 270]
- MD013:223: [Expected: 80, Actual: 253]
- MD013:225: [Expected: 80, Actual: 174]
- MD013:227: [Expected: 80, Actual: 271]
- MD013:229: [Expected: 80, Actual: 100]
- MD013:231: [Expected: 80, Actual: 331]
- MD013:235: [Expected: 80, Actual: 195]
- MD013:239: [Expected: 80, Actual: 138]
- MD013:245: [Expected: 80, Actual: 408]
- MD013:252: [Expected: 80, Actual: 114]
- MD013:262: [Expected: 80, Actual: 267]
- MD033:264: [Element: details]
- MD013:267: [Expected: 80, Actual: 122]
- MD036:269:
- MD013:273: [Expected: 80, Actual: 98]
- MD013:274: [Expected: 80, Actual: 98]
- MD013:275: [Expected: 80, Actual: 98]
- MD013:276: [Expected: 80, Actual: 98]
- MD013:278: [Expected: 80, Actual: 374]
- MD013:282: [Expected: 80, Actual: 583]
- MD013:284: [Expected: 80, Actual: 167]
- MD013:288: [Expected: 80, Actual: 433]
- MD013:289: [Expected: 80, Actual: 433]
- MD013:290: [Expected: 80, Actual: 433]
- MD013:291: [Expected: 80, Actual: 433]
- MD013:292: [Expected: 80, Actual: 433]
- MD013:293: [Expected: 80, Actual: 433]
- MD013:294: [Expected: 80, Actual: 433]
- MD013:295: [Expected: 80, Actual: 433]
- MD013:296: [Expected: 80, Actual: 433]
- MD013:297: [Expected: 80, Actual: 433]
- MD013:298: [Expected: 80, Actual: 433]
- MD013:299: [Expected: 80, Actual: 433]
- MD013:300: [Expected: 80, Actual: 433]
- MD013:301: [Expected: 80, Actual: 433]
- MD013:303: [Expected: 80, Actual: 352]
- MD013:305: [Expected: 80, Actual: 355]
- MD025:307:
- MD013:309: [Expected: 80, Actual: 469]
- MD013:311: [Expected: 80, Actual: 303]
- MD013:318: [Expected: 80, Actual: 125]
- MD013:320: [Expected: 80, Actual: 122]
- MD013:322: [Expected: 80, Actual: 200]
- MD013:326: [Expected: 80, Actual: 102]
- MD036:330:
- MD025:334:
- MD013:338: [Expected: 80, Actual: 324]
- MD013:340: [Expected: 80, Actual: 413]
- MD013:342: [Expected: 80, Actual: 508]
- MD013:350: [Expected: 80, Actual: 318]
- MD013:352: [Expected: 80, Actual: 288]
- MD036:354:
- MD013:356: [Expected: 80, Actual: 127]
- MD013:358: [Expected: 80, Actual: 111]
- MD013:367: [Expected: 80, Actual: 334]
- MD013:369: [Expected: 80, Actual: 393]
- MD013:371: [Expected: 80, Actual: 481]
- MD013:382: [Expected: 80, Actual: 204]
- MD033:384: [Element: details]
- MD036:389:
- MD013:395: [Expected: 80, Actual: 438]
- MD013:397: [Expected: 80, Actual: 772]
- MD013:401: [Expected: 80, Actual: 145]
- MD013:405: [Expected: 80, Actual: 961]
- MD013:407: [Expected: 80, Actual: 145]
- MD036:409:
- MD036:411:
- MD036:413:
- MD036:423:
- MD036:432:
- MD013:446: [Expected: 80, Actual: 201]
- MD013:448: [Expected: 80, Actual: 127]
- MD013:449: [Expected: 80, Actual: 98]
- MD013:450: [Expected: 80, Actual: 217]
- MD025:452:
- MD013:454: [Expected: 80, Actual: 145]
- MD013:456: [Expected: 80, Actual: 137]
- MD013:465: [Expected: 80, Actual: 402]
- MD013:467: [Expected: 80, Actual: 577]
- MD013:469: [Expected: 80, Actual: 255]
- MD013:471: [Expected: 80, Actual: 232]
- MD025:473:
- MD013:475: [Expected: 80, Actual: 420]
- MD013:477: [Expected: 80, Actual: 528]
- MD013:479: [Expected: 80, Actual: 378]
- MD013:481: [Expected: 80, Actual: 313]
- MD013:483: [Expected: 80, Actual: 916]
- MD013:485: [Expected: 80, Actual: 785]
- MD013:487: [Expected: 80, Actual: 243]
- MD013:489: [Expected: 80, Actual: 128]
- MD013:494: [Expected: 80, Actual: 94]
- MD013:499: [Expected: 80, Actual: 290]
- MD025:501:
- MD013:503: [Expected: 80, Actual: 281]
- MD013:505: [Expected: 80, Actual: 409]
- MD013:507: [Expected: 80, Actual: 356]
- MD025:509:
- MD013:511: [Expected: 80, Actual: 115]
- MD013:513: [Expected: 80, Actual: 190]
- MD013:515: [Expected: 80, Actual: 110]
- MD013:517: [Expected: 80, Actual: 86]
- MD013:519: [Expected: 80, Actual: 105]
- MD013:521: [Expected: 80, Actual: 148]
- MD013:523: [Expected: 80, Actual: 92]
- MD013:525: [Expected: 80, Actual: 132]
- MD013:527: [Expected: 80, Actual: 162]
- MD013:529: [Expected: 80, Actual: 170]
- MD013:531: [Expected: 80, Actual: 140]
- MD013:533: [Expected: 80, Actual: 173]
