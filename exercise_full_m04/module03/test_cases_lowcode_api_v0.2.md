# NovaBrain 3.0 - 低代码引擎 API 测试用例 (v0.2)

**文档版本**: 1.1  
**日期**: 2023-11-30  
**状态**: 待执行  
**作者**: 李晓明，QA工程师  
**相关测试计划**: `test_plan_lowcode_engine_v0.2.md`  
**相关API文档**: `api_design_review_lowcode_engine_v0.1.md` (注: 本测试用例基于v0.2 API, 需对照最新API规范)

## 1. 测试概述

本文档包含了针对NovaBrain 3.0低代码引擎核心API (v0.2) 的主要测试用例。测试用例涵盖了功能测试（正向、负向、边界）、错误处理和基本的数据验证。

## 2. 测试环境与前提

- **环境**: 集成测试环境 (Integration Test Environment)
- **API基础URL**: `http://[test-env-host]/api/v1/lowcode`
- **认证**: 所有请求需包含有效的 `Authorization: Bearer [token]` 头 (使用测试用户凭证获取)
- **前提数据**: 预置部分用户账户、项目和基础组件定义。

## 3. 测试用例 - 可视化流程图管理 (`/graphs`)

### 3.1 创建流程图 (`POST /graphs`)

| 用例ID | 优先级 | 描述 | 测试步骤 | 预期结果 | 测试数据 |
|--------|--------|------|---------|---------|---------|
| TC-GRAPH-001 | P0 | 创建一个包含基本节点的简单流程图 | 1. 发送 `POST /graphs` 请求，包含有效的名称、描述和基础节点列表 | 1. 响应状态码 201 Created <br> 2. 响应体包含新创建的 `graph_id` 和详细信息 <br> 3. `GET /graphs/{new_graph_id}` 返回一致的信息 | `{ "name": "Simple Flow", "description": "Test flow 1", "nodes": [ ... ], "edges": [ ... ] }` |
| TC-GRAPH-002 | P1 | 创建一个具有复杂结构（多分支、循环引用 - 如果支持）的流程图 | 1. 发送 `POST /graphs` 请求，包含多个相互连接的复杂节点 | 1. 响应状态码 201 Created <br> 2. 响应体包含正确的结构信息 | `{ "name": "Complex Flow", ... }` |
| TC-GRAPH-003 | P1 | 创建流程图时缺少必需字段（如 `name`） | 1. 发送 `POST /graphs` 请求，缺少 `name` 字段 | 1. 响应状态码 400 Bad Request <br> 2. 响应体包含明确的错误信息（字段缺失） | `{ "description": "No name flow", ... }` |
| TC-GRAPH-004 | P1 | 创建流程图时使用无效的节点类型 | 1. 发送 `POST /graphs` 请求，`nodes` 列表中包含未定义的节点类型 | 1. 响应状态码 400 Bad Request <br> 2. 响应体包含明确的错误信息（无效节点类型） | `{ "name": "Invalid Node Flow", "nodes": [ { "id": "n1", "type": "NonExistentType", ... } ] }` |
| TC-GRAPH-005 | P2 | 创建流程图时名称过长 | 1. 发送 `POST /graphs` 请求，`name` 字段超过最大长度限制 | 1. 响应状态码 400 Bad Request 或 201 Created (取决于是否截断) <br> 2. (如果400) 错误信息指明长度超限 | `{ "name": "[Very long name...]", ... }` |
| TC-GRAPH-006 | P2 | 创建流程图时不包含任何节点或边 | 1. 发送 `POST /graphs` 请求，`nodes` 和 `edges` 为空数组 | 1. 响应状态码 201 Created <br> 2. 响应体 `nodes` 和 `edges` 为空 | `{ "name": "Empty Flow", "nodes": [], "edges": [] }` |

### 3.2 获取流程图 (`GET /graphs/{graph_id}`)

