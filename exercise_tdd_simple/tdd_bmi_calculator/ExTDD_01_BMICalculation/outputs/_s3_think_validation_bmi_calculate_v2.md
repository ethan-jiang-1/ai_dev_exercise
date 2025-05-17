# BMI 计算器验证方案（v2 - 支持多单位）

## 1. 验证范围

本验证方案主要针对新增的单位转换功能，包括：
1. 身高单位转换函数 `convert_height_to_meters`
2. 体重单位转换函数 `convert_weight_to_kg`
3. 与原有 `bmi_calculate` 函数的集成测试

## 2. 测试用例设计

### 2.1 身高转换函数测试用例

#### A. 公制单位（米）测试
```python
def test_height_meters_direct():
    """测试米单位直接转换"""
    cases = [
        (1.75, 1.75),    # 常规身高
        (0.1, 0.1),      # 最小有效值
        (3.0, 3.0),      # 最大有效值
        (2, 2.0),        # 整数输入
        (1.685, 1.685)   # 精确小数
    ]
    for input_height, expected in cases:
        result = convert_height_to_meters(input_height, "m")
        assert abs(result - expected) < 0.01
```

#### B. 英制单位（英尺/英寸）测试
```python
def test_height_feet_inches():
    """测试英尺/英寸转换"""
    cases = [
        ((5, 9), 1.75),    # 5英尺9英寸 ≈ 1.75米
        ((6, 0), 1.83),    # 6英尺 ≈ 1.83米
        ((4, 0), 1.22),    # 4英尺 ≈ 1.22米
        ((5, 11.5), 1.82), # 带小数的英寸
        ((1, 0), 0.30),    # 最小边界
        ((10, 0), 3.05)    # 最大边界
    ]
    for (feet, inches), expected in cases:
        result = convert_height_to_meters((feet, inches), "ft_in")
        assert abs(result - expected) < 0.01
```

#### C. 异常情况测试
```python
def test_height_conversion_errors():
    """测试身高转换的异常情况"""
    error_cases = [
        # 类型错误
        ((None, "m"), TypeError),
        ((True, "m"), TypeError),
        (("170", "m"), TypeError),
        ((1.75, None), TypeError),
        
        # 值错误
        ((0, "m"), ValueError),
        ((-1.75, "m"), ValueError),
        ((3.1, "m"), ValueError),
        (((0, 5), "ft_in"), ValueError),
        (((11, 0), "ft_in"), ValueError),
        (((5, 12), "ft_in"), ValueError),
        (((5, -1), "ft_in"), ValueError),
        ((1.75, "invalid"), ValueError)
    ]
    for (height, unit), error_type in error_cases:
        with pytest.raises(error_type):
            convert_height_to_meters(height, unit)
```

### 2.2 体重转换函数测试用例

#### A. 公制单位（千克）测试
```python
def test_weight_kg_direct():
    """测试千克单位直接转换"""
    cases = [
        (70, 70),        # 常规体重
        (0.1, 0.1),      # 最小有效值
        (300, 300),      # 最大有效值
        (65.5, 65.5),    # 小数值
        (100, 100)       # 整数值
    ]
    for input_weight, expected in cases:
        result = convert_weight_to_kg(input_weight, "kg")
        assert abs(result - expected) < 0.01
```

#### B. 英制单位（磅）测试
```python
def test_weight_pounds():
    """测试磅转换为千克"""
    cases = [
        (154, 69.85),    # 154磅 ≈ 69.85千克
        (220, 99.79),    # 220磅 ≈ 99.79千克
        (110.5, 50.12),  # 带小数的磅值
        (0.5, 0.23),     # 最小边界
        (660, 299.37)    # 最大边界
    ]
    for input_pounds, expected_kg in cases:
        result = convert_weight_to_kg(input_pounds, "lb")
        assert abs(result - expected_kg) < 0.01
```

#### C. 异常情况测试
```python
def test_weight_conversion_errors():
    """测试体重转换的异常情况"""
    error_cases = [
        # 类型错误
        ((None, "kg"), TypeError),
        ((True, "kg"), TypeError),
        (("70", "kg"), TypeError),
        ((70, None), TypeError),
        
        # 值错误
        ((0, "kg"), ValueError),
        ((-70, "kg"), ValueError),
        ((301, "kg"), ValueError),
        ((0, "lb"), ValueError),
        ((-154, "lb"), ValueError),
        ((661, "lb"), ValueError),
        ((70, "invalid"), ValueError)
    ]
    for (weight, unit), error_type in error_cases:
        with pytest.raises(error_type):
            convert_weight_to_kg(weight, unit)
```

### 2.3 集成测试用例

```python
def test_bmi_calculation_with_different_units():
    """测试不同单位组合的 BMI 计算"""
    test_cases = [
        # (身高, 身高单位, 体重, 体重单位, 期望BMI)
        (1.75, "m", 70, "kg", 22.86),          # 全公制
        ((5, 9), "ft_in", 154, "lb", 22.86),   # 全英制（等价于上面的公制值）
        (1.75, "m", 154, "lb", 22.86),         # 混合单位1
        ((5, 9), "ft_in", 70, "kg", 22.86)     # 混合单位2
    ]
    
    for height, height_unit, weight, weight_unit, expected_bmi in test_cases:
        # 转换单位
        height_m = convert_height_to_meters(height, height_unit)
        weight_kg = convert_weight_to_kg(weight, weight_unit)
        
        # 计算 BMI
        bmi = bmi_calculate(height_m, weight_kg)
        
        # 验证结果
        assert abs(bmi - expected_bmi) < 0.01
```

## 3. 验证策略

### 3.1 单元测试执行顺序
1. 先测试单位转换函数的基本功能
2. 再测试边界值和异常情况
3. 最后进行集成测试

### 3.2 测试覆盖率要求
- 代码行覆盖率 > 95%
- 分支覆盖率 100%
- 所有异常路径都必须测试

### 3.3 性能测试考虑
- 验证单位转换的计算精度
- 确保转换函数的执行时间在可接受范围内
- 验证内存使用情况

## 4. 验证环境

### 4.1 测试框架
- 使用 pytest 进行单元测试
- 使用 pytest-cov 收集覆盖率数据

### 4.2 测试数据准备
- 准备已知的单位转换对照表
- 准备边界值测试数据
- 准备异常输入数据

## 5. 验收标准

1. 所有单元测试通过
2. 代码覆盖率达标
3. 所有已知的边界情况都经过测试
4. 不同单位组合的计算结果一致（误差范围内）
5. 异常处理符合设计要求
6. 性能指标满足要求

## 6. 回归测试

确保新功能不影响原有功能：
1. 运行原有的测试套件
2. 验证原有的 BMI 计算结果不变
3. 确保错误处理机制兼容 