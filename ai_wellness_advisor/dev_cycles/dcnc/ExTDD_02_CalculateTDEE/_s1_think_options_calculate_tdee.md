# S1: Think Options - Calculate TDEE 实现选项分析

## 特性信息
- **特性名称**: ExTDD_02_CalculateTDEE
- **模块**: dcnc (Daily Caloric Needs Calculator)
- **函数**: `calculate_tdee(bmr, activity_level)`
- **依赖**: ExTDD_01_CalculateBMR（概念依赖，非代码依赖）

## 需求回顾

### 核心功能
- 基于BMR值和活动水平计算每日总能量消耗（TDEE）
- 支持5种标准活动水平，每种对应不同的活动系数
- 提供完整的输入验证和错误处理
- 返回保留1位小数的float结果

### 关键约束
- BMR范围：500-5000
- 活动水平大小写不敏感
- 计算公式：TDEE = BMR × 活动系数

## 实现方案分析

### 方案1：简单函数实现

#### 设计概述
```python
def calculate_tdee(bmr: float, activity_level: str) -> float:
    # 参数验证
    # 活动系数映射
    # 计算并返回结果
```

#### 优点
✅ 实现简单直接  
✅ 符合单一职责原则  
✅ 易于测试和维护  
✅ 性能优秀  
✅ 与BMR函数保持一致的设计风格  

#### 缺点
❌ 活动系数硬编码在函数内  
❌ 扩展新活动水平需要修改函数  

### 方案2：配置驱动实现

#### 设计概述
```python
ACTIVITY_COEFFICIENTS = {
    'sedentary': 1.2,
    'lightly_active': 1.375,
    # ...
}

def calculate_tdee(bmr: float, activity_level: str, 
                  coefficients: dict = None) -> float:
    # 使用外部配置或默认配置
```

#### 优点
✅ 配置与逻辑分离  
✅ 易于扩展新活动水平  
✅ 支持自定义活动系数  
✅ 便于单元测试  

#### 缺点
❌ 增加了复杂性  
❌ 可能被误用（传入错误配置）  
❌ 对于当前需求过度设计  

### 方案3：类封装实现

#### 设计概述
```python
class TDEECalculator:
    def __init__(self):
        self.activity_coefficients = {...}
    
    def calculate(self, bmr: float, activity_level: str) -> float:
        # 计算逻辑
```

#### 优点
✅ 面向对象设计  
✅ 状态封装  
✅ 易于扩展功能  

#### 缺点
❌ 对于简单计算过度复杂  
❌ 增加内存开销  
❌ 与项目现有风格不一致  

## 技术考虑因素

### 1. 输入验证策略

#### BMR验证
- **类型检查**: isinstance(bmr, (int, float))
- **范围检查**: 500 ≤ bmr ≤ 5000
- **特殊值处理**: 排除NaN、无穷大等

#### 活动水平验证
- **类型检查**: isinstance(activity_level, str)
- **大小写处理**: activity_level.lower().strip()
- **有效性检查**: 在预定义列表中

### 2. 错误处理设计

#### TypeError场景
- bmr不是数值类型
- activity_level不是字符串类型

#### ValueError场景
- bmr超出合理范围
- activity_level不在预定义列表中

### 3. 性能考虑

#### 查找优化
- 使用字典而非if-elif链进行活动系数查找
- O(1)时间复杂度

#### 内存效率
- 常量定义在模块级别，避免重复创建
- 简单数据结构，最小内存占用

### 4. 扩展性设计

#### 未来可能的扩展
- 添加新的活动水平
- 支持自定义活动系数
- 集成其他TDEE计算公式
- 支持不同的精度要求

#### 设计原则
- 保持向后兼容
- 最小化接口变更
- 清晰的文档和错误信息

## 推荐方案

### 选择：方案1 - 简单函数实现

#### 决策理由

1. **需求匹配度高**
   - 当前需求明确且稳定
   - 5种活动水平是国际标准，变化可能性小
   - 简单直接的实现满足所有功能要求

2. **与现有代码一致**
   - 与calculate_bmr函数保持相同的设计风格
   - 维护代码库的一致性
   - 降低学习和维护成本

3. **性能和可靠性**
   - 最小的复杂度，最高的可靠性
   - 优秀的性能表现
   - 易于调试和测试

4. **YAGNI原则**
   - "You Aren't Gonna Need It"
   - 避免过度设计
   - 专注于当前需求

### 实现策略

#### 核心结构
```python
# 模块级常量
ACTIVITY_COEFFICIENTS = {
    'sedentary': 1.2,
    'lightly_active': 1.375,
    'moderately_active': 1.55,
    'very_active': 1.725,
    'extra_active': 1.9
}

def calculate_tdee(bmr: float, activity_level: str) -> float:
    """计算每日总能量消耗（TDEE）。"""
    # 1. 参数类型验证
    # 2. 参数值验证
    # 3. 活动系数查找
    # 4. TDEE计算
    # 5. 结果格式化
```

#### 验证流程
1. **类型验证** → TypeError
2. **BMR范围验证** → ValueError
3. **活动水平标准化** → 转小写、去空格
4. **活动水平有效性验证** → ValueError
5. **计算和格式化** → round(result, 1)

## 下一步行动

### S2阶段：详细设计
1. 确定具体的函数签名和文档字符串
2. 设计详细的参数验证逻辑
3. 定义所有错误消息的具体内容
4. 规划测试用例的具体数据
5. 确定文件结构和导入策略

### 关键决策点
- ✅ 实现方案：简单函数
- ✅ 常量定义：模块级字典
- ✅ 验证策略：类型+值+范围
- ✅ 错误处理：TypeError + ValueError
- ✅ 精度处理：round(result, 1)

---

**分析完成时间**: 当前  
**推荐方案**: 方案1 - 简单函数实现  
**置信度**: 高  
**下一阶段**: S2 - Think Design