def categorize_bmi(bmi_value: float) -> str:
    """
    根据BMI值返回健康状况分类。

    参数:
        bmi_value (float): 用户的BMI值。

    返回:
        str: 健康状况分类字符串。

    异常:
        ValueError: 如果BMI值无效 (例如，非正数或无法转换为浮点数)。
    """
    try:
        bmi = float(bmi_value)
    except (ValueError, TypeError):
        # This handles cases where bmi_value is None, or a string like "abc"
        raise ValueError("BMI值必须是有效的数字")

    # After successful conversion to float, check if the value is positive.
    if bmi <= 0:
        raise ValueError("BMI值必须是有效的正数")

    if bmi < 18.5:
        return "偏瘦 (Underweight)"
    elif bmi < 24.0: # 18.5 <= bmi < 24.0
        return "健康体重 (Healthy Weight)"
    elif bmi < 28.0: # 24.0 <= bmi < 28.0
        return "超重 (Overweight)"
    elif bmi < 30.0: # 28.0 <= bmi < 30.0
        return "肥胖前期 (Pre-obese)"
    else:  # bmi_value >= 30.0
        return "肥胖 (Obese)"