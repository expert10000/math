# Notation Guide

## Purpose

This file is the repository-wide source of truth for symbols and typographic conventions.

## General rules

1. Introduce every symbol before first use.
2. Avoid unrelated meanings for the same symbol.
3. Distinguish scalars, vectors, matrices, operators, and tensors typographically.
4. Use established physics notation unless a chapter explicitly explains an exception.

## Scalars and vectors

- Scalars: italic, for example `m`, `t`, `E`.
- Vectors: bold lowercase, for example `\mathbf r`, `\mathbf v`.
- Unit vectors: hatted bold symbols, for example `\hat{\mathbf e}_x`.
- Matrices: bold uppercase where practical.
- Quantum operators: hats, for example `\hat H`, `\hat p`.

## Differential operators

- Gradient: `\nabla f`.
- Divergence: `\nabla\cdot\mathbf F`.
- Curl: `\nabla\times\mathbf F`.
- Laplacian: `\nabla^2 f`.

## Complex and quantum notation

- Imaginary unit: `i`.
- Complex conjugate: `z^*`.
- Inner product: `\langle u,v\rangle`.
- Bra-ket notation: `\langle\psi|\phi\rangle`.
- Wavefunction: `\psi`.
- State vector: `|\psi\rangle`.

## Coordinates and indices

- Cartesian: `(x,y,z)`.
- Cylindrical: `(r,\phi,z)`.
- Spherical: `(r,\theta,\phi)`.
- Spatial indices: `i,j,k`.
- Relativistic indices: `\mu,\nu`.

## Reserved symbols

- `L`: Lagrangian.
- `H`: Hamiltonian.
- `\mathbf E`: electric field.
- `\mathbf B`: magnetic field.
- `\rho`: density, with its type stated explicitly.
- `\mathbf J`: current density.

## Rule

A reader should never need to guess what a symbol means.

## Dynamical systems and differential equations

- Time derivative: `\dot{x}`; second time derivative: `\ddot{x}`.
- State vector: `\mathbf x(t)`.
- General first-order system: `\dot{\mathbf x}=\mathbf f(t,\mathbf x)`.
- Autonomous system: `\dot{\mathbf x}=\mathbf f(\mathbf x)`.
- Initial data: `\mathbf x(t_0)=\mathbf x_0`.
- Matrix flow: `e^{At}`.
- Numerical step size: `h`; reserve `\Delta t` for a physical or finite time interval when useful.
- Natural angular frequency: `\omega_0`; driving angular frequency: `\Omega`.
- State clearly whether damping is represented by `b`, `\gamma`, or a dimensionless ratio `\zeta`.
