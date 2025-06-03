# S2: Think Design - Calculate TDEE 详细设计

## 特性信息
- **特性名称**: ExTDD_02_CalculateTDEE
- **模块**: dcnc (Daily Caloric Needs Calculator)
- **函数**: `calculate_tdee(bmr, activity_level)`
- **设计方案**: 简单函数实现（基于S1分析结果）

## 函数签名设计

### 完整函数定义
```python
def calculate_tdee(bmr: float, activity_level: str) -> float:
    """计算每日总能量消耗（TDEE）。
    
    基于基础代谢率（BMR）和日常活动水平计算每日总能量消耗。
    使用标准活动系数进行计算：TDEE = BMR × 活动系数
    
    Args:
        bmr (float): 基础代谢率（卡路里/天），范围 500-5000
        activity_level (str): 活动水平，可选值：
            - "sedentary": 久坐，很少或没有运动 (系数: 1.2)
            - "lightly_active": 轻度活动，轻度运动1-3天/周 (系数: 1.375)
            - "moderately_active": 中度活动，中度运动3-5天/周 (系数: 1.55)
            - "very_active": 重度活动，重度运动6-7天/周 (系数: 1.725)
            - "extra_active": 极重度活动，非常重度运动或体力工作 (系数: 1.9)
    
    Returns:
        float: 每日总能量消耗（卡路里/天），保留1位小数
    
    Raises:
        TypeError: 当参数类型不正确时
        ValueError: 当参数值超出合理范围或活动水平无效时
    
    Examples:
        >>> calculate_tdee(1500, "sedentary")
        1800.0
        >>> calculate_tdee(2000, "moderately_active")
        3100.0
        >>> calculate_tdee(1800, "very_active")
        3105.0
    """
```

## 常量定义设计

### 活动系数映射
```python
# 活动水平与系数的映射关系
ACTIVITY_COEFFICIENTS = {
    'sedentary': 1.2,           # 久坐
    'lightly_active': 1.375,    # 轻度活动
    'moderately_active': 1.55,  # 中度活动
    'very_active': 1.725,       # 重度活动
    'extra_active': 1.9         # 极重度活动
}

# BMR有效范围常量
MIN_BMR = 500   # 最小合理BMR值
MAX_BMR = 5000  # 最大合理BMR值
```

### 常量设计理由
1. **活动系数**: 基于国际通用的Harris-Benedict活动系数标准
2. **BMR范围**: 覆盖从儿童到极端体型成年人的合理范围
3. **命名规范**: 使用大写字母和下划线，符合Python常量命名约定

## 参数验证设计

### 1. BMR参数验证

#### 类型验证
```python
if not isinstance(bmr, (int, float)):
    raise TypeError(f"bmr must be int or float, got {type(bmr).__name__}")
```

#### 特殊值验证
```python
import math
if math.isnan(bmr) or math.isinf(bmr):
    raise ValueError(f"bmr must be a finite number, got {bmr}")
```

#### 范围验证
```python
if not (MIN_BMR <= bmr <= MAX_BMR):
    raise ValueError(f"bmr must be between {MIN_BMR} and {MAX_BMR}, got {bmr}")
```

### 2. 活动水平参数验证

#### 类型验证
```python
if not isinstance(activity_level, str):
    raise TypeError(f"activity_level must be str, got {type(activity_level).__name__}")
```

#### 标准化处理
```python
activity_level_normalized = activity_level.lower().strip()
```

#### 有效性验证
```python
if activity_level_normalized not in ACTIVITY_COEFFICIENTS:
    valid_levels = list(ACTIVITY_COEFFICIENTS.keys())
    raise ValueError(f"activity_level must be one of {valid_levels}, got '{activity_level}'")
```

## 计算逻辑设计

### 核心计算
```python
# 获取活动系数
activity_coefficient = ACTIVITY_COEFFICIENTS[activity_level_normalized]

# 计算TDEE
tdee = bmr * activity_coefficient

# 保留1位小数
return round(tdee, 1)
```

### 计算验证
- **公式**: TDEE = BMR × 活动系数
- **精度**: 使用round()函数保留1位小数
- **范围**: 结果应在600-9500之间（基于BMR和系数范围）

## 完整实现设计

### 函数实现结构
```python
def calculate_tdee(bmr: float, activity_level: str) -> float:
    """文档字符串..."""
    
    # 1. BMR类型验证
    if not isinstance(bmr, (int, float)):
        raise TypeError(f"bmr must be int or float, got {type(bmr).__name__}")
    
    # 2. 活动水平类型验证
    if not isinstance(activity_level, str):
        raise TypeError(f"activity_level must be str, got {type(activity_level).__name__}")
    
    # 3. BMR特殊值验证
    import math
    if math.isnan(bmr) or math.isinf(bmr):
        raise ValueError(f"bmr must be a finite number, got {bmr}")
    
    # 4. BMR范围验证
    if not (MIN_BMR <= bmr <= MAX_BMR):
        raise ValueError(f"bmr must be between {MIN_BMR} and {MAX_BMR}, got {bmr}")
    
    # 5. 活动水平标准化
    activity_level_normalized = activity_level.lower().strip()
    
    # 6. 活动水平有效性验证
    if activity_level_normalized not in ACTIVITY_COEFFICIENTS:
        valid_levels = list(ACTIVITY_COEFFICIENTS.keys())
        raise ValueError(f"activity_level must be one of {valid_levels}, got '{activity_level}'")
    
    # 7. 计算TDEE
    activity_coefficient = ACTIVITY_COEFFICIENTS[activity_level_normalized]
    tdee = bmr * activity_coefficient
    
    # 8. 返回结果（保留1位小数）
    return round(tdee, 1)
```

## 测试用例设计

### 1. 正常计算测试

