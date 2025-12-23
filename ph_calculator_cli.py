#!/usr/bin/env python3
"""
pH Calculator and Buffer Solution Analyzer - Command Line Interface

This script provides an interactive command-line interface for calculating pH values
and designing buffer solutions.
"""

import sys
from ph_calculator import pHCalculator, COMMON_ACIDS, COMMON_BASES


def print_header():
    """Print the application header."""
    print("\n" + "=" * 70)
    print("pH Calculator and Buffer Solution Analyzer".center(70))
    print("=" * 70)
    print()


def print_menu():
    """Print the main menu."""
    print("\nMain Menu:")
    print("1. Calculate pH of Strong Acid")
    print("2. Calculate pH of Strong Base")
    print("3. Calculate pH of Weak Acid")
    print("4. Calculate pH of Weak Base")
    print("5. Calculate pH of Buffer Solution (Henderson-Hasselbalch)")
    print("6. Design Buffer Solution (Calculate Concentrations for Target pH)")
    print("7. View Common Acids and Bases")
    print("8. Convert between Ka and pKa")
    print("9. Exit")
    print()


def get_float_input(prompt):
    """Get a float input from the user with error handling."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_int_input(prompt, min_val=None, max_val=None):
    """Get an integer input from the user with error handling and bounds checking."""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Invalid input. Please enter a number >= {min_val}.")
                continue
            if max_val is not None and value > max_val:
                print(f"Invalid input. Please enter a number <= {max_val}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")


def strong_acid_calculation(calculator):
    """Handle strong acid pH calculation."""
    print("\n--- Strong Acid pH Calculation ---")
    concentration = get_float_input("Enter the concentration of the strong acid (M): ")
    
    try:
        pH = calculator.strong_acid_ph(concentration)
        print(f"\nResult:")
        print(f"  Concentration: {concentration} M")
        print(f"  pH: {pH:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


def strong_base_calculation(calculator):
    """Handle strong base pH calculation."""
    print("\n--- Strong Base pH Calculation ---")
    concentration = get_float_input("Enter the concentration of the strong base (M): ")
    
    try:
        pH = calculator.strong_base_ph(concentration)
        print(f"\nResult:")
        print(f"  Concentration: {concentration} M")
        print(f"  pH: {pH:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


def weak_acid_calculation(calculator):
    """Handle weak acid pH calculation."""
    print("\n--- Weak Acid pH Calculation ---")
    
    # Ask if user wants to use a common acid
    print("\nUse a common acid? (y/n): ", end="")
    use_common = input().strip().lower()
    
    if use_common == 'y':
        print("\nCommon Acids:")
        for i, (key, acid) in enumerate(COMMON_ACIDS.items(), 1):
            print(f"  {i}. {acid['name']} (pKa = {acid['pKa']})")
        
        choice = get_int_input("\nSelect an acid (number): ", min_val=1, max_val=len(COMMON_ACIDS))
        acid_key = list(COMMON_ACIDS.keys())[choice - 1]
        pKa = COMMON_ACIDS[acid_key]['pKa']
        Ka = calculator.Ka_from_pKa(pKa)
        print(f"Selected: {COMMON_ACIDS[acid_key]['name']}")
    else:
        print("\nEnter Ka or pKa? (ka/pka): ", end="")
        choice = input().strip().lower()
        if choice == 'pka':
            pKa = get_float_input("Enter the pKa value: ")
            Ka = calculator.Ka_from_pKa(pKa)
        else:
            Ka = get_float_input("Enter the Ka value: ")
            pKa = calculator.pKa_from_Ka(Ka)
    
    concentration = get_float_input("Enter the concentration of the weak acid (M): ")
    
    try:
        pH = calculator.weak_acid_ph(concentration, Ka)
        print(f"\nResult:")
        print(f"  Concentration: {concentration} M")
        print(f"  Ka: {Ka:.2e}")
        print(f"  pKa: {pKa:.2f}")
        print(f"  pH: {pH:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


def weak_base_calculation(calculator):
    """Handle weak base pH calculation."""
    print("\n--- Weak Base pH Calculation ---")
    
    # Ask if user wants to use a common base
    print("\nUse a common base? (y/n): ", end="")
    use_common = input().strip().lower()
    
    if use_common == 'y':
        print("\nCommon Bases:")
        for i, (key, base) in enumerate(COMMON_BASES.items(), 1):
            print(f"  {i}. {base['name']} (pKb = {base['pKb']})")
        
        choice = get_int_input("\nSelect a base (number): ", min_val=1, max_val=len(COMMON_BASES))
        base_key = list(COMMON_BASES.keys())[choice - 1]
        pKb = COMMON_BASES[base_key]['pKb']
        Kb = calculator.Kb_from_pKb(pKb)
        print(f"Selected: {COMMON_BASES[base_key]['name']}")
    else:
        print("\nEnter Kb or pKb? (kb/pkb): ", end="")
        choice = input().strip().lower()
        if choice == 'pkb':
            pKb = get_float_input("Enter the pKb value: ")
            Kb = calculator.Kb_from_pKb(pKb)
        else:
            Kb = get_float_input("Enter the Kb value: ")
            pKb = calculator.pKb_from_Kb(Kb)
    
    concentration = get_float_input("Enter the concentration of the weak base (M): ")
    
    try:
        pH = calculator.weak_base_ph(concentration, Kb)
        print(f"\nResult:")
        print(f"  Concentration: {concentration} M")
        print(f"  Kb: {Kb:.2e}")
        print(f"  pKb: {pKb:.2f}")
        print(f"  pH: {pH:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


def henderson_hasselbalch_calculation(calculator):
    """Handle Henderson-Hasselbalch buffer pH calculation."""
    print("\n--- Buffer Solution pH Calculation (Henderson-Hasselbalch) ---")
    
    # Ask if user wants to use a common acid
    print("\nUse a common acid? (y/n): ", end="")
    use_common = input().strip().lower()
    
    if use_common == 'y':
        print("\nCommon Acids:")
        for i, (key, acid) in enumerate(COMMON_ACIDS.items(), 1):
            print(f"  {i}. {acid['name']} (pKa = {acid['pKa']})")
        
        choice = get_int_input("\nSelect an acid (number): ", min_val=1, max_val=len(COMMON_ACIDS))
        acid_key = list(COMMON_ACIDS.keys())[choice - 1]
        pKa = COMMON_ACIDS[acid_key]['pKa']
        print(f"Selected: {COMMON_ACIDS[acid_key]['name']}")
    else:
        print("\nEnter Ka or pKa? (ka/pka): ", end="")
        choice = input().strip().lower()
        if choice == 'pka':
            pKa = get_float_input("Enter the pKa value: ")
        else:
            Ka = get_float_input("Enter the Ka value: ")
            pKa = calculator.pKa_from_Ka(Ka)
    
    acid_conc = get_float_input("Enter the concentration of weak acid [HA] (M): ")
    base_conc = get_float_input("Enter the concentration of conjugate base [A-] (M): ")
    
    try:
        pH = calculator.henderson_hasselbalch(pKa, acid_conc, base_conc)
        capacity = calculator.buffer_capacity(acid_conc, base_conc)
        print(f"\nResult:")
        print(f"  pKa: {pKa:.2f}")
        print(f"  [HA]: {acid_conc} M")
        print(f"  [A-]: {base_conc} M")
        print(f"  Ratio [A-]/[HA]: {base_conc/acid_conc:.2f}")
        print(f"  Buffer Capacity: {capacity} M")
        print(f"  pH: {pH:.2f}")
    except ValueError as e:
        print(f"Error: {e}")


def buffer_preparation_calculation(calculator):
    """Handle buffer preparation calculation."""
    print("\n--- Buffer Solution Preparation ---")
    print("Calculate concentrations needed to achieve a target pH")
    
    # Ask if user wants to use a common acid
    print("\nUse a common acid? (y/n): ", end="")
    use_common = input().strip().lower()
    
    if use_common == 'y':
        print("\nCommon Acids:")
        for i, (key, acid) in enumerate(COMMON_ACIDS.items(), 1):
            print(f"  {i}. {acid['name']} (pKa = {acid['pKa']})")
        
        choice = get_int_input("\nSelect an acid (number): ", min_val=1, max_val=len(COMMON_ACIDS))
        acid_key = list(COMMON_ACIDS.keys())[choice - 1]
        pKa = COMMON_ACIDS[acid_key]['pKa']
        acid_name = COMMON_ACIDS[acid_key]['name']
        print(f"Selected: {acid_name}")
    else:
        acid_name = "your acid"
        print("\nEnter Ka or pKa? (ka/pka): ", end="")
        choice = input().strip().lower()
        if choice == 'pka':
            pKa = get_float_input("Enter the pKa value: ")
        else:
            Ka = get_float_input("Enter the Ka value: ")
            pKa = calculator.pKa_from_Ka(Ka)
    
    target_pH = get_float_input("Enter the target pH: ")
    total_volume = get_float_input("Enter the total volume (L): ")
    total_concentration = get_float_input("Enter the total buffer concentration (M): ")
    
    try:
        result = calculator.buffer_preparation(target_pH, pKa, total_volume, total_concentration)
        
        print(f"\nBuffer Preparation Recipe:")
        print(f"  Target pH: {target_pH}")
        print(f"  pKa: {pKa:.2f}")
        print(f"  Total Volume: {total_volume} L")
        print(f"  Total Concentration: {total_concentration} M")
        print(f"\n  Required Concentrations:")
        print(f"    Weak Acid [HA]: {result['acid_concentration']:.4f} M")
        print(f"    Conjugate Base [A-]: {result['base_concentration']:.4f} M")
        print(f"\n  Required Amounts:")
        print(f"    Weak Acid: {result['acid_moles']:.4f} moles")
        print(f"    Conjugate Base: {result['base_moles']:.4f} moles")
        print(f"\n  Ratio [A-]/[HA]: {result['ratio']:.4f}")
        
        # Additional advice
        if abs(target_pH - pKa) > 1:
            print(f"\n  Note: Target pH differs from pKa by more than 1 unit.")
            print(f"        Buffer capacity will be reduced. Consider using a different buffer system.")
        else:
            print(f"\n  Good choice! This buffer will have good capacity at pH {target_pH}.")
            
    except ValueError as e:
        print(f"Error: {e}")


def view_common_compounds(calculator):
    """Display common acids and bases with their constants."""
    print("\n--- Common Acids and Bases ---")
    
    print("\nCommon Acids:")
    for key, acid in COMMON_ACIDS.items():
        Ka = calculator.Ka_from_pKa(acid['pKa'])
        print(f"  {acid['name']}")
        print(f"    pKa = {acid['pKa']:.2f}, Ka = {Ka:.2e}")
    
    print("\nCommon Bases:")
    for key, base in COMMON_BASES.items():
        Kb = 10 ** (-base['pKb'])
        print(f"  {base['name']}")
        print(f"    pKb = {base['pKb']:.2f}, Kb = {Kb:.2e}")


def convert_constants(calculator):
    """Handle Ka/pKa conversion."""
    print("\n--- Ka/pKa Conversion ---")
    print("1. Convert Ka to pKa")
    print("2. Convert pKa to Ka")
    print("3. Calculate Kb from Ka")
    print("4. Calculate Ka from Kb")
    
    choice = get_int_input("\nSelect conversion (number): ", min_val=1, max_val=4)
    
    if choice == 1:
        Ka = get_float_input("Enter Ka value: ")
        try:
            pKa = calculator.pKa_from_Ka(Ka)
            print(f"\nResult: Ka = {Ka:.2e} → pKa = {pKa:.2f}")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == 2:
        pKa = get_float_input("Enter pKa value: ")
        Ka = calculator.Ka_from_pKa(pKa)
        print(f"\nResult: pKa = {pKa:.2f} → Ka = {Ka:.2e}")
    elif choice == 3:
        Ka = get_float_input("Enter Ka value: ")
        try:
            Kb = calculator.Kb_from_Ka(Ka)
            pKb = calculator.pKb_from_Kb(Kb)
            print(f"\nResult: Ka = {Ka:.2e} → Kb = {Kb:.2e} (pKb = {pKb:.2f})")
        except ValueError as e:
            print(f"Error: {e}")
    elif choice == 4:
        Kb = get_float_input("Enter Kb value: ")
        try:
            Ka = calculator.Ka_from_Kb(Kb)
            pKa = calculator.pKa_from_Ka(Ka)
            print(f"\nResult: Kb = {Kb:.2e} → Ka = {Ka:.2e} (pKa = {pKa:.2f})")
        except ValueError as e:
            print(f"Error: {e}")


def main():
    """Main application loop."""
    calculator = pHCalculator()
    
    print_header()
    print("Welcome to the pH Calculator and Buffer Solution Analyzer!")
    print("This tool helps you calculate pH values and design buffer solutions.")
    
    while True:
        print_menu()
        
        try:
            choice = input("Enter your choice (1-9): ").strip()
            
            if choice == '1':
                strong_acid_calculation(calculator)
            elif choice == '2':
                strong_base_calculation(calculator)
            elif choice == '3':
                weak_acid_calculation(calculator)
            elif choice == '4':
                weak_base_calculation(calculator)
            elif choice == '5':
                henderson_hasselbalch_calculation(calculator)
            elif choice == '6':
                buffer_preparation_calculation(calculator)
            elif choice == '7':
                view_common_compounds(calculator)
            elif choice == '8':
                convert_constants(calculator)
            elif choice == '9':
                print("\nThank you for using the pH Calculator!")
                print("Goodbye!\n")
                sys.exit(0)
            else:
                print("\nInvalid choice. Please enter a number between 1 and 9.")
                
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user.")
            print("Goodbye!\n")
            sys.exit(0)
        except Exception as e:
            print(f"\nAn error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
