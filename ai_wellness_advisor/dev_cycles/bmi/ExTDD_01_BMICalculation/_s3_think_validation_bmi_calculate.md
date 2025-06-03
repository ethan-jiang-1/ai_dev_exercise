# S3: 思考验证 - BMI 值计算 (ExTDD_01_BMICalculation)

**特性名称**: `bmi_calculate`
**模块名称**: `bmi`
**TDD周期**: ExTDD_01_BMICalculation

## 1. 验证目标

确保 <mcfile name="_s2_think_design_bmi_calculate.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/_s2_think_design_bmi_calculate.md"></mcfile> 中设计的 `calculate_bmi` 函数的测试用例能够全面覆盖 <mcfile name="_user_story_bmi_calculate.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/_user_story_bmi_calculate.md"></mcfile> 中定义的所有验收标准 (AC)。

## 2. 验收标准与测试用例映射回顾

| 验收标准 (AC)                                                                 | S2 设计的测试用例                                                                                                                                                                                                                            | 覆盖情况 | 备注                                                                                                                                                                                                                                                           |
| :---------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| AC1: 有效输入，正确计算BMI                                                      | Test Case 1, Test Case 2, Test Case 3, Test Case 10                                                                                                                                                                                          | 完全覆盖 | 包含了不同数值、需要四舍五入的场景以及整数输入。                                                                                                                                                                                                           |
| AC2: 结果四舍五入到小数点后两位                                                 | Test Case 1, Test Case 2, Test Case 3, Test Case 10                                                                                                                                                                                          | 完全覆盖 | 所有成功计算的用例都预期结果为两位小数。Test Case 3 (1.80m, 60kg -> 18.52) 特别验证了四舍五入。                                                                                                                                                           |
| AC3: 无效身高提示                                                               | Test Case 4 (身高0), Test Case 5 (身高负数), Test Case 6 (身高非数字 - 设计上抛ValueError)                                                                                                                                                           | 完全覆盖 | 覆盖了零、负数。对于非数字，设计上是函数内部检查并抛 `ValueError`。如果依赖外部类型检查，则测试行为会不同。当前设计是内部检查。                                                                                                                             |
| AC4: 无效体重提示                                                               | Test Case 7 (体重0), Test Case 8 (体重负数)                                                                                                                                                                                                  | 完全覆盖 | 覆盖了零和负数。                                                                                                                                                                                                                                             |
| AC5: 无效身高和体重同时存在时的提示优先级（设计为优先身高）                     | Test Case 9 (身高0, 体重-70)                                                                                                                                                                                                                 | 完全覆盖 | 验证了当身高无效时，即使体重也无效，优先提示身高错误。                                                                                                                                                                                                       |
| AC6: 清晰展示计算出的BMI值                                                      | Test Case 1, Test Case 2, Test Case 3, Test Case 10                                                                                                                                                                                          | 完全覆盖 | 函数成功时返回计算的 float 值，调用方负责展示。测试层面验证返回值正确。                                                                                                                                                                                           |

## 3. 测试用例完备性检查

*   **边界值分析**：
    *   身高：已测试0、负数。接近0的正数（如0.00001）是否需要特别考虑？对于BMI计算，极小的正数身高可能导致极大的BMI值，但从业务逻辑上，只要是正数就应计算。当前设计符合此逻辑。
    *   体重：已测试0、负数。极小的正数体重同理。
    *   **结论**：当前边界值覆盖基本足够。

*   **等价类划分**：
    *   有效身高：(0, +∞)
    *   无效身高：(-∞, 0] U 非数字
    *   有效体重：(0, +∞)
    *   无效体重：(-∞, 0] U 非数字
    *   **结论**：测试用例已从每个等价类中选取了代表值。

*   **异常路径覆盖**：
    *   已覆盖身高无效、体重无效、两者均无效（按优先级）的情况。
    *   `TypeError`：如果调用者传入了完全不兼容的类型（例如 `calculate_bmi("abc", "xyz")`），Python的算术运算会自然抛出 `TypeError`。我们的设计是在函数内部对输入值进行校验，如果它们不是预期的数字类型或者不能转换为数字，或者转换后不满足正数条件，则抛出 `ValueError`。Test Case 6 旨在覆盖这种情况，预期是 `ValueError`。如果严格依赖类型提示，那么 `TypeError` 可能是外部静态类型检查器或运行时类型检查库（如beartype）的范畴。对于本练习，我们假设输入可以被尝试转换为数字，然后检查其业务有效性（是否为正数）。
    *   **结论**：主要的业务异常路径已覆盖。

*   **数据类型覆盖**：
    *   Test Case 10 覆盖了整数输入的情况，确保 `int` 类型也能正确处理。
    *   **结论**：已覆盖。

## 4. 测试框架与环境

*   **测试框架**: 遵循 <mcfile name="planning_tdd_exercise.md" path="/Users/bowhead/ai_dev_exercise_tdd/tdd_rules/planning_tdd_exercise.md"></mcfile> 的建议，我们将使用 `pytest`。
*   **测试文件结构**: 测试类 `TestBMICalculate`，每个测试用例对应一个测试方法，例如 `test_calculate_bmi_valid_input()`，`test_calculate_bmi_invalid_height_zero()` 等。
*   **断言**: 使用 `pytest` 的 `assert` 语句，对于异常测试，使用 `pytest.raises` 上下文管理器。

## 5. 最终确认的测试用例列表 (用于编写测试代码)

