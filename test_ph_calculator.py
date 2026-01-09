"""
Unit tests for pH Calculator and Buffer Solution Analyzer
"""

import unittest
import math
from ph_calculator import pHCalculator, COMMON_ACIDS, COMMON_BASES


class TestpHCalculator(unittest.TestCase):
    """Test cases for the pHCalculator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calculator = pHCalculator()
    
    def test_strong_acid_ph(self):
        """Test strong acid pH calculation."""
        # Test case 1: 0.1 M HCl should have pH = 1
        pH = self.calculator.strong_acid_ph(0.1)
        self.assertAlmostEqual(pH, 1.0, places=5)
        
        # Test case 2: 0.01 M HCl should have pH = 2
        pH = self.calculator.strong_acid_ph(0.01)
        self.assertAlmostEqual(pH, 2.0, places=5)
        
        # Test case 3: 1 M HCl should have pH = 0
        pH = self.calculator.strong_acid_ph(1.0)
        self.assertAlmostEqual(pH, 0.0, places=5)
        
    def test_strong_acid_ph_invalid_input(self):
        """Test strong acid pH calculation with invalid input."""
        with self.assertRaises(ValueError):
            self.calculator.strong_acid_ph(0)
        with self.assertRaises(ValueError):
            self.calculator.strong_acid_ph(-0.1)
    
    def test_strong_base_ph(self):
        """Test strong base pH calculation."""
        # Test case 1: 0.1 M NaOH should have pH = 13
        pH = self.calculator.strong_base_ph(0.1)
        self.assertAlmostEqual(pH, 13.0, places=5)
        
        # Test case 2: 0.01 M NaOH should have pH = 12
        pH = self.calculator.strong_base_ph(0.01)
        self.assertAlmostEqual(pH, 12.0, places=5)
        
        # Test case 3: 1 M NaOH should have pH = 14
        pH = self.calculator.strong_base_ph(1.0)
        self.assertAlmostEqual(pH, 14.0, places=5)
    
    def test_strong_base_ph_invalid_input(self):
        """Test strong base pH calculation with invalid input."""
        with self.assertRaises(ValueError):
            self.calculator.strong_base_ph(0)
        with self.assertRaises(ValueError):
            self.calculator.strong_base_ph(-0.1)
    
    def test_weak_acid_ph(self):
        """Test weak acid pH calculation."""
        # Test case: 0.1 M acetic acid (Ka = 1.8e-5)
        # Expected pH ≈ 2.87
        Ka = 1.8e-5
        concentration = 0.1
        pH = self.calculator.weak_acid_ph(concentration, Ka)
        self.assertAlmostEqual(pH, 2.87, places=1)
        
        # Test case 2: 0.01 M acetic acid
        # Expected pH ≈ 3.37
        pH = self.calculator.weak_acid_ph(0.01, Ka)
        self.assertAlmostEqual(pH, 3.37, places=1)
    
    def test_weak_acid_ph_invalid_input(self):
        """Test weak acid pH calculation with invalid input."""
        with self.assertRaises(ValueError):
            self.calculator.weak_acid_ph(0, 1.8e-5)
        with self.assertRaises(ValueError):
            self.calculator.weak_acid_ph(0.1, 0)
        with self.assertRaises(ValueError):
            self.calculator.weak_acid_ph(-0.1, 1.8e-5)
    
    def test_weak_base_ph(self):
        """Test weak base pH calculation."""
        # Test case: 0.1 M ammonia (Kb = 1.8e-5)
        # Expected pH ≈ 11.13
        Kb = 1.8e-5
        concentration = 0.1
        pH = self.calculator.weak_base_ph(concentration, Kb)
        self.assertAlmostEqual(pH, 11.13, places=1)
        
        # Test case 2: 0.01 M ammonia
        # Expected pH ≈ 10.63
        pH = self.calculator.weak_base_ph(0.01, Kb)
        self.assertAlmostEqual(pH, 10.63, places=1)
    
    def test_weak_base_ph_invalid_input(self):
        """Test weak base pH calculation with invalid input."""
        with self.assertRaises(ValueError):
            self.calculator.weak_base_ph(0, 1.8e-5)
        with self.assertRaises(ValueError):
            self.calculator.weak_base_ph(0.1, 0)
        with self.assertRaises(ValueError):
            self.calculator.weak_base_ph(-0.1, 1.8e-5)
    
    def test_henderson_hasselbalch(self):
        """Test Henderson-Hasselbalch equation."""
        # Test case 1: Equal concentrations, pH should equal pKa
        pKa = 4.76
        pH = self.calculator.henderson_hasselbalch(pKa, 0.1, 0.1)
        self.assertAlmostEqual(pH, pKa, places=5)
        
        # Test case 2: Base concentration 10x acid concentration
        # pH = pKa + log(10) = pKa + 1
        pH = self.calculator.henderson_hasselbalch(pKa, 0.1, 1.0)
        self.assertAlmostEqual(pH, pKa + 1, places=5)
        
        # Test case 3: Acid concentration 10x base concentration
        # pH = pKa + log(0.1) = pKa - 1
        pH = self.calculator.henderson_hasselbalch(pKa, 1.0, 0.1)
        self.assertAlmostEqual(pH, pKa - 1, places=5)
    
    def test_henderson_hasselbalch_invalid_input(self):
        """Test Henderson-Hasselbalch with invalid input."""
        with self.assertRaises(ValueError):
            self.calculator.henderson_hasselbalch(4.76, 0, 0.1)
        with self.assertRaises(ValueError):
            self.calculator.henderson_hasselbalch(4.76, 0.1, 0)
    
    def test_buffer_capacity(self):
        """Test buffer capacity calculation."""
        capacity = self.calculator.buffer_capacity(0.1, 0.1)
        self.assertAlmostEqual(capacity, 0.2, places=5)
        
        capacity = self.calculator.buffer_capacity(0.05, 0.15)
        self.assertAlmostEqual(capacity, 0.2, places=5)
    
    def test_buffer_preparation(self):
        """Test buffer preparation calculation."""
        # Test case: Prepare a pH 4.76 buffer with pKa 4.76
        # With equal concentrations expected
        pKa = 4.76
        target_pH = 4.76
        total_volume = 1.0  # 1 liter
        total_concentration = 0.2  # 0.2 M total
        
        result = self.calculator.buffer_preparation(target_pH, pKa, total_volume, total_concentration)
        
        # When pH = pKa, concentrations should be equal
        self.assertAlmostEqual(result['acid_concentration'], 0.1, places=5)
        self.assertAlmostEqual(result['base_concentration'], 0.1, places=5)
        self.assertAlmostEqual(result['ratio'], 1.0, places=5)
        self.assertAlmostEqual(result['acid_moles'], 0.1, places=5)
        self.assertAlmostEqual(result['base_moles'], 0.1, places=5)
        
        # Test case 2: pH = pKa + 1 (base concentration should be 10x acid)
        target_pH = pKa + 1
        result = self.calculator.buffer_preparation(target_pH, pKa, total_volume, total_concentration)
        
        # Ratio should be 10
        self.assertAlmostEqual(result['ratio'], 10.0, places=5)
        # Base should be ~0.182 M, acid should be ~0.018 M
        self.assertAlmostEqual(result['base_concentration'] / result['acid_concentration'], 10.0, places=5)
        self.assertAlmostEqual(result['acid_concentration'] + result['base_concentration'], 
                              total_concentration, places=5)
    
    def test_buffer_preparation_invalid_input(self):
        """Test buffer preparation with invalid input."""
        with self.assertRaises(ValueError):
            self.calculator.buffer_preparation(7.0, 4.76, 0, 0.2)
        with self.assertRaises(ValueError):
            self.calculator.buffer_preparation(7.0, 4.76, 1.0, 0)
    
    def test_Ka_from_pKa(self):
        """Test Ka to pKa conversion."""
        pKa = 4.76
        Ka = self.calculator.Ka_from_pKa(pKa)
        expected_Ka = 10 ** (-4.76)
        self.assertAlmostEqual(Ka, expected_Ka, places=10)
    
    def test_pKa_from_Ka(self):
        """Test pKa to Ka conversion."""
        Ka = 1.8e-5
        pKa = self.calculator.pKa_from_Ka(Ka)
        expected_pKa = -math.log10(1.8e-5)
        self.assertAlmostEqual(pKa, expected_pKa, places=5)
    
    def test_pKa_from_Ka_invalid_input(self):
        """Test pKa from Ka with invalid input."""
        with self.assertRaises(ValueError):
            self.calculator.pKa_from_Ka(0)
        with self.assertRaises(ValueError):
            self.calculator.pKa_from_Ka(-1e-5)
    
    def test_Kb_from_Ka(self):
        """Test Kb from Ka conversion."""
        Ka = 1.8e-5
        Kb = self.calculator.Kb_from_Ka(Ka)
        # Ka * Kb = Kw
        self.assertAlmostEqual(Ka * Kb, 1.0e-14, places=20)
    
    def test_Kb_from_Ka_invalid_input(self):
        """Test Kb from Ka with invalid input."""
        with self.assertRaises(ValueError):
            self.calculator.Kb_from_Ka(0)
        with self.assertRaises(ValueError):
            self.calculator.Kb_from_Ka(-1e-5)
    
    def test_Ka_from_Kb(self):
        """Test Ka from Kb conversion."""
        Kb = 1.8e-5
        Ka = self.calculator.Ka_from_Kb(Kb)
        # Ka * Kb = Kw
        self.assertAlmostEqual(Ka * Kb, 1.0e-14, places=20)
    
    def test_Ka_from_Kb_invalid_input(self):
        """Test Ka from Kb with invalid input."""
        with self.assertRaises(ValueError):
            self.calculator.Ka_from_Kb(0)
        with self.assertRaises(ValueError):
            self.calculator.Ka_from_Kb(-1e-5)
    
    def test_common_acids_constants(self):
        """Test that common acids have valid pKa values."""
        for key, acid in COMMON_ACIDS.items():
            self.assertIn('name', acid)
            self.assertIn('pKa', acid)
            self.assertIsInstance(acid['pKa'], (int, float))
            self.assertGreater(acid['pKa'], 0)
            self.assertLess(acid['pKa'], 14)
    
    def test_common_bases_constants(self):
        """Test that common bases have valid pKb values."""
        for key, base in COMMON_BASES.items():
            self.assertIn('name', base)
            self.assertIn('pKb', base)
            self.assertIsInstance(base['pKb'], (int, float))
            self.assertGreater(base['pKb'], 0)
            self.assertLess(base['pKb'], 14)


class TestIntegration(unittest.TestCase):
    """Integration tests for complete workflows."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.calculator = pHCalculator()
    
    def test_acetic_acid_buffer_workflow(self):
        """Test complete workflow for creating an acetic acid buffer."""
        # Step 1: Get pKa for acetic acid
        pKa = COMMON_ACIDS['acetic_acid']['pKa']
        self.assertEqual(pKa, 4.76)
        
        # Step 2: Design a buffer at pH 5.0
        target_pH = 5.0
        result = self.calculator.buffer_preparation(target_pH, pKa, 1.0, 0.2)
        
        # Step 3: Verify the calculated concentrations give the target pH
        calculated_pH = self.calculator.henderson_hasselbalch(
            pKa, result['acid_concentration'], result['base_concentration']
        )
        self.assertAlmostEqual(calculated_pH, target_pH, places=5)
    
    def test_ammonia_buffer_workflow(self):
        """Test workflow with ammonia buffer (using Kb)."""
        # Ammonia: pKb = 4.75
        pKb = COMMON_BASES['ammonia']['pKb']
        Kb = 10 ** (-pKb)
        
        # Convert to Ka for conjugate acid (NH4+)
        Ka = self.calculator.Ka_from_Kb(Kb)
        pKa = self.calculator.pKa_from_Ka(Ka)
        
        # pKa should be 14 - pKb = 9.25
        self.assertAlmostEqual(pKa, 14 - pKb, places=5)
        
        # Design buffer at pH 9.0
        result = self.calculator.buffer_preparation(9.0, pKa, 1.0, 0.1)
        
        # Verify
        calculated_pH = self.calculator.henderson_hasselbalch(
            pKa, result['acid_concentration'], result['base_concentration']
        )
        self.assertAlmostEqual(calculated_pH, 9.0, places=5)


if __name__ == '__main__':
    unittest.main()
