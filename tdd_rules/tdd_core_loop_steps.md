# TDD 核心循环：5个关键步骤 (TDD Core Loop: 5 Key Steps)

本文档概述了测试驱动开发 (Test-Driven Development, TDD) 循环的5个核心步骤。这些步骤旨在按顺序执行，以确保结构化且有效的开发过程，尤其是在使用 AI 辅助编码时。

每个 TDD 练习系列模板都应包含这5个核心步骤，以形成一个完整的 TDD 循环。在这些步骤中生成的输出文件应遵循项目中 `README_folders.md` 和 `README_folder_feature.md` 文件定义的目录结构。

## 通用输出规范 (重点) (Universal Output Specifications (Key))

*   **思考/文档 Markdown 文件** (例如：`_s1_think_options_{feature_name}.md`, `_doc_{feature_name}.md`): 存储在 `{app_name}/dev_cycles/{module_name}/ExTDD_XX_FeatureName/`。
*   **功能实现代码** (`{feature_name}.py`): 存储在 `{app_name}/src/{module_name}/`。
*   **测试代码** (`test_{feature_name}.py`): 存储在 `{app_name}/tests/{module_name}/`。
*   **强调 (Emphasis)**: 必须遵守 `README_folders.md` 和 `README_folder_feature.md` 中定义的路径。

## TDD 5个核心步骤 (The 5 Core TDD Steps)

1.  **步骤1: 思考 - 探索实现选项 (Step 1: Think - Explore Implementation Options) (`_s1_think_options_{feature_name}.md`)**
    *   **目标 (Objective)**: 分析用户故事 (user story)，识别核心需求 (core requirements)、技术挑战 (technical challenges) 和初步的实现思路。
    *   **AI 执行约束 (AI Execution Constraint)**: AI 助手必须先创建并完成此文档，然后再继续下一步。

2.  **步骤2: 设计 - 制定实现计划 (Step 2: Design - Formulate Implementation Plan) (`_s2_think_design_{feature_name}.md`)**
    *   **目标 (Objective)**: 将想法固化为具体的设计，定义函数接口 (function interfaces)，并规划实现步骤。
    *   **AI 执行约束 (AI Execution Constraint)**: AI 助手必须先创建并完成此文档，然后再继续下一步。

3.  **步骤3: 验证与测试 - 编写失败的测试 (红色阶段) (Step 3: Validate & Test - Write Failing Tests (Red)) (`_s3_think_validation_{feature_name}.md`, `test_{feature_name}.py`)**
    *   **目标 (Objective)**: 编写一个或多个最初会失败的测试用例 (test cases)。
    *   **关键点 (Key Point)**: 如果功能单元依赖其他模块，通常使用测试替身 (test doubles) (例如 Mock 对象) 来隔离依赖。详细技术请参阅 `tdd_unit_test_design_techniques.md`。
    *   **测试框架建议 (Testing Framework Recommendation)**: 虽然 Python 内置的 `unittest` 模块是默认选项，但强烈推荐使用 `pytest` 来设计和编写测试。`pytest` 简洁的语法、强大的固件 (fixture) 支持以及丰富的插件生态系统显著提高了测试效率和可维护性。在实际项目中，`pytest` 通常是更现代、更高效的选择。
    *   **AI 执行约束 (AI Execution Constraint)**: AI 助手必须先创建并完成 `_s3_think_validation_{feature_name}.md` 文档和相应的 `test_{feature_name}.py` (确保测试失败)，然后再继续。

4.  **步骤4: 实现 - 编写代码以通过测试 (绿色阶段) (Step 4: Implement - Write Code to Pass Tests (Green)) (`{feature_name}.py`)**
    *   **目标 (Objective)**: 编写刚好足够的代码使所有测试通过。
    *   **AI 执行约束 (AI Execution Constraint)**: AI 助手只有在完成所有前面的思考文档和测试用例 (红色阶段) 后，才能开始编写此功能代码。

5.  **步骤5: 文档与重构 - 改进代码和文档 (Step 5: Document & Refactor - Improve Code and Document) (`_doc_{feature_name}.md`)**
    *   **目标 (Objective)**: 组织文档，解释函数用途、接口和使用示例。在测试的保护下优化代码。
    *   **AI 执行约束 (AI Execution Constraint)**: AI 助手只有在功能代码通过所有测试 (绿色阶段) 后，才能开始创建此文档和重构代码。

这5步循环是 TDD 方法论的基础，旨在促进稳健 (robust)、经过良好测试 (well-tested) 和可维护 (maintainable) 的代码。