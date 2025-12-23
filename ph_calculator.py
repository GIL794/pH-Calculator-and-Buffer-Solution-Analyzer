"""
pH Calculator and Buffer Solution Analyzer

This module provides tools for calculating pH values for various chemical solutions,
including strong acids/bases, weak acids/bases, and buffer solutions.
It also calculates concentrations needed to create buffer solutions with specific pH values.
"""

import math


class pHCalculator:
    """
    A comprehensive pH calculator for various types of chemical solutions.
    """
    
    def __init__(self):
        """Initialize the pH calculator with water ionization constant."""
        self.Kw = 1.0e-14  # Water ionization constant at 25°C
    
    def strong_acid_ph(self, concentration):
        """
        Calculate pH of a strong acid solution.
        
        Args:
            concentration (float): Molar concentration of the strong acid (M)
            
        Returns:
            float: pH value
            
        Raises:
            ValueError: If concentration is not positive
        """
        if concentration <= 0:
            raise ValueError("Concentration must be positive")
        
        # For strong acids, [H+] = concentration
        return -math.log10(concentration)
    
    def strong_base_ph(self, concentration):
        """
        Calculate pH of a strong base solution.
        
        Args:
            concentration (float): Molar concentration of the strong base (M)
            
        Returns:
            float: pH value
            
        Raises:
            ValueError: If concentration is not positive
        """
        if concentration <= 0:
            raise ValueError("Concentration must be positive")
        
        # For strong bases, [OH-] = concentration
        pOH = -math.log10(concentration)
        return 14 - pOH
    
    def weak_acid_ph(self, concentration, Ka):
        """
        Calculate pH of a weak acid solution using the acid dissociation constant.
        
        Args:
            concentration (float): Molar concentration of the weak acid (M)
            Ka (float): Acid dissociation constant
            
        Returns:
            float: pH value
            
        Raises:
            ValueError: If concentration or Ka is not positive
        """
        if concentration <= 0 or Ka <= 0:
            raise ValueError("Concentration and Ka must be positive")
        
        # For weak acids: [H+] ≈ sqrt(Ka * C) when Ka is small
        H_plus = math.sqrt(Ka * concentration)
        return -math.log10(H_plus)
    
    def weak_base_ph(self, concentration, Kb):
        """
        Calculate pH of a weak base solution using the base dissociation constant.
        
        Args:
            concentration (float): Molar concentration of the weak base (M)
            Kb (float): Base dissociation constant
            
        Returns:
            float: pH value
            
        Raises:
            ValueError: If concentration or Kb is not positive
        """
        if concentration <= 0 or Kb <= 0:
            raise ValueError("Concentration and Kb must be positive")
        
        # For weak bases: [OH-] ≈ sqrt(Kb * C) when Kb is small
        OH_minus = math.sqrt(Kb * concentration)
        pOH = -math.log10(OH_minus)
        return 14 - pOH
    
    def henderson_hasselbalch(self, pKa, acid_conc, base_conc):
        """
        Calculate pH using the Henderson-Hasselbalch equation for buffer solutions.
        
        pH = pKa + log([A-]/[HA])
        
        Args:
            pKa (float): pKa value of the weak acid
            acid_conc (float): Concentration of weak acid (HA) in M
            base_conc (float): Concentration of conjugate base (A-) in M
            
        Returns:
            float: pH value
            
        Raises:
            ValueError: If concentrations are not positive
        """
        if acid_conc <= 0 or base_conc <= 0:
            raise ValueError("Acid and base concentrations must be positive")
        
        # Henderson-Hasselbalch equation
        pH = pKa + math.log10(base_conc / acid_conc)
        return pH
    
    def buffer_capacity(self, acid_conc, base_conc):
        """
        Calculate the buffer capacity (total concentration of buffering species).
        
        Args:
            acid_conc (float): Concentration of weak acid (HA) in M
            base_conc (float): Concentration of conjugate base (A-) in M
            
        Returns:
            float: Total buffer capacity in M
        """
        return acid_conc + base_conc
    
    def buffer_preparation(self, target_pH, pKa, total_volume, total_concentration):
        """
        Calculate the concentrations needed to prepare a buffer solution with a specific pH.
        
        Args:
            target_pH (float): Desired pH value
            pKa (float): pKa value of the weak acid
            total_volume (float): Total volume of the buffer solution in liters
            total_concentration (float): Total molar concentration of buffering species in M
            
        Returns:
            dict: Dictionary containing:
                - 'acid_concentration': Concentration of weak acid (M)
                - 'base_concentration': Concentration of conjugate base (M)
                - 'acid_moles': Moles of weak acid needed
                - 'base_moles': Moles of conjugate base needed
                - 'ratio': Base to acid ratio
                
        Raises:
            ValueError: If parameters are invalid
        """
        if total_concentration <= 0 or total_volume <= 0:
            raise ValueError("Total concentration and volume must be positive")
        
        # From Henderson-Hasselbalch: pH = pKa + log([A-]/[HA])
        # Therefore: [A-]/[HA] = 10^(pH - pKa)
        ratio = 10 ** (target_pH - pKa)
        
        # [A-] + [HA] = total_concentration
        # [A-] = ratio * [HA]
        # ratio * [HA] + [HA] = total_concentration
        # [HA] * (ratio + 1) = total_concentration
        
        acid_conc = total_concentration / (ratio + 1)
        base_conc = total_concentration - acid_conc
        
        acid_moles = acid_conc * total_volume
        base_moles = base_conc * total_volume
        
        return {
            'acid_concentration': acid_conc,
            'base_concentration': base_conc,
            'acid_moles': acid_moles,
            'base_moles': base_moles,
            'ratio': ratio
        }
    
    def Ka_from_pKa(self, pKa):
        """
        Convert pKa to Ka.
        
        Args:
            pKa (float): pKa value
            
        Returns:
            float: Ka value
        """
        return 10 ** (-pKa)
    
    def pKa_from_Ka(self, Ka):
        """
        Convert Ka to pKa.
        
        Args:
            Ka (float): Ka value
            
        Returns:
            float: pKa value
            
        Raises:
            ValueError: If Ka is not positive
        """
        if Ka <= 0:
            raise ValueError("Ka must be positive")
        return -math.log10(Ka)
    
    def Kb_from_Ka(self, Ka):
        """
        Calculate Kb from Ka using the relationship Ka * Kb = Kw.
        
        Args:
            Ka (float): Acid dissociation constant
            
        Returns:
            float: Base dissociation constant
            
        Raises:
            ValueError: If Ka is not positive
        """
        if Ka <= 0:
            raise ValueError("Ka must be positive")
        return self.Kw / Ka
    
    def Ka_from_Kb(self, Kb):
        """
        Calculate Ka from Kb using the relationship Ka * Kb = Kw.
        
        Args:
            Kb (float): Base dissociation constant
            
        Returns:
            float: Acid dissociation constant
            
        Raises:
            ValueError: If Kb is not positive
        """
        if Kb <= 0:
            raise ValueError("Kb must be positive")
        return self.Kw / Kb


# Common acid/base constants
COMMON_ACIDS = {
    'acetic_acid': {'name': 'Acetic Acid (CH3COOH)', 'pKa': 4.76},
    'formic_acid': {'name': 'Formic Acid (HCOOH)', 'pKa': 3.75},
    'benzoic_acid': {'name': 'Benzoic Acid (C6H5COOH)', 'pKa': 4.20},
    'carbonic_acid': {'name': 'Carbonic Acid (H2CO3)', 'pKa': 6.35},  # first pKa
    'phosphoric_acid': {'name': 'Phosphoric Acid (H3PO4)', 'pKa': 2.15},  # first pKa
    'citric_acid': {'name': 'Citric Acid', 'pKa': 3.13},  # first pKa
}

COMMON_BASES = {
    'ammonia': {'name': 'Ammonia (NH3)', 'pKb': 4.75},
    'methylamine': {'name': 'Methylamine (CH3NH2)', 'pKb': 3.36},
    'pyridine': {'name': 'Pyridine (C5H5N)', 'pKb': 8.75},
}
