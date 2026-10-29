% --------------------------------------------------------------------------
% OUTLINE STUB -- headings only, no content yet.
% Lines beginning with '%' are MyST comments: visible here, absent from the build.
% Full provenance table: ~/.claude/plans/i-want-to-build-immutable-axolotl.md
% --------------------------------------------------------------------------
%
% SOURCES FOR THIS CHAPTER:
%   - CHME212 docs/chapter18/18_notebook.ipynb
%   - 06-262 notes/ordinary_differential_equations/ lectures 15, 16, 17,
%     19 (+ course-recap.ipynb)
%   - Chapra Part 7: Ch. 25 p. 707, Ch. 26 p. 752, Ch. 28 p. 808

# Ordinary Differential Equations

## Why ODEs

% CHME212 ch18 opens here.

## What is an ODE: order and standard form

% CHME212 ch18 18.1, incl. 18.1.4 verifying an analytical solution.

## Classification, and when a closed form exists

% 06-262 notes/course-recap.ipynb has an ODE classification rubric
%   (order / separability / exactness / linearity / homogeneity) and a
%   'Your Approach' decision tree -- the single most reusable artifact
%   in that repo.
% This one section COMPRESSES 06-262 lectures 8-14 (seven lectures of
%   analytical technique: separable, exact, integrating factors, second
%   order, undetermined coefficients, variation of parameters). Lectures
%   13 and 14 overlap heavily and have zero code.

## Euler's method, by hand then in code

% CHME212 ch18 18.2; 06-262 lecture 15 works y' = -y at h=1 and h=1/2 by
%   hand before writing the loop. Keep the by-hand pass -- it is what
%   makes the step-size study land.

## Runge-Kutta

% 06-262 lecture 15 writes k1..k4 explicitly and labels it O(dt^4), with
%   'Euler is very simple and not widely used in practice'; Chapra 25.3
%   p. 727. Adaptive RK is Chapra 25.5 p. 742.

## solve_ivp in practice

% CHME212 ch18 18.3: write the ODE as a function -> call -> read the
%   result -> pass parameters with args.
% 06-262 lecture 15 troubleshooting is better than CHME212's:
%   rtol=1e-3/atol=1e-6 defaults, the rescaling trap ('if your
%   concentration is on the scale of 1e-9 M you will have a problem --
%   rescale so your variables are near 1'), and the convergence self-
%   check ('if tightening the tolerances changes your solution, they
%   were not tight enough').

## Systems of ODEs

% CHME212 ch18 18.4: consecutive reactions A->B->C; controlled tank
%   level as a second-order ODE.
% 06-262 lecture 16: two tanks in series, transient -- the Ch. 11.7
%   system with accumulation turned on, solved THREE ways (collapse to
%   one second-order ODE / eigenvector solution / solve_ivp). This is
%   the section that makes Ch. 11, Ch. 12, and Ch. 15 one subject rather
%   than three.

## Stiffness

% CHME212 ch18 18.5 (fast/slow reaction network, stiff solvers) is
%   genuinely better than 06-262 here -- 06-262 only quotes the scipy
%   docs and never actually passes method=. Chapra Ch. 26 p. 752.

## Steady states and stability

% 06-262 lecture 19: fsolve for steady states, analytical Jacobian,
%   np.linalg.eig(J), and a clean 4-point rubric (all real parts
%   negative -> stable; any positive -> unstable; complex -> oscillation
%   about the steady state; purely imaginary -> stable oscillation).
%   Reuses Ch. 12 directly.

## Chemical engineering applications

% CHME212 ch18 18.6: non-isothermal batch reactor (coupled mass + energy
%   balance, Arrhenius kinetics) and CSTR start-up dynamics.
% 06-262 lecture 11: one CSTR under four feed forcing functions (none /
%   constant / exponentially decaying / oscillating), each preceded by a
%   'think first' physical prediction. Excellent reuse candidate.
% Chapra 28.1 p. 808: transient response of a reactor.

% DEFERRED, by decision: boundary-value problems and the shooting method (06-262 lectures
% 20-21), event detection, and PDEs (Chapra Part 8). 06-262's batch-reactor inverse problem
% in 21-BVP-shooting-method.ipynb is strong (2A<=>B, B->2C, find the unknown initial B and C
% from measurements at t=5 min, solve_ivp inside fsolve, plus a multi-start sweep exposing
% non-uniqueness) -- route it to an appendix rather than dropping it.
