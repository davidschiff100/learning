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

Interpretation
--------------
These are exploratory prediction-loss measurements, not calibrated training-set
membership probabilities. Corpus controls are verified corpus members, but exact
checkpoint consumption is unverified. The compared models differ substantially in
size, architecture, tokenizer, training volume, and data mixture.