1.  `test_valid_input_normal_case()`: height=1.75, weight=70, expected_bmi=22.86
2.  `test_valid_input_different_values()`: height=1.60, weight=55.5, expected_bmi=21.68
3.  `test_valid_input_needs_rounding()`: height=1.80, weight=60, expected_bmi=18.52
4.  `test_valid_input_integer_values()`: height=2, weight=80, expected_bmi=20.00
5.  `test_invalid_height_zero()`: height=0, weight=70, expect ValueError with message "身高必须是有效的正数，单位为米。"
6.  `test_invalid_height_negative()`: height=-1.75, weight=70, expect ValueError with message "身高必须是有效的正数，单位为米。"
7.  `test_invalid_weight_zero()`: height=1.75, weight=0, expect ValueError with message "体重必须是有效的正数，单位为千克。"
8.  `test_invalid_weight_negative()`: height=1.75, weight=-70, expect ValueError with message "体重必须是有效的正数，单位为千克。"
9.  `test_invalid_height_takes_precedence()`: height=0, weight=-70, expect ValueError with message "身高必须是有效的正数，单位为米。"
10. `test_invalid_height_non_numeric_string()`: height="abc", weight=70, expect ValueError (or TypeError, depending on strictness of internal type check vs relying on Python's ops. Design aims for ValueError from our checks).
11. `test_invalid_weight_non_numeric_string()`: height=1.75, weight="xyz", expect ValueError.

*Self-correction during validation*: Test Case 6 from S2 (`height = "abc"`) and a similar one for weight should be explicitly listed to ensure non-numeric (but potentially convertible by `float()`) inputs that are not positive are handled by our `ValueError`, or that `TypeError` is correctly anticipated if `float()` conversion itself fails before our checks. The design is that `float()` might succeed (e.g. `float("1.0")`) but our `>0` check then applies. If `float("abc")` is called, it raises `ValueError` from `float()` itself. Our code should catch this or let it propagate if it's also a `ValueError`. For clarity, let's assume our function *first* tries to convert to float, then checks `>0`. So, `float("abc")` would raise a `ValueError` that we might not distinguish from our own without careful `try-except` blocks. A simpler path for this TDD cycle is to assume inputs to `calculate_bmi` are already numbers (float/int) due to type hints, and our `ValueError`s are for *semantic* incorrectness (not positive). If we want to be robust against non-numeric strings passed *despite* type hints, the tests for `height="abc"` should expect `ValueError` (from `float()` conversion) or `TypeError` if we don't attempt conversion and an operation fails. Let's refine Test Cases 10 & 11 to target our *semantic* `ValueError` after a successful conversion, and add cases for `TypeError` if direct non-numeric types are passed and not converted. However, for simplicity and focus on TDD for the *logic*, we'll assume type hints guide correct numeric types, and our `ValueError` is for *value constraints* (positive numbers).

**Revised Test Cases for Non-Numeric (Focus on ValueError from our logic if conversion is assumed, or TypeError if not):**
Given the function signature `height: float, weight: float`, Python itself will raise `TypeError` if non-numeric types that cannot be implicitly converted are used in arithmetic. Our explicit checks `value > 0` assume `value` is already a number. If `height` or `weight` are passed as strings like "abc", the `**` or `/` operations would raise `TypeError`. If they are strings like "-1" or "0", `float("-1")` works, then our `>0` check raises `ValueError`. This is the desired behavior.

Test cases 10 and 11 above are good for testing the `ValueError` from our logic if a string *representing* an invalid number (like "0" or "-1.0") is passed and converted. If a string like "abc" is passed, `float("abc")` itself raises `ValueError`. The tests should be precise about what kind of invalid string is passed.

Let's stick to the S2 test cases, assuming the `calculate_bmi` function will attempt to use the inputs as numbers. If they are strings that `float()` cannot convert, `float()`'s `ValueError` will propagate. If they are strings that `float()` *can* convert (e.g., "0", "-5"), then *our* validation logic should raise the `ValueError` with our specific messages.

*   Test Case (from S2, #6, refined): `test_invalid_height_string_zero()`: input `height = "0"`, `weight = 70`. Expect `ValueError` with "身高..."
*   Test Case (new): `test_invalid_height_string_non_convertible()`: input `height = "abc"`, `weight = 70`. Expect `ValueError` (likely from `float("abc")`, message may not be ours, or `TypeError` if not explicitly converting string inputs within the function but relying on arithmetic ops). For TDD, we define *our* function's behavior. If we decide `calculate_bmi` should handle `float` conversion internally and robustly: 
    ```python
    try:
        h = float(height)
        w = float(weight)
    except ValueError:
        raise ValueError("身高和体重必须是有效的数字。") # Generic conversion error
    # Then our >0 checks
    ```
    This makes the function more robust. Let's assume this more robust internal conversion for now. Then `height="abc"` would hit this generic `ValueError`. Our specific messages are for *after* successful conversion to float but failing `>0`.

**Final Decision for Simplicity in this TDD Cycle**: We will assume that the inputs `height` and `weight` to `calculate_bmi` are already of `float` (or `int`) type, as per the type hints. The function's primary responsibility is to validate if these numeric inputs are positive. Thus, `Test Case 6 (AC3 - 无效身高：非数字)` from S2 is less about our *direct* logic if we assume type hints are met. We will focus tests on valid numeric types that fail semantic checks (e.g., 0, -1.0) and valid types that pass. If non-numeric strings are passed, a `TypeError` from Python's operations or a `ValueError` from an explicit `float()` cast (if we add one) would occur. For this cycle, we test `ValueError` from *our* positive number checks.

Therefore, the 10 test cases from S2 are a good starting point, focusing on the logic *after* type conversion (if any) or assuming correct types are passed.

## 6. 下一步

Proceed to write the test code in `../../../../ai_wellness_advisor/tests/bmi/test_bmi_calculate.py` using `pytest`, based on the 10 test cases identified in S2 and re-validated here.