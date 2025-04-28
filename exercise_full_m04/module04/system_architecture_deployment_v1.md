# NovaBrain 3.0 系统部署架构 v1.0

**文档版本**: 1.0
**日期**: 2024-01-15
**状态**: 草稿
**编制**: 赵工 (DevOps 专家), 王强 (后端负责人)

## 1. 概述

本文档描述了 NovaBrain 3.0 平台的核心部署架构。该架构旨在支持平台的模块化、可伸缩性、高可用性和安全性要求，特别是在满足中国大陆地区医疗和金融行业的合规要求方面。

## 2. 架构原则

*   **云原生**: 优先采用云原生技术（容器化、微服务、服务网格）。
*   **微服务**: 核心功能模块化为独立的微服务，独立部署和扩展。
*   **基础设施即代码 (IaC)**: 使用 Terraform 和 Helm 管理基础设施和应用部署。
*   **高可用与容灾**: 关键组件跨可用区部署，设计容灾预案。
*   **安全性**: 深度防御策略，零信任网络模型。
*   **可观测性**: 全面的日志、指标和追踪覆盖。

## 3. 部署环境

*   **云平台**: 阿里云 (主要面向中国大陆客户), AWS (用于国际客户和部分开发测试)
*   **主要部署区域 (生产)**: 阿里云华东 2 (上海)，多可用区部署 (如可用区 H, I, J)。
*   **容器编排**: 阿里云 ACK (容器服务 Kubernetes 版) / AWS EKS。
*   **网络**: 阿里云 VPC / AWS VPC, 使用安全组和网络 ACL 控制访问。

## 4. 核心组件与技术栈

以下是 NovaBrain 3.0 的主要组件及其部署方式：

```mermaid
graph TD
    subgraph "用户访问层"
        UI[Web UI (React)] --> GW(API 网关);
        CLI[CLI/SDK] --> GW;
    end

    subgraph "核心服务层 (Kubernetes 集群)"
        GW --> AuthNAuthZ(认证授权服务);
        GW --> LowCodeEngine(低代码引擎);
        GW --> ModelRegistry(模型注册中心);
        GW --> InferenceService(模型推理服务);
        GW --> DataIntegration(数据集成服务);
        GW --> NotificationService(通知服务);

        LowCodeEngine --> ModelRegistry;
        LowCodeEngine --> InferenceService;
        LowCodeEngine --> DataIntegration;
        ModelRegistry --> Storage(对象存储/模型库);
        InferenceService --> ModelRegistry;
        InferenceService --> GpuNodes(GPU 节点池);
        DataIntegration --> DbStore(数据库集群);
        DataIntegration --> Cache(分布式缓存);
        DataIntegration --> Storage;
        NotificationService --> MessageQueue(消息队列);

        AuthNAuthZ -.-> DbStore;
        LowCodeEngine -.-> DbStore;
        ModelRegistry -.-> DbStore;
    end

    subgraph "数据与存储层"
        DbStore[数据库集群 (PostgreSQL/RDS)];
        Storage[对象存储 (OSS/S3)];
        Cache[分布式缓存 (Redis)];
        MessageQueue[消息队列 (Kafka/RocketMQ)];
        GpuNodes[GPU 节点 (ACK/EKS)];
    end

    subgraph "运维与监控层"
        Logging[日志收集 (Fluentd/Elasticsearch/Kibana)];
        Metrics[指标监控 (Prometheus/Grafana)];
        Tracing[分布式追踪 (Jaeger)];
        Alerting[告警 (Alertmanager)];
        CICD[CI/CD (GitLab CI/Argo CD)];
    end

    style GW fill:#f9f,stroke:#333,stroke-width:2px
    style LowCodeEngine fill:#ccf,stroke:#333,stroke-width:2px
    style ModelRegistry fill:#ccf,stroke:#333,stroke-width:2px
    style InferenceService fill:#ccf,stroke:#333,stroke-width:2px
    style DataIntegration fill:#ccf,stroke:#333,stroke-width:2px
    style AuthNAuthZ fill:#ccf,stroke:#333,stroke-width:2px
    style GpuNodes fill:#fcc,stroke:#333,stroke-width:2px
```

*   **Web UI**: 基于 React 的单页应用，通过 CDN 加速，部署在对象存储或容器中。
*   **API 网关**: 基于 Nginx/Kong 或云厂商网关服务，处理入口流量、路由、限流、基础认证。
*   **认证授权服务**: 负责用户身份验证和 API 访问授权 (OAuth2/JWT)。
*   **低代码引擎**: 核心业务逻辑，提供可视化编排、组件管理、工作流执行。微服务架构，部署为 Kubernetes Deployment。
*   **模型注册中心**: 管理 AI 模型版本、元数据、生命周期。微服务架构，部署为 Kubernetes Deployment。
*   **模型推理服务**: 提供模型加载、预测接口。支持 CPU 和 GPU 推理，部署为 Kubernetes Deployment，使用 HPA (Horizontal Pod Autoscaler) 进行弹性伸缩，针对 GPU 使用特殊节点池。
*   **数据集成服务**: 负责连接外部数据源、数据转换、存储管理。微服务架构，部署为 Kubernetes Deployment。
*   **通知服务**: 处理异步通知、消息推送。
*   **数据库集群**: 使用云厂商 RDS (PostgreSQL)，配置主从复制和跨可用区副本，实现高可用。
*   **对象存储**: 使用云厂商 OSS/S3，存储模型文件、数据集、大文件等。
*   **分布式缓存**: 使用云厂商 Redis 服务，缓存热点数据，提高性能。
*   **消息队列**: 使用云厂商 Kafka/RocketMQ 服务，用于服务间异步通信、解耦。
*   **运维与监控**: 使用行业标准开源组件 (Prometheus, Grafana, EFK, Jaeger) 或云厂商服务，集成部署在 Kubernetes 集群或使用云厂商托管服务。

## 5. 网络架构

*   使用 VPC 划分网络边界，不同环境（开发、测试、生产）使用独立的 VPC。
*   核心服务部署在私有子网，通过负载均衡器 (SLB/ELB) 或 API 网关对外提供服务。
*   使用安全组严格限制实例间的访问策略，遵循最小权限原则。
*   考虑使用服务网格 (如 Istio) 增强服务间通信的可观测性、安全性和流量控制（未来规划）。

## 6. 高可用与容灾

*   **应用层**: 关键服务部署多个副本，分布在不同可用区。使用 Kubernetes 的自愈能力。
*   **数据层**: RDS/Redis/MQ 使用云厂商提供的多可用区高可用配置。对象存储本身具有高可用性。
*   **备份**: 数据库定期备份，跨区域存储备份文件。
*   **容灾**: （规划中）考虑在另一区域部署灾备环境，实现关键数据的异步复制和应用级的故障切换能力。

## 7. 部署流程

通过 CI/CD 流水线实现自动化部署。主要步骤包括：
1.  代码提交触发流水线。
2.  构建 Docker 镜像。
3.  单元测试和静态代码分析。
4.  将镜像推送到镜像仓库 (ACR/ECR)。
5.  使用 Helm 更新 Kubernetes Deployment 配置。
6.  通过 Argo CD 将变更同步到 Staging 环境。
7.  自动化集成测试和 API 测试。
8.  (手动审批)
9.  通过 Argo CD 将变更同步到 Production 环境（采用金丝雀发布策略）。

## 8. 未来考虑

*   服务网格 (Istio) 的引入。
*   AIOps 在监控和告警中的应用。
*   进一步优化多区域部署和容灾能力。
*   探索 Serverless 架构在特定场景的应用。 