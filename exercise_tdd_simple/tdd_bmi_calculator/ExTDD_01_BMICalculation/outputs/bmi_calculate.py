def bmi_calculate(height_m: float, weight_kg: float) -> float:
    """
    计算 BMI (身体质量指数)
    
    参数:
        height_m (float): 身高，单位为米
        weight_kg (float): 体重，单位为千克
        
    返回:
        float: BMI 值，保留两位小数
        
    异常:
        TypeError: 当输入参数不是数字类型时
        ValueError: 当输入参数小于或等于 0 时
    """
    # 类型检查
    if (isinstance(height_m, bool) or isinstance(weight_kg, bool) or
        not isinstance(height_m, (int, float)) or not isinstance(weight_kg, (int, float))):
        raise TypeError("身高和体重必须是数字类型")
    
    # 值范围检查
    if height_m <= 0:
        raise ValueError("身高必须大于0")
    if weight_kg <= 0:
        raise ValueError("体重必须大于0")
    
    # 计算 BMI
    bmi = weight_kg / (height_m ** 2)
    
    # 返回结果，保留两位小数
    return round(bmi, 2) 