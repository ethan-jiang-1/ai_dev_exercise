# s5: 执行与验证 - 迁移流程 (Execution & Validation - Migration Procedure)

本文档详细说明了将单个规则从旧格式迁移到新 MDC 格式的分步流程、未来更新过程以及最终验证清单。

## 迁移背景与目标 (Migration Context & Objectives)

本迁移计划的核心目标是将旧的规则文件从 `rule_migration/rules_old/` 目录迁移到 `rule_migration/rules_mdc/` 目录，同时转换格式并利用新的 MDC 特性。

### 迁移源与目标 (Migration Source & Destination)
- **源目录 (Source)**: `rule_migration/rules_old/` - 包含传统 `.md` 格式的规则文件
- **目标目录 (Destination)**: `rule_migration/rules_mdc/` - 将存放新的 `.mdc` 格式规则文件

### MDC 格式特性 (MDC Format Features)
新的 MDC 格式具有以下关键特性，这些特性必须在迁移过程中正确配置：

1. **YAML 元数据 (YAML Frontmatter)**:
   - `description`: 规则的简洁描述，将显示在编辑器界面中
   - `globs`: 指定规则应用的文件类型/路径模式
   - `alwaysApply`: 设置为 `false`，确保规则仅在相关上下文中触发
   - `trigger`: （可选）定义何时激活规则的具体条件

2. **结构化内容 (Structured Content)**:
   标准化的四部分结构确保规则的一致性和完整性，同时利用 MDC 的实时指导特性。

3. **交互式指导 (Interactive Guidance)**:
   新格式旨在提供主动指导而非被动检查，遵循 `s1_Requirements.md` 中定义的核心价值。

## 关键参考文档 (Key Reference Documents)

在执行迁移步骤之前，请确保您已熟悉以下关键文档：

* **`s2_Analysis.md`**: 定义了 MDC 规则的基本结构和 YAML 元数据要求。
* **`s3_Planning.md`**: 包含内容重组维度和各规则类型的定位。
* **`s4_MDC_Implementation_Guide.md`**: **最重要的内容指南** - 详细说明了如何编写每个 MDC 部分的具体内容，包括格式要求、提供的实例和模板。在编写和格式化规则内容时，请始终参考此文档。

## 内容重组与迁移流程 (Content Reorganization & Migration Procedure)

对每个目标 MDC 规则，执行以下步骤：

1. **内容分析与规划 (Content Analysis & Planning):**
   * 根据 `s3_Planning.md` 中的维度定义，确定目标 MDC 规则的精确范围和内容焦点
   * 从所有相关的旧规则中识别和提取相关内容
   * 使用 `s2_Analysis.md` 中的分析框架，规划内容如何映射到四段式结构

2. **内容准备与重组 (Content Preparation & Reorganization):**
   * 创建一个临时的 `.txt` 文件（例如 `rule_migration/target_rule_name.txt`）
   * 为该规则设计适当的 YAML 元数据（description, globs, alwaysApply: false）
   * 按照四段式结构组织提取的内容，进行必要的重写和增强
   * 参考 `s4_MDC_Implementation_Guide.md` 中该类型规则的特定实施指南

3. **内容编写与增强 (Content Writing & Enhancement):**
   * 按照 MDC 格式编写四个主要部分：
     * `## 核心原则宣言 (Core Principles Declaration)` - 根据规则类型突出相关问题、后果、好处和权衡
     * `## 关键实践指南 (Key Practices Guide)` - 提供针对该维度的具体实践和代码示例
     * `## 决策指导 (Decision Guidance)` - 创建适合该规则类型的决策树或对比表
     * `## 清单 (Checklist)` - 设计针对性的验证步骤和修复建议
   * 确保使用正确的 Emoji 标记和格式化

4. **文件完成与部署 (File Completion & Deployment):**
   * 审查临时 `.txt` 文件内容，确保其符合 MDC 规范并体现了正确的维度焦点
   * 将临时文件重命名为最终的 `.mdc` 文件，并移至 `rules_mdc/` 目录
   * 更新迁移清单，标记该规则为已完成

