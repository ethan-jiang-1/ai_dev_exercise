# s3: 计划 - MDC 迁移策略 (Planning - MDC Migration Strategy)

本文档概述了将现有规则迁移到 MDC 格式的分阶段方法。

## 迁移阶段 (Migration Phases)

迁移计划按以下阶段进行，针对特定类别的规则：

### 阶段 1: 核心开发原则 (Core Development Principles)
*   **目标 (Goal):** 迁移关于开发理念和结构的基础规则。
*   **规则 (Rules):**
    *   `principles.md` -> `principles.mdc`
    *   `structure.md` -> `structure.mdc`

### 阶段 2: 编码标准 (Coding Standards)
*   **目标 (Goal):** 迁移与代码风格、导入和通用编码实践相关的规则。
*   **规则 (Rules):**
    *   `coding_style.md` -> `coding_style.mdc`
    *   `imports.md` -> `imports.mdc`

### 阶段 3: 质量保证 (Quality Assurance)
*   **目标 (Goal):** 迁移关于测试和错误处理的规则。
*   **规则 (Rules):**
    *   `unit_testing.md` -> `unit_testing.mdc`
    *   `error_handling.md` -> `error_handling.mdc`

### 阶段 4: 文档标准 (Documentation Standards)
*   **目标 (Goal):** 迁移与 API 和技术文档相关的规则。
*   **规则 (Rules):**
    *   `api_documentation.md` -> `api_documentation.mdc`
    *   `technical_docs.md` -> `technical_docs.mdc`

*   **(注意 Note:** 迁移 *每个* 规则的详细分步流程在 `s5_Execution_Validation.md` 中。)*

*来源: 基于 mdc_execution.md (Source: Derived from mdc_execution.md)* 