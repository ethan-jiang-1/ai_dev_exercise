import os
import time
import logging
import uuid
from typing import Dict, List, Optional, Union, Tuple, Any
import numpy as np
import pydicom
import nibabel as nib
from PIL import Image
import cv2
import SimpleITK as sitk
import torch
from fastapi import UploadFile
from pymongo import MongoClient
import redis

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("image_processor")

# 数据库连接
mongo_client = MongoClient(os.environ.get("MONGO_URI", "mongodb://localhost:27017"))
db = mongo_client.medical_imaging
images_collection = db.images
results_collection = db.results

# Redis连接
redis_client = redis.Redis(
    host=os.environ.get("REDIS_HOST", "localhost"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    db=0
)

# 存储目录配置
UPLOAD_DIR = os.environ.get("UPLOAD_DIR", "/tmp/healthvision/uploads")
PROCESSED_DIR = os.environ.get("PROCESSED_DIR", "/tmp/healthvision/processed")

# 确保目录存在
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(PROCESSED_DIR, exist_ok=True)

class ImageProcessor:
    def __init__(self, config: Optional[Dict] = None):
        self.config = config or {}
        self.supported_formats = ["dicom", "nifti", "jpeg", "png", "tiff"]
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        logger.info(f"Using device: {self.device}")
        
        # 加载模型
        self.models = {}
        self._load_models()

    def _load_models(self):
        """加载影像分析模型"""
        model_configs = self.config.get("models", {})
        for model_id, model_config in model_configs.items():
            try:
                # 这里应该实现具体的模型加载逻辑
                logger.info(f"Loading model: {model_id}")
                # 示例实现，实际应根据模型类型加载不同模型
                self.models[model_id] = self._load_model_by_type(model_id, model_config)
            except Exception as e:
                logger.error(f"Failed to load model {model_id}: {str(e)}")
    
    def _load_model_by_type(self, model_id: str, config: Dict):
        model_type = config.get("type")
        if model_type == "lung_nodule":
            # 加载肺结节检测模型
            return self._load_lung_nodule_model(config)
        elif model_type == "brain_tumor":
            # 加载脑肿瘤分割模型
            return self._load_brain_tumor_model(config)
        elif model_type == "xray_classifier":
            # 加载X光分类模型
            return self._load_xray_classifier_model(config)
        else:
            raise ValueError(f"Unsupported model type: {model_type}")

    def _load_lung_nodule_model(self, config: Dict):
        # 实际项目中应该加载真实的肺结节检测模型
        # 这里仅作示例
        model_path = config.get("path")
        logger.info(f"Loading lung nodule model from {model_path}")
        # 返回一个示例模型
        return {"type": "lung_nodule", "loaded_at": time.time()}

    def _load_brain_tumor_model(self, config: Dict):
        # 实际项目中应该加载真实的脑肿瘤分割模型
        model_path = config.get("path")
        logger.info(f"Loading brain tumor model from {model_path}")
        # 返回一个示例模型
        return {"type": "brain_tumor", "loaded_at": time.time()}

    def _load_xray_classifier_model(self, config: Dict):
        # 实际项目中应该加载真实的X光分类模型
        model_path = config.get("path")
        logger.info(f"Loading X-ray classifier model from {model_path}")
        # 返回一个示例模型
        return {"type": "xray_classifier", "loaded_at": time.time()}

    async def save_upload_file(self, upload_file: UploadFile) -> str:
        """保存上传的文件并返回文件路径"""
        file_id = str(uuid.uuid4())
        file_extension = self._get_file_extension(upload_file.filename)
        file_path = os.path.join(UPLOAD_DIR, f"{file_id}{file_extension}")
        
        with open(file_path, "wb") as f:
            content = await upload_file.read()
            f.write(content)
        
        logger.info(f"Saved uploaded file to {file_path}")
        return file_path

    def _get_file_extension(self, filename: Optional[str]) -> str:
        if not filename:
            return ""
        return os.path.splitext(filename)[1].lower()

    def process_image(self, file_path: str, image_type: str, body_part: str, 
                     model_ids: List[str]) -> Dict:
        """
        处理医疗影像文件
        
        Args:
            file_path: 影像文件路径
            image_type: 影像类型 (ct, mri, xray)
            body_part: 身体部位 (brain, chest, lung, other)
            model_ids: 要应用的模型ID列表
            
        Returns:
            处理结果字典
        """
        try:
            # 检查文件格式
            file_format = self._detect_file_format(file_path)
            if file_format not in self.supported_formats:
                raise ValueError(f"Unsupported file format: {file_format}")
            
            # 加载影像
            image_data = self._load_image(file_path, file_format)
            
            # 预处理
            preprocessed_data = self._preprocess_image(image_data, image_type, body_part, file_format)
            
            # 应用指定的模型
            results = {}
            for model_id in model_ids:
                if model_id not in self.models:
                    logger.warning(f"Model {model_id} not found, skipping")
                    continue
                
                # 运行模型推理
                model_result = self._run_inference(preprocessed_data, model_id, image_type, body_part)
                results[model_id] = model_result
            
            # 保存处理后的影像和结果
            result_id = self._save_results(file_path, image_type, body_part, results)
            
            return {
                "status": "success",
                "result_id": result_id,
                "results": results
            }
            
        except Exception as e:
            logger.error(f"Error processing image: {str(e)}")
            return {
                "status": "error",
                "error": str(e)
            }

    def _detect_file_format(self, file_path: str) -> str:
        """检测文件格式"""
        ext = os.path.splitext(file_path)[1].lower()
        if ext == ".dcm":
            return "dicom"
        elif ext in [".nii", ".nii.gz"]:
            return "nifti"
        elif ext in [".jpg", ".jpeg"]:
            return "jpeg"
        elif ext == ".png":
            return "png"
        elif ext in [".tif", ".tiff"]:
            return "tiff"
        else:
            # 尝试进一步检测
            try:
                # 尝试作为DICOM读取
                pydicom.dcmread(file_path)
                return "dicom"
            except:
                try:
                    # 尝试作为NIfTI读取
                    nib.load(file_path)
                    return "nifti"
                except:
                    # 尝试作为常规图像读取
                    try:
                        Image.open(file_path)
                        # 根据实际格式返回
                        img = Image.open(file_path)
                        return img.format.lower()
                    except:
                        raise ValueError("Unknown file format")

    def _load_image(self, file_path: str, file_format: str) -> Any:
        """加载不同格式的医疗影像文件"""
        if file_format == "dicom":
            return pydicom.dcmread(file_path)
        elif file_format == "nifti":
            return nib.load(file_path)
        elif file_format in ["jpeg", "png", "tiff"]:
            return Image.open(file_path)
        else:
            raise ValueError(f"Unsupported format for loading: {file_format}")

    def _preprocess_image(self, image_data: Any, image_type: str, 
                         body_part: str, file_format: str) -> np.ndarray:
        """预处理医疗影像数据，转换为标准格式"""
        # 根据不同格式进行预处理
        if file_format == "dicom":
            # 处理DICOM格式
            try:
                # 转换为numpy数组
                return self._preprocess_dicom(image_data)
            except Exception as e:
                logger.error(f"Error preprocessing DICOM: {str(e)}")
                raise
        elif file_format == "nifti":
            # 处理NIfTI格式
            try:
                # 转换为numpy数组
                return self._preprocess_nifti(image_data)
            except Exception as e:
                logger.error(f"Error preprocessing NIfTI: {str(e)}")
                raise
        elif file_format in ["jpeg", "png", "tiff"]:
            # 处理常规图像格式
            try:
                return self._preprocess_regular_image(image_data, image_type, body_part)
            except Exception as e:
                logger.error(f"Error preprocessing image: {str(e)}")
                raise
        else:
            raise ValueError(f"Unsupported format for preprocessing: {file_format}")

    def _preprocess_dicom(self, dicom_data):
        """预处理DICOM数据"""
        pixel_array = dicom_data.pixel_array
        
        # 处理像素数据
        if dicom_data.PhotometricInterpretation == "MONOCHROME1":
            # 对于MONOCHROME1，需要反转像素值
            pixel_array = np.amax(pixel_array) - pixel_array
            
        # 归一化
        if pixel_array.max() > 0:
            pixel_array = pixel_array / pixel_array.max()
            
        return pixel_array

    def _preprocess_nifti(self, nifti_data):
        """预处理NIfTI数据"""
        # 获取数据数组
        data_array = nifti_data.get_fdata()
        
        # 标准化处理
        data_min = data_array.min()
        data_max = data_array.max()
        if data_max > data_min:
            data_array = (data_array - data_min) / (data_max - data_min)
            
        return data_array

    def _preprocess_regular_image(self, image_data, image_type, body_part):
        """预处理常规图像数据"""
        # 转换为numpy数组
        img_array = np.array(image_data)
        
        # 转换为灰度图（如果是彩色图像）
        if len(img_array.shape) == 3 and img_array.shape[2] == 3:
            img_array = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            
        # 调整尺寸（根据模型需求）
        if image_type == "xray" and body_part == "chest":
            # 胸部X光可能需要特定尺寸
            img_array = cv2.resize(img_array, (512, 512))
        else:
            # 默认尺寸
            img_array = cv2.resize(img_array, (256, 256))
            
        # 归一化
        if img_array.max() > 0:
            img_array = img_array / img_array.max()
            
        return img_array

    def _run_inference(self, preprocessed_data: np.ndarray, model_id: str, 
                      image_type: str, body_part: str) -> Dict:
        """运行模型推理"""
        model = self.models.get(model_id)
        if not model:
            raise ValueError(f"Model {model_id} not found")
        
        # 实际项目中应根据模型类型进行实际推理
        # 这里仅作示例，返回模拟结果
        if model["type"] == "lung_nodule" and image_type == "ct" and body_part in ["chest", "lung"]:
            return self._simulate_lung_nodule_result(preprocessed_data)
        elif model["type"] == "brain_tumor" and image_type == "mri" and body_part == "brain":
            return self._simulate_brain_tumor_result(preprocessed_data)
        elif model["type"] == "xray_classifier" and image_type == "xray" and body_part == "chest":
            return self._simulate_xray_classifier_result(preprocessed_data)
        else:
            # 返回一个空结果
            return {
                "findings": [],
                "summary": "No relevant findings for this model and image combination"
            }

    def _simulate_lung_nodule_result(self, image_data):
        """模拟肺结节检测结果"""
        # 在实际项目中，这里应该运行真实的肺结节检测模型
        # 这里仅作示例，生成一些模拟数据
        
        # 生成一个随机数，决定是否"检测到"结节
        has_nodule = np.random.random() > 0.5
        
        if has_nodule:
            # 模拟检测到1-3个结节
            nodule_count = np.random.randint(1, 4)
            findings = []
            
            for i in range(nodule_count):
                # 随机位置
                slice_idx = np.random.randint(0, max(1, image_data.shape[0] - 1))
                x = np.random.randint(100, 400)
                y = np.random.randint(100, 400)
                
                # 随机大小
                width = np.random.uniform(5.0, 15.0)
                height = np.random.uniform(5.0, 15.0)
                
                # 随机置信度
                confidence = np.random.uniform(0.7, 0.98)
                
                # 根据大小确定严重程度
                severity = "low"
                if width > 10:
                    severity = "moderate"
                if width > 12:
                    severity = "high"
                
                findings.append({
                    "type": "nodule",
                    "location": {
                        "slice": slice_idx,
                        "x": x,
                        "y": y
                    },
                    "dimensions": {
                        "width_mm": round(width, 1),
                        "height_mm": round(height, 1)
                    },
                    "confidence": round(confidence, 2),
                    "severity": severity,
                    "description": f"Potential pulmonary nodule detected"
                })
            
            summary = f"{nodule_count} potential {'nodule' if nodule_count == 1 else 'nodules'} found"
        else:
            findings = []
            summary = "No pulmonary nodules detected"
        
        return {
            "findings": findings,
            "summary": summary
        }

    def _simulate_brain_tumor_result(self, image_data):
        """模拟脑肿瘤分割结果"""
        # 在实际项目中，这里应该运行真实的脑肿瘤分割模型
        # 这里仅作示例，生成一些模拟数据
        
        # 生成一个随机数，决定是否"检测到"肿瘤
        has_tumor = np.random.random() > 0.7
        
        if has_tumor:
            # 随机位置
            x = np.random.randint(100, 150)
            y = np.random.randint(100, 150)
            z = np.random.randint(10, 30)
            
            # 随机体积
            volume_ml = np.random.uniform(2.0, 20.0)
            
            # 随机类型
            tumor_types = ["meningioma", "glioma", "pituitary"]
            tumor_type = np.random.choice(tumor_types)
            
            # 随机置信度
            confidence = np.random.uniform(0.75, 0.95)
            
            findings = [{
                "type": tumor_type,
                "location": {
                    "x_center": x,
                    "y_center": y,
                    "z_center": z
                },
                "volume_ml": round(volume_ml, 1),
                "confidence": round(confidence, 2),
                "description": f"Potential {tumor_type} tumor detected"
            }]
            
            summary = f"Potential {tumor_type} detected with {int(confidence*100)}% confidence"
        else:
            findings = []
            summary = "No brain tumor detected"
        
        return {
            "findings": findings,
            "summary": summary
        }

    def _simulate_xray_classifier_result(self, image_data):
        """模拟X光分类结果"""
        # 在实际项目中，这里应该运行真实的X光分类模型
        # 这里仅作示例，生成一些模拟数据
        
        # 可能的病症列表
        conditions = ["normal", "pneumonia", "covid-19", "tuberculosis", "pleural_effusion"]
        
        # 随机选择一个病症
        condition = np.random.choice(conditions)
        
        # 随机置信度
        confidence = np.random.uniform(0.7, 0.98)
        
        if condition == "normal":
            description = "No abnormalities detected"
        else:
            description = f"Findings consistent with {condition.replace('_', ' ')}"
        
        findings = [{
            "condition": condition,
            "confidence": round(confidence, 2),
            "description": description
        }]
        
        return {
            "findings": findings,
            "summary": description
        }

    def _save_results(self, file_path: str, image_type: str, body_part: str, 
                     results: Dict) -> str:
        """保存处理结果到数据库并返回结果ID"""
        # 生成结果ID
        result_id = str(uuid.uuid4())
        
        # 创建结果文档
        result_doc = {
            "result_id": result_id,
            "file_path": file_path,
            "image_type": image_type,
            "body_part": body_part,
            "processed_at": time.time(),
            "results": results
        }
        
        # 保存到MongoDB
        results_collection.insert_one(result_doc)
        
        # 同时保存一份到Redis缓存，方便快速查询
        # 设置1小时过期
        redis_client.setex(
            f"result:{result_id}", 
            3600,
            str(result_doc)
        )
        
        logger.info(f"Saved results with ID: {result_id}")
        
        return result_id

    def get_result(self, result_id: str) -> Optional[Dict]:
        """获取处理结果"""
        # 先尝试从Redis获取
        cached_result = redis_client.get(f"result:{result_id}")
        if cached_result:
            # 将字符串转回字典
            import ast
            return ast.literal_eval(cached_result.decode("utf-8"))
        
        # 如果Redis没有，从MongoDB获取
        result_doc = results_collection.find_one({"result_id": result_id})
        if result_doc:
            # 移除MongoDB的_id字段
            if "_id" in result_doc:
                del result_doc["_id"]
            return result_doc
        
        return None

    def delete_image_and_results(self, image_id: str) -> bool:
        """删除影像和相关结果"""
        try:
            # 获取影像信息
            image_doc = images_collection.find_one({"image_id": image_id})
            if not image_doc:
                logger.warning(f"Image {image_id} not found")
                return False
            
            # 删除文件
            file_path = image_doc.get("file_path")
            if file_path and os.path.exists(file_path):
                os.remove(file_path)
                logger.info(f"Deleted file: {file_path}")
            
            # 删除MongoDB中的记录
            images_collection.delete_one({"image_id": image_id})
            
            # 删除相关的处理结果
            results_collection.delete_many({"file_path": file_path})
            
            # 从Redis缓存中删除
            redis_client.delete(f"image:{image_id}")
            
            logger.info(f"Successfully deleted image {image_id} and related results")
            
            return True
        except Exception as e:
            logger.error(f"Error deleting image {image_id}: {str(e)}")
            return False

def process_batch(image_ids: List[str], model_ids: List[str], 
                 processor: ImageProcessor) -> Dict:
    """
    批量处理多个影像
    
    Args:
        image_ids: 影像ID列表
        model_ids: 要应用的模型ID列表
        processor: ImageProcessor实例
        
    Returns:
        批处理结果
    """
    batch_id = str(uuid.uuid4())
    total = len(image_ids)
    successful = 0
    failed = 0
    failed_ids = []
    results = {}
    
    for image_id in image_ids:
        try:
            # 获取影像信息
            image_doc = images_collection.find_one({"image_id": image_id})
            if not image_doc:
                logger.warning(f"Image {image_id} not found")
                failed += 1
                failed_ids.append({"image_id": image_id, "error": "Image not found"})
                continue
            
            # 处理影像
            file_path = image_doc.get("file_path")
            image_type = image_doc.get("image_type")
            body_part = image_doc.get("body_part")
            
            result = processor.process_image(file_path, image_type, body_part, model_ids)
            
            if result.get("status") == "success":
                successful += 1
                results[image_id] = result.get("result_id")
            else:
                failed += 1
                failed_ids.append({"image_id": image_id, "error": result.get("error")})
                
        except Exception as e:
            logger.error(f"Error processing image {image_id}: {str(e)}")
            failed += 1
            failed_ids.append({"image_id": image_id, "error": str(e)})
    
    # 保存批处理结果
    batch_result = {
        "batch_id": batch_id,
        "total": total,
        "successful": successful,
        "failed": failed,
        "results": results,
        "failed_details": failed_ids,
        "created_at": time.time()
    }
    
    # 保存到MongoDB
    db.batch_results.insert_one(batch_result)
    
    return {
        "batch_id": batch_id,
        "status": "completed",
        "total": total,
        "successful": successful,
        "failed": failed
    }

# 实例化处理器（单例模式）
default_processor = None

def get_processor(config=None):
    """获取处理器单例"""
    global default_processor
    if default_processor is None:
        default_processor = ImageProcessor(config)
    return default_processor
