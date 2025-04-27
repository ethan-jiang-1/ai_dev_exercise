# HealthVision 医疗影像API设计规范 v0.1

## 概述

HealthVision医疗影像API是一套RESTful API，允许开发者集成医疗影像分析功能到他们的应用中。API支持影像上传、分析请求、结果检索等功能，并提供严格的访问控制和审计能力。

## 基本信息

- **基础URL**: `https://api.healthvision.com/v1`
- **格式**: JSON
- **认证**: OAuth 2.0 + JWT
- **API版本**: v1

## 认证与授权

所有API请求必须包含有效的访问令牌，获取方式如下：

### 获取访问令牌

```
POST /auth/token
```

**请求参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| client_id | string | 是 | 开发者门户获取的客户端ID |
| client_secret | string | 是 | 开发者门户获取的客户端密钥 |
| grant_type | string | 是 | 授权类型，固定为"client_credentials" |
| scope | string | 否 | 请求的权限范围，如"images:read images:write" |

**响应**:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "expires_in": 3600,
  "scope": "images:read images:write"
}
```

## 错误处理

API使用标准HTTP状态码表示请求结果。常见状态码：

- 200: 成功
- 400: 请求参数错误
- 401: 未认证
- 403: 未授权
- 404: 资源未找到
- 429: 请求过于频繁
- 500: 服务器错误

错误响应格式：

```json
{
  "error": {
    "code": "invalid_parameter",
    "message": "Invalid value for parameter 'study_uid'",
    "details": {
      "parameter": "study_uid",
      "reason": "must be a valid DICOM UID"
    }
  }
}
```

## API端点

### 影像管理

#### 上传影像

```
POST /images/upload
```

**请求参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| image_type | string | 是 | 影像类型，可选："ct", "mri", "xray" |
| body_part | string | 是 | 身体部位，可选："brain", "chest", "lung", "other" |
| format | string | 是 | 文件格式，可选："dicom", "nifti", "jpeg", "tiff" |
| metadata | object | 否 | 影像相关元数据 |

**响应**:

```json
{
  "upload_id": "img_12345abcde",
  "upload_url": "https://storage.healthvision.com/uploads/temp/..."
}
```

上传完成后，客户端需要使用返回的`upload_url`通过PUT请求上传文件内容。

#### 获取上传状态

```
GET /images/upload/{upload_id}
```

**响应**:

```json
{
  "upload_id": "img_12345abcde",
  "status": "completed",
  "file_size": 15482367,
  "metadata": {
    "modality": "CT",
    "body_part": "chest"
  }
}
```

#### 获取影像列表

```
GET /images
```

**查询参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | integer | 否 | 页码，默认1 |
| limit | integer | 否 | 每页数量，默认20，最大100 |
| type | string | 否 | 按影像类型筛选 |
| body_part | string | 否 | 按身体部位筛选 |

**响应**:

```json
{
  "total": 127,
  "page": 1,
  "limit": 20,
  "images": [
    {
      "id": "img_12345abcde",
      "type": "ct",
      "body_part": "chest",
      "uploaded_at": "2023-11-01T10:30:15Z",
      "status": "active"
    },
    ...
  ]
}
```

#### 获取影像详情

```
GET /images/{image_id}
```

**响应**:

```json
{
  "id": "img_12345abcde",
  "type": "ct",
  "body_part": "chest",
  "format": "dicom",
  "file_size": 15482367,
  "slice_count": 120,
  "metadata": {
    "modality": "CT",
    "manufacturer": "GE Medical",
    "study_date": "2023-10-25"
  },
  "uploaded_at": "2023-11-01T10:30:15Z",
  "status": "active"
}
```

#### 删除影像

```
DELETE /images/{image_id}
```

**响应**:

```json
{
  "id": "img_12345abcde",
  "status": "deleted"
}
```

### 分析管理

#### 创建分析任务

```
POST /analyses
```

**请求参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| image_id | string | 是 | 待分析的影像ID |
| models | array | 是 | 要应用的模型ID列表 |
| priority | string | 否 | 优先级："normal"或"high" |
| callback_url | string | 否 | 分析完成回调URL |

**响应**:

```json
{
  "analysis_id": "an_67890fghij",
  "image_id": "img_12345abcde",
  "status": "pending",
  "models": ["lung_nodule_detection", "covid_screening"],
  "created_at": "2023-11-05T14:25:10Z",
  "estimated_completion_time": "2023-11-05T14:30:10Z"
}
```

#### 获取分析任务状态

```
GET /analyses/{analysis_id}
```

**响应**:

```json
{
  "analysis_id": "an_67890fghij",
  "image_id": "img_12345abcde",
  "status": "completed",
  "created_at": "2023-11-05T14:25:10Z",
  "completed_at": "2023-11-05T14:29:45Z",
  "models": ["lung_nodule_detection", "covid_screening"]
}
```

#### 获取分析任务列表

```
GET /analyses
```

**查询参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | integer | 否 | 页码，默认1 |
| limit | integer | 否 | 每页数量，默认20，最大100 |
| status | string | 否 | 按状态筛选："pending", "processing", "completed", "failed" |
| image_id | string | 否 | 按影像ID筛选 |

**响应**:

```json
{
  "total": 57,
  "page": 1,
  "limit": 20,
  "analyses": [
    {
      "analysis_id": "an_67890fghij",
      "image_id": "img_12345abcde",
      "status": "completed",
      "created_at": "2023-11-05T14:25:10Z"
    },
    ...
  ]
}
```

#### 取消分析任务

```
DELETE /analyses/{analysis_id}
```

**响应**:

```json
{
  "analysis_id": "an_67890fghij",
  "status": "cancelled"
}
```

### 结果管理

#### 获取分析结果

```
GET /analyses/{analysis_id}/results
```

**响应**:

```json
{
  "analysis_id": "an_67890fghij",
  "image_id": "img_12345abcde",
  "status": "completed",
  "results": [
    {
      "model": "lung_nodule_detection",
      "findings": [
        {
          "type": "nodule",
          "location": {
            "slice": 45,
            "x": 256,
            "y": 312
          },
          "dimensions": {
            "width_mm": 8.4,
            "height_mm": 7.9
          },
          "confidence": 0.92,
          "severity": "moderate",
          "description": "Possible pulmonary nodule detected"
        }
      ],
      "summary": "1 potential nodule found with high confidence"
    },
    {
      "model": "covid_screening",
      "findings": [
        {
          "result": "negative",
          "confidence": 0.87,
          "description": "No signs of COVID-19 related pneumonia"
        }
      ]
    }
  ]
}
```

#### 获取可视化结果

```
GET /analyses/{analysis_id}/visualizations
```

**查询参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| format | string | 否 | 可视化格式，可选："png", "jpeg", "html"，默认"png" |
| highlight | boolean | 否 | 是否高亮显示发现，默认true |

**响应**:

成功时返回二进制图像数据或HTML文档，失败时返回标准错误响应。

### 模型管理

#### 获取可用模型列表

```
GET /models
```

**查询参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| image_type | string | 否 | 按影像类型筛选 |
| body_part | string | 否 | 按身体部位筛选 |

**响应**:

```json
{
  "models": [
    {
      "id": "lung_nodule_detection",
      "name": "肺结节检测",
      "version": "2.3.0",
      "description": "检测肺部CT中的结节并进行分类",
      "supported_image_types": ["ct"],
      "supported_body_parts": ["chest", "lung"],
      "accuracy": 0.89,
      "average_processing_time": 45
    },
    {
      "id": "brain_tumor_segmentation",
      "name": "脑肿瘤分割",
      "version": "1.8.5",
      "description": "在脑部MRI中分割和分类肿瘤区域",
      "supported_image_types": ["mri"],
      "supported_body_parts": ["brain"],
      "accuracy": 0.91,
      "average_processing_time": 120
    },
    ...
  ]
}
```

#### 获取模型详情

```
GET /models/{model_id}
```

**响应**:

```json
{
  "id": "lung_nodule_detection",
  "name": "肺结节检测",
  "version": "2.3.0",
  "description": "检测肺部CT中的结节并进行分类",
  "supported_image_types": ["ct"],
  "supported_body_parts": ["chest", "lung"],
  "input_requirements": {
    "min_slices": 20,
    "max_slices": 500,
    "preferred_slice_thickness_mm": 1.25
  },
  "output_format": {
    "findings": [
      {
        "type": "string",
        "location": "object",
        "dimensions": "object",
        "confidence": "float",
        "severity": "string"
      }
    ]
  },
  "performance": {
    "accuracy": 0.89,
    "sensitivity": 0.92,
    "specificity": 0.87,
    "average_processing_time": 45
  },
  "last_updated": "2023-09-15"
}
```

### 批量处理

#### 创建批量处理任务

```
POST /batch
```

**请求参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| image_ids | array | 是 | 待分析的影像ID列表 |
| models | array | 是 | 要应用的模型ID列表 |
| priority | string | 否 | 优先级："normal"或"high" |
| callback_url | string | 否 | 批处理完成回调URL |

**响应**:

```json
{
  "batch_id": "ba_qrstuv12345",
  "status": "created",
  "total_images": 15,
  "models": ["lung_nodule_detection"],
  "created_at": "2023-11-06T09:15:30Z",
  "estimated_completion_time": "2023-11-06T09:45:30Z"
}
```

#### 获取批量处理状态

```
GET /batch/{batch_id}
```

**响应**:

```json
{
  "batch_id": "ba_qrstuv12345",
  "status": "in_progress",
  "total_images": 15,
  "completed_images": 8,
  "failed_images": 1,
  "created_at": "2023-11-06T09:15:30Z",
  "updated_at": "2023-11-06T09:25:45Z",
  "estimated_completion_time": "2023-11-06T09:40:00Z"
}
```

#### 获取批量处理结果

```
GET /batch/{batch_id}/results
```

**查询参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | integer | 否 | 页码，默认1 |
| limit | integer | 否 | 每页数量，默认20，最大100 |
| status | string | 否 | 按状态筛选："completed", "failed" |

**响应**:

```json
{
  "batch_id": "ba_qrstuv12345",
  "status": "completed",
  "total_images": 15,
  "completed_images": 14,
  "failed_images": 1,
  "page": 1,
  "limit": 20,
  "results": [
    {
      "image_id": "img_12345abcde",
      "analysis_id": "an_67890fghij",
      "status": "completed"
    },
    ...
  ],
  "failures": [
    {
      "image_id": "img_54321edcba",
      "error": {
        "code": "format_error",
        "message": "Failed to process the image format"
      }
    }
  ]
}
```

### 审计日志

#### 获取审计日志

```
GET /audit-logs
```

**查询参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | integer | 否 | 页码，默认1 |
| limit | integer | 否 | 每页数量，默认20，最大100 |
| start_date | string | 否 | 开始日期，ISO 8601格式 |
| end_date | string | 否 | 结束日期，ISO 8601格式 |
| action | string | 否 | 按操作类型筛选 |
| resource_type | string | 否 | 按资源类型筛选 |
| resource_id | string | 否 | 按资源ID筛选 |

**响应**:

```json
{
  "total": 256,
  "page": 1,
  "limit": 20,
  "logs": [
    {
      "id": "log_12345abcde",
      "timestamp": "2023-11-05T14:25:10Z",
      "action": "analysis.create",
      "actor": {
        "type": "api_key",
        "id": "key_56789fghij"
      },
      "resource": {
        "type": "analysis",
        "id": "an_67890fghij"
      },
      "details": {
        "image_id": "img_12345abcde",
        "models": ["lung_nodule_detection"]
      },
      "ip_address": "203.0.113.42"
    },
    ...
  ]
}
```

## 速率限制

API使用基于令牌桶算法的速率限制。限制因用户账户等级不同而异：

- 免费账户：每分钟60个请求，每天500个请求
- 专业账户：每分钟300个请求，每天5,000个请求
- 企业账户：每分钟1,000个请求，每天不限

HTTP响应头中包含速率限制信息：

```
X-RateLimit-Limit: 60
X-RateLimit-Remaining: 45
X-RateLimit-Reset: 1636042800
```

## Webhook

可以配置Webhook接收事件通知。支持的事件类型：

- `image.uploaded`: 影像上传完成
- `analysis.completed`: 分析任务完成
- `analysis.failed`: 分析任务失败
- `batch.completed`: 批处理任务完成

Webhook请求格式：

```json
{
  "event": "analysis.completed",
  "timestamp": "2023-11-05T14:29:45Z",
  "data": {
    "analysis_id": "an_67890fghij",
    "image_id": "img_12345abcde",
    "status": "completed"
  }
}
```

### 配置Webhook

```
POST /webhooks
```

**请求参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| url | string | 是 | Webhook接收URL |
| events | array | 是 | 要接收的事件类型列表 |
| secret | string | 否 | 用于验证Webhook请求的密钥 |

**响应**:

```json
{
  "webhook_id": "wh_12345abcde",
  "url": "https://example.com/webhooks/healthvision",
  "events": ["analysis.completed", "analysis.failed"],
  "created_at": "2023-11-06T10:00:00Z",
  "status": "active"
}
```

## SDK和客户端库

官方提供以下编程语言的SDK：

- Python
- JavaScript/TypeScript
- Java
- C#
- Ruby

## 未来功能

以下API功能计划在未来版本中添加：

- 支持更多影像类型和分析模型
- 批量上传功能
- 结果对比工具
- 自定义分析工作流
- 用户反馈和模型改进API
- 支持联邦学习
