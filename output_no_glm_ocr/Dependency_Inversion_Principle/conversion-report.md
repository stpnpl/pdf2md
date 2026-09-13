# Conversion report — Dependency_Inversion_Principle.pdf

- job_id: 8ebcf362-d7b5-4c7f-910a-8bc2032bc421
- status: assembling
- pages: 12
- wall-clock: not started
- tokens: prompt=336466 completion=17648
- pipeline_version: 9c215872aa0b575aade8ae9fb73a81b65c9fb7d96e9934b244133c2636e44bc0
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 112

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 98 | 1 | 300 | 30051 | 1293 | False |
| 2 | verified | 98 | 0 | 200 | 12730 | 720 | False |
| 3 | verified | 95 | 0 | 200 | 13159 | 804 | False |
| 4 | needs_review | 82 | 2 | 400 | 53658 | 3100 | True |
| 5 | needs_review | 92 | 2 | 400 | 54099 | 2864 | True |
| 6 | verified | 95 | 0 | 200 | 13884 | 1105 | False |
| 7 | needs_review | 92 | 2 | 400 | 52572 | 2353 | True |
| 8 | verified | 99 | 0 | 200 | 13800 | 734 | False |
| 9 | verified | 95 | 1 | 300 | 33662 | 2003 | False |
| 10 | verified | 95 | 0 | 200 | 13370 | 766 | False |
| 11 | verified | 95 | 1 | 300 | 32943 | 1414 | False |
| 12 | verified | 95 | 0 | 200 | 12538 | 492 | False |

## needs_review pages

[4, 5, 7]

## Diagram → Mermaid conversion

- figures: 13
- converted to Mermaid: 6 (46%)
- data-table fallbacks: 0
- image fallbacks: 7

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 1 | 85 | classDiagram | image | 95 |
| 3 | 86 | flowchart | mermaid | 98 |
| 4 | 87 |  | image | 98 |
| 4 | 88 |  | image | 98 |
| 5 | 89 | classDiagram | mermaid | 95 |
| 6 | 90 |  | image | 95 |
| 7 | 91 | flowchart | mermaid | 98 |
| 7 | 92 | classDiagram | image | 95 |
| 9 | 93 | flowchart | mermaid | 100 |
| 9 | 94 | classDiagram | mermaid | 95 |
| 10 | 95 | classDiagram | image | 95 |
| 10 | 96 |  | image | 95 |
| 11 | 97 | classDiagram | mermaid | 95 |

## Omissions log

