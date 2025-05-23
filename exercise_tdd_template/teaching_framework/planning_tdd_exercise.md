# 规划文档：AI+TDD 练习框架：支持多故事实例
> 版本: 1.0

本文档概述了用于创建一系列 AI 辅助测试驱动开发 (TDD) 练习的**框架设计**。该框架基于 `test_driven_development_with_ai.md` 的核心理念，旨在支持**多个独立的"故事"或"案例场景"**，每个故事包含若干个遵循 TDD 流程的**微功能开发系列 (Exercise Series)**。重点是使用 AI 辅助**系统性地实践 TDD 的 Red-Green-Refactor 循环**，并完成相应的思考和构建环节。

## 目标 (Goal)

设计一个可扩展的 TDD 练习框架，其中：
1.  定义一套**通用的、可复用的 TDD 练习系列模板 (Exercise Series Templates)**，这些系列演示 `test_driven_development_with_ai.md` 中描述的 AI 辅助 TDD 流程。
2.  允许用户为**不同的故事实例 (Story Instances)**（例如不同的项目或场景）提供独立的输入数据（用户故事）和存储独立的输出结果（思考文档、测试代码、实现代码、API文档）。
3.  阐明框架的核心思考与构建循环 如何在不同练习系列和故事中体现，**并强调 TDD 如何驱动这个循环**。
4.  练习将主要聚焦于后端 Python 开发场景，并严格遵循 TDD 的 "红-绿-重构" 循环思想，**使用 AI 作为 TDD 过程中的辅助工具**。
5.  **帮助学习者通过实践掌握 TDD 的核心节奏 (Red-Green-Refactor) 和 AI 协作技巧**。

## 核心设计理念：一套流程模板，多个故事，多个功能系列

本框架的核心设计理念是：**一套通用的 TDD 练习系列流程模板，应用于多个不同的故事场景，每个故事包含多个具体的微功能开发系列**。

这意味着：
1.  **TDD 练习系列 (Exercise Series)** 是通用的流程模板，定义了从需求分析到文档完善的 TDD 完整闭环，包含 5 个核心步骤，**严格对应 TDD 的思考、测试先行 (Red)、编码实现 (Green)、重构与文档 (Refactor) 阶段**，并与 `test_driven_development_with_ai.md` 中的思考与构建阶段相呼应。这些模板定义在本文件中。
2.  **故事实例 (Story Instance)** 是具体的，提供特定领域或场景的上下文、用户故事和可选的约束文件。每个故事拥有独立的目录。
3.  **微功能实现 (Micro-feature Implementation)** 是在特定故事背景下，对一个 TDD 练习系列模板的具体应用，通常围绕一个用户故事展开。
4.  学习者可以：
    *   在不同故事中实践相同的 TDD 流程，强化 TDD 技能。
    *   选择与自己兴趣或工作最相关的故事场景进行练习。
    *   在熟悉的故事背景中，通过完成多个练习系列，逐步构建更复杂的功能。
5.  教学者可以：
    *   轻松添加新的故事场景和用户故事，无需修改底层教学模型。
    *   为不同背景的学习者提供定制化的 TDD 实践体验。
    *   通过统一的 TDD 步骤和评估标准，对比不同功能实现的质量。

这种"流程模板与故事实例分离"的设计促进了 TDD 方法论的掌握，同时保持了学习体验的相关性和针对性。

## 框架与故事实例的关系

本框架采用"抽象到具体"的三层设计：

1.  **核心理念层** (`test_driven_development_with_ai.md`)：
    *   定义思考驱动开发的基本原则。
    *   确立测试驱动思维的重要性。
    *   规范与AI协作的方法论（思考过程优先）。
    *   定义思考与构建的 6 个阶段。

2.  **练习框架层** (本文档)：
    *   基于核心理念定义通用的 **TDD 练习系列模板 (Exercise Series Templates)**，每个系列包含 5 个子步骤。
    *   设计每个子步骤的输入输出模式、AI 角色和评估要点。
    *   提供练习系列目录（例如 ExTDD_01 到 ExTDD_N）。

3.  **故事实例层**：
    *   `story_tdd_*.md`: 定义具体的故事背景、业务目标、技术栈和初始用户故事。
    *   每个故事实例包含多个微功能开发，每个微功能遵循一个 ExTDD 系列模板。

