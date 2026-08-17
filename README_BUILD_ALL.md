# Canonical build-all helper

Place `BUILD_ALL.ps1` and `BUILD_ALL.bat` in the repository root.

The script discovers the canonical volumes dynamically from:

    books/vol*/

For each volume it compiles `book.tex`. By default it also compiles any root-level:

    part*_student.tex
    part*_hints.tex
    part*_complete.tex

This means Volume VI Part I student/study/complete editions are included automatically when
those wrappers exist, while future volume/part editions will also be picked up without
editing the script.

## Normal build

From the repository root:

    .\BUILD_ALL.bat

or:

    powershell -ExecutionPolicy Bypass -File .\BUILD_ALL.ps1

## Canonical volume books only

    .\BUILD_ALL.bat -CanonicalOnly

## Clean first

    .\BUILD_ALL.bat -CleanFirst

## Stop on first error

    .\BUILD_ALL.bat -FailFast

## Do not gather PDFs

    .\BUILD_ALL.bat -NoPdfCollection

By default, successful PDFs are copied to:

    build\pdf\

with names such as:

    vol06_algebraic_geometry_book.pdf
    vol06_algebraic_geometry_part1_student.pdf
    vol06_algebraic_geometry_part1_hints.pdf
    vol06_algebraic_geometry_part1_complete.pdf

The original PDFs remain in their volume directories as produced by latexmk.

No Git operations are performed.
