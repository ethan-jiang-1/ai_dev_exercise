# 任务约束：API数据验证框架

## 技术约束

1. **依赖项约束**：
   - 只使用Pydantic v2.0+
   - 不得使用其他验证库（如marshmallow、cerberus等）
   - 允许使用标准库和以下辅助库：
     - email-validator (用于邮箱验证)
     - phonenumbers (用于电话号码验证)

2. **架构约束**：
   - 必须采用模块化设计，将验证逻辑拆分为基础验证、业务规则验证和复合验证
   - 必须支持继承和组合模式以便复用验证规则
   - 必须实现责任链模式以支持分阶段验证

3. **实现约束**：
   - 使用Pydantic的Field类型注解进行基础验证
   - 必须实现自定义根验证器和字段验证器
   - 提供统一的错误处理机制，包括错误码和错误消息映射

## 测试要求

1. **测试覆盖**：
   - 单元测试覆盖率必须达到90%以上
   - 必须包含正向测试（有效数据）和反向测试（无效数据）
   - 必须测试所有验证规则的边界条件

2. **测试数据**：
   - 使用提供的测试集作为基准测试数据
   - 必须补充额外的边缘案例测试数据
   - 必须包含嵌套复杂结构的测试数据

3. **性能测试**：
   - 验证大型数据结构（100+字段）时性能不应明显下降
   - 批量验证（1000+条记录）的响应时间不超过3秒

## 演示数据集

以下测试数据将用于验证框架的功能完整性：

```json
// 有效用户数据示例
{
  "username": "valid_user123",
  "password": "SecureP@ss123",
  "email": "test@example.com",
  "phone": "+8613800138000",
  "profile": {
    "name": "张三",
    "age": 30,
    "address": {
      "province": "广东省",
      "city": "深圳市",
      "district": "南山区",
      "detail": "科技园南区T3栋5楼"
    }
  },
  "settings": {
    "notification_preferences": {
      "email_notifications": true,
      "sms_notifications": true,
      "push_notifications": false
    },
    "privacy": {
      "profile_visibility": "friends",
      "show_online_status": false
    }
  },
  "backup_email": "backup@example.org"
}

// 多个无效数据将用于测试不同验证规则
```

## 交付成果

1. 完整的API数据验证框架实现
2. 详细的单元测试
3. 演示脚本（展示验证框架的使用方法）
4. 技术文档（包括架构设计、API使用说明和扩展指南） 