每个故事实例下的微功能开发都是对框架的具体实现：
1.  遵循 `test_driven_development_with_ai.md` 的核心理念。
2.  采用本文档定义的 TDD 练习系列模板（ExTDD 系列）。
3.  在特定领域场景下，针对一个具体的用户故事，完成 TDD 的 5 个步骤。
4.  提供领域特定的输入文件（用户故事 `inputs/user_story_*.md`）和可选的约束文件 (`constraints/exercise_constraints_*.md`)。
5.  生成结构化的思考文档和代码产物:
    - `{func_name}.py` - 功能实现代码
    - `test_{func_name}.py` - 对应的测试代码
    - `doc_{func_name}.md` - 相关文档（包括实现分析、设计方案和API文档）

例如，ExTDD_01 "实现基础金额检查" 这个练习系列模板，在不同故事中可能应用为：
-   电商故事：实现订单金额有效性检查。
-   金融故事：实现交易金额阈值检查。
-   医疗故事：实现检查费用有效性检查。

这种设计确保了：
-   TDD 方法论实践的一致性（通过统一的系列模板）。
-   实践场景的多样性（通过不同的故事）。
-   学习路径的渐进性（通过完成故事中的多个功能系列）。
-   评估标准的统一性（通过共同的评估框架）。

## 假设的工具与能力

这些练习假设使用具备以下能力的 AI 助手（如 Cursor）：
*   处理指令的自然语言理解能力。
*   代码生成和解释能力（尤其是 Python 和 `unittest`）。
*   读取工作区内文件和写入文件的能力。
*   遵循 TDD 流程，能够基于测试生成代码，并进行重构的能力。
*   Markdown 渲染和生成技能。

## 提议的目录结构 (支持多故事, 只是示范, 参考, 指导目录结构而已)

```
project_root_or_exercise_name/
├── teaching_framework/                     (框架文档目录)
│   ├── test_driven_development_with_ai.md  (思考驱动开发核心理念)
│   └── planning_tdd_exercise.md            (本文件 - TDD 练习框架设计规划)
|
├── story_tdd_OverallStoryName.md           (某个具体"大故事"或"项目"的总体描述)
│
├── tdd_OverallStoryName/                   (针对 "OverallStoryName" 的TDD练习目录)
│   ├── story_tdd_OverallStoryName.md       (该故事的详细描述或副本)
│   ├── README.md                           (当前故事的总体说明和目标)
│   │
│   ├── ExTDD_01_FeatureNameA/              (第一个具体功能点/模块的练习)
│   │   ├── constraints/                    (约束文件目录)
│   │   │   └── task_constraints.md         (当前功能点的特定约束)
│   │   ├── inputs/                         (输入文件目录)
│   │   │   ├── test_data.json              (或 relevant_input_data.{ext})
│   │   │   └── user_story.md               (当前功能点的用户故事片段/需求)
│   │   ├── outputs/                        (输出文件 - TDD步骤产物)
│   │   │   ├── _s1_think_options_FeatureNameA.md
│   │   │   ├── _s2_think_design_FeatureNameA.md
│   │   │   ├── _s3_think_validation_FeatureNameA.md
│   │   │   ├── FeatureNameA.{ext}          (例如: FeatureNameA.py, FeatureNameA.js)
│   │   │   ├── test_FeatureNameA.{ext}     (例如: test_FeatureNameA.py)
│   │   │   └── doc_FeatureNameA.md
│   │   └── README.md                       (当前功能点 ExTDD_01_FeatureNameA 的练习说明)
│   │
│   ├── ExTDD_02_FeatureNameB/              (第二个具体功能点/模块的练习)
│   │   ├── constraints/
│   │   ├── inputs/
│   │   ├── outputs/                        (与 ExTDD_01_FeatureNameA/outputs/ 结构类似)
│   │   │   ├── _s1_think_options_FeatureNameB.md
│   │   │   ├── _s2_think_design_FeatureNameB.md
│   │   │   ├── _s3_think_validation_FeatureNameB.md
│   │   │   ├── FeatureNameB.{ext}
│   │   │   ├── test_FeatureNameB.{ext}
│   │   │   └── doc_FeatureNameB.md
│   │   └── README.md                       (当前功能点 ExTDD_02_FeatureNameB 的练习说明)
│   │
│   ├── ... (更多 ExTDD_XX_FeatureNameX 目录，代表更多功能点)
│
├── tdd_AnotherStoryName/                   (另一个完整"大故事"的TDD练习目录)
│   ├── story_tdd_AnotherStoryName.md
│   ├── README.md
│   ├── ExTDD_01_SomeOtherFeatureY/
│   │   └── ... (结构同上)
│   └── ...
│
└── ... (可以添加更多顶级故事实例目录 tdd_XYZStoryName)
```