| 用例ID | 优先级 | 描述 | 测试步骤 | 预期结果 | 前提 |
|--------|--------|------|---------|---------|------|
| TC-GRAPH-007 | P0 | 获取存在的流程图详细信息 | 1. 使用有效的 `graph_id` 发送 `GET /graphs/{graph_id}` 请求 | 1. 响应状态码 200 OK <br> 2. 响应体包含与创建时一致的流程图详细信息 | 存在一个有效的 `graph_id` |
| TC-GRAPH-008 | P1 | 获取不存在的流程图 | 1. 使用无效或不存在的 `graph_id` 发送 `GET /graphs/{graph_id}` 请求 | 1. 响应状态码 404 Not Found <br> 2. 响应体包含错误信息 | 使用随机或已删除的 `graph_id` |
| TC-GRAPH-009 | P2 | 获取流程图时 `graph_id` 格式无效 | 1. 使用格式错误的 `graph_id` (如包含特殊字符) 发送 `GET` 请求 | 1. 响应状态码 400 Bad Request <br> 2. 响应体包含明确的错误信息 | N/A |

### 3.3 全量更新流程图 (`PUT /graphs/{graph_id}`)

| 用例ID | 优先级 | 描述 | 测试步骤 | 预期结果 | 前提 |
|--------|--------|------|---------|---------|------|
| TC-GRAPH-010 | P0 | 使用有效的完整数据更新流程图 | 1. 准备完整的流程图更新数据 <br> 2. 使用有效的 `graph_id` 发送 `PUT /graphs/{graph_id}` 请求 | 1. 响应状态码 200 OK <br> 2. 响应体包含更新后的流程图信息 <br> 3. `GET /graphs/{graph_id}` 返回更新后的信息 | 存在一个有效的 `graph_id` |
| TC-GRAPH-011 | P1 | 使用部分数据更新流程图 (PUT应拒绝) | 1. 准备仅包含部分字段（如仅 `name`）的数据 <br> 2. 发送 `PUT` 请求 | 1. 响应状态码 400 Bad Request (因为 PUT 通常要求全量替换) <br> 2. 错误信息指明缺少必需字段 | 存在一个有效的 `graph_id` |
| TC-GRAPH-012 | P1 | 更新不存在的流程图 | 1. 使用无效或不存在的 `graph_id` 发送 `PUT` 请求 | 1. 响应状态码 404 Not Found | 使用随机或已删除的 `graph_id` |
| TC-GRAPH-013 | P1 | 使用无效数据更新流程图 (如无效节点) | 1. 准备包含无效节点类型的数据 <br> 2. 发送 `PUT` 请求 | 1. 响应状态码 400 Bad Request <br> 2. 响应体包含明确的错误信息 | 存在一个有效的 `graph_id` |

### 3.4 局部更新流程图 (`PATCH /graphs/{graph_id}` - v0.2 新增)

