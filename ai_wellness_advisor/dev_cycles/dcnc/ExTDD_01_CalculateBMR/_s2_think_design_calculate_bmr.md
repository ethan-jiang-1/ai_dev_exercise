# S2: Think Design - Calculate BMR 详细设计

## 特性标识
- **模块名**: dcnc
- **特性名**: calculate_bmr
- **TDD周期**: ExTDD_01_CalculateBMR
- **阶段**: S2 - 详细设计

## 设计概述

基于S1阶段的分析，采用简单函数实现方案，创建一个纯函数来计算基础代谢率（BMR）。

## 函数设计

### 函数签名
```python
def calculate_bmr(gender: str, age: int, height: float, weight: float) -> float:
    """计算基础代谢率（BMR）。
    
    使用Harris-Benedict公式计算每日基础代谢率。
    
    Args:
        gender (str): 性别，"male" 或 "female"
        age (int): 年龄（岁），范围 1-120
        height (float): 身高（厘米），范围 50-300
        weight (float): 体重（千克），范围 10-500
    
    Returns:
        float: 每日基础代谢率（卡路里/天），保留1位小数
    
    Raises:
        TypeError: 当参数类型不正确时
        ValueError: 当参数值超出合理范围或性别无效时
    """
```

### 算法设计

#### Harris-Benedict公式
- **男性**: BMR = 88.362 + (13.397 × 体重kg) + (4.799 × 身高cm) - (5.677 × 年龄)
- **女性**: BMR = 447.593 + (9.247 × 体重kg) + (3.098 × 身高cm) - (4.330 × 年龄)

#### 实现流程
1. **参数类型验证**
2. **参数值范围验证**
3. **性别值验证**
4. **根据性别选择公式计算**
5. **结果四舍五入到1位小数**
6. **返回结果**

## 验证逻辑设计

### 参数验证规则

| 参数 | 类型检查 | 值范围检查 | 错误类型 |
|------|----------|------------|----------|
| gender | str | "male" 或 "female" | TypeError/ValueError |
| age | int | 1 ≤ age ≤ 120 | TypeError/ValueError |
| height | int/float | 50 ≤ height ≤ 300 | TypeError/ValueError |
| weight | int/float | 10 ≤ weight ≤ 500 | TypeError/ValueError |

### 验证实现策略

```python
# 类型验证
if not isinstance(gender, str):
    raise TypeError(f"gender must be str, got {type(gender).__name__}")

if not isinstance(age, int):
    raise TypeError(f"age must be int, got {type(age).__name__}")

if not isinstance(height, (int, float)):
    raise TypeError(f"height must be int or float, got {type(height).__name__}")

if not isinstance(weight, (int, float)):
    raise TypeError(f"weight must be int or float, got {type(weight).__name__}")

# 值范围验证
if gender.lower() not in ['male', 'female']:
    raise ValueError(f"gender must be 'male' or 'female', got '{gender}'")

if not (1 <= age <= 120):
    raise ValueError(f"age must be between 1 and 120, got {age}")

if not (50 <= height <= 300):
    raise ValueError(f"height must be between 50 and 300 cm, got {height}")

if not (10 <= weight <= 500):
    raise ValueError(f"weight must be between 10 and 500 kg, got {weight}")
```

## 测试用例设计

### 正常情况测试

| 测试用例 | gender | age | height | weight | 期望BMR | 描述 |
|----------|--------|-----|--------|--------|---------|------|
| test_male_bmr_1 | "male" | 30 | 175 | 70 | 1680.0 | 标准成年男性 |
| test_male_bmr_2 | "male" | 25 | 180 | 80 | 1847.9 | 高大男性 |
| test_female_bmr_1 | "female" | 25 | 160 | 55 | 1350.0 | 标准成年女性 |
| test_female_bmr_2 | "female" | 35 | 165 | 65 | 1442.4 | 中年女性 |

### 边界值测试

| 测试用例 | 参数 | 值 | 期望结果 |
|----------|------|----|---------|
| test_min_age | age | 1 | 正常计算 |
| test_max_age | age | 120 | 正常计算 |
| test_min_height | height | 50 | 正常计算 |
| test_max_height | height | 300 | 正常计算 |
| test_min_weight | weight | 10 | 正常计算 |
| test_max_weight | weight | 500 | 正常计算 |

### 异常情况测试

| 测试用例 | 输入 | 期望异常 | 错误信息 |
|----------|------|----------|----------|
| test_invalid_gender_type | gender=123 | TypeError | "gender must be str" |
| test_invalid_gender_value | gender="unknown" | ValueError | "gender must be 'male' or 'female'" |
| test_invalid_age_type | age="30" | TypeError | "age must be int" |
| test_invalid_age_negative | age=-5 | ValueError | "age must be between 1 and 120" |
| test_invalid_height_type | height="175" | TypeError | "height must be int or float" |
| test_invalid_weight_zero | weight=0 | ValueError | "weight must be between 10 and 500" |

## 文件结构设计

```
ai_wellness_advisor/
├── src/dcnc/
│   ├── __init__.py
│   ├── calculate_bmr.py          # BMR计算函数实现
│   └── README_calculate_bmr.md   # 功能说明文档
└── tests/dcnc/
    ├── __init__.py
    └── test_calculate_bmr.py     # BMR计算测试用例
```

## 实现细节

### 常量定义
```python
# Harris-Benedict公式常量
MALE_BMR_CONSTANTS = {
    'base': 88.362,
    'weight_factor': 13.397,
    'height_factor': 4.799,
    'age_factor': 5.677
}

FEMALE_BMR_CONSTANTS = {
    'base': 447.593,
    'weight_factor': 9.247,
    'height_factor': 3.098,
    'age_factor': 4.330
}
```

### 计算逻辑
```python
def _calculate_bmr_male(age: int, height: float, weight: float) -> float:
    """计算男性BMR"""
    constants = MALE_BMR_CONSTANTS
    return (constants['base'] + 
            constants['weight_factor'] * weight + 
            constants['height_factor'] * height - 
            constants['age_factor'] * age)

def _calculate_bmr_female(age: int, height: float, weight: float) -> float:
    """计算女性BMR"""
    constants = FEMALE_BMR_CONSTANTS
    return (constants['base'] + 
            constants['weight_factor'] * weight + 
            constants['height_factor'] * height - 
            constants['age_factor'] * age)
```

## 性能考虑

- **时间复杂度**: O(1) - 简单的数学计算
- **空间复杂度**: O(1) - 只使用常量空间
- **预期性能**: 每次调用 < 1ms

## 扩展性考虑

1. **支持其他公式**: 可以添加Mifflin-St Jeor公式等
2. **支持更多性别选项**: 可以扩展支持非二元性别
3. **国际化**: 可以支持不同的单位系统
4. **缓存**: 对于相同输入可以添加缓存机制

## 下一步行动

1. 创建验证文档（S3阶段）
2. 编写测试用例（TDD Red阶段）
3. 实现函数（TDD Green阶段）
4. 重构优化（TDD Refactor阶段）