*说明*:
- 每个"大故事"实例 (例如 `tdd_OverallStoryName`, `tdd_AnotherStoryName`) 都在项目根目录级别有一个对应的总体故事描述文件 (如 `story_tdd_OverallStoryName.md`)，并且在其各自的 `tdd_OverallStoryName/` 目录下也会有一个详细的故事描述文件 (可以是副本或更细化的版本)。
- 每个具体的功能点练习都组织在 `ExTDD_XX_FeatureName/` 目录下，包含该功能点开发所需的特定约束、输入数据和最终的输出产物。
- 每个功能点练习的 TDD 流程都体现在其 `outputs/` 目录下的系列文件中，通常包括：思考选项 (`_s1_think_options_...`), 思考设计 (`_s2_think_design_...`), 思考验证 (`_s3_think_validation_...`), 功能实现代码 (`FeatureName.{ext}`), 测试代码 (`test_FeatureName.{ext}`), 和相关文档 (`doc_FeatureName.md`)。文件扩展名 (`.{ext}`) 会根据实际项目所用的技术栈 (如 Python 的 `.py`, JavaScript 的 `.js` 等) 而变化。
- 这种结构旨在清晰地分离不同故事和同一故事内不同功能点的开发过程，并完整记录TDD的每一个思考和实现步骤。

## 框架文件说明

本框架包含两个核心文件：

1.  **测试驱动开发核心理念** (`test_driven_development_with_ai.md`)
    *   定义了与 AI 协作进行 TDD 的基本原则和方法论。
    *   强调了思考留痕和结构化思考的重要性。
    *   提供了 AI 协作的最佳实践和 6 个思考/构建阶段。

2.  **TDD 练习框架设计规划** (本文件 `planning_tdd_exercise.md`)
    *   定义了一套完整的 **TDD 练习系列模板 (Exercise Series Templates)**。
    *   提供了每个 TDD 步骤的实施指南和评估标准。
    *   规范了练习系列的输入输出格式和文件命名。
    *   设计了可扩展的多故事支持机制。

这两个文件形成了完整的框架体系：核心理念文件提供思想指导，本文件则将这些理念转化为可执行的 TDD 练习框架。每个故事实例中的微功能开发都是这个框架的具体实现。

## 练习系列设计与定义流程

