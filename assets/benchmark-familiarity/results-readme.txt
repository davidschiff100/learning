Benchmark familiarity experiment - full-word result bundle
===========================================================

Published with:
https://davidschiff100.github.io/learning/blog/benchmark-familiarity/

Both experiments use teacher-forced top-1, top-5 and top-10 reconstruction of
every complete literal-space word in the second half of each text. A word is a hit
only when every tokenizer token composing that word is within the corresponding
next-token cutoff. Multi-token words and attached punctuation are included.

Why this score
--------------
Raw negative log probability depends on probability calibration. Per-step top-k
membership depends only on candidate order and is invariant to additive logit
shifts and positive temperature rescaling. Full-word reconstruction tests whether
the complete true token path survives that cutoff under teacher forcing.

This is not a claim that the sequence is globally among the k most probable words.
Tokenizer fragmentation remains a limitation: a word split into more pieces has
more chances to fail. On OLMES, GPT-2 averages 1.27 tokens per word and MiniCPM
1.21. Model capability, domain, size and training volume also remain confounded.

Main results
------------
Experiment 1: newer-minus-older OLMES gains are +7.3 percentage points at top-1,
+7.9 at top-5 and +8.7 at top-10. Novel English IOL gains are +7.5, +14.2 and
+10.8 points, respectively, so general predictive ability remains a sufficient
explanation.

Experiment 2: newer-minus-older benchmark-date slopes are +0.024/year at top-1
(95% family-bootstrap interval [-0.014,+0.075]), -0.020/year at top-5
([-0.079,+0.024]), and -0.016/year at top-10 ([-0.062,+0.028]). A negative slope
matches the proposed leakage pattern. The direction changes with k and every
interval includes zero.

Files
-----
full-word-pilot-summary.csv       Group accuracy, word counts and tokenization.
full-word-pilot-contrasts.csv     OLMES-minus-control reconstruction contrasts.
full-word-model-advantages.csv    Paired newer-minus-older differences.
full-word-temporal-components.csv Reconstruction by benchmark and model.
full-word-temporal-statistics.json Date slopes and family-bootstrap intervals.
full-word-pilot-runtime.json      Recorded control-run time and hardware.
full-word-temporal-runtime.json   Recorded temporal-run time and hardware.
temporal-manifest.json            Benchmark dates, sources, indices, and hashes.
run_full_word_topk.py              Inference and exact word-span reconstruction.
analyze_full_word_topk.py          Summaries, intervals, and graph generation.

The bundle excludes sampled source text, model weights, and local model files. The
scripts expect the frozen project inputs and model directories described in the PDF.
These are exploratory familiarity measurements, not membership probabilities.
