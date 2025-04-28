# tdd_example_code.py - 测试驱动开发示例
# 本文件展示如何使用TDD方法实现医疗数据验证服务中的患者ID验证规则

# 第一步：编写测试用例（使用pytest测试框架）

# 文件: test_patient_id_validator.py
import pytest
import re
import sys
import os
from datetime import datetime

# 导入模块的代码 - 在实际实现中需要处理导入路径
# 此时这些模块尚未实现

"""
测试患者ID验证器
"""
def test_valid_patient_id_format():
    """测试有效的患者ID格式"""
    from validators.patient_id_validator import validate_patient_id
    
    # 有效的患者ID：以P开头，后跟8位数字
    assert validate_patient_id("P12345678") == True
    assert validate_patient_id("P00000001") == True
    assert validate_patient_id("P99999999") == True

def test_reject_without_p_prefix():
    """测试无P前缀的患者ID"""
    from validators.patient_id_validator import validate_patient_id
    
    assert validate_patient_id("12345678") == False
    assert validate_patient_id("A12345678") == False

def test_reject_incorrect_length():
    """测试长度不正确的患者ID"""
    from validators.patient_id_validator import validate_patient_id
    
    assert validate_patient_id("P1234567") == False   # 太短
    assert validate_patient_id("P123456789") == False # 太长

def test_reject_non_numeric_after_p():
    """测试P后包含非数字字符的患者ID"""
    from validators.patient_id_validator import validate_patient_id
    
    assert validate_patient_id("PABCDEFGH") == False
    assert validate_patient_id("P1234567A") == False
    assert validate_patient_id("P-1234567") == False

def test_reject_null_or_none():
    """测试空值患者ID"""
    from validators.patient_id_validator import validate_patient_id
    
    assert validate_patient_id(None) == False

def test_handle_empty_string():
    """测试空字符串患者ID"""
    from validators.patient_id_validator import validate_patient_id
    
    assert validate_patient_id("") == False

def test_handle_patient_id_with_spaces():
    """测试包含空格的患者ID"""
    from validators.patient_id_validator import validate_patient_id
    
    assert validate_patient_id("P 1234567") == False
    assert validate_patient_id(" P12345678") == False
    assert validate_patient_id("P12345678 ") == False


# 第二步：运行测试，此时所有测试应该失败，因为我们尚未实现验证函数

# 第三步：实现最小可行的验证函数，使测试通过

# 文件: validators/patient_id_validator.py
"""
患者ID验证模块
用于验证患者ID是否符合格式要求（以P开头，后跟8位数字）
"""
import re

def validate_patient_id(patient_id):
    """
    验证患者ID是否符合格式要求（以P开头，后跟8位数字）
    
    Args:
        patient_id (str): 要验证的患者ID
        
    Returns:
        bool: 验证是否通过
    """
    # 如果patient_id为None，返回False
    if patient_id is None:
        return False
    
    # 使用正则表达式验证格式：P开头，后跟8位数字
    patient_id_regex = r"^P\d{8}$"
    return bool(re.match(patient_id_regex, patient_id))


# 第四步：将这个验证器集成到更广泛的验证框架中

# 文件: validators/__init__.py
"""
验证规则定义模块
包含各种验证规则的定义
"""
from validators.patient_id_validator import validate_patient_id

# 创建一个规则定义，符合前面规格中的ValidationRule格式
patient_id_rule = {
    "id": "PATIENT_ID_FORMAT",
    "name": "患者ID格式验证",
    "description": "验证患者ID是否符合指定格式：以P开头，后跟8位数字",
    "category": "患者数据",
    "severity": "error",
    "validation_fn": lambda data: {
        # 如果数据中没有patient_id字段，返回错误
        "is_valid": False,
        "error": {
            "path": "patient_id",
            "message": "患者ID是必填字段"
        }
    } if "patient_id" not in data else {
        # 使用前面定义的验证函数
        "is_valid": validate_patient_id(data["patient_id"]),
        "error": None if validate_patient_id(data["patient_id"]) else {
            "path": "patient_id",
            "value": data["patient_id"],
            "message": "患者ID格式不正确，应为P开头后跟8位数字"
        }
    },
    "dependencies": [],
    "error_message": "患者ID格式不正确，应为P开头后跟8位数字",
    "version": "1.0.0"
}

rules = {
    "PATIENT_ID_FORMAT": patient_id_rule
}


# 第五步：编写集成测试，测试规则在验证器框架中的使用

