# 基础代谢率(BMR)计算器使用文档

## 1. 简介

基础代谢率(BMR, Basal Metabolic Rate)计算器是一个用于计算人体每日维持基本生命活动所需能量的工具。本模块使用Harris-Benedict公式进行计算，该公式是目前最广泛使用的BMR计算公式之一。

## 2. 安装要求

- Python 3.12 或更高版本
- 不需要额外的第三方依赖

## 3. 功能特性

- 支持男性和女性的BMR计算
- 严格的输入验证
- 精确的计算结果（四舍五入到整数）
- 完善的错误处理
- 类型提示支持

## 4. API参考

### 4.1 PersonData类

用于存储和验证个人数据的数据类。

```python
@dataclass
class PersonData:
    gender: Literal["男", "女"]  # 性别
    age: int                    # 年龄(岁)
    height: float              # 身高(cm)
    weight: float              # 体重(kg)
```

#### 参数约束：

- gender: 只接受"男"或"女"
- age: 0-120的整数
- height: 30-250的浮点数
- weight: 2-300的浮点数

### 4.2 calculate_bmr函数

计算基础代谢率的主函数。

```python
def calculate_bmr(person: PersonData) -> int:
    """返回每日基础代谢率（单位：kcal/天）"""
```

#### Harris-Benedict公式：

- 男性：BMR = 66.5 + (13.75 × 体重kg) + (5.003 × 身高cm) - (6.755 × 年龄)
- 女性：BMR = 655.1 + (9.563 × 体重kg) + (1.850 × 身高cm) - (4.676 × 年龄)

### 4.3 异常处理

模块定义了自定义异常类`BMRInputError`，继承自`ValueError`：

- 当输入数据验证失败时抛出`BMRInputError`
- 当计算过程出错时抛出`ValueError`

## 5. 使用示例

### 5.1 基本使用

```python
from calculate_bmr import PersonData, calculate_bmr

try:
    # 创建个人数据实例
    person = PersonData(
        gender="男",
        age=25,
        height=175.0,
        weight=70.0
    )
    
    # 计算BMR
    bmr = calculate_bmr(person)
    print(f"基础代谢率: {bmr} kcal/天")
    
except Exception as e:
    print(f"错误: {str(e)}")
```

### 5.2 错误处理示例

```python
try:
    # 创建无效数据的实例
    invalid_person = PersonData(
        gender="其他",  # 无效的性别
        age=25,
        height=175.0,
        weight=70.0
    )
    
    bmr = calculate_bmr(invalid_person)
    
except BMRInputError as e:
    print(f"输入数据错误: {str(e)}")  # 将输出: "输入数据错误: 性别必须是'男'或'女'"
```

## 6. 注意事项

1. **输入验证**
   - 所有输入必须在指定范围内
   - 年龄必须是整数
   - 身高和体重可以是整数或浮点数

2. **计算精度**
   - 计算过程使用浮点数以保证精度
   - 最终结果会四舍五入到整数
   - 返回值单位为kcal/天

3. **异常处理**
   - 建议始终使用try-except块处理可能的异常
   - 检查异常信息以了解具体的错误原因

## 7. 常见问题

1. Q: 为什么我的BMR计算结果看起来偏高/偏低？
   A: BMR的计算结果会因人而异，影响因素包括年龄、性别、体重、身高等。如果怀疑结果不准确，请检查输入数据是否正确。

2. Q: 计算结果可以用于制定饮食计划吗？
   A: BMR只是每日能量消耗的基础值，实际的每日能量需求还需要考虑活动水平（TDEE）。建议咨询专业营养师获取个性化的建议。

3. Q: 为什么年龄必须是整数？
   A: 这是为了简化计算和提高可用性。在BMR计算中，精确到年是足够的。

## 8. 更新历史

- v1.0.0 (2024-03-21)
  - 初始版本
  - 实现基本的BMR计算功能
  - 添加完整的输入验证
  - 添加详细的文档 