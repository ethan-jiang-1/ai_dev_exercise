import pytest
from bmi_calculate_v2 import (
    convert_height_to_meters,
    convert_weight_to_kg,
    bmi_calculate,
    HEIGHT_UNIT_METERS,
    HEIGHT_UNIT_FT_IN,
    WEIGHT_UNIT_KG,
    WEIGHT_UNIT_LB
)

class TestHeightConversion:
    """身高单位转换测试类"""

    def test_height_meters_direct(self):
        """测试米单位直接转换"""
        cases = [
            (1.75, 1.75),    # 常规身高
            (0.1, 0.1),      # 最小有效值
            (3.0, 3.0),      # 最大有效值
            (2, 2.0),        # 整数输入
            (1.685, 1.685)   # 精确小数
        ]
        for input_height, expected in cases:
            result = convert_height_to_meters(input_height, HEIGHT_UNIT_METERS)
            assert abs(result - expected) < 0.01

    def test_height_feet_inches(self):
        """测试英尺/英寸转换"""
        cases = [
            ((5, 9), 1.75),    # 5英尺9英寸 ≈ 1.75米
            ((6, 0), 1.83),    # 6英尺 ≈ 1.83米
            ((4, 0), 1.22),    # 4英尺 ≈ 1.22米
            ((5, 11.5), 1.82), # 带小数的英寸
            ((1, 0), 0.30),    # 最小边界
            ((10, 0), 3.05)    # 最大边界
        ]
        for (feet, inches), expected in cases:
            result = convert_height_to_meters((feet, inches), HEIGHT_UNIT_FT_IN)
            assert abs(result - expected) < 0.01

    def test_height_type_errors(self):
        """测试身高转换的类型错误"""
        error_cases = [
            (None, HEIGHT_UNIT_METERS),
            (True, HEIGHT_UNIT_METERS),
            ("170", HEIGHT_UNIT_METERS),
            (1.75, None),
            (1.75, True),
            (1.75, 123)
        ]
        for height, unit in error_cases:
            with pytest.raises(TypeError):
                convert_height_to_meters(height, unit)

    def test_height_value_errors(self):
        """测试身高转换的值错误"""
        error_cases = [
            # 米单位错误
            (0, HEIGHT_UNIT_METERS),
            (-1.75, HEIGHT_UNIT_METERS),
            (3.1, HEIGHT_UNIT_METERS),
            
            # 英尺/英寸单位错误
            ((0, 5), HEIGHT_UNIT_FT_IN),
            ((11, 0), HEIGHT_UNIT_FT_IN),
            ((5, 12), HEIGHT_UNIT_FT_IN),
            ((5, -1), HEIGHT_UNIT_FT_IN),
            
            # 无效单位
            (1.75, "invalid")
        ]
        for height, unit in error_cases:
            with pytest.raises(ValueError):
                convert_height_to_meters(height, unit)

    def test_height_tuple_validation(self):
        """测试英尺/英寸元组验证"""
        invalid_tuples = [
            (1,),           # 单元素元组
            (5, 9, 2),      # 三元素元组
            ([5, 9],),      # 列表
            ((5,),),        # 嵌套元组
            ("5", "9")      # 字符串元组
        ]
        for invalid_tuple in invalid_tuples:
            with pytest.raises((TypeError, ValueError)):
                convert_height_to_meters(invalid_tuple, HEIGHT_UNIT_FT_IN)


