"""Tests for TDEE (Total Daily Energy Expenditure) calculation functionality.

This module contains comprehensive tests for the calculate_tdee function,
including normal cases, boundary values, error handling, and return type validation.
"""

import pytest
import math
from src.dcnc.calculate_tdee import calculate_tdee


class TestCalculateTDEENormalCases:
    """Test normal calculation cases for TDEE calculation."""
    
    def test_sedentary_activity(self):
        """Test TDEE calculation for sedentary activity level."""
        # Given: BMR=1500, sedentary activity
        bmr = 1500
        activity_level = "sedentary"
        
        # When: calculate TDEE
        result = calculate_tdee(bmr, activity_level)
        
        # Then: TDEE should be 1500 * 1.2 = 1800.0
        expected = 1800.0
        assert result == expected
    
    def test_lightly_active(self):
        """Test TDEE calculation for lightly active level."""
        # Given: BMR=1600, lightly active
        bmr = 1600
        activity_level = "lightly_active"
        
        # When: calculate TDEE
        result = calculate_tdee(bmr, activity_level)
        
        # Then: TDEE should be 1600 * 1.375 = 2200.0
        expected = 2200.0
        assert result == expected
    
    def test_moderately_active(self):
        """Test TDEE calculation for moderately active level."""
        # Given: BMR=1800, moderately active
        bmr = 1800
        activity_level = "moderately_active"
        
        # When: calculate TDEE
        result = calculate_tdee(bmr, activity_level)
        
        # Then: TDEE should be 1800 * 1.55 = 2790.0
        expected = 2790.0
        assert result == expected
    
    def test_very_active(self):
        """Test TDEE calculation for very active level."""
        # Given: BMR=2000, very active
        bmr = 2000
        activity_level = "very_active"
        
        # When: calculate TDEE
        result = calculate_tdee(bmr, activity_level)
        
        # Then: TDEE should be 2000 * 1.725 = 3450.0
        expected = 3450.0
        assert result == expected
    
    def test_extra_active(self):
        """Test TDEE calculation for extra active level."""
        # Given: BMR=2200, extra active
        bmr = 2200
        activity_level = "extra_active"
        
        # When: calculate TDEE
        result = calculate_tdee(bmr, activity_level)
        
        # Then: TDEE should be 2200 * 1.9 = 4180.0
        expected = 4180.0
        assert result == expected


class TestCalculateTDEEBoundaryValues:
    """Test boundary value cases for TDEE calculation."""
    
    def test_minimum_bmr(self):
        """Test TDEE calculation with minimum BMR value."""
        # Given: minimum BMR (500) with sedentary activity
        bmr = 500
        activity_level = "sedentary"
        
        # When: calculate TDEE
        result = calculate_tdee(bmr, activity_level)
        
        # Then: TDEE should be 500 * 1.2 = 600.0
        expected = 600.0
        assert result == expected
    
    def test_maximum_bmr(self):
        """Test TDEE calculation with maximum BMR value."""
        # Given: maximum BMR (5000) with extra active
        bmr = 5000
        activity_level = "extra_active"
        
        # When: calculate TDEE
        result = calculate_tdee(bmr, activity_level)
        
        # Then: TDEE should be 5000 * 1.9 = 9500.0
        expected = 9500.0
        assert result == expected


class TestCalculateTDEECaseInsensitive:
    """Test case insensitive activity level handling."""
    
    def test_uppercase_activity_level(self):
        """Test TDEE calculation with uppercase activity level."""
        # Given: BMR=1500, uppercase activity level
        bmr = 1500
        activity_level = "SEDENTARY"
        
        # When: calculate TDEE
        result = calculate_tdee(bmr, activity_level)
        
        # Then: should work same as lowercase
        expected = 1800.0
        assert result == expected
    
    def test_mixed_case_activity_level(self):
        """Test TDEE calculation with mixed case activity level."""
        # Given: BMR=1600, mixed case activity level
        bmr = 1600
        activity_level = "Lightly_Active"
        
        # When: calculate TDEE
        result = calculate_tdee(bmr, activity_level)
        
        # Then: should work same as lowercase
        expected = 2200.0
        assert result == expected
    
    def test_activity_level_with_spaces(self):
        """Test TDEE calculation with activity level containing spaces."""
        # Given: BMR=1800, activity level with spaces
        bmr = 1800
        activity_level = " moderately_active "
        
        # When: calculate TDEE
        result = calculate_tdee(bmr, activity_level)
        
        # Then: should work same as trimmed lowercase
        expected = 2790.0
        assert result == expected


class TestCalculateTDEETypeErrors:
    """Test type error cases for TDEE calculation."""
    
    def test_bmr_string_type(self):
        """Test TypeError when BMR is string."""
        with pytest.raises(TypeError, match="bmr must be int or float, got str"):
            calculate_tdee("1500", "sedentary")
    
    def test_bmr_none_type(self):
        """Test TypeError when BMR is None."""
        with pytest.raises(TypeError, match="bmr must be int or float, got NoneType"):
            calculate_tdee(None, "sedentary")
    
    def test_bmr_list_type(self):
        """Test TypeError when BMR is list."""
        with pytest.raises(TypeError, match="bmr must be int or float, got list"):
            calculate_tdee([1500], "sedentary")
    
    def test_activity_level_numeric_type(self):
        """Test TypeError when activity_level is numeric."""
        with pytest.raises(TypeError, match="activity_level must be str, got float"):
            calculate_tdee(1500, 1.2)
    
    def test_activity_level_none_type(self):
        """Test TypeError when activity_level is None."""
        with pytest.raises(TypeError, match="activity_level must be str, got NoneType"):
            calculate_tdee(1500, None)
    
    def test_activity_level_list_type(self):
        """Test TypeError when activity_level is list."""
        with pytest.raises(TypeError, match="activity_level must be str, got list"):
            calculate_tdee(1500, ["sedentary"])


