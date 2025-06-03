# 用户故事 - Calculate TDEE (每日总能量消耗)

## 特性标识
- **特性编号**: ExTDD_02_CalculateTDEE
- **模块名称**: dcnc (Daily Caloric Needs Calculator)
- **特性名称**: calculate_tdee
- **依赖特性**: ExTDD_01_CalculateBMR

## 用户故事描述

### 主要用户故事
> **作为** 一名关心健康的用户  
> **我希望** 在知道了自己的基础代谢率（BMR）之后，通过选择自己的日常活动量水平来估算每天实际消耗的总热量（TDEE）  
> **以便于** 更准确地制定饮食计划和健康管理策略

### 详细功能描述

用户需要能够：
1. **输入BMR值**：可以是之前计算得出的BMR，或者直接提供BMR数值
2. **选择活动量水平**：从预定义的活动量级别中选择最符合自己日常生活的一项
3. **获得TDEE计算结果**：基于BMR和活动系数计算出每日总能量消耗
4. **处理异常情况**：当输入无效时获得清晰的错误提示

### 活动量水平定义

根据国际通用标准，活动量水平分为以下5个级别：

| 活动水平 | 英文标识 | 活动系数 | 描述 |
|---------|---------|---------|------|
| 久坐 | sedentary | 1.2 | 很少或没有运动，主要是办公室工作 |
| 轻度活动 | lightly_active | 1.375 | 轻度运动/运动1-3天/周 |
| 中度活动 | moderately_active | 1.55 | 中度运动/运动3-5天/周 |
| 重度活动 | very_active | 1.725 | 重度运动/运动6-7天/周 |
| 极重度活动 | extra_active | 1.9 | 非常重度的运动/体力工作或每天2次训练 |

## 验收标准

### 场景1：正常TDEE计算

**Given** 用户提供有效的BMR值和活动水平  
**When** 调用calculate_tdee函数  
**Then** 应该返回正确的TDEE值（保留1位小数）

**测试用例**：
- BMR=1500, 活动水平="sedentary" → TDEE=1800.0
- BMR=1800, 活动水平="moderately_active" → TDEE=2790.0
- BMR=2000, 活动水平="very_active" → TDEE=3450.0

### 场景2：活动水平大小写不敏感

**Given** 用户提供的活动水平使用不同大小写  
**When** 调用calculate_tdee函数  
**Then** 应该正确识别并计算TDEE

**测试用例**：
- "SEDENTARY", "Lightly_Active", "moderately_ACTIVE" 等都应该被正确识别

### 场景3：边界值处理

**Given** 用户提供边界值的BMR  
**When** 调用calculate_tdee函数  
**Then** 应该正确计算TDEE

**测试用例**：
- 最小合理BMR值（如800）
- 最大合理BMR值（如4000）

### 场景4：输入类型错误处理

**Given** 用户提供错误类型的参数  
**When** 调用calculate_tdee函数  
**Then** 应该抛出TypeError并提供清晰的错误信息

**测试用例**：
- bmr参数不是数值类型
- activity_level参数不是字符串类型

### 场景5：输入值错误处理

**Given** 用户提供无效的参数值  
**When** 调用calculate_tdee函数  
**Then** 应该抛出ValueError并提供清晰的错误信息

**测试用例**：
- BMR值为负数或零
- BMR值超出合理范围（如<500或>5000）
- 活动水平不在预定义列表中

## 技术约束

### 函数签名
```python
def calculate_tdee(bmr: float, activity_level: str) -> float:
    """计算每日总能量消耗（TDEE）。
    
    Args:
        bmr (float): 基础代谢率，范围500-5000
        activity_level (str): 活动水平，可选值：
            - "sedentary": 久坐 (1.2)
            - "lightly_active": 轻度活动 (1.375)
            - "moderately_active": 中度活动 (1.55)
            - "very_active": 重度活动 (1.725)
            - "extra_active": 极重度活动 (1.9)
    
    Returns:
        float: 每日总能量消耗（卡路里/天），保留1位小数
    
    Raises:
        TypeError: 当参数类型不正确时
        ValueError: 当参数值无效时
    """
```

### 计算公式
```
TDEE = BMR × 活动系数
```

### 输入验证规则
1. **BMR验证**：
   - 类型：必须是int或float
   - 范围：500 ≤ BMR ≤ 5000
   - 说明：覆盖从儿童到极端体型成年人的合理BMR范围

2. **活动水平验证**：
   - 类型：必须是str
   - 值：必须在预定义的5个活动水平中
   - 大小写：不敏感，内部转换为小写处理

### 输出规范
1. **返回类型**：float
2. **精度**：保留1位小数
3. **范围**：600-9500（基于BMR和活动系数的合理范围）

## 相关文档

- [ExTDD_01_CalculateBMR用户故事](../ExTDD_01_CalculateBMR/_user_story_calculate_bmr.md)
- [TDD开发规范](../../../../tdd_rules/tdd_ai_thinking.md)
- [单元测试设计技巧](../../../../tdd_rules/tdd_unit_test_design_techniques.md)

## 开发注意事项

1. **依赖关系**：此特性依赖于BMR计算功能，但不直接调用calculate_bmr函数
2. **扩展性**：设计时考虑未来可能添加新的活动水平或自定义活动系数
3. **国际化**：活动水平标识使用英文，便于国际化扩展
4. **精度处理**：使用round()函数确保结果精度一致性

---

**创建时间**: 当前  
**最后更新**: 当前  
**状态**: 待开发