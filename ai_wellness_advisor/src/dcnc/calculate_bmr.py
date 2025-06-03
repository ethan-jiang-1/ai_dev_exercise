"""BMR (Basal Metabolic Rate) calculation module.

This module provides functionality to calculate daily basal metabolic rate
using the Harris-Benedict equation.
"""

# Harris-Benedict formula constants
MALE_BMR_CONSTANTS = {
    'base': 88.362,
    'weight_factor': 13.397,
    'height_factor': 4.799,
    'age_factor': 5.677
}

FEMALE_BMR_CONSTANTS = {
    'base': 447.593,
    'weight_factor': 9.247,
    'height_factor': 3.098,
    'age_factor': 4.330
}


def calculate_bmr(gender: str, age: int, height: float, weight: float) -> float:
    """计算基础代谢率（BMR）。
    
    使用Harris-Benedict公式计算每日基础代谢率。
    
    Args:
        gender (str): 性别，"male" 或 "female"
        age (int): 年龄（岁），范围 1-120
        height (float): 身高（厘米），范围 50-300
        weight (float): 体重（千克），范围 10-500
    
    Returns:
        float: 每日基础代谢率（卡路里/天），保留1位小数
    
    Raises:
        TypeError: 当参数类型不正确时
        ValueError: 当参数值超出合理范围或性别无效时
    """
    # Type validation
    if not isinstance(gender, str):
        raise TypeError(f"gender must be str, got {type(gender).__name__}")
    
    if not isinstance(age, int):
        raise TypeError(f"age must be int, got {type(age).__name__}")
    
    if not isinstance(height, (int, float)):
        raise TypeError(f"height must be int or float, got {type(height).__name__}")
    
    if not isinstance(weight, (int, float)):
        raise TypeError(f"weight must be int or float, got {type(weight).__name__}")
    
    # Value validation
    gender_lower = gender.lower()
    if gender_lower not in ['male', 'female']:
        raise ValueError(f"gender must be 'male' or 'female', got '{gender}'")
    
    if not (1 <= age <= 120):
        raise ValueError(f"age must be between 1 and 120, got {age}")
    
    if not (50 <= height <= 300):
        raise ValueError(f"height must be between 50 and 300 cm, got {height}")
    
    if not (10 <= weight <= 500):
        raise ValueError(f"weight must be between 10 and 500 kg, got {weight}")
    
    # Calculate BMR based on gender
    if gender_lower == 'male':
        bmr = _calculate_bmr_male(age, height, weight)
    else:  # female
        bmr = _calculate_bmr_female(age, height, weight)
    
    # Round to 1 decimal place
    return round(bmr, 1)


def _calculate_bmr_male(age: int, height: float, weight: float) -> float:
    """计算男性BMR。
    
    使用Harris-Benedict公式：
    BMR = 88.362 + (13.397 × 体重kg) + (4.799 × 身高cm) - (5.677 × 年龄)
    """
    constants = MALE_BMR_CONSTANTS
    return (constants['base'] + 
            constants['weight_factor'] * weight + 
            constants['height_factor'] * height - 
            constants['age_factor'] * age)


def _calculate_bmr_female(age: int, height: float, weight: float) -> float:
    """计算女性BMR。
    
    使用Harris-Benedict公式：
    BMR = 447.593 + (9.247 × 体重kg) + (3.098 × 身高cm) - (4.330 × 年龄)
    """
    constants = FEMALE_BMR_CONSTANTS
    return (constants['base'] + 
            constants['weight_factor'] * weight + 
            constants['height_factor'] * height - 
            constants['age_factor'] * age)