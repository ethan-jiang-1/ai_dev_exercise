# HealthVision医疗影像API文档 v0.5 (已过期)

> **警告**: 此文档已过期，仅供参考历史版本。请查阅最新版API文档。

## 基本信息

- **基础URL**: `https://api.healthvision.com/v0.5`
- **格式**: JSON
- **认证**: API密钥
- **状态**: Beta版，不推荐用于生产环境

## 认证

所有API请求需要在HTTP头中包含API密钥：

```
X-API-Key: your_api_key_here
```

获取API密钥，请联系support@healthvision.com。

## 端点列表

### 影像上传

```
POST /upload
```

**请求参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| image | file | 是 | 要上传的影像文件 |
| type | string | 是 | 影像类型，可选值: "ct", "mri", "xray" |
| body_part | string | 是 | 身体部位，可选值: "brain", "chest", "lung" |
| description | string | 否 | 影像描述 |

**响应**:

```json
{
  "status": "success",
  "image_id": "img12345",
  "message": "Image uploaded successfully"
}
```

### 影像分析

```
POST /analyze
```

**请求参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| image_id | string | 是 | 已上传的影像ID |
| analysis_type | string | 是 | 分析类型，可选值: "nodule_detection", "tumor_detection", "covid_screening" |

**响应**:

```json
{
  "status": "success",
  "analysis_id": "an12345",
  "message": "Analysis started"
}
```

### 获取分析状态

```
GET /analysis/{analysis_id}/status
```

**响应**:

```json
{
  "status": "in_progress",
  "progress": 45,
  "estimated_completion_time": "2023-09-15T14:30:00Z"
}
```

### 获取分析结果

```
GET /analysis/{analysis_id}/result
```

**响应**:

```json
{
  "status": "completed",
  "results": {
    "findings": [
      {
        "type": "nodule",
        "location": {
          "x": 256,
          "y": 312,
          "z": 45
        },
        "size_mm": 8.4,
        "confidence": 0.89,
        "is_suspicious": true
      }
    ],
    "summary": "发现1个疑似结节，建议进一步检查"
  }
}
```

### 获取影像列表

```
GET /images
```

**查询参数**:

| 参数 | 类型 | 必填 | 描述 |
|------|------|------|------|
| page | integer | 否 | 页码，默认1 |
| per_page | integer | 否 | 每页条数，默认20 |
| type | string | 否 | 按影像类型筛选 |

**响应**:

```json
{
  "total": 42,
  "page": 1,
  "per_page": 20,
  "images": [
    {
      "id": "img12345",
      "type": "ct",
      "body_part": "lung",
      "upload_date": "2023-09-10T08:15:30Z",
      "has_analysis": true
    },
    // ...更多影像
  ]
}
```

## 已知问题

1. 影像上传接口不支持断点续传
2. 大型DICOM序列可能导致超时
3. 分析结果不包含详细的置信度分布
4. 不支持批量处理
5. 无法定制化分析参数

## 即将废弃的功能

以下功能将在v1.0中移除：

- `/upload`端点将由`/images/upload`替代
- `/analyze`端点将由`/analyses`替代
- 使用API密钥的认证方式将由OAuth 2.0替代
- `per_page`参数将由`limit`替代

## 计划中的改进

1. 支持更多影像格式
2. 添加角色权限控制
3. 提供批量处理能力
4. 改进分析结果的可视化
5. 添加WebHook通知机制

## 限制

- 最大文件大小: 100MB
- 请求频率: 每分钟30次
- 并发分析任务: 最多5个

## 联系我们

如有问题，请联系：
- 技术支持: support@healthvision.com
- API文档反馈: api-docs@healthvision.com

文档更新日期: 2023年8月15日
