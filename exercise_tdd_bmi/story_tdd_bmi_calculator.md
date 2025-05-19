# User Story: Simple BMI Calculator

> **工作目录说明**：本文档位于 `~/ai_dev_exercise/exercise_tdd_bmi/` 目录下，所有文件引用路径均基于此目录。例如，`./teaching_framework/test_driven_development_with_ai.md` 实际指向 `/Users/bowhead/ai_dev_exercise/exercise_tdd_bmi/teaching_framework/test_driven_development_with_ai.md`。
>
> **实现目录说明**：本练习的实际实现位于 `./tdd_bmi_calculator/` 目录下。

(核心开发理念参考: [测试驱动开发核心理念](./teaching_framework/test_driven_development_with_ai.md))
(练习框架规划参考: [TDD练习框架设计规划](./teaching_framework/planning_tdd_exercise.md))

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

每个练习系列（如ExTDD_01_BMICalculation）都**必须, 一定**包含：

```
tdd_bmi_calculator/ExTDD_XX_FeatureName/
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
tdd_bmi_calculator/ExTDD_01_BMICalculation/
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

#### 核心用户需求 (ExTDD_01_BMICalculation)
> 作为一名普通用户，我希望能方便地输入我的身高（以米为单位）和体重（以千克为单位），然后系统能帮我算出我的身体质量指数（BMI）。如果我输错了数字（比如不是有效的身高体重值），希望能得到一个友好的提示。我最主要就是想知道计算出来的BMI结果。

### 2. ExTDD_02_BMICategorization: 实现BMI值的分类

feature_name: bmi_categorize

```
tdd_bmi_calculator/ExTDD_02_BMICategorization/
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

#### 核心用户需求 (ExTDD_02_BMICategorization)
> 作为一名关心健康的用户，在我知道自己的BMI值之后，我还想知道这个数值到底代表什么意思，比如我是不是偏瘦了、体重是否标准，或者是不是有点超重。希望能给我一个简单明了的健康状况分类。

