# Conversion report — Liskov_Substitution_Principle.pdf

- job_id: 17078dc7-4dde-4c8f-bf6d-d421ad75fb68
- status: assembling
- pages: 11
- wall-clock: not started
- tokens: prompt=365038 completion=17900
- pipeline_version: 77ca3a05b80cc24b9f872d6b9b7d3a5a3e45d53f35b87e62d9835656f30dcc5e
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 85

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 95 | 0 | 200 | 11744 | 640 | False |
| 2 | verified | 99 | 0 | 200 | 12605 | 720 | False |
| 3 | verified | 95 | 0 | 200 | 13124 | 834 | False |
| 4 | verified | 95 | 2 | 400 | 53390 | 2480 | False |
| 5 | verified | 95 | 2 | 400 | 52857 | 2195 | False |
| 6 | verified | 97 | 0 | 200 | 13745 | 828 | False |
| 7 | needs_review | 90 | 2 | 400 | 53553 | 2596 | True |
| 8 | verified | 97 | 1 | 300 | 33463 | 2078 | False |
| 9 | verified | 95 | 2 | 400 | 54232 | 2610 | False |
| 10 | needs_review | 90 | 2 | 400 | 53395 | 2514 | True |
| 11 | verified | 98 | 0 | 200 | 12930 | 405 | False |

## needs_review pages

[7, 10]

## Diagram → Mermaid conversion

- figures: 6
- converted to Mermaid: 4 (67%)
- data-table fallbacks: 0
- image fallbacks: 2

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 1 | 24 | classDiagram | image | 90 |
| 3 | 25 | classDiagram | mermaid | 95 |
| 7 | 26 | classDiagram | mermaid | 95 |
| 8 | 27 |  | image | 95 |
| 8 | 28 | classDiagram | mermaid | 90 |
| 10 | 29 | classDiagram | mermaid | 98 |

## Omissions log

