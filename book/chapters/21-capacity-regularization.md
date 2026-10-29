% --------------------------------------------------------------------------
% OUTLINE STUB -- headings only, no content yet.
% Lines beginning with '%' are MyST comments: visible here, absent from the build.
% Full provenance table: ~/.claude/plans/i-want-to-build-immutable-axolotl.md
% --------------------------------------------------------------------------
%
% SOURCES FOR THIS CHAPTER:
%   - 06-325 notes/overfitting_regularization.ipynb (77 cells, the
%     largest ML notebook)

# Model Capacity, Overfitting, and Regularization

## Model capacity

% 06-325 states the problem form first: supervised regression y-hat =
%   f(X), where X is 2-D (one row per data point, one column per
%   feature).
% Capacity is varied by polynomial feature expansion: sklearn
%   PolynomialFeatures + StandardScaler + make_pipeline.

## Under- and overfitting

% 06-325 generates 60 noisy samples from Himmelblau's function (the SAME
%   function optimized in Ch. 18.5) with a 60/20/20 split.

## The generalization gap

% 06-325's definition: the gap between training and validation
%   performance, showing how well the model generalizes. Canonical shape
%   -- the validation curve sits above the training curve; training
%   error decreases monotonically with capacity; validation error passes
%   through a minimum (at polynomial order 4 in their example),
%   flattens, then shoots up.

## L2 regularization: ridge

% 06-325's framing is the one to keep: regularization changes THE
%   FITTING PROCEDURE, NOT THE MODEL. 'We're not going to change the
%   model at all - we're only going to change the fitting procedure.'
%   Add a penalty on parameter size: min [ sum (y - y_hat)^2 + alpha *
%   sum theta_j^2 ].
% Keep its warning: large alpha effectively reduces model capacity, and
%   too large will hurt the training error too.
% Also its naming note: L2 = Tikhonov = ridge.

## L1 regularization: LASSO and feature selection

% 06-325 same notebook: Lasso, plus sklearn.feature_selection.RFE. Also
%   its recovery check -- after fitting 4th-order polynomial features,
%   compare get_feature_names_out() against the known true coefficients.

## Where this goes next

% POINTER ONLY, no content. 06-325 continues for five more lectures:
%   classification and logistic regression; non-parametric models;
%   featurizing molecules and materials; neural networks; dimensionality
%   reduction and unsupervised learning; Bayesian optimization / active
%   learning for design of experiments. Out of scope for this phase by
%   decision -- Part III stops at the bridge.
