# AI个性化健康顾问：项目迁移与演进执行计划

**与LLM协作执行此多步骤计划的注意事项：**

*   **任务分解与原子化**：每个编号的步骤应被视为一个独立的、可与LLM交互的任务单元。在指导LLM时，一次专注于一个或少数几个紧密相关的子步骤。
*   **明确指令与预期输出**：对每个步骤，向LLM提供清晰、无歧义的指令，并明确说明预期的产出物或状态变化。
*   **上下文保持与提醒**：在连续步骤中，可能需要提醒LLM当前的上下文（例如，当前正在处理的模块、目标目录结构等）。
*   **增量验证**：在关键步骤完成后（尤其是涉及文件修改、代码生成、测试执行的步骤），立即进行验证，确保结果符合预期，再进行下一步。
*   **错误处理与迭代**：如果LLM的输出不符合预期，需要有机制进行反馈、修正指令并要求LLM重试。
*   **人类监督与决策**：对于设计决策、复杂逻辑判断或最终确认等环节，仍需人工介入和把关。

详细的项目目录结构请查阅：[`overall_folder_structure.md`](./overall_folder_structure.md)

## 执行步骤 (TodoList)

**阶段一：搭建统一项目基础 (`ai_wellness_advisor`)**

*   **P1_S01_CreateProjectRoot**: [ ] 1.1 创建顶级项目目录: 在 `/Users/bowhead/ai_dev_exercise_tdd/` 下创建新目录 `ai_wellness_advisor`。
*   **P1_S02_InitProjectStructure**: [ ] 1.2 初始化项目结构: 在 `ai_wellness_advisor` 内创建基础结构，例如：
    *   `ai_wellness_advisor/src/` (存放所有Python模块源代码)
    *   `ai_wellness_advisor/tests/` (存放所有Python测试代码)
    *   `ai_wellness_advisor/docs/` (存放项目级文档、架构图等)
    *   `ai_wellness_advisor/docs/user_stories/` (存放所有模块的用户故事/需求文档)
    *   `ai_wellness_advisor/requirements.txt` (或 `pyproject.toml` 用于依赖管理)
    *   `ai_wellness_advisor/.gitignore`
    *   `ai_wellness_advisor/README.md` (项目总体说明)
    *   **LLM协作注意事项 (P1_S02):**
        *   **目录创建确认**: LLM执行创建目录结构后，应要求其列出创建的目录和文件，以供人工核对。
        *   **初始化文件内容**: 对于 `requirements.txt`, `.gitignore`, `README.md` 等文件，可以提供初始模板或要求LLM生成基础内容，并进行人工审查。

**阶段二：迁移现有0层模块**

对于每个现有的 `exercise_tdd_xxx` (bmi, dcnc, pydantic, llm)，依次执行以下步骤 (以 `bmi` 模块为例进行命名，其他模块类似)：

*   **P2_BMI_S01_MigrateSourceCode**: [ ] 2.1.1 (BMI) 迁移源代码: 将 `exercise_tdd_bmi/tdd_bmi_calculator/ExTDD_01_BMICalculator/outputs/bmi_calculator.py` 移动到 `ai_wellness_advisor/src/bmi/calculator.py`。
*   **P2_BMI_S02_MigrateTests**: [ ] 2.1.2 (BMI) 迁移测试代码: 将 `exercise_tdd_bmi/tdd_bmi_calculator/ExTDD_01_BMICalculator/outputs/test_bmi_calculator.py` 移动到 `ai_wellness_advisor/tests/bmi/test_calculator.py`。
*   **P2_BMI_S03_MigrateStoryDoc**: [ ] 2.1.3 (BMI) 迁移用户故事/需求文档: 将 `exercise_tdd_bmi/story_bmi.md` (或其核心需求部分) 整理并移动到 `ai_wellness_advisor/docs/user_stories/bmi_story.md`。
*   **P2_BMI_S04_MigrateTDDProcessDocs**: [ ] 2.1.4 (BMI) 迁移TDD过程文档 (可选但推荐): 将 `exercise_tdd_bmi/tdd_bmi_calculator/ExTDD_01_BMICalculator/outputs/_s*.md` 等思考和设计文档，归档到 `ai_wellness_advisor/docs/tdd_process_archive/bmi/ExTDD_01_BMICalculator/`。
*   **P2_BMI_S05_UpdateExerciseDir**: [ ] 2.1.5 (BMI) 更新 `exercise_tdd_bmi` 目录: 
    *   删除其下的代码和测试副本。
    *   修改其 `story_bmi.md` (或创建一个新的 `README.md`)，使其内容转变为对 `ai_wellness_advisor` 项目中对应模块的TDD练习指引。说明如何在 `ai_wellness_advisor` 中找到代码、运行测试、查看需求。
    *   保留 `teaching_framework` 等通用指导文档。
