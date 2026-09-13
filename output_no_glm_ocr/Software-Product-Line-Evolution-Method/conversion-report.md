# Conversion report — Software-Product-Line-Evolution-Method.pdf

- job_id: 8faa08f8-1a0a-4016-be20-13f6ea0c0b94
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=138381 completion=12811
- pipeline_version: 9c215872aa0b575aade8ae9fb73a81b65c9fb7d96e9934b244133c2636e44bc0
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 157

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 99 | 0 | 200 | 13849 | 1235 | False |
| 2 | verified | 99 | 0 | 200 | 15439 | 1401 | False |
| 3 | verified | 95 | 0 | 200 | 16694 | 1402 | False |
| 4 | verified | 95 | 0 | 200 | 17954 | 1753 | False |
| 5 | verified | 95 | 0 | 200 | 17994 | 1535 | False |
| 6 | verified | 95 | 0 | 200 | 18217 | 1762 | False |
| 7 | verified | 95 | 0 | 200 | 19066 | 1962 | False |
| 8 | verified | 97 | 0 | 200 | 19168 | 1761 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 3
- converted to Mermaid: 1 (33%)
- data-table fallbacks: 0
- image fallbacks: 2

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 114 | flowchart | image | 78 |
| 6 | 115 | flowchart | image | 78 |
| 6 | 116 | xychart-beta | mermaid | 95 |

## Omissions log

