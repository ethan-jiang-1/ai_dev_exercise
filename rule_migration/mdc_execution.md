# MDC规则迁移执行计划

## 迁移步骤

### 阶段一：核心规则迁移

#### 1. 核心开发原则 (principles.mdc)
1. [x] 备份转换
   ```bash
   cp principles.mdc principles.txt
   ```
2. [x] 检查并修正元数据
   ```yaml
   ---
   description: 确保代码遵循KISS、单一职责、渐进式开发等核心原则
   globs: \.py$
   alwaysApply: false
   ---
   ```
3. [x] 根据 mdc_design.md 更新内容并验证文档结构
   - 核心原则宣言
   - 关键实践指南
   - 决策指导
   - Checklist
4. [x] 删除原文件并重命名
   ```bash
   rm principles.mdc
   mv principles.txt principles.mdc
   ```

#### 2. 项目结构规范 (structure.mdc)
1. [x] 备份转换
   ```bash
   cp structure.mdc structure.txt
   ```
2. [x] 检查并修正元数据
   ```yaml
   ---
   description: 规范项目目录结构和模块划分
   globs: __init__\.py$,^[^/]+/$
   alwaysApply: false
   ---
   ```
3. [x] 根据 mdc_design.md 更新内容并验证文档结构
   - 目录组织规范
   - 模块划分标准
   - 包设计规范
4. [x] 删除原文件并重命名
   ```bash
   rm structure.mdc
   mv structure.txt structure.mdc
   ```

### 阶段二：编码规范迁移

#### 3. 代码风格规范 (coding_style.mdc)
1. [x] 备份转换
   ```bash
   cp coding_style.mdc coding_style.txt
   ```
2. [x] 检查并修正元数据
   ```yaml
   ---
   description: 统一Python代码风格和最佳实践
   globs: \.py$
   alwaysApply: false
   ---
   ```
3. [x] 根据 mdc_design.md 更新内容并验证文档结构
   - 命名规范
   - 格式规范
   - 代码组织规范
4. [x] 删除原文件并重命名
   ```bash
   rm coding_style.mdc
   mv coding_style.txt coding_style.mdc
   ```

#### 4. 模块导入规范 (imports.mdc)
1. [x] 备份转换
   ```bash
   cp imports.mdc imports.txt
   ```
2. [x] 检查并修正元数据
   ```yaml
   ---
   description: 规范化模块导入顺序和依赖管理
   globs: .*\.py$
   alwaysApply: false
   ---
   ```
3. [x] 根据 mdc_design.md 更新内容并验证文档结构
   - 导入顺序规范
   - 循环依赖处理
   - 第三方包管理
4. [x] 删除原文件并重命名
   ```bash
   rm imports.mdc
   mv imports.txt imports.mdc
   ```

### 阶段三：质量保障规则迁移

#### 5. 单元测试规范 (unit_testing.mdc)
1. [x] 备份转换
   ```bash
   cp unit_testing.mdc unit_testing.txt
   ```
2. [x] 检查并修正元数据
   ```yaml
   ---
   description: 规范化单元测试编写
   globs: test_.*\.py$,.*_test\.py$
   alwaysApply: false
   ---
   ```
3. [x] 根据 mdc_design.md 更新内容并验证文档结构
   - 测试用例设计
   - 断言规范
   - 测试隔离原则
4. [x] 删除原文件并重命名
   ```bash
   rm unit_testing.mdc
   mv unit_testing.txt unit_testing.mdc
   ```

#### 6. 错误处理指南 (error_handling.mdc)
1. [x] 备份转换
   ```bash
   cp error_handling.mdc error_handling.txt
   ```
2. [x] 检查并修正元数据
   ```yaml
   ---
   description: 标准化异常处理和错误管理
   globs: .*try.*except.*\.py$,.*raise.*\.py$
   alwaysApply: false
   ---
   ```
3. [x] 根据 mdc_design.md 更新内容并验证文档结构
   - 异常层次设计
   - 错误恢复策略
   - 日志记录规范
4. [x] 删除原文件并重命名
   ```bash
   rm error_handling.mdc
   mv error_handling.txt error_handling.mdc
   ```

### 阶段四：文档规范迁移

#### 7. API文档规范 (api_documentation.mdc)
1. [x] 备份转换
   ```bash
   cp api_documentation.mdc api_documentation.txt
   ```
2. [x] 检查并修正元数据
   ```yaml
   ---
   description: 标准化API文档编写
   globs: .*api.*\.py$,swagger\.yaml$,openapi\.json$
   alwaysApply: false
   ---
   ```
3. [x] 根据 mdc_design.md 更新内容并验证文档结构
   - 接口描述规范
   - 参数说明标准
   - 返回值规范
4. [x] 删除原文件并重命名
   ```bash
   rm api_documentation.mdc
   mv api_documentation.txt api_documentation.mdc
   ```

#### 8. 技术文档规范 (technical_docs.mdc)
1. [x] 备份转换
   ```bash
   cp technical_docs.mdc technical_docs.txt
   ```
2. [x] 检查并修正元数据
   ```yaml
   ---
   description: 规范化技术文档编写
   globs: docs/.*\.md$,README\.md$
   alwaysApply: false
   ---
   ```
3. [x] 根据 mdc_design.md 更新内容并验证文档结构
   - 文档结构规范
   - 示例编写标准
   - 维护更新流程
4. [x] 删除原文件并重命名
   ```bash
   rm technical_docs.mdc
   mv technical_docs.txt technical_docs.mdc
   ```

## 最终验证清单

### 单个规则文件验证 (对每个 *.mdc 文件执行)
1.  **元数据**: 
    - [x] 格式符合 `mdc_overview.md` YAML 规范
    - [x] `description`, `globs`, `alwaysApply` 值与 `mdc_design.md` 定义一致
2.  **文档结构**:
    - [x] 包含 `mdc_overview.md` 定义的四大核心章节:
        - `## 核心原则宣言`
        - `## 关键实践`
        - `## 决策指导`
        - `## Checklist`
    - [x] Markdown 格式规范，无明显渲染错误
3.  **内容质量 (参照 mdc_design.md)**:
    - [x] `核心原则宣言` 清晰阐述问题、后果、收益、权衡
    - [x] `关键实践` 包含具体指导和正反代码示例
    - [x] `决策指导` 提供明确判断标准或决策树
    - [x] `Checklist` 包含具体检查项、判断标准和修复建议
4.  **可执行性与可操作性**:
    - [x] 代码示例:
        - [x] 语法正确 (可通过 Linter 检查)
        - [x] 逻辑清晰，能说明问题
    - [x] Checklist 项:
        - [x] 判断标准明确，易于衡量
        - [x] 修复建议具体可行