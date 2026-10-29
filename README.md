# Numerical Methods and AI Modeling for Chemical Engineers

Course materials for a junior/senior undergraduate chemical engineering course,
authored as a [Jupyter Book](https://jupyterbook.org). Every chapter is an
executable notebook.

## Status

**Scaffold.** The toolchain, styling, build, and deploy pipeline work end to end.
The chapter outline is still to be written — see `_refs/README.md`.

## Quick start

```bash
conda env create -f environment.yml
conda activate numerical-methods
pip install -e .                 # installs the cheme_numerics helper package

jupyter-book build book/
open book/_build/html/index.html
```

Notebook execution is cached; only changed chapters re-run. Force a full
rebuild with `jupyter-book build --all book/`.

## Layout

| Path | Purpose |
|---|---|
| `book/_config.yml` | Jupyter Book configuration |
| `book/_toc.yml` | Table of contents — **placeholder**, to be rewritten |
| `book/intro.md` | Landing page |
| `book/chapters/` | Chapter notebooks |
| `book/appendix/` | Setup instructions, bibliography |
| `book/references.bib` | BibTeX; cite with `` {cite}`key` `` |
| `cheme_numerics/` | Shared helpers — plotting style, utilities |
| `_refs/` | Source/reference material (**gitignored**) |
| `.github/workflows/deploy.yml` | Build + publish to GitHub Pages |

## Authoring conventions

- **Never set Matplotlib styles in a notebook.** Call `use_course_style()` in the
  first cell and change `cheme_numerics/plotting.py` if something needs adjusting.
  This keeps every figure in the book consistent.
- **Hard-code no colors.** Use the default property cycle, or `COLORS` from
  `cheme_numerics` when you need a specific one.
- Cite with `` {cite}`key` ``; add entries to `book/references.bib`.
- Name chapter files `NN-slug.ipynb` so the filesystem order matches the TOC.
- A file named `*-solutions.ipynb` is excluded from execution (see
  `execute.exclude_patterns`) — but note it is still *published* if listed in the
  TOC. Keep solutions out of `_toc.yml`.

## Publishing

The repository is currently **private**, so GitHub Pages is not available (it
requires a paid plan for private repos). CI still builds the book on every push
to `main`; the deploy job skips itself until the repo is public.

To publish, make the repo public and enable Pages once:

```bash
gh api -X POST repos/hoon-ock/numerical-methods-ai-cheme/pages -f 'build_type=workflow'
```

The book then appears at <https://hoon-ock.github.io/numerical-methods-ai-cheme/>.
