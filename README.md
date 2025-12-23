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
