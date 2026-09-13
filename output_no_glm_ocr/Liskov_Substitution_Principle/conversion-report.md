# Conversion report — Liskov_Substitution_Principle.pdf

- job_id: e90dc451-89af-4de8-b7eb-adcf40a5ac14
- status: assembling
- pages: 11
- wall-clock: not started
- tokens: prompt=266101 completion=13643
- pipeline_version: 9c215872aa0b575aade8ae9fb73a81b65c9fb7d96e9934b244133c2636e44bc0
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 90

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 98 | 0 | 200 | 11755 | 661 | False |
| 2 | verified | 98 | 0 | 200 | 12605 | 737 | False |
| 3 | verified | 95 | 0 | 200 | 13123 | 979 | False |
| 4 | verified | 98 | 0 | 200 | 13562 | 757 | False |
| 5 | verified | 96 | 0 | 200 | 13380 | 716 | False |
| 6 | verified | 98 | 2 | 400 | 53948 | 2598 | False |
| 7 | verified | 95 | 0 | 200 | 13612 | 819 | False |
| 8 | verified | 96 | 0 | 200 | 13514 | 904 | False |
| 9 | verified | 98 | 2 | 400 | 54283 | 2568 | False |
| 10 | needs_review | 88 | 2 | 400 | 53373 | 2465 | True |
| 11 | verified | 95 | 0 | 200 | 12946 | 439 | False |

## needs_review pages

[10]

## Diagram → Mermaid conversion

- figures: 6
- converted to Mermaid: 4 (67%)
- data-table fallbacks: 0
- image fallbacks: 2

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 1 | 30 | classDiagram | image | 95 |
| 3 | 31 | classDiagram | mermaid | 95 |
| 7 | 32 | classDiagram | mermaid | 95 |
| 8 | 33 |  | image | 95 |
| 8 | 34 | classDiagram | mermaid | 95 |
| 10 | 35 | classDiagram | mermaid | 90 |

## Omissions log

