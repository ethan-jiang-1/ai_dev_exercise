"""Tests for calculate_bmr function.

This module contains comprehensive test cases for the BMR (Basal Metabolic Rate) calculation function,
following TDD principles.
"""

import pytest
from src.dcnc.calculate_bmr import calculate_bmr


class TestCalculateBMRNormalCases:
    """Test normal calculation cases for BMR."""
    
    def test_male_bmr_standard_case(self):
        """Test BMR calculation for standard adult male."""
        # Given: 30-year-old male, 175cm, 70kg
        gender = "male"
        age = 30
        height = 175
        weight = 70
        
        # When: calculate BMR
        result = calculate_bmr(gender, age, height, weight)
        
        # Then: BMR should be approximately 1695.7 calories/day
        expected = 1695.7
        assert result == expected
    
    def test_male_bmr_tall_heavy(self):
        """Test BMR calculation for tall, heavy male."""
        # Given: 25-year-old male, 180cm, 80kg
        gender = "male"
        age = 25
        height = 180
        weight = 80
        
        # When: calculate BMR
        result = calculate_bmr(gender, age, height, weight)
        
        # Then: BMR should be approximately 1882.0 calories/day
        expected = 1882.0
        assert result == expected
    
    def test_female_bmr_standard_case(self):
        """Test BMR calculation for standard adult female."""
        # Given: 25-year-old female, 160cm, 55kg
        gender = "female"
        age = 25
        height = 160
        weight = 55
        
        # When: calculate BMR
        result = calculate_bmr(gender, age, height, weight)
        
        # Then: BMR should be approximately 1343.6 calories/day
        expected = 1343.6
        assert result == expected
    
    def test_female_bmr_older_heavier(self):
        """Test BMR calculation for older, heavier female."""
        # Given: 35-year-old female, 165cm, 65kg
        gender = "female"
        age = 35
        height = 165
        weight = 65
        
        # When: calculate BMR
        result = calculate_bmr(gender, age, height, weight)
        
        # Then: BMR should be approximately 1408.3 calories/day
        expected = 1408.3
        assert result == expected


class TestCalculateBMRBoundaryValues:
    """Test boundary value cases for BMR calculation."""
    
    def test_minimum_age(self):
        """Test BMR calculation with minimum age (1 year)."""
        result = calculate_bmr("male", 1, 100, 20)
        assert isinstance(result, float)
        assert result > 0
    
    def test_maximum_age(self):
        """Test BMR calculation with maximum age (120 years)."""
        result = calculate_bmr("female", 120, 150, 50)
        assert isinstance(result, float)
        assert result > 0
    
    def test_minimum_height(self):
        """Test BMR calculation with minimum height (50cm)."""
        result = calculate_bmr("male", 30, 50, 30)
        assert isinstance(result, float)
        assert result > 0
    
    def test_maximum_height(self):
        """Test BMR calculation with maximum height (300cm)."""
        result = calculate_bmr("female", 30, 300, 100)
        assert isinstance(result, float)
        assert result > 0
    
    def test_minimum_weight(self):
        """Test BMR calculation with minimum weight (10kg)."""
        result = calculate_bmr("male", 30, 150, 10)
        assert isinstance(result, float)
        assert result > 0
    
    def test_maximum_weight(self):
        """Test BMR calculation with maximum weight (500kg)."""
        result = calculate_bmr("female", 30, 170, 500)
        assert isinstance(result, float)
        assert result > 0


class TestCalculateBMRGenderCaseInsensitive:
    """Test gender parameter case insensitivity."""
    
    def test_male_uppercase(self):
        """Test BMR calculation with uppercase 'MALE'."""
        result = calculate_bmr("MALE", 30, 175, 70)
        expected = calculate_bmr("male", 30, 175, 70)
        assert result == expected
    
    def test_female_mixed_case(self):
        """Test BMR calculation with mixed case 'Female'."""
        result = calculate_bmr("Female", 25, 160, 55)
        expected = calculate_bmr("female", 25, 160, 55)
        assert result == expected


