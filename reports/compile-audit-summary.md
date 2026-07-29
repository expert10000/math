# Compile-Ready Audit Summary

## Compile-ready folder

- Folder: `imports/COMPILE_READY`
- Top-level document TeX files: 237
- Files under `figures/`: 1983
- Image assets under `figures/`: 1483
- Figure/TikZ TeX files under `figures/`: 500
- Rewritten LaTeX references: 696
- Unresolved references: 4

## Compile results

- Standalone documents: 197 tested, 180 success, 16 fail, 1 timeout
- Top-level fragments: 40 wrapper-tested, 32 success, 8 fail, 0 timeout
- Figure TeX snippets: 500 wrapper-tested, 213 success, 287 fail, 0 timeout
- Final listed PDFs: 426

## Lists

- `reports/compile-audit-results.tsv`: standalone document results
- `reports/fragment-wrapper-results.tsv`: top-level fragment wrapper results
- `reports/figure-tex-results.tsv`: figure TeX wrapper results
- `reports/compiled-pdfs.txt`: final PDF list from successful/usable audit outputs
- `imports/COMPILE_READY/MISSING_REFERENCES.tsv`: unresolved references
- `imports/COMPILE_READY/REWRITES.tsv`: all path rewrites

## Unresolved references

- `Downloads_Exercise_1_2_append.tex`: `includegraphics{f_and_psi.png}`
- `Downloads_Exercise_1_2_append.tex`: `includegraphics{residual_check.png}`
- `MATH-ALLS-2_Exercise_1_2_append.tex`: `includegraphics{f_and_psi.png}`
- `MATH-ALLS-2_Exercise_1_2_append.tex`: `includegraphics{residual_check.png}`

## Standalone failures

- `Downloads_diagrams_01-13_tikz.tex` [fail]: Downloads_diagrams_01-13_tikz.tex:96: Package pgfkeys Error: I do not know the
- `Downloads_merged_exercises.tex` [fail]: Downloads_merged_exercises.tex:17: Package enumitem Error: a) undefined.
- `Downloads_merged_exercises_1_.tex` [fail]: Downloads_merged_exercises_1_.tex:48: Package enumitem Error: a) undefined.
- `Downloads_merged_exercises_corrected.tex` [fail]: Downloads_merged_exercises_corrected.tex:213: Extra }, or forgotten $.
- `Downloads_merged_exercises_FULL_v2.tex` [fail]: Downloads_merged_exercises_FULL_v2.tex:223: Extra }, or forgotten $.
- `Downloads_theory-of-complex-analysis-gamma.tex` [fail]: Downloads_theory-of-complex-analysis-gamma.tex:1735: Undefined control sequence
- `Downloads_theory-of-geometry-2.tex` [fail]: Downloads_theory-of-geometry-2.tex:2547: LaTeX Error: Command \k unavailable in
- `Downloads_theory-of-geometry-IV.tex` [fail]: Downloads_theory-of-geometry-IV.tex:2170: Improper \spacefactor.
- `MATH_ALLS-3_diagrams_01-13_tikz.tex` [fail]: MATH_ALLS-3_diagrams_01-13_tikz.tex:96: Package pgfkeys Error: I do not know th
- `MATH-ALLS-2_merged_exercises.tex` [fail]: MATH-ALLS-2_merged_exercises.tex:17: Package enumitem Error: a) undefined.
- `MATH-ALLS-2_merged_exercises_1_.tex` [fail]: MATH-ALLS-2_merged_exercises_1_.tex:48: Package enumitem Error: a) undefined.
- `MATH-ALLS-2_merged_exercises_corrected.tex` [fail]: MATH-ALLS-2_merged_exercises_corrected.tex:213: Extra }, or forgotten $.
- `MATH-ALLS-2_merged_exercises_FULL_v2.tex` [fail]: MATH-ALLS-2_merged_exercises_FULL_v2.tex:223: Extra }, or forgotten $.
- `MATH-ALLS-2_theory-of-complex-analysis-gamma.tex` [fail]: MATH-ALLS-2_theory-of-complex-analysis-gamma.tex:1735: Undefined control sequen
- `MATH-ALLS-2_theory-of-geometry-2.tex` [fail]: MATH-ALLS-2_theory-of-geometry-2.tex:2547: LaTeX Error: Command \k unavailable
- `MATH-ALLS-2_theory-of-geometry-IV.tex` [fail]: MATH-ALLS-2_theory-of-geometry-IV.tex:2170: Improper \spacefactor.
- `MATH-ALLS-2_theory-of-real-analysis.tex` [timeout]: 

## Fragment failures

