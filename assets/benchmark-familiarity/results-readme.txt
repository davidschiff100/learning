Benchmark familiarity experiment - word-rank result bundle
===========================================================

Published with:
https://davidschiff100.github.io/learning/blog/benchmark-familiarity/

Both experiments use exact next-word top-1, top-5 and top-10 accuracy at the
neutral 50% continuation boundary. Words are divided at literal ASCII spaces.
The candidate vocabulary is the intersection of 28,853 strings that both model
tokenizers encode as one canonical token. Multi-token targets are excluded from
both models, so eligible positions and denominators match exactly.

Why this score
--------------
Raw negative log probability depends on probability calibration. Top-k membership
depends only on candidate order and is invariant to additive logit shifts and
positive temperature rescaling. The shared word vocabulary also prevents different
subword candidate sets from driving the comparison. The tradeoff is that the score
covers common one-token words rather than all words and still confounds memory with
model capability.

Main results
------------
Experiment 1: newer-minus-older OLMES gains are +7.1 percentage points at top-1,
+7.5 at top-5, and +8.1 at top-10. Novel English IOL gains are +10.3 at top-1 and
+12.6 at top-5, so general predictive ability remains a sufficient explanation.

Experiment 2: newer-minus-older benchmark-date slopes are +0.017/year at top-1
(95% family-bootstrap interval [-0.029,+0.079]), -0.010/year at top-5
([-0.036,+0.013]), and -0.021/year at top-10 ([-0.090,+0.029]). A negative slope
matches the proposed leakage pattern. The direction changes with k and every
interval includes zero.

Files
-----
word-topk-pilot-summary.csv       Group accuracy and shared-word coverage.
word-topk-pilot-contrasts.csv     OLMES-minus-control accuracy contrasts.
word-topk-model-advantages.csv    Paired newer-minus-older differences.
word-topk-temporal-components.csv Accuracy by benchmark component and model.
word-topk-temporal-statistics.json Date slopes and family-bootstrap intervals.
word-topk-vocabulary.json         Shared-vocabulary definition and SHA-256.
temporal-manifest.json            Benchmark dates, sources, indices, and hashes.
run_word_topk.py                   Inference and shared-vocabulary construction.
analyze_word_topk.py               Summaries, intervals, and chart generation.

The bundle excludes sampled source text, model weights, and local model files. The
scripts expect the frozen project inputs and model directories described in the PDF.
These are exploratory familiarity measurements, not training-membership probabilities.
