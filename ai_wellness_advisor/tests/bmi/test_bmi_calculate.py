import pytest
from ai_wellness_advisor.src.bmi.bmi_calculate import calculate_bmi # This import will fail until the source file is created

class TestBmiCalculate:
    def test_valid_input_normal_case(self):
        """AC1, AC2, AC6 - 正常情况"""
        assert calculate_bmi(height=1.75, weight=70) == 22.86

    def test_valid_input_different_values(self):
        """AC1, AC2, AC6 - 正常情况，不同数值"""
        assert calculate_bmi(height=1.60, weight=55.5) == 21.68

    def test_valid_input_needs_rounding(self):
        """AC1, AC2, AC6 - 边界情况，结果需四舍五入"""
        assert calculate_bmi(height=1.80, weight=60) == 18.52

    def test_valid_input_integer_values(self):
        """AC1, AC2, AC6 - 整数输入"""
        assert calculate_bmi(height=2, weight=80) == 20.00

    def test_invalid_height_zero(self):
        """AC3 - 无效身高：零"""
        with pytest.raises(ValueError, match="身高必须是有效的正数，单位为米。"):
            calculate_bmi(height=0, weight=70)

    def test_invalid_height_negative(self):
        """AC3 - 无效身高：负数"""
        with pytest.raises(ValueError, match="身高必须是有效的正数，单位为米。"):
            calculate_bmi(height=-1.75, weight=70)

    def test_invalid_weight_zero(self):
        """AC4 - 无效体重：零"""
        with pytest.raises(ValueError, match="体重必须是有效的正数，单位为千克。"):
            calculate_bmi(height=1.75, weight=0)

    def test_invalid_weight_negative(self):
        """AC4 - 无效体重：负数"""
        with pytest.raises(ValueError, match="体重必须是有效的正数，单位为千克。"):
            calculate_bmi(height=1.75, weight=-70)

    def test_invalid_height_takes_precedence(self):
        """AC5 - 无效身高优先于无效体重"""
        with pytest.raises(ValueError, match="身高必须是有效的正数，单位为米。"):
            calculate_bmi(height=0, weight=-70)

    # Optional: Test for non-numeric string inputs if the function is designed to handle them.
    # Based on S3, we assume type hints are met and focus on semantic validation of numbers.
    # If calculate_bmi itself tries float() conversion:
    # def test_invalid_height_string_non_convertible(self):
    #     with pytest.raises(ValueError, match="身高和体重必须是有效的数字。"):
    #         calculate_bmi(height="abc", weight=70)

    # def test_invalid_weight_string_non_convertible(self):
    #     with pytest.raises(ValueError, match="身高和体重必须是有效的数字。"):
    #         calculate_bmi(height=1.75, weight="xyz")

    # def test_invalid_height_string_zero_convertible(self):
    #     with pytest.raises(ValueError, match="身高必须是有效的正数，单位为米。"):
    #         calculate_bmi(height="0", weight=70)