% --------------------------------------------------------------------------
% OUTLINE STUB -- headings only, no content yet.
% Lines beginning with '%' are MyST comments: visible here, absent from the build.
% Full provenance table: ~/.claude/plans/i-want-to-build-immutable-axolotl.md
% --------------------------------------------------------------------------
%
% SOURCES FOR THIS CHAPTER:
%   - CHME212 docs/chapter11/11_notebook.ipynb +
%     11_rank_supplement.ipynb
%   - 06-262 notes/linear_algebra/ lectures 2, 3, 4, 5 (+ 7b tail)
%   - Chapra Part 3: Ch. 9 p. 241, Ch. 10 p. 274, Ch. 12 p. 315

# Linear Systems of Equations

## Why matrices: systems of equations

% 06-262 lecture 2: stoichiometric matrix times rate vector = species
%   production rates, for 2H2+O2->2H2O and CO+H2O->H2+CO2. Sold as 'very
%   helpful for reaction engineering'.

## Vectors, matrices, and matrix arithmetic

% CHME212 ch11 11.1-11.3; 06-262 lecture 2.

## Gaussian elimination by hand

% 06-262 lecture 3 (augmented matrix -> upper triangular -> row echelon
%   -> reduced row echelon); Chapra Ch. 9 p. 241. Also 06-262's use of
%   Gauss elimination as a test for linear independence.

## Solving in NumPy: solve, inv, det

% CHME212 ch11 11.4-11.5; 06-262 lecture 4 tail (np.linalg.solve / inv /
%   det / matrix_rank, sympy rref). Teach np.linalg.solve over inv --
%   say why.

## Rank and degrees of freedom

% CHME212 ch11_rank_supplement section 6 'Why Rank Matters in Chemical
%   Engineering': material balances, DOF analysis, checking your balance
%   before solving. Renumber its 1.-7. headings to 11.x.
% 06-262 lecture 4 covers rank with under- and over-determined examples.

## Conditioning, and when solve lies to you

% ADDITION. Chapra Ch. 10 section 10.3 p. 287 (error analysis and system
%   condition). Neither reference course covers condition number --
%   06-262 claims 10^5-10^6-equation flowsheets in lecture 1 but never
%   discusses conditioning or sparsity.

## Chemical engineering applications

% CHME212 ch11 11.6: three-stream mixer-splitter; heat-exchanger-network
%   energy balance; four-component separation train as a 5x5 system.
% 06-262 lecture 4: three tanks in series at steady state -- the best-
%   constructed example in either course (full balances, every row
%   operation longhand, units check h ~ FR = m, physical-sense check,
%   answer h = (20,10,5) m). Reused transiently in Ch. 15.6.
% Chapra 12.1 p. 315: steady-state analysis of a system of reactors.

## Closing the loop: the Chapter 1 flowsheet

% Solve the 17-equation recycle system posed in 1.7. Use rank to confirm
%   the equation count -- this is the promise 06-262 lecture 1 makes and
%   never cashes out.
