# `practice_*.md` 文件调整清单

本文档总结了在与AI助手对话过程中，对 `practice_tdd_bmi_calculator.md` 文件所做的关键调整。这些调整可以作为更新其他 `practice_*.md` 文件的参考清单。

## 调整项列表：

1.  **[] 统一TDD周期产出物归档路径**：
    *   确保 “TDD周期产出物归档说明” 中，路径指向 `{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/`。
    *   示例：`../ai_wellness_advisor/dev_cycles/bmi/ExTDD_01_BMICalculation/`。

2.  **[] 统一最终用户故事文档路径**：
    *   确保 “本练习中定义的各特性对应的最终用户故事文档 (`_user_story_{feature_name}.md`) 位于 `{app_name}` 项目的相应特性开发周期目录中” 的描述准确。
    *   示例路径：`../{app_name}/dev_cycles/bmi/ExTDD_01_BMICalculation/_user_story_bmi_calculate.md`。

3.  **[] 更新TDD周期产出物目录结构规范内部路径**：
    *   确保 “TDD周期产出物目录结构规范 (位于 `{app_name}` 项目内)” 部分，描述的目录结构为 `{app_name}/dev_cycles/{module_name}/ExTDD_NN_{FeatureName}/`。
    *   明确指出当前练习对应的 `{app_name}` 和 `{module_name}`。
        *   例如，在 `practice_tdd_bmi_calculator.md` 中，明确说明：在本练习中，`{app_name}` 为 `ai_wellness_advisor`，`{module_name}` 为 `bmi`。

4.  **[] 移除 `doc_{feature_name}.md` 的描述**：
    *   从“文件命名”规范中移除了关于 `doc_{feature_name}.md` 的描述，因为实际目录结构中并未使用此文件。

5.  **[] 规范化文件引用格式**：
    *   将文档中对其他 `.md` 文件（如 `README_folder_feature.md`, `README_folders.md`）的 `<mcfile>` 格式引用，修改为标准的 Markdown 文件链接格式。
    *   例如：`[ExTDD 特性研发目录结构：核心原则与详解](../README_folder_feature.md)`。

6.  **[] 添加对 `README_folder_feature.md` 的引用**：
    *   在“目录结构核心原则参考”部分，确保有对 `README_folder_feature.md` 的 Markdown 链接引用，以强调目录命名约束的重要性。

7.  **[] 统一文件引用的相对路径**：
    *   检查并确保所有对项目内其他 `README_*.md` 文件的引用路径是正确的相对路径。
    *   例如，从 `exercise_tdd_bmi/` 目录下的文件引用根目录的 `README_folder_feature.md`，路径应为 `../README_folder_feature.md`。

8.  **[] 明确各特性实现中的 `module_name` 和 `feature_name`**：
    *   在每个特性实现章节（例如 “ExTDD_01_BMICalculation: 实现BMI值的计算”）的开头，明确列出该特性对应的 `module_name` 和 `feature_name`。
    *   例如：
        ```
        module_name: bmi
        feature_name: bmi_calculate
        ```

## 注意事项：

*   在调整其他 `practice_*.md` 文件时，请根据具体练习的 `{module_name}` 和 `{feature_name}` 替换上述示例中的值。
*   确保所有路径引用（相对路径）根据当前 `practice_*.md` 文件的实际位置进行正确调整。