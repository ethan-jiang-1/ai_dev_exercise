# BMI Calculator Exercise Constraints

为了简化练习并聚焦于 TDD 流程，请遵循以下基本约束：

1.  **输入单位**: 
    *   体重 (`weight_kg`) 始终以公斤 (kg) 为单位。
    *   身高 (`height_m`) 始终以米 (m) 为单位。
    *   无需进行单位转换。

2.  **输入类型**: 
    *   体重和身高应被视为数值类型（整数或浮点数）。
    *   函数应能处理这两种类型，但主要测试用例可以使用浮点数。

3.  **BMI 分类标准**: 
    *   使用以下世界卫生组织 (WHO) 推荐的成人标准：
        *   < 18.5: Underweight
        *   18.5 到 24.9: Normal
        *   25.0 到 29.9: Overweight
        *   >= 30.0: Obese
    *   注意边界值的包含关系（例如，18.5 属于 Normal，25.0 属于 Overweight）。

4.  **错误处理**: 
    *   仅需处理明确提到的错误情况（身高 <= 0，体重 < 0，BMI < 0）。
    *   使用 `ValueError` 来表示无效输入。
    *   暂时不考虑非数值输入（如字符串）等更复杂的错误处理。

5.  **精度**: 
    *   `calculate_bmi` 函数返回的 BMI 值建议四舍五入到小数点后两位。

6.  **实现**: 
    *   将两个功能 (`calculate_bmi` 和 `categorize_bmi`) 实现在同一个 Python 文件 `bmi_calculator.py` 中。
    *   对应的测试也放在同一个测试文件 `test_bmi_calculator.py` 中。

这些约束旨在确保练习的核心在于应用 TDD 方法，而不是处理复杂的单位转换或边缘错误情况。 