# 详细设计方案：基础代谢率（BMR）计算器

## 1. 模块结构设计

### 1.1 文件组织
```
calculate_bmr.py          # 主实现文件
├── BMRCalculator         # 主类
├── BMRValidationError   # 自定义异常基类
└── 具体异常类           # 特定验证错误的异常类
```

### 1.2 常量定义
```python
# 性别常量
GENDER_MALE = "男"
GENDER_FEMALE = "女"
VALID_GENDERS = {GENDER_MALE, GENDER_FEMALE}

# 年龄范围
AGE_MIN = 15
AGE_MAX = 80

# 身高范围（厘米）
HEIGHT_MIN = 130
HEIGHT_MAX = 230

# 体重范围（公斤）
WEIGHT_MIN = 30
WEIGHT_MAX = 150

# BMR计算系数（Harris-Benedict公式）
MALE_BMR_CONSTANT = 66.5
MALE_WEIGHT_MULTIPLIER = 13.75
MALE_HEIGHT_MULTIPLIER = 5.003
MALE_AGE_MULTIPLIER = 6.755

FEMALE_BMR_CONSTANT = 655.1
FEMALE_WEIGHT_MULTIPLIER = 9.563
FEMALE_HEIGHT_MULTIPLIER = 1.850
FEMALE_AGE_MULTIPLIER = 4.676
```

## 2. 异常类设计

```python
class BMRValidationError(ValueError):
    """基础代谢率计算器的基础异常类"""
    pass

class InvalidGenderError(BMRValidationError):
    """性别输入无效时抛出"""
    pass

class InvalidAgeError(BMRValidationError):
    """年龄输入无效时抛出"""
    pass

class InvalidHeightError(BMRValidationError):
    """身高输入无效时抛出"""
    pass

class InvalidWeightError(BMRValidationError):
    """体重输入无效时抛出"""
    pass
```

## 3. 主类设计

```python
class BMRCalculator:
    """基础代谢率(BMR)计算器"""
    
    def validate_gender(self, gender: str) -> None:
        """验证性别输入是否有效
        
        Args:
            gender: 性别，必须是 "男" 或 "女"
            
        Raises:
            InvalidGenderError: 当性别不是 "男" 或 "女" 时抛出
        """
        if gender not in VALID_GENDERS:
            raise InvalidGenderError(f"性别必须是 {GENDER_MALE} 或 {GENDER_FEMALE}")
    
    def validate_age(self, age: int) -> None:
        """验证年龄输入是否有效
        
        Args:
            age: 年龄，必须是 15-80 岁之间的整数
            
        Raises:
            InvalidAgeError: 当年龄不在有效范围内时抛出
        """
        if not isinstance(age, int):
            raise InvalidAgeError("年龄必须是整数")
        if not (AGE_MIN <= age <= AGE_MAX):
            raise InvalidAgeError(f"年龄必须在 {AGE_MIN}-{AGE_MAX} 岁之间")
    
    def validate_height(self, height: float) -> None:
        """验证身高输入是否有效
        
        Args:
            height: 身高（厘米），必须在 130-230 厘米之间
            
        Raises:
            InvalidHeightError: 当身高不在有效范围内时抛出
        """
        if not isinstance(height, (int, float)):
            raise InvalidHeightError("身高必须是数字")
        if not (HEIGHT_MIN <= height <= HEIGHT_MAX):
            raise InvalidHeightError(f"身高必须在 {HEIGHT_MIN}-{HEIGHT_MAX} 厘米之间")
    
    def validate_weight(self, weight: float) -> None:
        """验证体重输入是否有效
        
        Args:
            weight: 体重（公斤），必须在 30-150 公斤之间
            
        Raises:
            InvalidWeightError: 当体重不在有效范围内时抛出
        """
        if not isinstance(weight, (int, float)):
            raise InvalidWeightError("体重必须是数字")
        if not (WEIGHT_MIN <= weight <= WEIGHT_MAX):
            raise InvalidWeightError(f"体重必须在 {WEIGHT_MIN}-{WEIGHT_MAX} 公斤之间")
    
    def validate_inputs(self, gender: str, age: int, height: float, weight: float) -> None:
        """验证所有输入参数是否有效
        
        Args:
            gender: 性别
            age: 年龄（岁）
            height: 身高（厘米）
            weight: 体重（公斤）
            
        Raises:
            BMRValidationError: 当任何输入无效时抛出对应的异常
        """
        self.validate_gender(gender)
        self.validate_age(age)
        self.validate_height(height)
        self.validate_weight(weight)
    
    def calculate(self, gender: str, age: int, height: float, weight: float) -> float:
        """计算基础代谢率(BMR)
        
        Args:
            gender: 性别（"男" 或 "女"）
            age: 年龄（岁）
            height: 身高（厘米）
            weight: 体重（公斤）
            
        Returns:
            float: 基础代谢率（kcal/天），保留一位小数
            
        Raises:
            BMRValidationError: 当输入参数无效时抛出
        """
        # 首先验证所有输入
        self.validate_inputs(gender, age, height, weight)
        
        # 根据性别选择计算公式
        if gender == GENDER_MALE:
            bmr = (MALE_BMR_CONSTANT +
                  (MALE_WEIGHT_MULTIPLIER * weight) +
                  (MALE_HEIGHT_MULTIPLIER * height) -
                  (MALE_AGE_MULTIPLIER * age))
        else:  # gender == GENDER_FEMALE
            bmr = (FEMALE_BMR_CONSTANT +
                  (FEMALE_WEIGHT_MULTIPLIER * weight) +
                  (FEMALE_HEIGHT_MULTIPLIER * height) -
                  (FEMALE_AGE_MULTIPLIER * age))
        
        # 返回结果，保留一位小数
        return round(bmr, 1)
```

## 4. 使用示例

```python
def main():
    calculator = BMRCalculator()
    try:
        bmr = calculator.calculate("男", 25, 175.0, 70.0)
        print(f"您的基础代谢率是：{bmr} 千卡/天")
    except BMRValidationError as e:
        print(f"输入错误：{str(e)}")

if __name__ == "__main__":
    main()
```

## 5. 测试策略

### 5.1 验证测试
- 测试所有输入验证函数
- 测试边界值
- 测试无效输入
- 测试异常信息的准确性

### 5.2 计算测试
- 测试男性 BMR 计算
- 测试女性 BMR 计算
- 测试结果精度（一位小数）
- 测试已知输入的预期输出

### 5.3 集成测试
- 测试完整的计算流程
- 测试异常处理流程
- 测试性能要求（10ms）

## 6. 性能优化策略

1. 验证顺序优化：
   - 先进行类型检查（开销最小）
   - 再进行范围检查
   - 最后进行其他验证

2. 计算优化：
   - 使用局部变量存储常量引用
   - 避免重复计算
   - 使用内置的 round 函数进行精度控制

## 7. 下一步行动

1. 实现单元测试（test_calculate_bmr.py）
2. 完成主要实现（calculate_bmr.py）
3. 进行性能测试和优化
4. 编写详细的 API 文档 