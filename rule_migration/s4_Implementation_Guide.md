# s4: 实施指南 - 编写 MDC 规则内容 (Implementation Guide - Writing MDC Rule Content)

本指南详细说明了如何为 MDC 规则文件中的四个必需部分编写有效内容，遵循 `s2_Analysis.md` 中定义的结构。

## MDC 内容结构指南 (MDC Content Structure Guide)

每个 MDC 文件必须包含以下四个 H2 部分：

### 1. `## 核心原则宣言 (Core Principles Declaration)`

*   **目的 (Purpose):** 清晰阐述规则的基本原理。
*   **内容 (Content):**
    *   **⚡️ 核心问题 (Core Problem):** 简洁地说明此规则要解决的问题。
    *   **💥 忽略的后果 (Consequences of Ignoring):** 列出不遵守规则的具体负面后果。
    *   **💎 遵守的好处 (Benefits of Following):** 列出遵守规则的实际积极成果。
    *   **⚖️ 必要的权衡 (Necessary Trade-offs):** 承认所涉及的任何妥协或平衡（例如，性能 vs. 可读性）。

### 2. `## 关键实践指南 (Key Practices Guide)`

*   **目的 (Purpose):** 提供关于 *如何* 实施规则的可操作、实用的指导。
*   **内容 (Content) (针对每个不同的实践):**
    *   使用 H4 标题标识每个实践 (`#### 实践名称 Practice Name`)。
    *   **为何需要这样做 (Why this is necessary):** 解释实践背后的基本原理。
    *   **❌ 常见错误 / 反模式 (Common Mistakes / Anti-patterns):** 展示清晰的 *错误* 代码示例。
        ```python
        # 错误示例代码 (Bad example code)
        ```
    *   **✅ 正确方法 (Correct Approach):** 展示清晰的 *正确* 代码示例。
        ```python
        # 正确示例代码 (Good example code)
        ```
    *   **(可选 Optional) 🔄 重构路径 (Refactoring Path):** 提供将坏代码转换为好代码的分步说明。
    *   **(可选 Optional) 陷阱/缺陷 (Traps/Pitfalls):** 提及常见的误解或边缘情况。

### 3. `## 决策指导 (Decision Guidance)`

*   **目的 (Purpose):** 帮助开发者在规则涉及选择或复杂性时进行导航。
*   **内容 (Content) (使用相关格式):**
    *   **🌲 决策树 (Decision Tree):** 使用嵌套列表或图表，根据特定标准指导选择。
        ```
        1. 条件 A? (Condition A?)
           - 是 (Yes) -> 方法 X (Approach X)
           - 否 (No) -> 检查条件 B (Check Condition B)
        2. 条件 B? (Condition B?)
           ...
        ```
    *   **📊 对比表 (Comparison Table):** 使用 Markdown 表格，根据上下文、优缺点等比较不同的方法。
        ```markdown
        | 方法 (Approach) | 使用场景 (When to Use) | 优点 (Pros) | 缺点 (Cons) | 注意事项 (Notes) |
        |---------------|--------------------|-----------|-----------|--------------|
        | 选项 1 (Option 1) | 场景 A (Scenario A)  | 性能好 (Good Perf) | 复杂 (Complex) | 需谨慎 (Be careful) |
        | 选项 2 (Option 2) | 场景 B (Scenario B)  | 简单 (Simple) | 性能稍差 (Less Perf) | 更容易 (Easier) |
        ```
    *   **明确的标准 (Clear Criteria):** 提供明确的判断标准。

### 4. `## 清单 (Checklist)`

*   **目的 (Purpose):** 提供具体、可验证的步骤，以确保规则被正确应用。
*   **内容 (Content):**
    *   逻辑地组织清单项（例如，按开发阶段：编码阶段 Coding Phase, 重构阶段 Refactoring Phase, 代码审查阶段 Code Review Phase）。
    *   使用 H4 标题标识阶段 (`#### 编码阶段 Coding Phase`)。
    *   每个项目应为一个复选框 (`- [ ] 清单项名称 Check Item Name`)。
    *   为每个项目指定：
        *   `判断标准 (Judgment Standard):` 如何确定项目是否通过/失败。
        *   `快速修复 (Quick Fix):` 如果失败，如何纠正问题。
    *   在适用时指出自动化检查的可能性。

## 各类规则实施指南 (Implementation Guidelines for Different Rule Types)

根据 `s3_Planning.md` 中定义的不同规则类型，每类规则在实施时需特别注意以下方面：

### 原则类规则 (Principles Rules)

