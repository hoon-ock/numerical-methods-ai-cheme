% --------------------------------------------------------------------------
% OUTLINE STUB -- headings only, no content yet.
% Lines beginning with '%' are MyST comments: visible here, absent from the build.
% Full provenance table: ~/.claude/plans/i-want-to-build-immutable-axolotl.md
% --------------------------------------------------------------------------
%
% SOURCES FOR THIS CHAPTER:
%   - CHME212 docs/chapter13/13_notebook.ipynb
%   - 06-262 notes/statistics/24-intro-statistics.ipynb, 25-statistics-
%     continue-linear-regression.ipynb
%   - CHME212 docs/lab09/09_lab.ipynb (Monte Carlo uncertainty
%     propagation)
%   - Chapra 4.2 p. 94 (error propagation); PT5.2 p. 441 (simple
%     statistics)

# Probability and Statistics

## Deterministic versus stochastic models

% 06-262 lecture 24 opens with three sources of non-determinism:
%   uncertain parameters, genuinely stochastic models ('chemical
%   kinetics at very small concentrations'), and model-form uncertainty.
%   Best available framing.

## Descriptive statistics

% CHME212 ch13 13.1, incl. why ddof=1 (Bessel's correction) and
%   scipy.stats.describe.

## Random sampling and reproducibility

% CHME212 ch13 13.2: default_rng, seeds.

## Distributions: PDF, CDF, and the normal distribution

% CHME212 ch13 13.3 (uniform, normal, 68-95-99.7, CDF and PPF).
% 06-262 lecture 24 cross-checks the error-function CDF against
%   scipy.integrate.quad of the PDF -- a nice tie back to Ch. 14.

## Histogram pitfalls

% 06-262 lecture 24: unnormalized counts and bin-size dependence, fixed
%   with gaussian_kde. Also its better idea -- fit the empirical CDF
%   instead, 'no binning error here'.

## The central limit theorem

% CHME212 ch13 13.4 (incl. the standard error of the mean); 06-262
%   lecture 24 demonstrates it with repeated coin-toss averages and
%   justifies it for ChemE: 'many chemical engineering examples are the
%   result of a huge number of independent random interactions... so we
%   often get Gaussian distributions -- but should be checked'.

## Confidence intervals

% CHME212 ch13 13.5: Z-interval (known sigma) and t-interval (unknown
%   sigma).
% 06-262 lecture 25 has the carefully-worded interpretation sentence
%   plus the advice to verify your interpretation by direct sampling.
%   Both courses stop short of formal hypothesis testing -- no t-test,
%   no p-values. Decide whether to add.

## Error propagation

% ADDITION, and the most conspicuous gap in both reference courses --
%   the phrase does not appear anywhere in 06-262, and it is standard
%   for junior/senior ChemE lab work.
% Analytical: Chapra 4.2 p. 94.
% Monte Carlo: CHME212 lab09 has process reliability from input
%   uncertainty, heat-exchanger outlet-temperature reliability, and
%   batch-reactor yield. This is also where CHME212's dropped ch14
%   (Monte Carlo Simulation) survives.

## Chemical engineering applications

% CHME212 ch13: batch reaction yield data (15 values, mean 87.7%, std
%   1.8%), thermocouple drift, flow-meter noise, 'is the process in
%   control?'.
% CHME212 lab08: pressure-relief-valve distribution analysis.
