# bmi_calculate.py

def calculate_bmi(height: float, weight: float) -> float:
    """
    计算身体质量指数 (BMI)。

    参数:
        height (float): 身高，单位为米 (m)，必须为正数。
        weight (float): 体重，单位为千克 (kg)，必须为正数。

    返回:
        float: 计算得到的BMI值，四舍五入到小数点后两位。

    抛出:
        ValueError: 如果身高或体重不是有效的正数。
    """
    if not isinstance(height, (int, float)):
        # 这层检查主要针对调用者未遵循类型提示的情况，严格来说，如果类型提示被遵守，这里可能不需要。
        # 但为了稳健性，可以保留，或者依赖静态类型检查器。
        # 对于本练习，我们假设如果类型错误，后续的 <= 0 检查或算术运算会失败。
        # 更简洁的方式是直接检查数值有效性，因为类型提示已指明 float。
        pass # 暂时不为此添加特定的错误，依赖后续的数值检查

    if not isinstance(weight, (int, float)):
        pass # 同上

    # 1. 身高验证
    # 检查类型和值。由于类型提示为float，主要检查值。
    # 如果传入的是非数字类型，Python的比较操作符或算术操作符会引发TypeError。
    # 如果传入的是可以转换为float的字符串（如"abc"），float()会引发ValueError。
    # 此处的逻辑是假设输入已经是数字（int或float）。
    try:
        h = float(height) # 确保处理整数输入以及可转换为float的字符串
    except (ValueError, TypeError):
        raise ValueError("身高必须是一个有效的数字。")

    if h <= 0:
        raise ValueError("身高必须是有效的正数，单位为米。")

    # 2. 体重验证
    try:
        w = float(weight)
    except (ValueError, TypeError):
        raise ValueError("体重必须是一个有效的数字。")

    if w <= 0:
        raise ValueError("体重必须是有效的正数，单位为千克。")

    # 3. BMI 计算
    # 身高 h 已经是 float 类型
    bmi_raw = w / (h ** 2)

    # 4. 结果格式化
    bmi_rounded = round(bmi_raw, 2)

    return bmi_rounded