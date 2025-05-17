# BMI 计算功能 - 验证思路

## 1. 验证策略概述

基于 TDD (测试驱动开发) 的原则，我们将：
1. 先编写测试用例，确保它们都失败（红色阶段）
2. 然后实现功能代码使测试通过（绿色阶段）
3. 最后进行代码优化（重构阶段）

## 2. 测试框架选择

- 使用 Python 标准库的 `unittest` 模块
- 创建 `TestBMICalculate` 测试类
- 每个测试场景使用一个独立的测试方法

## 3. 测试用例实现计划

### 3.1 正常情况测试方法

```python
def test_normal_weight_height(self):
    """测试正常体重和身高的情况"""
    # 身高 1.75 米，体重 70 千克，预期 BMI 约为 22.86
    result = bmi_calculate(1.75, 70)
    self.assertEqual(result, 22.86)

def test_integer_inputs(self):
    """测试整数输入的情况"""
    # 身高 2 米，体重 80 千克，预期 BMI 为 20.00
    result = bmi_calculate(2, 80)
    self.assertEqual(result, 20.00)

def test_decimal_inputs(self):
    """测试小数输入的情况"""
    # 身高 1.68 米，体重 58.5 千克，预期 BMI 约为 20.73
    result = bmi_calculate(1.68, 58.5)
    self.assertEqual(result, 20.73)
```

### 3.2 边界情况测试方法

```python
def test_very_small_valid_values(self):
    """测试极小的有效值"""
    # 身高 0.1 米，体重 0.1 千克，确保计算正确
    result = bmi_calculate(0.1, 0.1)
    self.assertEqual(result, 10.00)

def test_very_large_valid_values(self):
    """测试较大的有效值"""
    # 身高 3 米，体重 300 千克
    result = bmi_calculate(3, 300)
    self.assertEqual(result, 33.33)
```

### 3.3 异常情况测试方法

```python
def test_type_error_string_input(self):
    """测试字符串输入"""
    with self.assertRaises(TypeError):
        bmi_calculate("170", "60")

def test_type_error_none_input(self):
    """测试 None 输入"""
    with self.assertRaises(TypeError):
        bmi_calculate(None, None)

def test_type_error_boolean_input(self):
    """测试布尔值输入"""
    with self.assertRaises(TypeError):
        bmi_calculate(True, False)

def test_value_error_zero_input(self):
    """测试零值输入"""
    with self.assertRaises(ValueError):
        bmi_calculate(0, 70)
    with self.assertRaises(ValueError):
        bmi_calculate(1.75, 0)

def test_value_error_negative_input(self):
    """测试负值输入"""
    with self.assertRaises(ValueError):
        bmi_calculate(-1.75, 70)
    with self.assertRaises(ValueError):
        bmi_calculate(1.75, -70)
```

## 4. 验证要点

1. **精度验证**:
   - 确保所有计算结果都正确保留两位小数
   - 验证四舍五入的正确性

2. **异常信息验证**:
   - 确保抛出的异常类型正确
   - 验证异常信息的文本内容清晰准确

3. **边界条件验证**:
   - 确保函数能处理极小的有效输入
   - 确保函数能处理较大的有效输入

4. **类型处理验证**:
   - 验证函数能正确处理整数和浮点数混合输入
   - 确保对无效类型输入的正确处理

## 5. 测试执行策略

1. 先运行所有测试，确保它们都失败（红色阶段）
2. 实现最简单的代码使测试通过
3. 逐步完善实现，确保测试持续通过
4. 进行代码重构，确保测试仍然通过

## 6. 预期的测试结果

- 所有正常情况测试应返回正确的 BMI 值
- 所有异常情况测试应抛出预期的异常
- 所有边界情况测试应正确处理并返回合理结果

接下来，我们将基于这个验证策略创建具体的测试代码文件 `test_bmi_calculate.py`。 