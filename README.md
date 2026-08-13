# Code Switching NLP | Code Saviours SI-26 | Humna Imran

Project 2 of the Code Saviours SI-26 internship: a labeled dataset of naturally
code-switched **Roman Urdu + English** sentences — the way ~230 million
Pakistanis actually write online (e.g. *"Aaj mera mood nahi hai for anything"*).

## What's in this repo

| File | Description |
|---|---|
| `SI26-Week6-Humna.ipynb` | Colab notebook — collects, filters, and labels the dataset end to end |
| `dataset.csv` | Final labeled dataset (220 sentences, 2,490 word-level rows) |

## Method

Instead of manually copying tweets one by one, this project pulls from an
existing **real, public Roman Urdu dataset** and mines it for sentences that
are genuinely code-switched, then labels them automatically:

1. **Source data** — [`Smat26/Roman-Urdu-Dataset`](https://github.com/Smat26/Roman-Urdu-Dataset)
   on GitHub, a public, UCI-referenced compilation of 20,000+ Roman Urdu
   sentences gathered from Twitter, Facebook comments, and e-commerce reviews
   (compiled by Zareen Sharf, GPL-3.0 license).
2. **Filtering** — kept only sentences with genuine bilingual mixing: 2+
   English-tagged words and 3+ Urdu-tagged words, with Urdu still the
   majority language (max ~55% English).
3. **Word-level labeling (URD / ENG / MIX)** — dictionary lookup against the
   top 10,000 common English words (`google-10000-english`), with a curated
   override list for Roman Urdu words that collide with English spellings
   (e.g. `"mil"`, `"beta"`, `"par"`, `"is"`). This mirrors the approach used
   in prior Roman Urdu code-switching research (Ali & Sabir, arXiv:2103.02252,
   who built the English side of their labeler from the `dwyl/english-words`
   list the same way).
4. **Manual spot-check** — a random sample was reviewed and corrected before
   publishing, since dictionary-based labeling is a bootstrapping method, not
   a gold standard.

## Dataset stats

- 220 sentences
- 2,490 word-level rows
- Label distribution: ~73% URD, ~27% ENG (MIX is rare — mostly hyphenated hybrids)

## Label meanings

- `URD` — Roman Urdu word
- `ENG` — English word
- `MIX` — hybrid/hyphenated token combining both

## Limitations

Automatic labeling can misclassify short words that happen to exist in both
languages (e.g. "to", "par"). The curated override list reduces this but
doesn't eliminate it — treat labels as high-quality silver annotations, spot
checked, rather than perfect gold-standard.

## Credit

Source sentences: [`Smat26/Roman-Urdu-Dataset`](https://github.com/Smat26/Roman-Urdu-Dataset)
(GPL-3.0), originally compiled by Zareen Sharf, referenced at the
[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/Roman+Urdu+Data+Set).

## Links

- Hugging Face dataset: `https://huggingface.co/datasets/[your-username]/code-switching-codesaviours-si26-humna`
