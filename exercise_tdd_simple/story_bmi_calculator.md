# User Story: Simple BMI Calculator

(核心开发理念参考: [测试驱动开发核心理念](teaching_framework/test_driven_development_with_ai.md))
(练习框架规划参考: [TDD练习框架设计规划](teaching_framework/planning_tdd_exercise_template.md))

## 1. User Story (用户故事)

# 简单BMI计算器：AI+TDD练习故事实例

> **重要约束**：在整个故事实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。

## 基础结构说明

本故事遵循标准的TDD练习框架结构：

### 命名规范

1. **特性名称 (feature_name)**：
   - 格式：`小写字母_用下划线分隔`
   - 示例：`bmi_calculate`, `bmi_categorize`
   - 要求：描述性、简洁、表明功能

2. **目录命名**：
   - 练习系列目录：`ExTDD_XX_FeatureName`
     - XX：两位数字编号（01、02等）
     - FeatureName：驼峰式命名
     - 示例：`ExTDD_01_BMICalculation`

3. **文件命名**：
   - 思考文件：`_s{step}_{type}_{feature_name}.md`
   - 代码文件：`{feature_name}.py`
   - 测试文件：`test_{feature_name}.py`
   - 文档文件：`doc_{feature_name}.md`

### 目录结构规范

每个练习系列（如ExTDD_01_BMICalculation）都必须包含：

```
ExTDD_XX_FeatureName/
├── constraints/                    # 约束条件
│   └── task_constraints.md        # 任务特定约束
├── inputs/                        # 输入文件
│   └── user_story.md             # 用户故事
├── outputs/                       # 输出文件
│   ├── _s1_think_options_{feature_name}.md
│   ├── _s2_think_design_{feature_name}.md
│   ├── _s3_think_validation_{feature_name}.md
│   ├── {feature_name}.py
│   ├── test_{feature_name}.py
│   └── doc_{feature_name}.md
└── README.md                      # 练习说明
```

## BMI计算器特定实现

### 1. ExTDD_01_BMICalculation: 实现BMI值的计算

feature_name: bmi_calculate

```
ExTDD_01_BMICalculation/
├── constraints/
│   └── task_constraints.md        # BMI计算的特定约束
├── inputs/
│   └── user_story.md             # BMI计算的用户故事
└── outputs/
    ├── _s1_think_options_bmi_calculate.md
    ├── _s2_think_design_bmi_calculate.md
    ├── _s3_think_validation_bmi_calculate.md
    ├── bmi_calculate.py
    ├── test_bmi_calculate.py
    └── doc_bmi_calculate.md
```

#### 特定需求
- 接收用户的身高(米)和体重(千克)输入
- 计算BMI值（体重除以身高的平方）
- 处理无效输入（如零或负数）
- 控制计算精度（保留两位小数）

#### 技术要点
- 输入验证逻辑
- 精确的浮点数计算
- 异常处理策略
- 单位换算考虑

#### 验收标准
- 正确计算正常输入的BMI值
- 适当处理无效输入
- 保持计算精度
- 提供清晰的错误信息

### 2. ExTDD_02_BMICategorization: 实现BMI值的分类

feature_name: bmi_categorize

```
ExTDD_02_BMICategorization/
├── constraints/
│   └── task_constraints.md        # BMI分类的特定约束
├── inputs/
│   └── user_story.md             # BMI分类的用户故事
└── outputs/
    ├── _s1_think_options_bmi_categorize.md
    ├── _s2_think_design_bmi_categorize.md
    ├── _s3_think_validation_bmi_categorize.md
    ├── bmi_categorize.py
    ├── test_bmi_categorize.py
    └── doc_bmi_categorize.md
```

#### 特定需求
- 接收BMI值作为输入
- 根据标准阈值返回分类
- 支持不同的分类标准（可选）
- 提供分类的详细说明

#### 技术要点
- 分类阈值的设定
- 分类逻辑的实现
- 结果的本地化（中英文）
- 分类标准的可扩展性

#### 验收标准
- 准确的分类判断
- 清晰的分类描述
- 合理的边界处理
- 可扩展的设计

