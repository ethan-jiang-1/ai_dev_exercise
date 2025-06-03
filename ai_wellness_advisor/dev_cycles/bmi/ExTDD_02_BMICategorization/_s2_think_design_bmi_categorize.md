# S2: 思考设计 - BMI 值分类 (ExTDD_02_BMICategorization)

**特性名称**: `categorize_bmi`
**模块名称**: `bmi`
**TDD周期**: ExTDD_02_BMICategorization

参考文档：
*   用户故事: <mcfile name="_user_story_bmi_categorize.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_02_BMICategorization/_user_story_bmi_categorize.md"></mcfile>
*   思考选项: <mcfile name="_s1_think_options_bmi_categorize.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_02_BMICategorization/_s1_think_options_bmi_categorize.md"></mcfile>

## 1. 函数签名与模块结构

*   **模块**: `ai_wellness_advisor.src.bmi.bmi_categorize`
*   **函数签名**:
    ```python
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
        pass
    ```

## 2. 输入验证逻辑

1.  **类型检查与转换**: 首先，尝试将 `bmi_value` 转换为 `float`。如果转换失败（例如，输入是无法转换为数字的字符串），捕获 `TypeError` 或 `ValueError`，并重新抛出统一的 `ValueError`，信息为：“BMI值必须是有效的数字”。
2.  **正数校验**: 转换成功后，检查 `bmi_value` 是否大于 0。如果不大于 0（即 `bmi_value <= 0`），则抛出 `ValueError`，信息为：“BMI值必须是有效的正数”。

## 3. BMI 分类逻辑 (基于AC1)

将使用 `if-elif-else` 结构实现，严格按照用户故事AC1中定义的边界和分类名称：

```python
# 伪代码，实际在函数内部
if bmi_value < 18.5:
    return "偏瘦 (Underweight)"
elif bmi_value < 24.0:  # 18.5 <= bmi_value < 24.0
    return "健康体重 (Healthy Weight)"
elif bmi_value < 28.0:  # 24.0 <= bmi_value < 28.0
    return "超重 (Overweight)"
elif bmi_value < 30.0:  # 28.0 <= bmi_value < 30.0
    return "肥胖前期 (Pre-obese)"
else:  # bmi_value >= 30.0
    return "肥胖 (Obese)"
```

**注意边界条件**：
*   `< 18.5`
*   `>= 18.5` and `< 24.0`
*   `>= 24.0` and `< 28.0`
*   `>= 28.0` and `< 30.0`
*   `>= 30.0`

## 4. 错误处理机制

*   统一使用 `ValueError` 抛出所有与输入 `bmi_value` 相关的业务逻辑错误。
    *   无效数字输入: `ValueError("BMI值必须是有效的数字")`
    *   非正数输入: `ValueError("BMI值必须是有效的正数")`

## 5. 模块与文件结构

*   **源文件**: `ai_wellness_advisor/src/bmi/bmi_categorize.py` (新文件)
*   **测试文件**: `ai_wellness_advisor/tests/bmi/test_bmi_categorize.py` (新文件)
*   **`__init__.py` 更新**: 需要在 `ai_wellness_advisor/src/bmi/__init__.py` 中导出 `categorize_bmi` 函数。
    ```python
    # ai_wellness_advisor/src/bmi/__init__.py
    from .bmi_calculate import calculate_bmi
    from .bmi_categorize import categorize_bmi # 新增此行

    __all__ = ['calculate_bmi', 'categorize_bmi'] # 更新此列表
    ```

## 6. 详细测试用例设计 (TDD驱动)

基于用户故事的验收标准 (AC) 和S1中的考量，设计以下测试用例：

**测试目标**: `categorize_bmi` 函数

1.  **AC1 & AC3: 正常分类 - 偏瘦 (Underweight)**
    *   `test_categorize_underweight_lower_bound()`: BMI = 10.0 -> "偏瘦 (Underweight)"
    *   `test_categorize_underweight_just_below_healthy()`: BMI = 18.49 -> "偏瘦 (Underweight)"

