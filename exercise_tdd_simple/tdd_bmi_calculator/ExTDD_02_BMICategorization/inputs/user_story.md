# 用户故事: BMI分类器

**ID**: BMI_02
**功能名称**: bmi_categorize

## 用户故事

**作为** 健康应用的开发者，
**我希望** 有一个函数能够根据BMI值确定用户的体重状态类别，
**以便** 向用户提供有关其健康状况的明确反馈。

## 详细描述

在计算出用户的BMI值后，需要将这个数值转化为有意义的分类，以便用户理解自己的健康状况。世界卫生组织(WHO)定义了标准的BMI分类标准，将BMI值分为四个主要类别：过轻、正常、超重和肥胖。

这个功能需要一个函数，接收BMI值作为输入，然后返回相应的分类结果。函数应该能够处理所有有效的BMI值，并对无效输入（如负值）进行适当的错误处理。

## 验收标准

1. **输入验证**:
   - 当BMI值为负数时，函数应该抛出ValueError异常
   - 函数应该能够处理整数和浮点数类型的BMI输入

2. **分类准确性**:
   - 函数应该根据以下标准准确分类BMI值：
     * BMI < 18.5：返回"Underweight"
     * 18.5 ≤ BMI < 25.0：返回"Normal"
     * 25.0 ≤ BMI < 30.0：返回"Overweight"
     * BMI ≥ 30.0：返回"Obese"

3. **边界处理**:
   - 函数应该正确处理分类边界值
   - 例如，BMI值为18.5应归类为"Normal"，而不是"Underweight"
   - BMI值为25.0应归类为"Overweight"，而不是"Normal"
   - BMI值为30.0应归类为"Obese"，而不是"Overweight"

## 示例

- **Example 1**:
  - 输入: bmi = 17.5
  - 输出: "Underweight"
  
- **Example 2**:
  - 输入: bmi = 18.5
  - 输出: "Normal"
  
- **Example 3**:
  - 输入: bmi = 24.9
  - 输出: "Normal"
  
- **Example 4**:
  - 输入: bmi = 25.0
  - 输出: "Overweight"
  
- **Example 5**:
  - 输入: bmi = 29.9
  - 输出: "Overweight"
  
- **Example 6**:
  - 输入: bmi = 30.0
  - 输出: "Obese"
  
- **Example 7**:
  - 输入: bmi = 35.5
  - 输出: "Obese"
  
- **Example 8**:
  - 输入: bmi = -5.0
  - 输出: ValueError("BMI cannot be negative") 