- page 1: - Two-column layout linearized: left column (Abstract through 1.1 partial) then right column (1.1 continuation through 1.3).
- Copyright/permission block placed at end as a block quote; it appears bottom-left in the original layout.
- No figures on this page.
- No typos detected requiring correction.
- page 2: Corrected source typo "themselves" → "themselves" (2.2 Level of Consistency paragraph). Full-width bracket character "［3］" in source normalized to "[3]". List items (a)–(c) and dash list reproduced per source. Page ends mid-sentence ("An organization develops core") — continues on page 3. No figures on this page.
- page 3: Tables 1 and 2 rendered as GFM tables from the source table images (the OCR reference contained duplicated cell text; single instance used). Typo allowance: "consistent each other" and "An existing feature is a part of a product" left as in source. No figures/diagrams beyond the tables. Page number 1209 excluded from body.
- page 4: - Page number "1210" is a running page number, excluded from body.
- Figure region 1 contains the arrow overlay of Table 3; table text reproduced as GFM table beneath the placeholder.
- OCR source contained full-width character "［5］．" corrected to "[5]."
- Column-header text of Table 3 ("Level of Consistency", "Level of Coverage", "Consistent Core Assets", "Inconsistent Core Assets", row labels "All Kinds of Software Artifacts" / "Some Kinds of Software Artifacts") reproduced in the GFM table.
- page 5: - Table 4 (spanning the full page width, caption "Table 4. Kaizen patterns") transcribed as a GFM pipe table; scenario entries within a cell were separated by semicolons since they were laid out in two sub-columns in the source.
- Two-column body linearized: left column first, then right column.
- Page number "1211" is a footer (proceedings page number), excluded from body.
- No figures on this page; Figure 1 is referenced in text but appears on a later page.
- Minor spacing irregularities in source ("concerned  about", "asset base.") normalized.
- page 6: - The running text of Section 5's PDCA description ended on the previous page (page 1211); this page begins mid-Section 5 with Figure 1, then Section 6. Reading order per two-column layout: left column (Figure 1, Section 6 through "(2) Analyzing scenarios" equation introduction), right column (equation, Figure 2 discussion, Table 5 introduction).
- Figure 1 and Figure 2 bboxes are approximate; the equation block in the right column immediately after "(2) Analyzing scenarios" was transcribed as LaTeX rather than a figure since it is typeset text.
- Page number "1212" appears at bottom center; excluded from body.
- The full-width parenthesis characters "（2）" in the OCR reference were normalized to "(2)"; full-width parentheses elsewhere normalized.
- page 7: - Table 5 is composed of three sub-tables with hand-drawn circled annotations (a)–(e); annotation letters reproduced as text labels after each sub-table.
- "the advantageous of" retained as in source (grammatical oddity in original).
- Full-width comma characters in source ("，") normalized to standard commas.
- Section 6.3 heading numbered "6.3" though it appears under Section 6 after Section 5; source numbering preserved.
- Text ends mid-sentence ("...obtained through product development, into"); continues on next page (page 8).
- page 8: - Continuation of Section 8 (Related Work) from previous page ("into" -> "into previous core assets.").
- ROI equation region transcribed as LaTeX; original OCR shows "(Here, n1 ...)" — rendered as $n_1$; [?] on subscript digit.
- Reference [8]: "CUM/SEI-2003-TR-005" reproduced as in source (likely typo for CMU/SEI, not corrected in body; corrected in OCR ground-truth reference [8] to CMU but image shows CUM — kept CUM per source, logged as possible typo).
- Page number "1214" excluded from body.
- No figures on this page.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 562756B model=glm-5.3-flash effort=low transcribe_ms=7373.0 verify_ms=4025.3 ocr_ms=469.9 retries=0 verification_score=99 floor=100% hashes=391aa4cf3b97b9d62aaa448de10642f7d87d3cae025ce59696d1c16ebf04ac1f/1c80001f10bc630667e4897c393cd9b39d7fb8c8add9fe13f358149d3db20470/8e93b73922addce0e863200cdd2cb2b4b888e6b8a958f8cd47e63e536cf3bed7/b6de2244d0d389c25dccc04a6e0420bff08d90921de283806e64fde930367677
- page 2: dpi=200 image=1700x2200 647180B model=glm-5.3-flash effort=low transcribe_ms=12373.1 verify_ms=3305.9 ocr_ms=520.0 retries=0 verification_score=99 floor=100% hashes=0aa803bb25678cca60bb1d57dfbd1d1a754085ea874dfd4ddfca526b01e49c8a/7931e2595fd2ae6f92735b4a03238e00f58dcbc1f6fa8dc94cc58376884f5cab/2bd93379515ff3ecc3624bf6622184a40e705ff3b873666b1c2d7583513c1c19/17b5d9b5fe7eab64d4f9fd23303a8101ff4d25caa47a559280447d6e77f93790
- page 3: dpi=200 image=1700x2200 607029B model=glm-5.3-flash effort=low transcribe_ms=11830.6 verify_ms=4069.6 ocr_ms=427.1 retries=0 verification_score=95 floor=100% hashes=8dbae235d59eb195204cd9fa576093f34fcb378f4c91d99f999de32b083a361b/2de92b5f21157644475575363dc56b812584427dbc97e9931cff10f9974c74fc/24050025bd06467b45e87a76619117755db4140798ca37711ec70503d7b09449/41f15897268bfbba93d6805160a337bc70cf5588f36c3b6f1a6235d60bad082b
- page 4: dpi=200 image=1700x2200 623396B model=glm-5.3-flash effort=low transcribe_ms=15457.9 verify_ms=4307.6 ocr_ms=483.1 retries=0 verification_score=95 floor=100% hashes=b3075efd981a37d4be934876ab90227c69ba563282111d00e02f5982967f8d9e/260a030976afafda190615593c57904d96a92ac936bb46241decd7938cf8b1cb/dd7e46f4a935b4a153d27efaaab0f0d22972e1af6c51359242192b05c7b3cc80/f4cd91527a887563f32c2efd696a282d76b798af90c6338e65d9577e01efd762
- page 5: dpi=200 image=1700x2200 508625B model=glm-5.3-flash effort=low transcribe_ms=11425.9 verify_ms=3223.8 ocr_ms=408.2 retries=0 verification_score=95 floor=100% hashes=5db4ed8d189827e7873145d244c59826c0aa5a22fc8630d1c25a70dcfc256ce0/6a483bc45c09b3213eb9e48f8688d76118cf9d1cc1ac173febc6ec24e7619883/fb9ea4ae9e2a6aeec4cc1cb7518c4ade929a722bd9035670ee5454dc7e171a47/250bea8208a3c9d1ce2be6918d0fd051de69b0f9686a565992b939e98dcddd63
- page 6: dpi=200 image=1700x2200 612054B model=glm-5.3-flash effort=low transcribe_ms=11439.8 verify_ms=7207.0 ocr_ms=502.7 retries=0 verification_score=95 floor=94% hashes=d6967d7dc4c02401b861c1e7e9c5f5dbe44e3c5d6db28747fd2c44fdcc30f061/36673e9e179bf33417bbaedd603143f2467fdfe263433f4442ba1697b214f431/938e22513bfce81ff59fb6e40e165523f7767da495e189ff45cc1095ce051c07/a3c90349e2fdea3219802134cdf3e383020271a3fc94c3bf4d23336235fdf29c
- page 7: dpi=200 image=1700x2200 634905B model=glm-5.3-flash effort=low transcribe_ms=16532.1 verify_ms=3194.4 ocr_ms=451.4 retries=0 verification_score=95 floor=100% hashes=657b76fbcc18f9b4e359ce6d75edb0cfdfb6bc3393200a455d61cd93ee8c4876/1a448d204b230e02a8df63863f0af61fa27784c098a9be8fb8e0daf6cfe2b2ea/66a7605511bc4edd6925fbf01e2641624f8ff52451482f95111de785388e833c/8b2fa1c59e22b5bea2d7c8294c52a3dcc6e5387406a5110a2fa1e5439363de15
- page 8: dpi=200 image=1700x2200 636013B model=glm-5.3-flash effort=low transcribe_ms=16721.1 verify_ms=3629.1 ocr_ms=514.3 retries=0 verification_score=97 floor=98% hashes=f6f68320cdfa89b14bf4b455e53e0f1325ad0a54f4c7353fbda4ccfa71361731/04ef84ffec47c2afd7a2b1a6fe91719101e7bc65981b5075ab0e7bb75d92901a/f414142b7c4c37da950eb78054106315f149fd32c67abfc2df44474494db3c76/21b29dc85f0030eb4992b78d948699b253c2b1dc0339c5c6bbec7107c07edc96

