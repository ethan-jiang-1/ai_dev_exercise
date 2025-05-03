# s2: 分析 - MDC 文件规范 (Analysis - MDC File Specification)

本文档概述了 MDC (Markdown Component) 规则文件的技术规范。

## MDC 文件格式规范 (MDC File Format Specification)

### 1. 元数据要求 (YAML Frontmatter)

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

### 2. 内容结构要求 (Content Structure Requirements)

在 YAML 元数据之后，每个 MDC 文件 **必须** 按顺序包含以下四个部分：

1.  `## 核心原则宣言 (Core Principles Declaration)`
    *   解释规则背后的"为什么"（问题、后果、好处、权衡）。
2.  `## 关键实践指南 (Key Practices Guide)`
    *   提供具体的"如何做"指导和示例。
3.  `## 决策指导 (Decision Guidance)`
    *   帮助在与规则相关的复杂选择中导航。
4.  `## 清单 (Checklist)`
    *   提供可操作的验证步骤。

*   **(注意 Note:** 每个部分的详细编写指南位于 `s4_Implementation_Guide.md` 中。)*

## 利用的关键特性 (Key Features Leveraged)

*   **清晰的清单 (Clear Checklists):** 每个规则都为验证和修复提供了可操作的步骤。
*   **结构化内容 (Structured Content):** 四段式结构确保了一致性和清晰度。
*   **元数据驱动 (Metadata Driven):** `globs` 允许基于文件路径/名称进行上下文感知触发。

## 应用场景示例 (Application Scenario Examples)

*   **项目初始化 (Project Initialization):**
    ```yaml
    ---
    description: 初始化新项目的最佳实践
    globs: setup.py,requirements.txt,pyproject.toml
    alwaysApply: false
    ---
    ```
*   **单元测试 (Unit Testing):**
    ```yaml
    ---
    description: 编写有效单元测试的指南
    globs: test_*.py,*_test.py
    alwaysApply: false
    ---
    ```
*   **错误处理 (Error Handling):**
    ```yaml
    ---
    description: 异常处理的最佳实践
    globs: *try*except*.py,*raise*.py
    alwaysApply: false
    ---
    ```

## MDC 核心定位与价值 (Core Positioning & Value)

1.  **主动指导，而非被动检查 (Proactive Guidance, Not Passive Checks):**
    *   在编码过程中 *期间* 就提供指导，而非事后检查。
    *   通过及时的建议，尽早防止不良的编码实践。
    *   减少后期重构相关的成本和精力。

2.  **在坏习惯形成前及时纠正 (Timely Correction Before Bad Habits Form):**
    *   实时识别潜在的问题模式。
    *   提供即时、可操作的改进建议。
    *   在开发团队中培养良好的编码习惯。

3.  **系统化的最佳实践传承 (Systematic Best Practice Inheritance):**
    *   将团队积累的经验和教训固化为可执行的指导。
    *   确保新团队成员能够快速理解和应用既定标准。
    *   保持团队技术实践的一致性。

4.  **降低认知负荷 (Reduced Cognitive Load):**
    *   在需要的时间和地点精确提供相关指导。
    *   消除开发者需要记住所有规则细节的负担。
    *   将规则遵循无缝集成到自然的开发流程中。

