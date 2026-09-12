# Conversion report — Generative AI for Test Driven Development - arxiv.pdf

- job_id: db12dc6a-d93e-4335-98d4-d02073cefe4e
- status: assembling
- pages: 8
- wall-clock: not started
- tokens: prompt=111558 completion=7815
- pipeline_version: e0804123b115bceb6fe27a3fb5bbe5cb5c3757a3a32381593bed7112ec02ec58
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 73

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 95 | 0 | 200 | 12331 | 951 | False |
| 2 | verified | 98 | 0 | 200 | 13160 | 862 | False |
| 3 | verified | 95 | 0 | 200 | 13811 | 943 | False |
| 4 | verified | 96 | 0 | 200 | 13931 | 875 | False |
| 5 | verified | 97 | 0 | 200 | 14565 | 1001 | False |
| 6 | verified | 96 | 0 | 200 | 14344 | 1084 | False |
| 7 | verified | 98 | 0 | 200 | 14305 | 1061 | False |
| 8 | verified | 98 | 0 | 200 | 15111 | 1038 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 1
- converted to Mermaid: 1 (100%)
- data-table fallbacks: 0
- image fallbacks: 0

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 4 | 130 | flowchart | mermaid | 92 |

## Omissions log

- page 1: - Running arXiv sidebar banner ("arXiv:2405.10849v1 [cs.SE] 17 May 2024") and top-right date "17 May 2024" are marginal furniture, excluded from body.
- Footnote URLs 1 and 2 transcribed at end of body as they appear at bottom of page.
- Ligatures/hyphenation joined across line breaks (e.g., "practices", "developers", "experiment").
- No figures or tables on this page.
- page 2: Page continues from previous page (mid-sentence "can speed up testing"). No figures on this page. Angle brackets in prompts rendered as LaTeX $\langle...\rangle$; kept source spelling "automatize" as-is per DEC-009. "prevent from doing so" left uncorrected as likely source wording.
- page 3: - Page begins by continuing the bullet list of prompts from Section 2 (page 2).
- Circled numbers ① and ② preserved as Unicode.
- Header and page number excluded from body.
- page 4: Fig. 1 shows the fully-automated TDD workflow: feature/test case → specify prompt (Prompt note) → develop failing test (AI) with Test/Prompt note → develop code (AI) → execute tests → Pass/Fail? decision (Pass loops back to specify prompt; Fail loops via Repeat through "Choose prompt" (activity 5) with an Error Trace/Code/Test note labeled Prompt) — transcribed as figure placeholder per rules. Uncertain bbox for Fig. 1 (approximate). Page ends mid-sentence continuing on page 5. No typo corrections made.
- page 5: No figures on this page. The monospace log output from ChatGPT is rendered as a fenced code block; line wrapping follows the source layout, with the quoted variable name broken across lines as in the original ('textFormatter'). Table 2 caption continues from prior page context.
- page 6: - Continuation of a `text` code block started on page 5 (ChatGPT-recommended changes, items 2 and 3).
- The line "variable was mistakenly assigned instead of ` textFormatter`." contains a hard line wrap in the source with the opening backtick at the end of the previous line; reproduced as in source.
- No figures on this page.
- page 7: No figures on this page. The final sentence is incomplete and continues on the next page ("for our experiment and settings," ...). No typos or uncertain characters observed.
- page 8: Continuation of Section 5 Conclusions from previous page (first paragraph completes the sentence begun on page 7: "...for our experiment and settings, GenAI can be efficiently used in TDD..."). No figures on this page. Header excluded from body.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 314126B model=glm-5.3-flash effort=low transcribe_ms=5563.3 verify_ms=3663.0 ocr_ms=22821.5 retries=0 verification_score=95 floor=99% hashes=1964c7cade1db971a180794d5a9f107e14ee1f9ac7b029611b05c613e32099ba/649897b2f7db240c132fe92c9c0649ab608ae7a2b7c57e11d3d304a52c920655/7c370e103d63562bc1b82edf8a63e16c7401f64cbe0232f78fbc9a83ee783bdc/14d7c0d49df1eb0119fd8731cd91c1366761c5106ee63a3fa6e8647d7d7a08f7
- page 2: dpi=200 image=1700x2200 375495B model=glm-5.3-flash effort=low transcribe_ms=5089.6 verify_ms=2920.8 ocr_ms=23566.4 retries=0 verification_score=98 floor=100% hashes=3c648d8a8ad82d73cb3ad8682164e9dd6d1eff4634e3d208ce3528912bb2cdf2/2097b825ff6e6ae62164cb5147145d318ebc4976006ff4c1f75e9a842aa3cd22/88b02b75cb86ca2ff13849bea728c5aa021ea6c39ec8293139908f606ec2f3b7/cd667c49d97e66b5600fc08cdeb9eb6b0fd3d48a85e47579f8fecdef07a45905
- page 3: dpi=200 image=1700x2200 377854B model=glm-5.3-flash effort=low transcribe_ms=5952.4 verify_ms=4244.8 ocr_ms=22347.0 retries=0 verification_score=95 floor=100% hashes=6d8946229ce606afd2d87696403caf0101d9e89a904d19116b0dd0fe97abe035/aff78325cb55fa51fec9b9392070b4e6ef96d9d90df8b6ba912b1b8cae5133d9/f0de9a4c9fba4c44efc930bdea4f0dd0261a0318732513d439e97c1d0bdf8933/928505a12e0c238a03b392d5f383b133d018b913592a731aef10c10d0106215c
- page 4: dpi=200 image=1700x2200 271130B model=glm-5.3-flash effort=low transcribe_ms=5652.2 verify_ms=3335.4 ocr_ms=18015.7 retries=0 verification_score=96 floor=100% hashes=32e24aa9bee2ee11f48a382710253abb427086a93cb7db1ecb5e0af6504dea45/e8eba92ee8548bf5889de49b9ab7b0b45a8e0de04008758cb997656f2e848014/6ab9752babea71f9ddb8861e24a90c1189e6a6c69939ed16336c949617842aa2/cddf2f83c813d3d45fa49c1f1d222e0aac061c9b8402f9069ef755550ab83539
- page 5: dpi=200 image=1700x2200 340524B model=glm-5.3-flash effort=low transcribe_ms=7033.0 verify_ms=3118.4 ocr_ms=24816.1 retries=0 verification_score=97 floor=100% hashes=44deedf3162db13b3c4bb6e3a72ac287bbda44100286431ad4562a2bce10698b/04e32695178e626fd0f301944013f9806cc08a7cfaa42b0d1d1bdfb74dfea6d2/7bbdaa390b2f3fbc5be92b53b938af997b7883fd2857a0f0e85dd1b51053dc79/a85ccc35402098be6c790682ce50b9978ac340df5037d3c3e53ce20bd7d924ec
- page 6: dpi=200 image=1700x2200 343544B model=glm-5.3-flash effort=low transcribe_ms=7070.1 verify_ms=3498.1 ocr_ms=22176.1 retries=0 verification_score=96 floor=100% hashes=8cfd0be1b76af5ca8574a616f35d45b0d001350825be92b20291ad67e28f045e/5187b870b93b25e34f6475f857dd9f2e45c1cbe1c234673f06901d6951b78e8c/4afe8dadbdcca2cc2adb3bd055ab1f564ee4e5238dc107ecf8907e56ebbfbbd8/887fc5a0b074d23c2f3f98fc1a32b2da2c0200e65c55bb6455e4060da3306bb7
- page 7: dpi=200 image=1700x2200 370883B model=glm-5.3-flash effort=low transcribe_ms=7444.4 verify_ms=3414.2 ocr_ms=21952.8 retries=0 verification_score=98 floor=100% hashes=a0785837b1858dda78f6e96da32f0e32a949627f5aebe1fec56e1bd021f630b0/698739cc078a2ed4fb950d766b43327b237c7be93c1221028c4f34080c29bc04/4d96ea8f32b087dec64b681b8ce7a0bc1084f0fb7d307217b7de9d3fa3db8734/561a534e4bcb2e5dfc797e01081be5e2194ab9cf0a252934dcb54278e82e36d5
- page 8: dpi=200 image=1700x2200 388311B model=glm-5.3-flash effort=low transcribe_ms=6828.2 verify_ms=2425.6 ocr_ms=31158.3 retries=0 verification_score=98 floor=100% hashes=139af2dfceaa712a4219f2d96163cb24fdeda73a739de7814c5dec1941d53072/7bd35a4831ba08e0f631bd9be6e5ec288eef541b8ad48cbb7fcaed3b7088f151/2765b8ec85bd4e919b9538cb567ac94cbf1a67ff2c37a9f1338ebeda77e297bf/16a8774998859aad0450fb117c69a6d272e6d810c6ec6da3a3f3b007adf28d86

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:13: [Expected: 80, Actual: 127]
- MD013:18: [Expected: 80, Actual: 1109]
- MD013:24: [Expected: 80, Actual: 884]
- MD034:26:
- MD034:27:
- MD013:29: [Expected: 80, Actual: 138]
- MD013:31: [Expected: 80, Actual: 238]
- MD013:35: [Expected: 80, Actual: 2335]
- MD013:37: [Expected: 80, Actual: 304]
- MD013:38: [Expected: 80, Actual: 138]
- MD013:41: [Expected: 80, Actual: 942]
- MD013:43: [Expected: 80, Actual: 549]
- MD013:45: [Expected: 80, Actual: 616]
- MD034:45:
- MD013:49: [Expected: 80, Actual: 1018]
- MD013:68: [Expected: 80, Actual: 253]
- MD033:70: [Element: details]
- MD036:75:
- MD013:81: [Expected: 80, Actual: 187]
- MD013:83: [Expected: 80, Actual: 337]
- MD013:85: [Expected: 80, Actual: 290]
- MD013:87: [Expected: 80, Actual: 640]
- MD013:91: [Expected: 80, Actual: 98]
- MD013:92: [Expected: 80, Actual: 98]
- MD013:93: [Expected: 80, Actual: 98]
- MD013:94: [Expected: 80, Actual: 98]
- MD013:95: [Expected: 80, Actual: 98]
- MD013:96: [Expected: 80, Actual: 98]
- MD013:97: [Expected: 80, Actual: 98]
- MD013:99: [Expected: 80, Actual: 145]
- MD013:101: [Expected: 80, Actual: 97]
- MD013:102: [Expected: 80, Actual: 97]
- MD013:103: [Expected: 80, Actual: 97]
- MD013:104: [Expected: 80, Actual: 97]
- MD013:105: [Expected: 80, Actual: 97]
- MD013:106: [Expected: 80, Actual: 97]
- MD013:107: [Expected: 80, Actual: 97]
- MD013:108: [Expected: 80, Actual: 97]
- MD013:110: [Expected: 80, Actual: 154]
- MD013:112: [Expected: 80, Actual: 1628]
- MD013:114: [Expected: 80, Actual: 510]
- MD029:123: [Expected: 1; Actual: 2; Style: 1/2/3]
- MD038:124:
- MD013:128: [Expected: 80, Actual: 248]
- MD013:130: [Expected: 80, Actual: 1657]
- MD013:134: [Expected: 80, Actual: 312]
- MD013:135: [Expected: 80, Actual: 312]
- MD013:136: [Expected: 80, Actual: 312]
- MD013:137: [Expected: 80, Actual: 312]
- MD013:138: [Expected: 80, Actual: 312]
- MD013:139: [Expected: 80, Actual: 312]
- MD013:140: [Expected: 80, Actual: 312]
- MD013:142: [Expected: 80, Actual: 318]
- MD013:146: [Expected: 80, Actual: 2403]
- MD013:150: [Expected: 80, Actual: 305]
- MD013:152: [Expected: 80, Actual: 545]
- MD013:156: [Expected: 80, Actual: 229]
- MD013:161: [Expected: 80, Actual: 155]
- MD013:162: [Expected: 80, Actual: 220]
- MD013:163: [Expected: 80, Actual: 132]
- MD013:164: [Expected: 80, Actual: 117]
- MD013:165: [Expected: 80, Actual: 195]
- MD013:166: [Expected: 80, Actual: 130]
- MD013:167: [Expected: 80, Actual: 141]
- MD013:168: [Expected: 80, Actual: 119]
- MD013:169: [Expected: 80, Actual: 101]
- MD013:170: [Expected: 80, Actual: 161]
- MD013:171: [Expected: 80, Actual: 151]
- MD013:172: [Expected: 80, Actual: 164]
- MD034:172:
- MD013:173: [Expected: 80, Actual: 226]
- MD013:174: [Expected: 80, Actual: 167]
- MD034:174:
