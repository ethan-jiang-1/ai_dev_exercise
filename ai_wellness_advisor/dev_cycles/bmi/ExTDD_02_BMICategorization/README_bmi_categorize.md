# 特性说明: BMI 值分类 (`categorize_bmi`)

**特性名称**: `categorize_bmi`
**模块**: `ai_wellness_advisor.src.bmi.bmi_categorize`
**TDD周期**: `ExTDD_02_BMICategorization`

## 1. 功能描述

`categorize_bmi` 函数根据输入的世界卫生组织 (WHO) 成人BMI分类标准，将一个已计算的BMI（身体质量指数）值映射到相应的健康状况分类字符串。此函数旨在帮助用户理解其BMI数值的含义。

## 2. 如何使用

可以通过从 `ai_wellness_advisor.src.bmi` 包导入 `categorize_bmi` 函数来使用它。

```python
from ai_wellness_advisor.src.bmi import categorize_bmi

try:
    bmi_value = 22.5
    category = categorize_bmi(bmi_value)
    print(f"BMI值为 {bmi_value} 的健康分类是: {category}")

    bmi_value_over = 29.1
    category_over = categorize_bmi(bmi_value_over)
    print(f"BMI值为 {bmi_value_over} 的健康分类是: {category_over}")

    # 示例：无效输入
    invalid_bmi = -5
    category_invalid = categorize_bmi(invalid_bmi)
except ValueError as e:
    print(f"错误: {e}")

# 预期输出:
# BMI值为 22.5 的健康分类是: 健康体重 (Healthy Weight)
# BMI值为 29.1 的健康分类是: 肥胖前期 (Pre-obese)
# 错误: BMI值必须是有效的正数
```

## 3. 实现细节

### 3.1. 函数签名

```python
def categorize_bmi(bmi_value: float) -> str:
```

### 3.2. 输入验证

1.  **类型转换与检查**: 函数首先尝试将 `bmi_value` 转换为 `float` 类型。如果转换失败（例如，输入为 `None` 或非数字字符串如 `"abc"`），则会抛出 `ValueError` 并提示“BMI值必须是有效的数字”。
2.  **正数校验**: 成功转换为浮点数后，函数会检查该值是否为正数。如果 `bmi_value` 小于或等于0，则会抛出 `ValueError` 并提示“BMI值必须是有效的正数”。

### 3.3. 分类逻辑

函数使用一系列 `if-elif-else` 条件语句，根据以下WHO成人BMI分类标准返回相应的分类字符串：

*   BMI < 18.5: "偏瘦 (Underweight)"
*   18.5 <= BMI < 24.0: "健康体重 (Healthy Weight)"
*   24.0 <= BMI < 28.0: "超重 (Overweight)"
*   28.0 <= BMI < 30.0: "肥胖前期 (Pre-obese)"
*   BMI >= 30.0: "肥胖 (Obese)"

边界值被精确处理，例如，BMI恰好为18.5时归类为“健康体重 (Healthy Weight)”。

## 4. 测试情况

此特性通过了全面的单元测试，覆盖了所有分类的典型值、边界值以及各种无效输入情况。

*   **测试文件**: <mcfile name="test_bmi_categorize.py" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/tests/bmi/test_bmi_categorize.py"></mcfile>
*   **测试覆盖**: 17个测试用例，全部通过。
    *   正常分类（包括各区间的典型值和边界值）。
    *   无效输入（零值、负值、非数字字符串、None）。

## 5. TDD 开发文档链接

*   **用户故事**: <mcfile name="_user_story_bmi_categorize.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_02_BMICategorization/_user_story_bmi_categorize.md"></mcfile>
*   **思考选项**: <mcfile name="_s1_think_options_bmi_categorize.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_02_BMICategorization/_s1_think_options_bmi_categorize.md"></mcfile>
*   **思考设计**: <mcfile name="_s2_think_design_bmi_categorize.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_02_BMICategorization/_s2_think_design_bmi_categorize.md"></mcfile>
*   **思考验证**: <mcfile name="_s3_think_validation_bmi_categorize.md" path="/Users/bowhead/ai_dev_exercise_tdd/ai_wellness_advisor/dev_cycles/bmi/ExTDD_02_BMICategorization/_s3_think_validation_bmi_categorize.md"></mcfile>

## 6. 依赖关系

*   Python 3.x
*   `pytest` (用于测试)

## 7. 未来可能的改进

*   允许传入自定义的分类标准，以适应不同地区或特定人群的需求。
*   提供更详细的健康建议，而不仅仅是分类名称。