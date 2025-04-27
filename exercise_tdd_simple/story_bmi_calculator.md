# User Story: Simple BMI Calculator

(核心开发理念参考: [AI辅助测试驱动开发](teaching_framework/test_driven_development_with_ai.md))
(练习框架规划参考: [TDD练习框架规划](teaching_framework/planning_tdd_exercise_template.md))

## 1. User Story (用户故事)

# 简单BMI计算器：AI+TDD练习故事实例

> **重要约束**：在整个故事实践过程中，请确保所有在Cursor中的交互对话均使用中文，这是出于演示目的的要求。

本文档描述了"简单BMI计算器"这个故事实例的背景、业务场景和相关资料，用于支持AI+TDD练习框架。本故事聚焦于一个非常基础的健康计算功能：根据身高和体重计算身体质量指数 (BMI) 及其分类。

## 故事背景

假设我们正在为一个简单的健康管理应用开发一个核心工具模块。第一个需要实现的功能是BMI计算器。用户需要能够输入他们的身高（米）和体重（公斤），程序需要计算出BMI值，并能根据标准提供BMI分类（例如，体重过轻、正常、超重等）。

## 业务目标

1.  提供一个准确计算BMI值的函数。
2.  提供一个根据BMI值返回对应分类的函数。
3.  确保函数能够处理有效的数值输入，并对无效输入（如零身高、负数体重）进行适当处理。
4.  代码需要通过测试驱动开发完成，保证质量和可维护性。

## 团队角色

-   **产品经理 (假设)**: 负责定义 BMI 计算器和分类的基本需求。
-   **你 (后端开发者)**: 负责实现这些功能，遵循 TDD 流程。

## 技术栈 (建议)

-   **语言**: Python 3.9+
-   **测试框架**: `unittest` (Python内置)
-   **文档**: Markdown

## 故事目录结构 (已创建)

```
exercise_tdd_simple/
├── teaching_framework/
│   ├── test_driven_development_with_ai.md
│   └── planning_tdd_exercise_template.md
|
├── story_example_bmi_calculator/            (本故事)
│   ├── story_bmi_calculator.md             (本文件 - 故事描述)
│   ├── constraints/
│   │   └── exercise_constraints_bmi_01.md    (BMI练习约束)
│   ├── inputs/
│   │   ├── user_story_bmi_01_calculate.md  (计算BMI值用户故事)
│   │   └── user_story_bmi_02_categorize.md (BMI分类用户故事)
│   └── outputs/
│       ├── ExTDD_01_BMICalculation/        (计算BMI值系列输出)
│       │   ├── s1_implementation_analysis.md
│       │   ├── s2_action_plan.md
│       │   ├── bmi_calculator.py
│       │   ├── test_bmi_calculator.py
│       │   └── s5_api_documentation.md
│       └── ExTDD_02_BMICategorization/     (BMI分类系列输出)
│           └── ... (类似结构)
└── ...
```

## 如何使用本故事进行练习

1.  **准备**: 熟悉本故事背景和业务目标。
2.  **学习核心理念**: 阅读 `teaching_framework/test_driven_development_with_ai.md`，理解AI辅助TDD的原则。
3.  **查阅约束**: 阅读 `constraints/exercise_constraints_bmi_01.md` 文件，了解本故事练习的基本要求和简化假设。
4.  **选择用户故事**: 从 `inputs/` 目录选择一个用户故事开始 (建议从 `user_story_bmi_01_calculate.md` 开始)。
5.  **确定练习系列类型**: 查阅 `teaching_framework/planning_tdd_exercise_template.md` 中定义的练习系列模板 (这两个用户故事都适用于 `ExTDD_01: 实现简单计算/验证功能系列`)。
6.  **创建输出目录**: 在 `outputs/` 下创建对应的子目录 (例如 `outputs/ExTDD_01_BMICalculation/`)。
7.  **执行TDD流程**: 遵循 `planning_tdd_exercise_template.md` 中定义的5个步骤，使用AI助手辅助完成从分析到文档的整个TDD循环。
8.  **反思**: 评估每个步骤的产出质量，思考AI在TDD流程中的作用和挑战。

## 练习系列说明

本故事包含两个核心的微功能开发系列：

1.  **ExTDD_01_BMICalculation**: 实现BMI值的计算。
    *   **输入**: `inputs/user_story_bmi_01_calculate.md`
    *   **目标**: 开发一个函数，接收体重(kg)和身高(m)作为输入，返回计算出的BMI值。需要处理无效输入（如零身高）。
    *   **对应模板**: `ExTDD_01: 实现简单计算/验证功能系列`

2.  **ExTDD_02_BMICategorization**: 实现BMI值的分类。
    *   **输入**: `inputs/user_story_bmi_02_categorize.md`
    *   **目标**: 开发一个函数，接收BMI值作为输入，根据标准阈值返回对应的分类字符串（例如，"Underweight", "Normal", "Overweight", "Obese"）。
    *   **对应模板**: `ExTDD_01: 实现简单计算/验证功能系列`

---
祝您学习愉快！ 