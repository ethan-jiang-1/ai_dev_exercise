"""基础代谢率(BMR)计算器

这个模块实现了基础代谢率(BMR)的计算功能，使用Harris-Benedict公式。
包含输入验证和计算逻辑。
"""

from typing import Union, Any
from decimal import Decimal, ROUND_HALF_UP

class BMRValidationError(Exception):
    """BMR计算器验证错误的基类"""
    pass

class InvalidGenderError(BMRValidationError):
    """性别输入无效时抛出的异常"""
    pass

class InvalidAgeError(BMRValidationError):
    """年龄输入无效时抛出的异常"""
    pass

class InvalidHeightError(BMRValidationError):
    """身高输入无效时抛出的异常"""
    pass

class InvalidWeightError(BMRValidationError):
    """体重输入无效时抛出的异常"""
    pass

class BMRCalculator:
    """基础代谢率计算器类"""

    def __init__(self):
        """初始化BMR计算器"""
        # 定义输入验证的范围
        self.VALID_GENDERS = {"男", "女"}
        self.AGE_RANGE = (15, 80)
        self.HEIGHT_RANGE = (130.0, 230.0)
        self.WEIGHT_RANGE = (30.0, 150.0)

        # BMR计算系数（Harris-Benedict公式）
        # 使用Decimal保持高精度计算
        self.MALE_BMR_CONSTANT = Decimal('66.5')
        self.MALE_WEIGHT_MULTIPLIER = Decimal('13.75')
        self.MALE_HEIGHT_MULTIPLIER = Decimal('5.003')
        self.MALE_AGE_MULTIPLIER = Decimal('6.755')

        self.FEMALE_BMR_CONSTANT = Decimal('655.1')
        self.FEMALE_WEIGHT_MULTIPLIER = Decimal('9.563')
        self.FEMALE_HEIGHT_MULTIPLIER = Decimal('1.850')
        self.FEMALE_AGE_MULTIPLIER = Decimal('4.676')

    def validate_gender(self, gender: Any) -> None:
        """验证性别输入是否有效

        Args:
            gender: 性别输入值

        Raises:
            InvalidGenderError: 当性别输入无效时抛出
        """
        if not isinstance(gender, str) or gender not in self.VALID_GENDERS:
            raise InvalidGenderError("性别必须是'男'或'女'")

    def validate_age(self, age: Any) -> None:
        """验证年龄输入是否有效

        Args:
            age: 年龄输入值

        Raises:
            InvalidAgeError: 当年龄输入无效时抛出
        """
        if not isinstance(age, int):
            raise InvalidAgeError("年龄必须是整数")
        if not (self.AGE_RANGE[0] <= age <= self.AGE_RANGE[1]):
            raise InvalidAgeError(f"年龄必须在{self.AGE_RANGE[0]}到{self.AGE_RANGE[1]}岁之间")

    def validate_height(self, height: Any) -> None:
        """验证身高输入是否有效

        Args:
            height: 身高输入值（厘米）

        Raises:
            InvalidHeightError: 当身高输入无效时抛出
        """
        if not isinstance(height, (int, float)):
            raise InvalidHeightError("身高必须是数字")
        if not (self.HEIGHT_RANGE[0] <= float(height) <= self.HEIGHT_RANGE[1]):
            raise InvalidHeightError(f"身高必须在{self.HEIGHT_RANGE[0]}到{self.HEIGHT_RANGE[1]}厘米之间")

    def validate_weight(self, weight: Any) -> None:
        """验证体重输入是否有效

        Args:
            weight: 体重输入值（千克）

        Raises:
            InvalidWeightError: 当体重输入无效时抛出
        """
        if not isinstance(weight, (int, float)):
            raise InvalidWeightError("体重必须是数字")
        if not (self.WEIGHT_RANGE[0] <= float(weight) <= self.WEIGHT_RANGE[1]):
            raise InvalidWeightError(f"体重必须在{self.WEIGHT_RANGE[0]}到{self.WEIGHT_RANGE[1]}千克之间")

    def validate_inputs(self, gender: str, age: int, height: float, weight: float) -> None:
        """验证所有输入参数是否有效

        Args:
            gender: 性别
            age: 年龄（岁）
            height: 身高（厘米）
            weight: 体重（千克）

        Raises:
            BMRValidationError: 当任何输入无效时抛出
        """
        self.validate_gender(gender)
        self.validate_age(age)
        self.validate_height(height)
        self.validate_weight(weight)

    def calculate(self, gender: str, age: int, height: float, weight: float) -> float:
        """计算基础代谢率(BMR)

        使用Harris-Benedict公式计算BMR：
        男性：BMR = 66.5 + (13.75 × 体重kg) + (5.003 × 身高cm) - (6.755 × 年龄)
        女性：BMR = 655.1 + (9.563 × 体重kg) + (1.850 × 身高cm) - (4.676 × 年龄)

        Args:
            gender: 性别（"男"或"女"）
            age: 年龄（岁）
            height: 身高（厘米）
            weight: 体重（千克）

        Returns:
            float: 基础代谢率（卡路里/天），保留一位小数

        Raises:
            BMRValidationError: 当输入参数无效时抛出
        """
        # 验证所有输入
        self.validate_inputs(gender, age, height, weight)

        # 转换输入为Decimal以保持高精度计算
        d_weight = Decimal(str(weight))
        d_height = Decimal(str(height))
        d_age = Decimal(str(age))

        # 根据性别选择计算公式
        if gender == "男":
            bmr = (self.MALE_BMR_CONSTANT +
                  (self.MALE_WEIGHT_MULTIPLIER * d_weight) +
                  (self.MALE_HEIGHT_MULTIPLIER * d_height) -
                  (self.MALE_AGE_MULTIPLIER * d_age))
        else:  # gender == "女"
            bmr = (self.FEMALE_BMR_CONSTANT +
                  (self.FEMALE_WEIGHT_MULTIPLIER * d_weight) +
                  (self.FEMALE_HEIGHT_MULTIPLIER * d_height) -
                  (self.FEMALE_AGE_MULTIPLIER * d_age))

        # 返回结果，保留一位小数，使用ROUND_HALF_UP确保四舍五入
        return float(bmr.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)) 