## Figures placed without placeholder (appended at page end)

none

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
- MD013:225: [Expected: 80, Actual: 172]
- MD013:227: [Expected: 80, Actual: 269]
- MD013:229: [Expected: 80, Actual: 98]
- MD013:231: [Expected: 80, Actual: 329]
- MD013:235: [Expected: 80, Actual: 195]
- MD013:239: [Expected: 80, Actual: 138]
- MD013:245: [Expected: 80, Actual: 408]
- MD013:247: [Expected: 80, Actual: 125]
- MD036:249:
- MD013:253: [Expected: 80, Actual: 98]
- MD013:254: [Expected: 80, Actual: 98]
- MD013:255: [Expected: 80, Actual: 98]
- MD013:256: [Expected: 80, Actual: 98]
- MD013:258: [Expected: 80, Actual: 374]
- MD013:262: [Expected: 80, Actual: 583]
- MD013:264: [Expected: 80, Actual: 167]
- MD013:268: [Expected: 80, Actual: 433]
- MD013:269: [Expected: 80, Actual: 433]
- MD013:270: [Expected: 80, Actual: 433]
- MD013:271: [Expected: 80, Actual: 433]
- MD013:272: [Expected: 80, Actual: 433]
- MD013:273: [Expected: 80, Actual: 433]
- MD013:274: [Expected: 80, Actual: 433]
- MD013:275: [Expected: 80, Actual: 433]
- MD013:276: [Expected: 80, Actual: 433]
- MD013:277: [Expected: 80, Actual: 433]
- MD013:278: [Expected: 80, Actual: 433]
- MD013:279: [Expected: 80, Actual: 433]
- MD013:280: [Expected: 80, Actual: 433]
- MD013:281: [Expected: 80, Actual: 433]
- MD013:283: [Expected: 80, Actual: 352]
- MD013:285: [Expected: 80, Actual: 355]
- MD025:287:
- MD013:289: [Expected: 80, Actual: 469]
- MD013:291: [Expected: 80, Actual: 303]
- MD013:298: [Expected: 80, Actual: 125]
- MD013:300: [Expected: 80, Actual: 122]
- MD013:302: [Expected: 80, Actual: 200]
- MD013:306: [Expected: 80, Actual: 102]
- MD013:312: [Expected: 80, Actual: 324]
- MD013:314: [Expected: 80, Actual: 413]
- MD013:316: [Expected: 80, Actual: 508]
- MD013:324: [Expected: 80, Actual: 318]
- MD013:326: [Expected: 80, Actual: 288]
- MD036:328:
- MD013:330: [Expected: 80, Actual: 127]
- MD013:334: [Expected: 80, Actual: 85]
- MD013:343: [Expected: 80, Actual: 156]
- MD013:358: [Expected: 80, Actual: 161]
- MD033:360: [Element: details]
- MD013:363: [Expected: 80, Actual: 156]
- MD036:365:
- MD033:367: [Element: details]
- MD013:370: [Expected: 80, Actual: 143]
- MD013:377: [Expected: 80, Actual: 334]
- MD013:379: [Expected: 80, Actual: 393]
- MD013:381: [Expected: 80, Actual: 481]
- MD013:383: [Expected: 80, Actual: 424]
- MD013:385: [Expected: 80, Actual: 751]
- MD013:389: [Expected: 80, Actual: 138]
- MD013:393: [Expected: 80, Actual: 961]
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
- MD013:481: [Expected: 80, Actual: 95]
- MD013:482: [Expected: 80, Actual: 89]
- MD013:492: [Expected: 80, Actual: 269]
- MD025:494:
- MD013:496: [Expected: 80, Actual: 281]
- MD013:498: [Expected: 80, Actual: 409]
- MD013:500: [Expected: 80, Actual: 356]
- MD025:502:
- MD013:504: [Expected: 80, Actual: 115]
- MD013:506: [Expected: 80, Actual: 190]
- MD013:508: [Expected: 80, Actual: 110]
- MD013:510: [Expected: 80, Actual: 86]
- MD013:512: [Expected: 80, Actual: 105]
- MD013:514: [Expected: 80, Actual: 148]
- MD013:516: [Expected: 80, Actual: 92]
- MD013:518: [Expected: 80, Actual: 132]
- MD013:520: [Expected: 80, Actual: 162]
- MD013:522: [Expected: 80, Actual: 170]
- MD013:524: [Expected: 80, Actual: 140]
- MD013:526: [Expected: 80, Actual: 173]