# 文件: test_medical_data_validator.py
"""
医疗数据验证器集成测试
测试患者ID验证规则在验证框架中的使用
"""
import pytest
from medical_data_validator import MedicalDataValidator
from validators import rules

@pytest.fixture
def validator():
    """创建一个配置好的验证器实例"""
    validator = MedicalDataValidator()
    validator.register_rule(rules["PATIENT_ID_FORMAT"])
    return validator

def test_validate_correct_patient_id(validator):
    """测试验证正确的患者ID"""
    data = {
        "patient_id": "P12345678",
        "name": "张三"
    }
    
    result = validator.validate(data, ["PATIENT_ID_FORMAT"])
    assert result["is_valid"] == True
    assert len(result["errors"]) == 0

def test_reject_incorrect_patient_id(validator):
    """测试拒绝不正确的患者ID"""
    data = {
        "patient_id": "12345678",  # 缺少P前缀
        "name": "张三"
    }
    
    result = validator.validate(data, ["PATIENT_ID_FORMAT"])
    assert result["is_valid"] == False
    assert len(result["errors"]) == 1
    assert result["errors"][0]["rule_id"] == "PATIENT_ID_FORMAT"
    assert result["errors"][0]["path"] == "patient_id"

def test_reject_data_without_patient_id(validator):
    """测试拒绝没有患者ID的数据"""
    data = {
        "name": "张三"
    }
    
    result = validator.validate(data, ["PATIENT_ID_FORMAT"])
    assert result["is_valid"] == False
    assert len(result["errors"]) == 1
    assert result["errors"][0]["rule_id"] == "PATIENT_ID_FORMAT"
    assert result["errors"][0]["path"] == "patient_id"


# 第六步：实现验证器框架的基本结构（为了使集成测试通过）

# 文件: medical_data_validator.py
"""
医疗数据验证器类
用于验证医疗数据是否符合预定义的规则
"""
from datetime import datetime

class MedicalDataValidator:
    """
    医疗数据验证器类
    用于验证医疗数据是否符合预定义的规则
    """
    
    def __init__(self):
        """初始化验证器"""
        self.rules = {}
    
    def register_rule(self, rule):
        """
        注册验证规则
        
        Args:
            rule (dict): 验证规则对象
        """
        self.rules[rule["id"]] = rule
    
    def validate(self, data, rule_ids, options=None):
        """
        验证数据
        
        Args:
            data (dict): 待验证的数据
            rule_ids (list): 要应用的规则ID列表
            options (dict, optional): 验证选项. Defaults to None.
            
        Returns:
            dict: 验证结果
        """
        if options is None:
            options = {}
            
        import time
        start_time = time.time()
        errors = []
        warnings = []
        applied_rules = []
        
        # 依次应用每个规则
        for rule_id in rule_ids:
            rule = self.rules.get(rule_id)
            
            # 如果规则不存在，跳过
            if not rule:
                continue
            
            applied_rules.append(rule_id)
            
            try:
                # 执行验证函数
                result = rule["validation_fn"](data)
                
                # 如果验证失败，添加错误
                if not result["is_valid"] and result["error"]:
                    error = {
                        "rule_id": rule["id"],
                        "path": result["error"]["path"],
                        "value": result["error"].get("value"),
                        "message": result["error"].get("message") or rule["error_message"],
                        "severity": rule["severity"]
                    }
                    
                    if rule["severity"] == "warning":
                        warnings.append(error)
                    else:
                        errors.append(error)
            except Exception as err:
                # 捕获验证过程中的异常
                errors.append({
                    "rule_id": rule["id"],
                    "path": "",
                    "message": f"验证过程发生错误: {str(err)}",
                    "severity": "error"
                })
        
        # 生成验证结果
        return {
            "is_valid": len(errors) == 0,
            "errors": errors,
            "warnings": warnings,
            "metadata": {
                "validated_at": datetime.now(),
                "duration": time.time() - start_time,
                "rules_applied": applied_rules
            }
        }

# 第七步：运行所有测试，确保它们通过

# 第八步：重构代码，提高可维护性和性能
# 这一步通常会在测试通过后进行，以改进代码的质量
# 由于这是一个示例，我们省略了具体的重构步骤

# 测试驱动开发的迭代过程：
# 1. 编写失败的测试 -> 2. 实现最小可行代码使测试通过 -> 3. 重构代码 -> 回到步骤1
# 这个过程被称为"红-绿-重构"循环

# 通过TDD方法，我们首先明确了患者ID验证的规则和期望行为
# 然后才开始实现代码，确保实现满足所有测试要求
# 这种方式有助于确保代码质量和功能正确性 