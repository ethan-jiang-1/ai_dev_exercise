# 用户故事: BMI计算器

**ID**: BMI_01
**功能名称**: bmi_calculate

## 用户故事

**作为** 健康应用的开发者，
**我希望** 有一个函数能够计算用户的BMI值，
**以便** 在健康应用中为用户提供身体状况的基本指标。

## 详细描述

体质指数（Body Mass Index, 简称BMI）是评价体重与身高关系的常用指标，用于衡量一个人的体重是否处于健康范围。BMI的计算公式是：体重(kg)除以身高(m)的平方。

这个功能需要一个函数，接收用户的体重（千克）和身高（米）作为输入，计算并返回用户的BMI值。计算结果应该四舍五入到小数点后两位，以保证适当的精度。

## 验收标准

1. **输入验证**:
   - 当身高小于或等于0时，函数应该抛出ValueError异常
   - 当体重小于0时，函数应该抛出ValueError异常
   - 函数应该能够处理整数和浮点数类型的输入

2. **计算准确性**:
   - 函数应该使用公式 BMI = 体重(kg) / 身高(m)² 进行计算
   - 计算结果应该精确到小数点后两位（四舍五入）
   
3. **边界情况**:
   - 当体重为0时，函数应该返回0

## 示例

- **Example 1**:
  - 输入: weight_kg = 70, height_m = 1.75
  - 输出: 22.86
  
- **Example 2**:
  - 输入: weight_kg = 0, height_m = 1.8
  - 输出: 0.0
  
- **Example 3**:
  - 输入: weight_kg = 60, height_m = 0
  - 输出: ValueError("Height must be greater than zero")
  
- **Example 4**:
  - 输入: weight_kg = -5, height_m = 1.6
  - 输出: ValueError("Weight must be greater than or equal to zero") 