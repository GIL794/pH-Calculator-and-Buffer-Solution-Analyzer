#!/usr/bin/env python3
"""
Demo script for pH Calculator and Buffer Solution Analyzer

This script demonstrates the key features of the pH calculator tool.
"""

import math
from ph_calculator import pHCalculator, COMMON_ACIDS, COMMON_BASES


def print_section(title):
    """Print a formatted section header."""
    print("\n" + "=" * 70)
    print(f" {title}")
    print("=" * 70)


def demo_strong_acids_bases():
    """Demonstrate strong acid and base calculations."""
    print_section("Strong Acids and Bases")
    
    calculator = pHCalculator()
    
    # Strong acids
    print("\nStrong Acids:")
    concentrations = [1.0, 0.1, 0.01, 0.001]
    for conc in concentrations:
        pH = calculator.strong_acid_ph(conc)
        print(f"  {conc} M HCl → pH = {pH:.2f}")
    
    # Strong bases
    print("\nStrong Bases:")
    for conc in concentrations:
        pH = calculator.strong_base_ph(conc)
        print(f"  {conc} M NaOH → pH = {pH:.2f}")


def demo_weak_acids_bases():
    """Demonstrate weak acid and base calculations."""
    print_section("Weak Acids and Bases")
    
    calculator = pHCalculator()
    
    # Weak acids
    print("\nWeak Acids (0.1 M solutions):")
    for key, acid in COMMON_ACIDS.items():
        Ka = calculator.Ka_from_pKa(acid['pKa'])
        pH = calculator.weak_acid_ph(0.1, Ka)
        print(f"  {acid['name']}: pKa = {acid['pKa']:.2f}, pH = {pH:.2f}")
    
    # Weak bases
    print("\nWeak Bases (0.1 M solutions):")
    for key, base in COMMON_BASES.items():
        Kb = 10 ** (-base['pKb'])
        pH = calculator.weak_base_ph(0.1, Kb)
        print(f"  {base['name']}: pKb = {base['pKb']:.2f}, pH = {pH:.2f}")


def demo_buffers():
    """Demonstrate buffer calculations using Henderson-Hasselbalch."""
    print_section("Buffer Solutions (Henderson-Hasselbalch)")
    
    calculator = pHCalculator()
    
    print("\nAcetic acid buffer (pKa = 4.76, total 0.2 M):")
    pKa = COMMON_ACIDS['acetic_acid']['pKa']
    
    ratios = [
        (0.1, 0.1, "1:1"),
        (0.15, 0.05, "1:3 (base:acid)"),
        (0.05, 0.15, "3:1 (base:acid)"),
        (0.18, 0.02, "1:9"),
    ]
    
    for base_conc, acid_conc, ratio_desc in ratios:
        pH = calculator.henderson_hasselbalch(pKa, acid_conc, base_conc)
        capacity = calculator.buffer_capacity(acid_conc, base_conc)
        print(f"  [{ratio_desc}] [HA]={acid_conc} M, [A-]={base_conc} M → pH = {pH:.2f}")


def demo_buffer_design():
    """Demonstrate buffer solution design."""
    print_section("Buffer Solution Design")
    
    calculator = pHCalculator()
    
    print("\nDesigning buffers with different pH targets:")
    print("Using acetic acid/acetate system (pKa = 4.76)")
    print("Total concentration: 0.2 M, Volume: 1.0 L\n")
    
    pKa = COMMON_ACIDS['acetic_acid']['pKa']
    target_pHs = [4.0, 4.5, 4.76, 5.0, 5.5]
    
    for target_pH in target_pHs:
        result = calculator.buffer_preparation(target_pH, pKa, 1.0, 0.2)
        print(f"Target pH {target_pH:.2f}:")
        print(f"  Acid (CH3COOH):  {result['acid_moles']:.4f} moles ({result['acid_concentration']:.4f} M)")
        print(f"  Base (CH3COO-):  {result['base_moles']:.4f} moles ({result['base_concentration']:.4f} M)")
        print(f"  Ratio [A-]/[HA]: {result['ratio']:.4f}")
        
        # Verify the pH
        actual_pH = calculator.henderson_hasselbalch(pKa, result['acid_concentration'], 
                                                      result['base_concentration'])
        print(f"  Verification: pH = {actual_pH:.2f} ✓")
        print()


