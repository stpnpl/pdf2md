# Conversion report — Dependency_Inversion_Principle.pdf

- job_id: e72fb547-3bd4-4fa9-ba18-747f76658914
- status: assembling
- pages: 12
- wall-clock: not started
- tokens: prompt=397737 completion=20916
- pipeline_version: 77ca3a05b80cc24b9f872d6b9b7d3a5a3e45d53f35b87e62d9835656f30dcc5e
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 103

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 98 | 0 | 200 | 11866 | 656 | False |
| 2 | verified | 98 | 0 | 200 | 12729 | 735 | False |
| 3 | verified | 95 | 0 | 200 | 13158 | 808 | False |
| 4 | needs_review | 70 | 2 | 400 | 53761 | 2955 | True |
| 5 | verified | 95 | 2 | 400 | 54090 | 2858 | False |
| 6 | needs_review | 88 | 2 | 400 | 54313 | 2820 | True |
| 7 | needs_review | 92 | 2 | 400 | 52355 | 2388 | True |
| 8 | verified | 98 | 0 | 200 | 13725 | 764 | False |
| 9 | verified | 95 | 2 | 400 | 53388 | 2916 | False |
| 10 | verified | 96 | 2 | 400 | 52625 | 2892 | False |
| 11 | verified | 95 | 0 | 200 | 13244 | 736 | False |
| 12 | verified | 98 | 0 | 200 | 12483 | 388 | False |

## needs_review pages

[4, 6, 7]

## Diagram → Mermaid conversion

- figures: 11
- converted to Mermaid: 5 (45%)
- data-table fallbacks: 0
- image fallbacks: 6

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 1 | 47 | classDiagram | image | 88 |
| 3 | 48 | flowchart | mermaid | 95 |
| 4 | 49 |  | image | 98 |
| 4 | 50 | flowchart | image | 72 |
| 5 | 51 | classDiagram | mermaid | 96 |
| 6 | 52 |  | image | 98 |
| 7 | 53 | flowchart | mermaid | 98 |
| 7 | 54 | classDiagram | mermaid | 95 |
| 9 | 55 | flowchart | image | 80 |
| 10 | 56 |  | image | 98 |
| 11 | 57 | classDiagram | mermaid | 95 |

## Omissions log

