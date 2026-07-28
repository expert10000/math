# Suggested Git Workflow

- `main` — stable, compiling book.
- `develop` — integration branch.
- `pr-book/08-1-chapter-1` — example feature branch.

Before merging:

```bash
make clean
make
python3 tools/book_state.py
git status
```

Commit the source and metadata, but not generated build artifacts.
