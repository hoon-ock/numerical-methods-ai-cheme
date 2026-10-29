% --------------------------------------------------------------------------
% OUTLINE STUB -- headings only, no content yet.
% Lines beginning with '%' are MyST comments: visible here, absent from the build.
% Full provenance table: ~/.claude/plans/i-want-to-build-immutable-axolotl.md
% --------------------------------------------------------------------------
%
% SOURCES FOR THIS CHAPTER:
%   - Chapra 6th ed. Ch. 1 (p. 11), Ch. 3 (p. 52), Ch. 4 (p. 78)
%   - 06-262 notes/linear_algebra/1-intro-matrices.ipynb
%   - 06-262 notes/ordinary_differential_equations/15-springs-numerical-
%     odes.ipynb

# Numerical Methods in Chemical Engineering

## What is a mathematical model?

% Chapra 1.1 p. 11. Eq. (1.1): dependent variable = f(independent
%   variables, parameters, forcing functions). Use this form as the
%   organizing scaffold for the whole book.

## The engineering problem-solving loop

% 06-262 lecture 1, the 5-step loop: statement -> formulation ->
%   analysis -> solution -> evaluation.
% Key lines to keep: 'solve the *mathematical* problem (which is not the
%   same as the engineering problem)' and 'most of your math courses
%   only dealt with steps 3 & 4'.

## Conservation laws are where chemical engineering equations come from

% Chapra 1.2 p. 18: Change = increases - decreases; steady state In =
%   Out. Fig. 1.6 tabulates conservation laws by field.

## Analytical versus numerical: the trade-off

% 06-262 lecture 15 has a two-column pros/cons table (analytical: exact,
%   shows which parameters matter, gives functional form; numerical:
%   fast, solves hard problems, but approximate and 'hard to check if
%   answer is correct'). It is currently buried 15 lectures in -- it
%   belongs here.

## Worked example: a draining tank

% REPLACES Chapra's falling parachutist (Examples 1.1/1.2, p. 15-17),
%   which is mechanics with no ChemE content.
% Use Chapra problems 1.7/1.8 (tank, liquid depth y, outflow) for the
%   same three-beat structure: first-order ODE -> closed-form solution
%   -> Euler -> error versus step size.

## Where you will use this

% 06-262 lecture 1 downstream-course map: fluids / Navier-Stokes;
%   reaction engineering; unit ops / distillation; heat and mass
%   transfer; process design.

## The motivating problem: a recycle flowsheet

% 06-262 lecture 1: mixer -> reactor -> flash -> splitter with recycle.
%   3 components x 6 streams, 17 longhand mole balances.
% Punchlines: 'That's a mess!' and 'real chemical plants have about
%   10^5-10^6 unknowns and equations'.
% FORWARD REFERENCES: Ch. 11 solves this system; Ch. 11.5 (rank) answers
%   'do I have enough equations?'. Redraw the flowsheet locally --
%   06-262's figure is a remote Google Drawing.

## Error: round-off, truncation, and floating point

% ADDITION to the author's draft. Neither reference course covers error
%   analysis, but Ch. 14's order-of-accuracy claims and Ch. 15's
%   tolerance discussion are unmotivated without it.
% Chapra Ch. 3 p. 52 (significant figures, accuracy vs precision, error
%   definitions, round-off) and Ch. 4 p. 78 (Taylor series, error
%   propagation, total numerical error).
% 06-262 lecture 15 ends with a floating-point saturation demo: error
%   stops improving at ~16 digits. Use
%   cheme_numerics.plotting.annotate_convergence() for the log-log plot.