| 用例ID | 优先级 | 描述 | 测试步骤 | 预期结果 | 前提 |
|--------|--------|------|---------|---------|------|
| TC-GRAPH-014 | P0 | 更新流程图名称和描述 | 1. 准备包含新 `name` 和 `description` 的数据 <br> 2. 使用有效的 `graph_id` 发送 `PATCH` 请求 | 1. 响应状态码 200 OK <br> 2. 响应体包含更新后的名称和描述，其他字段不变 <br> 3. `GET /graphs/{graph_id}` 验证更新 | 存在一个有效的 `graph_id` |
| TC-GRAPH-015 | P0 | 添加新的节点和边 | 1. 准备包含新 `nodes` 和 `edges` 的数据 <br> 2. 发送 `PATCH` 请求 | 1. 响应状态码 200 OK <br> 2. 响应体包含新增的节点和边 <br> 3. `GET /graphs/{graph_id}` 验证更新 | 存在一个有效的 `graph_id` |
| TC-GRAPH-016 | P1 | 更新现有节点的属性 | 1. 准备仅包含要更新的节点ID和新属性的数据 <br> 2. 发送 `PATCH` 请求 | 1. 响应状态码 200 OK <br> 2. 响应体中对应节点的属性已更新 <br> 3. `GET /graphs/{graph_id}` 验证更新 | 存在一个有效的 `graph_id` 和节点ID |
| TC-GRAPH-017 | P1 | 删除现有节点和相关边 | 1. 准备包含要删除的节点ID和相关边ID的数据（或通过特定语法标记删除）<br> 2. 发送 `PATCH` 请求 | 1. 响应状态码 200 OK <br> 2. 响应体中不再包含被删除的节点和边 <br> 3. `GET /graphs/{graph_id}` 验证更新 | 存在一个有效的 `graph_id`, 节点ID和边ID |
| TC-GRAPH-018 | P1 | 使用无效数据进行局部更新 (如更新不存在的节点) | 1. 准备更新一个不存在节点ID的数据 <br> 2. 发送 `PATCH` 请求 | 1. 响应状态码 400 Bad Request 或 404 Not Found <br> 2. 响应体包含明确的错误信息 | 存在一个有效的 `graph_id` |
| TC-GRAPH-019 | P1 | 局部更新不存在的流程图 | 1. 使用无效或不存在的 `graph_id` 发送 `PATCH` 请求 | 1. 响应状态码 404 Not Found | 使用随机或已删除的 `graph_id` |

### 3.5 删除流程图 (`DELETE /graphs/{graph_id}`)

| 用例ID | 优先级 | 描述 | 测试步骤 | 预期结果 | 前提 |
|--------|--------|------|---------|---------|------|
| TC-GRAPH-020 | P0 | 删除存在的流程图 | 1. 使用有效的 `graph_id` 发送 `DELETE /graphs/{graph_id}` 请求 | 1. 响应状态码 204 No Content <br> 2. `GET /graphs/{graph_id}` 返回 404 Not Found | 存在一个有效的 `graph_id` |
| TC-GRAPH-021 | P1 | 删除不存在的流程图 | 1. 使用无效或不存在的 `graph_id` 发送 `DELETE` 请求 | 1. 响应状态码 404 Not Found | 使用随机或已删除的 `graph_id` |
| TC-GRAPH-022 | P2 | 删除一个已被任务引用的流程图 (根据策略可能失败) | 1. 创建一个任务引用某 `graph_id` <br> 2. 发送 `DELETE` 请求删除该 `graph_id` | 1. 响应状态码 409 Conflict 或 400 Bad Request (如果禁止删除被引用的图) <br> 2. 响应体包含错误信息 | 存在一个任务引用该图 |

## 4. 测试用例 - 任务管理 (`/tasks`)

### 4.1 创建任务 (`POST /tasks`)

| 用例ID | 优先级 | 描述 | 测试步骤 | 预期结果 | 前提 |
|--------|--------|------|---------|---------|------|
| TC-TASK-001 | P0 | 基于有效的流程图创建任务 | 1. 准备包含有效 `graph_id` 的请求体 <br> 2. 发送 `POST /tasks` 请求 | 1. 响应状态码 201 Created <br> 2. 响应体包含新创建的 `task_id` 和初始状态 (如 `Pending`) <br> 3. `GET /tasks/{new_task_id}` 返回一致信息 | 存在一个有效的 `graph_id` |
| TC-TASK-002 | P1 | 创建任务时指定运行时参数 | 1. 准备包含有效 `graph_id` 和 `runtime_parameters` 的请求体 <br> 2. 发送 `POST /tasks` 请求 | 1. 响应状态码 201 Created <br> 2. 响应体包含 `task_id` 和 `runtime_parameters` <br> 3. 任务执行时应使用这些参数 | 存在有效的 `graph_id`，参数与图定义兼容 |
| TC-TASK-003 | P1 | 基于不存在的流程图创建任务 | 1. 使用无效或不存在的 `graph_id` 发送 `POST /tasks` 请求 | 1. 响应状态码 404 Not Found 或 400 Bad Request <br> 2. 响应体包含明确错误信息 | 使用随机或已删除的 `graph_id` |
| TC-TASK-004 | P1 | 创建任务时缺少 `graph_id` | 1. 发送不包含 `graph_id` 的 `POST /tasks` 请求 | 1. 响应状态码 400 Bad Request <br> 2. 错误信息指明字段缺失 | N/A |
| TC-TASK-005 | P2 | 创建任务时指定无效的运行时参数格式 | 1. 准备 `runtime_parameters` 格式错误 (如非 JSON 对象) 的请求 <br> 2. 发送 `POST /tasks` 请求 | 1. 响应状态码 400 Bad Request <br> 2. 错误信息指明参数格式错误 | 存在一个有效的 `graph_id` |

