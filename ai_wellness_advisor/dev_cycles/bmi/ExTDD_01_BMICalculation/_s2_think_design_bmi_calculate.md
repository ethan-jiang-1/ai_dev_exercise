# S2: 思考设计 - BMI 值计算 (ExTDD_01_BMICalculation)

**特性名称**: `bmi_calculate`
**模块名称**: `bmi`
**TDD周期**: ExTDD_01_BMICalculation

## 1. 设计目标

基于 <mcfile name="_s1_think_options_bmi_calculate.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/_s1_think_options_bmi_calculate.md"></mcfile> 中的分析和决策，设计一个健壮、易于测试的BMI计算函数。

## 2. 核心组件设计

### 2.1. 函数签名

```python
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
    pass
```

### 2.2. 输入验证逻辑

1.  **身高验证**:
    *   检查 `height` 是否为 `float` 或 `int` 类型 (虽然类型提示是 `float`，但实际传入 `int` 也应能处理)。
    *   检查 `height` 是否大于 0。
    *   如果无效，抛出 `ValueError("身高必须是有效的正数，单位为米。")`。

2.  **体重验证**:
    *   检查 `weight` 是否为 `float` 或 `int` 类型。
    *   检查 `weight` 是否大于 0。
    *   如果无效，抛出 `ValueError("体重必须是有效的正数，单位为千克。")`。

3.  **验证顺序与AC5处理**:
    *   我们将按照“先校验身高，再校验体重”的顺序。这意味着如果身高无效，将首先抛出关于身高的错误，即使体重也无效。这符合 <mcfile name="_s1_think_options_bmi_calculate.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/_s1_think_options_bmi_calculate.md"></mcfile> 中AC5的初步倾向（选项A）。

### 2.3. BMI 计算与格式化

1.  **计算**:
    *   `bmi_raw = weight / (height ** 2)`
2.  **格式化**:
    *   `bmi_rounded = round(bmi_raw, 2)`
    *   返回 `bmi_rounded`。

## 3. 错误处理机制

*   统一使用 Python 内置的 `ValueError` 异常。
*   异常消息应清晰指明错误原因，如：“身高必须是有效的正数，单位为米。”或“体重必须是有效的正数，单位为千克。”

## 4. 模块与文件结构

*   **源代码文件**: `../{app_name}/src/{module_name}/{feature_name}.py` 即 `../../../../ai_wellness_advisor/src/bmi/bmi_calculate.py`
    *   此文件将包含 `calculate_bmi` 函数的实现。
*   **测试代码文件**: `../{app_name}/tests/{module_name}/test_{feature_name}.py` 即 `../../../../ai_wellness_advisor/tests/bmi/test_bmi_calculate.py`
    *   此文件将包含针对 `calculate_bmi` 函数的单元测试。

## 5. 详细测试用例设计 (TDD核心)

基于验收标准 (<mcfile name="_user_story_bmi_calculate.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/_user_story_bmi_calculate.md"></mcfile>) 和本设计，初步规划以下测试用例：

*   **Test Case 1 (AC1, AC2, AC6 - 正常情况)**:
    *   输入: `height = 1.75`, `weight = 70`
    *   预期输出: `22.86`
*   **Test Case 2 (AC1, AC2, AC6 - 正常情况，不同数值)**:
    *   输入: `height = 1.60`, `weight = 55.5`
    *   预期输出: `21.68`
*   **Test Case 3 (AC1, AC2, AC6 - 边界情况，结果需四舍五入)**:
    *   输入: `height = 1.80`, `weight = 60`
    *   预期输出: `18.52` (实际计算 60 / (1.8*1.8) = 18.5185...)
*   **Test Case 4 (AC3 - 无效身高：零)**:
    *   输入: `height = 0`, `weight = 70`
    *   预期行为: 抛出 `ValueError`，消息包含“身高必须是有效的正数”。
*   **Test Case 5 (AC3 - 无效身高：负数)**:
    *   输入: `height = -1.75`, `weight = 70`
    *   预期行为: 抛出 `ValueError`，消息包含“身高必须是有效的正数”。
*   **Test Case 6 (AC3 - 无效身高：非数字，虽然类型提示会先拦截，但测试应覆盖防御性编程)**:
    *   输入: `height = "abc"`, `weight = 70` (此场景下，Python的类型系统和函数调用前的转换可能先出错，但测试逻辑应考虑函数内部如何处理非期望类型，或依赖于调用者保证类型正确性。对于强类型语言或使用Pydantic会更优雅处理。在此，我们假设输入到函数的是数值类型或可转换为数值类型，主要测试数值本身的有效性)
    *   预期行为: 抛出 `ValueError` (或 `TypeError` 如果函数内部不做类型转换检查，依赖外部)。设计上我们倾向于函数内部检查数值有效性，所以是 `ValueError`。
*   **Test Case 7 (AC4 - 无效体重：零)**:
    *   输入: `height = 1.75`, `weight = 0`
    *   预期行为: 抛出 `ValueError`，消息包含“体重必须是有效的正数”。
*   **Test Case 8 (AC4 - 无效体重：负数)**:
    *   输入: `height = 1.75`, `weight = -70`
    *   预期行为: 抛出 `ValueError`，消息包含“体重必须是有效的正数”。
*   **Test Case 9 (AC5 - 无效身高优先于无效体重)**:
    *   输入: `height = 0`, `weight = -70`
    *   预期行为: 抛出 `ValueError`，消息包含“身高必须是有效的正数”。
*   **Test Case 10 (AC1, AC2, AC6 - 整数输入)**:
    *   输入: `height = 2`, `weight = 80`
    *   预期输出: `20.00`

## 6. 实现考量

*   **类型检查**: 虽然Python是动态类型语言，但函数内部可以使用 `isinstance()` 进行类型检查，或者更依赖于调用者遵循类型提示。对于此练习，我们将主要关注数值本身的有效性（大于0）。如果传入非数字类型，Python的算术运算会自然抛出 `TypeError`，测试时可以区分 `ValueError`（业务逻辑错误）和 `TypeError`（类型不匹配）。我们的设计是抛出 `ValueError`。
*   **除零错误**: 如果身高为0，`height ** 2` 会是0，导致 `ZeroDivisionError`。我们的验证逻辑（身高 > 0）会在此之前捕获这个问题并抛出 `ValueError`。

## 7. 下一步

进入 S3 验证阶段，进一步确认测试用例的完备性，然后开始编写测试代码 (`test_bmi_calculate.py`)。