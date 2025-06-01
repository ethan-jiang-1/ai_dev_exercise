# AI个性化健康顾问 (AI Personalized Wellness Advisor)

## 项目概述

本项目旨在构建一个先进的AI个性化健康顾问系统。该系统整合了多项健康评估工具与智能分析能力，致力于为用户提供定制化的健康管理方案和建议，帮助用户更好地理解和改善自身健康状况。

##核心目标

*   **统一平台**：创建一个名为 `ai_wellness_advisor` 的统一代码库，作为所有健康相关模块和服务的中央枢纽。
*   **模块化设计**：采用清晰的模块化架构，将功能分解为可独立开发、测试和维护的组件。
*   **TDD驱动开发**：严格遵循测试驱动开发（TDD）原则，确保代码质量、可靠性和可维护性。
*   **智能化服务**：利用大型语言模型（LLM）和其他AI技术，提供智能化的健康分析和个性化建议。

## 主要功能模块

项目将包含以下核心功能层级和模块：

1.  **基础健康指标计算（第0层模块）**：
    *   身体质量指数（BMI）计算器 (第0层)
    *   每日所需热量（DCNC）计算器 (第0层)
    *   （未来可能集成更多基础健康评估工具）

2.  **核心服务（第1层与第2层模块）**：
    *   **健康档案构建器 (`WellnessProfileBuilder`)** (第1层)：负责收集、处理和管理用户的健康数据，构建全面的个人健康档案。此模块将使用Pydantic进行数据结构定义和验证。
    *   **个性化健康顾问 (`PersonalizedAdvisor`)** (第2层)：基于用户的健康档案和AI分析，提供个性化的健康建议、生活方式指导和潜在风险提示。此模块将利用LLM工具集进行智能交互和内容生成。

3.  **应用逻辑与集成**：
    *   顶层应用逻辑，整合各层模块，提供统一的服务接口或用户交互界面。
    *   全面的集成测试，确保系统各部分协同工作。

## 项目结构

项目 `ai_wellness_advisor` 将遵循标准的Python项目结构。更详细的整体项目目录结构和各目录的用途说明，请参考 <mcfile name="README_folders.md" path="/Users/bowhead/ai_dev_exercise_tdd/README_folders.md"></mcfile>。

*   `ai_wellness_advisor/src/`: 存放所有Python模块的源代码。
    *   `ai_wellness_advisor/src/bmi/`: BMI计算器模块。
    *   `ai_wellness_advisor/src/dcnc/`: DCNC计算器模块。
    *   `ai_wellness_advisor/src/pydantic_models/`: Pydantic数据模型定义。
    *   `ai_wellness_advisor/src/core_services/`: 核心服务模块（如WellnessProfileBuilder, PersonalizedAdvisor）。
*   `ai_wellness_advisor/tests/`: 存放所有Python测试代码，与`src`目录结构对应。
*   `ai_wellness_advisor/docs/`: 存放项目级文档、架构图、用户故事等。
    *   `ai_wellness_advisor/docs/user_stories/`: 各模块的用户故事和需求文档。
    *   `ai_wellness_advisor/docs/archived_tdd_cycles/`: 归档的TDD开发周期记录，包含每个特性开发过程中的思考、设计和实现细节。详细结构参见 <mcfile name="README_folders.md" path="/Users/bowhead/ai_dev_exercise_tdd/README_folders.md"></mcfile> 中的 `ExTDD_XX_FeatureName` 示例。
*   `ai_wellness_advisor/requirements.txt` (或 `pyproject.toml`): 项目依赖管理。
*   `ai_wellness_advisor/README.md`: 本项目的总体说明和使用指南。

## 技术栈（初步）

*   **主要语言**：Python
*   **数据校验**：Pydantic (用于定义和校验如用户健康档案等复杂数据结构)
*   **测试框架**：pytest (或其他Python标准测试框架，用于单元测试、集成测试)
*   **AI/LLM集成**：通过项目根目录下的 `utils_llm/` 目录提供的可复用工具集与大型语言模型进行交互，支持 `PersonalizedAdvisor` 等模块的智能功能。

## TDD实践

本项目严格遵循测试驱动开发（TDD）原则。每个功能的开发都始于编写测试用例，这些测试用例定义了功能的期望行为。随后编写代码以使测试通过，并进行重构以优化代码质量。

*   所有测试代码位于 `ai_wellness_advisor/tests/` 目录下，并与 `src/` 中的模块结构相对应。
*   每个TDD练习周期的详细思考、设计、约束、实现代码和测试代码等过程性文档，将按照规范结构归档于 `ai_wellness_advisor/docs/archived_tdd_cycles/` 目录下。关于此目录结构和TDD练习周期的详细规范，请参考 <mcfile name="README_folders.md" path="/Users/bowhead/ai_dev_exercise_tdd/README_folders.md"></mcfile> 中的 “每个 ExTDD 练习的目录结构” 和 “重要原则再次强调” 部分。

这个项目旨在通过现代软件工程实践（如TDD）和AI技术，打造一个实用且强大的个性化健康管理工具。