## 未来规则更新流程 (Future Rule Update Procedure)

为了安全地更新 `rules_mdc/` 中 *现有* 的 `.mdc` 规则文件而不与文件监控冲突：

1.  **备份与转换 (Backup & Convert):** 将目标 `.mdc` 文件复制为一个 `.txt` 文件 (`cp rules_mdc/rule_name.mdc rule_migration/rule_name.txt`)。
2.  **编辑内容 (Edit Content):** 在 `.txt` 文件中进行所有必要的修改。
3.  **替换文件 (Replace File):**
    *   删除原始的 `.mdc` 文件 (`rm rules_mdc/rule_name.mdc`)。
    *   将编辑后的 `.txt` 文件重命名回 `.mdc` (`mv rule_migration/rule_name.txt rules_mdc/rule_name.mdc`)。

## 最终验证清单 (Final Validation Checklist - Per Rule)

在完成每个 MDC 规则后，验证以下各项：

1.  **元数据 (Metadata):**
    *   [ ] YAML 元数据是否存在于文件顶部？
    *   [ ] YAML 格式是否有效？
    *   [ ] 是否包含 `description`, `globs`, 和 `alwaysApply: false`？
    *   [ ] `description` 和 `globs` 的值是否适合该规则？
2.  **文档结构 (Document Structure):**
    *   [ ] 文件是否按顺序包含了所有四个必需的 H2 部分？(`核心原则 Core Principles`, `关键实践 Key Practices`, `决策指导 Decision Guidance`, `清单 Checklist`)
    *   [ ] Markdown 格式是否正确（无渲染错误）？
3.  **内容质量 (Content Quality - 参考 `s4_MDC_Implementation_Guide.md`):**
    *   [ ] **核心原则 (Core Principles):** 是否清晰地陈述了问题、后果、好处和权衡？
    *   [ ] **关键实践 (Key Practices):** 是否提供了带有对比代码示例 (✅❌) 的清晰指导？
    *   [ ] **决策指导 (Decision Guidance):** 是否提供了清晰的决策标准或流程 (🌲📊)？
    *   [ ] **清单 (Checklist):** 项目是否可操作，并带有清晰的判断标准和修复建议？\n\
    *   [ ] **格式与 Emoji (Formatting & Emojis):** 是否遵循了 `s4` 中定义的 Markdown 格式和 Emoji 约定 (例如 ✅❌🌲📊⚡️💥💎⚖️)？\n\
4.  **维度一致性 (Dimensional Consistency):**\n\
    *   [ ] 内容是否符合 `s3_Planning.md` 中定义的该规则类型的定位和重组维度？\n\
    *   [ ] 是否成功从多个来源整合了相关内容？\n\
    *   [ ] 是否避免了与其他规则的内容重叠？\n\
5.  **可操作性 (Actionability):**
    *   [ ] **代码示例 (Code Examples):** 语法是否正确且具有说明性？
    *   [ ] **清单项 (Checklist Items):** 判断标准是否可衡量？修复建议是否实用？

## 规则维护原则 (Rule Maintenance Principles)

*   **持续优化 (Continuous Optimization):** 根据反馈和不断发展的最佳实践定期更新规则。
*   **价值驱动 (Value-Driven):** 确保每条规则都能带来明确的、实际的价值；移除过时的规则。
*   **实用性优先 (Practicality First):** 关注真实世界的场景、具体的示例和可操作的解决方案。
*   **维度一致性 (Dimensional Consistency):** 保持每个规则在其定义的维度内，避免内容偏离其核心焦点。

## 迁移计划步骤 (Migration Plan Steps)

本节列出了按照内容维度和规则类型（遵循 `s3_Planning.md` 定义）生成每个目标 `.mdc` 文件的步骤。每个步骤都需要从 `rule_migration/rules_old/` 目录中的一个或多个旧规则中提取相关内容，并按照 `s4_MDC_Implementation_Guide.md` 的指导进行重组和编写。

