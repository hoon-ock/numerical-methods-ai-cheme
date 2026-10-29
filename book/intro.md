# Numerical Methods and AI Modeling for Chemical Engineers

Chemical engineering problems rarely have closed-form answers. A distillation
column at steady state is a large nonlinear algebraic system. A batch reactor is
a stiff initial-value problem. Fitting a rate law to lab data is a constrained
optimization. Predicting a catalyst's activity from its composition is a
regression problem over a space too large to enumerate.

This book has two aims, and they are inseparable:

1. **The methods** — the numerical techniques that have underpinned process
   simulation for fifty years, and the data-driven methods now used alongside them.
2. **The practice** — how to actually carry them out, in Python, on problems that
   look like the ones you will meet.

The emphasis throughout is on *using* these methods correctly: knowing when a
method will fail, how its error behaves, and how to recognize a wrong answer that
looks plausible.

## Who this is for

Junior and senior undergraduates in chemical engineering. You should have had:

- single- and multivariable calculus, and ordinary differential equations
- linear algebra (matrices, eigenvalues) — a refresher is included
- an introductory programming course; Python specifically is **not** assumed, and
  Part I brings you up to speed from the beginning

Mass and energy balances, thermodynamics, and reaction engineering appear
constantly as the *source* of the problems we solve. You don't need to have
finished those courses, but having seen a mole balance will make the examples
land.

## How the book is organized

**{doc}`Chapter 1 <chapters/01-numerical-methods-in-cheme>`** sets up the whole
subject: what a numerical method is, where chemical engineering equations come
from, what you trade away when you stop solving by hand, and how error behaves.

**Part I — Python for Chemical Engineers** starts from nothing: the language, its
data structures, control flow, files, functions, and scientific figures. If you
already write Python comfortably, skim it and move on.

**Part II — Numerical Methods** is the core: arrays and vectorization, linear
systems, eigenvalues, roots of equations, differentiation and integration,
ordinary differential equations, statistics, curve fitting, and optimization.
Each chapter ends on a chemical engineering problem — a reactor network, a PFR
sizing calculation, a van der Waals molar volume, a non-isothermal batch reactor.

**Part III — From Curve Fitting to Machine Learning** is the payoff, and it is
deliberately continuous with Part II rather than a fresh start. Fitting a
polynomial by least squares and training a machine-learning model are the *same
operation*: minimize an error between a model and data. What separates them is
not the mathematics but the protocol — holding data back, and asking whether the
model works on cases it has never seen. We build the bridge in that order:
vocabulary first, on a fit you have already done; then held-out data; then model
capacity and regularization.

**Part IV — Lab Exercises** holds the longer problems, one lab per topic.

## How to use this book

Every chapter is an executable Jupyter notebook. You can:

- **Read it as a web page** — all code and output is already rendered.
- **Run it in the cloud** — use the launch button (🚀) at the top of any chapter
  to open it in Google Colab. Nothing to install.
- **Run it locally** — see {doc}`appendix/setup`. Recommended if you'll be doing
  the labs, since local runs are faster and keep your work.

Code in this book is meant to be read, modified, and broken. The exercises and
labs are where the learning actually happens; the worked examples in the body are
there to give you something to modify.

:::{admonition} A note on libraries
:class: tip

We implement the core algorithms from scratch first — Newton's method, Euler and
Runge–Kutta, Gaussian elimination, the normal equations — because you cannot
diagnose a solver you have never taken apart. We then switch to the production
implementations in SciPy {cite}`virtanen2020scipy` for everything afterward.
Writing your own solver is a learning exercise, not engineering practice.

The same applies in Part III. Before `sklearn.LinearRegression().fit()` appears,
you will have solved the identical problem two other ways and confirmed that all
three give the same coefficients.
:::

## Software

Python, with NumPy and SciPy for numerics, Matplotlib for plotting, SymPy for
symbolic work, scikit-learn for the machine-learning chapters, and Cantera for
thermodynamic and kinetic properties. All of it is free and open source.

## Sources

This course is built on four references, and says where it draws from each:

- Chapra and Canale, *Numerical Methods for Engineers*, 6th ed.
  {cite}`chapra2010numerical` — the classical methods and their error analysis.
- Fogler, *Elements of Chemical Reaction Engineering* {cite}`fogler2020elements`
  — the source of several reactor problems.
- Kreyszig, *Advanced Engineering Mathematics* {cite}`kreyszig2011advanced` — the
  analytical ODE background that Chapter 15 compresses.
- Open-access course material from Carnegie Mellon (06-262 *Math Methods in
  Chemical Engineering* and 06-325 *Numerical Methods and ML for ChE*) and from
  the predecessor course, *Introduction to Chemical Engineering Computation*.