1.  **识别通用功能模式**: 回顾常见开发任务，识别可以抽象为通用 **TDD 练习系列模板 (Exercise Series Template)** 的功能模式（例如，简单验证、数据处理、状态管理等）。
2.  **在本文档中定义练习系列模板**: 为每个识别出的模板创建条目，包含：
    *   **系列 ID 与名称**: 清晰的顺序 ID (例如 `ExTDD_01`) 和描述性中文名称，代表练习系列的**类型**。
    *   **系列目标 (Series Goal)**: 该**类型**的练习系列旨在让用户掌握的 TDD 应用场景或特定功能模式。
    *   **系列复杂度 (Series Complexity)**: 低、中、高，表示该**类型**系列通常涉及的功能复杂度。
    *   **针对该系列的 5 个步骤定义**: (注意：这些步骤共同构成了 TDD 的核心循环)
        *   **步骤 1: 思考功能实现可选方案 (`_s1_think_options_{feature_name}.md`)**
            *   **目标**: 分析用户故事，识别核心需求、技术挑战和初步实现思路。
            *   **输入模式**: `inputs/user_story.md`
            *   **AI 助手角色**: 分析师，帮助理解需求、识别边界、提出初步方案。
            *   **输出**: 包含分析结果和可选实现方案的 Markdown 文件。
            *   **评估**: 是否准确识别需求和挑战？方案是否初步可行？
        *   **步骤 2: 设计功能实现方案 (`_s2_think_design_{feature_name}.md`)**
            *   **目标**: 将思路具体化为设计方案，设计函数接口，规划实现步骤。
            *   **输入模式**: `outputs/ExTDD_XX_FeatureName/_s1_think_options_{feature_name}.md`
            *   **AI 助手角色**: 设计师/规划师，帮助详细设计功能的实现方案。
            *   **输出**: 设计方案 Markdown 文件，包含函数设计、测试设计和实现步骤。
            *   **评估**: 设计是否合理？接口设计是否清晰？测试设计是否全面？
        *   **步骤 3: 验证功能实现思路 (`_s3_think_validation_{feature_name}.md`, `test_{feature_name}.py`)**
            *   **目标**: 验证设计方案的可行性，编写测试用例。**这是 TDD 的 "Red" 阶段的准备工作，目标是编写一个（或一组）会失败的测试**。在设计这些测试时，如果功能单元依赖其他模块，通常需要运用测试替身（如Mock对象）来隔离依赖，确保测试的焦点。关于如何有效地设计这些单元测试及应用Mocking技术，请参阅《TDD单元测试设计技巧》(`./tdd_unit_test_design_techniques.md`)。
            *   **输入模式**: `outputs/ExTDD_XX_FeatureName/_s2_think_design_{feature_name}.md`
            *   **AI 助手角色**: 测试工程师，帮助验证设计方案、编写测试用例。
            *   **输出**: 验证方案 Markdown 文件和包含单元测试的 Python 文件 (此时运行应失败 - Red)。
            *   **评估**: 测试用例是否覆盖主要路径和边界？测试是否可以正确运行？
        *   **步骤 4: 功能实现代码 (`{feature_name}.py`)**
            *   **目标**: 编写刚好能通过所有测试的功能代码。**这是 TDD 的 "Green" 阶段，目标是让之前失败的测试通过**。
            *   **输入模式**: `outputs/ExTDD_XX_FeatureName/_s3_think_validation_{feature_name}.md`, `test_{feature_name}.py`
            *   **AI 助手角色**: 开发者，根据测试用例编写功能代码，使其通过测试 (Green)。
            *   **输出**: 包含通过测试的功能代码的 Python 文件。
            *   **评估**: 是否所有测试都通过？代码是否简洁且仅满足测试需求？
        *   **步骤 5: 函数文档完善 (`doc_{feature_name}.md`)**
            *   **目标**: 整理文档，说明函数用途、接口和使用示例。**这是 TDD 的 "Refactor" 阶段，在测试保护下完善文档和代码**。
            *   **输入模式**: `outputs/ExTDD_XX_FeatureName/{feature_name}.py`, `test_{feature_name}.py`
            *   **AI 助手角色**: 文档工程师/重构师，帮助完善文档、优化代码 (Refactor)。
            *   **输出**: 完整的 API 文档 Markdown 文件。
            *   **评估**: 文档是否清晰准确？使用示例是否充分？
3.  **为具体故事创建输入用户故事**: 在每个故事实例的练习系列目录下的 `inputs/` 目录中，创建 `user_story.md` 文件，描述该练习系列的具体功能需求。
4.  **创建任务约束文件**: 在每个故事实例的练习系列目录下的 `constraints/` 目录中，创建 `task_constraints.md` 文件，描述该功能实现的具体约束条件。
5.  **审查与完善**: 审查本文档（模板库）的清晰性、一致性和可行性。

## 如何使用框架进行练习 (用户视角)

#### **关于运行单元测试的重要说明**

本框架中的单元测试文件（`test_{feature_name}.py`）和其对应的被测功能代码文件（`{feature_name}.py`）都位于各自特性练习目录下的 `outputs/` 子目录中 (例如，`./tdd_OverallStoryName/ExTDD_01_FeatureNameA/outputs/`)。

为了确保测试文件能够正确导入同一目录下的被测模块，同时避免在内容生成或编辑过程中频繁手动切换主终端的工作目录，**推荐采用让单元测试命令本身临时改变其执行工作目录的方式**。

例如，在Linux或macOS的bash/zsh环境下，可以这样执行测试：

*   运行特定的测试文件 (例如 `test_FeatureNameA.py`)：
    ```bash
    (cd ./tdd_OverallStoryName/ExTDD_01_FeatureNameA/outputs/ && python -m unittest test_FeatureNameA.py)
    ```
*   运行指定目录下所有的测试文件 (discover模式)：
    ```bash
    (cd ./tdd_OverallStoryName/ExTDD_01_FeatureNameA/outputs/ && python -m unittest discover)
    ```

**这种方式的工作原理：**
*   `(...)`：圆括号会创建一个子shell（subshell）。
*   `cd ./path/to/.../outputs/`：在子shell中，首先临时切换到包含测试和代码文件的 `outputs/` 目录。请将示例路径替换为实际的练习路径。
*   `python -m unittest ...`：接着，在该 `outputs/` 目录下执行Python的单元测试命令。
*   当子shell中的命令执行完毕后，子shell会退出，您的主终端工作目录将保持在执行此命令之前的位置，不受影响。

