# Practice: 每日所需热量计算器 (Daily Caloric Needs Calculator)

> **工作目录说明**：本文档位于 /Users/bowhead/ai_dev_exercise_tdd/exercise_tdd_dcnc/ 目录下，所有文件引用路径均基于此目录。例如，`./teaching_framework/test_driven_development_with_ai.md` 实际指向 `/Users/bowhead/ai_dev_exercise_tdd/exercise_tdd_dcnc/teaching_framework/test_driven_development_with_ai.md`。
>
> **归档目录说明**：本练习各TDD周期的详细思考、设计、代码快照及总结，均归档于 `../ai_wellness_advisor/docs/archived_tdd_cycles/dcnc/` 目录下。实际的功能代码和测试代码在稳定后，将整合到 `../ai_wellness_advisor/src/dcnc/` 和 `../ai_wellness_advisor/tests/dcnc/`。用户故事的权威版本位于 `../ai_wellness_advisor/docs/user_stories/`。

(核心开发理念参考: [测试驱动开发核心理念](./teaching_framework/test_driven_development_with_ai.md))
(单元测试设计参考: [TDD单元测试设计技巧](./teaching_framework/tdd_unit_test_design_techniques.md))
(练习框架规划参考: [TDD练习框架设计规划](./teaching_framework/planning_tdd_exercise.md))

## 1. User Story (用户故事)

# 每日所需热量计算器 (Daily Caloric Needs Calculator): AI+TDD练习实践实例

> **重要约束**：在整个实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。

## 基础结构说明

本实践遵循标准的TDD练习框架结构：

### 命名规范

1.  **特性名称 (feature_name)**：
    *   格式：`小写字母_用下划线分隔`
    *   示例：`calculate_bmr`, `calculate_tdee`
    *   要求：描述性、简洁、表明功能

2.  **目录命名**：
    *   练习系列目录：`ExTDD_XX_FeatureName`
        *   XX：两位数字编号（01、02等）
        *   FeatureName：驼峰式命名
        *   示例：`ExTDD_01_CalculateBMR`

3.  **文件命名**：
    *   思考文件：`_s{step}_{type}_{feature_name}.md`
    *   代码文件：`{feature_name}.py`
    *   测试文件：`test_{feature_name}.py`
    *   文档文件：`doc_{feature_name}.md`

### 目录结构规范 (TDD周期归档)

每个练习系列的TDD周期产出物将归档在 `../ai_wellness_advisor/docs/archived_tdd_cycles/dcnc/ExTDD_XX_FeatureName/` 目录下，其结构**必须, 一定**包含：

```
../ai_wellness_advisor/docs/archived_tdd_cycles/dcnc/ExTDD_XX_FeatureName/
├── constraints/                    # (Constraints) 约束条件
│   └── {feature_name}_constraints.md # (Task Constraints) 记录当前TDD周期的特定约束和假设。
├── outputs/                       # (Outputs) TDD周期内的主要产出物
│   ├── _s1_think_options_{feature_name}.md  # 思考过程：方案选择与分析。
│   ├── _s2_think_design_{feature_name}.md   # 思考过程：详细设计。
│   ├── _s3_think_validation_{feature_name}.md # 思考过程：验证和测试点设计。
│   ├── {feature_name}.py              # TDD练习的功能代码 (归档快照, 非项目最终代码)。
│   ├── test_{feature_name}.py         # TDD练习的单元测试 (归档快照, 非项目最终代码)。
│   └── doc_{feature_name}.md         # (Optional) 特性相关的简要说明或API文档（如果适用）。
└── README.md                      # (README) 对当前TDD周期的总结、遇到的问题、学习和反思。
```

## 每日所需热量计算器 (Daily Caloric Needs Calculator) 特定实现

### 01. ExTDD_01_CalculateBMR: 计算基础代谢率 (BMR)

feature_name: calculate_bmr

