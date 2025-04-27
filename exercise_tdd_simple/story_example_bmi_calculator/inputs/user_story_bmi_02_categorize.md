# User Story: Categorize BMI Value

**ID**: BMI_02
**功能名称**: categorize_bmi

**作为** 健康应用开发者，
**我希望** 有一个函数能够接收一个计算好的 BMI 值，
**以便** 根据世界卫生组织 (WHO) 的标准，返回对应的 BMI 分类。

**验收标准**: 

1.  函数应接受一个参数：`bmi` (float)。
2.  函数应根据以下标准返回一个字符串分类：
    *   `bmi < 18.5` → "Underweight"
    *   `18.5 <= bmi < 25` → "Normal"
    *   `25 <= bmi < 30` → "Overweight"
    *   `bmi >= 30` → "Obese"
3.  如果输入的 `bmi` 值为负数，函数应引发 `ValueError`。
4.  输入值可以为整数或浮点数，函数内部应能正确处理。
5.  边界值应按标准正确分类 (例如, BMI 18.5 应分类为 "Normal", BMI 25 应分类为 "Overweight", BMI 30 应分类为 "Obese")。

**示例**:
- 输入: bmi = 17.0
- 输出: "Underweight"
- 输入: bmi = 22.5
- 输出: "Normal"
- 输入: bmi = 27.8
- 输出: "Overweight"
- 输入: bmi = 35.1
- 输出: "Obese"
- 输入: bmi = 18.5
- 输出: "Normal"
- 输入: bmi = -5.0
- 输出: ValueError 