% --------------------------------------------------------------------------
% OUTLINE STUB -- headings only, no content yet.
% Lines beginning with '%' are MyST comments: visible here, absent from the build.
% Full provenance table: ~/.claude/plans/i-want-to-build-immutable-axolotl.md
% --------------------------------------------------------------------------
%
% SOURCES FOR THIS CHAPTER:
%   - CHME212 docs/chapter16/16_notebook.ipynb
%   - Chapra Part 2: Ch. 5 p. 120, Ch. 6 p. 142, Ch. 8 p. 202

# Roots of Equations

## What is a root, and graphical methods

% CHME212 ch16 16.1; Chapra 5.1 p. 120.

## Polynomial roots: np.roots

% CHME212 ch16 16.2: van der Waals as a cubic, plus its 'why eigenvalues
%   = roots?' aside -- ties straight back to Ch. 12.

## Bracketing methods: bisection

% CHME212 ch16 16.3; Chapra 5.2 p. 124. Also false position, Chapra 5.3
%   p. 132.

## Open methods: Newton-Raphson and secant

% CHME212 ch16 16.4 incl. quadratic-vs-linear convergence and failure
%   modes; Chapra 6.2 p. 148, 6.3 p. 154.
% NOTE: CHME212 nests a heading numbered 16.3.2 under 16.4 -- renumber.

## The practical choice: brentq

% CHME212 ch16 16.5; Chapra 6.4 p. 159.

## Systems of nonlinear equations: fsolve

% CHME212 ch16 16.6; Chapra 6.6 p. 167. CHME212's example finds two
%   roots from two different initial guesses -- keep that.

## Chemical engineering applications

% CHME212 ch16 16.7: gas-phase equilibrium A <=> 2B, y_A=(1-Xe)/(1+Xe),
%   K=1.5 at 600 K and 2 atm, solve for Xe then sweep pressure. Plus van
%   der Waals molar volume via brentq.
% Chapra 8.1 p. 202: ideal and nonideal gas laws -- the designated
%   Chemical/Bio case study for Part 2.

## Choosing a method

% CHME212 ch16 has a closing 'root-finding workflow' plus common
%   pitfalls. Keep as a decision table.
