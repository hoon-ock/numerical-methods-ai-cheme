% --------------------------------------------------------------------------
% OUTLINE STUB -- headings only, no content yet.
% Lines beginning with '%' are MyST comments: visible here, absent from the build.
% Full provenance table: ~/.claude/plans/i-want-to-build-immutable-axolotl.md
% --------------------------------------------------------------------------
%
% SOURCES FOR THIS CHAPTER:
%   - CHME212 docs/chapter12/12_notebook.ipynb
%   - 06-262 notes/statistics/25-statistics-continue-linear-
%     regression.ipynb, 26-bonus-nonlinear-regression.ipynb
%   - Chapra Part 5: Ch. 17 p. 454, Ch. 18 p. 488, Ch. 20 p. 561

# Curve Fitting and Regression

## Two different problems: regression and interpolation

% Chapra PT5.1 p. 439: noisy data -> least-squares regression; precise
%   tabular data -> interpolation. Its own motivation is already ChemE
%   -- steam tables, and heat capacity of gases as a function of
%   temperature (PT5.1.2 p. 440).

## Polynomials in NumPy

% CHME212 ch12 12.2: poly1d, polyval, polyfit.

## Least-squares fitting

% CHME212 ch12 12.3; Chapra 17.1 p. 454. Polynomial regression is Chapra
%   17.2 p. 470.

## The normal equations: regression is linear algebra

% 06-262 lecture 25 builds the design matrix and solves
%   np.linalg.solve(X.T@X, X.T@y) explicitly, then shows it is exactly
%   the SSE minimizer by plotting a 1-D slice through the SSE surface
%   with the solution at the bottom of the well.
% Frame regression as 'linear in the coefficients', y = sum a_i f_i(x),
%   so arbitrary nonlinear basis functions are fair game. Ties directly
%   back to Ch. 11. Chapra 17.4 p. 477 (general linear least squares).

## Fit quality: MAE, MSE, R-squared -- and when they disagree

% CHME212 ch12 12.3.2 and 12.3.3 ('MAE vs R-squared: They Can
%   Disagree').

## Degrees of freedom and overfitting

% CHME212 ch12 12.3.4 and 12.3.5 ('Overfitting: When Higher Degree
%   Hurts'). This is already most of the way into Part III -- the only
%   missing ingredient is held-out data.

## Residual diagnostics

% 06-262 lecture 25: 'if the residuals do not look gaussian distributed
%   and random, you are probably missing additional physics'.

## Parameter confidence intervals

% 06-262 lecture 25 uses statsmodels. Keep its in-class task: judge from
%   the confidence interval whether the quadratic term is warranted --
%   model selection by CI is a transferable habit.

## Interpolation and splines

% Chapra Ch. 18 p. 488: Newton divided-difference p. 489, Lagrange p.
%   500, splines 18.6 p. 509. KEEP BRIEF -- interpolation is the lesser
%   half of Part 5 for this audience. Chapra 20.2 p. 565 uses splines to
%   find a thermocline where d2T/dx2 = 0, which is a transport-flavored
%   gradient-estimation application if a ChemE hook is wanted.

## Nonlinear regression: curve_fit

% 06-262 lecture 26: rate constant and reaction order from batch C_A(t)
%   data. First by log-linearization (numerically differentiate, then
%   regress in log space), THEN the critique -- residuals show a
%   systematic sigmoidal trend, 'derivatives tend to magnify errors in
%   data', and taking logs nonlinearly transforms the errors so the
%   confidence limits are skewed. Then redone as true nonlinear
%   regression with curve_fit (p0 guesses, multiple minima) and lmfit
%   for parameter uncertainty.
% This is the best single example in either course for 'the convenient
%   transformation costs you something'. Chapra 17.5 p. 481.

## Chemical engineering applications

% CHME212 ch12 12.1: NIST tabulated Cp(T) for CO2, 10 points 300-1200 K,
%   motivated by Q = n * integral Cp dT.
% CHME212 lab07 Problem 2: viscosity data with degrees of freedom and
%   overfitting.
% Chapra 20.1 p. 561: linearizing a nonlinear growth model to fit it by
%   linear regression. Chapra problems 20.4-20.8 (nitrogen P-T,
%   superheated steam specific volume, stratified reactor, stirred tank
%   reactor) are better teaching material than its case studies.

% This chapter is the hinge of the book. It must end standing on the edge of Part III:
% the reader should have least squares, metrics, degrees of freedom, and overfitting in hand,
% and be missing only (a) held-out data and (b) the vocabulary.
