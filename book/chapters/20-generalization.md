% --------------------------------------------------------------------------
% OUTLINE STUB -- headings only, no content yet.
% Lines beginning with '%' are MyST comments: visible here, absent from the build.
% Full provenance table: ~/.claude/plans/i-want-to-build-immutable-axolotl.md
% --------------------------------------------------------------------------
%
% SOURCES FOR THIS CHAPTER:
%   - 06-325 notes/ml_basics.ipynb (pitfalls, extrapolation, splits)
%   - 06-325 notes/train_validation.ipynb (18 cells, synthetic, no
%     downloads)

# Generalization: Train, Validation, and Test

## The problem with fitting on all your data

% 06-325 ml_basics, 'Pitfalls with fitting models using all of the
%   available data': no idea how the model works on data it has not
%   seen; no idea whether it extrapolates; and 'we can perfectly fit
%   most data by just throwing more polynomial features and fitted
%   parameters at the problem'.

## Extrapolation failure, demonstrated

% 06-325 ml_basics: the fit is reasonable inside the data range and
%   absurd outside it. Then the pivot: 'We want models that can predict
%   things that we haven't seen before, so we need to change our way of
%   evaluating the models.'

## Train, validation, and test

% 06-325's three-way glossary, worth keeping close to verbatim: TRAIN =
%   data shown to the model during fitting; VALIDATION = data used to
%   decide which model to use or how to adjust the fitting procedure;
%   TEST = data set aside and looked at as infrequently as possible,
%   standing in for the real task.
% Mechanics: 80/10/10, sklearn.model_selection.train_test_split.

## The split is an engineering decision

% 06-325's strongest pedagogical idea. Splitting randomly defines the
%   task as 'fill in missing points'. Splitting on time without
%   shuffling defines it as 'predict the future'. Same data, same model,
%   different task -- and the second is usually the one you actually
%   care about.
% Its worked version: fit on 1840-1985, choose the model on 1985-2003,
%   test on 2003-2022. Re-cast this for whatever ChemE dataset Ch. 19
%   settles on.

## Why three splits and not two

% 06-325 train_validation.ipynb, told as a deliberate self-deception: 20
%   numbers drawn from a Gaussian used as BOTH features and target, so
%   no model should work. Feature selection against the validation set
%   'achieves' an error of 0.21; the test set then destroys it. 'This is
%   VERY different; what happened here? Which of these numbers do you
%   trust more?'
% Cheap to reproduce -- 18 cells, synthetic, no downloads. Slot it after
%   the ChemE-flavored introduction above.
