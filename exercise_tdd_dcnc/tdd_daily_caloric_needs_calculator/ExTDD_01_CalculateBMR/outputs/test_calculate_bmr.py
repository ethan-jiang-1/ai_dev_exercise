"""基础代谢率(BMR)计算器的单元测试"""

import unittest
import time
from typing import Any
from calculate_bmr import (
    BMRCalculator,
    BMRValidationError,
    InvalidGenderError,
    InvalidAgeError,
    InvalidHeightError,
    InvalidWeightError,
)

class TestBMRCalculator(unittest.TestCase):
    """测试基础代谢率计算器"""

    def setUp(self):
        """测试前准备工作"""
        self.calculator = BMRCalculator()

    def test_validate_gender_valid(self):
        """测试有效的性别输入"""
        # 测试男性
        self.calculator.validate_gender("男")
        # 测试女性
        self.calculator.validate_gender("女")

    def test_validate_gender_invalid(self):
        """测试无效的性别输入"""
        invalid_genders = ["", "male", "female", "其他", 123, None]
        for gender in invalid_genders:
            with self.assertRaises(InvalidGenderError):
                self.calculator.validate_gender(gender)

    def test_validate_age_valid(self):
        """测试有效的年龄输入"""
        valid_ages = [15, 30, 50, 80]  # 包含边界值和正常值
        for age in valid_ages:
            self.calculator.validate_age(age)

    def test_validate_age_invalid_type(self):
        """测试无效类型的年龄输入"""
        invalid_ages = [25.5, "25", None, [25], {25}]
        for age in invalid_ages:
            with self.assertRaises(InvalidAgeError):
                self.calculator.validate_age(age)

    def test_validate_age_out_of_range(self):
        """测试超出范围的年龄输入"""
        invalid_ages = [14, 81, -1, 0, 100]
        for age in invalid_ages:
            with self.assertRaises(InvalidAgeError):
                self.calculator.validate_age(age)

    def test_validate_height_valid(self):
        """测试有效的身高输入"""
        valid_heights = [130, 175.5, 230]  # 包含边界值和正常值
        for height in valid_heights:
            self.calculator.validate_height(height)

    def test_validate_height_invalid_type(self):
        """测试无效类型的身高输入"""
        invalid_heights = ["175", None, [175], {175}]
        for height in invalid_heights:
            with self.assertRaises(InvalidHeightError):
                self.calculator.validate_height(height)

    def test_validate_height_out_of_range(self):
        """测试超出范围的身高输入"""
        invalid_heights = [129.9, 230.1, 0, -1, 300]
        for height in invalid_heights:
            with self.assertRaises(InvalidHeightError):
                self.calculator.validate_height(height)

    def test_validate_weight_valid(self):
        """测试有效的体重输入"""
        valid_weights = [30, 60.5, 150]  # 包含边界值和正常值
        for weight in valid_weights:
            self.calculator.validate_weight(weight)

    def test_validate_weight_invalid_type(self):
        """测试无效类型的体重输入"""
        invalid_weights = ["70", None, [70], {70}]
        for weight in invalid_weights:
            with self.assertRaises(InvalidWeightError):
                self.calculator.validate_weight(weight)

    def test_validate_weight_out_of_range(self):
        """测试超出范围的体重输入"""
        invalid_weights = [29.9, 150.1, 0, -1, 200]
        for weight in invalid_weights:
            with self.assertRaises(InvalidWeightError):
                self.calculator.validate_weight(weight)

    def test_calculate_bmr_male(self):
        """测试男性BMR计算"""
        # 测试用例：25岁，175cm，70kg的男性
        bmr = self.calculator.calculate("男", 25, 175.0, 70.0)
        # 只要小数点后一位的精度接近即可
        self.assertGreater(bmr, 1700)  # BMR应该大于1700
        self.assertLess(bmr, 1800)     # BMR应该小于1800
        self.assertEqual(len(str(bmr).split('.')[-1]), 1)  # 确保只有一位小数

    def test_calculate_bmr_female(self):
        """测试女性BMR计算"""
        # 测试用例：25岁，165cm，55kg的女性
        bmr = self.calculator.calculate("女", 25, 165.0, 55.0)
        # 只要小数点后一位的精度接近即可
        self.assertGreater(bmr, 1300)  # BMR应该大于1300
        self.assertLess(bmr, 1400)     # BMR应该小于1400
        self.assertEqual(len(str(bmr).split('.')[-1]), 1)  # 确保只有一位小数

    def test_boundary_values(self):
        """测试各个输入的边界值"""
        # 测试最小允许值
        bmr_min = self.calculator.calculate("男", 15, 130.0, 30.0)
        self.assertGreater(bmr_min, 0)

        # 测试最大允许值
        bmr_max = self.calculator.calculate("女", 80, 230.0, 150.0)
        self.assertGreater(bmr_max, 0)

    def test_result_precision(self):
        """测试计算结果精度"""
        bmr = self.calculator.calculate("男", 25, 175.0, 70.0)
        # 确保结果是浮点数
        self.assertIsInstance(bmr, float)
        # 确保只有一位小数
        self.assertEqual(len(str(bmr).split('.')[-1]), 1)

    def test_performance(self):
        """测试计算性能"""
        start_time = time.time()
        self.calculator.calculate("男", 25, 175.0, 70.0)
        end_time = time.time()
        
        # 确保计算时间不超过10ms
        self.assertLess(end_time - start_time, 0.01)

    def test_validate_inputs_all_valid(self):
        """测试所有输入都有效时的情况"""
        # 不应该抛出异常
        self.calculator.validate_inputs("男", 25, 175.0, 70.0)
        self.calculator.validate_inputs("女", 30, 165.0, 55.0)

    def test_validate_inputs_all_invalid(self):
        """测试所有输入都无效时的情况"""
        invalid_inputs = [
            ("other", -1, -1.0, -1.0),  # 全部无效
            (None, None, None, None),    # 全部None
            ("", 0, 0.0, 0.0),          # 全部空值或零
        ]
        for gender, age, height, weight in invalid_inputs:
            with self.assertRaises(BMRValidationError):
                self.calculator.validate_inputs(gender, age, height, weight)

if __name__ == '__main__':
    unittest.main() 