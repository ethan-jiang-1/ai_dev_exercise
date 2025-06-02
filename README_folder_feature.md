## 每个 ExTDD 练习的目录结构 (针对 feature的详尽说明, 核心思想)

为了确保每个TDD练习周期的产出物管理清晰、一致且易于理解，我们遵循以下核心原则：

*   **模块化组织**: 所有与特定功能模块（如 `bmi`, `dcnc`）相关的代码和文档都组织在该模块的专属目录中。
*   **关注点分离**: 源代码 (`src`)、测试代码 (`tests`) 和开发过程文档 (`dev_cycles`) 严格分离，各司其职。
*   **标准化命名**: 文件和目录的命名遵循预定义的模式（例如 `ExTDD_NN_{FeatureName}` , 01是FeatureName在BMI模块里的编号），以保证可预测性和自动化处理的潜力。
*   **结构稳定性**: 下述定义的目录结构是固定的，不应随意更改，以维护项目的一致性。

每个模块的TDD练习周期（例如，针对BMI模块的 `ExTDD_01_BMICalculation`）的产出物，将主要集中在 `ai_wellness_advisor/` 目录下。具体组织结构如下：

*   **`ai_wellness_advisor/src/{module_name}/`**: 存放该TDD周期内特定模块的**源代码快照**。
    *   `README_{feature_name}.md`: 对当前特性代码的说明文档。
    *   `{feature_name}.py`: 特性的核心实现代码。
*   **`ai_wellness_advisor/tests/{module_name}/`**: 存放该TDD周期内特定模块的**测试代码快照**。
    *   `test_{feature_name}.py`: 针对特性实现的单元测试代码。
*   **`ai_wellness_advisor/dev_cycles/{module_name}/ExTDD_XX_{FeatureName}/`**: 存放与该TDD练习周期相关的**思考、设计、用户故事、验证和约束**等文档。
    *   `_user_story_{feature_name}.md`: 用户故事描述。
    *   `_s1_think_options_{feature_name}.md`: 思考与选项分析。
    *   `_s2_think_design_{feature_name}.md`: 设计方案。
    *   `_s3_think_validation_{feature_name}.md`: 验证方法与结果。
    *   `_constraints_{feature_name}.md`: (可选) 项目约束或特殊说明。

以下是详细的目录结构示例 (例如，针对BMI模块的 `ExTDD_01_BMICalculation`）：

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
│       └── ExTDD_NN_{feature_name}/ # 例如 ExTDD_01_BMICalculation/
│           ├── _user_story_{feature_name}.md
│           ├── _s1_think_options_{feature_name}.md
│           ├── _s2_think_design_{feature_name}.md
│           ├── _s3_think_validation_{feature_name}.md
│           └── _constraints_{feature_name}.md # (Optional)
```