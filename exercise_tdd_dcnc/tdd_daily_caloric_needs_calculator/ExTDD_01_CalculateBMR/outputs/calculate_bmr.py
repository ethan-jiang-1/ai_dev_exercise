"""
基础代谢率(BMR)计算器模块

本模块实现了基础代谢率的计算功能，使用Harris-Benedict公式。
"""
from dataclasses import dataclass
from typing import Literal


class BMRInputError(ValueError):
    """BMR计算器输入验证异常"""
    pass


@dataclass
class PersonData:
    """人体数据类，用于BMR计算的输入数据验证和存储"""
    
    gender: Literal["男", "女"]  # 使用Literal类型确保性别只能是"男"或"女"
    age: int                    # 年龄(岁)
    height: float              # 身高(cm)
    weight: float              # 体重(kg)


def validate_person_data(data: PersonData) -> None:
    """
    验证PersonData实例中的数据是否有效
    
    Args:
        data: PersonData实例，包含需要验证的数据
        
    Raises:
        BMRInputError: 当输入数据验证失败时抛出
    """
    # 验证性别
    if data.gender not in ["男", "女"]:
        raise BMRInputError("性别必须是'男'或'女'")
    
    # 验证年龄
    if not isinstance(data.age, int):
        raise BMRInputError("年龄必须是整数")
    if not 0 <= data.age <= 120:
        raise BMRInputError("年龄必须在0-120岁之间")
    
    # 验证身高
    if not isinstance(data.height, (int, float)):
        raise BMRInputError("身高必须是数字")
    if not 30 <= data.height <= 250:
        raise BMRInputError("身高必须在30-250厘米之间")
    
    # 验证体重
    if not isinstance(data.weight, (int, float)):
        raise BMRInputError("体重必须是数字")
    if not 2 <= data.weight <= 300:
        raise BMRInputError("体重必须在2-300公斤之间")


def calculate_bmr(person: PersonData) -> int:
    """
    计算基础代谢率(BMR)
    
    使用Harris-Benedict公式计算BMR：
    男性：BMR = 66.5 + (13.75 × 体重kg) + (5.003 × 身高cm) - (6.755 × 年龄)
    女性：BMR = 655.1 + (9.563 × 体重kg) + (1.850 × 身高cm) - (4.676 × 年龄)
    
    Args:
        person: PersonData实例，包含计算所需的个人数据
        
    Returns:
        int: 基础代谢率(kcal/天)，四舍五入到整数
        
    Raises:
        BMRInputError: 当输入数据验证失败时抛出
        ValueError: 当计算过程中出现错误时抛出
    """
    # 1. 验证输入数据
    validate_person_data(person)
    
    # 2. 根据Harris-Benedict公式计算BMR
    try:
        if person.gender == "男":
            bmr = 66.5 + (13.75 * person.weight) + (5.003 * person.height) - (6.755 * person.age)
        else:  # 女性
            bmr = 655.1 + (9.563 * person.weight) + (1.850 * person.height) - (4.676 * person.age)
        
        # 3. 四舍五入到整数
        return round(bmr)
        
    except (ValueError, ArithmeticError) as e:
        raise ValueError(f"BMR计算过程出错: {str(e)}")


if __name__ == "__main__":
    # 使用示例
    try:
        # 创建PersonData实例
        person = PersonData(
            gender="男",
            age=25,
            height=175.0,
            weight=70.0
        )
        
        # 计算BMR
        bmr = calculate_bmr(person)
        print(f"基础代谢率: {bmr} kcal/天")
        
    except BMRInputError as e:
        print(f"输入数据错误: {str(e)}")
    except ValueError as e:
        print(f"计算错误: {str(e)}") 