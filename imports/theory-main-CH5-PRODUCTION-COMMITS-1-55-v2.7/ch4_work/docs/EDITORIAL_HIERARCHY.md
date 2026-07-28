# Editorial Hierarchy Standard — PR-BOOK-12

## Numbered levels

1. Part
2. Chapter
3. Section
4. Subsection

Subsubsections are unnumbered by default. A subsubsection may be restored only when it contains substantial material, normally at least half a page.

## Short concepts

Short concepts use `\booktopic{Title}` or a semantic environment:

- `definition`
- `property`
- `bookrule`
- `bookremark`
- `workedexample`
- `historicalnote`
- `physical`
- `warningbox`

## Refactoring rule

The automated pass demotes a subsection only when it contains fewer than 16 nonblank source lines and fewer than 500 normalized characters. Long derivations and substantial discussions retain numbered subsection status.