*   **P2_DCNC_S01_MigrateSourceCode**: [ ] 2.2.1 (DCNC) 迁移源代码 ...
*   **P2_DCNC_S02_MigrateTests**: [ ] 2.2.2 (DCNC) 迁移测试代码 ...
*   ... (DCNC模块的其他步骤 P2_DCNC_S03 至 P2_DCNC_S05)
*   **P2_PYDANTIC_S01_MigrateSourceCode**: [ ] 2.3.1 (Pydantic) 迁移源代码 ...
*   ... (Pydantic模块的其他步骤 P2_PYDANTIC_S02 至 P2_PYDANTIC_S05)
*   **P2_LLM_S01_MigrateSourceCode**: [ ] 2.4.1 (LLM) 迁移源代码 ...
*   ... (LLM模块的其他步骤 P2_LLM_S02 至 P2_LLM_S05)
*   **P2_ALL_S06_AdjustImportPaths**: [ ] 2.5 调整导入路径: 确保 `ai_wellness_advisor` 项目内的测试代码可以正确导入对应的源代码模块。可能需要调整 `sys.path` 或使用Python包结构。
*   **P2_ALL_S07_VerifyTests**: [ ] 2.6 验证测试: 在 `ai_wellness_advisor` 项目根目录下运行所有已迁移模块的测试，确保通过。
    *   **LLM协作注意事项 (阶段二 - 针对每个0层模块的迁移):**
        *   **精确文件定位**: 确保LLM能够准确理解源文件路径模式 (`exercise_tdd_xxx/tdd_xxx_yyy/ExTDD_ZZ_FeatureName/outputs/...`) 和目标路径模式 (`ai_wellness_advisor/src/{module_name}/`)，特别是 `{module_name}` 的正确替换。
        *   **迁移操作确认**: 每个文件迁移后，要求LLM确认源文件已删除（或按策略处理）且目标文件已正确创建。
        *   **`story_xxx.md` 更新指导**: 对于步骤 `P2_XXX_S05_UpdateExerciseDir`，需要向LLM提供清晰的指导，说明更新后的 `story_xxx.md` 或 `README.md` 应包含哪些关键信息（如指向新代码库的链接、运行测试的命令等）。可能需要提供一个模板或示例。
        *   **导入路径调整 (P2_ALL_S06_AdjustImportPaths)**: 这是关键且易错步骤。需要LLM分析迁移后的代码，识别并修正导入语句。建议先让LLM列出需要修改的导入语句，人工确认后再执行修改。或者，提供明确的Python包结构，指导LLM如何调整。
        *   **测试验证 (P2_ALL_S07_VerifyTests)**: LLM执行测试后，要求其提供完整的测试报告。如果测试失败，需要LLM协助分析失败原因（例如，导入错误、代码逻辑问题），并进行修复尝试。

**阶段三：规划并启动新练习集 `exercise_ai_wellness_advisor`**

*   **P3_S01_CreateNewExerciseDir**: [ ] 3.1 创建 `exercise_ai_wellness_advisor` 目录: 在 `/Users/bowhead/ai_dev_exercise_tdd/` 下创建 `exercise_ai_wellness_advisor`。
*   **P3_S02_InitNewExercise**: [ ] 3.2 初始化 `exercise_ai_wellness_advisor`:
    *   复制 `/Users/bowhead/ai_dev_exercise_tdd/exercise_tdd_template/teaching_framework/` 到 `exercise_ai_wellness_advisor/`。
    *   根据 `/Users/bowhead/ai_dev_exercise_tdd/exercise_tdd_template/generate_tdd_exercise_instructions.md` 的指导，与AI协作（或手动）生成 `exercise_ai_wellness_advisor/story_ai_wellness_advisor_core_services.md`，内容如全盘计划文档第2部分所述。