2.  **AC1 & AC3: 正常分类 - 健康体重 (Healthy Weight)**
    *   `test_categorize_healthy_lower_bound()`: BMI = 18.5 -> "健康体重 (Healthy Weight)"
    *   `test_categorize_healthy_mid_range()`: BMI = 22.0 -> "健康体重 (Healthy Weight)"
    *   `test_categorize_healthy_just_below_overweight()`: BMI = 23.99 -> "健康体重 (Healthy Weight)"

3.  **AC1 & AC3: 正常分类 - 超重 (Overweight)**
    *   `test_categorize_overweight_lower_bound()`: BMI = 24.0 -> "超重 (Overweight)"
    *   `test_categorize_overweight_mid_range()`: BMI = 26.0 -> "超重 (Overweight)"
    *   `test_categorize_overweight_just_below_pre_obese()`: BMI = 27.99 -> "超重 (Overweight)"

4.  **AC1 & AC3: 正常分类 - 肥胖前期 (Pre-obese)**
    *   `test_categorize_pre_obese_lower_bound()`: BMI = 28.0 -> "肥胖前期 (Pre-obese)"
    *   `test_categorize_pre_obese_mid_range()`: BMI = 29.0 -> "肥胖前期 (Pre-obese)"
    *   `test_categorize_pre_obese_just_below_obese()`: BMI = 29.99 -> "肥胖前期 (Pre-obese)"

5.  **AC1 & AC3: 正常分类 - 肥胖 (Obese)**
    *   `test_categorize_obese_lower_bound()`: BMI = 30.0 -> "肥胖 (Obese)"
    *   `test_categorize_obese_high_value()`: BMI = 40.0 -> "肥胖 (Obese)"

6.  **AC2: 无效输入 - 零值**
    *   `test_categorize_invalid_bmi_zero()`: BMI = 0 -> `ValueError` ("BMI值必须是有效的正数")

7.  **AC2: 无效输入 - 负值**
    *   `test_categorize_invalid_bmi_negative()`: BMI = -5.0 -> `ValueError` ("BMI值必须是有效的正数")

8.  **AC2: 无效输入 - 非数字 (字符串)**
    *   `test_categorize_invalid_bmi_string()`: BMI = "abc" -> `ValueError` ("BMI值必须是有效的数字")

9.  **AC2: 无效输入 - None**
    *   `test_categorize_invalid_bmi_none()`: BMI = None -> `ValueError` ("BMI值必须是有效的数字") (或 `TypeError` 被捕获后转为 `ValueError`)

## 7. 实现步骤规划 (TDD流程)

1.  **创建测试文件**: `ai_wellness_advisor/tests/bmi/test_bmi_categorize.py`。
2.  **编写第一个失败的测试**: 例如，`test_categorize_underweight_lower_bound()`。
3.  **创建源文件和空函数**: `ai_wellness_advisor/src/bmi/bmi_categorize.py` 包含 `categorize_bmi` 的空实现或直接 `raise NotImplementedError`。
4.  **运行测试**: 确认测试失败。
5.  **编写最小代码使测试通过**: 实现 `categorize_bmi` 中处理 `bmi_value < 18.5` 的逻辑以及基本的输入验证（正数）。
6.  **运行测试**: 确认测试通过。
7.  **重构 (如果需要)**。
8.  **重复步骤2-7**: 逐步添加其他分类的测试用例和相应的实现逻辑 (健康体重、超重等)。
9.  **添加错误处理测试**: 编写针对无效输入的测试用例 (零、负数、非数字) 并实现相应的错误抛出逻辑。
10. **更新 `__init__.py`**: 将 `categorize_bmi` 添加到 `ai_wellness_advisor/src/bmi/__init__.py`。
11. **运行所有测试**: 确保所有测试都通过。

## 8. 下一步

进入 S3 验证阶段，仔细回顾 S2 设计的测试用例是否全面覆盖了用户故事ACs。然后开始编写测试代码。