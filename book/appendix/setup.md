# Software setup

You have two options. If you only want to read and occasionally experiment, use
Colab and skip this page. If you're doing the homework, install locally.

## Option 1: Run in the cloud (no install)

Click the 🚀 launch button at the top of any chapter and choose **Colab**. The
notebook opens in your browser with everything preinstalled.

:::{warning}
Colab does not save your work back to the book. Use **File → Save a copy in
Drive** before you start editing, or you will lose it.
:::

## Option 2: Install locally

### 1. Install Miniforge

Download and install [Miniforge](https://github.com/conda-forge/miniforge), a
minimal conda distribution. On macOS you can also use Homebrew:

```bash
brew install miniforge
```

### 2. Get the course materials

```bash
git clone https://github.com/hoon-ock/numerical-methods-ai-cheme.git
cd numerical-methods-ai-cheme
```

### 3. Create the environment

```bash
conda env create -f environment.yml
conda activate numerical-methods
pip install -e .
```

The last line installs the small `cheme_numerics` helper package that the
chapters import for consistent plotting. It's an *editable* install, so it picks
up changes without reinstalling.

### 4. Launch JupyterLab

```bash
jupyter lab
```

Open any notebook under `book/chapters/` and run the first cell. If you see a
figure, you're set.

## Verifying your install

Run this in a notebook or at a Python prompt:

```python
import numpy, scipy, matplotlib, sklearn, cantera, torch
from cheme_numerics import use_course_style

print("numpy      ", numpy.__version__)
print("scipy      ", scipy.__version__)
print("matplotlib ", matplotlib.__version__)
print("scikit-learn", sklearn.__version__)
print("cantera    ", cantera.__version__)
print("torch      ", torch.__version__)
use_course_style()
print("OK")
```

## Building the book yourself

```bash
conda activate numerical-methods
jupyter-book build book/
open book/_build/html/index.html     # on Linux: xdg-open
```

Notebook execution is cached, so only changed chapters re-run. To force a full
rebuild:

```bash
jupyter-book build --all book/
```

## Common problems

:::{dropdown} `ModuleNotFoundError: No module named 'cheme_numerics'`
You skipped `pip install -e .`, or you ran it in a different environment. Run
`conda activate numerical-methods` first, then `pip install -e .` from the
repository root.
:::

:::{dropdown} Figures don't appear, or look different from the book
Make sure the notebook's first cell calls `use_course_style()`. If figures are
missing entirely, check that you selected the `numerical-methods` kernel
(Kernel → Change Kernel) rather than a system Python.
:::

:::{dropdown} The build fails with a notebook execution error
Jupyter Book stops on the first error by default. The traceback names the
offending notebook and cell. Run that notebook interactively in JupyterLab to
debug it — the error is in the notebook, not in the build.
:::
