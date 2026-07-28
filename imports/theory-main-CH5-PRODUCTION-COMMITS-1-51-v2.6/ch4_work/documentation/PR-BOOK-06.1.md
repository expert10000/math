# PR-BOOK-06.1 — Chapter 1 Master Structure

## Purpose

This release defines the authoritative master structure, scale, content targets,
and staged implementation plan for Chapter 1, **Vectors and Coordinate
Systems**. It does not claim that all target prose, examples, historical notes,
programming companions, or exercises have already been written. It establishes
the specification against which PR-BOOK-06.2 through PR-BOOK-06.6 will be
implemented and reviewed.

## Target size and content

- **Length:** 80–100 pages
- **Illustrations:** 25 (already complete)
- **Worked examples:** 40–60
- **Exercises:** 150–250
- **Historical notes:** 20–30
- **Programming examples:** 15–20

---

## Chapter 1 layout

### Part I — Foundations (approximately 20 pages)

#### 1.1 What Is Mathematics in Physics?

Topics:

- Why mathematics is the language of physics
- Scalars versus vectors
- Physical quantities
- SI units
- Measurement
- Dimension

Learning objectives:

- Understand why vectors are needed.
- Distinguish scalar and vector quantities.
- Recognize physical examples.

#### 1.2 Scalars and Vectors

Topics:

- Definition
- Examples
- Magnitude
- Direction
- Equality
- Free versus bound vectors

Figures:

- Scalar illustration
- Vector illustration
- Position vector

Worked examples:

- Force
- Velocity
- Displacement

Exercises:

- 10–15

#### 1.3 Coordinate Systems

Topics:

- Cartesian coordinates
- Polar coordinates
- Cylindrical coordinates
- Spherical coordinates

Figures:

- Already completed in the Chapter 1 illustration library

New material:

- When each coordinate system is useful
- Symmetry considerations

Applications:

- Planets
- Pipes
- Atoms

---

### Part II — Vector Algebra (approximately 35 pages)

#### 2.1 Vector Addition

Include:

- Triangle rule
- Parallelogram rule
- Polygon rule
- Negative vectors
- Zero vector

Applications:

- Forces
- Navigation
- Velocity addition

#### 2.2 Scalar Multiplication

Topics:

- Stretching
- Shrinking
- Reversing direction
- Normalization

#### 2.3 Components

Topics:

- Projections
- Decomposition
- Basis vectors
- Orthogonal basis
- Orthonormal basis

Applications:

- Inclined plane
- Aircraft navigation

#### 2.4 Dot Product

Target length: approximately 10 pages.

Suggested structure:

- Motivation
- Definition
- Geometry
- Projection
- Coordinate formula
- Physical interpretation
- Engineering examples
- Worked examples
- Common mistakes
- Exercises

#### 2.5 Cross Product

Target length: approximately 10 pages.

Topics:

- Orientation
- Right-hand rule
- Area
- Normal vectors
- Torque
- Angular momentum
- Lorentz force
- Magnetic fields

Later chapters will reuse this material extensively.

#### 2.6 Triple Products

Topics:

- Scalar triple product
- Vector triple product
- BAC–CAB identity
- Determinant interpretation
- Volume

---

### Part III — Transformations (approximately 15 pages)

Topics:

- Rotation
- Reflection
- Translation
- Change of basis
- Coordinate transformation

Figures:

- Already produced

Applications:

- Robotics
- Computer graphics
- Spacecraft attitude
- Quantum-state rotations as a preview

---

### Part IV — Vector Fields (approximately 10 pages)

Topics:

- Definition
- Visualization
- Examples

Applications:

- Gravity
- Electric field
- Magnetic field
- Fluid velocity

This material prepares the reader for Maxwell's equations and field theory.

---

### Part V — Physics Applications (approximately 15 pages)

One section per application area.

#### Mechanics

- Position
- Velocity
- Acceleration
- Force

#### Electromagnetism

- Electric field
- Magnetic field
- Lorentz force

#### Relativity

- Four-vectors as a preview

#### Quantum Mechanics

- State vectors as a conceptual preview
- Hilbert space introduced later

---

## Historical notes

Include concise profiles and context explaining contributions such as:

- Euclid — geometric foundations
- René Descartes — analytic geometry
- Isaac Newton — vectors in mechanics
- Hermann Grassmann — abstract vector algebra
- William Rowan Hamilton — quaternions
- Josiah Willard Gibbs — modern vector notation

Target: 20–30 historical notes distributed naturally through the chapter.

---

## Programming companion

For each major topic, include implementations in:

- Python with NumPy
- MATLAB / Octave
- Julia
- C++ with Eigen

The programs should reproduce the mathematical operations introduced in the
text rather than introduce unrelated software abstractions.

Target: 15–20 programming examples.

---

## End-of-chapter material

Conclude with:

- Concept map connecting all vector concepts
- Notation table and units
- Formula sheet with key identities
- Summary of common mistakes
- Glossary of terms
- Approximately 150–250 exercises divided into:
  - Basic calculations
  - Intermediate problems
  - Proofs
  - Programming tasks
  - Challenge problems
- A **Looking Ahead** section showing how vectors lead naturally into motion,
  the subject of Chapter 2

---

## Recommended implementation releases

### PR-BOOK-06.2 — Foundations

- Sections 1.1–1.3
- What Is Mathematics in Physics?
- Scalars and Vectors
- Coordinate Systems

### PR-BOOK-06.3 — Basic Vector Algebra

- Sections 2.1–2.3
- Vector Addition
- Scalar Multiplication
- Components

### PR-BOOK-06.4 — Vector Products

- Sections 2.4–2.6
- Dot Product
- Cross Product
- Triple Products

### PR-BOOK-06.5 — Transformations and Vector Fields

- Part III — Transformations
- Part IV — Vector Fields

### PR-BOOK-06.6 — Applications and Chapter Completion

- Physics Applications
- Historical Notes
- Programming Companion
- End-of-Chapter Material

This incremental plan keeps every release coherent, reviewable, testable, and
easy to integrate into the growing textbook.

---

## Integration status

- [x] Master structure recorded in the project
- [x] Existing 25-figure Chapter 1 library retained
- [x] PR-BOOK-06.2 through PR-BOOK-06.6 staged in the roadmap
- [ ] Full prose target reached
- [ ] 40–60 worked examples complete
- [ ] 150–250 exercises complete
- [ ] 20–30 historical notes complete
- [ ] 15–20 programming examples complete
- [ ] Final 80–100-page Chapter 1 build verified
