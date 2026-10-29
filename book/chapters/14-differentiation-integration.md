% --------------------------------------------------------------------------
% OUTLINE STUB -- headings only, no content yet.
% Lines beginning with '%' are MyST comments: visible here, absent from the build.
% Full provenance table: ~/.claude/plans/i-want-to-build-immutable-axolotl.md
% --------------------------------------------------------------------------
%
% SOURCES FOR THIS CHAPTER:
%   - CHME212 docs/chapter15/15_notebook.ipynb
%   - Chapra Part 6: Ch. 21 p. 601, Ch. 22 p. 631, Ch. 23 p. 653, Ch. 24
%     p. 671

# Numerical Differentiation and Integration

## Two problems you cannot solve by hand

% CHME212 ch15 opens this way. Keep it.

## The geometric picture

% CHME212 ch15 15.1; Chapra PT6.1 p. 585 and Fig. PT6.3 (differentiation
%   and integration as inverse operations, via position/velocity).

## Finite differences and np.gradient

% CHME212 ch15 15.2, incl. 15.2.2 reaction rate from concentration data;
%   Chapra Ch. 23 p. 653.

## The trapezoidal rule

% CHME212 ch15 15.3 incl. the trapezoid visualization; Chapra 21.1 p.
%   603.

## Simpson's rules and order of accuracy

% ADDITION -- Chapra 21.2 p. 613. CHME212 jumps from trapezoid straight
%   to quad. Simpson is where 1.8's error-order lesson pays off; show
%   the observed order with annotate_convergence().

## Adaptive quadrature: scipy.integrate.quad

% CHME212 ch15 15.4; Chapra 22.3 p. 638 (adaptive quadrature, new in the
%   6th ed.). Gauss quadrature is Chapra 22.4 p. 640 if wanted.

## Cumulative integration

% CHME212 ch15 15.5: cumulative_trapezoid.

## Differentiating noisy data

% ADDITION -- Chapra 23.4 p. 659. Motivated by 06-262 lecture 26's hard-
%   won lesson: 'derivatives tend to MAGNIFY errors in data'. This
%   section sets up Ch. 17.10.

## Chemical engineering applications

% CHME212 ch15 15.6: full PFR design -- mole balance -> design equation
%   -> Levenspiel plot -> quad -> conversion-versus-volume sizing chart.
%   The strongest worked example in CHME212.
% CHME212 ch15 15.4.2: Delta-H for 1 mol N2, 300 -> 1200 K, from the
%   NIST Shomate Cp(T).
% Chapra 24.1 p. 671: total quantity of heat, Delta-H = m * integral
%   c(T) dT.

## When to use which tool

% CHME212 ch15 closes with this table. Keep.
