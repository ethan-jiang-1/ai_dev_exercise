# Pydantic功能TDD练习

本目录包含了基于Pydantic库的测试驱动开发(TDD)练习集合。每个练习都围绕Pydantic的特定功能设计，旨在通过TDD方式掌握Pydantic的核心功能和最佳实践。

## 练习内容

该练习系列包含以下几个子练习：

1. **ExTDD_01_PydanticValidation**: 实现API数据验证框架，重点关注Pydantic的数据验证能力
2. **ExTDD_02_PydanticSerialization**: 实现数据序列化与转换框架，探索Pydantic的序列化功能
3. **ExTDD_03_PydanticConfig**: 基于Pydantic实现配置管理系统，利用Settings特性
4. **ExTDD_04_PydanticSchema**: 实现API模式演进与兼容性工具，处理API版本兼容问题

## 目录结构

每个练习子目录遵循以下统一结构：

```
ExTDD_XX_FeatureName/
├── constraints/                    # 约束条件
│   └── task_constraints.md        # 任务特定约束
├── inputs/                        # 输入文件
│   ├── user_story.md             # 用户故事
│   └── ...                       # 其他输入数据
├── outputs/                       # 输出文件
│   ├── _s1_think_options_{feature_name}.md
│   ├── _s2_think_design_{feature_name}.md
│   ├── _s3_think_validation_{feature_name}.md
│   ├── {feature_name}.py
│   ├── test_{feature_name}.py
│   └── doc_{feature_name}.md
└── README.md                      # 练习说明
```

## 学习目标

通过这些练习，您将学习：

1. 如何使用Pydantic定义强类型的数据模型
2. 如何实现和自定义复杂的数据验证规则
3. 如何使用Pydantic进行数据序列化和反序列化
4. 如何基于Pydantic构建配置管理系统
5. 如何处理API模式演进和版本兼容性问题

## 前置条件

- Python 3.8+
- Pydantic v2.0+
- 熟悉测试驱动开发的基本原则
- 了解Python的类型标注系统 