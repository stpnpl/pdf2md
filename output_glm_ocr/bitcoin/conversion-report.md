# Conversion report — bitcoin.pdf

- job_id: 716eb161-a931-46d1-9277-72d4e6c0703a
- status: assembling
- pages: 9
- wall-clock: not started
- tokens: prompt=122356 completion=6805
- pipeline_version: 77ca3a05b80cc24b9f872d6b9b7d3a5a3e45d53f35b87e62d9835656f30dcc5e
- prompts: {'transcription': 'transcription-v2', 'verification': 'verification-v2', 'diagram': 'diagram-v1', 'diagram_verification': 'diagram-verification-v1'}
- models: agent=glm-5.3-flash ocr=glm-ocr
- dpi: 200
- lint warnings: 77

## Per-page coverage

| page | status | coverage | retries | dpi | prompt_tok | completion_tok | needs_review |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | verified | 100 | 0 | 200 | 12358 | 669 | False |
| 2 | verified | 97 | 0 | 200 | 12770 | 800 | False |
| 3 | verified | 98 | 0 | 200 | 13649 | 834 | False |
| 4 | verified | 95 | 0 | 200 | 14144 | 871 | False |
| 5 | verified | 97 | 0 | 200 | 13733 | 754 | False |
| 6 | verified | 97 | 0 | 200 | 13983 | 820 | False |
| 7 | verified | 98 | 0 | 200 | 14028 | 768 | False |
| 8 | verified | 99 | 0 | 200 | 14183 | 811 | False |
| 9 | verified | 100 | 0 | 200 | 13508 | 478 | False |

## needs_review pages

none

## Diagram → Mermaid conversion

- figures: 7
- converted to Mermaid: 4 (57%)
- data-table fallbacks: 0
- image fallbacks: 3

| page | index | type | status | confidence |
| --- | --- | --- | --- | --- |
| 2 | 40 | flowchart | image | 90 |
| 2 | 41 | flowchart | mermaid | 92 |
| 3 | 42 | flowchart | image | 90 |
| 4 | 43 | flowchart | mermaid | 95 |
| 5 | 44 | flowchart | mermaid | 92 |
| 5 | 45 | flowchart | image | 80 |
| 6 | 46 | flowchart | mermaid | 95 |

## Omissions log

