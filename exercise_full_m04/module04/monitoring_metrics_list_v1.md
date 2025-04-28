# NovaBrain 3.0 监控指标列表

## 基础设施指标

| 指标名称 | 说明 | 来源 | 默认阈值 | 告警级别 |
|---------|------|------|----------|----------|
| cpu_usage | CPU使用率 | 节点监控 | >85% | 警告 |
| memory_usage | 内存使用率 | 节点监控 | >90% | 警告 |
| disk_usage | 磁盘使用率 | 节点监控 | >85% | 警告 |
| disk_iops | 磁盘IO操作数 | 节点监控 | >5000 | 警告 |
| network_in | 网络入带宽 | 节点监控 | >800Mbps | 警告 |
| network_out | 网络出带宽 | 节点监控 | >800Mbps | 警告 |

## 应用指标

| 指标名称 | 说明 | 来源 | 默认阈值 | 告警级别 |
|---------|------|------|----------|----------|
| api_latency_p95 | API 95%延迟 | API网关 | >200ms | 警告 |
| api_latency_p99 | API 99%延迟 | API网关 | >500ms | 严重 |
| api_error_rate | API错误率 | API网关 | >1% | 警告 |
| api_error_rate | API错误率 | API网关 | >5% | 严重 |
| http_5xx_rate | HTTP 5xx错误率 | API网关 | >0.1% | 警告 |

## 数据库指标

| 指标名称 | 说明 | 来源 | 默认阈值 | 告警级别 |
|---------|------|------|----------|----------|
| db_connection_usage | 数据库连接使用率 | 数据库监控 | >80% | 警告 |
| db_query_latency_p95 | 查询延迟P95 | 数据库监控 | >100ms | 警告 |
| db_deadlocks | 死锁数量 | 数据库监控 | >0 | 警告 |
| db_replication_lag | 复制延迟 | 数据库监控 | >30s | 严重 |

## 模型服务指标

| 指标名称 | 说明 | 来源 | 默认阈值 | 告警级别 |
|---------|------|------|----------|----------|
| model_inference_latency_p95 | 模型推理延迟P95 | 模型服务 | >300ms | 警告 |
| model_inference_latency_p99 | 模型推理延迟P99 | 模型服务 | >800ms | 严重 |
| model_error_rate | 模型错误率 | 模型服务 | >1% | 警告 |
| model_inference_queue_length | 推理请求队列长度 | 模型服务 | >100 | 警告 |
| gpu_memory_usage | GPU内存使用率 | 模型服务 | >90% | 警告 |

## 低代码引擎指标

| 指标名称 | 说明 | 来源 | 默认阈值 | 告警级别 |
|---------|------|------|----------|----------|
| lowcode_component_load_time | 组件加载时间 | 低代码引擎 | >500ms | 警告 |
| lowcode_workflow_execution_time | 工作流执行时间 | 低代码引擎 | >5s | 警告 |
| lowcode_error_rate | 低代码操作错误率 | 低代码引擎 | >1% | 警告 |

## 业务指标

| 指标名称 | 说明 | 来源 | 默认阈值 | 告警级别 |
|---------|------|------|----------|----------|
| login_success_rate | 登录成功率 | 认证服务 | <98% | 严重 |
| active_sessions | 活跃会话数 | 会话服务 | 监控趋势 | 信息 |
| transaction_success_rate | 交易成功率 | 交易服务 | <99.9% | 严重 |
| user_action_latency_p95 | 用户操作延迟P95 | 前端监控 | >1s | 警告 |
