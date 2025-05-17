# 单位转换常量
INCHES_PER_FOOT = 12
INCHES_TO_METERS = 0.0254
POUNDS_TO_KG = 0.45359237

# 单位类型常量
HEIGHT_UNIT_METERS = "m"
HEIGHT_UNIT_FT_IN = "ft_in"
WEIGHT_UNIT_KG = "kg"
WEIGHT_UNIT_LB = "lb"

# 范围限制常量
MIN_HEIGHT_METERS = 0.1
MAX_HEIGHT_METERS = 3.048  # 10英尺
MIN_WEIGHT_KG = 0.1
MAX_WEIGHT_KG = 300
MIN_WEIGHT_LB = 0.5
MAX_WEIGHT_LB = 660

# 错误消息模板
ERROR_MESSAGES = {
    "invalid_height_unit": "身高单位必须是 'm' 或 'ft_in'",
    "invalid_weight_unit": "体重单位必须是 'kg' 或 'lb'",
    "invalid_height_type": "身高必须是数字或(英尺,英寸)元组",
    "invalid_weight_type": "体重必须是数字",
    "invalid_inches": "英寸必须在 0-11 范围内",
    "height_out_of_range": "身高超出有效范围",
    "weight_out_of_range": "体重超出有效范围",
    "invalid_tuple": "英尺/英寸必须是包含两个数字的元组"
}

def convert_height_to_meters(height: float | tuple[float, float], unit: str = HEIGHT_UNIT_METERS) -> float:
    """
    将身高转换为米
    
    参数:
        height: 身高值
            - float: 米为单位的身高，或英尺为单位的身高
            - tuple: (英尺, 英寸)的身高
        unit: 输入单位，"m" 或 "ft_in"
            
    返回:
        float: 转换后的身高（米）
        
    异常:
        TypeError: 输入类型错误
        ValueError: 单位类型错误或输入值无效
    """
    # 类型检查
    if not isinstance(unit, str):
        raise TypeError(ERROR_MESSAGES["invalid_height_unit"])
        
    # 单位验证
    if unit not in [HEIGHT_UNIT_METERS, HEIGHT_UNIT_FT_IN]:
        raise ValueError(ERROR_MESSAGES["invalid_height_unit"])
    
    # 处理米单位
    if unit == HEIGHT_UNIT_METERS:
        if isinstance(height, bool) or not isinstance(height, (int, float)):
            raise TypeError(ERROR_MESSAGES["invalid_height_type"])
        if height < MIN_HEIGHT_METERS or height > MAX_HEIGHT_METERS:
            raise ValueError(ERROR_MESSAGES["height_out_of_range"])
        return float(height)
    
    # 处理英尺/英寸单位
    if unit == HEIGHT_UNIT_FT_IN:
        # 验证元组格式
        if not isinstance(height, tuple) or len(height) != 2:
            raise TypeError(ERROR_MESSAGES["invalid_tuple"])
        
        feet, inches = height
        
        # 验证数字类型
        if (isinstance(feet, bool) or isinstance(inches, bool) or
            not isinstance(feet, (int, float)) or not isinstance(inches, (int, float))):
            raise TypeError(ERROR_MESSAGES["invalid_height_type"])
        
        # 验证范围
        if feet < 1 or feet > 10:
            raise ValueError(ERROR_MESSAGES["height_out_of_range"])
        if inches < 0 or inches >= INCHES_PER_FOOT:
            raise ValueError(ERROR_MESSAGES["invalid_inches"])
            
        # 转换为米
        total_inches = feet * INCHES_PER_FOOT + inches
        meters = round(total_inches * INCHES_TO_METERS, 4)  # 保留4位小数以确保精度
        
        # 验证最终结果范围
        if meters < MIN_HEIGHT_METERS or meters > MAX_HEIGHT_METERS:
            raise ValueError(ERROR_MESSAGES["height_out_of_range"])
            
        return meters

def convert_weight_to_kg(weight: float, unit: str = WEIGHT_UNIT_KG) -> float:
    """
    将体重转换为千克
    
    参数:
        weight: 体重值
        unit: 输入单位，"kg" 或 "lb"
            
    返回:
        float: 转换后的体重（千克）
        
    异常:
        TypeError: 输入类型错误
        ValueError: 单位类型错误或输入值无效
    """
    # 类型检查
    if not isinstance(unit, str):
        raise TypeError(ERROR_MESSAGES["invalid_weight_unit"])
    if isinstance(weight, bool) or not isinstance(weight, (int, float)):
        raise TypeError(ERROR_MESSAGES["invalid_weight_type"])
        
    # 单位验证
    if unit not in [WEIGHT_UNIT_KG, WEIGHT_UNIT_LB]:
        raise ValueError(ERROR_MESSAGES["invalid_weight_unit"])
    
    # 处理千克单位
    if unit == WEIGHT_UNIT_KG:
        if weight < MIN_WEIGHT_KG or weight > MAX_WEIGHT_KG:
            raise ValueError(ERROR_MESSAGES["weight_out_of_range"])
        return float(weight)
    
    # 处理磅单位
    if unit == WEIGHT_UNIT_LB:
        if weight < MIN_WEIGHT_LB or weight > MAX_WEIGHT_LB:
            raise ValueError(ERROR_MESSAGES["weight_out_of_range"])
        kg = round(weight * POUNDS_TO_KG, 4)  # 提高精度，保留4位小数
        if kg < MIN_WEIGHT_KG or kg > MAX_WEIGHT_KG:
            raise ValueError(ERROR_MESSAGES["weight_out_of_range"])
        return kg

def bmi_calculate(height_m: float, weight_kg: float) -> float:
    """
    计算 BMI (身体质量指数)
    
    参数:
        height_m: 身高，单位为米
        weight_kg: 体重，单位为千克
        
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
    if height_m < MIN_HEIGHT_METERS:
        raise ValueError("身高必须大于最小值")
    if weight_kg < MIN_WEIGHT_KG:
        raise ValueError("体重必须大于最小值")
    
    # 计算 BMI，提高中间计算精度
    height_squared = round(height_m * height_m, 6)  # 提高平方计算精度
    bmi = round(weight_kg / height_squared, 4)  # 提高除法计算精度
    
    # 返回结果，保留两位小数
    return round(bmi, 2) 