采用这种方法可以有效地避免因Python模块导入错误（`ImportError`）导致的测试失败，并保持您主工作流程的整洁与连贯。

1.  **选择一个故事实例**: 选择一个故事实例目录，例如 `exercise_tdd_xxx/` 或 `exercise_tdd_yyy/`。
2.  **了解故事背景**: 阅读对应的故事描述文件，例如 `story_tdd_xxx.md` 或 `tdd_pydantic/story_tdd_yyy.md`。
3.  **选择一个练习系列**: 根据故事中描述的功能，选择对应的 ExTDD 目录，例如 `tdd_bmi_calculator/ExTDD_01_{task_name}/`。
4.  **了解用户故事和约束**: 阅读该练习系列的 `inputs/user_story.md` 和 `constraints/task_constraints.md` 文件。
5.  **按步骤执行 TDD 流程**:
   *   **步骤 1**: 思考功能实现的可选方案，将思考过程记录在 `outputs/_s1_think_options_{feature_name}.md` 中。
   *   **步骤 2**: 设计功能实现方案，记录在 `outputs/_s2_think_design_{feature_name}.md` 中。
   *   **步骤 3**: 验证功能实现思路并编写测试代码，记录验证思路在 `outputs/_s3_think_validation_{feature_name}.md` 中，编写测试代码 `outputs/test_{feature_name}.py`。运行测试，确认失败 (Red)。
   *   **步骤 4**: 实现功能代码 `outputs/{feature_name}.py`，使其通过测试 (Green)。
   *   **步骤 5**: 完善文档 `outputs/doc_{feature_name}.md` (Refactor)。
6.  **反思与评估**: 参考每个步骤的评估要点，反思 TDD 流程的应用和 AI 辅助的效果。
7.  **继续下一个练习**: 选择同一故事中的下一个练习系列，或者选择另一个故事实例，重复步骤 3-6。

文件命名应遵循前文所述的命名规范，确保所有练习的文件结构保持一致性。

## 输入文件设计原则 (针对具体故事的用户故事)

*   **聚焦单一功能**: 每个用户故事应尽可能描述一个独立的、可测试的小功能。
*   **明确验收标准**: 用户故事中应包含清晰的成功条件，便于后续设计测试用例。
*   **故事相关性**: 用户故事内容需与所属故事实例的背景和目标一致。
*   **适度复杂性**: 用户故事的复杂度可根据故事或练习系列类型调整，允许从简单到复杂。

## 文件命名规范

为确保所有文件和目录结构的一致性，我们采用以下命名规范：

1. **特性名称 (feature_name)**：
   - 格式：`小写字母_用下划线分隔`
   - 示例：`bmi_calculate`, `bmi_categorize`, `api_data_validator`
   - 要求：描述性、简洁、表明功能

2. **目录命名**：
   - 练习系列目录：`ExTDD_XX_FeatureName`
     - XX：两位数字编号（01、02等）
     - FeatureName：驼峰式命名
     - 示例：`ExTDD_01_BMICalculation`, `ExTDD_02_BMICategorization`

3. **文件命名**：
   - 思考文件：`_s{step}_{type}_{feature_name}.md`
     - 示例：`_s1_think_options_bmi_calculate.md`
   - 代码文件：`{feature_name}.py`
     - 示例：`bmi_calculate.py`, `api_data_validator.py`
   - 测试文件：`test_{feature_name}.py`
     - 示例：`test_bmi_calculate.py`
   - 文档文件：`doc_{feature_name}.md`
     - 示例：`doc_bmi_calculate.md`

4. **用户故事和约束文件**：
   - 用户故事：`user_story.md`
   - 任务约束：`task_constraints.md`

这些命名规范确保了所有练习系列和功能实现的文件结构保持一致，便于组织和查找。

## AI 能力边界注意

在执行练习和评估结果时，请始终牢记 `test_driven_development_with_ai.md` 中提到的 **AI 能力边界**。
*   AI 生成的测试用例可能不够全面，需要人工补充边界情况。
*   AI 生成的实现代码可能不是最优的，需要人工审查和重构。
*   AI 对复杂业务逻辑的理解可能有限，需要清晰的指导和分解。
*   **关键在于人主导思考，AI辅助执行和验证。**

## 后续步骤

1.  审查这份最终的规划文档。
2.  **选择或创建一个初始故事实例** (例如 `story_tdd_xxx/`)。
3.  为该初始故事实例，在对应的 `inputs/` 目录中创建至少一到两个具体的 `user_story_*.md` 文件，与本文档中定义的练习系列类型相匹配。

