# Runbook: LoginService 响应时间过长

**告警**: `LoginService response time > 2s`

**初步处理步骤**:

1.  **检查日志**: 登录到相关节点 (`prod-app-03`)，查看 `LoginService` 的最新日志，寻找错误信息或异常堆栈跟踪。
   ```bash
   ssh prod-app-03 'tail -n 100 /var/log/novabrain/loginservice.log'
   ```
2.  **检查资源**: 查看节点 `prod-app-03` 的 CPU 和内存使用情况，判断是否资源耗尽。
   ```bash
   ssh prod-app-03 'top -bn1 | head -n 5 && free -h'
   ```
3.  **考虑重启**: 如果日志无明显错误且资源充足，但问题持续，可考虑安全重启 `LoginService` 实例。**注意：联系相关负责人确认是否可以重启。**
   ```bash
   # 重启命令示例 (具体命令需根据部署方式确定)
   ssh prod-app-03 'sudo systemctl restart loginservice'
   ``` 