class TestWeightConversion:
    """体重单位转换测试类"""

    def test_weight_kg_direct(self):
        """测试千克单位直接转换"""
        cases = [
            (70, 70),        # 常规体重
            (0.1, 0.1),      # 最小有效值
            (300, 300),      # 最大有效值
            (65.5, 65.5),    # 小数值
            (100, 100)       # 整数值
        ]
        for input_weight, expected in cases:
            result = convert_weight_to_kg(input_weight, WEIGHT_UNIT_KG)
            assert abs(result - expected) < 0.01

    def test_weight_pounds(self):
        """测试磅转换为千克"""
        cases = [
            (154, 69.85),    # 154磅 ≈ 69.85千克
            (220, 99.79),    # 220磅 ≈ 99.79千克
            (110.5, 50.12),  # 带小数的磅值
            (0.5, 0.23),     # 最小边界
            (660, 299.37)    # 最大边界
        ]
        for input_pounds, expected_kg in cases:
            result = convert_weight_to_kg(input_pounds, WEIGHT_UNIT_LB)
            assert abs(result - expected_kg) < 0.01

    def test_weight_type_errors(self):
        """测试体重转换的类型错误"""
        error_cases = [
            (None, WEIGHT_UNIT_KG),
            (True, WEIGHT_UNIT_KG),
            ("70", WEIGHT_UNIT_KG),
            (70, None),
            (70, True),
            (70, 123)
        ]
        for weight, unit in error_cases:
            with pytest.raises(TypeError):
                convert_weight_to_kg(weight, unit)

    def test_weight_value_errors(self):
        """测试体重转换的值错误"""
        error_cases = [
            # 千克单位错误
            (0, WEIGHT_UNIT_KG),
            (-70, WEIGHT_UNIT_KG),
            (301, WEIGHT_UNIT_KG),
            
            # 磅单位错误
            (0, WEIGHT_UNIT_LB),
            (-154, WEIGHT_UNIT_LB),
            (661, WEIGHT_UNIT_LB),
            
            # 无效单位
            (70, "invalid")
        ]
        for weight, unit in error_cases:
            with pytest.raises(ValueError):
                convert_weight_to_kg(weight, unit)


class TestBMICalculationIntegration:
    """BMI 计算集成测试类"""

    def test_bmi_calculation_with_different_units(self):
        """测试不同单位组合的 BMI 计算"""
        test_cases = [
            # (身高, 身高单位, 体重, 体重单位, 期望BMI)
            (1.75, HEIGHT_UNIT_METERS, 70, WEIGHT_UNIT_KG, 22.86),          # 全公制
            ((5, 9), HEIGHT_UNIT_FT_IN, 154, WEIGHT_UNIT_LB, 22.74),       # 全英制
            (1.75, HEIGHT_UNIT_METERS, 154, WEIGHT_UNIT_LB, 22.81),         # 混合单位1
            ((5, 9), HEIGHT_UNIT_FT_IN, 70, WEIGHT_UNIT_KG, 22.79)         # 混合单位2 - 更新期望值
        ]
        
        for height, height_unit, weight, weight_unit, expected_bmi in test_cases:
            # 转换单位
            height_m = convert_height_to_meters(height, height_unit)
            weight_kg = convert_weight_to_kg(weight, weight_unit)
            
            # 打印调试信息
            print(f"\n测试用例: {height} {height_unit}, {weight} {weight_unit}")
            print(f"转换后: 身高 = {height_m}m, 体重 = {weight_kg}kg")
            
            # 计算 BMI
            bmi = bmi_calculate(height_m, weight_kg)
            print(f"计算得到 BMI = {bmi}, 期望 BMI = {expected_bmi}")
            
            # 验证结果
            assert abs(bmi - expected_bmi) < 0.01

    def test_extreme_combinations(self):
        """测试极端组合情况"""
        test_cases = [
            # 最小有效值组合 - BMI应该在合理范围内
            ((4, 0), HEIGHT_UNIT_FT_IN, 44, WEIGHT_UNIT_LB),  # 约1.22m, 20kg -> BMI ≈ 13.4
            # 最大有效值组合 - BMI应该在合理范围内
            ((6, 0), HEIGHT_UNIT_FT_IN, 220, WEIGHT_UNIT_LB),  # 约1.83m, 100kg -> BMI ≈ 29.8
            # 混合单位 - 合理范围
            (1.5, HEIGHT_UNIT_METERS, 110, WEIGHT_UNIT_LB),    # 1.5m, 50kg -> BMI ≈ 22.2
            (2.0, HEIGHT_UNIT_METERS, 176, WEIGHT_UNIT_LB)     # 2.0m, 80kg -> BMI ≈ 20.0
        ]
        
        for height, height_unit, weight, weight_unit in test_cases:
            # 转换单位
            height_m = convert_height_to_meters(height, height_unit)
            weight_kg = convert_weight_to_kg(weight, weight_unit)
            
            # 计算 BMI
            bmi = bmi_calculate(height_m, weight_kg)
            
            # 验证 BMI 在合理范围内 (1-100)
            assert 1 <= bmi <= 100 