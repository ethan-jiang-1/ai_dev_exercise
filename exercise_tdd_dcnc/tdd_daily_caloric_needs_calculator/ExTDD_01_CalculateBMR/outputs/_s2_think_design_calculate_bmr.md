# 基础代谢率(BMR)计算器 - 详细设计

## 1. 数据类设计

### 1.1 PersonData类
```python
from dataclasses import dataclass
from typing import Literal

@dataclass
class PersonData:
    """人体数据类，用于BMR计算的输入数据验证和存储"""
    
    gender: Literal["男", "女"]  # 使用Literal类型确保性别只能是"男"或"女"
    age: int                    # 年龄(岁)
    height: float              # 身高(cm)
    weight: float              # 体重(kg)
```

### 1.2 自定义异常类
```python
class BMRInputError(ValueError):
    """BMR计算器输入验证异常"""
    pass
```

### 1.3 数据验证方法
```python
def validate_person_data(data: PersonData) -> None:
    """验证PersonData实例中的数据是否有效"""
    
    # 验证性别
    if data.gender not in ["男", "女"]:
        raise BMRInputError("性别必须是'男'或'女'")
    
    # 验证年龄
    if not isinstance(data.age, int):
        raise BMRInputError("年龄必须是整数")
    if not 0 <= data.age <= 120:
        raise BMRInputError("年龄必须在0-120岁之间")
    
    # 验证身高
    if not isinstance(data.height, (int, float)):
        raise BMRInputError("身高必须是数字")
    if not 30 <= data.height <= 250:
        raise BMRInputError("身高必须在30-250厘米之间")
    
    # 验证体重
    if not isinstance(data.weight, (int, float)):
        raise BMRInputError("体重必须是数字")
    if not 2 <= data.weight <= 300:
        raise BMRInputError("体重必须在2-300公斤之间")
```

## 2. 核心功能设计

### 2.1 BMR计算函数
```python
def calculate_bmr(person: PersonData) -> int:
    """
    计算基础代谢率(BMR)
    
    Args:
        person (PersonData): 包含个人数据的PersonData实例
        
    Returns:
        int: 基础代谢率(kcal/天)，四舍五入到整数
        
    Raises:
        BMRInputError: 当输入数据验证失败时抛出
        ValueError: 当计算过程中出现错误时抛出
    """
    # 1. 验证输入数据
    validate_person_data(person)
    
    # 2. 根据Harris-Benedict公式计算BMR
    try:
        if person.gender == "男":
            bmr = 66.5 + (13.75 * person.weight) + (5.003 * person.height) - (6.755 * person.age)
        else:  # 女性
            bmr = 655.1 + (9.563 * person.weight) + (1.850 * person.height) - (4.676 * person.age)
        
        # 3. 四舍五入到整数
        return round(bmr)
        
    except (ValueError, ArithmeticError) as e:
        raise ValueError(f"BMR计算过程出错: {str(e)}")
```

## 3. 使用示例

```python
# 创建PersonData实例
person = PersonData(
    gender="男",
    age=25,
    height=175.0,
    weight=70.0
)

# 计算BMR
try:
    bmr = calculate_bmr(person)
    print(f"基础代谢率: {bmr} kcal/天")
except BMRInputError as e:
    print(f"输入数据错误: {str(e)}")
except ValueError as e:
    print(f"计算错误: {str(e)}")
```

## 4. 实现步骤

1. **创建基础文件结构**
   - 创建`calculate_bmr.py`文件
   - 创建`test_calculate_bmr.py`文件

2. **实现数据类和验证**
   - 实现`PersonData`数据类
   - 实现`BMRInputError`异常类
   - 实现`validate_person_data`函数

3. **实现BMR计算功能**
   - 实现`calculate_bmr`函数
   - 添加必要的类型提示
   - 添加完整的文档字符串

4. **编写单元测试**
   - 测试数据验证功能
   - 测试BMR计算功能
   - 测试边界条件
   - 测试异常处理

5. **优化和文档完善**
   - 确保代码符合PEP 8规范
   - 完善函数文档
   - 添加使用示例

## 5. 注意事项

1. **数据验证**
   - 所有输入必须严格验证
   - 验证失败必须提供清晰的错误信息
   - 验证规则必须符合约束文档要求

2. **计算精度**
   - 中间计算使用浮点数
   - 最终结果四舍五入为整数
   - 确保计算过程不会溢出

3. **异常处理**
   - 区分输入验证异常和计算异常
   - 提供有意义的错误信息
   - 确保所有异常都被适当处理

4. **代码质量**
   - 确保代码可读性
   - 添加适当的注释
   - 遵循Python类型提示最佳实践 