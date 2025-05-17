# BMI 计算器详细设计方案（v2 - 支持多单位）

## 1. 单位转换常量定义

```python
# 单位转换常量
INCHES_PER_FOOT = 12
INCHES_TO_METERS = 0.0254
POUNDS_TO_KG = 0.45359237

# 单位类型常量
HEIGHT_UNIT_METERS = "m"
HEIGHT_UNIT_FT_IN = "ft_in"
WEIGHT_UNIT_KG = "kg"
WEIGHT_UNIT_LB = "lb"
```

## 2. 函数接口设计

### 2.1 身高单位转换函数

```python
def convert_height_to_meters(
    height: float | tuple[float, float],
    unit: str = HEIGHT_UNIT_METERS
) -> float:
    """
    将身高转换为米
    
    参数:
        height: 身高值
            - float: 米为单位的身高，或英尺为单位的身高
            - tuple: (英尺, 英寸)的身高
        unit: 输入单位，"m" 或 "ft_in"
            
    返回:
        float: 转换后的身高（米）
        
    异常:
        TypeError: 输入类型错误
        ValueError: 单位类型错误或输入值无效
    """
```

### 2.2 体重单位转换函数

```python
def convert_weight_to_kg(
    weight: float,
    unit: str = WEIGHT_UNIT_KG
) -> float:
    """
    将体重转换为千克
    
    参数:
        weight: 体重值
        unit: 输入单位，"kg" 或 "lb"
            
    返回:
        float: 转换后的体重（千克）
        
    异常:
        TypeError: 输入类型错误
        ValueError: 单位类型错误或输入值无效
    """
```

## 3. 实现细节

### 3.1 身高转换实现要点

1. 类型检查：
   - 检查 height 是否为 float 或 tuple[float, float]
   - 检查 unit 是否为字符串

2. 单位验证：
   - 验证 unit 是否为有效值（"m" 或 "ft_in"）
   - 对于 "ft_in" 单位，验证 tuple 长度为 2

3. 值范围验证：
   - 米：0.1 到 3.0
   - 英尺：1 到 10
   - 英寸：0 到 11

4. 转换逻辑：
   ```python
   if unit == "m":
       return height  # 直接返回
   elif unit == "ft_in":
       feet, inches = height
       total_inches = feet * INCHES_PER_FOOT + inches
       return total_inches * INCHES_TO_METERS
   ```

### 3.2 体重转换实现要点

1. 类型检查：
   - 检查 weight 是否为数字类型
   - 检查 unit 是否为字符串

2. 单位验证：
   - 验证 unit 是否为有效值（"kg" 或 "lb"）

3. 值范围验证：
   - 千克：0.1 到 300
   - 磅：0.2 到 660

4. 转换逻辑：
   ```python
   if unit == "kg":
       return weight  # 直接返回
   elif unit == "lb":
       return weight * POUNDS_TO_KG
   ```

## 4. 错误处理策略

### 4.1 TypeError 情况
- 输入参数类型错误
- 布尔值作为数字输入
- None 值输入

### 4.2 ValueError 情况
- 无效的单位类型
- 数值超出有效范围
- 英寸值超过 11
- 负数或零值输入

### 4.3 错误消息模板
```python
ERROR_MESSAGES = {
    "invalid_height_unit": "身高单位必须是 'm' 或 'ft_in'",
    "invalid_weight_unit": "体重单位必须是 'kg' 或 'lb'",
    "invalid_height_type": "身高必须是数字或(英尺,英寸)元组",
    "invalid_weight_type": "体重必须是数字",
    "invalid_inches": "英寸必须在 0-11 范围内",
    "height_out_of_range": "身高超出有效范围",
    "weight_out_of_range": "体重超出有效范围"
}
```

## 5. 测试策略

### 5.1 身高转换测试
1. 正常情况测试：
   - 米到米的转换
   - 英尺/英寸到米的转换
   - 整数和小数输入
   
2. 边界值测试：
   - 最小有效身高
   - 最大有效身高
   - 11 英寸边界
   
3. 错误情况测试：
   - 无效单位
   - 无效类型
   - 超出范围的值
   - 非法英寸值（>11）

### 5.2 体重转换测试
1. 正常情况测试：
   - 千克到千克的转换
   - 磅到千克的转换
   - 整数和小数输入
   
2. 边界值测试：
   - 最小有效体重
   - 最大有效体重
   
3. 错误情况测试：
   - 无效单位
   - 无效类型
   - 超出范围的值

### 5.3 精度测试
- 验证已知输入值的精确转换
- 验证舍入行为
- 验证转换精度在 ±0.01 范围内

## 6. 示例用法

```python
# 示例 1：公制单位
height_m = convert_height_to_meters(1.75, "m")
weight_kg = convert_weight_to_kg(70, "kg")
bmi = bmi_calculate(height_m, weight_kg)  # 22.86

# 示例 2：英制单位
height_m = convert_height_to_meters((5, 9), "ft_in")  # 5英尺9英寸
weight_kg = convert_weight_to_kg(154, "lb")  # 154磅
bmi = bmi_calculate(height_m, weight_kg)  # 约22.86
```

## 7. 性能考虑

1. 计算精度：
   - 使用标准浮点数运算
   - 关键转换系数使用高精度常量
   - 结果统一保留两位小数

2. 内存使用：
   - 仅使用基本数据类型
   - 无需维护状态
   - 常量定义集中管理

3. 执行效率：
   - 简单的数学运算
   - 最小化条件判断
   - 无循环操作 