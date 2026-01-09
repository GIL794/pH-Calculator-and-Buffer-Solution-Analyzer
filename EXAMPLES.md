# Example Usage Guide for pH Calculator and Buffer Solution Analyzer

This document provides examples of how to use the pH Calculator both as a Python module and through the command-line interface.

## Using as a Python Module

```python
from ph_calculator import pHCalculator, COMMON_ACIDS

# Create calculator instance
calculator = pHCalculator()

# Example 1: Calculate pH of a strong acid
pH = calculator.strong_acid_ph(0.1)  # 0.1 M HCl
print(f"pH of 0.1 M HCl: {pH:.2f}")  # Output: pH of 0.1 M HCl: 1.00

# Example 2: Calculate pH of a strong base
pH = calculator.strong_base_ph(0.01)  # 0.01 M NaOH
print(f"pH of 0.01 M NaOH: {pH:.2f}")  # Output: pH of 0.01 M NaOH: 12.00

# Example 3: Calculate pH of a weak acid
Ka = 1.8e-5  # Acetic acid Ka
pH = calculator.weak_acid_ph(0.1, Ka)
print(f"pH of 0.1 M acetic acid: {pH:.2f}")  # Output: pH of 0.1 M acetic acid: 2.87

# Example 4: Calculate pH using Henderson-Hasselbalch equation
pKa = 4.76  # Acetic acid pKa
acid_conc = 0.1  # [CH3COOH]
base_conc = 0.1  # [CH3COO-]
pH = calculator.henderson_hasselbalch(pKa, acid_conc, base_conc)
print(f"Buffer pH: {pH:.2f}")  # Output: Buffer pH: 4.76

# Example 5: Design a buffer solution
result = calculator.buffer_preparation(
    target_pH=5.0,
    pKa=4.76,
    total_volume=1.0,  # 1 liter
    total_concentration=0.2  # 0.2 M total
)
print(f"Acid concentration needed: {result['acid_concentration']:.4f} M")
print(f"Base concentration needed: {result['base_concentration']:.4f} M")
print(f"Acid moles needed: {result['acid_moles']:.4f} moles")
print(f"Base moles needed: {result['base_moles']:.4f} moles")

# Example 6: Convert between Ka and pKa
Ka = 1.8e-5
pKa = calculator.pKa_from_Ka(Ka)
print(f"Ka = {Ka:.2e} corresponds to pKa = {pKa:.2f}")

# Example 7: Using common acids database
acetic_acid_pKa = COMMON_ACIDS['acetic_acid']['pKa']
print(f"Acetic acid pKa: {acetic_acid_pKa}")
```

## Using the Command-Line Interface

Run the interactive CLI:

```bash
python ph_calculator_cli.py
```

### Example Session

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

Enter your choice (1-9): 1

--- Strong Acid pH Calculation ---
Enter the concentration of the strong acid (M): 0.1

Result:
  Concentration: 0.1 M
  pH: 1.00
```

## Common Use Cases

### 1. Calculating pH of Laboratory Solutions

```python
# Hydrochloric acid (HCl) - Strong acid
pH_hcl = calculator.strong_acid_ph(0.05)  # 0.05 M

# Sodium hydroxide (NaOH) - Strong base
pH_naoh = calculator.strong_base_ph(0.02)  # 0.02 M

# Acetic acid - Weak acid
Ka_acetic = 1.8e-5
pH_acetic = calculator.weak_acid_ph(0.1, Ka_acetic)
```

### 2. Preparing Buffer Solutions

```python
# Prepare a phosphate buffer at pH 7.4 (physiological pH)
pKa_phosphate = 7.21  # Second pKa of phosphoric acid

buffer_recipe = calculator.buffer_preparation(
    target_pH=7.4,
    pKa=pKa_phosphate,
    total_volume=0.5,  # 500 mL
    total_concentration=0.1  # 0.1 M buffer
)

print(f"For 500 mL of 0.1 M phosphate buffer at pH 7.4:")
print(f"  H2PO4- needed: {buffer_recipe['acid_moles']:.4f} moles")
print(f"  HPO4²- needed: {buffer_recipe['base_moles']:.4f} moles")
```

### 3. Buffer Capacity Analysis

```python
# Compare different buffer compositions
compositions = [
    (0.05, 0.05),
    (0.1, 0.1),
    (0.08, 0.12),
]

pKa = 4.76
for acid, base in compositions:
    pH = calculator.henderson_hasselbalch(pKa, acid, base)
    capacity = calculator.buffer_capacity(acid, base)
    print(f"[HA]={acid} M, [A-]={base} M: pH={pH:.2f}, Capacity={capacity:.2f} M")
```

### 4. Converting Between Constants

```python
# Given Ka, find pKa
Ka = 1.8e-5
pKa = calculator.pKa_from_Ka(Ka)
print(f"Ka = {Ka:.2e} → pKa = {pKa:.2f}")

# Given pKa, find Ka
pKa = 4.76
Ka = calculator.Ka_from_pKa(pKa)
print(f"pKa = {pKa} → Ka = {Ka:.2e}")

# Convert between Ka and Kb (conjugate pairs)
Ka = 1.8e-5
Kb = calculator.Kb_from_Ka(Ka)
print(f"If Ka = {Ka:.2e}, then Kb = {Kb:.2e}")
```

## Tips for Effective Buffer Design

1. **Choose appropriate pKa**: The buffer should have a pKa within ±1 pH unit of your target pH for maximum buffering capacity.

2. **Total concentration**: Higher total concentrations provide greater buffer capacity but may affect other solution properties.

3. **Ratio considerations**: The [A-]/[HA] ratio should be between 0.1 and 10 for effective buffering (corresponding to pH = pKa ± 1).

## Running Tests

To verify the calculator works correctly:

```bash
python test_ph_calculator.py
```

All tests should pass, confirming:
- Accurate pH calculations for all solution types
- Correct Henderson-Hasselbalch equation implementation
- Valid buffer preparation calculations
- Proper error handling for invalid inputs
