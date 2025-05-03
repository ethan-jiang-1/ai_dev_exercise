# s2: 分析 - MDC 文件规范与迁移策略选择 (Analysis - MDC Specification & Migration Strategy Selection)

本文档首先定义了新的 MDC (Markdown Component) 规则文件的技术规范，然后记录了将旧规则迁移到新格式的策略探索过程，并最终确定了采用"内容重组"的核心迁移策略。

## 1. MDC 文件格式规范 (MDC File Format Specification)

(此部分定义了新格式的技术基础)

### 1.1. 元数据要求 (YAML Frontmatter)

*   **位置 (Location):** 必须位于文件的绝对顶部。
*   **格式 (Format):** 必须使用严格的 YAML 语法，并由 `---` 分隔符包裹。
*   **支持的字段 (Supported Fields):**
    *   `description`: (字符串 String) 对规则目的和价值的简洁说明。不要使用引号包裹。
    *   `globs`: (字符串 String) 逗号分隔的 glob 模式，用于指定哪些文件触发此规则。不要使用引号。
    *   `alwaysApply`: (布尔值 Boolean) 设置为 `false`。表示该规则提供指导而非强制执行变更。

*   **标准格式示例 (Standard Format Example):**

    ```yaml
    ---
    description: 对规则的描述，突出其核心思想和价值
    globs: *.py,specific_module/*.py
    alwaysApply: false
    ---
    ```

### 1.2. 内容结构要求 (Content Structure Requirements)

在 YAML 元数据之后，每个 MDC 文件 **必须** 按顺序包含以下四个部分：

1.  `## 核心原则宣言 (Core Principles Declaration)`
    *   解释规则背后的"为什么"（问题、后果、好处、权衡）。
2.  `## 关键实践指南 (Key Practices Guide)`
    *   提供具体的"如何做"指导和示例。
3.  `## 决策指导 (Decision Guidance)`
    *   帮助在与规则相关的复杂选择中导航。
4.  `## 清单 (Checklist)`
    *   提供可操作的验证步骤。

## 2. 迁移策略探索与决策 (Migration Strategy Exploration & Decision)

在明确了目标 MDC 格式后，我们需要确定如何有效地将 `rule_migration/rules_old/` 目录下的旧规则内容迁移并适配到新的四段式结构中。我们探讨了以下两种主要方法：

### 2.1. 方法一 (初步构思): 直接内容映射 (Direct Content Mapping)

最初，我们考虑了一种相对直接的方法：尝试将每个旧规则文件或其特定段落直接映射到新 MDC 文件的对应部分。

*   **思路:** 为每个旧规则创建一个映射表，追踪原始内容如何放入新的四个部分，并标记需要补充的信息。
*   **具体体现 (分析过程中的模板):**

    ```markdown
    # (分析模板) 规则内容映射分析表

    ## 规则基本信息
    - **旧文件名称**: `原始文件名.md`
    - **新文件名称**: `目标文件名.mdc`
    - **规则主题**: [主题描述]
    - **适用范围**: [适用的文件类型/场景]

    ## 内容映射

    ### 1. 核心原则宣言
    | 旧内容 (位置/段落) | 映射方式 | 需要补充的内容 |
    |-------------------|----------|---------------|
    | ...               | ...      | ...           |
    ### 2. 关键实践指南
    | 旧内容 (位置/段落) | 映射方式 | 需要补充的内容 |
    |-------------------|----------|---------------|
    | ...               | ...      | ...           |
    ### 3. 决策指导
    | 旧内容 (位置/段落) | 映射方式 | 需要补充的内容 |
    |-------------------|----------|---------------|
    | ...               | ...      | ...           |
    ### 4. 清单
    | 旧内容 (位置/段落) | 映射方式 | 需要补充的内容 |
    |-------------------|----------|---------------|
    | ...               | ...      | ...           |

    ## 元数据设计
    - **description**: [规则描述]
    - **globs**: [适用的文件模式]
    - **alwaysApply**: false
    ```