### 4.2 获取任务状态 (`GET /tasks/{task_id}`)

| 用例ID | 优先级 | 描述 | 测试步骤 | 预期结果 | 前提 |
|--------|--------|------|---------|---------|------|
| TC-TASK-006 | P0 | 获取存在的任务状态 | 1. 使用有效的 `task_id` 发送 `GET /tasks/{task_id}` 请求 | 1. 响应状态码 200 OK <br> 2. 响应体包含任务的详细信息，包括当前状态 (`Pending`, `Running`, `Completed`, `Failed`) | 存在一个有效的 `task_id` |
| TC-TASK-007 | P1 | 获取不存在的任务状态 | 1. 使用无效或不存在的 `task_id` 发送 `GET` 请求 | 1. 响应状态码 404 Not Found | 使用随机或已删除的 `task_id` |
| TC-TASK-008 | P2 | 获取任务状态时 `task_id` 格式无效 | 1. 使用格式错误的 `task_id` 发送 `GET` 请求 | 1. 响应状态码 400 Bad Request | N/A |

### 4.3 触发任务执行 (`POST /tasks/{task_id}/run`)

| 用例ID | 优先级 | 描述 | 测试步骤 | 预期结果 | 前提 |
|--------|--------|------|---------|---------|------|
| TC-TASK-009 | P0 | 触发一个处于 `Pending` 状态的任务 | 1. 使用处于 `Pending` 状态的有效 `task_id` 发送 `POST /tasks/{task_id}/run` 请求 | 1. 响应状态码 202 Accepted <br> 2. 稍后 `GET /tasks/{task_id}` 应返回 `Running` 或 `Completed`/`Failed` 状态 | 存在一个 `Pending` 状态的有效 `task_id` |
| TC-TASK-010 | P1 | 重复触发一个已在运行或已完成的任务 | 1. 使用处于 `Running` 或 `Completed`/`Failed` 状态的 `task_id` 发送 `POST /tasks/{task_id}/run` 请求 | 1. 响应状态码 409 Conflict 或 400 Bad Request <br> 2. 响应体包含错误信息（任务已运行/完成） | 存在一个非 `Pending` 状态的 `task_id` |
| TC-TASK-011 | P1 | 触发一个不存在的任务 | 1. 使用无效或不存在的 `task_id` 发送 `POST /tasks/{task_id}/run` 请求 | 1. 响应状态码 404 Not Found | 使用随机或已删除的 `task_id` |
| TC-TASK-012 | P2 | 触发任务时提供运行时参数 (覆盖创建时的参数) | 1. 发送 `POST /tasks/{task_id}/run` 请求，请求体包含 `runtime_parameters` | 1. 响应状态码 202 Accepted <br> 2. 任务执行时应使用本次请求提供的参数 | 存在一个 `Pending` 状态的有效 `task_id` |

### 4.4 查询任务列表 (`GET /tasks`)

