## ExTDD 特性研发目录结构：核心原则与详解

为了确保每个TDD练习周期的产出物管理清晰、一致且易于理解，我们定义了以下核心原则。**模块（Module）、特性（Feature）及其在该模块内的顺序编号（NN）是决定整个目录结构和命名规范的基石，其重要性贯穿始终：**

*   **模块化组织 (Module-centric)**: 所有与特定功能模块（例如 `bmi`, `dcnc`）相关的代码和文档，都严格地组织在该模块的专属目录中。这是我们组织项目结构的第一层级划分，确保了不同模块间的独立性。
*   **关注点分离**: 源代码 (`src`)、测试代码 (`tests`) 和开发过程文档 (`dev_cycles`) 严格分离，各司其职。
*   **标准化命名 (Standardized Naming for Features & Sequence)**:
    *   **核心要素**: 模块名 (`{module_name}`), 特性在该模块内的两位数字顺序编号 (`NN`), 以及特性名 (`{FeatureName}`) 是构成所有相关目录和文件命名的核心要素。
    *   开发周期目录命名为 `ExTDD_NN_{FeatureName}`。这里的 `NN` (例如 `01`, `02`) 至关重要，它不仅标识了特性在模块内的开发顺序，也确保了目录的唯一性和可追溯性。`{FeatureName}` 通常采用驼峰式命名 (e.g., `BMICalculation`)。
    *   相关的源代码文件 (`.py`)、测试文件 (`test_*.py`) 及 Markdown 文档 (`.md`) 文件名中的特性部分，则统一使用 `{FeatureName}` 对应的小写形式 (e.g., `bmicalculation.py`, `README_bmicalculation.md`)，以保持一致性。
    *   这种基于模块、特性和序号的统一命名规则，是保证项目可预测性、可维护性和自动化处理潜力的关键。
*   **结构稳定性**: 下述定义的目录结构是固定的，不应随意更改，以维护项目的一致性。

基于上述核心原则，特别是围绕**模块**、**特性**及其**序号**的组织方式，每个模块内的一个TDD练习周期 (例如，`bmi` 模块的第一个特性 `ExTDD_01_BMICalculation`) 的产出物，在 `ai_wellness_advisor/` 目录内按以下结构组织：

*   **`ai_wellness_advisor/src/{module_name}/`**: 存放该TDD周期内特定模块的**源代码快照**。
    *   `README_{feature_name}.md`: 对当前特性代码的说明文档 (例如 `README_bmicalculation.md`)。
    *   `{feature_name}.py`: 特性的核心实现代码 (例如 `bmicalculation.py`)。
*   **`ai_wellness_advisor/tests/{module_name}/`**: 存放该TDD周期内特定模块的**测试代码快照**。
    *   `test_{feature_name}.py`: 针对特性实现的单元测试代码 (例如 `test_bmicalculation.py`)。
*   **`ai_wellness_advisor/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/`**: 存放与该TDD练习周期相关的**思考、设计、用户故事、验证和约束**等文档 (例如 `ExTDD_01_BMICalculation/`)。
    *   `_user_story_{feature_name}.md`: 用户故事描述。
    *   `_s1_think_options_{feature_name}.md`: 思考与选项分析。
    *   `_s2_think_design_{feature_name}.md`: 设计方案。
    *   `_s3_think_validation_{feature_name}.md`: 验证方法与结果。
    *   `_constraints_{feature_name}.md`: (可选) 项目约束或特殊说明。

以下针对**某一特定模块 (`{module_name}`) 内**的一个具体特性（Feature），其在该模块内的顺序由 `NN` 标识，特性名为 `{FeatureName}` 的目录结构示例。请再次注意这些核心要素是如何共同定义目录和文件路径的 (再次强调，`NN` 代表该特性在该模块内的两位数字编号，`{FeatureName}` 为驼峰式命名，其余文件名中特性相关部分统一使用小写)：

```
ai_wellness_advisor/
├── src/                            # (Source Code Snapshot) TDD周期内的源代码快照
│   └── {module_name}/              # 例如 bmi/
│       ├── README_{feature_name}.md
│       └── {feature_name}.py
├── tests/                          # (Test Code Snapshot) TDD周期内的测试代码快照
│   └── {module_name}/              # 例如 bmi/
│       └── test_{feature_name}.py
├── dev_cycles/                     # (User Story, Design and Planning Documents) 思考、设计、约束、验证等文档
│   └── {module_name}/              # 例如 bmi/
│       └── ExTDD_NN_{FeatureName}/ # 例如 ExTDD_01_BMICalculation/
│           ├── _user_story_{feature_name}.md
│           ├── _s1_think_options_{feature_name}.md
│           ├── _s2_think_design_{feature_name}.md
│           ├── _s3_think_validation_{feature_name}.md
│           └── _constraints_{feature_name}.md # (Optional)
```