- page 1: - The sidebar figure (diagram with labels: Sidebar: Unified Notation 0.8; Used; Base Class; Had by Reference; Had By Value; Derived 1; Derived 2) is represented by a placeholder; its caption is preserved in the alt text.
- Page number "1" excluded from body.
- No typo corrections made.
- page 2: No corrections needed; "The Cause of "Bad Design"." retains the source's trailing period after the closing quote (heading punctuation as in source). Italicized "that" preserved. Running header and page number excluded from body.
- page 3: - Continuation from previous page: body text resumes mid-sentence ("predicted by the designers...") under section "The Cause of 'Bad Design'."
- Figure 1 (structure chart with Copy, Read Keyboard, Write Printer boxes) rendered as placeholder; bbox approximates the diagram region on the right side of the page.
- Footnote 1 rendered as GFM footnote.
- No text corrections made; source text matches OCR reference verbatim.
- page 4: verification cap reached
- page 5: - Figure 2 diagram rendered as FIG placeholder; the code box beneath it transcribed verbatim as Listing 3 code block.
- The listing box is a bordered region on the page; emitted as code block rather than FIG per listing convention.
- Italic emphasis (*dependency inversion*, *inverted*) and inline code (`stdio.h`, `getchar`, `putchar`) preserved.
- Continuation: paragraph begins mid-sentence from page 4 ("input device to any output device...") and ends mid-sentence continuing to page 6 ("abstract facilities").
- page 6: verification cap reached
- page 7: verification cap reached
- page 8: - Continuing paragraph "The Button object senses..." ends mid-word ("detec-"), continues on next page.
- "have any affect at all" retained verbatim ("affect" vs "effect" appears in source).
- Inline code formatting (`.h`, `.cc`) applied to monospaced tokens in source.
- No figures on this page.
- page 9: - Page continues the "A Simple Example" section from prior page.
- Listing 5 code transcribed as text (per verification fix) rather than a FIG placeholder; the figure region for Listing 5's box is omitted from FIGURES because the code is transcribed verbatim above; only Figure 5 diagram is a placeholder.
- Curly quotes in source ("button.h", "lamp.h", "contains") normalized to straight quotes in code block.
- Caption "Listing 5: Naive Button/Lamp Code" placed after code block per source order (caption appears at bottom of box in source).
- page 10: - Figure 6 diagram placeholder: bbox estimates in absolute pixels; the two-column page text wraps around the figure, linearized as left column then figure.
- Source typos preserved verbatim: "byttonClient.h" (likely "buttonClient.h"), "ButtonImplementaton(" (likely "ButtonImplementation("), "public ButtonImplementation : public Button" split across lines. Per DEC-009 these were NOT corrected in the code block to preserve source.
- "itsClient->TurnOff();}" — closing brace of Detect() function appears at line break in source; preserved as in OCR.
- Listing 6 caption "Listing 6: Inverted Button Model" appears at bottom of the listing box in source; rendered as bold heading before the code block.
- Note in OCR "itsClient->TurnOn();" uses "itsClient" but Button member is "itsClient" — consistent.
- page 11: - "Once could make" is a source typo for "One could make" — left as-is per DEC-009 verbatim rule (logged here).
- Figure 7 diagram transcribed as placeholder; internal boxes: Button ◇— ButtonClient; Button Implementation ▷ Button; Lamp Adapter ▷ ButtonClient; Lamp ◇— Lamp Adapter.
- Footnote 3 continues from previous page context (superscript on "abstract button class³").
- Text ends mid-sentence ("resilient to") — continues on page 12.
- page 12: - Page begins mid-sentence ("change. And, since..."), continuing the Conclusion section from page 11.
- "deﬁne" ligature rendered as "define".
- No figures on this page; figure tokens from rolling context belong to earlier pages.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 256484B model=glm-5.3-flash effort=low transcribe_ms=6950.8 verify_ms=2583.2 ocr_ms=323.0 retries=0 verification_score=98 floor=95% hashes=98fcf3409ab247b464c154b30cc2c33e70f128df42d0c81dd636b93f1128acc8/7922486e22df248c45c82cd9404721609f2f430ee620362f39917b2265b20cb5/b9b9710fcb2ec8c653db535c02512716d9ba52ea812b2ab24a6b5c54608603c4/4514e28e4d39c60e2530161d00ba6eec1ccd85ebc2793891a99abc4deeb7c9fa
- page 2: dpi=200 image=1700x2200 297346B model=glm-5.3-flash effort=low transcribe_ms=11375.7 verify_ms=4123.6 ocr_ms=98.5 retries=0 verification_score=98 floor=96% hashes=d087cc7f753da5c73adf29bdceb9ffddbada973d4e5979ae45ae311eb4c8c7d6/1932ec7acde543f3fbfaf6ec36479663747a42e97c5e400f83f3a67874734f88/5412b090dc33bd0f56d5882c5fea7cd3f080054955cf17ca9a000a0975928fa1/2ee36b4031c4aba0b787ec56cc5f5dea056f68d6bec5a2a7567bb6ae7f5bfec5
- page 3: dpi=200 image=1700x2200 313437B model=glm-5.3-flash effort=low transcribe_ms=7103.8 verify_ms=3475.1 ocr_ms=365.2 retries=0 verification_score=95 floor=96% hashes=b914daeecf32c8dd3e743c8a9a95f2565d42f4fa642798aaaf5a0d8b8ce17e32/a2be612fe2d2dd0aef2a0b2152c9669cdbc9f5a5a409deee0f22944239cab6f8/1a2a80404c6096fa97f0950b024bec6598bca828e2fbf25494939577b7036cf8/dceaa98dbe69cc9fbe29cbc1f57c86bf826631ed9908b17d0f74c761cd730f8e
- page 4: dpi=400 image=3400x4400 610262B model=glm-5.3-flash effort=low transcribe_ms=31733.1 verify_ms=17194.8 ocr_ms=588.7 retries=2 verification_score=70 floor=91% hashes=e2fc467f6ed36b4f920784b5ed38130808b1038c074f59994507548c784ea5ca/83d69d8eadb5a812de9b519069dffef0cba60b23b6985820038a49928cd57796/326744171702920f0203a41a3049de8cfa6c8132516f499cbd78f6dc4834b429/6f2b1ee8b49739b47ba75c600a3ba434648214347cf2a140354a518687223d4a
- page 5: dpi=400 image=3400x4400 661438B model=glm-5.3-flash effort=low transcribe_ms=29206.0 verify_ms=14627.9 ocr_ms=880.8 retries=2 verification_score=95 floor=97% hashes=da77801832ffe631937fbc358c4538915a918330964da1ec747e622ffcffe6a6/eb710b38e17ff9b4c7af390d2b92cd30f62de6123690e1e65f63739b6be43806/2dbe9e347d2c514d22eb447f5b067074cc17a682af81779b0100615dccb4b660/4342cfd87838f4d0fbecdd4ecd066df2fbda458cea887b30eca409f687f228a9
- page 6: dpi=400 image=3400x4400 608398B model=glm-5.3-flash effort=low transcribe_ms=27285.0 verify_ms=15742.3 ocr_ms=1353.6 retries=2 verification_score=88 floor=92% hashes=1e292551985cd2d36acd1115bfb481dbf1f4dbf9a85bdcf8b6f13de735e58dd8/21c052758c4119bfadd3774b2f3606f893b8d7d7d38a08d90f4fde47317e00ee/56d21d458c84cbcd6422fe78ebfa6388c63bb3152c1b83b531fcbe614fe83614/91213f2aa37e84c94d9212718d578ce4466d49284d3681c1fc7614b13ba766c2
- page 7: dpi=400 image=3400x4400 535697B model=glm-5.3-flash effort=low transcribe_ms=26191.7 verify_ms=14733.7 ocr_ms=1290.6 retries=2 verification_score=92 floor=93% hashes=562f8dbf32d0c9a12007f27bb2635b4748b2a2937f9965caf3a507a9aff06618/ceda4428057b25cd2eaaedd62fb90389370dcddc4d7391b3e0394a0f89cde635/eb478ecb09205bed6ca9022197261ac7abd33cf44400540eab7d6d23c4a570de/cd7b7a522c1294ebdbe0a2e59515e3eb3e8ca0e6f7dec49de627d33ef119d80f
- page 8: dpi=200 image=1700x2200 305156B model=glm-5.3-flash effort=low transcribe_ms=8077.0 verify_ms=3161.5 ocr_ms=343.9 retries=0 verification_score=98 floor=95% hashes=53475ec7027126143fbbaac403af1cd80eb644b9d0df9eb792171407026ba53a/bdb6c0bc982c025b7509da74b001150107ccf41aa89183d4874a8eb66f5db418/ff7c7cf73670f3498bc5ff7a4551e9f4cb12612e8e2d617c6dc8b79df0c4a160/4a7a7b795e827e500f2382724ffd75d9aeb4290bb8ca6ac97de57bd797eeb1c3
- page 9: dpi=400 image=3400x4400 651524B model=glm-5.3-flash effort=low transcribe_ms=25948.3 verify_ms=18552.1 ocr_ms=2232.9 retries=2 verification_score=95 floor=95% hashes=4316ce4be6fb9426917181946e03c2d7b6cfe42ea55edd00c596ea870d0ddceb/7eacb500152e2eb6b4fb1288c7ffabfc1a1205d35a8e4649c64b135c70277c7b/421754364c4b29a2b714a648f0b5e10c79b45151a5351c42a393772fddd39f32/4410110d6f7579815ec9cda96115a3d781fe0f9036f3fa3026ea6a4268bf01d9
- page 10: dpi=400 image=3400x4400 527186B model=glm-5.3-flash effort=low transcribe_ms=31636.6 verify_ms=13856.7 ocr_ms=2006.9 retries=2 verification_score=96 floor=97% hashes=88de5f4dad761bcb0f85552f9be8f4cd4e17911c5cd70965e5270d10b9eed72c/a511d0db5ded4bd00b522503a122dd958399de999c33f36cd69b5d08ced13d56/8dd0349b0f6fa761960f1b3c1fc0d39ac25f45244bd57691d8d41b84111e46ce/3899d27b1ab332208dfe88a97fd7ce369e79b0efe209abd73c2b18f14ad40f42
- page 11: dpi=200 image=1700x2200 224205B model=glm-5.3-flash effort=low transcribe_ms=6261.0 verify_ms=2468.5 ocr_ms=357.6 retries=0 verification_score=95 floor=96% hashes=de62d0689a2e055653b38acffc914f134725cb28b6d92cf1b6d22f1d544df99b/7f24720dfdbec3dcb2656af156769a20c41863f95f61f68de0f33333bd9ff49d/c25b62bb6994fcbd857eba3b0639cddfa79ed5bc6b02f83785b4eed5d8d6de11/6f53d851fc6a5f167a103027df2da2fc6cfc19d4f0b843af6265773d629532c6
- page 12: dpi=200 image=1700x2200 111032B model=glm-5.3-flash effort=low transcribe_ms=8008.2 verify_ms=2571.6 ocr_ms=279.4 retries=0 verification_score=98 floor=95% hashes=67540c80a3199391e2ee238c0ef6e517e1b10b254fbf19cd5079427e50a0e836/b22926c49967245b57227bffb917c34a299b8c52398167b61e9bd639a34596e1/58fcae54bab46cb4ffbe57976ff71ffb2f54749e421e48ae30b0897a3acc8bea/f390f28bb8324c9a088e928ac2299136a764311f5664ac7f385c246cc576396e

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:21: [Expected: 80, Actual: 509]
- MD013:23: [Expected: 80, Actual: 156]
- MD036:25:
- MD033:27: [Element: details]
- MD013:30: [Expected: 80, Actual: 177]
- MD013:36: [Expected: 80, Actual: 971]
- MD013:38: [Expected: 80, Actual: 248]
- MD025:40:
- MD013:42: [Expected: 80, Actual: 289]
- MD013:44: [Expected: 80, Actual: 372]
- MD013:48: [Expected: 80, Actual: 506]
- MD013:50: [Expected: 80, Actual: 203]
- MD013:52: [Expected: 80, Actual: 99]
- MD013:54: [Expected: 80, Actual: 122]
- MD013:56: [Expected: 80, Actual: 314]
- MD026:58:
- MD013:60: [Expected: 80, Actual: 361]
- MD013:62: [Expected: 80, Actual: 270]
- MD013:64: [Expected: 80, Actual: 601]
- MD013:66: [Expected: 80, Actual: 674]
- MD026:68:
- MD013:70: [Expected: 80, Actual: 356]
- MD013:81: [Expected: 80, Actual: 138]
- MD033:83: [Element: details]
- MD013:86: [Expected: 80, Actual: 156]
- MD033:90: [Element: details]
- MD013:93: [Expected: 80, Actual: 129]
- MD013:98: [Expected: 80, Actual: 405]
- MD013:100: [Expected: 80, Actual: 106]
- MD013:102: [Expected: 80, Actual: 211]
- MD013:115: [Expected: 80, Actual: 284]
- MD013:117: [Expected: 80, Actual: 377]
- MD013:119: [Expected: 80, Actual: 556]
- MD025:136:
- MD013:138: [Expected: 80, Actual: 445]
- MD013:140: [Expected: 80, Actual: 103]
- MD013:142: [Expected: 80, Actual: 547]
- MD013:162: [Expected: 80, Actual: 179]
- MD033:164: [Element: details]
- MD036:169:
- MD013:174: [Expected: 80, Actual: 467]
- MD036:197:
- MD013:201: [Expected: 80, Actual: 733]
- MD013:203: [Expected: 80, Actual: 232]
- MD036:209:
- MD024:211:
- MD025:211:
- MD013:213: [Expected: 80, Actual: 107]
- MD013:217: [Expected: 80, Actual: 695]
- MD013:219: [Expected: 80, Actual: 426]
- MD013:221: [Expected: 80, Actual: 280]
- MD013:223: [Expected: 80, Actual: 433]
- MD025:227:
- MD013:235: [Expected: 80, Actual: 170]
- MD033:237: [Element: details]
- MD036:242:
- MD013:246: [Expected: 80, Actual: 797]
- MD013:262: [Expected: 80, Actual: 216]
- MD033:264: [Element: details]
- MD036:269:
- MD013:273: [Expected: 80, Actual: 538]
- MD013:277: [Expected: 80, Actual: 353]
- MD025:279:
- MD013:281: [Expected: 80, Actual: 313]
- MD013:283: [Expected: 80, Actual: 321]
- MD013:285: [Expected: 80, Actual: 741]
- MD013:287: [Expected: 80, Actual: 468]
- MD025:289:
- MD013:291: [Expected: 80, Actual: 155]
- MD013:293: [Expected: 80, Actual: 267]
- MD013:295: [Expected: 80, Actual: 447]
- MD013:297: [Expected: 80, Actual: 292]
- MD013:299: [Expected: 80, Actual: 399]
- MD013:301: [Expected: 80, Actual: 377]
- MD013:303: [Expected: 80, Actual: 156]
- MD036:305:
- MD033:307: [Element: details]
- MD013:310: [Expected: 80, Actual: 141]
- MD036:314:
- MD040:316:
- MD036:348:
- MD025:350:
- MD013:352: [Expected: 80, Actual: 439]
- MD013:354: [Expected: 80, Actual: 251]
- MD013:356: [Expected: 80, Actual: 267]
- MD036:358:
- MD036:360:
- MD040:362:
- MD013:414: [Expected: 80, Actual: 253]
- MD013:416: [Expected: 80, Actual: 266]
- MD013:420: [Expected: 80, Actual: 242]
- MD013:422: [Expected: 80, Actual: 260]
- MD013:432: [Expected: 80, Actual: 177]
- MD033:434: [Element: details]
- MD013:437: [Expected: 80, Actual: 140]
- MD036:439:
- MD025:443:
- MD013:445: [Expected: 80, Actual: 275]
- MD013:447: [Expected: 80, Actual: 290]
- MD024:449:
- MD025:449:
- MD013:451: [Expected: 80, Actual: 118]
- MD013:453: [Expected: 80, Actual: 701]
