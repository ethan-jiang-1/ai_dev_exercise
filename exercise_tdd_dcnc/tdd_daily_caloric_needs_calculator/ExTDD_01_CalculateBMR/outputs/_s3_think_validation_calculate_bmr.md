# 验证方案：基础代谢率（BMR）计算器

## 1. 测试用例设计思路

### 1.1 测试分类
1. **输入验证测试**：确保所有输入验证功能正常工作
2. **计算逻辑测试**：确保 BMR 计算公式正确实现
3. **边界值测试**：确保在边界条件下正常工作
4. **异常处理测试**：确保错误提示清晰准确
5. **性能测试**：确保满足性能要求

### 1.2 测试优先级
1. 首要测试：输入验证（因为这是数据进入系统的门槛）
2. 次要测试：计算逻辑（在确保输入有效后进行）
3. 补充测试：边界值和异常处理
4. 最后测试：性能要求

## 2. 具体测试用例

### 2.1 性别验证测试
```python
def test_validate_gender_valid(self):
    """测试有效的性别输入"""
    # 测试 "男" 和 "女" 都应该通过验证

def test_validate_gender_invalid(self):
    """测试无效的性别输入"""
    # 测试空字符串、其他字符串、非字符串类型等
```

### 2.2 年龄验证测试
```python
def test_validate_age_valid(self):
    """测试有效的年龄输入"""
    # 测试正常范围内的整数

def test_validate_age_invalid_type(self):
    """测试无效类型的年龄输入"""
    # 测试浮点数、字符串等非整数类型

def test_validate_age_out_of_range(self):
    """测试超出范围的年龄输入"""
    # 测试小于15和大于80的值
```

### 2.3 身高验证测试
```python
def test_validate_height_valid(self):
    """测试有效的身高输入"""
    # 测试正常范围内的数值（整数和浮点数）

def test_validate_height_invalid_type(self):
    """测试无效类型的身高输入"""
    # 测试字符串等非数字类型

def test_validate_height_out_of_range(self):
    """测试超出范围的身高输入"""
    # 测试小于130和大于230的值
```

### 2.4 体重验证测试
```python
def test_validate_weight_valid(self):
    """测试有效的体重输入"""
    # 测试正常范围内的数值（整数和浮点数）

def test_validate_weight_invalid_type(self):
    """测试无效类型的体重输入"""
    # 测试字符串等非数字类型

def test_validate_weight_out_of_range(self):
    """测试超出范围的体重输入"""
    # 测试小于30和大于150的值
```

### 2.5 BMR计算测试
```python
def test_calculate_bmr_male(self):
    """测试男性BMR计算"""
    # 使用已知输入和预期输出进行测试
    # 例如：男，25岁，175cm，70kg，预期BMR=1752.8

def test_calculate_bmr_female(self):
    """测试女性BMR计算"""
    # 使用已知输入和预期输出进行测试
    # 例如：女，25岁，165cm，55kg，预期BMR=1332.1
```

### 2.6 边界值测试
```python
def test_boundary_values(self):
    """测试各个输入的边界值"""
    # 测试年龄、身高、体重的最小和最大允许值
```

### 2.7 精度测试
```python
def test_result_precision(self):
    """测试计算结果精度"""
    # 确保结果保留一位小数
```

### 2.8 性能测试
```python
def test_performance(self):
    """测试计算性能"""
    # 确保单次计算在10ms内完成
```

## 3. 测试数据设计

### 3.1 标准测试数据
- 男性标准用例：{"gender": "男", "age": 25, "height": 175.0, "weight": 70.0}
- 女性标准用例：{"gender": "女", "age": 25, "height": 165.0, "weight": 55.0}

### 3.2 边界测试数据
- 年龄边界：15岁和80岁
- 身高边界：130cm和230cm
- 体重边界：30kg和150kg

### 3.3 无效测试数据
- 性别：["male", "female", "", "其他", 123]
- 年龄：[14, 81, 25.5, "25", None]
- 身高：[129.9, 230.1, "175", None]
- 体重：[29.9, 150.1, "70", None]

## 4. 下一步行动

1. 创建测试文件 `test_calculate_bmr.py`
2. 实现所有计划的测试用例
3. 运行测试（预期全部失败 - Red阶段）
4. 准备开始实现功能代码（Green阶段） 