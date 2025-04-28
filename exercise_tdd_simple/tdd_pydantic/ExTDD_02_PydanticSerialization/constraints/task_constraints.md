# 任务约束：数据序列化与转换框架

## 技术约束

1. **依赖项约束**：
   - 必须使用Pydantic v2.0+作为核心库
   - 可选使用以下辅助库：
     - xmltodict（用于XML转换）
     - pendulum（处理日期时间）
     - python-dateutil（复杂日期解析）
   - 不允许使用其他序列化库（如marshmallow等）

2. **架构约束**：
   - 采用适配器设计模式支持多种序列化格式
   - 使用策略模式处理不同类型的序列化规则
   - 实现访问者模式以支持模型遍历和定制序列化
   - 设计模式必须高内聚、低耦合

3. **实现约束**：
   - 使用Pydantic的model_dump/model_dump_json等原生方法
   - 必须实现自定义序列化器和反序列化器
   - 实现缓存机制以提高性能
   - 支持部分更新和增量序列化

## 测试要求

1. **测试覆盖**：
   - 单元测试覆盖率达到85%以上
   - 包含基准性能测试
   - 测试所有支持的数据格式
   - 测试各种边界情况和错误处理

2. **测试数据**：
   - 使用提供的金融交易数据集作为测试基准
   - 测试大型数据集的序列化性能
   - 测试复杂嵌套结构的完整性
   - 测试敏感数据脱敏效果

3. **兼容性测试**：
   - 测试不同版本模型间的向前/向后兼容性
   - 测试字段重命名和弃用场景
   - 测试模型迁移功能

## 演示数据集

以下为部分测试数据结构示例：

```json
// 金融交易记录示例
{
  "transaction_id": "TX123456789",
  "timestamp": "2023-05-15T14:30:45.123456+08:00",
  "amount": {
    "value": 1250.75,
    "currency": "CNY"
  },
  "type": "PAYMENT",
  "status": "COMPLETED",
  "payment_method": {
    "type": "CREDIT_CARD",
    "card": {
      "number": "4111111111111111",
      "expiry": "05/2025",
      "holder_name": "张三"
    }
  },
  "merchant": {
    "id": "MCH987654321",
    "name": "某某电商平台",
    "category": "RETAIL",
    "location": {
      "latitude": 39.9042,
      "longitude": 116.4074,
      "address": "北京市朝阳区某某大厦"
    }
  },
  "customer": {
    "id": "CUS12345",
    "name": "李四",
    "account_age_days": 732,
    "risk_score": 0.02
  },
  "items": [
    {
      "id": "ITM001",
      "name": "高端笔记本电脑",
      "quantity": 1,
      "unit_price": 8999.00,
      "discount": 500.00,
      "category": "ELECTRONICS"
    },
    {
      "id": "ITM002",
      "name": "无线鼠标",
      "quantity": 2,
      "unit_price": 199.50,
      "category": "ACCESSORIES"
    }
  ],
  "metadata": {
    "source_ip": "203.0.113.1",
    "device": "Web/Chrome",
    "promo_code": "SUMMER2023"
  }
}
```

## 交付成果

1. 完整的数据序列化与转换框架
2. 全面的单元测试和性能测试
3. 多种格式序列化的演示脚本
4. 技术设计文档
5. 用户指南（包含示例和最佳实践） 