class TestCalculateTDEEValueErrors:
    """Test value error cases for TDEE calculation."""
    
    def test_bmr_too_low(self):
        """Test ValueError when BMR is below minimum."""
        with pytest.raises(ValueError, match="bmr must be between 500 and 5000, got 400"):
            calculate_tdee(400, "sedentary")
    
    def test_bmr_too_high(self):
        """Test ValueError when BMR is above maximum."""
        with pytest.raises(ValueError, match="bmr must be between 500 and 5000, got 6000"):
            calculate_tdee(6000, "sedentary")
    
    def test_bmr_zero(self):
        """Test ValueError when BMR is zero."""
        with pytest.raises(ValueError, match="bmr must be between 500 and 5000, got 0"):
            calculate_tdee(0, "sedentary")
    
    def test_bmr_negative(self):
        """Test ValueError when BMR is negative."""
        with pytest.raises(ValueError, match="bmr must be between 500 and 5000, got -100"):
            calculate_tdee(-100, "sedentary")
    
    def test_bmr_nan(self):
        """Test ValueError when BMR is NaN."""
        with pytest.raises(ValueError, match="bmr must be a finite number, got nan"):
            calculate_tdee(float('nan'), "sedentary")
    
    def test_bmr_infinity(self):
        """Test ValueError when BMR is infinity."""
        with pytest.raises(ValueError, match="bmr must be a finite number, got inf"):
            calculate_tdee(float('inf'), "sedentary")
    
    def test_invalid_activity_level(self):
        """Test ValueError when activity_level is invalid."""
        with pytest.raises(ValueError, match="activity_level must be one of"):
            calculate_tdee(1500, "invalid_level")
    
    def test_empty_activity_level(self):
        """Test ValueError when activity_level is empty string."""
        with pytest.raises(ValueError, match="activity_level must be one of"):
            calculate_tdee(1500, "")
    
    def test_activity_level_with_typo(self):
        """Test ValueError when activity_level has typo."""
        with pytest.raises(ValueError, match="activity_level must be one of"):
            calculate_tdee(1500, "sedantary")  # typo in sedentary


class TestCalculateTDEEReturnType:
    """Test return type and precision for TDEE calculation."""
    
    def test_return_type_is_float(self):
        """Test that calculate_tdee returns float type."""
        result = calculate_tdee(1500, "sedentary")
        assert isinstance(result, float)
    
    def test_result_precision_one_decimal(self):
        """Test that result is rounded to 1 decimal place."""
        # Given: BMR that will produce decimal result
        bmr = 1333  # 1333 * 1.375 = 1832.875
        activity_level = "lightly_active"
        
        # When: calculate TDEE
        result = calculate_tdee(bmr, activity_level)
        
        # Then: should be rounded to 1 decimal place
        expected = 1832.9  # 1832.875 rounded to 1 decimal
        assert result == expected
    
    def test_result_is_positive(self):
        """Test that TDEE result is always positive."""
        result = calculate_tdee(500, "sedentary")
        assert result > 0
    
    def test_integer_bmr_returns_float(self):
        """Test that integer BMR input still returns float."""
        result = calculate_tdee(1500, "sedentary")  # integer BMR
        assert isinstance(result, float)
        assert result == 1800.0
    
    def test_float_bmr_precision(self):
        """Test precision with float BMR input."""
        result = calculate_tdee(1500.5, "sedentary")  # 1500.5 * 1.2 = 1800.6
        assert result == 1800.6


class TestCalculateTDEEIntegration:
    """Integration tests for TDEE calculation with various combinations."""
    
    def test_all_activity_levels_with_same_bmr(self):
        """Test all activity levels with the same BMR for consistency."""
        bmr = 2000
        expected_results = {
            "sedentary": 2400.0,        # 2000 * 1.2
            "lightly_active": 2750.0,   # 2000 * 1.375
            "moderately_active": 3100.0, # 2000 * 1.55
            "very_active": 3450.0,      # 2000 * 1.725
            "extra_active": 3800.0      # 2000 * 1.9
        }
        
        for activity_level, expected in expected_results.items():
            result = calculate_tdee(bmr, activity_level)
            assert result == expected, f"Failed for {activity_level}"
    
    def test_tdee_increases_with_activity_level(self):
        """Test that TDEE increases as activity level increases."""
        bmr = 1800
        activity_levels = ["sedentary", "lightly_active", "moderately_active", 
                          "very_active", "extra_active"]
        
        results = []
        for level in activity_levels:
            result = calculate_tdee(bmr, level)
            results.append(result)
        
        # Verify that each result is greater than the previous
        for i in range(1, len(results)):
            assert results[i] > results[i-1], f"TDEE should increase from {activity_levels[i-1]} to {activity_levels[i]}"
    
    def test_tdee_scales_with_bmr(self):
        """Test that TDEE scales proportionally with BMR."""
        activity_level = "moderately_active"
        coefficient = 1.55
        
        test_bmrs = [1000, 1500, 2000, 2500, 3000]
        
        for bmr in test_bmrs:
            result = calculate_tdee(bmr, activity_level)
            expected = bmr * coefficient
            assert result == expected, f"TDEE should be {expected} for BMR {bmr}"