## 核心理念与练习框架的步骤映射

本框架的5个TDD步骤是对`test_driven_development_with_ai.md`中6个思考构建步骤的实践性转化。以下是它们的对应关系：

1. **核心理念文档中的6个步骤**:
   - `user_story.md` → 问题定义
   - `_s1_think_options_{user_story}.md` → 解决方案思考
   - `_s2_think_design_{user_story}.md` → 设计方案思考
   - `_s3_think_validation_{user_story}.md` → 验证策略构建
   - `build_solution.{ext}` + `build_solution_tests.{ext}` → 解决方案构建
   - `doc_build_solution.md` → 文档构建

2. **练习框架中的5个TDD步骤**:
   - 步骤1 (`_s1_think_options_{user_story}.md`) ← 对应理念步骤1-2
   - 步骤2 (`_s2_think_design_{user_story}.md`) ← 对应理念步骤3
   - 步骤3 (`test_{func_name}.py`) ← 对应理念步骤4
   - 步骤4 (`{func_name}.py`) ← 对应理念步骤5
   - 步骤5 (`doc_{func_name}.md`) ← 对应理念步骤6

3. **关键区别说明**:
   - 练习框架将理念文档中的前两个步骤（问题定义和解决方案思考）合并为一个实践步骤
   - 练习框架更强调TDD的"Red-Green-Refactor"循环，将其明确体现在步骤3-5中
   - 每个步骤都保持了思考在先、实现在后的核心原则
   - 文件命名约定更加规范化，便于在多个故事实例中统一使用

## 示例练习系列：ExTDD_01 简单计算/验证功能

这是一个基础的练习系列模板，用于指导如何实现简单的计算或验证功能。

### 系列定义

- **系列ID**: ExTDD_01
- **名称**: 简单计算/验证功能系列
- **目标**: 掌握基础的数值计算和输入验证的TDD实践
- **复杂度**: 低
- **技术要求**: Python, unittest
- **适用场景**: 单一函数的数值计算、数据验证、简单转换等

### 步骤指导

1. **步骤1 - 实现思考** (`_s1_think_options_{feature_name}.md`):
   ```markdown
   # 功能名称 - 实现思考
   
   ## 1. 核心需求分析
   - 明确输入参数及其限制
   - 定义预期输出及其格式
   - 识别异常情况
   
   ## 2. 技术挑战
   - 输入验证要点
   - 计算/处理精度要求
   - 错误处理策略
   
   ## 3. 可选方案
   - 函数式方案
   - 类封装方案
   - 异常处理方案
   ```

2. **步骤2 - 设计方案** (`_s2_think_design_{feature_name}.md`):
   ```markdown
   # 功能名称 - 设计方案
   
   ## 函数/类接口设计
   - 参数定义及类型
   - 返回值类型
   - 异常定义
   
   ## 实现步骤
   1. 输入验证
   2. 核心处理
   3. 结果格式化
   ```

3. **步骤3 - 测试设计** (`test_{feature_name}.py`):
   ```python
   """测试用例应覆盖：
   1. 正常输入场景
   2. 边界值场景
   3. 异常输入场景
   """
   ```

4. **步骤4 - 功能实现** (`{feature_name}.py`):
   ```python
   """实现要点：
   1. 严格遵循测试用例
   2. 实现必要的验证
   3. 保持代码简洁
   """
   ```

5. **步骤5 - API文档** (`doc_{feature_name}.md`):
   ```markdown
   # API文档模板
   
   ## 功能说明
   - 目的
   - 使用场景
   
   ## 接口定义
   - 参数说明
   - 返回值说明
   - 异常说明
   
   ## 使用示例
   - 基本用法
   - 异常处理
   ```

### 评估要点

1. **需求理解**
   - 是否准确识别了核心功能需求
   - 是否考虑了必要的边界条件

2. **测试设计**
   - 是否覆盖了主要场景
   - 是否包含边界测试
   - 是否测试了异常情况

3. **实现质量**
   - 代码是否简洁清晰
   - 是否恰当处理了异常
   - 是否符合Python编码规范

4. **文档完整性**
   - 是否清晰说明了使用方法
   - 是否完整记录了参数和返回值
   - 是否提供了适当的示例

### 注意事项

- 保持功能单一，专注于一个计算或验证任务
- 优先考虑代码的可读性和可维护性
- 确保异常处理的合理性和友好性
- 注意数值计算的精度要求
