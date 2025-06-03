"""TDEE (Total Daily Energy Expenditure) calculation module.

This module provides functionality to calculate daily total energy expenditure
based on BMR and activity level using standard activity coefficients.
"""

import math

# 活动水平系数常量 - 基于Harris-Benedict标准
ACTIVITY_COEFFICIENTS = {
    'sedentary': 1.2,           # 久坐，很少或没有运动
    'lightly_active': 1.375,    # 轻度活动，轻度运动1-3天/周
    'moderately_active': 1.55,  # 中度活动，中度运动3-5天/周
    'very_active': 1.725,       # 重度活动，重度运动6-7天/周
    'extra_active': 1.9         # 极重度活动，非常重度运动或体力工作
}

# BMR有效范围常量
MIN_BMR = 500   # 最小合理BMR值
MAX_BMR = 5000  # 最大合理BMR值


def calculate_tdee(bmr: float, activity_level: str) -> float:
    """计算每日总能量消耗（TDEE）。
    
    基于基础代谢率（BMR）和日常活动水平计算每日总能量消耗。
    使用标准活动系数进行计算：TDEE = BMR × 活动系数
    
    Args:
        bmr (float): 基础代谢率（卡路里/天），范围 500-5000
        activity_level (str): 活动水平，可选值：
            - "sedentary": 久坐，很少或没有运动 (系数: 1.2)
            - "lightly_active": 轻度活动，轻度运动1-3天/周 (系数: 1.375)
            - "moderately_active": 中度活动，中度运动3-5天/周 (系数: 1.55)
            - "very_active": 重度活动，重度运动6-7天/周 (系数: 1.725)
            - "extra_active": 极重度活动，非常重度运动或体力工作 (系数: 1.9)
    
    Returns:
        float: 每日总能量消耗（卡路里/天），保留1位小数
    
    Raises:
        TypeError: 当参数类型不正确时
        ValueError: 当参数值超出合理范围或活动水平无效时
    
    Examples:
        >>> calculate_tdee(1500, "sedentary")
        1800.0
        >>> calculate_tdee(2000, "moderately_active")
        3100.0
        >>> calculate_tdee(1800, "very_active")
        3105.0
    """
    
    # 1. BMR类型验证
    if not isinstance(bmr, (int, float)):
        raise TypeError(f"bmr must be int or float, got {type(bmr).__name__}")
    
    # 2. 活动水平类型验证
    if not isinstance(activity_level, str):
        raise TypeError(f"activity_level must be str, got {type(activity_level).__name__}")
    
    # 3. BMR特殊值验证
    if math.isnan(bmr) or math.isinf(bmr):
        raise ValueError(f"bmr must be a finite number, got {bmr}")
    
    # 4. BMR范围验证
    if not (MIN_BMR <= bmr <= MAX_BMR):
        raise ValueError(f"bmr must be between {MIN_BMR} and {MAX_BMR}, got {bmr}")
    
    # 5. 活动水平标准化
    activity_level_normalized = activity_level.lower().strip()
    
    # 6. 活动水平有效性验证
    if activity_level_normalized not in ACTIVITY_COEFFICIENTS:
        valid_levels = list(ACTIVITY_COEFFICIENTS.keys())
        raise ValueError(f"activity_level must be one of {valid_levels}, got '{activity_level}'")
    
    # 7. 计算TDEE
    activity_coefficient = ACTIVITY_COEFFICIENTS[activity_level_normalized]
    tdee = bmr * activity_coefficient
    
    # 8. 返回结果（保留1位小数）
    return round(tdee, 1)