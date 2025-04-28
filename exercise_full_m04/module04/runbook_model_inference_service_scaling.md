# 操作手册 (Runbook): 手动扩缩容 NovaBrain 模型推理服务

*   **服务**: `model-inference-service`
*   **目标**: 根据实时负载或预期流量变化，手动增加或减少模型推理服务的 Pod 实例数量。
*   **触发条件**: 
    *   监控告警: CPU/GPU 使用率持续高于阈值 (e.g., > 80% for 15 mins)。
    *   监控告警: P99 推理延迟持续高于 SLA (e.g., > 500ms for 10 mins)。
    *   预期流量高峰: 大型营销活动、新功能上线前。
    *   预期流量低谷: 非工作时间、节假日。
*   **执行者**: SRE 团队 / 平台运维团队
*   **依赖工具**: `kubectl`, Helm, Grafana (监控), K8s Dashboard (可选)
*   **版本**: 1.1
*   **日期**: 2024-02-01

## 1. 前置检查与准备

*   **[ ] 确认 Kubernetes 集群状态**: 
    *   使用 `kubectl get nodes` 检查集群节点是否 `Ready`。
    *   使用 `kubectl cluster-info` 确认 API Server 可访问。
*   **[ ] 确认 Helm 配置**: 
    *   确认当前环境 (`staging` 或 `production`) 的 Helm Release 名称和 Chart 版本。
    *   (通常在部署记录或配置管理库中查找)
*   **[ ] 检查当前副本数和资源使用情况**: 
    *   获取当前 Deployment 的副本数: `kubectl get deployment model-inference-service -n novabrain -o jsonpath='{.spec.replicas}'` (替换 namespace `novabrain`)
    *   查看 Pod 资源使用率: 通过 Grafana 仪表盘或 `kubectl top pods -n novabrain -l app=model-inference-service`。
*   **[ ] 确定目标副本数**: 
    *   根据触发条件和历史数据评估所需的目标副本数 (e.g., 扩容增加 50%, 缩容减少 30%)。
    *   确保目标副本数不超过集群可用资源（CPU, Memory, GPU）。
*   **[ ] (重要) 通知相关方**: 在执行变更前，通过内部通讯工具（如 Slack #operations 频道）通知相关开发团队和产品负责人，说明变更原因、预期影响和预计完成时间。

## 2. 执行扩容 (Scaling Up)

*   **[ ] 使用 `kubectl scale` 命令直接调整副本数**: 
    *   命令: `kubectl scale deployment model-inference-service --replicas=<目标副本数> -n novabrain`
    *   示例: `kubectl scale deployment model-inference-service --replicas=15 -n novabrain`
*   **[ ] (替代方案) 使用 `helm upgrade` 修改副本数 (如果副本数由 Helm Chart 管理)**: 
    *   命令: `helm upgrade <release-name> <chart-path> -n novabrain --set replicaCount=<目标副本数>`
    *   *注意: 此方法会应用 Chart 中的其他可能变更，通常用于版本更新而非临时扩缩容。优先使用 `kubectl scale` 进行临时调整。*
*   **[ ] 监控 Pod 启动状态**: 
    *   使用 `kubectl get pods -n novabrain -l app=model-inference-service -w` 实时观察新 Pod 是否成功启动并进入 `Running` 状态。
    *   检查 Pod Events: `kubectl describe pod <new-pod-name> -n novabrain` 查看是否有错误信息。
*   **[ ] 验证服务健康**: 
    *   检查 K8s Service Endpoint 是否包含新的 Pod IP: `kubectl get endpoints model-inference-service -n novabrain`
    *   观察 Grafana 仪表盘，确认新 Pod 开始处理流量，整体 QPS 上升，延迟下降或保持稳定，错误率无明显增加。

## 3. 执行缩容 (Scaling Down)

*   **[ ] 使用 `kubectl scale` 命令直接调整副本数**: 
    *   命令: `kubectl scale deployment model-inference-service --replicas=<目标副本数> -n novabrain`
    *   示例: `kubectl scale deployment model-inference-service --replicas=5 -n novabrain`
    *   *注意: 缩容时，Kubernetes 会根据策略（默认是随机）终止多余的 Pod。*
*   **[ ] 监控 Pod 终止状态**: 
    *   使用 `kubectl get pods -n novabrain -l app=model-inference-service -w` 观察多余的 Pod 是否平滑进入 `Terminating` 状态并最终消失。
*   **[ ] 验证服务健康**: 
    *   观察 Grafana 仪表盘，确认剩余 Pod 能够承载当前流量，延迟、错误率等指标仍在可接受范围内。
    *   确保 QPS 符合预期（如果缩容是为了降低成本，QPS 应相应下降）。

## 4. 后续操作与验证

*   **[ ] 持续监控**: 在变更完成后，持续监控相关指标（延迟、错误率、资源使用率、QPS）至少 30 分钟，确保服务稳定运行在新的副本数下。
*   **[ ] (扩容后) 评估 HPA (Horizontal Pod Autoscaler) 配置**: 如果频繁需要手动扩容，评估是否应配置或调整 HPA 策略，使其能根据 CPU/Memory 使用率或自定义指标自动扩缩容。
*   **[ ] 更新事件记录**: 在事件跟踪系统或运维日志中记录本次操作的时间、原因、执行步骤、目标副本数和结果。
*   **[ ] 通知相关方**: 操作完成且服务稳定后，再次通知相关方。

## 5. 回滚计划

*   **触发条件**: 
    *   扩容/缩容后，服务核心指标（延迟、错误率）显著恶化且持续超过 5 分钟。
    *   新 Pod 无法正常启动或持续 CrashLoopBackOff。
*   **回滚步骤**: 
    1.  立即使用 `kubectl scale` 将副本数恢复到变更前的数量。
        *   命令: `kubectl scale deployment model-inference-service --replicas=<变更前副本数> -n novabrain`
    2.  监控服务指标和 Pod 状态，确认是否恢复正常。
    3.  如果问题仍然存在，可能需要回滚整个 Deployment 版本（参考平台服务部署的回滚流程）。
    4.  记录回滚操作和原因。
    5.  深入排查导致回滚的原因。 