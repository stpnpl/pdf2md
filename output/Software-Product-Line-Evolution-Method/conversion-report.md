# Conversion report — Software-Product-Line-Evolution-Method.pdf

- job_id: 06bc6f48-834b-45fc-a396-3afbda698fc7
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=263614 completion=23679
- pipeline_version: 49d37aab5011162c95b2267d3c52c5edb25ebd6d06ffb252038f28d3523593bc
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 164

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 98 | 0 | 200 | 13852 | 1228 | False |
| 2 | verified | 99 | 0 | 200 | 15448 | 1421 | False |
| 3 | verified | 98 | 0 | 200 | 16703 | 1456 | False |
| 4 | verified | 96 | 2 | 400 | 66677 | 5350 | False |
| 5 | verified | 98 | 0 | 200 | 18018 | 1620 | False |
| 6 | verified | 96 | 0 | 200 | 18215 | 1797 | False |
| 7 | verified | 97 | 2 | 400 | 70058 | 7062 | False |
| 8 | verified | 97 | 1 | 300 | 44643 | 3745 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 4
- converted to Mermaid: 2 (50%)
- data-table fallbacks: 0
- image fallbacks: 2

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 24 | flowchart | image | 85 |
| 6 | 25 | flowchart | mermaid | 85 |
| 6 | 26 | xychart-beta | mermaid | 98 |
| 7 | 27 |  | image | 90 |

## Omissions log

