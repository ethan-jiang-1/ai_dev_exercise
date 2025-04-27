# 用户故事：DICOM 文件加载

## 用户故事

作为医疗影像系统的开发人员，我需要一个函数来加载和解析DICOM格式的医疗影像文件，以便从中提取元数据和像素数据用于后续处理和显示。

## 验收标准

1. 能够从指定路径加载DICOM文件
2. 验证文件是否为有效的DICOM格式
3. 从DICOM文件中提取关键元数据，包括：
   - 患者信息（PatientID、PatientName）
   - 研究信息（StudyInstanceUID、StudyDescription）
   - 序列信息（SeriesInstanceUID、SeriesDescription）
   - 图像信息（ImageType、Modality、PixelSpacing）
4. 能够访问和返回原始像素数据
5. 当文件不存在或格式无效时提供适当的错误处理

## 技术约束

1. 使用Python 3.10+
2. 使用pydicom库进行DICOM文件处理
3. 实现为单个函数，返回一个包含元数据和像素数据的对象或字典
4. 不修改原始DICOM文件
5. 在元数据提取过程中处理可能缺失的DICOM标签

## 注意事项

- 此功能是医疗影像处理流程的基础组件
- 需要考虑不同制造商和不同模态（如CT、MRI、超声等）的DICOM文件格式差异
- 为简化起见，可以专注于处理单帧DICOM文件
- 应优化内存使用，尤其是处理大型DICOM文件时 