Benchmark familiarity experiment - compact result bundle
========================================================

Published with:
https://davidschiff100.github.io/learning/blog/benchmark-familiarity/

This bundle contains aggregate and component-level results needed to inspect the
figures in the post. It intentionally excludes the sampled source text and model
weights. See benchmark_experiment_findings.pdf for the complete methodology,
limitations, model revisions, and interpretation.

Primary temporal outcome
------------------------
Neutral prompt, 50% prefix, bits per UTF-8 byte. Each benchmark family receives
equal weight; ARC Easy and ARC Challenge are averaged into one family.

Older model slope: +0.0566 bits/byte/year
Newer model slope: +0.0541 bits/byte/year
Newer-minus-older slope: -0.00249 bits/byte/year
95% descriptive family-bootstrap interval: [-0.0788, +0.0826]

Files
-----
pilot-dataset-summary.csv       Pilot means by model, group, prompt, and prefix.
pilot-contrasts.csv             OLMES versus IOL cluster-bootstrap contrasts.
pilot-cue-effect.csv            Benchmark-cue minus neutral comparisons.
temporal-components.json        Component means by model and analysis condition.
temporal-statistics.json        Temporal slopes and family-bootstrap intervals.
temporal-coverage.json          Number of scorable items by condition/component.
temporal-leave-one-out.json     Primary slope with each family excluded.
temporal-manifest.json          Dates, source links, splits, indices, and hashes.
word-topk-pilot-summary.csv     Top-5/top-10 accuracy and shared-word coverage.
word-topk-pilot-contrasts.csv   OLMES-minus-control word-accuracy contrasts.
word-topk-model-advantages.csv  Paired newer-minus-older accuracy differences.
word-topk-temporal-components.csv  Word-rank accuracy by benchmark component.
word-topk-temporal-statistics.json Word-rank date slopes and family intervals.
word-topk-vocabulary.json       Shared one-token word-vocabulary definition/hash.

Interpretation
--------------
These are exploratory prediction-loss measurements, not calibrated training-set
membership probabilities. Corpus controls are verified corpus members, but exact
checkpoint consumption is unverified. The compared models differ substantially in
size, architecture, tokenizer, training volume, and data mixture.

Calibration-free word-rank check
--------------------------------
The addendum reports top-1, top-5 and top-10 ranks for the correct next
literal-space word among 28,853 identical
candidate strings that each model encodes as one canonical token. Multi-token
targets are excluded from both models, yielding 80.2% coverage on the OLMES pilot.
The newer-minus-older OLMES gain is +7.1 percentage points at top-1, +7.5 at
top-5 and +8.1 at top-10. The novel English IOL control gains +10.3 top-1 and
+12.6 top-5 points, so model ability remains a confound. The newer-advantage date
slopes are +0.017/year at top-1 (95% family-bootstrap interval [-0.029,+0.079]),
-0.010/year at top-5 ([-0.036,+0.013]) and -0.021/year at top-10
([-0.090,+0.029]).