def demo_physiological_buffers():
    """Demonstrate physiological buffer systems."""
    print_section("Physiological Buffer Systems")
    
    calculator = pHCalculator()
    
    print("\nBlood pH is maintained at ~7.4 by several buffer systems:\n")
    
    # Phosphate buffer
    print("1. Phosphate Buffer (H2PO4- / HPO4²-)")
    pKa_phosphate = 7.21  # Second pKa
    result = calculator.buffer_preparation(7.4, pKa_phosphate, 1.0, 0.1)
    print(f"   pKa = {pKa_phosphate}")
    print(f"   For pH 7.4 buffer:")
    print(f"   [H2PO4-] = {result['acid_concentration']:.4f} M")
    print(f"   [HPO4²-] = {result['base_concentration']:.4f} M")
    
    # Carbonic acid buffer (bicarbonate system)
    print("\n2. Bicarbonate Buffer (H2CO3 / HCO3-)")
    pKa_carbonic = COMMON_ACIDS['carbonic_acid']['pKa']
    result = calculator.buffer_preparation(7.4, pKa_carbonic, 1.0, 0.025)
    print(f"   pKa = {pKa_carbonic}")
    print(f"   For pH 7.4 buffer:")
    print(f"   [H2CO3] = {result['acid_concentration']:.4f} M")
    print(f"   [HCO3-] = {result['base_concentration']:.4f} M")
    print(f"   Note: The large ratio ({result['ratio']:.1f}:1) makes this system")
    print(f"         effective at buffering against acid loads.")


def demo_conversions():
    """Demonstrate constant conversions."""
    print_section("Constant Conversions")
    
    calculator = pHCalculator()
    
    print("\nConverting between Ka, pKa, Kb, and pKb:\n")
    
    # Example with acetic acid
    print("Acetic Acid / Acetate System:")
    pKa = COMMON_ACIDS['acetic_acid']['pKa']
    Ka = calculator.Ka_from_pKa(pKa)
    Kb = calculator.Kb_from_Ka(Ka)
    pKb = calculator.pKb_from_Kb(Kb)
    
    print(f"  Acetic acid:  pKa = {pKa:.2f}, Ka = {Ka:.2e}")
    print(f"  Acetate ion:  pKb = {pKb:.2f}, Kb = {Kb:.2e}")
    print(f"  Verification: pKa + pKb = {pKa + pKb:.2f} (should be 14.00)")
    
    # Example with ammonia
    print("\nAmmonia / Ammonium System:")
    pKb = COMMON_BASES['ammonia']['pKb']
    Kb = calculator.Kb_from_pKb(pKb)
    Ka = calculator.Ka_from_Kb(Kb)
    pKa = calculator.pKa_from_Ka(Ka)
    
    print(f"  Ammonia (NH3):      pKb = {pKb:.2f}, Kb = {Kb:.2e}")
    print(f"  Ammonium (NH4+):    pKa = {pKa:.2f}, Ka = {Ka:.2e}")
    print(f"  Verification: pKa + pKb = {pKa + pKb:.2f} (should be 14.00)")


def main():
    """Run all demonstrations."""
    print("\n" + "=" * 70)
    print(" pH CALCULATOR AND BUFFER SOLUTION ANALYZER - DEMO")
    print("=" * 70)
    print("\nThis demo showcases the key features of the pH calculator tool.")
    
    demo_strong_acids_bases()
    demo_weak_acids_bases()
    demo_buffers()
    demo_buffer_design()
    demo_physiological_buffers()
    demo_conversions()
    
    print("\n" + "=" * 70)
    print(" Demo Complete!")
    print("=" * 70)
    print("\nFor interactive use, run: python ph_calculator_cli.py")
    print("For more examples, see: EXAMPLES.md\n")


if __name__ == "__main__":
    main()