- page 1: No spelling corrections needed beyond de-hyphenation of line-broken words (engineer-ing, soft-ware, uni-fied). Sidebar diagram rendered as figure placeholder; its internal labels are described in alt text. Page number "1" treated as furniture.
- page 2: - No figures on this page (the sidebar figure token in rolling context belongs to page 1).
- Typo correction: "make is safer" left as-is (matches source); flagged but not corrected per ambiguity.
- "nearly 8 years ago¹:" rendered with footnote marker ^1^; footnote text reproduced at bottom.
- Subscripts in Liskov quote (o₁, o₂) rendered as Unicode.
- page 3: - Corrected "problem are" to "problems are" (obvious typo).
- Source code contains a bug: `SetHeight(double h) {itsHeight=w;}` — reproduced verbatim per DEC-009 typo allowance (source typo, not corrected).
- Stray quote mark after "identical.\"." reproduced verbatim from source.
- Figure 1 (Rectangle/Square inheritance diagram) shown in right column beside the "Imagine that this application..." paragraphs; text wraps around it in source, linearized with placeholder at reading-order position.
- page 4: - Continues the code block for the `Rectangle` class that began on page 3; the listing is incomplete at page break (private section continues on next page).
- Corrected "s,SetHeight(2);" to "s.SetHeight(2);" (obvious typo); source "heigt" retained per DEC-009 allowance.
- Source shows "{itsWidth=w;}" style; normalized spacing inside braces.
- Running header "The Liskov Substitution Principle" and page number "4" excluded from body.
- page 5: - Code block continues from previous page (Rectangle class definition). Text continues onto next page ("Therefore, there exist functions..." incomplete sentence).
- Typo in source code retained verbatim: `assert(r.GetWidth() * r.GetHeight()) == 20);` has unbalanced parentheses (source error, not corrected as it is verbatim code).
- Running header and page number excluded from body.
- No figures on this page.
- page 6: - No figures on this page; the figure placeholder in rolling context belongs to the previous page.
- Continuation: page begins mid-sentence ("but cannot operate properly upon `Square` objects.") continuing the paragraph from page 5; next page continues from "postcondition will be true."
- "W³" rendered as W^3 superscript; footnote 2 converted to GFM footnote.
- "broken these function" left as in source (likely intended "functions" but not clearly an OCR error); "can not" left as in source.
- page 7: - Figure 2 (Container Hierarchy) is a UML diagram; text labels within it (Set, BoundedSet, ThirdParty BoundedSet, UnboundedSet, ThirdParty UnboundedSet) are represented by the figure placeholder.
- "stronger then" — source typo retained? Corrected "then" to "than" would alter quote; retained as printed per verbatim rule; flagged as likely typo.
- Footnote 3 (ibid, p256) continues the footnote series from page 6 ([^2] on previous page).
- "A Real Example." heading includes trailing period as in source.
- page 8: - Page continues from previous page: opening sentence begins "third parties..." completing the sentence "I was unhappy with the interfaces of the container classes that were available through".
- The PrintSet code listing (Figure region 1) is a boxed code snippet beside the paragraph text.
- Figure region 2 is the boxed "Figure 3. Persistent Set" UML diagram; code listing inside box not transcribed.
- The trailing code listing shown in rolling context (PrintSet) corresponds to Figure region 1 on this page.
- page 9: - No figures on this page; figure references in text (Figure 3) are mentions only.
- Typo corrections per DEC-009: "sup-posed"/"Persisten-tObjects"/"deriva-tive" hyphenated line breaks joined; "difﬁcult" ligature normalized to "difficult".
- Continuation: page begins mid-sentence from prior page ("derived from the abstract base class `PersistentObject`...").
- page 10: verification cap reached
- page 11: No figures on this page. Typo correction: "A.K.A" retained as in source. "oriented" in "object oriented design" spelled "orientied" in source? No—source reads "object oriented design" per OCR; kept standard.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 235465B model=glm-5.3-flash effort=low transcribe_ms=6624.9 verify_ms=3872.5 ocr_ms=88.4 retries=0 verification_score=98 floor=90% hashes=5998bc4b664a35fec94149313de33b19dbb85fd134d7d74915733ee6c2282de0/e993b9f4270e0b367b753633561d62701b3331eb706d7d4efe88dc8972d616be/983ecc130a49961f87c24112a48582453bfe68ff0d9b3864800b3974f4d15a61/57cbd0d6841b725c426ea4c4c2776843c9605bc709578ee93b61bd9d51d6e656
- page 2: dpi=200 image=1700x2200 283840B model=glm-5.3-flash effort=low transcribe_ms=7579.6 verify_ms=2844.9 ocr_ms=97.2 retries=0 verification_score=98 floor=96% hashes=7d3a927fedb2f0466ac4bb27a60b6966b57ebebb80d322cfef2d408c118f13aa/eeb0c00b3313ca8d080bca5b25f722dc75af6723dfee7b855a3a71998e378048/b0abf7be68d5d77b28d876f51661acc459874a1f0cd0ac279852433996c9ace2/987398327468558646797532ca63faf4aba1e99be01a64697339123c449d3900
- page 3: dpi=200 image=1700x2200 311095B model=glm-5.3-flash effort=low transcribe_ms=6416.1 verify_ms=4446.2 ocr_ms=100.2 retries=0 verification_score=95 floor=96% hashes=11471c5890ef936407054f477fab795aa927c84addb70d9bb3583ef42fbd629b/835b3e81ef192ddcab2cf3412b752f70f058aca8920299980fcbfa86b38aed37/de9a735cd32cecd1d125620997d4a94e8a13bebfe3965f11c05fff530c6d478e/e3f5051d0e6a3b5b570f9e2420234fb8ab7584d891048bb5abf90d4ea2c5d5bf
- page 4: dpi=200 image=1700x2200 283753B model=glm-5.3-flash effort=low transcribe_ms=6678.3 verify_ms=3050.5 ocr_ms=94.8 retries=0 verification_score=98 floor=98% hashes=3f81b3bd7f28876042dcbd7bbf4d0e3d87765bfd3a23c91beed2097585a800ad/0d82930bddc0832f6bc93f217ac2bb18d1a3bb2d4a447ce8c04e9a86136b2570/a01bbc3e33280b4bea9c6d57c1154179af2b6fe34f80e3869ebdbd96e1fc3322/9a8a0164e88c7eb4952065a6a6fbd1ec747ded5fa84e8a6b11c4bc5acf2a2c33
- page 5: dpi=200 image=1700x2200 256748B model=glm-5.3-flash effort=low transcribe_ms=5447.1 verify_ms=3923.6 ocr_ms=97.0 retries=0 verification_score=96 floor=96% hashes=3eede37b33c7352b889d5e1652978a23493c8e6764781e715de2c8b42aacf634/22ef3f64b54fb6732e60e9549695021a0e24bcce903b4ebf2f95a87e0225c7f6/6d65a887d19d243d967e23cfb03873b016f99ee616e5d7f1df79c4180acc93df/f147b673214e7d78a4ac65c1b1bfb60a73883aed89e61eb5207a9612b93296a5
- page 6: dpi=400 image=3400x4400 611589B model=glm-5.3-flash effort=low transcribe_ms=23895.6 verify_ms=11223.2 ocr_ms=571.7 retries=2 verification_score=98 floor=95% hashes=54c35f03b60a7928f744b9858364824b720e2a7ccb2d9d5699b725cd78aa6562/a0d626aade7e9d371d5886f932b086887aa5a0bc3b1371cdc9acedff8bd9d056/3e21d5f473a8d588df83de1d9895d5038a39796fdeb095c4309ccfc6b0c3e5d8/9e21ebc5a27abaec5550671dff6af935c17f8f51e2469dbf637782fcbf72b9e5
- page 7: dpi=200 image=1700x2200 286737B model=glm-5.3-flash effort=low transcribe_ms=10837.8 verify_ms=3658.4 ocr_ms=99.9 retries=0 verification_score=95 floor=93% hashes=3139caea835157409600e3d29231fae14ad99cbca86103956cdac4632b59dd05/9d03bc2d8aad32f74ff8d51a861a8c0e8216750d511ed0db3aff37ea3f88f6fc/7fff2c12ac45f1d28b74c8dee067f000cae13ed2b89a1f14f5f52db1d3889cf7/23bf14379399ce6ea2b45c61a798b8882557ac1fcd0100c29e2c82a02b3af1a2
- page 8: dpi=200 image=1700x2200 281161B model=glm-5.3-flash effort=low transcribe_ms=8097.8 verify_ms=4694.1 ocr_ms=96.7 retries=0 verification_score=96 floor=94% hashes=0b0379aa336daf205062c82dd3f302c1227c09caa2d814728e0ebea250779141/3bc6aa8c18033592eedfd4cd31df8774f779e56821ef597b35b6002e36abc5af/973d71254f96a6a5ca86f58d81e6cc650d3c8ab6a85967e7e7d0f9e73de4588d/70ea016bc09c25e2a453ca4493fc7f892805bb04f3cf15d0da2aa285ffed6947
- page 9: dpi=400 image=3400x4400 623663B model=glm-5.3-flash effort=low transcribe_ms=25617.6 verify_ms=11400.2 ocr_ms=618.6 retries=2 verification_score=98 floor=96% hashes=7c9f94ba5b733809a41052bb36cafdd827d4c4d24741f5e3d79f610ffdb884ee/908b84af3088e3e1dbf7b817e957823beb8545cd052b75b88b9a4143f2e4059d/44f8642c42ca68016690ccfc761c52428594a7e3732f61cabf14af9a0d9d55d3/36067efc7adf902e138421c0c9999961f3db80bc9aedd49311db1d0eafa1a7cc
- page 10: dpi=400 image=3400x4400 568361B model=glm-5.3-flash effort=low transcribe_ms=24506.4 verify_ms=14933.7 ocr_ms=595.8 retries=2 verification_score=88 floor=92% hashes=a2687ffe4f42e685a535ffb5b0d0c067a473d38cfbca4e2f11cdd01df33d1d2d/2843f16496c0718cd16566772a1baf234be91dd88c64a3ffd240a0dbd204e0b8/0e9c7cf2552944625f0219dbff9aca3df26b7be1ecc9d0b4a57f900cc7b672ca/93f1eb774abf5bc71836df71105e1eb5ad1bca2c4d58c0985aea9bd8b436e02b
- page 11: dpi=200 image=1700x2200 158060B model=glm-5.3-flash effort=low transcribe_ms=6561.0 verify_ms=3969.7 ocr_ms=86.2 retries=0 verification_score=95 floor=97% hashes=c1d6d2f7b602001014273b610443910f77a383d6a9638fa1607cd7ff674b71fd/acacb667d5af5778d630e63c5c68268cf504fa357039036aac980c814655925f/0482fb65cc221958346f77c5e8f248240e94d7ac1009c0adce9f61c55b0028f7/2de79a05e5619c1479012a4f8692906cac2a4de489e2a3e83a90683b28284364

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:21: [Expected: 80, Actual: 510]
- MD013:23: [Expected: 80, Actual: 156]
- MD036:25:
- MD033:27: [Element: details]
- MD013:30: [Expected: 80, Actual: 200]
- MD036:34:
- MD013:38: [Expected: 80, Actual: 349]
- MD013:40: [Expected: 80, Actual: 388]
- MD013:42: [Expected: 80, Actual: 305]
- MD024:44:
- MD025:44:
- MD013:46: [Expected: 80, Actual: 126]
- MD013:48: [Expected: 80, Actual: 133]
- MD013:50: [Expected: 80, Actual: 281]
- MD013:52: [Expected: 80, Actual: 419]
- MD013:56: [Expected: 80, Actual: 164]
- MD013:68: [Expected: 80, Actual: 294]
- MD013:70: [Expected: 80, Actual: 276]
- MD013:74: [Expected: 80, Actual: 89]
- MD025:76:
- MD026:76:
- MD013:78: [Expected: 80, Actual: 146]
- MD013:94: [Expected: 80, Actual: 271]
- MD013:104: [Expected: 80, Actual: 109]
- MD033:106: [Element: details]
- MD013:115: [Expected: 80, Actual: 264]
- MD013:117: [Expected: 80, Actual: 196]
- MD013:119: [Expected: 80, Actual: 391]
- MD013:121: [Expected: 80, Actual: 398]
- MD013:123: [Expected: 80, Actual: 346]
- MD013:125: [Expected: 80, Actual: 122]
- MD013:141: [Expected: 80, Actual: 275]
- MD013:158: [Expected: 80, Actual: 343]
- MD013:160: [Expected: 80, Actual: 579]
- MD013:162: [Expected: 80, Actual: 105]
- MD025:200:
- MD013:202: [Expected: 80, Actual: 461]
- MD013:204: [Expected: 80, Actual: 225]
- MD013:215: [Expected: 80, Actual: 367]
- MD013:217: [Expected: 80, Actual: 254]
- MD013:219: [Expected: 80, Actual: 231]
- MD013:223: [Expected: 80, Actual: 472]
- MD013:225: [Expected: 80, Actual: 228]
- MD013:229: [Expected: 80, Actual: 175]
- MD013:231: [Expected: 80, Actual: 311]
- MD013:233: [Expected: 80, Actual: 455]
- MD013:235: [Expected: 80, Actual: 168]
- MD013:239: [Expected: 80, Actual: 343]
- MD013:249: [Expected: 80, Actual: 98]
- MD013:251: [Expected: 80, Actual: 147]
- MD013:253: [Expected: 80, Actual: 607]
- MD013:255: [Expected: 80, Actual: 294]
- MD013:257: [Expected: 80, Actual: 464]
- MD025:259:
- MD026:259:
- MD013:261: [Expected: 80, Actual: 166]
- MD013:271: [Expected: 80, Actual: 202]
- MD033:273: [Element: details]
- MD036:278:
- MD025:282:
- MD024:288:
- MD025:288:
- MD026:288:
- MD013:290: [Expected: 80, Actual: 259]
- MD013:292: [Expected: 80, Actual: 108]
- MD013:305: [Expected: 80, Actual: 343]
- MD013:309: [Expected: 80, Actual: 613]
- MD025:311:
- MD013:327: [Expected: 80, Actual: 232]
- MD033:329: [Element: details]
- MD036:334:
- MD013:338: [Expected: 80, Actual: 346]
- MD013:340: [Expected: 80, Actual: 99]
- MD013:342: [Expected: 80, Actual: 294]
- MD013:356: [Expected: 80, Actual: 468]
- MD013:358: [Expected: 80, Actual: 658]
- MD025:360:
- MD026:360:
- MD013:362: [Expected: 80, Actual: 816]
- MD025:364:
- MD013:366: [Expected: 80, Actual: 320]
- MD013:368: [Expected: 80, Actual: 364]
- MD013:394: [Expected: 80, Actual: 235]
- MD033:396: [Element: details]
- MD036:401:
- MD013:405: [Expected: 80, Actual: 749]
- MD013:417: [Expected: 80, Actual: 238]
- MD025:419:
- MD013:421: [Expected: 80, Actual: 525]
- MD013:423: [Expected: 80, Actual: 686]