- `Downloads_Exercise_1_2_append.tex` [fail]: _1_2_append.tex:83: Package pdftex.def Error: File `f_and_psi.png' not found: u
- `Downloads_merged_exercises_2_.tex` [fail]: xercises_2_.tex:24: Extra }, or forgotten $.
- `Downloads_merged_exercises_3_.tex` [fail]: xercises_3_.tex:25: Extra }, or forgotten $.
- `Downloads_vector_bundle_diagrams_snippet_1_.tex` [fail]: undle_diagrams_snippet_1_.tex:23: Undefined control sequence.
- `Downloads_vector_bundle_diagrams_snippet.tex` [fail]: undle_diagrams_snippet.tex:23: Undefined control sequence.
- `MATH-ALLS-2_Exercise_1_2_append.tex` [fail]: se_1_2_append.tex:83: Package pdftex.def Error: File `f_and_psi.png' not found:
- `MATH-ALLS-2_merged_exercises_2_.tex` [fail]: _exercises_2_.tex:24: Extra }, or forgotten $.
- `MATH-ALLS-2_merged_exercises_3_.tex` [fail]: _exercises_3_.tex:25: Extra }, or forgotten $.

## Figure TeX failures

The full list is in `reports/figure-tex-results.tsv`; first failures are shown here.

- `Downloads_theory_figures_ch01_basis_vectors.tex` [fail]: theory_figures_ch01_basis_vectors.tex:2: Undefined control sequence.
- `Downloads_theory_figures_ch01_cartesian_position_vector.tex` [fail]: theory_figures_ch01_cartesian_position_vector.tex:4: Package pgfkeys Error: I d
- `Downloads_theory_figures_ch01_change_of_basis.tex` [fail]: theory_figures_ch01_change_of_basis.tex:3: Package pgfkeys Error: I do not know
- `Downloads_theory_figures_ch01_coordinate_rotation.tex` [fail]: theory_figures_ch01_coordinate_rotation.tex:2: Package pgfkeys Error: I do not
- `Downloads_theory_figures_ch01_distance_between_points.tex` [fail]: theory_figures_ch01_distance_between_points.tex:2: Undefined control sequence.
- `Downloads_theory_figures_ch01_function_vector_space.tex` [fail]: theory_figures_ch01_function_vector_space.tex:2: Package pgfkeys Error: I do no
- `Downloads_theory_figures_ch01_hilbert_space_bridge.tex` [fail]: theory_figures_ch01_hilbert_space_bridge.tex:2: Package xcolor Error: Undefined
- `Downloads_theory_figures_ch01_parallelogram_area.tex` [fail]: theory_figures_ch01_parallelogram_area.tex:3: Package pgfkeys Error: I do not k
- `Downloads_theory_figures_ch01_scalar_multiplication.tex` [fail]: theory_figures_ch01_scalar_multiplication.tex:3: Package pgfkeys Error: I do no
- `Downloads_theory_figures_ch01_span_plane.tex` [fail]: theory_figures_ch01_span_plane.tex:2: Package pgfkeys Error: I do not know the
- `Downloads_theory_figures_ch01_torque_lever_arm.tex` [fail]: theory_figures_ch01_torque_lever_arm.tex:2: Package pgfkeys Error: I do not kno
- `Downloads_theory_figures_ch01_unit_vector_geometry.tex` [fail]: theory_figures_ch01_unit_vector_geometry.tex:2: Undefined control sequence.
- `Downloads_theory_figures_ch01_vector_addition_head_to_tail.tex` [fail]: theory_figures_ch01_vector_addition_head_to_tail.tex:5: Package pgfkeys Error:
- `Downloads_theory_figures_ch01_vector_components.tex` [fail]: theory_figures_ch01_vector_components.tex:2: Package pgfkeys Error: I do not kn
- `Downloads_theory_figures_ch01_vector_subtraction.tex` [fail]: theory_figures_ch01_vector_subtraction.tex:3: Package pgfkeys Error: I do not k
- `Downloads_theory_figures_ch01_work_interpretation.tex` [fail]: theory_figures_ch01_work_interpretation.tex:2: Package pgfkeys Error: I do not
- `Downloads_theory_figures_ch02_chain_rule_graph.tex` [fail]: theory_figures_ch02_chain_rule_graph.tex:2: Package pgfkeys Error: I do not kno
- `Downloads_theory_figures_ch02_directional_derivative_geometry.tex` [fail]: theory_figures_ch02_directional_derivative_geometry.tex:6: Package pgfkeys Erro
- `Downloads_theory_figures_ch02_epsilon_delta_limit.tex` [fail]: theory_figures_ch02_epsilon_delta_limit.tex:2: Package pgfkeys Error: I do not
- `Downloads_theory_figures_ch02_function_mapping.tex` [fail]: theory_figures_ch02_function_mapping.tex:2: Package pgfkeys Error: I do not kno
- `Downloads_theory_figures_ch02_gradient_flow.tex` [fail]: theory_figures_ch02_gradient_flow.tex:2: Package xcolor Error: Undefined color
- `Downloads_theory_figures_ch02_jacobian_area.tex` [fail]: theory_figures_ch02_jacobian_area.tex:3: Package pgfkeys Error: I do not know t
- `Downloads_theory_figures_ch02_local_linearization.tex` [fail]: theory_figures_ch02_local_linearization.tex:2: Package pgfkeys Error: I do not
- `Downloads_theory_figures_ch02_total_differential_plane.tex` [fail]: theory_figures_ch02_total_differential_plane.tex:3: Package xcolor Error: Undef
- `Downloads_theory_figures_ch03_divergence_source_sink.tex` [fail]: theory_figures_ch03_divergence_source_sink.tex:15: Package pgfkeys Error: I do