*   **P3_S03_ClarifyOutputLocationInStory**: [ ] 3.3 明确产出物位置: 在 `story_ai_wellness_advisor_core_services.md` 中明确指出，虽然TDD的思考和流程文档在该练习集目录中，但实际的代码和测试将直接在 `ai_wellness_advisor` 项目中创建和修改。
    *   **LLM协作注意事项 (阶段三):**
        *   **`story`文档生成 (P3_S02)**: 与LLM协作生成 `story_ai_wellness_advisor_core_services.md` 时，需仔细审查LLM提出的用户故事、需求描述和TDD练习系列划分，确保其符合项目目标且具有可测试性。
        *   **产出物位置强调 (P3_S03 及后续)**: 在与LLM后续交互开发第1、2层功能时，需反复强调代码和测试的实际存放位置是在 `ai_wellness_advisor` 项目中，避免LLM在 `exercise_ai_wellness_advisor` 目录下错误地创建它们。

**阶段四：通过TDD开发第1层和第2层功能 (`core_services`)**

*   **P4_F01_WellnessProfileBuilder_ExecuteTDD**: [ ] 4.1 执行 `ExTDD_01_WellnessProfileBuilder`:
    *   **P4_F01_S01_GenerateThinkingDocs_And_Placeholder**: [ ] 4.1.1 遵循 `story_ai_wellness_advisor_core_services.md` 中该练习系列的指引，在 `ai_wellness_advisor/docs/tdd_process_archive/core_services/ExTDD_01_WellnessProfileBuilder/` 中生成实际的思考文档 `_s1_think_options_wellness_profile_builder.md`, `_s2_think_design_wellness_profile_builder.md`, `_s3_think_validation_wellness_profile_builder.md`。同时，在 `exercise_ai_wellness_advisor/tdd_feature_notes/ExTDD_01_WellnessProfileBuilder/` 目录下创建指向这些实际文档的占位符或引用说明文件 (例如，`README.md` 或 `reference_to_actual_docs.md`)。
    *   **P4_F01_S02_CreateTestFile_Red**: [ ] 4.1.2 在 `ai_wellness_advisor/tests/core_services/` 中创建 `test_wellness_profile_builder.py` (Red)。
    *   **P4_F01_S03_CreateSourceFile_Green**: [ ] 4.1.3 在 `ai_wellness_advisor/src/core_services/` 中创建 `wellness_profile_builder.py` (Green)。
    *   **P4_F01_S04_GenerateFeatureDoc_And_Placeholder_Refactor**: [ ] 4.1.4 在 `ai_wellness_advisor/docs/tdd_process_archive/core_services/ExTDD_01_WellnessProfileBuilder/` 中生成实际的特性文档 `doc_wellness_profile_builder.md` (Refactor)。同时，在 `exercise_ai_wellness_advisor/tdd_feature_notes/ExTDD_01_WellnessProfileBuilder/` 目录下的占位符或引用说明文件中更新或添加指向此特性文档的引用。
