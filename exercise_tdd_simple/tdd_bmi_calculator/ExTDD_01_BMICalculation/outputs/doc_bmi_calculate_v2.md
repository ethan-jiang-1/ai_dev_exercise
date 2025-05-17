# BMI 计算器 V2 文档

## 功能概述

BMI计算器V2版本支持多种单位输入，可以处理公制（米、千克）和英制（英尺/英寸、磅）单位，并提供精确的BMI计算结果。

## 单位转换常量

```python
INCHES_PER_FOOT = 12
INCHES_TO_METERS = 0.0254  # 1 inch = 0.0254 meters exactly
POUNDS_TO_KG = 0.45359237  # 1 pound = 0.45359237 kg exactly
```

## 函数接口

### 1. 身高转换函数

```python
def convert_height_to_meters(
    height: float | tuple[float, float],
    unit: str = "m"
) -> float:
```

#### 参数说明
- `height`: 身高值
  - 当unit为"m"时：float类型，单位为米
  - 当unit为"ft_in"时：tuple类型，格式为(英尺, 英寸)
- `unit`: 输入单位
  - "m": 米
  - "ft_in": 英尺/英寸

#### 返回值
- float类型，转换后的身高（米）

#### 异常
- TypeError: 输入类型错误
- ValueError: 单位类型错误或输入值无效

### 2. 体重转换函数

```python
def convert_weight_to_kg(
    weight: float,
    unit: str = "kg"
) -> float:
```

#### 参数说明
- `weight`: 体重值（float类型）
- `unit`: 输入单位
  - "kg": 千克
  - "lb": 磅

#### 返回值
- float类型，转换后的体重（千克）

#### 异常
- TypeError: 输入类型错误
- ValueError: 单位类型错误或输入值无效

### 3. BMI计算函数

```python
def bmi_calculate(
    height_m: float,
    weight_kg: float
) -> float:
```

#### 参数说明
- `height_m`: 身高（米）
- `weight_kg`: 体重（千克）

#### 返回值
- float类型，BMI值（保留两位小数）

#### 异常
- TypeError: 输入参数类型错误
- ValueError: 输入参数无效或计算结果超出范围

## 精度说明

### 单位转换精度

1. 英制到公制的转换使用精确的转换系数：
   - 1英寸 = 0.0254米（精确值）
   - 1磅 = 0.45359237千克（精确值）

2. 转换过程保持高精度，避免中间舍入

### BMI计算精度

1. BMI计算保持高精度直到最终结果
2. 最终结果四舍五入到两位小数

### 不同单位组合的BMI值差异说明

由于单位转换的精确性，相同输入在不同单位组合下可能得到略微不同的BMI值。例如：

1. 全公制单位：
   ```
   身高: 1.75米
   体重: 70千克
   BMI = 22.86
   ```

2. 全英制单位：
   ```
   身高: 5英尺9英寸 (≈ 1.7526米)
   体重: 154磅 (≈ 69.85322498千克)
   BMI = 22.74
   ```

3. 混合单位1：
   ```
   身高: 1.75米
   体重: 154磅 (≈ 69.85322498千克)
   BMI = 22.81
   ```

4. 混合单位2：
   ```
   身高: 5英尺9英寸 (≈ 1.7526米)
   体重: 70千克
   BMI = 22.79
   ```

这些差异是正确的，因为：
1. 5'9"转换为米的精确值（1.7526米）与1.75米有细微差异
2. 所有计算都使用精确的转换系数
3. 最终BMI值的差异反映了实际的身高差异

## 使用示例

```python
# 示例1：全公制单位
height_m = convert_height_to_meters(1.75, "m")
weight_kg = convert_weight_to_kg(70, "kg")
bmi = bmi_calculate(height_m, weight_kg)  # 22.86

# 示例2：全英制单位
height_m = convert_height_to_meters((5, 9), "ft_in")
weight_kg = convert_weight_to_kg(154, "lb")
bmi = bmi_calculate(height_m, weight_kg)  # 22.74

# 示例3：混合单位
height_m = convert_height_to_meters(1.75, "m")
weight_kg = convert_weight_to_kg(154, "lb")
bmi = bmi_calculate(height_m, weight_kg)  # 22.81
```

## 注意事项

1. 输入范围限制：
   - 身高（米）：0.1 - 3.05
   - 身高（英尺）：1 - 10
   - 英寸：0 - 11.99
   - 体重（千克）：0.1 - 300
   - 体重（磅）：0.2 - 660

2. BMI值范围：
   - 有效范围：1 - 100
   - 超出范围将抛出ValueError

3. 精度考虑：
   - 所有中间计算保持高精度
   - 只在最终BMI结果中进行四舍五入
   - 不同单位组合可能产生轻微的BMI值差异（≤0.1） 