# pH Calculator and Buffer Solution Analyzer

A comprehensive Python tool for calculating pH values of various chemical solutions and designing buffer solutions. This tool demonstrates the chemistry and numerical computation power of Python.

## Features

- **Strong Acid/Base pH Calculations**: Calculate pH for strong acids and bases given their molar concentrations
- **Weak Acid/Base pH Calculations**: Calculate pH for weak acids and bases using dissociation constants (Ka/Kb)
- **Henderson-Hasselbalch Equation**: Calculate pH of buffer solutions with weak acid/conjugate base pairs
- **Buffer Solution Design**: Determine the exact concentrations needed to create buffer solutions with specific target pH values
- **Constant Conversions**: Convert between Ka, pKa, Kb, and pKb values
- **Common Compounds Database**: Built-in database of common acids and bases with their constants
- **Interactive CLI**: User-friendly command-line interface for all calculations

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only Python standard library)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/GIL794/pH-Calculator-and-Buffer-Solution-Analyzer.git
cd pH-Calculator-and-Buffer-Solution-Analyzer
```

2. No additional installation required! The tool uses only Python's standard library.

## Usage

### Command-Line Interface

Run the interactive CLI:
```bash
python ph_calculator_cli.py
```

The CLI provides a menu-driven interface for:
1. Calculating pH of strong acids
2. Calculating pH of strong bases
3. Calculating pH of weak acids
4. Calculating pH of weak bases
5. Calculating pH of buffer solutions (Henderson-Hasselbalch)
6. Designing buffer solutions for target pH values
7. Viewing common acids and bases
8. Converting between Ka and pKa values

### Interface Preview

**Main Menu:**
```
======================================================================
              pH Calculator and Buffer Solution Analyzer              
======================================================================

Welcome to the pH Calculator and Buffer Solution Analyzer!
This tool helps you calculate pH values and design buffer solutions.

Main Menu:
1. Calculate pH of Strong Acid
2. Calculate pH of Strong Base
3. Calculate pH of Weak Acid
4. Calculate pH of Weak Base
5. Calculate pH of Buffer Solution (Henderson-Hasselbalch)
6. Design Buffer Solution (Calculate Concentrations for Target pH)
7. View Common Acids and Bases
8. Convert between Ka and pKa
9. Exit

Enter your choice (1-9):
```

**Example: Strong Acid pH Calculation**
```
--- Strong Acid pH Calculation ---
Enter the concentration of the strong acid (M): 0.1

Result:
  Concentration: 0.1 M
  pH: 1.00
```

**Example: Buffer Solution Design**
```
--- Buffer Solution Preparation ---
Calculate concentrations needed to achieve a target pH

Use a common acid? (y/n): y

Common Acids:
  1. Acetic Acid (CH3COOH) (pKa = 4.76)
  2. Formic Acid (HCOOH) (pKa = 3.75)
  3. Benzoic Acid (C6H5COOH) (pKa = 4.2)
  4. Carbonic Acid (H2CO3) (pKa = 6.35)
  5. Phosphoric Acid (H3PO4) (pKa = 2.15)
  6. Citric Acid (pKa = 3.13)

Select an acid (number): 1
Selected: Acetic Acid (CH3COOH)
Enter the target pH: 5.0
Enter the total volume (L): 1.0
Enter the total buffer concentration (M): 0.2

Buffer Preparation Recipe:
  Target pH: 5.0
  pKa: 4.76
  Total Volume: 1.0 L
  Total Concentration: 0.2 M

  Required Concentrations:
    Weak Acid [HA]: 0.0731 M
    Conjugate Base [A-]: 0.1269 M

  Required Amounts:
    Weak Acid: 0.0731 moles
    Conjugate Base: 0.1269 moles

  Ratio [A-]/[HA]: 1.7378

  Good choice! This buffer will have good capacity at pH 5.0.
```

**Example: Viewing Common Acids and Bases**
```
--- Common Acids and Bases ---

Common Acids:
  Acetic Acid (CH3COOH)
    pKa = 4.76, Ka = 1.74e-05
  Formic Acid (HCOOH)
    pKa = 3.75, Ka = 1.78e-04
  Benzoic Acid (C6H5COOH)
    pKa = 4.20, Ka = 6.31e-05
  Carbonic Acid (H2CO3)
    pKa = 6.35, Ka = 4.47e-07
  Phosphoric Acid (H3PO4)
    pKa = 2.15, Ka = 7.08e-03
  Citric Acid
    pKa = 3.13, Ka = 7.41e-04

Common Bases:
  Ammonia (NH3)
    pKb = 4.75, Kb = 1.78e-05
  Methylamine (CH3NH2)
    pKb = 3.36, Kb = 4.37e-04
  Pyridine (C5H5N)
    pKb = 8.75, Kb = 1.78e-09
```

### Python Module

Import and use the calculator in your Python code:

```python
from ph_calculator import pHCalculator

# Create calculator instance
calculator = pHCalculator()

# Calculate pH of 0.1 M HCl
pH = calculator.strong_acid_ph(0.1)
print(f"pH: {pH:.2f}")  # Output: pH: 1.00

# Design a buffer solution
result = calculator.buffer_preparation(
    target_pH=7.4,
    pKa=7.21,
    total_volume=1.0,
    total_concentration=0.1
)
print(f"Acid needed: {result['acid_moles']:.4f} moles")
print(f"Base needed: {result['base_moles']:.4f} moles")
```

See [EXAMPLES.md](EXAMPLES.md) for more detailed usage examples.

## Core Calculations

### 1. Strong Acids/Bases
For strong acids: pH = -log[H⁺] where [H⁺] = concentration
For strong bases: pH = 14 - pOH where pOH = -log[OH⁻]

### 2. Weak Acids/Bases
For weak acids: [H⁺] ≈ √(Ka × C)
For weak bases: [OH⁻] ≈ √(Kb × C)

### 3. Henderson-Hasselbalch Equation
pH = pKa + log([A⁻]/[HA])

Where [A⁻] is conjugate base concentration and [HA] is weak acid concentration.

### 4. Buffer Preparation
Given target pH and pKa, calculates the ratio and amounts of acid/base needed:
- Ratio: [A⁻]/[HA] = 10^(pH - pKa)
- Concentrations calculated from ratio and total concentration

## Testing

Run the comprehensive test suite:
```bash
python test_ph_calculator.py
```

The test suite includes:
- Unit tests for all calculation methods
- Input validation tests
- Integration tests for complete workflows
- Tests using common acids and bases

## Example Calculations

**Strong Acid**: 0.1 M HCl → pH = 1.00

**Strong Base**: 0.01 M NaOH → pH = 12.00

**Weak Acid**: 0.1 M acetic acid (Ka = 1.8×10⁻⁵) → pH ≈ 2.87

**Buffer**: 0.1 M acetic acid + 0.1 M acetate (pKa = 4.76) → pH = 4.76

**Buffer Design**: Target pH 7.4 with 0.1 M phosphate buffer (pKa = 7.21)
- Requires 0.0394 M H₂PO₄⁻ and 0.0606 M HPO₄²⁻

## Common Acids and Bases

The tool includes built-in constants for:
- **Acids**: Acetic acid, formic acid, benzoic acid, carbonic acid, phosphoric acid, citric acid
- **Bases**: Ammonia, methylamine, pyridine

## License

This project is open source and available for educational and research purposes.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests.

## Author

Created to demonstrate chemistry calculations and numerical computation in Python.