*   **P4_F02_PersonalizedAdvisor_ExecuteTDD**: [ ] 4.2 执行 `ExTDD_02_PersonalizedAdvisor`:
    *   **P4_F02_S01_GenerateThinkingDocs_And_Placeholder**: [ ] 4.2.1 遵循 `story_ai_wellness_advisor_core_services.md` 中该练习系列的指引，在 `ai_wellness_advisor/docs/tdd_process_archive/core_services/ExTDD_02_PersonalizedAdvisor/` 中生成相应的实际思考、设计、验证文档。同时，在 `exercise_ai_wellness_advisor/tdd_feature_notes/ExTDD_02_PersonalizedAdvisor/` 目录下创建指向这些实际文档的占位符或引用说明文件。
    *   **P4_F02_S02_CreateTestFile_Red**: [ ] 4.2.2 在 `ai_wellness_advisor/tests/core_services/` 中创建 `test_personalized_advisor.py` (Red)。
    *   **P4_F02_S03_CreateSourceFile_Green**: [ ] 4.2.3 在 `ai_wellness_advisor/src/core_services/` 中创建 `personalized_advisor.py` (Green)。
    *   **P4_F02_S04_GenerateFeatureDoc_And_Placeholder_Refactor**: [ ] 4.2.4 在 `ai_wellness_advisor/docs/tdd_process_archive/core_services/ExTDD_02_PersonalizedAdvisor/` 中生成相应的实际特性文档 (Refactor)。同时，在 `exercise_ai_wellness_advisor/tdd_feature_notes/ExTDD_02_PersonalizedAdvisor/` 目录下的占位符或引用说明文件中更新或添加指向此特性文档的引用。
    *   **LLM协作注意事项 (阶段四 - 针对每个ExTDD练习):**
        *   **TDD流程引导**: 在每个练习（如 `ExTDD_01_WellnessProfileBuilder`）开始时，明确告知LLM当前处于TDD的哪个阶段（Red, Green, Refactor），并给出该阶段的具体任务。
        *   **Red (编写测试)**: 要求LLM根据用户需求编写测试用例。人工审查测试的覆盖率和有效性。LLM应先创建测试文件并写入测试代码，此时运行测试预期失败。测试文件创建于 `ai_wellness_advisor/tests/core_services/`。
        *   **Green (编写代码)**: 要求LLM编写最小化的功能代码以使测试通过。LLM创建或修改源代码文件。运行测试预期通过。源代码文件创建于 `ai_wellness_advisor/src/core_services/`。
        *   **Refactor (重构与文档)**: 指导LLM对代码进行重构（如改进结构、消除重复、提高可读性），并生成必要的文档。此阶段不应破坏测试。实际的TDD过程文档（思考、设计、特性文档）生成在 `ai_wellness_advisor/docs/tdd_process_archive/core_services/{FeatureName}/`，并在 `exercise_ai_wellness_advisor/tdd_feature_notes/{FeatureName}/` 中创建或更新引用。
        *   **Pydantic与LLM工具集应用**: 在开发 `WellnessProfileBuilder` 时，明确指示LLM使用Pydantic模型定义数据结构。在开发 `PersonalizedAdvisor` 时，明确指示LLM如何调用先前建立的LLM API工具集。
        *   **文件路径精确性**: 始终确保LLM在正确的文件路径下操作：实际的TDD思考和特性文档在 `ai_wellness_advisor/docs/tdd_process_archive/core_services/{FeatureName}/`；占位符/引用文档在 `exercise_ai_wellness_advisor/tdd_feature_notes/{FeatureName}/`；代码在 `ai_wellness_advisor/src/core_services/`；测试在 `ai_wellness_advisor/tests/core_services/`。

**阶段五：整合与完善**

*   **P5_S01_ImplementAppLogic**: [ ] 5.1 实现顶层应用逻辑 (如果需要): 在 `ai_wellness_advisor/src/` 下创建主应用入口或服务接口，调用第0、1、2层的功能。
*   **P5_S02_WriteIntegrationTests**: [ ] 5.2 编写集成测试: 在 `ai_wellness_advisor/tests/` 下编写集成测试，验证各层模块协同工作的正确性。
*   **P5_S03_FinalizeProjectDocs**: [ ] 5.3 完善项目文档: 更新 `ai_wellness_advisor/README.md`，添加架构图、部署说明等。
*   **P5_S04_SetupCICD**: [ ] 5.4 配置CI/CD (可选): 为 `ai_wellness_advisor` 项目配置持续集成和部署流程。
    *   **LLM协作注意事项 (阶段五):**
        *   **顶层逻辑设计 (P5_S01)**: 顶层应用逻辑的设计可能需要更多的人工参与和决策，LLM可以辅助实现。
        *   **集成测试编写 (P5_S02)**: 指导LLM编写集成测试时，需明确测试场景和跨模块的交互点。
        *   **文档完善 (P5_S03)**: 要求LLM根据最终实现更新项目 `README.md` 和其他相关文档，人工审查其准确性和完整性。

这个执行计划提供了一个从分散到统一，从基础模块到高层应用的清晰演进路径，全程强调TDD的实践，并为每个步骤提供了唯一的标识符，方便任务跟踪和驱动。