- page 1: - Sidebar diagram (Unified Notation 0.8) rendered as figure placeholder; its text labels (Used, Base Class, Had by Reference, Had By Value, Derived 1, Derived 2) are described in figure alt text.
- Page number "1" excluded from body as furniture.
- No typo corrections made; source text reproduced as-is (hyphenated line breaks rejoined).
- page 2: - Source typo "make is safer" left as-is per DEC-009? Corrected contextually not applied — kept verbatim ("make is safer to use").
- Epigraph and Liskov quote rendered as block quotes; subscripts o1/o2 rendered as LaTeX math.
- Footnote 1 rendered as GFM footnote.
- No figures on this page.
- page 3: - Transcribed verbatim including source typos: "{itsHeight=w;}" (likely should be itsHeight=h), "Generally these problem are not foreseen", and stray quote marks in "identical.\"." — retained per DEC-009 allowance but noted.
- Figure 1 diagram is wrapped in a bordered box in the source; the diagram region is tokenized.
- page 4: - Page continues from previous page's sentence ("with the design. However, ...") and code block (Rectangle class continues past page end).
- Corrected `s,SetHeight(2)` to `s.SetHeight(2)`; corrected `itsHeight=w` in SetHeight (prior page had typo `itsHeight=w` where `=h` expected) — here the fixed version uses `itsHeight=h` per OCR.
- "heigt" typo in comment retained verbatim (source typo in code comment).
- "We might counter this with argument that" — source grammar retained.
- Header "The Liskov Substitution Principle" and page number "4" excluded from body per rules.
- page 5: - Running header "5 : The Liskov Substitution Principle" and page number "5" excluded from body per rules; recorded here for verification.
- Continued code block from previous page (Rectangle class private section completed at top).
- Paragraph "Thus, we might conclude..." continues from previous page; next paragraph continues onto following page.
- OCR source contains unbalanced parentheses in `assert(r.GetWidth() * r.GetHeight()) == 20);` — reproduced verbatim as in source.
- "mathematical" hyphenated across lines in source ("mathe-matical") joined.
- page 6: - Continuation from previous page: body begins mid-sentence "but cannot operate properly upon...".
- Corrected OCR "Bertrand" for "Bertrand" (source image shows "Bertrand"); no change.
- Kept source typo "has broken these function;" (DEC-009 allowance; not corrected).
- Superscript footnote marker 2 rendered as ²; footnote reproduced at page bottom.
- Heading "What Went Wrong? (W³)" rendered with superscript 3.
- page 7: verification cap reached
- page 8: - Continuation: paragraph "third parties. I did not want..." continues the sentence started on the previous page under "## Motivation" ("I was unhappy with the interfaces of the container classes that were available through").
- Figure 1 is the boxed PrintSet code listing; its code content is transcribed verbatim in the Markdown as follows (kept also as figure region for layout fidelity):
```cpp
template <class T>
void PrintSet(const Set<T>& s)
{
  for (Iterator<T>i(s); i; i++)
    cout << (*i) << endl;
}
```
- Figure 2 (Figure 3 in document numbering) contains node labels: Set, PersistentSet, ThirdParty PersistentSet, PersistentObject; caption "Figure 3. Persistent Set".
- Hyphenation joined: "con-tainers" → "containers", "pro-grammer" → "programmer", "Persistent-Set" → "PersistentSet", "pos-sibly" → "possibly", "Unfor-tunately" → "Unfortunately".
- No [?] uncertainties.
- page 9: - Page continues the "A Real Example / Problem" section from page 8; ends mid-convention narrative, continued on next page.
- No figures on this page (the Figure 3 figure token appears on the prior page in the rolling context).
- Hyphenated line breaks (Persistent-Set, Persisten-tObjects, deriva-tive, sup-posed, Per-sistentSet, non-per-sistent) rejoined per DEC-009; no other corrections needed.
- page 10: verification cap reached
- page 11: No figures on this page. "A.K.A Design by Contract" left as in source.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 235465B model=glm-5.3-flash effort=low transcribe_ms=4571.8 verify_ms=2736.0 ocr_ms=85.1 retries=0 verification_score=95 floor=90% hashes=5998bc4b664a35fec94149313de33b19dbb85fd134d7d74915733ee6c2282de0/e993b9f4270e0b367b753633561d62701b3331eb706d7d4efe88dc8972d616be/983ecc130a49961f87c24112a48582453bfe68ff0d9b3864800b3974f4d15a61/9354e0902f42b10fb0fae4148fefad49dfb93aa41591d9619040351e9aba0f67
- page 2: dpi=200 image=1700x2200 283840B model=glm-5.3-flash effort=low transcribe_ms=4878.0 verify_ms=2973.4 ocr_ms=109.0 retries=0 verification_score=99 floor=97% hashes=7d3a927fedb2f0466ac4bb27a60b6966b57ebebb80d322cfef2d408c118f13aa/eeb0c00b3313ca8d080bca5b25f722dc75af6723dfee7b855a3a71998e378048/b0abf7be68d5d77b28d876f51661acc459874a1f0cd0ac279852433996c9ace2/93a0c7461bf2cc64bdd85617cb0d8ed54297940a811b1aa24ab7cb85b397ed03
- page 3: dpi=200 image=1700x2200 311095B model=glm-5.3-flash effort=low transcribe_ms=6203.0 verify_ms=3927.2 ocr_ms=96.5 retries=0 verification_score=95 floor=96% hashes=11471c5890ef936407054f477fab795aa927c84addb70d9bb3583ef42fbd629b/835b3e81ef192ddcab2cf3412b752f70f058aca8920299980fcbfa86b38aed37/de9a735cd32cecd1d125620997d4a94e8a13bebfe3965f11c05fff530c6d478e/d505763ec11e6e64c6c185bb858513f5af5b8c642da5151012ab392f986f98e4
- page 4: dpi=400 image=3400x4400 547594B model=glm-5.3-flash effort=low transcribe_ms=31726.3 verify_ms=9533.6 ocr_ms=594.8 retries=2 verification_score=95 floor=98% hashes=3f81b3bd7f28876042dcbd7bbf4d0e3d87765bfd3a23c91beed2097585a800ad/4991f4d9f451b2f15d5e37bd6c50e6bc8440b31c2bae9e6e32529207e5bfc358/a01bbc3e33280b4bea9c6d57c1154179af2b6fe34f80e3869ebdbd96e1fc3322/9a8a0164e88c7eb4952065a6a6fbd1ec747ded5fa84e8a6b11c4bc5acf2a2c33
- page 5: dpi=400 image=3400x4400 511860B model=glm-5.3-flash effort=low transcribe_ms=16030.9 verify_ms=10948.7 ocr_ms=551.4 retries=2 verification_score=95 floor=96% hashes=3eede37b33c7352b889d5e1652978a23493c8e6764781e715de2c8b42aacf634/f49a4a4f07de37f73350dd93339360b9e9fbb3f68d587a2907c60058d0329785/6d65a887d19d243d967e23cfb03873b016f99ee616e5d7f1df79c4180acc93df/9ee8f4acd921063e057f0bbcb23ff3d92be609663c04a2ea9988752ab84186ee
- page 6: dpi=200 image=1700x2200 315516B model=glm-5.3-flash effort=low transcribe_ms=5100.6 verify_ms=3109.0 ocr_ms=102.5 retries=0 verification_score=97 floor=95% hashes=54c35f03b60a7928f744b9858364824b720e2a7ccb2d9d5699b725cd78aa6562/c572e36b928e76ec0227de039dc906bcc43dff62714305412a3363087974a6a4/3e21d5f473a8d588df83de1d9895d5038a39796fdeb095c4309ccfc6b0c3e5d8/1fe1a0f9b446d15051bbb9972e3b174e073ea132a0d9ea81a36db399a9b0392c
- page 7: dpi=400 image=3400x4400 557758B model=glm-5.3-flash effort=low transcribe_ms=22389.7 verify_ms=11670.8 ocr_ms=610.8 retries=2 verification_score=90 floor=93% hashes=3139caea835157409600e3d29231fae14ad99cbca86103956cdac4632b59dd05/7c5c18f5585dd8d4668a5a053ce8f2a85a57cf27f8e295db1ea362fab0be374a/7fff2c12ac45f1d28b74c8dee067f000cae13ed2b89a1f14f5f52db1d3889cf7/101dcb7b5286eb14e982b2f70c9dc3e8eed953330a6ddd4703e839ad5e7ed555
- page 8: dpi=300 image=2550x3300 453283B model=glm-5.3-flash effort=low transcribe_ms=17033.9 verify_ms=7308.1 ocr_ms=281.6 retries=1 verification_score=97 floor=94% hashes=0b0379aa336daf205062c82dd3f302c1227c09caa2d814728e0ebea250779141/a181912aa2809a559024f3483ce5099643e66ae3a7c2c5e2c7aa66abab49a52f/973d71254f96a6a5ca86f58d81e6cc650d3c8ab6a85967e7e7d0f9e73de4588d/a77a81ab862060da4548f1165df3fbd76a00c91b9ab9013fa05ec6f23677de82
- page 9: dpi=400 image=3400x4400 623663B model=glm-5.3-flash effort=low transcribe_ms=19422.7 verify_ms=10659.1 ocr_ms=582.7 retries=2 verification_score=95 floor=96% hashes=7c9f94ba5b733809a41052bb36cafdd827d4c4d24741f5e3d79f610ffdb884ee/908b84af3088e3e1dbf7b817e957823beb8545cd052b75b88b9a4143f2e4059d/44f8642c42ca68016690ccfc761c52428594a7e3732f61cabf14af9a0d9d55d3/36067efc7adf902e138421c0c9999961f3db80bc9aedd49311db1d0eafa1a7cc
- page 10: dpi=400 image=3400x4400 568361B model=glm-5.3-flash effort=low transcribe_ms=26532.8 verify_ms=14293.8 ocr_ms=565.6 retries=2 verification_score=90 floor=92% hashes=a2687ffe4f42e685a535ffb5b0d0c067a473d38cfbca4e2f11cdd01df33d1d2d/2843f16496c0718cd16566772a1baf234be91dd88c64a3ffd240a0dbd204e0b8/0e9c7cf2552944625f0219dbff9aca3df26b7be1ecc9d0b4a57f900cc7b672ca/13924e2ccf9a815d0d381dee3c2cdfda16b208b6ac575d234630ae3b51bc0d92
- page 11: dpi=200 image=1700x2200 158060B model=glm-5.3-flash effort=low transcribe_ms=3670.2 verify_ms=2430.4 ocr_ms=81.5 retries=0 verification_score=98 floor=97% hashes=c1d6d2f7b602001014273b610443910f77a383d6a9638fa1607cd7ff674b71fd/acacb667d5af5778d630e63c5c68268cf504fa357039036aac980c814655925f/0482fb65cc221958346f77c5e8f248240e94d7ac1009c0adce9f61c55b0028f7/2de79a05e5619c1479012a4f8692906cac2a4de489e2a3e83a90683b28284364

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:20: [Expected: 80, Actual: 510]
- MD013:22: [Expected: 80, Actual: 156]
- MD036:24:
- MD033:26: [Element: details]
- MD013:29: [Expected: 80, Actual: 238]
- MD013:35: [Expected: 80, Actual: 349]
- MD013:37: [Expected: 80, Actual: 388]
- MD013:39: [Expected: 80, Actual: 305]
- MD024:41:
- MD025:41:
- MD013:43: [Expected: 80, Actual: 126]
- MD013:45: [Expected: 80, Actual: 136]
- MD013:47: [Expected: 80, Actual: 293]
- MD013:49: [Expected: 80, Actual: 419]
- MD013:53: [Expected: 80, Actual: 164]
- MD013:65: [Expected: 80, Actual: 294]
- MD013:67: [Expected: 80, Actual: 276]
- MD013:69: [Expected: 80, Actual: 94]
- MD026:71:
- MD013:73: [Expected: 80, Actual: 146]
- MD013:89: [Expected: 80, Actual: 271]
- MD013:96: [Expected: 80, Actual: 127]
- MD033:98: [Element: details]
- MD013:107: [Expected: 80, Actual: 264]
- MD013:109: [Expected: 80, Actual: 196]
- MD013:111: [Expected: 80, Actual: 390]
- MD013:113: [Expected: 80, Actual: 398]
- MD013:115: [Expected: 80, Actual: 346]
- MD013:117: [Expected: 80, Actual: 122]
- MD013:133: [Expected: 80, Actual: 275]
- MD013:150: [Expected: 80, Actual: 343]
- MD013:152: [Expected: 80, Actual: 579]
- MD013:154: [Expected: 80, Actual: 105]
- MD013:193: [Expected: 80, Actual: 461]
- MD013:195: [Expected: 80, Actual: 227]
- MD013:206: [Expected: 80, Actual: 367]
- MD013:208: [Expected: 80, Actual: 254]
- MD013:210: [Expected: 80, Actual: 231]
- MD013:214: [Expected: 80, Actual: 472]
- MD013:216: [Expected: 80, Actual: 228]
- MD013:220: [Expected: 80, Actual: 175]
- MD013:222: [Expected: 80, Actual: 311]
- MD013:224: [Expected: 80, Actual: 455]
- MD013:226: [Expected: 80, Actual: 168]
- MD013:230: [Expected: 80, Actual: 340]
- MD029:232: [Expected: 1; Actual: 2; Style: 1/2/3]
- MD013:240: [Expected: 80, Actual: 95]
- MD013:242: [Expected: 80, Actual: 147]
- MD013:244: [Expected: 80, Actual: 607]
- MD013:246: [Expected: 80, Actual: 294]
- MD013:248: [Expected: 80, Actual: 464]
- MD025:250:
- MD026:250:
- MD013:266: [Expected: 80, Actual: 222]
- MD033:268: [Element: details]
- MD036:273:
- MD013:277: [Expected: 80, Actual: 166]
- MD029:283: [Expected: 1; Actual: 3; Style: 1/2/3]
- MD013:285: [Expected: 80, Actual: 259]
- MD013:287: [Expected: 80, Actual: 108]
- MD013:300: [Expected: 80, Actual: 341]
- MD013:304: [Expected: 80, Actual: 613]
- MD013:308: [Expected: 80, Actual: 346]
- MD013:321: [Expected: 80, Actual: 266]
- MD033:323: [Element: details]
- MD013:326: [Expected: 80, Actual: 149]
- MD036:328:
- MD013:332: [Expected: 80, Actual: 99]
- MD013:334: [Expected: 80, Actual: 294]
- MD013:348: [Expected: 80, Actual: 468]
- MD013:350: [Expected: 80, Actual: 658]
- MD025:352:
- MD026:352:
- MD013:354: [Expected: 80, Actual: 816]
- MD013:356: [Expected: 80, Actual: 320]
- MD013:358: [Expected: 80, Actual: 364]
- MD025:360:
- MD013:362: [Expected: 80, Actual: 749]
- MD013:389: [Expected: 80, Actual: 215]
- MD033:391: [Element: details]
- MD036:396:
- MD013:410: [Expected: 80, Actual: 238]
- MD025:412:
- MD013:414: [Expected: 80, Actual: 525]
- MD013:416: [Expected: 80, Actual: 686]
