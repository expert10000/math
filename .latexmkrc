# Canonical latexmk defaults for the Theory of Mathematics series.
# BUILD_ALL.ps1 loads this file explicitly so every volume uses the same
# engine mode, convergence limit, recorder output, and noninteractive policy.
$pdf_mode = 1;
$max_repeat = 5;
$recorder = 1;
$halt_on_error = 1;
$interaction = 'nonstopmode';
