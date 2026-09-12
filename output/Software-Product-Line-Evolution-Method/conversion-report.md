# Conversion report — Software-Product-Line-Evolution-Method.pdf

- job_id: 56e26a7a-6774-4dcb-aeaf-232e2d45f5e9
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=226199 completion=20204
- pipeline_version: e0804123b115bceb6fe27a3fb5bbe5cb5c3757a3a32381593bed7112ec02ec58
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 183

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 99 | 1 | 300 | 33116 | 2768 | False |
| 2 | verified | 98 | 0 | 200 | 15193 | 1404 | False |
| 3 | verified | 98 | 0 | 200 | 16333 | 1347 | False |
| 4 | verified | 97 | 2 | 400 | 65500 | 5036 | False |
| 5 | verified | 98 | 0 | 200 | 16612 | 1634 | False |
| 6 | verified | 97 | 0 | 200 | 17949 | 2031 | False |
| 7 | verified | 97 | 1 | 300 | 42426 | 4190 | False |
| 8 | verified | 98 | 0 | 200 | 19070 | 1794 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 3
- converted to Mermaid: 1 (33%)
- data-table fallbacks: 0
- image fallbacks: 2

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 127 | flowchart | image | 62 |
| 6 | 128 | flowchart | image | 88 |
| 6 | 129 | xychart-beta | mermaid | 97 |

## Omissions log