*   **核心原则宣言:** 重点阐述广泛适用的设计思想和基本理念。
*   **关键实践指南:** 提供多个领域的实践示例，强调原则的通用性。
*   **决策指导:** 包含高层次决策框架，帮助在不同场景中应用原则。
*   **清单:** 侧重于原则实施的验证，而非具体技术实现。

### 结构类规则 (Structure Rules)

*   **核心原则宣言:** 聚焦于项目组织和结构带来的长期影响。
*   **关键实践指南:** 提供不同类型项目的目录结构示例。
*   **决策指导:** 包含项目规模与结构复杂度的决策矩阵。
*   **清单:** 包括项目创建和重构两个阶段的检查项。

### 编码规范类规则 (Coding Style Rules)

*   **核心原则宣言:** 强调一致性和可读性的价值。
*   **关键实践指南:** 提供具体的格式规范和多种典型场景的示例。
*   **决策指导:** 包含风格选择的决策树和例外情况处理指南。
*   **清单:** 具体到代码行级别的检查，适合自动化验证。

### 模块导入类规则 (Import Rules)

*   **核心原则宣言:** 强调模块组织和依赖管理的重要性。
*   **关键实践指南:** 提供不同类型模块的导入示例和组织方式。
*   **决策指导:** 包含模块选择和依赖管理的决策框架。
*   **清单:** 包括导入顺序、分组和优化的检查项。

### 错误处理类规则 (Error Handling Rules)

*   **核心原则宣言:** 强调错误处理对系统稳定性的核心价值。
*   **关键实践指南:** 针对不同类型的错误提供处理模式。
*   **决策指导:** 包含错误类型和处理策略的详细决策树。
*   **清单:** 区分系统级、应用级和用户交互级错误的检查项。

### 测试类规则 (Testing Rules)

*   **核心原则宣言:** 强调测试对代码质量的保障作用。
*   **关键实践指南:** 提供单元测试、集成测试的编写模式。
*   **决策指导:** 包含测试范围和深度的决策框架。
*   **清单:** 包含测试覆盖率、边界条件和测试维护的检查项。

### 文档类规则 (Documentation Rules)

*   **核心原则宣言:** 强调文档的受众和目的。
*   **关键实践指南:** 针对不同类型文档（API文档、架构文档）提供模板。
*   **决策指导:** 包含文档详细程度和更新频率的指南。
*   **清单:** 包含文档完整性、准确性和维护性的检查项。

## 模板示例 (Template Example)

```markdown
# 规则标题 (Rule Title)

---
# (此处为 YAML 元数据 YAML Frontmatter here)
---

## 核心原则宣言 (Core Principles Declaration)

⚡️ **核心问题 (Core Problem):** [简洁的问题陈述]

💥 **忽略的后果 (Consequences of Ignoring):**
- 后果 1
- 后果 2

💎 **遵守的好处 (Benefits of Following):**
- 好处 1
- 好处 2

⚖️ **必要的权衡 (Necessary Trade-offs):**
- 权衡 1: X vs Y
- 权衡 2: A vs B

## 关键实践指南 (Key Practices Guide)

#### 实践 1: [实践名称 (Practice Name)]

**为何需要 (Why):** [基本原理]

❌ **常见错误 (Common Mistake):**
```python
# 错误代码 (Bad code)
```

✅ **正确方法 (Correct Approach):**
```python
# 正确代码 (Good code)
```

🔄 **重构路径 (Refactoring Path):**
1. 步骤 1 (Step 1)
2. 步骤 2 (Step 2)

#### 实践 2: [实践名称 (Practice Name)]
...

## 决策指导 (Decision Guidance)

🌲 **决策树 (Decision Tree):**
1. 条件 X 是否为真? (Is condition X true?)
   - 是 (Yes): 使用方法 A (Use Method A)
   - 否 (No): 继续... (Continue...)

*或者 (or)*

📊 **方法比较 (Approach Comparison):**
| 方法 (Approach) | 背景 (Context) | 优点 (Pro) | 缺点 (Con) |
|---|---|---|---|
| ... | ... | ... | ... |

## 清单 (Checklist)

#### 编码阶段 (Coding Phase)
- [ ] 检查项 A (Check Item A)
      *判断标准 (Judgment Standard):* [如何判断]
      *快速修复 (Quick Fix):* [如何修复]

#### 代码审查阶段 (Code Review Phase)
- [ ] 检查项 B (Check Item B)
      *判断标准 (Judgment Standard):* [如何判断]
      *快速修复 (Quick Fix):* [如何修复]
```

