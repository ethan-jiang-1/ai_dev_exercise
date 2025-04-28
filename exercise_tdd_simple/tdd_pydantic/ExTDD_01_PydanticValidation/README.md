# ExTDD_01_PydanticValidation: API数据验证框架

## 练习概述

本练习旨在实现一个基于Pydantic的API数据验证框架，主要用于验证用户注册信息。该框架将展示Pydantic强大的数据验证能力，包括基础类型验证、复杂业务规则验证和自定义验证器。

## 功能特点

- 创建可复用的数据验证模型
- 实现多层次嵌套数据结构验证
- 自定义验证器处理复杂业务规则
- 提供友好的错误报告机制
- 实现跨字段和条件验证

## 学习目标

通过本练习，您将学习：

1. 如何使用Pydantic定义强类型数据模型
2. 如何使用Field设置验证约束
3. 如何实现自定义验证器
4. 如何处理嵌套模型验证
5. 如何设计友好的错误反馈机制

## 文件说明

- `inputs/user_story.md`: 用户故事描述
- `inputs/test_data.json`: 测试数据集
- `constraints/task_constraints.md`: 技术约束和需求
- `outputs/api_data_validator.py`: 实现的验证框架(将创建)
- `outputs/test_api_data_validator.py`: 单元测试(将创建)

## 相关资源

- [Pydantic官方文档](https://docs.pydantic.dev/)
- [API数据验证最佳实践](https://fastapi.tiangolo.com/tutorial/body-validations/) 