- page 1: Page number "1207" retained in the Markdown body at the end (per verification requirement); it is also listed as page-number furniture. No figures on this page. No typos corrected.
- page 2: Two-column layout linearized column by column. No figures on page. Corrected source typo "themselves"→"themselves" (source: "Core assets are not products thenseleves." — OCR reference shows "themselves"; image appears to show "themselves", no correction logged beyond this note). Heading "1.4 Research Approach" continues from prior page structure. Page number 1208 excluded from body.
- page 3: Two-column layout linearized column by column; tables transcribed as GFM pipe tables with diagonal header cell of Table 1 flattened into row labels. No figures on this page. Page number 1209 excluded from body.
- page 4: - Page 4 continues section 3.2's item (3) from previous page.
- Table 3 is rendered in the source as a shaded table overlaid with blue arrows indicating scenarios (1), (2), (3); arrow graphic captured as FIG placeholder; table content reproduced as GFM table.
- Typo correction: OCR reference gave "Type B's level of coverage is low" — source text reads "Type B's"; retained. OCR table cell "Mixture of Chain and Grain" corrected to "Mixture of Chaff and Grain" per Table 1 on earlier page.
- Footer page number "1210" excluded from body per furniture rules (per verification request, listed here and in FURNITURE).
- Scenario numbers (1)/(2)/(3) in the diagram body appear as annotations over table cells; represented only in figure alt/caption.
- page 5: Page 5 continues the document; Table 4 transcribed as GFM pipe table (scenarios flattened with line breaks; multi-line description cells joined). Table cell text reproduced verbatim from OCR reference, including "Harvesting-->Refactoring" arrows rendered as escaped ">\\". Page number "1211" appears at bottom center, excluded from body. Column layout linearized: left column (paragraphs + section 5 heading/intro) then right column (rest of section 5). Table 4 header row has green shading (decorative, omitted). "Recomme-ndation" header hyphenation joined. Table 4 is a real table, not treated as a figure; no figure regions on this page (Figure 1 is referenced but appears on a later page).
- page 6: - Page 6 of paper (printed page number 1212 in footer, excluded from body).
- Figure 2 chart values transcribed from chart data table; values are small print, potential uncertainty.
- No typos corrected on this page.
- page 7: - Table 5 rendered as three GFM pipe tables corresponding to sub-tables (1)/(a), (2)/(b), (3)/(c); callout labels (a)–(e) preserved inline (e.g., "(d) 12.25", "(e) 4.5"). Blue annotation circles/arrows in the original image omitted as decorative elements.
- Page number "1213" at bottom center excluded from body per rules.
- "the advantageous of" in Section 7 is a source typo left verbatim (log only, per DEC-009).
- Text ends mid-sentence ("...into"), continuing on next page (Section 8, item (b)).
- page 8: - Reference [6]: OCR shows "Helms, R." where standard form is "Helm, R."; kept as source "Helms" since uncertain whether to correct reference text — logged as possible typo.
- Reference [8]: "CUM/SEI-2003-TR-005" appears to be a typo for "CMU/SEI-2003-TR-005" but kept as in source image (both OCR and image show CUM). Logged as source typo, not corrected.
- Equation in original is split across lines with "Cost savings" on its own line; merged into single display equation.
- "(Here, $n_1$ ...)" — subscript rendered as in OCR; image shows "n₁" [?].
- C_del, C_ref, C_cab rendered as inline subscripts as in source body text.
- No figures on this page.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=300 image=2550x3300 785534B model=glm-5.3-flash effort=low transcribe_ms=16926.5 verify_ms=8060.2 ocr_ms=65112.9 retries=1 verification_score=99 floor=100% hashes=391aa4cf3b97b9d62aaa448de10642f7d87d3cae025ce59696d1c16ebf04ac1f/ffcaff68e6ed9ef5a0a74e721cafc4e10f8d23c8f453ec4b7bbc5d16c65b778f/b3dd44af6ed1694f02b986dcee49cc880a7a20eba2ebc5a2ab741441126a1b01/4fbec28271835a1c7a7fdb3f8b0d395a396c715aa042170f1524c4e7b87e6b32
- page 2: dpi=200 image=1700x2200 647180B model=glm-5.3-flash effort=low transcribe_ms=7261.6 verify_ms=2472.9 ocr_ms=37373.3 retries=0 verification_score=98 floor=100% hashes=0aa803bb25678cca60bb1d57dfbd1d1a754085ea874dfd4ddfca526b01e49c8a/7931e2595fd2ae6f92735b4a03238e00f58dcbc1f6fa8dc94cc58376884f5cab/a1acfb6d6cb2f7a80de49b617d8c4a3eddebf446893a8806ed1362ec6100deab/17b5d9b5fe7eab64d4f9fd23303a8101ff4d25caa47a559280447d6e77f93790
- page 3: dpi=200 image=1700x2200 607029B model=glm-5.3-flash effort=low transcribe_ms=7377.8 verify_ms=3664.1 ocr_ms=36778.2 retries=0 verification_score=98 floor=100% hashes=8dbae235d59eb195204cd9fa576093f34fcb378f4c91d99f999de32b083a361b/2de92b5f21157644475575363dc56b812584427dbc97e9931cff10f9974c74fc/10e18ea253f841116c66addf9e76e587e93d680f393d109e205088dfedfbcb2e/06ae4ea9ddd8f76703123f6785a0bfad61d338eb95ef91bcc3e6096c64275bea
- page 4: dpi=400 image=3400x4400 1274206B model=glm-5.3-flash effort=low transcribe_ms=23835.4 verify_ms=14207.5 ocr_ms=114758.1 retries=2 verification_score=97 floor=100% hashes=b3075efd981a37d4be934876ab90227c69ba563282111d00e02f5982967f8d9e/978990b9fa0768afa9e7228129378c7fc12b2fe06868c00ec319296d52beac5a/6f1126412d607eb470652a33ca804a8506cdac9b878ef23344f63011b089bf1a/b5651802d682697769705fa9ae264a96925d083325859cd8f5cc3a0e86d6ea31
- page 5: dpi=200 image=1700x2200 508625B model=glm-5.3-flash effort=low transcribe_ms=7317.1 verify_ms=2983.2 ocr_ms=18485.0 retries=0 verification_score=98 floor=100% hashes=5db4ed8d189827e7873145d244c59826c0aa5a22fc8630d1c25a70dcfc256ce0/6a483bc45c09b3213eb9e48f8688d76118cf9d1cc1ac173febc6ec24e7619883/f6c8d3c76fbaf321db92c63510173e9fc21f67cee031c8de4c4afe0acf1016ae/c7ec5408e3ee130f1a80ed69ec5db28716e338c28b4ad278e0078f0da0be82d2
- page 6: dpi=200 image=1700x2200 612054B model=glm-5.3-flash effort=low transcribe_ms=7907.2 verify_ms=4621.4 ocr_ms=38543.5 retries=0 verification_score=97 floor=100% hashes=d6967d7dc4c02401b861c1e7e9c5f5dbe44e3c5d6db28747fd2c44fdcc30f061/36673e9e179bf33417bbaedd603143f2467fdfe263433f4442ba1697b214f431/a8d6994e54c9bbc27f9e5997c860f8b2d253c2d157c49b8fdf47014d383401fe/18a65f4e8e9f83b71efefcb939c567310c51f01c3fdfeb72949a3d5159a16cc1
- page 7: dpi=300 image=2550x3300 892860B model=glm-5.3-flash effort=low transcribe_ms=18869.1 verify_ms=9057.6 ocr_ms=70710.8 retries=1 verification_score=97 floor=100% hashes=657b76fbcc18f9b4e359ce6d75edb0cfdfb6bc3393200a455d61cd93ee8c4876/910b253dddd63c7c01038feb7aaa4bac829f087ab18491a332a2a8f4dc8d9892/5b190cd44273a30034d8ada6519e17ff2d610d4ac93645911eaae0bfc1f296aa/de85944ecd67d238425fdc7596c13c419447987e9a23f3639423ae0d1ab538c2
- page 8: dpi=200 image=1700x2200 636013B model=glm-5.3-flash effort=low transcribe_ms=8941.1 verify_ms=3406.2 ocr_ms=48537.5 retries=0 verification_score=98 floor=100% hashes=f6f68320cdfa89b14bf4b455e53e0f1325ad0a54f4c7353fbda4ccfa71361731/04ef84ffec47c2afd7a2b1a6fe91719101e7bc65981b5075ab0e7bb75d92901a/fa0f24d0b88cbaf7241ec2f2d1b3ac3a753e2b252a917124668642a60f2a3959/e86c04729bcd7c04eb983e8fe954e61da298b39063115e8a8764bfcb30534c92

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:49: [Expected: 80, Actual: 675]
- MD013:53: [Expected: 80, Actual: 156]
- MD025:63:
- MD013:67: [Expected: 80, Actual: 376]
- MD013:69: [Expected: 80, Actual: 761]
- MD013:71: [Expected: 80, Actual: 412]
- MD013:77: [Expected: 80, Actual: 308]
- MD013:79: [Expected: 80, Actual: 372]
- MD013:81: [Expected: 80, Actual: 816]
- MD013:85: [Expected: 80, Actual: 269]
- MD013:98: [Expected: 80, Actual: 813]
- MD013:100: [Expected: 80, Actual: 625]
- MD013:104: [Expected: 80, Actual: 343]
- MD013:106: [Expected: 80, Actual: 317]
- MD013:114: [Expected: 80, Actual: 424]
- MD013:116: [Expected: 80, Actual: 241]
- MD013:118: [Expected: 80, Actual: 435]
- MD025:120:
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
- MD025:161:
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
- MD025:218:
- MD013:220: [Expected: 80, Actual: 270]
- MD013:224: [Expected: 80, Actual: 253]
- MD013:226: [Expected: 80, Actual: 172]
- MD013:228: [Expected: 80, Actual: 269]
- MD013:230: [Expected: 80, Actual: 98]
- MD013:232: [Expected: 80, Actual: 329]
- MD013:236: [Expected: 80, Actual: 195]
- MD013:240: [Expected: 80, Actual: 138]
- MD013:246: [Expected: 80, Actual: 408]
- MD013:250: [Expected: 80, Actual: 133]
- MD036:252:
- MD013:254: [Expected: 80, Actual: 107]
- MD033:254: [Element: br]
- MD013:255: [Expected: 80, Actual: 107]
- MD013:256: [Expected: 80, Actual: 107]
- MD013:257: [Expected: 80, Actual: 107]
- MD013:259: [Expected: 80, Actual: 374]
- MD013:263: [Expected: 80, Actual: 583]
- MD013:265: [Expected: 80, Actual: 167]
- MD013:269: [Expected: 80, Actual: 445]
- MD013:270: [Expected: 80, Actual: 445]
- MD013:271: [Expected: 80, Actual: 445]
- MD033:271: [Element: br]
- MD033:271: [Element: br]
- MD033:271: [Element: br]
- MD033:271: [Element: br]
- MD033:271: [Element: br]
- MD033:271: [Element: br]
- MD013:272: [Expected: 80, Actual: 445]
- MD033:272: [Element: br]
- MD013:273: [Expected: 80, Actual: 445]
- MD013:274: [Expected: 80, Actual: 445]
- MD013:275: [Expected: 80, Actual: 445]
- MD033:275: [Element: br]
- MD033:275: [Element: br]
- MD013:276: [Expected: 80, Actual: 445]
- MD033:276: [Element: br]
- MD013:277: [Expected: 80, Actual: 445]
- MD013:278: [Expected: 80, Actual: 445]
- MD013:279: [Expected: 80, Actual: 445]
- MD033:279: [Element: br]
- MD033:279: [Element: br]
- MD013:280: [Expected: 80, Actual: 445]
- MD013:281: [Expected: 80, Actual: 445]
- MD013:282: [Expected: 80, Actual: 445]
- MD033:282: [Element: br]
- MD033:282: [Element: br]
- MD033:282: [Element: br]
- MD033:282: [Element: br]
- MD033:282: [Element: br]
- MD033:282: [Element: br]
- MD013:284: [Expected: 80, Actual: 352]
- MD013:286: [Expected: 80, Actual: 355]
- MD025:288:
- MD013:290: [Expected: 80, Actual: 469]
- MD013:292: [Expected: 80, Actual: 303]
- MD013:299: [Expected: 80, Actual: 125]
- MD013:301: [Expected: 80, Actual: 122]
- MD013:303: [Expected: 80, Actual: 200]
- MD013:307: [Expected: 80, Actual: 102]
- MD013:309: [Expected: 80, Actual: 156]
- MD036:311:
- MD033:313: [Element: details]
- MD013:316: [Expected: 80, Actual: 228]
- MD025:322:
- MD013:326: [Expected: 80, Actual: 324]
- MD013:328: [Expected: 80, Actual: 413]
- MD013:330: [Expected: 80, Actual: 508]
- MD013:338: [Expected: 80, Actual: 318]
- MD013:340: [Expected: 80, Actual: 288]
- MD036:342:
- MD013:344: [Expected: 80, Actual: 127]
- MD036:348:
- MD013:355: [Expected: 80, Actual: 334]
- MD013:357: [Expected: 80, Actual: 393]
- MD013:359: [Expected: 80, Actual: 481]
- MD013:370: [Expected: 80, Actual: 205]
- MD033:372: [Element: details]
- MD013:375: [Expected: 80, Actual: 156]
- MD036:377:
- MD033:379: [Element: details]
- MD013:382: [Expected: 80, Actual: 222]
- MD013:389: [Expected: 80, Actual: 424]
- MD013:391: [Expected: 80, Actual: 751]
- MD013:395: [Expected: 80, Actual: 138]
- MD013:399: [Expected: 80, Actual: 961]
- MD013:436: [Expected: 80, Actual: 201]
- MD013:438: [Expected: 80, Actual: 127]
- MD013:439: [Expected: 80, Actual: 98]
- MD013:440: [Expected: 80, Actual: 217]
- MD025:442:
- MD013:444: [Expected: 80, Actual: 145]
- MD013:446: [Expected: 80, Actual: 137]
- MD013:455: [Expected: 80, Actual: 402]
- MD013:457: [Expected: 80, Actual: 581]
- MD013:459: [Expected: 80, Actual: 257]
- MD013:461: [Expected: 80, Actual: 232]
- MD025:463:
- MD013:465: [Expected: 80, Actual: 420]
- MD013:467: [Expected: 80, Actual: 528]
- MD013:469: [Expected: 80, Actual: 378]
- MD013:471: [Expected: 80, Actual: 313]
- MD013:473: [Expected: 80, Actual: 916]
- MD013:475: [Expected: 80, Actual: 785]
- MD013:477: [Expected: 80, Actual: 243]
- MD013:479: [Expected: 80, Actual: 128]
- MD036:481:
- MD013:484: [Expected: 80, Actual: 94]
- MD013:489: [Expected: 80, Actual: 269]
- MD025:491:
- MD013:493: [Expected: 80, Actual: 281]
- MD013:495: [Expected: 80, Actual: 409]
- MD013:497: [Expected: 80, Actual: 356]
- MD025:499:
- MD013:501: [Expected: 80, Actual: 115]
- MD013:503: [Expected: 80, Actual: 190]
- MD013:505: [Expected: 80, Actual: 110]
- MD013:507: [Expected: 80, Actual: 86]
- MD013:509: [Expected: 80, Actual: 105]
- MD013:511: [Expected: 80, Actual: 148]
- MD013:513: [Expected: 80, Actual: 92]
- MD013:515: [Expected: 80, Actual: 132]
- MD013:517: [Expected: 80, Actual: 162]
- MD013:519: [Expected: 80, Actual: 170]
- MD013:521: [Expected: 80, Actual: 140]
- MD013:523: [Expected: 80, Actual: 173]
