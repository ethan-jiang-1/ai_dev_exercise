import pytest
from bmi_calculate_v2 import (
    convert_height_to_meters, convert_weight_to_kg, bmi_calculate,
    HEIGHT_UNIT_METERS, HEIGHT_UNIT_FT_IN,
    WEIGHT_UNIT_KG, WEIGHT_UNIT_LB
)

class TestHeightConversion:
    """身高单位转换测试"""
    
    def test_height_meters_direct(self):
        """测试米单位直接转换"""
        cases = [
            (1.75, 1.75),  # 正常值
            (1.0, 1.0),   # 最小边界
            (3.0, 3.0)    # 最大边界
        ]
        for input_height, expected in cases:
            result = convert_height_to_meters(input_height, HEIGHT_UNIT_METERS)
            assert abs(result - expected) < 0.0001
    
    def test_height_feet_inches(self):
        """测试英尺/英寸转换"""
        cases = [
            ((5, 9), 1.75),    # 5英尺9英寸 ≈ 1.75米
            ((6, 0), 1.83),    # 6英尺 ≈ 1.83米
            ((4, 0), 1.22),    # 4英尺 ≈ 1.22米
            ((5, 11.5), 1.82), # 带小数的英寸
            ((1, 0), 0.30),    # 最小边界
            ((10, 0), 3.048)   # 最大边界
        ]
        for (feet, inches), expected in cases:
            result = convert_height_to_meters((feet, inches), HEIGHT_UNIT_FT_IN)
            assert abs(result - expected) < 0.0001
    
    def test_height_type_errors(self):
        """测试类型错误"""
        with pytest.raises(TypeError):
            convert_height_to_meters(True, HEIGHT_UNIT_METERS)  # 布尔值
        with pytest.raises(TypeError):
            convert_height_to_meters("170", HEIGHT_UNIT_METERS)  # 字符串
        with pytest.raises(TypeError):
            convert_height_to_meters([170], HEIGHT_UNIT_METERS)  # 列表
        with pytest.raises(TypeError):
            convert_height_to_meters((5,), HEIGHT_UNIT_FT_IN)  # 单元素元组
        with pytest.raises(TypeError):
            convert_height_to_meters((5, "9"), HEIGHT_UNIT_FT_IN)  # 元组中含字符串
    
    def test_height_value_errors(self):
        """测试数值错误"""
        with pytest.raises(ValueError):
            convert_height_to_meters(0, HEIGHT_UNIT_METERS)  # 零值
        with pytest.raises(ValueError):
            convert_height_to_meters(-1.7, HEIGHT_UNIT_METERS)  # 负值
        with pytest.raises(ValueError):
            convert_height_to_meters(3.5, HEIGHT_UNIT_METERS)  # 超过最大值
        with pytest.raises(ValueError):
            convert_height_to_meters((0, 0), HEIGHT_UNIT_FT_IN)  # 零英尺
        with pytest.raises(ValueError):
            convert_height_to_meters((11, 0), HEIGHT_UNIT_FT_IN)  # 超过最大英尺
    
    def test_height_tuple_validation(self):
        """测试英尺/英寸元组验证"""
        with pytest.raises(ValueError):
            convert_height_to_meters((5, -1), HEIGHT_UNIT_FT_IN)  # 负英寸
        with pytest.raises(ValueError):
            convert_height_to_meters((5, 12), HEIGHT_UNIT_FT_IN)  # 英寸超过11
        with pytest.raises(TypeError):
            convert_height_to_meters((5, 9, 2), HEIGHT_UNIT_FT_IN)  # 元组元素过多

