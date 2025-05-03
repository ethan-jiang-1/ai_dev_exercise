# s5: 执行与验证 - 迁移流程 (Execution & Validation - Migration Procedure)

本文档详细说明了将单个规则从旧格式迁移到新 MDC 格式的分步流程、未来更新过程以及最终验证清单。

## 单个规则迁移流程 (Individual Rule Migration Procedure)

对 `s3_Planning.md` 中列出的 **每个** 规则执行以下步骤：

1.  **备份与转换 (Backup & Convert - Safety Step):**
    *   将 `rules_old/` 中的原始 `.md` 规则文件复制为一个临时的 `.txt` 文件（例如 `cp rules_old/rule_name.md rule_migration/rule_name.txt`）。这是为了避免过早触发文件监视器 (file watchers)。
2.  **检查与更新元数据 (Check & Update Metadata):**
    *   编辑该 `.txt` 文件。
    *   在文件最顶部添加或更正 YAML 元数据 (frontmatter)，确保其符合 `s2_Analysis.md` 中的规范（正确的 `description`, `globs`, `alwaysApply: false`）。
3.  **更新内容与结构 (Update Content & Structure):**
    *   根据 `s2_Analysis.md` 中指定的四段式结构 (`## 核心原则宣言 Core Principles Declaration`, `## 关键实践指南 Key Practices Guide`, `## 决策指导 Decision Guidance`, `## 清单 Checklist`)，重构 `.txt` 文件的 *全部* 内容。
    *   遵循 `s4_Implementation_Guide.md` 中的指南重写和增强内容。
4.  **替换原始文件 (Replace Original File):**
    *   从 `rules_old/` (或适用的目标 `rules_mdc/`) 中删除 *原始* 的 `.md` 文件 (`rm rules_old/rule_name.md`)。
    *   将更新后的 `.txt` 文件重命名为 `rules_mdc/` 目录中的最终 `.mdc` 文件 (`mv rule_migration/rule_name.txt rules_mdc/rule_name.mdc`)。

## 未来规则更新流程 (Future Rule Update Procedure)

为了安全地更新 `rules_mdc/` 中 *现有* 的 `.mdc` 规则文件而不与文件监控冲突：

1.  **备份与转换 (Backup & Convert):** 将目标 `.mdc` 文件复制为一个 `.txt` 文件 (`cp rules_mdc/rule_name.mdc rule_migration/rule_name.txt`)。
2.  **编辑内容 (Edit Content):** 在 `.txt` 文件中进行所有必要的修改。
3.  **替换文件 (Replace File):**
    *   删除原始的 `.mdc` 文件 (`rm rules_mdc/rule_name.mdc`)。
    *   将编辑后的 `.txt` 文件重命名回 `.mdc` (`mv rule_migration/rule_name.txt rules_mdc/rule_name.mdc`)。

## 最终验证清单 (Final Validation Checklist - Per Rule)

在使用上述流程将每个规则迁移到 `.mdc` 后，验证以下各项：

1.  **元数据 (Metadata):**
    *   [ ] YAML 元数据是否存在于文件顶部？
    *   [ ] YAML 格式是否有效？
    *   [ ] 是否包含 `description`, `globs`, 和 `alwaysApply: false`？
    *   [ ] `description` 和 `globs` 的值是否适合该规则？
2.  **文档结构 (Document Structure):**
    *   [ ] 文件是否按顺序包含了所有四个必需的 H2 部分？(`核心原则 Core Principles`, `关键实践 Key Practices`, `决策指导 Decision Guidance`, `清单 Checklist`)
    *   [ ] Markdown 格式是否正确（无渲染错误）？
3.  **内容质量 (Content Quality - 参考 `s4_Implementation_Guide.md`):**
    *   [ ] **核心原则 (Core Principles):** 是否清晰地陈述了问题、后果、好处和权衡？
    *   [ ] **关键实践 (Key Practices):** 是否提供了带有对比代码示例 (✅❌) 的清晰指导？
    *   [ ] **决策指导 (Decision Guidance):** 是否提供了清晰的决策标准或流程 (🌲📊)？
    *   [ ] **清单 (Checklist):** 项目是否可操作，并带有清晰的判断标准和修复建议？
4.  **可操作性 (Actionability):**
    *   [ ] **代码示例 (Code Examples):** 语法是否正确且具有说明性？
    *   [ ] **清单项 (Checklist Items):** 判断标准是否可衡量？修复建议是否实用？

## 规则维护原则 (Rule Maintenance Principles)

*   **持续优化 (Continuous Optimization):** 根据反馈和不断发展的最佳实践定期更新规则。
*   **价值驱动 (Value-Driven):** 确保每条规则都能带来明确的、实际的价值；移除过时的规则。
*   **实用性优先 (Practicality First):** 关注真实世界的场景、具体的示例和可操作的解决方案。

*来源: 基于 mdc_execution.md 和 mdc_overview.md (Source: Derived from mdc_execution.md and mdc_overview.md)* 