### Step 1: Produce principles.mdc
- **目标**: 生成 `principles.mdc` - 高层次的设计和开发原则。
- **主要来源**: 主要从 `cursorrules_principles.md` 提取，可能涉及其他文件的原则性内容。
- **重组指导**: 遵循 `s3_Planning.md` 中关于 `principles.mdc` 的重组方式（提取核心思想，添加示例，扩展为完整指南）。
- **状态**: [ ] 未开始 / [ ] 进行中 / [ ] 已完成

### Step 2: Produce structure.mdc
- **目标**: 生成 `structure.mdc` - 项目文件和目录组织的最佳实践。
- **主要来源**: 主要从 `cursorrules_principles.md` 的项目结构部分和 `cursorrules_init_guide.md` 提取。
- **重组指导**: 遵循 `s3_Planning.md` 中关于 `structure.mdc` 的重组方式（提升为独立规则，添加不同类型项目建议，包含具体实践）。
- **状态**: [ ] 未开始 / [ ] 进行中 / [ ] 已完成

### Step 3: Produce coding_style.mdc
- **目标**: 生成 `coding_style.mdc` - 代码格式和风格约定。
- **主要来源**: 从 `.cursorrules`, `cursorrules_iteration_guide.md` 及其他文件中分散的编码风格/格式规范提取。
- **重组指导**: 遵循 `s3_Planning.md` 中关于 `coding_style.mdc` 的重组方式（聚焦纯代码风格，提供清晰规范示例，添加工具指南）。
- **状态**: [ ] 未开始 / [ ] 进行中 / [ ] 已完成

### Step 4: Produce imports.mdc
- **目标**: 生成 `imports.mdc` - 模块导入和依赖管理的最佳实践。
- **主要来源**: 从 `.cursorrules`, `cursorrules_iteration_guide.md` 及其他文件中分散的导入和依赖管理相关内容提取。
- **重组指导**: 遵循 `s3_Planning.md` 中关于 `imports.mdc` 的重组方式（整合导入规范，提供明确指导，添加依赖管理实践）。
- **状态**: [ ] 未开始 / [ ] 进行中 / [ ] 已完成

### Step 5: Produce error_handling.mdc
- **目标**: 生成 `error_handling.mdc` - 异常处理和错误管理的综合指南。
- **主要来源**: 主要从 `cursorrules_principles.md` 的错误处理部分提取，并整合其他文件中相关的错误处理实践。
- **重组指导**: 遵循 `s3_Planning.md` 中关于 `error_handling.mdc` 的重组方式（建立完整框架，按类型/策略分类，提供示例/模式）。
- **状态**: [ ] 未开始 / [ ] 进行中 / [ ] 已完成

### Step 6: Produce unit_testing.mdc
- **目标**: 生成 `unit_testing.mdc` - 测试编写和组织的最佳实践。
- **主要来源**: 从 `cursorrules_iteration_guide.md` 及其他文件中分散的测试相关内容提取。
- **重组指导**: 遵循 `s3_Planning.md` 中关于 `unit_testing.mdc` 的重组方式（整合测试指南，提供编写模式，包含组织/执行实践）。
- **状态**: [ ] 未开始 / [ ] 进行中 / [ ] 已完成

### Step 7: Produce api_documentation.mdc
- **目标**: 生成 `api_documentation.mdc` - API接口文档的编写规范。
- **主要来源**: 主要从 `cursorrules_doc_guide.md` 的 API 文档部分提取。
- **重组指导**: 遵循 `s3_Planning.md` 中关于 `api_documentation.mdc` 的重组方式（专注函数/类/模块文档标准，提供示例/模板，包含生成指南）。
- **状态**: [ ] 未开始 / [ ] 进行中 / [ ] 已完成

### Step 8: Produce technical_docs.mdc
- **目标**: 生成 `technical_docs.mdc` - 系统和架构级文档的编写指南。
- **主要来源**: 主要从 `cursorrules_doc_guide.md` 的技术文档部分和 `README.md` 提取。
- **重组指导**: 遵循 `s3_Planning.md` 中关于 `technical_docs.mdc` 的重组方式（整合高级文档指南，按文档类型重组，添加模板/示例）。
- **状态**: [ ] 未开始 / [ ] 进行中 / [ ] 已完成