- page 1: Two-column layout linearized; copyright/permission block placed after the 1.1 section where it appears in the left column. OCR reference showed "[9] [10]" spaced; image shows "[9][10]" — kept image form. No figures on page. Page number "1207" excluded from body and listed as furniture.
- page 2: - Continuations: page begins mid-section (end of §1.3 list of kaizen activities continued from previous page); page ends mid-sentence in §2.3 Type A ("An organization develops core" continues on next page).
- Corrected "themselves" → "themselves" (source had "themselves" misspelled as "themselves" in OCR; rendered as standard form). No other corrections.
- Page number "1208" excluded from body; listed as furniture.
- page 3: - Two-column layout linearized: left column (continuation of section 2.3, Table 1, section 3 intro, Table 2, section 3.1, section 3.2 heading and start) followed by right column (continuation of 3.1 examples, 3.2 Detoxing).
- Tables 1 and 2 rendered as GFM tables; original table cells shaded light green (decorative, omitted).
- "The core assets are consistent each other" kept as in source (minor grammatical quirk in original).
- Page number "1209" appears at bottom center; excluded from body.
- page 4: - Table 3 transcribed as a GFM table; the arrow overlays (1), (2), (3) are graphical scenario paths and are represented by the FIG placeholder, not in the table cells.
- Corrected fullwidth "＊" after "[5]" in source to "]" followed by standard period; source had "refactoring  [5]．" with fullwidth period — normalized.
- Scenario headings (1)(2)(3) rendered as plain paragraphs per source layout.
- Page number "1210" listed in furniture (not body).
- page 5: - Table 4 caption title "Kaizen patterns" italicized per source emphasis convention for *kaizen*.
- Scenario lists in Table 4 were rendered as semicolon-separated items within a single cell to preserve GFM table structure; in the source they appear as multiple lines within each cell.
- Figure 1 (PDCA cycle diagram) is referenced in text but appears on a later page; no figure region on this page.
- OCR reference contained a stray FIG token from rolling context; not part of this page.
- page 6: - Page 6 of the document; the top of the page begins mid-document with Figure 1 completing the PDCA cycle discussion from Section 5 (which started on page 5).
- The OCR reference repeats the PDCA diagram text three times (duplicated OCR artifacts); only one diagram instance was used for Figure 1.
- Equation rendered as LaTeX math from the image; variable definitions preserved verbatim.
- Figure 1 caption in OCR reads "Figure 1.  Kaizen Processes" (two spaces collapsed to one).
- Page number footer "1212" excluded from body.
- Note: rolling context on page 5 included a stray figure token <!--FIG:page:1:1800,2210,3070,2870--> that does not appear on this page; no action taken.
- page 7: - Page continues Section 6.2 from previous page ("Verification misses" sentence completes in previous page's context; the equation "(c) = (a) * (b)" opens this page).
- Page number "1213" at bottom is a running page number; excluded from body per rules.
- Table 5 transcribed as three GFM tables from OCR ground truth; the hand-drawn blue annotation circles and leader lines with labels (a)–(e) could not be represented inline, so a FIG placeholder covers the Table 5 region (bbox estimated from image layout).
- "We have evaluated the advantageous of" — source typo retained per DEC-009 verbatim rule (should be "advantages").
- Source uses full-width commas (，) after "infrastructure-based evolution" and "branch-and-unite"; preserved.
- Section 8 RELATED WORK text ends mid-sentence ("into"); continues on next page.
- Subsection headings "(3) Defining Direction to Kaizen" and "6.3" rendered per document outline levels ((3) as bold item, 6.3 as ###).
- page 8: - Two-column layout linearized: left column first (Related Work continuation, equation, Section 9 start), then right column (Section 9 continuation, Section 10 References).
- The ROI equation and its variable definitions are typeset text, not a figure; rendered as LaTeX/display text. Inline blank spacing gaps around the equation in the source were omitted.
- "1214" at bottom center is a page number, excluded from body.
- "CUM/SEI-2003-TR-005" in reference [8] is likely a typo for "CMU/SEI" but left as-is (not an obvious standard-form correction within source style); noted.
- OCR context listed "indispensible" miss but page image shows "indispensable"; transcribed as "indispensable" — no correction needed.
- Full-width comma in "（Here, n1..." source rendered as standard parentheses per DEC-009 typo allowance.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 562756B model=glm-5.3-flash effort=low transcribe_ms=7116.3 verify_ms=2971.3 ocr_ms=450.3 retries=0 verification_score=98 floor=100% hashes=391aa4cf3b97b9d62aaa448de10642f7d87d3cae025ce59696d1c16ebf04ac1f/1c80001f10bc630667e4897c393cd9b39d7fb8c8add9fe13f358149d3db20470/8e93b73922addce0e863200cdd2cb2b4b888e6b8a958f8cd47e63e536cf3bed7/490d193bbbf4da531f9c34ceb0fdd292bb193facb0ed135b3693d8d90ceb4f16
- page 2: dpi=200 image=1700x2200 647180B model=glm-5.3-flash effort=low transcribe_ms=7574.2 verify_ms=3132.5 ocr_ms=468.8 retries=0 verification_score=99 floor=100% hashes=0aa803bb25678cca60bb1d57dfbd1d1a754085ea874dfd4ddfca526b01e49c8a/7931e2595fd2ae6f92735b4a03238e00f58dcbc1f6fa8dc94cc58376884f5cab/2bd93379515ff3ecc3624bf6622184a40e705ff3b873666b1c2d7583513c1c19/9e0d38ff3f517f3206c1c8005eafc721b1d9b1ffc72988254158eae90bf53d64
- page 3: dpi=200 image=1700x2200 607029B model=glm-5.3-flash effort=low transcribe_ms=7505.2 verify_ms=3418.2 ocr_ms=443.8 retries=0 verification_score=98 floor=100% hashes=8dbae235d59eb195204cd9fa576093f34fcb378f4c91d99f999de32b083a361b/2de92b5f21157644475575363dc56b812584427dbc97e9931cff10f9974c74fc/24050025bd06467b45e87a76619117755db4140798ca37711ec70503d7b09449/41f15897268bfbba93d6805160a337bc70cf5588f36c3b6f1a6235d60bad082b
- page 4: dpi=400 image=3400x4400 1274206B model=glm-5.3-flash effort=low transcribe_ms=25438.7 verify_ms=13539.7 ocr_ms=1547.7 retries=2 verification_score=96 floor=100% hashes=b3075efd981a37d4be934876ab90227c69ba563282111d00e02f5982967f8d9e/978990b9fa0768afa9e7228129378c7fc12b2fe06868c00ec319296d52beac5a/dd7e46f4a935b4a153d27efaaab0f0d22972e1af6c51359242192b05c7b3cc80/e3e1a91c273f938e496a135aea01e8a56d34389987de77c6d2fad321135e4652
- page 5: dpi=200 image=1700x2200 508625B model=glm-5.3-flash effort=low transcribe_ms=9132.6 verify_ms=3288.6 ocr_ms=441.8 retries=0 verification_score=98 floor=100% hashes=5db4ed8d189827e7873145d244c59826c0aa5a22fc8630d1c25a70dcfc256ce0/6a483bc45c09b3213eb9e48f8688d76118cf9d1cc1ac173febc6ec24e7619883/fb9ea4ae9e2a6aeec4cc1cb7518c4ade929a722bd9035670ee5454dc7e171a47/ae7eedd17b604a5b7e1036fa8f1b12bec6ffefa1153f3897b83915167389ab3a
- page 6: dpi=200 image=1700x2200 612054B model=glm-5.3-flash effort=low transcribe_ms=9758.3 verify_ms=4023.3 ocr_ms=506.1 retries=0 verification_score=96 floor=94% hashes=d6967d7dc4c02401b861c1e7e9c5f5dbe44e3c5d6db28747fd2c44fdcc30f061/36673e9e179bf33417bbaedd603143f2467fdfe263433f4442ba1697b214f431/938e22513bfce81ff59fb6e40e165523f7767da495e189ff45cc1095ce051c07/4c8844bfd8a4f2e491c788cd80c1482d706c9c0eebdf15ce59fac28152acaef8
- page 7: dpi=400 image=3400x4400 1292491B model=glm-5.3-flash effort=low transcribe_ms=31557.3 verify_ms=15566.3 ocr_ms=1206.9 retries=2 verification_score=97 floor=100% hashes=657b76fbcc18f9b4e359ce6d75edb0cfdfb6bc3393200a455d61cd93ee8c4876/bf6f4172cd1f3c6d31da161bde04618717a12d1b4653fea4871d1e01af8a92ed/66a7605511bc4edd6925fbf01e2641624f8ff52451482f95111de785388e833c/62ccbb7eae3cfdff683fc09d05c777c5c1f5da4b2782d472e185e4b5a7adfa6d
- page 8: dpi=300 image=2550x3300 900678B model=glm-5.3-flash effort=low transcribe_ms=25745.6 verify_ms=7352.4 ocr_ms=897.6 retries=1 verification_score=97 floor=98% hashes=f6f68320cdfa89b14bf4b455e53e0f1325ad0a54f4c7353fbda4ccfa71361731/86767a0d95fa9568bd1e8f91b74a45ded91ada7c3785da7960be99b62ec0677c/f414142b7c4c37da950eb78054106315f149fd32c67abfc2df44474494db3c76/05fbcb39ddca007dfe925dbd3da580e99913fb34b6b136a39c10bbd7a603e2f1

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:53: [Expected: 80, Actual: 675]
- MD013:57: [Expected: 80, Actual: 156]
- MD013:71: [Expected: 80, Actual: 376]
- MD013:73: [Expected: 80, Actual: 761]
- MD013:75: [Expected: 80, Actual: 412]
- MD013:81: [Expected: 80, Actual: 308]
- MD013:83: [Expected: 80, Actual: 372]
- MD013:85: [Expected: 80, Actual: 816]
- MD013:89: [Expected: 80, Actual: 269]
- MD013:100: [Expected: 80, Actual: 813]
- MD013:102: [Expected: 80, Actual: 625]
- MD013:106: [Expected: 80, Actual: 343]
- MD013:108: [Expected: 80, Actual: 317]
- MD013:114: [Expected: 80, Actual: 424]
- MD013:116: [Expected: 80, Actual: 241]
- MD013:118: [Expected: 80, Actual: 435]
- MD013:122: [Expected: 80, Actual: 269]
- MD013:124: [Expected: 80, Actual: 206]
- MD013:128: [Expected: 80, Actual: 509]
- MD013:132: [Expected: 80, Actual: 296]
- MD013:134: [Expected: 80, Actual: 223]
- MD013:136: [Expected: 80, Actual: 188]
- MD013:138: [Expected: 80, Actual: 306]
- MD013:142: [Expected: 80, Actual: 154]
- MD013:144: [Expected: 80, Actual: 265]
- MD013:146: [Expected: 80, Actual: 106]
- MD013:148: [Expected: 80, Actual: 445]
- MD013:150: [Expected: 80, Actual: 220]
- MD013:152: [Expected: 80, Actual: 336]
- MD013:156: [Expected: 80, Actual: 98]
- MD013:157: [Expected: 80, Actual: 98]
- MD013:158: [Expected: 80, Actual: 98]
- MD013:159: [Expected: 80, Actual: 98]
- MD013:163: [Expected: 80, Actual: 501]
- MD013:176: [Expected: 80, Actual: 376]
- MD013:178: [Expected: 80, Actual: 428]
- MD013:180: [Expected: 80, Actual: 457]
- MD013:182: [Expected: 80, Actual: 214]
- MD013:184: [Expected: 80, Actual: 421]
- MD013:186: [Expected: 80, Actual: 142]
- MD013:188: [Expected: 80, Actual: 351]
- MD013:192: [Expected: 80, Actual: 184]
- MD013:194: [Expected: 80, Actual: 118]
- MD013:196: [Expected: 80, Actual: 323]
- MD013:198: [Expected: 80, Actual: 150]
- MD013:200: [Expected: 80, Actual: 343]
- MD013:202: [Expected: 80, Actual: 136]
- MD013:204: [Expected: 80, Actual: 149]
- MD013:208: [Expected: 80, Actual: 169]
- MD013:210: [Expected: 80, Actual: 160]
- MD013:212: [Expected: 80, Actual: 474]
- MD013:214: [Expected: 80, Actual: 557]
- MD013:216: [Expected: 80, Actual: 296]
- MD013:220: [Expected: 80, Actual: 270]
- MD013:224: [Expected: 80, Actual: 253]
- MD013:226: [Expected: 80, Actual: 176]
- MD013:228: [Expected: 80, Actual: 273]
- MD013:230: [Expected: 80, Actual: 102]
- MD013:232: [Expected: 80, Actual: 333]
- MD013:236: [Expected: 80, Actual: 195]
- MD013:240: [Expected: 80, Actual: 138]
- MD013:246: [Expected: 80, Actual: 408]
- MD013:248: [Expected: 80, Actual: 155]
- MD036:250:
- MD033:252: [Element: details]
- MD013:255: [Expected: 80, Actual: 259]
- MD013:261: [Expected: 80, Actual: 98]
- MD013:262: [Expected: 80, Actual: 98]
- MD013:263: [Expected: 80, Actual: 98]
- MD013:264: [Expected: 80, Actual: 98]
- MD013:266: [Expected: 80, Actual: 374]
- MD013:270: [Expected: 80, Actual: 583]
- MD013:272: [Expected: 80, Actual: 167]
- MD013:276: [Expected: 80, Actual: 433]
- MD013:277: [Expected: 80, Actual: 433]
- MD013:278: [Expected: 80, Actual: 433]
- MD013:279: [Expected: 80, Actual: 433]
- MD013:280: [Expected: 80, Actual: 433]
- MD013:281: [Expected: 80, Actual: 433]
- MD013:282: [Expected: 80, Actual: 433]
- MD013:283: [Expected: 80, Actual: 433]
- MD013:284: [Expected: 80, Actual: 433]
- MD013:285: [Expected: 80, Actual: 433]
- MD013:286: [Expected: 80, Actual: 433]
- MD013:287: [Expected: 80, Actual: 433]
- MD013:288: [Expected: 80, Actual: 433]
- MD013:289: [Expected: 80, Actual: 433]
- MD013:291: [Expected: 80, Actual: 352]
- MD013:293: [Expected: 80, Actual: 355]
- MD013:297: [Expected: 80, Actual: 469]
- MD013:299: [Expected: 80, Actual: 303]
- MD013:306: [Expected: 80, Actual: 127]
- MD013:308: [Expected: 80, Actual: 124]
- MD013:310: [Expected: 80, Actual: 200]
- MD013:314: [Expected: 80, Actual: 102]
- MD013:344: [Expected: 80, Actual: 170]
- MD033:346: [Element: details]
- MD013:349: [Expected: 80, Actual: 156]
- MD036:351:
- MD033:353: [Element: details]
- MD013:356: [Expected: 80, Actual: 257]
- MD013:367: [Expected: 80, Actual: 324]
- MD013:369: [Expected: 80, Actual: 413]
- MD013:371: [Expected: 80, Actual: 508]
- MD013:379: [Expected: 80, Actual: 318]
- MD013:381: [Expected: 80, Actual: 288]
- MD036:383:
- MD013:385: [Expected: 80, Actual: 127]
- MD013:397: [Expected: 80, Actual: 334]
- MD013:399: [Expected: 80, Actual: 393]
- MD013:401: [Expected: 80, Actual: 481]
- MD013:412: [Expected: 80, Actual: 194]
- MD033:414: [Element: details]
- MD013:417: [Expected: 80, Actual: 156]
- MD036:419:
- MD033:421: [Element: details]
- MD013:424: [Expected: 80, Actual: 140]
- MD013:431: [Expected: 80, Actual: 424]
- MD013:433: [Expected: 80, Actual: 751]
- MD013:437: [Expected: 80, Actual: 138]
- MD013:441: [Expected: 80, Actual: 961]
- MD013:443: [Expected: 80, Actual: 156]
- MD036:445:
- MD033:447: [Element: details]
- MD013:450: [Expected: 80, Actual: 140]
- MD036:454:
- MD036:456:
- MD036:466:
- MD036:475:
- MD013:489: [Expected: 80, Actual: 201]
- MD013:491: [Expected: 80, Actual: 127]
- MD013:492: [Expected: 80, Actual: 98]
- MD013:493: [Expected: 80, Actual: 217]
- MD013:497: [Expected: 80, Actual: 145]
- MD013:499: [Expected: 80, Actual: 137]
- MD013:508: [Expected: 80, Actual: 402]
- MD013:510: [Expected: 80, Actual: 581]
- MD013:512: [Expected: 80, Actual: 257]
- MD013:514: [Expected: 80, Actual: 232]
- MD013:518: [Expected: 80, Actual: 420]
- MD013:520: [Expected: 80, Actual: 528]
- MD013:522: [Expected: 80, Actual: 376]
- MD013:524: [Expected: 80, Actual: 313]
- MD013:526: [Expected: 80, Actual: 916]
- MD013:528: [Expected: 80, Actual: 785]
- MD013:530: [Expected: 80, Actual: 243]
- MD013:532: [Expected: 80, Actual: 95]
- MD036:534:
- MD013:542: [Expected: 80, Actual: 260]
- MD013:546: [Expected: 80, Actual: 281]
- MD013:548: [Expected: 80, Actual: 409]
- MD013:550: [Expected: 80, Actual: 356]
- MD013:554: [Expected: 80, Actual: 115]
- MD013:555: [Expected: 80, Actual: 190]
- MD013:556: [Expected: 80, Actual: 110]
- MD013:557: [Expected: 80, Actual: 88]
- MD013:558: [Expected: 80, Actual: 105]
- MD013:559: [Expected: 80, Actual: 148]
- MD013:560: [Expected: 80, Actual: 92]
- MD013:561: [Expected: 80, Actual: 132]
- MD013:562: [Expected: 80, Actual: 162]
- MD013:563: [Expected: 80, Actual: 170]
- MD013:564: [Expected: 80, Actual: 140]
- MD013:565: [Expected: 80, Actual: 173]