#### 基础测试用例
```python
class TestCalculateTDEENormalCases:
    def test_sedentary_activity(self):
        # BMR=1500, sedentary → 1500 * 1.2 = 1800.0
        assert calculate_tdee(1500, "sedentary") == 1800.0
    
    def test_lightly_active(self):
        # BMR=1600, lightly_active → 1600 * 1.375 = 2200.0
        assert calculate_tdee(1600, "lightly_active") == 2200.0
    
    def test_moderately_active(self):
        # BMR=1800, moderately_active → 1800 * 1.55 = 2790.0
        assert calculate_tdee(1800, "moderately_active") == 2790.0
    
    def test_very_active(self):
        # BMR=2000, very_active → 2000 * 1.725 = 3450.0
        assert calculate_tdee(2000, "very_active") == 3450.0
    
    def test_extra_active(self):
        # BMR=2200, extra_active → 2200 * 1.9 = 4180.0
        assert calculate_tdee(2200, "extra_active") == 4180.0
```

### 2. 边界值测试

```python
class TestCalculateTDEEBoundaryValues:
    def test_minimum_bmr(self):
        # 最小BMR值
        result = calculate_tdee(500, "sedentary")
        assert result == 600.0
    
    def test_maximum_bmr(self):
        # 最大BMR值
        result = calculate_tdee(5000, "extra_active")
        assert result == 9500.0
```

### 3. 大小写不敏感测试

```python
class TestCalculateTDEECaseInsensitive:
    def test_uppercase_activity_level(self):
        assert calculate_tdee(1500, "SEDENTARY") == 1800.0
    
    def test_mixed_case_activity_level(self):
        assert calculate_tdee(1600, "Lightly_Active") == 2200.0
    
    def test_activity_level_with_spaces(self):
        assert calculate_tdee(1800, " moderately_active ") == 2790.0
```

### 4. 类型错误测试

```python
class TestCalculateTDEETypeErrors:
    def test_bmr_string_type(self):
        with pytest.raises(TypeError, match="bmr must be int or float"):
            calculate_tdee("1500", "sedentary")
    
    def test_activity_level_numeric_type(self):
        with pytest.raises(TypeError, match="activity_level must be str"):
            calculate_tdee(1500, 1.2)
```

### 5. 值错误测试

```python
class TestCalculateTDEEValueErrors:
    def test_bmr_too_low(self):
        with pytest.raises(ValueError, match="bmr must be between 500 and 5000"):
            calculate_tdee(400, "sedentary")
    
    def test_bmr_too_high(self):
        with pytest.raises(ValueError, match="bmr must be between 500 and 5000"):
            calculate_tdee(6000, "sedentary")
    
    def test_invalid_activity_level(self):
        with pytest.raises(ValueError, match="activity_level must be one of"):
            calculate_tdee(1500, "invalid_level")
```

### 6. 返回类型和精度测试

```python
class TestCalculateTDEEReturnType:
    def test_return_type_is_float(self):
        result = calculate_tdee(1500, "sedentary")
        assert isinstance(result, float)
    
    def test_result_precision_one_decimal(self):
        # 测试精度保留
        result = calculate_tdee(1333, "lightly_active")  # 1333 * 1.375 = 1832.875
        assert result == 1832.9
    
    def test_result_is_positive(self):
        result = calculate_tdee(500, "sedentary")
        assert result > 0
```

## 文件结构设计

### 源代码文件
**路径**: `/src/dcnc/calculate_tdee.py`

```python
"""TDEE (Total Daily Energy Expenditure) calculation module.

This module provides functionality to calculate daily total energy expenditure
based on BMR and activity level.
"""

import math

# 活动水平系数常量
ACTIVITY_COEFFICIENTS = {
    'sedentary': 1.2,
    'lightly_active': 1.375,
    'moderately_active': 1.55,
    'very_active': 1.725,
    'extra_active': 1.9
}

# BMR有效范围常量
MIN_BMR = 500
MAX_BMR = 5000


def calculate_tdee(bmr: float, activity_level: str) -> float:
    # 实现代码...
```

### 测试文件
**路径**: `/tests/dcnc/test_calculate_tdee.py`

```python
"""Tests for TDEE calculation functionality."""

import pytest
import math
from src.dcnc.calculate_tdee import calculate_tdee

# 测试类和方法...
```

## 性能和扩展性考虑

### 性能优化
1. **字典查找**: O(1)时间复杂度的活动系数查找
2. **常量缓存**: 模块级常量避免重复创建
3. **最小计算**: 简单的乘法运算，性能优秀

### 扩展性设计
1. **新活动水平**: 只需在ACTIVITY_COEFFICIENTS中添加新项
2. **自定义系数**: 未来可考虑添加可选参数支持自定义系数
3. **国际化**: 错误消息可提取为常量便于翻译

## 实现细节

### 导入策略
- 使用标准库`math`模块进行特殊值检查
- 避免不必要的外部依赖

### 错误消息设计
- 提供清晰、具体的错误信息
- 包含期望值和实际值
- 便于调试和用户理解

### 代码风格
- 遵循PEP 8编码规范
- 使用类型提示增强代码可读性
- 详细的文档字符串和注释

## 下一步行动

### S3阶段：设计验证
1. 验证函数签名的完整性和正确性
2. 检查测试用例的覆盖度和有效性
3. 确认错误处理的完备性
4. 验证性能和扩展性要求
5. 检查与现有代码的一致性

### 关键设计决策
- ✅ 函数签名确定
- ✅ 常量定义完成
- ✅ 验证逻辑设计
- ✅ 测试用例规划
- ✅ 文件结构确定

---

**设计完成时间**: 当前  
**设计复杂度**: 中等  
**实现预估时间**: 30-45分钟  
**下一阶段**: S3 - Think Validation