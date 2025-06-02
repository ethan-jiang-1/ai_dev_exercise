# 规划文档：AI+TDD 练习框架（精简版）
> 版本: 3.1 (精简)

> **通用占位符定义**：
> - `{app_name}`: 指代项目或应用的核心名称，例如 `ai_wellness_advisor`。
> - `{module_name}`: 指代项目中的一个具体模块，例如 `bmi` 或 `dcnc`。
> - `{FeatureName}`: 指代一个特性或功能的驼峰式名称，例如 `BMICalculation`。
> - `{feature_name}`: 指代一个特性或功能的小写下划线名称，例如 `bmi_calculation`。
> - `NN`: 指代一个两位数的序号，例如 `01`, `02`。

本文档概述了AI辅助测试驱动开发 (TDD) 练习框架的核心设计。该框架旨在通过系统性实践TDD的Red-Green-Refactor循环，支持多故事实例，帮助学习者提升TDD技能和AI协作能力。

## 1. 目标 (Goal)
设计一个可扩展的TDD练习框架，其核心目标包括：
*   定义一套通用的、可复用的TDD练习系列模板。
*   允许用户为不同的故事实例提供独立的输入数据和存储独立的输出结果。
*   主要聚焦于后端Python开发场景，严格遵循TDD的 "红-绿-重构" 循环思想。
*   使用AI作为TDD过程中的辅助工具，帮助学习者通过实践掌握TDD的核心节奏和AI协作技巧。

## 2. 核心设计理念：一套流程模板，多个故事与功能系列
*   **核心思想**: 一套通用的TDD练习系列流程模板，应用于多个不同的故事场景，每个故事包含多个具体的微功能开发系列。
*   **TDD阶段对应**: 练习系列严格对应TDD的思考、测试先行(Red)、编码实现(Green)、重构与文档(Refactor)阶段。

## 3. 框架与故事实例的关系
本框架采用"抽象到具体"的三层设计：
1.  **核心理念层** (`test_driven_development_with_ai.md`): 定义思考驱动开发的基本原则、测试驱动思维的重要性、与AI协作的方法论（思考过程优先），以及思考与构建的6个阶段。
2.  **练习框架层** (本文档精简版): 基于核心理念定义通用的TDD练习系列模板（包含5个子步骤）、各步骤的实施指南、输入输出规范和文件命名约定。
3.  **故事实例层**:
    *   `story_tdd_*.md`: 定义具体的故事背景、业务目标、技术栈和初始用户故事。
    *   每个故事实例下的微功能开发都是对框架的具体实现，遵循TDD练习系列模板。
    *   **重要**: 所有代码、测试及文档的产出路径，必须严格遵守项目根目录下 `README_folders.md` 及特性级 `README_folder_feature.md` (如果存在) 中定义的统一目录结构。

## 4. AI 助手能力、边界与协作原则
*   **AI能力假设**: 具备自然语言理解、代码处理（Python, `unittest`)、文件操作、TDD流程支持和Markdown处理能力。
*   **人工主导与AI边界**:
    *   AI生成的测试用例可能不全面，实现代码可能非最优，对复杂业务理解可能有限。
    *   **核心原则：人主导思考，AI辅助执行和验证。学习者应主动批判性思考AI的输出，并对最终产出的质量负责。**

## 5. 目录结构与核心文档
*   **权威目录结构**: **所有实际项目开发和TDD练习的代码、测试、以及最终的思考和设计文档，都必须遵循项目根目录下 `README_folders.md` 文件中定义的统一目录结构。** `exercise_tdd_xxx/` 等目录严格作为TDD练习的“控制器”或“入口点”（静态指南），其内部不包含实际的Python源代码或测试脚本。
*   **框架核心文档**:
    1.  `test_driven_development_with_ai.md`: AI辅助TDD的核心理念与原则。
    2.  本文件 (`planning_tdd_exercise.md` 精简版): TDD练习框架的设计规划。

## 6. TDD练习系列设计 (5步骤核心循环)
每个TDD练习系列模板包含以下5个核心步骤，构成完整的TDD循环。产出文件的存放位置需遵循第3点和第5点中强调的目录规范。