- page 1: No figures on this page. No corrections needed; source text matches standard form.
- page 2: No typo corrections needed. No uncertain characters. Diagram labels (Transaction, Owner's Public Key, Hash, Signature, Verify, Sign, Block, Item) are represented by figure placeholders rather than transcribed as body text.
- page 3: List step numbers "1)" ... "6)" in source converted to Markdown ordered list (1.–6.). Figure bbox estimated from block diagram position on page.
- page 4: Figure is a single composite image containing two side-by-side Merkle tree diagrams; kept as one figure region. No typo corrections made. Continuation: opening paragraph completes Section 5 (Network) from the previous page. Section numbering continues from previous pages.
- page 5: - Page 5 continues from Section 7 (Reclaiming Disk Space) on page 4; this page begins Section 8.
- No typo corrections needed.
- No uncertain characters.
- page 6: Page 6 of Bitcoin whitepaper. The privacy diagram region rendered as figure placeholder; its labels (Traditional Privacy Model, New Privacy Model, Identities, Transactions, Trusted Third Party, Counterparty, Public) are recorded in the figure alt text. The piecewise equation was reconstructed from the OCR's garbled brace layout. No typo corrections made.
- page 7: Continuation of Section 11 (Calculations) from previous page. No figures on this page. No typo corrections needed. Equations rendered as LaTeX math from the OCR/reference image representation.
- page 8: No figures on this page (page 8 of the Bitcoin whitepaper, containing end of Section 11 results and Section 12 Conclusion). Page number "8" at bottom center excluded from body.
- page 9: No figures on this page. Reference list converted from bracketed labels [1]–[8] to a GFM numbered list; text verbatim, italics added for journal/proceedings names per source italicization.

## Running furniture stripped

none

## Per-page telemetry (FR-AGT-10)

- page 1: dpi=200 image=1700x2200 336238B model=glm-5.3-flash effort=low transcribe_ms=6285.4 verify_ms=3760.7 ocr_ms=99.7 retries=0 verification_score=100 floor=100% hashes=d6e2f38823c869115faac4f01ab7dea1d398a0e83fd8453ac2d9aa9f7fbb7bd5/8e1a0c8d3947469c7bec09ffa1d18caf80d52cdfca164bd9627b10c4c51f54a3/427e85bed23ec53ebc591a19298b304fdb516fbb95eef92c70c8d3a66353fca5/a8ab02851b92c00ad722b2830978dc5d6b9def13ce54d4a344bd84c3de15cb64
- page 2: dpi=200 image=1700x2200 284373B model=glm-5.3-flash effort=low transcribe_ms=7578.4 verify_ms=3657.4 ocr_ms=97.4 retries=0 verification_score=97 floor=95% hashes=f9948c67dd4011aebc6d452e3bdf683fa2697c17f41612143f7f1784db4e97ee/48be9cc639d62eee69acb2e0fbcfd7e028367fc95c8e0bc425c98e1c9c1e769f/ce59cf4ceb97cdf0ff506f35112208c62e97adfbd8a6c6e58810068ebafa11b3/a102d8a77dca6ef9fef093aa4625d6c451f42a17b8c0f0d39041607807944993
- page 3: dpi=200 image=1700x2200 353335B model=glm-5.3-flash effort=low transcribe_ms=8088.5 verify_ms=3469.6 ocr_ms=111.1 retries=0 verification_score=98 floor=99% hashes=64134eaee44d2964aa5c52def2708d287e1764395ab39b37194d358ceb875eaa/1096044ea6a81876dc6d57fc3698a37cfa68ef4ae343d3c9dcea6c4ad3a069c8/8226a28d8f4ee4ea47f2c7bc44a632e514679aaf386e6cc90c23493111d863dd/267fed0c868fca5ee42757a47f360c0141009cadde93a8d55ca5c449770d4698
- page 4: dpi=200 image=1700x2200 327622B model=glm-5.3-flash effort=low transcribe_ms=7128.2 verify_ms=3898.2 ocr_ms=109.6 retries=0 verification_score=95 floor=95% hashes=0daecae88b85d3ad7f07a7131e17f6d2ac1ccad790939fc265315689cf987113/a9a27b534a89a68a48b894f112c1ef13021d63d4f6db4c37059d09e1e63c4784/951e68d241b3c2ab020b9e9e9ca01f75485f02d5955f6e3f6caa725da57889fd/b5204ff6995ed79d8dd951fef3bc51398329f14246a9007d97fc2e6599123d2b
- page 5: dpi=200 image=1700x2200 276070B model=glm-5.3-flash effort=low transcribe_ms=7033.9 verify_ms=3345.3 ocr_ms=100.9 retries=0 verification_score=97 floor=94% hashes=a908726d2917ae3575783217d25d4f8f2473c24cd0b4c52f4fca8271084ba1d6/0dd85db1997be6ad65e391b7b3c359a3c1ffde7f61f463cc76cb73d37ccb8f8e/7c2999520cfec635c2fb86bebca2150182a84b7bcaf087139e4a19c56ee00436/2c97c4cc60e6c0dd729d77799be3fa1041f217ca604f30e1958fb6030907f492
- page 6: dpi=200 image=1700x2200 304207B model=glm-5.3-flash effort=low transcribe_ms=8595.2 verify_ms=3505.7 ocr_ms=107.1 retries=0 verification_score=97 floor=99% hashes=176d0b231f889a838467a690c661536b3f7c68986ed117a1f5272e39d5efded8/115700d6733d38e34435d533d1496906654556ddb622197221d39dcebb12d416/26b059aad12e1fc100a141d48d4da509675a70222ed375a11785761fe92af8d4/5ac6df0a82f5683d1c66cf118082115c569054a3a0d2c05a4ef55855ea759fe0
- page 7: dpi=200 image=1700x2200 259411B model=glm-5.3-flash effort=low transcribe_ms=6193.6 verify_ms=3180.6 ocr_ms=108.0 retries=0 verification_score=98 floor=99% hashes=78205fb552a99f2a9c17a59576c503b2d63af63f98e7853eb399b4d8c450689c/0b289e586b9bb0c7121faa95ed010cb2cf67ad91b642ca865232225ecefbd160/e293e261f46b18ce7b4538dde42ea37530afa6f94691b4d63f2e15fc1928ec19/f6c3dd1c43125c4ae24ed613daa370474c3fcc2e71ff46a0fb74dffdd1c746d1
- page 8: dpi=200 image=1700x2200 215528B model=glm-5.3-flash effort=low transcribe_ms=7134.6 verify_ms=2768.9 ocr_ms=122.5 retries=0 verification_score=99 floor=100% hashes=17110863cb1558037f3dd2c179eed093f5711e47ac95240cdf70955a0c354dfb/41aae7856b28dba5cbcf9aa73495f95a062d991f48d7e2bd2ee52e3a491c2f38/f5cddb1a04bc75aeff575033d24b4fcc85c01cda7cbb339e07a84d7f0b08d0c9/3a9aa6b8ac56125db5a75602ed8638850d754b0ef41ae9a7491359ab795696fa
- page 9: dpi=200 image=1700x2200 155714B model=glm-5.3-flash effort=low transcribe_ms=5425.8 verify_ms=2283.5 ocr_ms=110.4 retries=0 verification_score=100 floor=99% hashes=7b09e8df46f536b0f860a0c3c4e882660b499598f3374f6ce5815a81a175dc5d/382bbb0cf72bfa12e9f1b234f5fa4f087a4c591399fd401ee14cb6fe7e580ffc/7de2f62fcd9846bd0fb270435b35e876ec89ffc0cccbd5d68421de2ed905ef19/6fd97ddb96e1713cb8a0c1a2d5b77176baa1c32e78e713241244c57db34e847a

## Figures placed without placeholder (appended at page end)

none

## Lint warnings (non-fatal)

- MD013:23: [Expected: 80, Actual: 1134]
- MD013:27: [Expected: 80, Actual: 1098]
- MD013:29: [Expected: 80, Actual: 700]
- MD013:33: [Expected: 80, Actual: 306]
- MD013:35: [Expected: 80, Actual: 156]
- MD033:37: [Element: details]
- MD013:40: [Expected: 80, Actual: 242]
- MD013:44: [Expected: 80, Actual: 572]
- MD013:46: [Expected: 80, Actual: 721]
- MD013:50: [Expected: 80, Actual: 460]
- MD013:61: [Expected: 80, Actual: 133]
- MD033:63: [Element: details]
- MD013:66: [Expected: 80, Actual: 156]
- MD033:68: [Element: details]
- MD013:71: [Expected: 80, Actual: 126]
- MD013:78: [Expected: 80, Actual: 444]
- MD013:80: [Expected: 80, Actual: 413]
- MD013:82: [Expected: 80, Actual: 123]
- MD013:84: [Expected: 80, Actual: 816]
- MD013:86: [Expected: 80, Actual: 260]
- MD013:96: [Expected: 80, Actual: 89]
- MD013:97: [Expected: 80, Actual: 157]
- MD013:99: [Expected: 80, Actual: 507]
- MD013:101: [Expected: 80, Actual: 315]
- MD013:105: [Expected: 80, Actual: 500]
- MD013:107: [Expected: 80, Actual: 391]
- MD013:109: [Expected: 80, Actual: 461]
- MD013:113: [Expected: 80, Actual: 410]
- MD013:150: [Expected: 80, Actual: 236]
- MD033:152: [Element: details]
- MD013:155: [Expected: 80, Actual: 155]
- MD036:157:
- MD033:159: [Element: details]
- MD013:162: [Expected: 80, Actual: 251]
- MD013:167: [Expected: 80, Actual: 366]
- MD037:167:
- MD037:167:
- MD013:171: [Expected: 80, Actual: 543]
- MD013:215: [Expected: 80, Actual: 238]
- MD033:217: [Element: details]
- MD013:220: [Expected: 80, Actual: 156]
- MD036:222:
- MD033:224: [Element: details]
- MD013:227: [Expected: 80, Actual: 156]
- MD013:232: [Expected: 80, Actual: 730]
- MD013:236: [Expected: 80, Actual: 462]
- MD036:240:
- MD013:242: [Expected: 80, Actual: 242]
- MD013:246: [Expected: 80, Actual: 661]
- MD013:252: [Expected: 80, Actual: 100]
- MD013:263: [Expected: 80, Actual: 269]
- MD033:265: [Element: details]
- MD013:268: [Expected: 80, Actual: 156]
- MD033:270: [Element: details]
- MD013:273: [Expected: 80, Actual: 178]
- MD013:278: [Expected: 80, Actual: 390]
- MD013:282: [Expected: 80, Actual: 511]
- MD013:284: [Expected: 80, Actual: 296]
- MD013:286: [Expected: 80, Actual: 380]
- MD013:294: [Expected: 80, Actual: 282]
- MD013:296: [Expected: 80, Actual: 405]
- MD013:298: [Expected: 80, Actual: 447]
- MD013:300: [Expected: 80, Actual: 336]
- MD013:304: [Expected: 80, Actual: 194]
- MD013:306: [Expected: 80, Actual: 147]
- MD040:335:
- MD040:365:
- MD013:379: [Expected: 80, Actual: 1113]
- MD025:381:
- MD034:383:
- MD013:384: [Expected: 80, Actual: 191]
- MD013:385: [Expected: 80, Actual: 129]
- MD013:386: [Expected: 80, Actual: 204]
- MD013:387: [Expected: 80, Actual: 169]
- MD013:388: [Expected: 80, Actual: 112]
- MD034:388:
- MD013:389: [Expected: 80, Actual: 158]
