% --------------------------------------------------------------------------
% OUTLINE STUB -- headings only, no content yet.
% Lines beginning with '%' are MyST comments: visible here, absent from the build.
% Full provenance table: ~/.claude/plans/i-want-to-build-immutable-axolotl.md
% --------------------------------------------------------------------------
%
% SOURCES FOR THIS CHAPTER:
%   - 06-325 notes/review_optimization.ipynb -- in that book's TOC this
%     is the page IMMEDIATELY BEFORE intro_ml
%   - Chapra Part 4: Ch. 13 p. 351, Ch. 14 p. 367, Ch. 16 p. 413

# Optimization

## Finding extrema

% 06-325 review_optimization; Chapra Ch. 13 p. 351. Golden-section
%   search is Chapra 13.1 p. 352 if a derivative-free method is wanted.

## Set the derivative to zero

% 06-325 frames minimization as 'finding the zeros of the derivative of
%   a nonlinear function' -- an explicit callback to Ch. 13.

## scipy.optimize.minimize

% 06-325 review_optimization, 'Standard python approach'.

## Multiple minima and global optimization

% 06-325 same notebook: a periodic function with minima near 2.2 and
%   4.5, then basinhopping. Chapra 14.1 p. 368.

## Functions of several variables

% 06-325 same notebook uses Himmelblau's function, (x^2+y-11)^2 +
%   (x+y^2-7)^2. NOTE: 06-325 deliberately reuses the SAME function as
%   an ML regression target in overfitting_regularization.ipynb --
%   preserve that link into Ch. 21.

## Gradient methods

% Chapra 14.2 p. 372. Include so that 'gradient descent' is not a new
%   idea when Part III arrives.

## Regression as minimization

% THE BRIDGE. 06-325's own section heading is the thesis: 'Regression of
%   data is a form of function minimization.'
% Quote to work from: 'When we say regression, we really mean find some
%   parameters of a model that best reproduces some known data. By best
%   reproduces we mean the sum of all the errors between the values
%   predicted by the model, and the real data is minimized.'
% Also its note on why squared rather than absolute error -- 'it has a
%   continuous derivative' -- which forward-references the ML unit.

## Chemical engineering application

% Chapra 16.1 p. 413: least-cost design of a tank -- the designated
%   Chemical/Bio case study for Part 4.
% 06-325 fits a Birch-Murnaghan equation of state to energy-volume data.
%   That is materials, not ChemE; consider substituting a ChemE
%   equation-of-state fit (van der Waals or Peng-Robinson against P-V-T
%   data) to stay in domain.