class TestWeightConversion:
    """体重单位转换测试"""
    
    def test_weight_kg_direct(self):
        """测试千克单位直接转换"""
        cases = [
            (70, 70),    # 正常值
            (0.5, 0.5),  # 最小边界
            (300, 300)   # 最大边界
        ]
        for input_weight, expected in cases:
            result = convert_weight_to_kg(input_weight, WEIGHT_UNIT_KG)
            assert abs(result - expected) < 0.0001
    
    def test_weight_pounds(self):
        """测试磅转换"""
        cases = [
            (154, 69.8533),  # 正常值
            (1, 0.4536),     # 小值
            (220, 99.7903),  # 大值
            (0.5, 0.2268),   # 最小边界
            (660, 299.3711)  # 最大边界
        ]
        for input_weight, expected in cases:
            result = convert_weight_to_kg(input_weight, WEIGHT_UNIT_LB)
            assert abs(result - expected) < 0.0001
    
    def test_weight_type_errors(self):
        """测试类型错误"""
        with pytest.raises(TypeError):
            convert_weight_to_kg(True, WEIGHT_UNIT_KG)  # 布尔值
        with pytest.raises(TypeError):
            convert_weight_to_kg("70", WEIGHT_UNIT_KG)  # 字符串
        with pytest.raises(TypeError):
            convert_weight_to_kg([70], WEIGHT_UNIT_KG)  # 列表
    
    def test_weight_value_errors(self):
        """测试数值错误"""
        with pytest.raises(ValueError):
            convert_weight_to_kg(0, WEIGHT_UNIT_KG)  # 零值
        with pytest.raises(ValueError):
            convert_weight_to_kg(-70, WEIGHT_UNIT_KG)  # 负值
        with pytest.raises(ValueError):
            convert_weight_to_kg(301, WEIGHT_UNIT_KG)  # 超过最大值
        with pytest.raises(ValueError):
            convert_weight_to_kg(0, WEIGHT_UNIT_LB)  # 零磅
        with pytest.raises(ValueError):
            convert_weight_to_kg(661, WEIGHT_UNIT_LB)  # 超过最大磅

class TestBMICalculationIntegration:
    """BMI 计算集成测试"""
    
    def test_bmi_calculation_with_different_units(self):
        """测试不同单位组合的 BMI 计算"""
        test_cases = [
            # (身高, 身高单位, 体重, 体重单位, 期望BMI)
            (1.75, HEIGHT_UNIT_METERS, 70, WEIGHT_UNIT_KG, 22.86),          # 全公制
            ((5, 9), HEIGHT_UNIT_FT_IN, 154, WEIGHT_UNIT_LB, 22.74),   # 全英制（等价于上面的公制值）
            (1.75, HEIGHT_UNIT_METERS, 154, WEIGHT_UNIT_LB, 22.74),         # 混合单位1
            ((5, 9), HEIGHT_UNIT_FT_IN, 70, WEIGHT_UNIT_KG, 22.74)     # 混合单位2
        ]
        
        for height, height_unit, weight, weight_unit, expected_bmi in test_cases:
            # 转换单位
            height_m = convert_height_to_meters(height, height_unit)
            weight_kg = convert_weight_to_kg(weight, weight_unit)
            
            # 计算 BMI
            bmi = bmi_calculate(height_m, weight_kg)
            
            # 验证结果
            assert abs(bmi - expected_bmi) < 0.01
    
    def test_extreme_combinations(self):
        """测试极端组合情况"""
        test_cases = [
            # 最小有效值组合
            ((1, 0), HEIGHT_UNIT_FT_IN, 0.5, WEIGHT_UNIT_LB),
            # 最大有效值组合
            ((10, 0), HEIGHT_UNIT_FT_IN, 660, WEIGHT_UNIT_LB),
            # 混合极值
            (0.1, HEIGHT_UNIT_METERS, 660, WEIGHT_UNIT_LB),
            (3.048, HEIGHT_UNIT_METERS, 0.5, WEIGHT_UNIT_LB)
        ]
        
        for height, height_unit, weight, weight_unit in test_cases:
            # 验证转换不抛出异常
            height_m = convert_height_to_meters(height, height_unit)
            weight_kg = convert_weight_to_kg(weight, weight_unit)
            
            # 验证 BMI 计算不抛出异常
            bmi_calculate(height_m, weight_kg) 