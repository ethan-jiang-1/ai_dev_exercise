# BMI 计算器实现方案分析（v2 - 支持多单位）

## 背景
原有的 BMI 计算器仅支持公制单位（米和千克），现需要扩展支持英制单位（英尺/英寸和磅）。

## 需求变更要点
1. 支持新的输入单位：
   - 身高：米 或 英尺/英寸
   - 体重：千克 或 磅
2. 保持原有功能不变
3. 确保不同单位系统下计算结果一致（误差 ±0.01）

## 可选方案分析

### 方案 A：扩展现有函数
```python
def bmi_calculate(
    height: float,
    weight: float,
    height_unit: str = "m",      # "m" 或 "ft_in"
    weight_unit: str = "kg"      # "kg" 或 "lb"
) -> float:
    # 单位转换后复用现有逻辑
    pass
```

优点：
- 向后兼容，默认参数保持原有行为
- 使用简单，接口统一
- 实现直观

缺点：
- 英尺/英寸输入需要特殊处理
- 函数职责增加，违反单一职责原则
- 参数组合可能产生混淆

### 方案 B：单位转换 + 现有函数
```python
def convert_height_to_meters(height: float | tuple[float, float], unit: str) -> float:
    # 转换身高为米
    pass

def convert_weight_to_kg(weight: float, unit: str) -> float:
    # 转换体重为千克
    pass

def bmi_calculate(height_m: float, weight_kg: float) -> float:
    # 保持原有实现不变
    pass
```

优点：
- 职责分离清晰
- 单位转换可独立测试
- 原有功能完全不变
- 转换函数可被其他模块复用

缺点：
- 使用时需要多个函数调用
- 接口略显复杂

### 方案 C：面向对象封装
```python
class BMICalculator:
    def __init__(self, height_unit: str = "m", weight_unit: str = "kg"):
        self.height_unit = height_unit
        self.weight_unit = weight_unit
    
    def calculate(self, height: float | tuple[float, float], weight: float) -> float:
        # 内部处理单位转换和计算
        pass
```

优点：
- 状态管理清晰
- 可扩展性好
- 使用灵活

缺点：
- 过度设计，当前需求可能不需要这么复杂
- 增加了使用的复杂度
- 需要维护类的状态

### 方案 D：Pydantic 模型
```python
from pydantic import BaseModel, validator

class BMIInput(BaseModel):
    height: float | tuple[float, float]
    weight: float
    height_unit: str = "m"
    weight_unit: str = "kg"
    
    @validator("height_unit")
    def validate_height_unit(cls, v):
        if v not in ["m", "ft_in"]:
            raise ValueError("Invalid height unit")
        return v
```

优点：
- 输入验证强大
- 类型提示完善
- 序列化/反序列化方便

缺点：
- 引入额外依赖
- 可能过于复杂
- 学习成本较高

## 方案选择

推荐采用**方案 B：单位转换 + 现有函数**，原因如下：

1. **保持原有代码稳定**：
   - 现有的 `bmi_calculate` 函数保持不变
   - 已有的测试用例仍然有效
   - 不影响现有用户

2. **职责分离清晰**：
   - 单位转换独立封装
   - 每个函数职责单一
   - 便于测试和维护

3. **实现简单直观**：
   - 无需管理状态
   - 无需引入新的依赖
   - 代码结构清晰

4. **灵活性好**：
   - 转换函数可独立使用
   - 便于未来扩展其他单位
   - 便于其他模块复用

## 实现步骤规划

1. 创建单位转换函数：
   - `convert_height_to_meters`
   - `convert_weight_to_kg`

2. 为新函数编写测试：
   - 单位转换精度测试
   - 边界值测试
   - 错误处理测试

3. 保持原有 `bmi_calculate` 不变

4. 更新文档，添加新函数说明

## 风险评估

1. **精度风险**：
   - 单位转换中的精度损失
   - 缓解：使用高精度浮点数计算

2. **使用复杂度**：
   - 需要多个函数调用
   - 缓解：提供清晰的文档和示例

3. **错误处理**：
   - 新增的单位转换错误
   - 缓解：完善的输入验证和错误提示 