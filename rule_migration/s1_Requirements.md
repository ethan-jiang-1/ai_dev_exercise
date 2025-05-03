# s1: 需求 - MDC 迁移目标 (Requirements - MDC Migration Goals)

## 迁移的目的
- 本迁移计划的核心目标是将旧的规则文件从 `rule_migration/rules_old/` 目录迁移到 `rule_migration/rules_mdc/` 目录，同时转换格式并利用新的 MDC 特性。

- 新的MDC的优点: **YAML 元数据 (YAML Frontmatter)**:
   - `description`: 规则的简洁描述，将显示在编辑器界面中
   - `globs`: 指定规则应用的文件类型/路径模式
   - `alwaysApply`: 设置为 `false`，确保规则仅在相关上下文中触发
   - `trigger`: （可选）定义何时激活规则的具体条件

- 老的RULES的文件划分, 可能没法完全利用新的MDC的优点, 可以重新组织.