| 用例ID | 优先级 | 描述 | 测试步骤 | 预期结果 | 前提 |
|--------|--------|------|---------|---------|------|
| TC-TASK-013 | P0 | 查询任务列表（无过滤） | 1. 发送 `GET /tasks` 请求 | 1. 响应状态码 200 OK <br> 2. 响应体为一个任务列表数组，包含用户有权访问的任务 | 存在多个任务 |
| TC-TASK-014 | P1 | 按状态过滤任务列表 (如 `status=Completed`) | 1. 发送 `GET /tasks?status=Completed` 请求 | 1. 响应状态码 200 OK <br> 2. 响应体只包含状态为 `Completed` 的任务 | 存在不同状态的任务 |
| TC-TASK-015 | P1 | 按 `graph_id` 过滤任务列表 | 1. 发送 `GET /tasks?graph_id=[valid_graph_id]` 请求 | 1. 响应状态码 200 OK <br> 2. 响应体只包含基于指定 `graph_id` 创建的任务 | 存在基于不同 `graph_id` 的任务 |
| TC-TASK-016 | P2 | 使用分页参数查询任务列表 (如 `limit=10&offset=10`) | 1. 发送带分页参数的 `GET /tasks` 请求 | 1. 响应状态码 200 OK <br> 2. 响应体包含对应分页的任务列表 <br> 3. (可选) 响应头或响应体包含总数信息 | 存在超过 `limit` 数量的任务 |
| TC-TASK-017 | P2 | 使用无效的过滤参数查询 | 1. 发送 `GET /tasks?invalid_param=abc` 请求 | 1. 响应状态码 400 Bad Request 或 200 OK (忽略无效参数) | N/A |

## 5. 错误处理测试用例

| 用例ID | 优先级 | 描述 | 测试步骤 | 预期结果 |
|--------|--------|------|---------|---------|
| TC-ERR-001 | P0 | 无效的请求方法 (如对 `/graphs` 使用 `DELETE`) | 1. 对不支持的方法发送请求 | 1. 响应状态码 405 Method Not Allowed |
| TC-ERR-002 | P0 | 无效的请求体 (如非 JSON 格式) | 1. 发送 `Content-Type: application/json` 但请求体格式错误 | 1. 响应状态码 400 Bad Request |
| TC-ERR-003 | P0 | 未提供认证信息 | 1. 发送请求时不带 `Authorization` 头 | 1. 响应状态码 401 Unauthorized |
| TC-ERR-004 | P0 | 提供无效的认证令牌 | 1. 发送请求时使用过期或伪造的令牌 | 1. 响应状态码 401 Unauthorized |
| TC-ERR-005 | P1 | 请求频率过高 (如果实现了速率限制) | 1. 在短时间内发送大量请求 | 1. 部分请求响应状态码 429 Too Many Requests |
| TC-ERR-006 | P1 | 内部服务器错误 (通过模拟触发) | 1. 模拟后端依赖服务异常 | 1. 响应状态码 500 Internal Server Error <br> 2. 响应体不应暴露敏感信息 |

## 6. 性能基准测试用例

| 用例ID | 优先级 | 描述 | 测试工具 | 并发用户/请求 | 关注指标 |
|--------|--------|------|---------|----------------|----------|
| TC-PERF-001 | P1 | 创建简单流程图 API 性能 | Locust | 10 VUs | 平均/P95/P99 响应时间, RPS, 失败率 |
| TC-PERF-002 | P1 | 获取流程图 API 性能 | Locust | 20 VUs | 平均/P95/P99 响应时间, RPS, 失败率 |
| TC-PERF-003 | P1 | 创建任务 API 性能 | Locust | 10 VUs | 平均/P95/P99 响应时间, RPS, 失败率 |
| TC-PERF-004 | P1 | 触发任务执行 API 性能 | Locust | 5 VUs | 平均/P95/P99 响应时间 (主要关注接收速度), RPS, 失败率 |
| TC-PERF-005 | P1 | 获取任务状态 API 性能 | Locust | 20 VUs | 平均/P95/P99 响应时间, RPS, 失败率 |

*注：性能测试目标值参考 `performance_test_requirements_draft.md`* 