*   **通用输出规范 (重点)**：
    *   思考类Markdown文档 (如 `_s1_think_options_{feature_name}.md`, `_doc_{feature_name}.md`): 存放于 `{app_name}/dev_cycles/{module_name}/ExTDD_XX_FeatureName/`。
    *   功能实现代码 (`{feature_name}.py`): 存放于 `{app_name}/src/{module_name}/`。
    *   测试代码 (`test_{feature_name}.py`): 存放于 `{app_name}/tests/{module_name}/`。
    *   **再次强调**: 具体路径必须符合 `README_folders.md` 和 `README_folder_feature.md` 的规定。

1.  **步骤 1: 思考功能实现可选方案 (`_s1_think_options_{feature_name}.md`)**
    *   **目标**: 分析用户故事，识别核心需求、技术挑战和初步实现思路。
2.  **步骤 2: 设计功能实现方案 (`_s2_think_design_{feature_name}.md`)**
    *   **目标**: 将思路具体化为设计方案，设计函数接口，规划实现步骤。
3.  **步骤 3: 验证功能实现思路与编写测试 (Red) (`_s3_think_validation_{feature_name}.md`, `test_{feature_name}.py`)**
    *   **目标**: 编写一个（或一组）会失败的测试用例。
    *   **关键点**: 若功能单元依赖其他模块，通常需运用测试替身（如Mock对象）隔离依赖。详细技巧参考 `tdd_unit_test_design_techniques.md`。
4.  **步骤 4: 功能实现代码 (Green) (`{feature_name}.py`)**
    *   **目标**: 编写刚好能通过所有测试的功能代码。
5.  **步骤 5: 函数文档完善与代码重构 (Refactor) (`_doc_{feature_name}.md`)**
    *   **目标**: 整理文档，说明函数用途、接口和使用示例，并在测试保护下优化代码。

## 7. 如何使用框架进行练习 (用户视角概要)
1.  选择一个故事实例目录 (e.g., `exercise_tdd_dcnc/`) 和其中的一个练习系列 (e.g., `ExTDD_01_FeatureName/`)。
2.  仔细阅读该练习的用户故事 (`_user_story_{feature_name}.md`) 和任何约束文件。
3.  **严格按照上述5个步骤执行TDD流程**：
    *   为每个步骤创建对应的思考文档、测试代码 (`test_{feature_name}.py`) 和实现代码 (`{feature_name}.py`)。
    *   **务必注意所有文件的正确存放位置**，遵循项目级和特性级的目录规范。
4.  每个步骤完成后进行反思与评估。

## 8. 文件命名规范 (核心规则强调)
为确保一致性，请严格遵守以下命名规范，并结合 `README_folders.md` 和 `README_folder_feature.md` 的具体路径规定：
*   **特性名称 (`{feature_name}`)**: 小写字母，下划线分隔 (e.g., `daily_caloric_needs_calculate`)。
*   **练习系列目录**: `ExTDD_XX_FeatureName` (驼峰式特性名, e.g., `ExTDD_01_DailyCaloricNeedsCalculation`)。
*   **思考文件**: `_s{step_number}_{type}_{feature_name}.md` (e.g., `_s1_think_options_daily_caloric_needs_calculate.md`)。
*   **代码文件**: `{feature_name}.py` (e.g., `daily_caloric_needs_calculate.py`)。
*   **测试文件**: `test_{feature_name}.py` (e.g., `test_daily_caloric_needs_calculate.py`)。
*   **最终文档**: `_doc_{feature_name}.md` (e.g., `_doc_daily_caloric_needs_calculate.md`)。
*   **用户故事**: 通常为 `_user_story_{feature_name}.md` 或在练习系列目录下的 `user_story.md`。
*   **重要**: 文件名中的 `{feature_name}` 必须一致。所有路径需符合项目规范。

## 9. 核心理念与练习框架的步骤映射
本框架的5个TDD步骤是对 `test_driven_development_with_ai.md` 中6个思考构建步骤的实践性转化，强调TDD的Red-Green-Refactor循环：
1.  **步骤1 (思考可选方案)** ≈ 理念步骤1 (问题定义) + 步骤2 (解决方案思考)。
2.  **步骤2 (设计实现方案)** ≈ 理念步骤3 (设计方案思考)。
3.  **步骤3 (验证与测试 - Red)** ≈ 理念步骤4 (验证策略构建)。
4.  **步骤4 (功能实现 - Green)** ≈ 理念步骤5 (解决方案构建)。
5.  **步骤5 (文档与重构 - Refactor)** ≈ 理念步骤6 (文档构建)。
