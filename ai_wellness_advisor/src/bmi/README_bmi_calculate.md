# 特性: BMI 计算 (`bmi_calculate`)

**模块**: `bmi`
**应用**: `ai_wellness_advisor`

## 1. 功能描述

本特性提供了一个函数 `calculate_bmi(height: float, weight: float) -> float`，用于根据用户提供的身高（单位：米）和体重（单位：千克）计算身体质量指数 (BMI)。

主要功能点：
*   接收身高和体重作为浮点数输入。
*   验证输入的身高和体重是否为有效的正数。
*   如果输入无效（非正数或无法转换为有效数字），则抛出 `ValueError` 并附带描述性错误信息。
*   根据公式 `体重 (kg) / (身高 (m) ^ 2)` 计算BMI值。
*   将计算得到的BMI值四舍五入到小数点后两位并返回。

## 2. 如何使用

可以从 `ai_wellness_advisor.src.bmi`模块导入并调用 `calculate_bmi` 函数。

```python
from ai_wellness_advisor.src.bmi import calculate_bmi

try:
    height_m = 1.75
    weight_kg = 70
    bmi = calculate_bmi(height_m, weight_kg)
    print(f"您的BMI是: {bmi}")  # 输出: 您的BMI是: 22.86

    # 示例：无效输入
    bmi_invalid = calculate_bmi(height_m, -5)
except ValueError as e:
    print(f"错误: {e}") # 输出: 错误: 体重必须是有效的正数，单位为千克。

```

## 3. 实现细节

*   **文件位置**: <mcfile name="bmi_calculate.py" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/src/bmi/bmi_calculate.py"></mcfile>
*   **核心函数**: `calculate_bmi(height: float, weight: float) -> float`
*   **输入验证**:
    *   函数内部首先尝试将输入转换为 `float` 类型，如果转换失败（例如输入了无法识别的字符串），会抛出 `ValueError`。
    *   转换成功后，会检查身高和体重是否大于零。如果任一值小于或等于零，会抛出 `ValueError` 并提供具体的错误原因。
    *   验证顺序：优先校验身高，然后校验体重。
*   **错误处理**: 使用 `ValueError` 异常来指示无效的输入。
*   **精度**: BMI计算结果通过 `round()` 函数四舍五入保留两位小数。

## 4. 测试

本特性的单元测试位于 <mcfile name="test_bmi_calculate.py" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/tests/bmi/test_bmi_calculate.py"></mcfile>。
测试覆盖了以下场景：
*   有效的身高和体重输入，包括整数和浮点数，以及需要四舍五入的情况。
*   无效的输入，包括：
    *   身高为零或负数。
    *   体重为零或负数。
    *   身高和体重均为无效值（验证错误提示的优先级）。
*   （可选，取决于实现）输入为无法转换为数字的字符串。

所有测试均使用 `pytest` 框架编写和执行。

## 5. TDD 开发周期文档

关于此特性详细的TDD开发思考过程、设计决策和验证步骤，请参考以下文档：
*   用户故事: <mcfile name="_user_story_bmi_calculate.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/_user_story_bmi_calculate.md"></mcfile>
*   思考选项: <mcfile name="_s1_think_options_bmi_calculate.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/_s1_think_options_bmi_calculate.md"></mcfile>
*   思考设计: <mcfile name="_s2_think_design_bmi_calculate.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/_s2_think_design_bmi_calculate.md"></mcfile>
*   思考验证: <mcfile name="_s3_think_validation_bmi_calculate.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/_s3_think_validation_bmi_calculate.md"></mcfile>