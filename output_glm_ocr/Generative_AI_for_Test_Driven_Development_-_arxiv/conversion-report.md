# Conversion report — Generative AI for Test Driven Development - arxiv.pdf

- job_id: 95a9af03-9e85-495e-ad59-07c7363dc30b
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=153160 completion=9252
- pipeline_version: 77ca3a05b80cc24b9f872d6b9b7d3a5a3e45d53f35b87e62d9835656f30dcc5e
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 73

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 98 | 0 | 200 | 12363 | 822 | False |
| 2 | verified | 98 | 0 | 200 | 13234 | 865 | False |
| 3 | verified | 100 | 0 | 200 | 13880 | 840 | False |
| 4 | verified | 95 | 2 | 400 | 54858 | 2756 | False |
| 5 | verified | 98 | 0 | 200 | 14570 | 964 | False |
| 6 | verified | 96 | 0 | 200 | 14505 | 1052 | False |
| 7 | verified | 97 | 0 | 200 | 14499 | 860 | False |
| 8 | verified | 98 | 0 | 200 | 15251 | 1093 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 1
- converted to Mermaid: 0 (0%)
- data-table fallbacks: 0
- image fallbacks: 1

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 58 | flowchart | image | 95 |

## Omissions log

- page 1: No figures on page. arXiv sidebar stamp excluded from body (furniture). Superscript footnote markers rendered as ¹/². No typo corrections needed; OCR text matched source verbatim.
- page 2: No figures on page. Page begins mid-sentence continuing from page 1. ⟨ ⟩ angle-bracket placeholders preserved. No typo corrections made; "prevent from doing so" is source phrasing.
- page 3: Page continues from previous page: the "– Final iteration" bullet item belongs to the prompt list begun on page 2. Continuation sentence ("...modify the input passed to the AI in") continues onto page 4. No figures on this page; Fig. 1 referenced but appears on a later page. No uncertain characters.
- page 4: ["Figure 1 is a workflow diagram spanning the top of the page; transcribed as placeholder with caption 'Fig. 1. Fully-automated pattern'.", "Text begins mid-sentence, continuing from previous page: '...the developer can modify' follows 'the developer can modify the input passed to the AI in activity ③' from prior page context.", "Table 1 source text '< 1 years' for P4/P5 Python Experience kept verbatim as it appears in the source table (not corrected, as it may be intentional).", "Circled numbers ①②③ rendered as unicode circled digits."]
- page 5: Code block at bottom (ChatGPT recommendation) continues on next page. Curly quote characters in code block normalized to straight quotes. No figures on this page.
- page 6: - The code block continues from the previous page (item 1 appeared there); items 2–3 transcribed here as continuation of the same fenced block from the prior page context.
- The final sentence "...but without replacing" continues on the next page.
- Code block: reformatted wrapped lines of the OCR verbatim text into a single fenced block; backtick-style quotes in source rendered as backticks.
- No figure regions on this page.
- page 7: No figures on this page. Paragraph at top of body ("developers in terms of creativity...") continues the sentence from page 6 ("...without replacing"). Conclusions section ends mid-sentence, continues on page 8.
- page 8: Page continues Section 5 (Conclusions) from previous page; the body text here resumes the paragraph cut off at the end of page 7 ("...for our experiment and settings, GenAI can be efficiently used in TDD..."). Running header ("8  Moritz Mock, Jorge Melegati, and Barbara Russo") excluded from body. Hyphenated line-break words rejoined ("method-ology", "Develop-ment", "En-gineering", "formal-ization", "devel-oper"). No figures on this page.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 314126B model=glm-5.3-flash effort=low transcribe_ms=8150.9 verify_ms=3225.3 ocr_ms=361.1 retries=0 verification_score=98 floor=94% hashes=1964c7cade1db971a180794d5a9f107e14ee1f9ac7b029611b05c613e32099ba/649897b2f7db240c132fe92c9c0649ab608ae7a2b7c57e11d3d304a52c920655/688f57078d8ba5b9524782167cf287a243c58580d3c3a5f0b5dd9d38798e5a06/d9569cef90555f8bea945b731cafaf34eac04b10c80d13d3eda015b62b459dc8
- page 2: dpi=200 image=1700x2200 375495B model=glm-5.3-flash effort=low transcribe_ms=6391.5 verify_ms=5082.4 ocr_ms=359.6 retries=0 verification_score=98 floor=97% hashes=3c648d8a8ad82d73cb3ad8682164e9dd6d1eff4634e3d208ce3528912bb2cdf2/2097b825ff6e6ae62164cb5147145d318ebc4976006ff4c1f75e9a842aa3cd22/2bcc31d6bd6e2807a8240f6979f8ad6d00fafcf1396a7d4216d81c387226a632/fe04bad2b7187c5b29167c5b759d1cb7c7a88b3e508f771fe6177c0732b33428
- page 3: dpi=200 image=1700x2200 377854B model=glm-5.3-flash effort=low transcribe_ms=7348.5 verify_ms=3475.1 ocr_ms=381.1 retries=0 verification_score=100 floor=99% hashes=6d8946229ce606afd2d87696403caf0101d9e89a904d19116b0dd0fe97abe035/aff78325cb55fa51fec9b9392070b4e6ef96d9d90df8b6ba912b1b8cae5133d9/198bfe0dcf17096dc90d003535c2d91b7fbd7b7b74a45e9e920bce162a4f28f8/3135576c670cefef1bab595ff6f39ad221bfe3d30976fb3b099cde345f9e4319
- page 4: dpi=400 image=3400x4400 541097B model=glm-5.3-flash effort=low transcribe_ms=24870.9 verify_ms=19071.6 ocr_ms=3217.9 retries=2 verification_score=95 floor=90% hashes=32e24aa9bee2ee11f48a382710253abb427086a93cb7db1ecb5e0af6504dea45/a8691b26e7985e3658b6074648518c0dfc1016a070b0bbb817a2e8f1c1cda56d/5bc3597a624462d594fe69910a9ca61946fd2c4c3f1f1ed51e177a7de40a82b1/8ed4ad40734c84a403967ef861ebb579b8a1aa9031b296488d816583c216e832
- page 5: dpi=200 image=1700x2200 340524B model=glm-5.3-flash effort=low transcribe_ms=9023.1 verify_ms=3808.7 ocr_ms=382.0 retries=0 verification_score=98 floor=99% hashes=44deedf3162db13b3c4bb6e3a72ac287bbda44100286431ad4562a2bce10698b/04e32695178e626fd0f301944013f9806cc08a7cfaa42b0d1d1bdfb74dfea6d2/3c736a84688fc4a3d47bb532f9d06b011e828fcd1a93ee3045fda6eebb06b9c2/a06b275698ae080029cff644fdc9e144289538a0b145ebec6db210fcdc2e9e4a
- page 6: dpi=200 image=1700x2200 343544B model=glm-5.3-flash effort=low transcribe_ms=9409.4 verify_ms=5023.6 ocr_ms=353.7 retries=0 verification_score=96 floor=98% hashes=8cfd0be1b76af5ca8574a616f35d45b0d001350825be92b20291ad67e28f045e/5187b870b93b25e34f6475f857dd9f2e45c1cbe1c234673f06901d6951b78e8c/0319b9bbde5142f0aae776a75e79120d534b36a19c143b16e8c653a6775a51b1/c2afd5e57442b1fba4e495432ecc6d7a9d687bb4ce32f045a75886d8f82ec1d4
- page 7: dpi=200 image=1700x2200 370883B model=glm-5.3-flash effort=low transcribe_ms=7799.5 verify_ms=4701.6 ocr_ms=339.1 retries=0 verification_score=97 floor=97% hashes=a0785837b1858dda78f6e96da32f0e32a949627f5aebe1fec56e1bd021f630b0/698739cc078a2ed4fb950d766b43327b237c7be93c1221028c4f34080c29bc04/b7cbe7efa4db4c4f44679a19665adbf7f3dac47c4fb450d8f03a635c998277d5/561a534e4bcb2e5dfc797e01081be5e2194ab9cf0a252934dcb54278e82e36d5
- page 8: dpi=200 image=1700x2200 388311B model=glm-5.3-flash effort=low transcribe_ms=11199.6 verify_ms=3142.5 ocr_ms=103.0 retries=0 verification_score=98 floor=97% hashes=139af2dfceaa712a4219f2d96163cb24fdeda73a739de7814c5dec1941d53072/7bd35a4831ba08e0f631bd9be6e5ec288eef541b8ad48cbb7fcaed3b7088f151/dfc5e5e711a91494c1b28a54cf1898a89e9c09e489ed944716ad4839a0f150dd/16a8774998859aad0450fb117c69a6d272e6d810c6ec6da3a3f3b007adf28d86

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:13: [Expected: 80, Actual: 109]
- MD013:18: [Expected: 80, Actual: 1109]
- MD013:24: [Expected: 80, Actual: 878]
- MD034:26:
- MD034:27:
- MD013:29: [Expected: 80, Actual: 138]
- MD013:31: [Expected: 80, Actual: 238]
- MD013:35: [Expected: 80, Actual: 2333]
- MD013:37: [Expected: 80, Actual: 247]
- MD013:38: [Expected: 80, Actual: 138]
- MD013:42: [Expected: 80, Actual: 942]
- MD013:44: [Expected: 80, Actual: 551]
- MD013:46: [Expected: 80, Actual: 616]
- MD034:46:
- MD013:50: [Expected: 80, Actual: 1018]
- MD013:52: [Expected: 80, Actual: 156]
- MD036:54:
- MD033:56: [Element: details]
- MD013:59: [Expected: 80, Actual: 179]
- MD013:65: [Expected: 80, Actual: 187]
- MD013:67: [Expected: 80, Actual: 337]
- MD013:69: [Expected: 80, Actual: 290]
- MD013:71: [Expected: 80, Actual: 640]
- MD013:75: [Expected: 80, Actual: 98]
- MD013:76: [Expected: 80, Actual: 98]
- MD013:77: [Expected: 80, Actual: 98]
- MD013:78: [Expected: 80, Actual: 98]
- MD013:79: [Expected: 80, Actual: 98]
- MD013:80: [Expected: 80, Actual: 98]
- MD013:81: [Expected: 80, Actual: 98]
- MD013:83: [Expected: 80, Actual: 145]
- MD013:85: [Expected: 80, Actual: 97]
- MD013:86: [Expected: 80, Actual: 97]
- MD013:87: [Expected: 80, Actual: 97]
- MD013:88: [Expected: 80, Actual: 97]
- MD013:89: [Expected: 80, Actual: 97]
- MD013:90: [Expected: 80, Actual: 97]
- MD013:91: [Expected: 80, Actual: 97]
- MD013:92: [Expected: 80, Actual: 97]
- MD013:94: [Expected: 80, Actual: 154]
- MD013:96: [Expected: 80, Actual: 1628]
- MD013:98: [Expected: 80, Actual: 510]
- MD029:106: [Expected: 1; Actual: 2; Style: 1/2/3]
- MD013:112: [Expected: 80, Actual: 248]
- MD013:114: [Expected: 80, Actual: 1657]
- MD013:118: [Expected: 80, Actual: 318]
- MD013:119: [Expected: 80, Actual: 318]
- MD013:120: [Expected: 80, Actual: 318]
- MD013:121: [Expected: 80, Actual: 318]
- MD013:122: [Expected: 80, Actual: 318]
- MD013:123: [Expected: 80, Actual: 318]
- MD013:124: [Expected: 80, Actual: 318]
- MD013:126: [Expected: 80, Actual: 318]
- MD013:130: [Expected: 80, Actual: 2403]
- MD013:134: [Expected: 80, Actual: 305]
- MD013:136: [Expected: 80, Actual: 545]
- MD013:140: [Expected: 80, Actual: 229]
- MD013:145: [Expected: 80, Actual: 155]
- MD013:146: [Expected: 80, Actual: 220]
- MD013:147: [Expected: 80, Actual: 132]
- MD013:148: [Expected: 80, Actual: 117]
- MD013:149: [Expected: 80, Actual: 195]
- MD013:150: [Expected: 80, Actual: 130]
- MD013:151: [Expected: 80, Actual: 141]
- MD013:152: [Expected: 80, Actual: 119]
- MD013:153: [Expected: 80, Actual: 101]
- MD013:154: [Expected: 80, Actual: 161]
- MD013:155: [Expected: 80, Actual: 151]
- MD013:156: [Expected: 80, Actual: 164]
- MD034:156:
- MD013:157: [Expected: 80, Actual: 226]
- MD013:158: [Expected: 80, Actual: 167]
- MD034:158:
