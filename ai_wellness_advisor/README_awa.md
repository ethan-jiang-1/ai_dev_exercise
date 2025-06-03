# AI 个性化健康顾问 (AI Personalized Wellness Advisor) - 应用入口

欢迎来到 AI 个性化健康顾问应用！

本应用旨在通过整合先进的健康评估工具和智能分析能力，为您提供定制化的健康管理方案和建议。

## 主要功能

*   **基础健康指标计算**: 包括 BMI、每日所需热量等。
*   **健康档案构建**: 全面管理您的健康数据。
*   **个性化健康建议**: 基于您的健康档案和 AI 分析，提供定制化指导。

## 快速开始

本应用目前主要作为TDD练习的框架和示例代码库。以下是如何进行不同程度的“从头开始”练习：

### 1. 完全重置整个 `ai_wellness_advisor` 应用

如果您希望将整个 `ai_wellness_advisor` 应用恢复到初始状态，以便从零开始所有模块的TDD练习，您可以：

*   删除以下目录及其所有内容：
    *   `ai_wellness_advisor/dev_cycles/`
    *   `ai_wellness_advisor/src/`
    *   `ai_wellness_advisor/tests/`

完成上述操作后，您可以根据项目根目录的 `README_prj.md` 和相关的TDD练习指导（如 `exercise_tdd_xxx` 目录下的文档）重新开始构建整个应用。

### 2. 重置特定的功能模块

如果您只想针对 `ai_wellness_advisor` 中的某一个或几个特定功能模块（例如 `bmi` 或 `dcnc`）从头开始TDD练习，您可以：

*   假设您要重置名为 `your_module_name` 的模块，请删除以下特定于该模块的目录：
    *   `ai_wellness_advisor/dev_cycles/your_module_name/`
    *   `ai_wellness_advisor/src/your_module_name/`
    *   `ai_wellness_advisor/tests/your_module_name/`

这样，您可以保留其他模块的进度，仅针对选定的模块重新进行TDD开发周期。

### 3. 应用的运行与交互

由于本应用的核心是作为TDD练习的载体，其“运行”主要体现在通过 `pytest` 等工具执行单元测试和集成测试，以验证各个模块功能的正确性。具体的测试执行命令和方法，请参考各模块TDD练习文档中的指导。

目前，本应用可能不包含一个统一的可执行入口点或用户界面，其价值在于提供一个结构化的环境来实践和学习测试驱动开发。

## 详细信息

*   关于本项目的**整体目标、架构设计、技术栈和详细的TDD开发实践规范**，请参考项目根目录下的 [README_prj.md](../../README_prj.md)。
*   关于本项目的**完整目录结构和文件组织规范**，请参考项目根目录下的 [README_folders.md](../../README_folders.md)。
*   关于本项目中**每个特性（Feature）的TDD开发周期文档结构和命名规范**，请参考项目根目录下的 [README_folder_feature.md](../../README_folder_feature.md)。

我们致力于通过现代软件工程实践（如TDD）和AI技术，打造一个实用且强大的个性化健康管理工具。