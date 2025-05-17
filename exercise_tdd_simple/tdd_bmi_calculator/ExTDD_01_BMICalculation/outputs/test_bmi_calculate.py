import unittest
from bmi_calculate import bmi_calculate

class TestBMICalculate(unittest.TestCase):
    """BMI 计算函数的测试类"""

    def test_normal_weight_height(self):
        """测试正常体重和身高的情况"""
        # 身高 1.75 米，体重 70 千克，预期 BMI 约为 22.86
        result = bmi_calculate(1.75, 70)
        self.assertEqual(result, 22.86)

    def test_integer_inputs(self):
        """测试整数输入的情况"""
        # 身高 2 米，体重 80 千克，预期 BMI 为 20.00
        result = bmi_calculate(2, 80)
        self.assertEqual(result, 20.00)

    def test_decimal_inputs(self):
        """测试小数输入的情况"""
        # 身高 1.68 米，体重 58.5 千克，预期 BMI 约为 20.73
        result = bmi_calculate(1.68, 58.5)
        self.assertEqual(result, 20.73)

    def test_very_small_valid_values(self):
        """测试极小的有效值"""
        # 身高 0.1 米，体重 0.1 千克，确保计算正确
        result = bmi_calculate(0.1, 0.1)
        self.assertEqual(result, 10.00)

    def test_very_large_valid_values(self):
        """测试较大的有效值"""
        # 身高 3 米，体重 300 千克
        result = bmi_calculate(3, 300)
        self.assertEqual(result, 33.33)

    def test_type_error_string_input(self):
        """测试字符串输入"""
        with self.assertRaises(TypeError) as context:
            bmi_calculate("170", "60")
        self.assertIn("数字类型", str(context.exception))

    def test_type_error_none_input(self):
        """测试 None 输入"""
        with self.assertRaises(TypeError) as context:
            bmi_calculate(None, None)
        self.assertIn("数字类型", str(context.exception))

    def test_type_error_boolean_input(self):
        """测试布尔值输入"""
        with self.assertRaises(TypeError) as context:
            bmi_calculate(True, False)
        self.assertIn("数字类型", str(context.exception))

    def test_value_error_zero_input(self):
        """测试零值输入"""
        with self.assertRaises(ValueError) as context:
            bmi_calculate(0, 70)
        self.assertIn("身高必须大于0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            bmi_calculate(1.75, 0)
        self.assertIn("体重必须大于0", str(context.exception))

    def test_value_error_negative_input(self):
        """测试负值输入"""
        with self.assertRaises(ValueError) as context:
            bmi_calculate(-1.75, 70)
        self.assertIn("身高必须大于0", str(context.exception))

        with self.assertRaises(ValueError) as context:
            bmi_calculate(1.75, -70)
        self.assertIn("体重必须大于0", str(context.exception))

if __name__ == '__main__':
    unittest.main() 