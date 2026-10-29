% --------------------------------------------------------------------------
% OUTLINE STUB -- headings only, no content yet.
% Lines beginning with '%' are MyST comments: visible here, absent from the build.
% Full provenance table: ~/.claude/plans/i-want-to-build-immutable-axolotl.md
% --------------------------------------------------------------------------
%
% SOURCES FOR THIS CHAPTER:
%   - 06-325 notes/ml_basics.ipynb
%   - 06-325 notes/overfitting_regularization.ipynb (the three-way
%     equivalence)
%   - NOTE: 06-325's notes/intro_ml.md and notes/extrapolation.md are
%     one-line title-only stubs -- there is no prose to copy, and
%     extrapolation.md is orphaned from its TOC

# From Curve Fitting to Machine Learning

## What tasks is this for?

% 06-325 ml_basics opens from engineering tasks, not algorithms: insight
%   into complex datasets, property prediction, pattern finding,
%   deciding where to add experiments, process control. Then: 'we are
%   limited in how well we can solve these problems by our understanding
%   of the underlying science or our ability to solve/model complex
%   systems'.
% KEEP its honest tip: 'If you have a physical model (based on mol/mass
%   balances, kinetics, engineering principles) that describes your data
%   sufficiently well and accomplishes your goals, stick with it!'

## The same fit, new vocabulary

% THE SINGLE MOST IMPORTANT THING TO COPY. 06-325 fits a CONSTANT model
%   first, using lmfit -- the same tool from the previous lecture -- and
%   relabels what the reader already knows: y becomes the target or
%   label; x becomes the feature matrix X (rows = data points, columns =
%   features); the data used to fit becomes training data, X_train and
%   y_train.
% No new mathematics is introduced at the moment the words 'machine
%   learning' appear. Only the names change.

## Linear regression is the simplest machine-learning model

% 06-325: 'polynomial models are linear in the fitted parameters... We
%   could fit this model using linear regression if we wanted.' Its
%   overfitting lecture adds: 'We're only going to use linear regression
%   models in today's lecture.'

## Three routes to the same coefficients

% 06-325 overfitting_regularization demonstrates NUMERICALLY that
%   scipy.optimize.minimize on an explicit SSE loss == (X^T X)^-1 X^T y
%   == sklearn.LinearRegression().fit(), confirming 'These coefficients
%   are exactly the same as the custom model we optimized' and 'Same
%   coefficients either way!'.
% This demystifies .fit() as the optimization from Ch. 18 applied to the
%   linear algebra from Ch. 11. Reproduce this cell sequence.

## Evaluating a model: metrics and parity plots

% 06-325 ml_basics: MAE, RMSE, parity plots. Metrics already defined in
%   Ch. 17.5 -- reuse, do not redefine.
% Keep its diagnostic tip: a flat (horizontal) parity plot usually means
%   the inputs have no relationship to the outputs, so the best the
%   model can do is predict the average; one common cause is inputs
%   shuffled relative to targets.

## The dataset

% SUBSTITUTE a ChemE dataset for 06-325's Berkeley Earth northern-
%   hemisphere temperature series (which it wget-s at build time -- a
%   network dependency we do not want).
% CHME212 ch12's NIST CO2 Cp(T) has the same pedagogical shape: 1-D
%   input, polynomial degree sweep, visible overfitting. It is ChemE-
%   native and already vendored. CHME212 lab07's viscosity data is a
%   second option.
% Using the Ch. 17 dataset again is a feature, not a shortcut -- it is
%   what makes 'this is the same fit' concrete.