class TestCalculateBMRTypeErrors:
    """Test type error cases for BMR calculation."""
    
    def test_gender_not_string(self):
        """Test TypeError when gender is not a string."""
        with pytest.raises(TypeError, match="gender must be str, got int"):
            calculate_bmr(123, 30, 175, 70)
    
    def test_age_not_integer(self):
        """Test TypeError when age is not an integer."""
        with pytest.raises(TypeError, match="age must be int, got str"):
            calculate_bmr("male", "30", 175, 70)
    
    def test_height_not_numeric(self):
        """Test TypeError when height is not numeric."""
        with pytest.raises(TypeError, match="height must be int or float, got str"):
            calculate_bmr("male", 30, "175", 70)
    
    def test_weight_not_numeric(self):
        """Test TypeError when weight is not numeric."""
        with pytest.raises(TypeError, match="weight must be int or float, got str"):
            calculate_bmr("male", 30, 175, "70")


class TestCalculateBMRValueErrors:
    """Test value error cases for BMR calculation."""
    
    def test_invalid_gender_value(self):
        """Test ValueError when gender is invalid."""
        with pytest.raises(ValueError, match="gender must be 'male' or 'female', got 'unknown'"):
            calculate_bmr("unknown", 30, 175, 70)
    
    def test_age_too_low(self):
        """Test ValueError when age is below minimum."""
        with pytest.raises(ValueError, match="age must be between 1 and 120, got 0"):
            calculate_bmr("male", 0, 175, 70)
    
    def test_age_too_high(self):
        """Test ValueError when age is above maximum."""
        with pytest.raises(ValueError, match="age must be between 1 and 120, got 150"):
            calculate_bmr("male", 150, 175, 70)
    
    def test_height_too_low(self):
        """Test ValueError when height is below minimum."""
        with pytest.raises(ValueError, match="height must be between 50 and 300 cm, got 30"):
            calculate_bmr("male", 30, 30, 70)
    
    def test_height_too_high(self):
        """Test ValueError when height is above maximum."""
        with pytest.raises(ValueError, match="height must be between 50 and 300 cm, got 350"):
            calculate_bmr("male", 30, 350, 70)
    
    def test_weight_too_low(self):
        """Test ValueError when weight is below minimum."""
        with pytest.raises(ValueError, match="weight must be between 10 and 500 kg, got 5"):
            calculate_bmr("male", 30, 175, 5)
    
    def test_weight_too_high(self):
        """Test ValueError when weight is above maximum."""
        with pytest.raises(ValueError, match="weight must be between 10 and 500 kg, got 600"):
            calculate_bmr("male", 30, 175, 600)
    
    def test_negative_age(self):
        """Test ValueError when age is negative."""
        with pytest.raises(ValueError, match="age must be between 1 and 120, got -5"):
            calculate_bmr("male", -5, 175, 70)
    
    def test_negative_height(self):
        """Test ValueError when height is negative."""
        with pytest.raises(ValueError, match="height must be between 50 and 300 cm, got -175"):
            calculate_bmr("male", 30, -175, 70)
    
    def test_negative_weight(self):
        """Test ValueError when weight is negative."""
        with pytest.raises(ValueError, match="weight must be between 10 and 500 kg, got -70"):
            calculate_bmr("male", 30, 175, -70)


class TestCalculateBMRReturnType:
    """Test return type and precision of BMR calculation."""
    
    def test_return_type_is_float(self):
        """Test that BMR calculation returns a float."""
        result = calculate_bmr("male", 30, 175, 70)
        assert isinstance(result, float)
    
    def test_result_precision_one_decimal(self):
        """Test that BMR result is rounded to 1 decimal place."""
        result = calculate_bmr("male", 30, 175, 70)
        # Check that result has at most 1 decimal place
        assert result == round(result, 1)
    
    def test_result_is_positive(self):
        """Test that BMR result is always positive."""
        result = calculate_bmr("female", 1, 50, 10)  # Minimum values
        assert result > 0