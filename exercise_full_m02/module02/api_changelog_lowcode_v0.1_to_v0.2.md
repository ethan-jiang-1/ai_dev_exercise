# NovaBrain Low-Code API 变更日志：v0.1 → v0.2

## 变更概述

本次更新（2023年10月15日）主要针对 Low-Code 引擎 API 接口进行了多项改进，重点解决了用户反馈的性能瓶颈、扩展性问题，并支持了新的多模态处理功能。本文档详细记录了从 v0.1 到 v0.2 的所有 API 变更，供开发团队参考。

## 核心 API 变更

### 1. 模型部署接口优化

#### 变更前 (v0.1)

```http
POST /api/v1/models/deploy
Content-Type: application/json

{
  "model_id": "string",
  "version": "string",
  "config": {
    "resources": {
      "cpu": "number",
      "memory": "number",
      "gpu": "number"
    },
    "scaling": {
      "min_replicas": "number",
      "max_replicas": "number"
    }
  }
}
```

#### 变更后 (v0.2)

```http
POST /api/v1/models/deploy
Content-Type: application/json

{
  "model_id": "string",
  "version": "string",
  "deployment_name": "string",  // 新增：支持自定义部署名称
  "config": {
    "resources": {
      "cpu": "number",
      "memory": "number",
      "gpu": "number",
      "gpu_type": "string"     // 新增：指定 GPU 类型
    },
    "scaling": {
      "min_replicas": "number",
      "max_replicas": "number",
      "target_cpu_utilization": "number" // 新增：CPU 利用率阈值
    },
    "timeout": "number",       // 新增：请求超时设置
    "circuit_breaker": {       // 新增：熔断器配置
      "error_threshold": "number",
      "min_request_amount": "number"
    }
  },
  "monitoring": {              // 新增：监控配置
    "prometheus_endpoint": "string",
    "log_level": "string"
  }
}
```

#### 变更理由

1. 支持更精细的资源控制，解决 MediScan 项目中大模型部署资源分配不合理的问题
2. 增加熔断器和监控功能，提高系统稳定性和可观测性
3. 为多环境部署提供更灵活的命名支持

### 2. 数据处理 API 重构

#### 变更前 (v0.1)

```http
POST /api/v1/data/process
Content-Type: application/json

{
  "data_source_id": "string",
  "processor_type": "string",
  "parameters": { /* ... */ }
}
```

#### 变更后 (v0.2)

```http
POST /api/v1/data/pipelines
Content-Type: application/json

{
  "name": "string",
  "description": "string",  // 新增：管道描述
  "steps": [                // 重构：使用步骤数组替代单一处理器
    {
      "id": "string",
      "type": "string",
      "parameters": { /* ... */ },
      "dependencies": ["string"] // 新增：步骤依赖关系
    }
  ],
  "input": {
    "data_source_id": "string",
    "format": "string"       // 新增：指定输入格式
  },
  "output": {                // 新增：输出配置
    "destination": "string",
    "format": "string"
  },
  "scheduling": {           // 新增：执行调度控制
    "timeout": "number",
    "retry": {
      "max_attempts": "number",
      "backoff": "string"
    }
  }
}
```

#### 变更理由

1. 从单一处理器模型过渡到完整的处理管道，支持复杂的多步骤数据处理流程
2. 增强错误处理和重试机制，提高生产环境的可靠性
3. 支持 FinSecure 项目中的复杂数据转换需求

### 3. 新增 PATCH 方法支持

#### API 端点

```http
PATCH /api/v1/workflows/{workflow_id}
PATCH /api/v1/models/{model_id}/config
PATCH /api/v1/data/pipelines/{pipeline_id}
```

#### 功能描述

- 引入标准 JSON-Patch 格式(RFC 6902)支持部分更新操作
- 减少数据传输量，提高 API 响应速度
- 支持乐观并发控制，通过 ETag 和 If-Match 头处理更新冲突

## 非向后兼容变更

### 1. 弃用的 API 端点

以下 API 端点将在 v0.3 中完全移除，v0.2 中已标记为弃用：

- `/api/v1/models/simple-deploy` → 请使用 `/api/v1/models/deploy`
- `/api/v1/data/quick-process` → 请使用 `/api/v1/data/pipelines`

### 2. 状态码变更

- 操作成功但无内容返回时，状态码从 `200 OK` 变更为更符合语义的 `204 No Content`
- 资源创建成功时，确保返回 `201 Created` 而非之前的 `200 OK`

## 性能优化

1. 响应压缩：所有 API 响应默认启用 gzip 压缩，大幅减少传输数据大小
2. 批量操作：新增批量 API 端点 `/api/v1/batch`，支持在单一请求中执行多个操作
3. 分页优化：列表 API 引入基于游标的分页，替代偏移分页，提升大数据集查询性能

## 技术讨论记录

### 会议摘要：2023-10-02 API 设计评审

**参与者**：李工(前端)、孙工(后端)、王强(工程负责)

#### 讨论要点

1. **PATCH 接口实现方式**：
   - 孙工提议采用标准 JSON Patch (RFC 6902)，前端团队有顾虑
   - 李工指出前端实现 JSON Patch 生成较为繁琐
   - 最终决定：提供两种方式，标准 JSON Patch 和简化的"字段名-值"格式，后者仅适用于简单更新场景

2. **API 版本管理策略**：
   - 王强建议在 URL 中保留主版本号，细微变化通过内容协商处理
   - 一致同意在响应头中添加 API 版本信息，便于调试和问题追踪

3. **性能考量**：
   - 团队讨论了用户报告的大数据集 API 响应缓慢问题
   - 孙工解释了分页策略变更的技术原理和优势
   - 李工确认前端分页逻辑需要相应调整，预计工期为1天

### 后续行动

1. 前端团队（负责人：李工）：
   - 更新 API 客户端适配新的 API 结构
   - 实现 JSON Patch 支持
   - 调整分页组件逻辑

2. 后端团队（负责人：孙工）：
   - 完成新 API 端点实现和测试
   - 为弃用的端点添加警告响应头
   - 编写 API 迁移文档

3. QA 团队：
   - 设计向后兼容性测试用例
   - 验证性能指标改进情况

## 附件：影响评估

| 变更点 | 影响范围 | 迁移复杂度 | 兼容性策略 |
|-------|---------|-----------|----------|
| 模型部署 API 扩展 | 低（字段扩展） | 低 | 保持向后兼容，旧字段保持不变 |
| 数据处理 API 重构 | 高 | 中 | v0.1 端点保留，但标记为弃用 |
| PATCH 方法支持 | 中 | 低 | 新功能，无兼容性问题 |
| 状态码变更 | 低 | 低 | 客户端需松散检查成功状态码 |
| 批量操作 API | 低 | 低 | 新功能，无兼容性问题 |
| 分页机制变更 | 中 | 中 | 同时支持两种分页策略，6个月后移除旧分页 | 