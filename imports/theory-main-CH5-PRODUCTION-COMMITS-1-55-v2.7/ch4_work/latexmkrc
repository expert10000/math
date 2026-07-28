$pdf_mode = 1;
$interaction = 'nonstopmode';
$halt_on_error = 1;
$out_dir = 'build';
$aux_dir = 'build';
$bibtex_use = 2;
$bibtex = 'bibtex %O %B';
$makeindex = 'makeindex %O -o %D %S';
$clean_ext .= ' acr acn alg glg glo gls glsdefs ist xdy';

# Build glossaries inside the configured output directory.
add_cus_dep('glo', 'gls', 0, 'run_makeglossaries');
add_cus_dep('acn', 'acr', 0, 'run_makeglossaries');
sub run_makeglossaries {
  my ($base) = @_;
  $base =~ s!.*/!!;
  return system("makeglossaries -d $out_dir $base");
}