- page 1: - Sidebar text ("Sidebar: Unified Notation 0.8" and diagram labels: Used, Base Class, Derived 1, Derived 2, Had by Reference, Had By Value) captured within the figure placeholder.
- Page number "1" excluded from body.
- No corrections needed; ligature "unified" normalized from "uniﬁed".
- page 2: - Paragraph text ends mid-sentence; continues on next page ("When the extent of that cascade of change cannot be ...").
- Header and page number excluded from body per rules.
- Heading "The Cause of "Bad Design"." retains source trailing period.
- page 3: - Continuation from page 2: paragraph "predicted by the designers..." completes the sentence started on prior page.
- Footnote rendered as GFM footnote [^1].
- Figure 1 is a simple structure chart (Copy → Read Keyboard, Write Printer); rendered as placeholder token.
- No typo corrections made.
- page 4: verification cap reached
- page 5: verification cap reached
- page 6: Continuation from page 5 (paragraph begins mid-sentence "declared in stdio.h"). Listing 4 box rendered as figure placeholder plus fenced code block; content transcribed from image/OCR. Text rendered verbatim from the image, not the rolling context (rolling context contains content from earlier pages plus OCR of this page). No uncertain characters.
- page 7: verification cap reached
- page 8: - Text "affect" in "have any affect at all" reproduced as-is (source's usage; could be "effect" but left per DEC-009 as borderline).
- Paragraph continues onto next page ("...motion detec-").
- Monospace rendering of ".h" and ".cc" inferred from typeface; no uncertain characters.
- No figures on this page.
- page 9: - Page is a continuation of the sentence "…or even a motion detec-tor in a home security system" from the previous page.
- Figure 5 and Listing 5 appear as boxed regions in the right portion of the page (text wraps around them); reading order linearized with left-column text first, then the boxes.
- Curly quotes in source ("contains", "button.h", "lamp.h") normalized to straight quotes in code block.
- No [?] uncertainties.
- page 10: - Source typos preserved per DEC-009: "byttonClient.h" and "ButtonImplementaton(" (should be "buttonClient.h" / "ButtonImplementation(").
- `#include` lines lack angle brackets/quotes in source; preserved verbatim.
- Figure 1 bbox approximate; diagram includes Button/ButtonClient (Abstract) and ButtonImplementation/Lamp classes.
- page 11: - Typo left as-is per source: "Once could make a legitimate complaint" (source reads "Once", likely "One"; DEC-009 correction could change it, but kept verbatim as it is the source text — flagging as likely typo). If correcting: "One could make...".
- Footnote 3 continuation from previous page: body sentence "abstract button class[^3]" continues the previous page's text ending "...entirely captured within the".
- Text "The principle of dependency inversion... resilient to" continues on next page.
- Figure 7 caption is inside the figure frame; transcribed as caption below placeholder.
- page 12: - Page contains only the Conclusion continuation text; heading "Conclusion" and page number "12" are running header/footer, listed in FURNITURE.
- First paragraph begins mid-sentence, continuing from the previous page ("resilient to change.").
- Book title "Patterns and Advanced Principles of OOD" is italicized in source (line break hyphenation "Pat-terns" joined).
- The rolling context provided (Figures 5–7, Listings 5–6, footnotes) corresponds to earlier pages, not this page image, and is therefore not part of this page's transcription.
- No figures on this page; no uncertain characters.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=300 image=2550x3300 411138B model=glm-5.3-flash effort=low transcribe_ms=13593.9 verify_ms=6732.3 ocr_ms=966.2 retries=1 verification_score=98 floor=95% hashes=98fcf3409ab247b464c154b30cc2c33e70f128df42d0c81dd636b93f1128acc8/35e9fe8f548350927fc71d59c9e49b282842a9f4001bbc51419088a193427fa1/b9b9710fcb2ec8c653db535c02512716d9ba52ea812b2ab24a6b5c54608603c4/24b095840893c079c6015750e6617951975af7212b6ca335549b106706b8f5db
- page 2: dpi=200 image=1700x2200 297346B model=glm-5.3-flash effort=low transcribe_ms=6411.7 verify_ms=2988.1 ocr_ms=334.5 retries=0 verification_score=98 floor=96% hashes=d087cc7f753da5c73adf29bdceb9ffddbada973d4e5979ae45ae311eb4c8c7d6/1932ec7acde543f3fbfaf6ec36479663747a42e97c5e400f83f3a67874734f88/5412b090dc33bd0f56d5882c5fea7cd3f080054955cf17ca9a000a0975928fa1/d43806d88631d6e22838ec30f3f4ff4a46674ea65b743b5164f58ee0df77a194
- page 3: dpi=200 image=1700x2200 313437B model=glm-5.3-flash effort=low transcribe_ms=6322.4 verify_ms=3656.3 ocr_ms=325.1 retries=0 verification_score=95 floor=96% hashes=b914daeecf32c8dd3e743c8a9a95f2565d42f4fa642798aaaf5a0d8b8ce17e32/a2be612fe2d2dd0aef2a0b2152c9669cdbc9f5a5a409deee0f22944239cab6f8/1a2a80404c6096fa97f0950b024bec6598bca828e2fbf25494939577b7036cf8/b14d3315f240070e5683fe928867a7fcfd41a847e01f0c1b00b42366401954bd
- page 4: dpi=400 image=3400x4400 610262B model=glm-5.3-flash effort=low transcribe_ms=27596.4 verify_ms=42798.7 ocr_ms=2079.8 retries=2 verification_score=82 floor=91% hashes=e2fc467f6ed36b4f920784b5ed38130808b1038c074f59994507548c784ea5ca/83d69d8eadb5a812de9b519069dffef0cba60b23b6985820038a49928cd57796/326744171702920f0203a41a3049de8cfa6c8132516f499cbd78f6dc4834b429/ee872f410504be3d4cd82a3957d1939a33b2d87fac01e5efd06aa2aa6d43790f
- page 5: dpi=400 image=3400x4400 661438B model=glm-5.3-flash effort=low transcribe_ms=23983.0 verify_ms=13950.9 ocr_ms=2081.9 retries=2 verification_score=92 floor=97% hashes=da77801832ffe631937fbc358c4538915a918330964da1ec747e622ffcffe6a6/eb710b38e17ff9b4c7af390d2b92cd30f62de6123690e1e65f63739b6be43806/2dbe9e347d2c514d22eb447f5b067074cc17a682af81779b0100615dccb4b660/afed09530630675277c064307e7f6adae909ed9dfa33b109281b482e9e9c6300
- page 6: dpi=200 image=1700x2200 317592B model=glm-5.3-flash effort=low transcribe_ms=7218.4 verify_ms=4936.6 ocr_ms=349.8 retries=0 verification_score=95 floor=96% hashes=1e292551985cd2d36acd1115bfb481dbf1f4dbf9a85bdcf8b6f13de735e58dd8/2ff975c6809e5947cabf871e4918c5cd61cec49f67f67bc53c27ec01be3a899c/56d21d458c84cbcd6422fe78ebfa6388c63bb3152c1b83b531fcbe614fe83614/2069b7ef7c3ee2b550a8e97e88653c85df43d9f1bd35432bcc88c378fa965b43
- page 7: dpi=400 image=3400x4400 535697B model=glm-5.3-flash effort=low transcribe_ms=27264.1 verify_ms=12392.7 ocr_ms=2056.1 retries=2 verification_score=92 floor=93% hashes=562f8dbf32d0c9a12007f27bb2635b4748b2a2937f9965caf3a507a9aff06618/ceda4428057b25cd2eaaedd62fb90389370dcddc4d7391b3e0394a0f89cde635/eb478ecb09205bed6ca9022197261ac7abd33cf44400540eab7d6d23c4a570de/c2a46456057b26560bdfa5eb31cc63f4b153672d0e540e1fe4f9434b34a44941
- page 8: dpi=200 image=1700x2200 305156B model=glm-5.3-flash effort=low transcribe_ms=5702.0 verify_ms=2589.1 ocr_ms=355.2 retries=0 verification_score=99 floor=95% hashes=53475ec7027126143fbbaac403af1cd80eb644b9d0df9eb792171407026ba53a/bdb6c0bc982c025b7509da74b001150107ccf41aa89183d4874a8eb66f5db418/ff7c7cf73670f3498bc5ff7a4551e9f4cb12612e8e2d617c6dc8b79df0c4a160/4a7a7b795e827e500f2382724ffd75d9aeb4290bb8ca6ac97de57bd797eeb1c3
- page 9: dpi=300 image=2550x3300 514876B model=glm-5.3-flash effort=low transcribe_ms=16549.8 verify_ms=7386.7 ocr_ms=1014.3 retries=1 verification_score=95 floor=95% hashes=4316ce4be6fb9426917181946e03c2d7b6cfe42ea55edd00c596ea870d0ddceb/37185dd9f80964cd69fc2aea973f707606751184d17487a8e0762eced12bb709/421754364c4b29a2b714a648f0b5e10c79b45151a5351c42a393772fddd39f32/7fe653499aa7bd96209532452ad14b155ad9228fd8189c1e7f2125052013fbd5
- page 10: dpi=200 image=1700x2200 270409B model=glm-5.3-flash effort=low transcribe_ms=5230.5 verify_ms=2977.8 ocr_ms=339.5 retries=0 verification_score=95 floor=97% hashes=88de5f4dad761bcb0f85552f9be8f4cd4e17911c5cd70965e5270d10b9eed72c/68e84a1db2800010e1ccbd73697fb3abdf8a3768fba2995ab8561827415578d1/8dd0349b0f6fa761960f1b3c1fc0d39ac25f45244bd57691d8d41b84111e46ce/2bc1309fe625ae7f49745d416ba8b3dc77cf51925266e5c9755a5a7d5786add4
- page 11: dpi=300 image=2550x3300 355016B model=glm-5.3-flash effort=low transcribe_ms=15273.0 verify_ms=7884.9 ocr_ms=923.5 retries=1 verification_score=95 floor=96% hashes=de62d0689a2e055653b38acffc914f134725cb28b6d92cf1b6d22f1d544df99b/40eb6be8c733441428eb4ef3d9e287352282a9dee9ca529c405c3d95e1da6169/c25b62bb6994fcbd857eba3b0639cddfa79ed5bc6b02f83785b4eed5d8d6de11/9b9d8a43fbca36927445c7010821b9e9ea39244f52def2c29e7b83fe9cd0c611
- page 12: dpi=200 image=1700x2200 111032B model=glm-5.3-flash effort=low transcribe_ms=6080.9 verify_ms=2368.8 ocr_ms=254.6 retries=0 verification_score=95 floor=94% hashes=67540c80a3199391e2ee238c0ef6e517e1b10b254fbf19cd5079427e50a0e836/b22926c49967245b57227bffb917c34a299b8c52398167b61e9bd639a34596e1/58fcae54bab46cb4ffbe57976ff71ffb2f54749e421e48ae30b0897a3acc8bea/9037d998e23bfeed1bdd6610109ae7a5e2e007b3d4fa20a28a33fbf8342c0e66

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:20: [Expected: 80, Actual: 509]
- MD013:22: [Expected: 80, Actual: 156]
- MD036:24:
- MD033:26: [Element: details]
- MD013:29: [Expected: 80, Actual: 162]
- MD013:35: [Expected: 80, Actual: 971]
- MD013:37: [Expected: 80, Actual: 248]
- MD025:39:
- MD013:41: [Expected: 80, Actual: 289]
- MD013:43: [Expected: 80, Actual: 372]
- MD013:47: [Expected: 80, Actual: 507]
- MD013:49: [Expected: 80, Actual: 203]
- MD013:51: [Expected: 80, Actual: 99]
- MD013:53: [Expected: 80, Actual: 122]
- MD013:55: [Expected: 80, Actual: 314]
- MD026:57:
- MD013:59: [Expected: 80, Actual: 361]
- MD013:61: [Expected: 80, Actual: 270]
- MD013:63: [Expected: 80, Actual: 601]
- MD013:65: [Expected: 80, Actual: 674]
- MD026:67:
- MD013:69: [Expected: 80, Actual: 356]
- MD013:80: [Expected: 80, Actual: 135]
- MD033:82: [Element: details]
- MD013:91: [Expected: 80, Actual: 405]
- MD013:93: [Expected: 80, Actual: 106]
- MD013:95: [Expected: 80, Actual: 211]
- MD036:99:
- MD013:101: [Expected: 80, Actual: 284]
- MD013:103: [Expected: 80, Actual: 377]
- MD013:105: [Expected: 80, Actual: 276]
- MD036:109:
- MD013:111: [Expected: 80, Actual: 279]
- MD025:113:
- MD013:115: [Expected: 80, Actual: 445]
- MD013:117: [Expected: 80, Actual: 103]
- MD013:119: [Expected: 80, Actual: 547]
- MD013:121: [Expected: 80, Actual: 467]
- MD013:141: [Expected: 80, Actual: 149]
- MD033:143: [Element: details]
- MD013:146: [Expected: 80, Actual: 156]
- MD036:148:
- MD036:152:
- MD013:177: [Expected: 80, Actual: 733]
- MD013:179: [Expected: 80, Actual: 234]
- MD036:185:
- MD024:199:
- MD025:199:
- MD013:201: [Expected: 80, Actual: 109]
- MD013:203: [Expected: 80, Actual: 96]
- MD013:205: [Expected: 80, Actual: 695]
- MD013:207: [Expected: 80, Actual: 426]
- MD013:209: [Expected: 80, Actual: 280]
- MD013:211: [Expected: 80, Actual: 433]
- MD025:215:
- MD013:217: [Expected: 80, Actual: 792]
- MD013:225: [Expected: 80, Actual: 157]
- MD033:227: [Element: details]
- MD013:230: [Expected: 80, Actual: 142]
- MD036:232:
- MD013:238: [Expected: 80, Actual: 156]
- MD036:240:
- MD033:242: [Element: details]
- MD013:245: [Expected: 80, Actual: 191]
- MD013:249: [Expected: 80, Actual: 538]
- MD029:253: [Expected: 1; Actual: 2; Style: 1/2/3]
- MD013:255: [Expected: 80, Actual: 353]
- MD025:257:
- MD013:259: [Expected: 80, Actual: 313]
- MD013:261: [Expected: 80, Actual: 321]
- MD013:263: [Expected: 80, Actual: 741]
- MD013:265: [Expected: 80, Actual: 468]
- MD025:267:
- MD013:269: [Expected: 80, Actual: 155]
- MD013:271: [Expected: 80, Actual: 267]
- MD013:273: [Expected: 80, Actual: 447]
- MD013:275: [Expected: 80, Actual: 292]
- MD013:277: [Expected: 80, Actual: 399]
- MD013:279: [Expected: 80, Actual: 377]
- MD013:287: [Expected: 80, Actual: 105]
- MD033:289: [Element: details]
- MD013:292: [Expected: 80, Actual: 156]
- MD036:294:
- MD033:296: [Element: details]
- MD013:299: [Expected: 80, Actual: 156]
- MD013:320: [Expected: 80, Actual: 128]
- MD033:322: [Element: details]
- MD036:327:
- MD036:331:
- MD025:365:
- MD013:367: [Expected: 80, Actual: 439]
- MD013:369: [Expected: 80, Actual: 251]
- MD013:371: [Expected: 80, Actual: 204]
- MD036:375:
- MD036:381:
- MD036:383:
- MD013:437: [Expected: 80, Actual: 253]
- MD013:439: [Expected: 80, Actual: 266]
- MD025:441:
- MD013:443: [Expected: 80, Actual: 242]
- MD013:445: [Expected: 80, Actual: 260]
- MD013:455: [Expected: 80, Actual: 194]
- MD033:457: [Element: details]
- MD013:460: [Expected: 80, Actual: 156]
- MD036:462:
- MD033:464: [Element: details]
- MD013:467: [Expected: 80, Actual: 152]
- MD025:474:
- MD013:476: [Expected: 80, Actual: 275]
- MD013:478: [Expected: 80, Actual: 290]
- MD013:480: [Expected: 80, Actual: 118]
- MD013:482: [Expected: 80, Actual: 701]
