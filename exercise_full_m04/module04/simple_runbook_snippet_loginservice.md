# 登录服务故障处理手册

## 告警：登录服务失败率高

### 检查步骤

1. 登录到登录服务器，执行 `systemctl status login-service` 检查服务状态
2. 查看日志文件 `/var/log/login-service/error.log` 寻找最近的错误信息
3. 检查数据库连接状态 `login-service-cli connection-test`
4. 检查认证系统状态 `curl -v https://auth-system.internal/health`

### 可能的解决方案

1. 如果服务未运行，尝试重启: `systemctl restart login-service`
2. 如果日志显示数据库连接问题，检查数据库状态和连接配置
3. 如果认证系统不可用，通知认证团队并考虑临时启用本地认证模式: `login-service-cli enable-local-auth`

### 升级流程

如果以上步骤无法解决问题，请按以下流程升级:
1. 通知运维组长
2. 创建P1级事件票据
3. 启动事件响应会议 