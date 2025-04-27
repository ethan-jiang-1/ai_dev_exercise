# User Story: Calculate BMI Value

**ID**: BMI_01
**功能名称**: calculate_bmi

**作为** 健康应用开发者，
**我希望** 有一个函数能够接收用户的体重（公斤）和身高（米），
**以便** 计算出用户的身体质量指数 (BMI) 值。

**验收标准**: 

1.  函数应接受两个参数：`weight_kg` (float) 和 `height_m` (float)。
2.  函数应返回一个 float 类型的 BMI 值，计算公式为 `weight_kg / (height_m ** 2)`。
3.  如果 `height_m` 为 0 或负数，函数应引发 `ValueError`。
4.  如果 `weight_kg` 为负数，函数应引发 `ValueError` (体重可以为0)。
5.  输入值可以为整数或浮点数，函数内部应能正确处理。
6.  返回的 BMI 值应保留合理的小数位数（例如，2位）。

**示例**:
- 输入: weight_kg = 70, height_m = 1.75
- 输出: BMI ≈ 22.86
- 输入: weight_kg = 60, height_m = 0
- 输出: ValueError
- 输入: weight_kg = -5, height_m = 1.6
- 输出: ValueError