归档目录: `../ai_wellness_advisor/docs/archived_tdd_cycles/dcnc/ExTDD_01_CalculateBMR/`
```
../ai_wellness_advisor/docs/archived_tdd_cycles/dcnc/ExTDD_01_CalculateBMR/
├── constraints/
│   └── calculate_bmr_constraints.md # 计算基础代谢率 (BMR)的特定约束
├── outputs/
│   ├── _s1_think_options_calculate_bmr.md  # 思考过程：方案选择与分析。
│   ├── _s2_think_design_calculate_bmr.md   # 思考过程：详细设计。
│   ├── _s3_think_validation_calculate_bmr.md # 思考过程：验证和测试点设计。
│   ├── calculate_bmr.py              # TDD练习的功能代码 (归档快照, 非项目最终代码)。
│   ├── test_calculate_bmr.py         # TDD练习的单元测试 (归档快照, 非项目最终代码)。
│   └── doc_calculate_bmr.md         # (Optional) 特性相关的简要说明或API文档（如果适用）。
└── README.md                      # 对 ExTDD_01_CalculateBMR 周期的总结
```

#### 核心用户需求 (ExTDD_01_CalculateBMR)
> 用户希望输入自己的性别、年龄、身高和体重，就能知道自己每天最少需要消耗多少能量来维持生命。

### 02. ExTDD_02_CalculateTDEE: 计算每日总能量消耗 (TDEE)

feature_name: calculate_tdee

归档目录: `../ai_wellness_advisor/docs/archived_tdd_cycles/dcnc/ExTDD_02_CalculateTDEE/`
```
../ai_wellness_advisor/docs/archived_tdd_cycles/dcnc/ExTDD_02_CalculateTDEE/
├── constraints/
│   └── calculate_tdee_constraints.md # 计算每日总能量消耗 (TDEE)的特定约束
├── outputs/
│   ├── _s1_think_options_calculate_tdee.md  # 思考过程：方案选择与分析。
│   ├── _s2_think_design_calculate_tdee.md   # 思考过程：详细设计。
│   ├── _s3_think_validation_calculate_tdee.md # 思考过程：验证和测试点设计。
│   ├── calculate_tdee.py              # TDD练习的功能代码 (归档快照, 非项目最终代码)。
│   ├── test_calculate_tdee.py         # TDD练习的单元测试 (归档快照, 非项目最终代码)。
│   └── doc_calculate_tdee.md         # (Optional) 特性相关的简要说明或API文档（如果适用）。
└── README.md                      # 对 ExTDD_02_CalculateTDEE 周期的总结
```

#### 核心用户需求 (ExTDD_02_CalculateTDEE)
> 在知道了自己的基础代谢率之后，用户希望通过选择自己的日常活动量，来估算每天实际消耗的总热量。

## 通用约束条件
*   所有代码实现应遵循 PEP 8 Python 编码规范。
*   函数和方法应具有清晰、描述性的名称，并遵循单一职责原则。
*   测试用例的名称应明确描述其所验证的行为或场景。
*   如前所述，实现应仅依赖Python标准库，不引入外部包。
*   错误处理应明确，对无效输入或计算中可能发生的异常情况提供适当反馈（尽管具体的错误提示也是一个特性）。

## 学习顺序
学习顺序将强调从简单到复杂，确保学习者首先完成 `CalculateBMR` (计算基础代谢率) 的练习，然后再进行到 `CalculateTDEE` (计算每日总能量消耗) 的练习。

## 技术依赖
Python 3.12

## 练习难度递进
练习从核心的BMR计算开始，这是一个相对直接的公式实现，帮助学习者熟悉TDD的基本流程和单个功能的构建。随后，练习过渡到TDEE的计算，它建立在BMR的基础上，并引入了基于用户选择（活动水平）的条件逻辑和乘数，增加了少许复杂性，要求学习者处理不同分支情况和状态的组合。这种安排旨在平稳地引导学习者从简单计算到稍复杂的逻辑处理。