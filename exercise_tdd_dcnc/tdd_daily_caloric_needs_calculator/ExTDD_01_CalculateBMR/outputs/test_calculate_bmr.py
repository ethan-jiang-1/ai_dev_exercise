"""
基础代谢率(BMR)计算器测试模块
"""
import pytest
from calculate_bmr import PersonData, BMRInputError, validate_person_data, calculate_bmr

class TestPersonData:
    """PersonData类测试"""
    
    def test_person_data_creation_valid(self):
        """测试使用有效数据创建PersonData实例"""
        person = PersonData(gender="男", age=25, height=175.0, weight=70.0)
        assert person.gender == "男"
        assert person.age == 25
        assert person.height == 175.0
        assert person.weight == 70.0

class TestDataValidation:
    """数据验证功能测试"""
    
    def test_validate_gender_valid(self):
        """测试有效性别验证"""
        person_male = PersonData(gender="男", age=25, height=175.0, weight=70.0)
        person_female = PersonData(gender="女", age=25, height=175.0, weight=70.0)
        
        # 不应抛出异常
        validate_person_data(person_male)
        validate_person_data(person_female)
    
    def test_validate_gender_invalid(self):
        """测试无效性别验证"""
        person = PersonData(gender="其他", age=25, height=175.0, weight=70.0)
        with pytest.raises(BMRInputError, match="性别必须是'男'或'女'"):
            validate_person_data(person)
    
    def test_validate_age_valid(self):
        """测试有效年龄验证"""
        # 测试边界值
        ages = [0, 1, 119, 120]
        for age in ages:
            person = PersonData(gender="男", age=age, height=175.0, weight=70.0)
            validate_person_data(person)  # 不应抛出异常
    
    def test_validate_age_invalid(self):
        """测试无效年龄验证"""
        invalid_ages = [
            (-1, "年龄必须在0-120岁之间"),
            (121, "年龄必须在0-120岁之间"),
            (25.5, "年龄必须是整数")
        ]
        
        for age, error_msg in invalid_ages:
            person = PersonData(gender="男", age=age, height=175.0, weight=70.0)
            with pytest.raises(BMRInputError, match=error_msg):
                validate_person_data(person)
    
    def test_validate_height_valid(self):
        """测试有效身高验证"""
        # 测试边界值
        heights = [30.0, 30.1, 249.9, 250.0]
        for height in heights:
            person = PersonData(gender="男", age=25, height=height, weight=70.0)
            validate_person_data(person)  # 不应抛出异常
    
    def test_validate_height_invalid(self):
        """测试无效身高验证"""
        invalid_heights = [
            (29.9, "身高必须在30-250厘米之间"),
            (250.1, "身高必须在30-250厘米之间"),
            (-1.0, "身高必须在30-250厘米之间"),
            ("175", "身高必须是数字")
        ]
        
        for height, error_msg in invalid_heights:
            person = PersonData(gender="男", age=25, height=height, weight=70.0)
            with pytest.raises(BMRInputError, match=error_msg):
                validate_person_data(person)
    
    def test_validate_weight_valid(self):
        """测试有效体重验证"""
        # 测试边界值
        weights = [2.0, 2.1, 299.9, 300.0]
        for weight in weights:
            person = PersonData(gender="男", age=25, height=175.0, weight=weight)
            validate_person_data(person)  # 不应抛出异常
    
    def test_validate_weight_invalid(self):
        """测试无效体重验证"""
        invalid_weights = [
            (1.9, "体重必须在2-300公斤之间"),
            (300.1, "体重必须在2-300公斤之间"),
            (-1.0, "体重必须在2-300公斤之间"),
            ("70", "体重必须是数字")
        ]
        
        for weight, error_msg in invalid_weights:
            person = PersonData(gender="男", age=25, height=175.0, weight=weight)
            with pytest.raises(BMRInputError, match=error_msg):
                validate_person_data(person)

class TestBMRCalculation:
    """BMR计算功能测试"""
    
    def test_calculate_bmr_male(self):
        """测试男性BMR计算"""
        person = PersonData(gender="男", age=25, height=175.0, weight=70.0)
        bmr = calculate_bmr(person)
        # 根据Harris-Benedict公式计算的预期值
        expected = round(66.5 + (13.75 * 70) + (5.003 * 175) - (6.755 * 25))
        assert bmr == expected
    
    def test_calculate_bmr_female(self):
        """测试女性BMR计算"""
        person = PersonData(gender="女", age=30, height=160.0, weight=55.0)
        bmr = calculate_bmr(person)
        # 根据Harris-Benedict公式计算的预期值
        expected = round(655.1 + (9.563 * 55) + (1.850 * 160) - (4.676 * 30))
        assert bmr == expected
    
    def test_calculate_bmr_rounding(self):
        """测试BMR计算结果四舍五入"""
        # 创建一个会产生小数的测试用例
        person = PersonData(gender="男", age=25, height=175.5, weight=70.5)
        bmr = calculate_bmr(person)
        # 验证结果是整数
        assert isinstance(bmr, int)
        # 验证是通过四舍五入得到的
        expected = round(66.5 + (13.75 * 70.5) + (5.003 * 175.5) - (6.755 * 25))
        assert bmr == expected

    def test_calculate_bmr_boundary_values(self):
        """测试边界值的BMR计算"""
        # 测试最小有效值
        person_min = PersonData(gender="男", age=0, height=30.0, weight=2.0)
        bmr_min = calculate_bmr(person_min)
        assert bmr_min > 0  # BMR应该始终为正数
        
        # 测试最大有效值
        person_max = PersonData(gender="男", age=120, height=250.0, weight=300.0)
        bmr_max = calculate_bmr(person_max)
        assert bmr_max > 0  # BMR应该始终为正数

def test_end_to_end():
    """端到端测试：从创建实例到计算BMR的完整流程"""
    # 测试用例1：标准男性
    person1 = PersonData(gender="男", age=25, height=175.0, weight=70.0)
    bmr1 = calculate_bmr(person1)
    assert 1700 <= bmr1 <= 1900  # 合理范围检查
    
    # 测试用例2：标准女性
    person2 = PersonData(gender="女", age=30, height=160.0, weight=55.0)
    bmr2 = calculate_bmr(person2)
    assert 1200 <= bmr2 <= 1400  # 合理范围检查 