*   **局限性评估:** 这种方法对于那些内容单一、结构清晰的旧规则可能有效。但我们发现旧规则内容往往分散在多个文件中，且单个文件可能涉及多个主题。直接映射难以有效整合这些分散的内容，也难以确保最终的 MDC 文件具有清晰的主题聚焦和一致性，无法完全发挥新格式的优势。

### 2.2. 方法二 (最终选择): 主题式内容重组 (Thematic Content Reorganization)

认识到直接映射的局限性后，我们转向了一种更根本性的方法：**内容重组**。

*   **思路:** 不再局限于单个旧规则文件，而是根据新 MDC 规则的目标主题（如：编码原则、项目结构、错误处理等），跨越所有相关的旧规则文件，主动地 **提取、整合、重写和增强** 内容，使其符合新的四段式结构和主题要求。
*   **优点:** 这种方法能够更好地处理内容分散和主题交叉的问题，确保每个新的 MDC 文件都具有清晰的焦点、完整的结构和高价值的内容，从而最大化迁移的收益。
*   **核心策略:** 为了指导这种重组过程，我们制定了以下内容重组策略原则：

    1.  **主题聚焦与拆分 (Topic Focus and Splitting):**
        *   如果旧规则覆盖多个不相关的主题，考虑拆分为多个 MDC 规则。
        *   确保每个 MDC 规则都有清晰的主题焦点和适用范围。
    2.  **内容整合与关联 (Content Integration and Correlation):**
        *   如果多个旧规则包含相关主题，考虑整合到一个 MDC 规则中。
        *   确保整合后的内容保持一致性和连贯性。
    3.  **内容扩展与增强 (Content Expansion and Enhancement):**
        *   基于团队经验和最佳实践，补充和扩展原有内容。
        *   添加具体的示例、决策指导和清单项，以满足 MDC 四段结构的要求。

### 2.3. 决策结论 (Decision Conclusion)

经过分析和比较，我们决定 **采用"主题式内容重组"作为本次规则迁移的核心策略**。这意味着后续的迁移工作（如 `s3_Planning.md` 中的详细规划）将基于这一策略进行，指导我们如何从 `rules_old` 中提取内容并构建新的 `rules_mdc` 文件。

## 3. MDC 关键特性与价值 (Key Features & Value of MDC)

采用内容重组策略迁移到 MDC 格式后，我们将能充分利用以下关键特性并实现其核心价值：

*   **清晰的清单 (Clear Checklists):** 每个规则都为验证和修复提供了可操作的步骤。
*   **结构化内容 (Structured Content):** 四段式结构确保了一致性和清晰度。
*   **元数据驱动 (Metadata Driven):** `globs` 允许基于文件路径/名称进行上下文感知触发。
*   **(核心价值重申)**:
    1.  **主动指导，而非被动检查 (Proactive Guidance, Not Passive Checks)**
    2.  **在坏习惯形成前及时纠正 (Timely Correction Before Bad Habits Form)**
    3.  **系统化的最佳实践传承 (Systematic Best Practice Inheritance)**
    4.  **降低认知负荷 (Reduced Cognitive Load)**

## 4. 应用场景示例 (Application Scenario Examples)

以下是一些通过内容重组后可能产生的 MDC 规则及其元数据示例：

*   **项目初始化 (Project Initialization):**
    ```yaml
    ---
    description: 初始化新项目的最佳实践 (整合自 init_guide 等)
    globs: setup.py,requirements.txt,pyproject.toml
    alwaysApply: false
    ---
    ```
*   **单元测试 (Unit Testing):**
    ```yaml
    ---
    description: 编写有效单元测试的指南 (整合自 iteration_guide 等)
    globs: test_*.py,*_test.py
    alwaysApply: false
    ---
    ```
*   **错误处理 (Error Handling):**
    ```yaml
    ---
    description: 异常处理的最佳实践 (整合自 principles 及其他相关内容)
    globs: *try*except*.py,*raise*.py
    alwaysApply: false
    ---
    ```

