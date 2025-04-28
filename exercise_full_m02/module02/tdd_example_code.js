// tdd_example_code.js - 测试驱动开发示例
// 本文件展示如何使用TDD方法实现医疗数据验证服务中的患者ID验证规则

// 第一步：编写测试用例（使用Jest测试框架）

// patientIdValidator.test.js
describe('Patient ID Validator', () => {
  // 引入待测试的模块（此时该模块尚未实现）
  const { validatePatientId } = require('./validators/patientIdValidator');

  test('should accept valid patient ID format', () => {
    // 有效的患者ID：以P开头，后跟8位数字
    expect(validatePatientId('P12345678')).toBe(true);
    expect(validatePatientId('P00000001')).toBe(true);
    expect(validatePatientId('P99999999')).toBe(true);
  });

  test('should reject patient ID without P prefix', () => {
    expect(validatePatientId('12345678')).toBe(false);
    expect(validatePatientId('A12345678')).toBe(false);
  });

  test('should reject patient ID with incorrect length', () => {
    expect(validatePatientId('P1234567')).toBe(false);   // 太短
    expect(validatePatientId('P123456789')).toBe(false); // 太长
  });

  test('should reject patient ID with non-numeric characters after P', () => {
    expect(validatePatientId('PABCDEFGH')).toBe(false);
    expect(validatePatientId('P1234567A')).toBe(false);
    expect(validatePatientId('P-1234567')).toBe(false);
  });

  test('should reject null or undefined patient ID', () => {
    expect(validatePatientId(null)).toBe(false);
    expect(validatePatientId(undefined)).toBe(false);
  });

  test('should handle empty string patient ID', () => {
    expect(validatePatientId('')).toBe(false);
  });

  test('should handle patient ID with spaces', () => {
    expect(validatePatientId('P 1234567')).toBe(false);
    expect(validatePatientId(' P12345678')).toBe(false);
    expect(validatePatientId('P12345678 ')).toBe(false);
  });
});

// 第二步：运行测试，此时所有测试应该失败，因为我们尚未实现验证函数

// 第三步：实现最小可行的验证函数，使测试通过

// validators/patientIdValidator.js
/**
 * 验证患者ID是否符合格式要求（以P开头，后跟8位数字）
 * @param {string} patientId - 要验证的患者ID
 * @returns {boolean} - 验证是否通过
 */
function validatePatientId(patientId) {
  // 如果patientId为null或undefined，返回false
  if (patientId == null) {
    return false;
  }
  
  // 使用正则表达式验证格式：P开头，后跟8位数字
  const patientIdRegex = /^P\d{8}$/;
  return patientIdRegex.test(patientId);
}

module.exports = {
  validatePatientId
};

// 第四步：将这个验证器集成到更广泛的验证框架中

// validators/index.js
const { validatePatientId } = require('./patientIdValidator');

// 创建一个规则定义，符合前面规格中的ValidationRule格式
const patientIdRule = {
  id: 'PATIENT_ID_FORMAT',
  name: '患者ID格式验证',
  description: '验证患者ID是否符合指定格式：以P开头，后跟8位数字',
  category: '患者数据',
  severity: 'error',
  validationFn: (data) => {
    // 如果数据中没有patientId字段，返回错误
    if (!data.patientId) {
      return {
        isValid: false,
        error: {
          path: 'patientId',
          message: '患者ID是必填字段'
        }
      };
    }
    
    // 使用前面定义的验证函数
    const isValid = validatePatientId(data.patientId);
    
    // 返回验证结果
    return {
      isValid,
      error: isValid ? null : {
        path: 'patientId',
        value: data.patientId,
        message: '患者ID格式不正确，应为P开头后跟8位数字'
      }
    };
  },
  dependencies: [],
  errorMessage: '患者ID格式不正确，应为P开头后跟8位数字',
  version: '1.0.0'
};

module.exports = {
  rules: {
    PATIENT_ID_FORMAT: patientIdRule
  },
  validatePatientId
};

// 第五步：编写集成测试，测试规则在验证器框架中的使用

// medicalDataValidator.test.js
describe('Medical Data Validator - Patient ID integration', () => {
  const { MedicalDataValidator } = require('./MedicalDataValidator');
  const { rules } = require('./validators');
  
  let validator;
  
  beforeEach(() => {
    // 为每个测试创建一个新的验证器实例
    validator = new MedicalDataValidator();
    // 注册患者ID验证规则
    validator.registerRule(rules.PATIENT_ID_FORMAT);
  });
  
  test('should validate data with correct patient ID', () => {
    const data = {
      patientId: 'P12345678',
      name: '张三'
    };
    
    const result = validator.validate(data, ['PATIENT_ID_FORMAT']);
    expect(result.isValid).toBe(true);
    expect(result.errors).toHaveLength(0);
  });
  
  test('should reject data with incorrect patient ID', () => {
    const data = {
      patientId: '12345678', // 缺少P前缀
      name: '张三'
    };
    
    const result = validator.validate(data, ['PATIENT_ID_FORMAT']);
    expect(result.isValid).toBe(false);
    expect(result.errors).toHaveLength(1);
    expect(result.errors[0].ruleId).toBe('PATIENT_ID_FORMAT');
    expect(result.errors[0].path).toBe('patientId');
  });
  
  test('should reject data without patient ID', () => {
    const data = {
      name: '张三'
    };
    
    const result = validator.validate(data, ['PATIENT_ID_FORMAT']);
    expect(result.isValid).toBe(false);
    expect(result.errors).toHaveLength(1);
    expect(result.errors[0].ruleId).toBe('PATIENT_ID_FORMAT');
    expect(result.errors[0].path).toBe('patientId');
  });
});

// 第六步：实现验证器框架的基本结构（为了使集成测试通过）

// MedicalDataValidator.js
/**
 * 医疗数据验证器类
 * 用于验证医疗数据是否符合预定义的规则
 */
class MedicalDataValidator {
  constructor() {
    this.rules = {};
  }
  
  /**
   * 注册验证规则
   * @param {Object} rule - 验证规则对象
   */
  registerRule(rule) {
    this.rules[rule.id] = rule;
  }
  
  /**
   * 验证数据
   * @param {Object} data - 待验证的数据
   * @param {Array<string>} ruleIds - 要应用的规则ID列表
   * @param {Object} options - 验证选项
   * @returns {Object} - 验证结果
   */
  validate(data, ruleIds, options = {}) {
    const startTime = Date.now();
    const errors = [];
    const warnings = [];
    const appliedRules = [];
    
    // 依次应用每个规则
    for (const ruleId of ruleIds) {
      const rule = this.rules[ruleId];
      
      // 如果规则不存在，跳过
      if (!rule) {
        continue;
      }
      
      appliedRules.push(ruleId);
      
      try {
        // 执行验证函数
        const result = rule.validationFn(data);
        
        // 如果验证失败，添加错误
        if (!result.isValid && result.error) {
          const error = {
            ruleId: rule.id,
            path: result.error.path,
            value: result.error.value,
            message: result.error.message || rule.errorMessage,
            severity: rule.severity
          };
          
          if (rule.severity === 'warning') {
            warnings.push(error);
          } else {
            errors.push(error);
          }
        }
      } catch (err) {
        // 捕获验证过程中的异常
        errors.push({
          ruleId: rule.id,
          path: '',
          message: `验证过程发生错误: ${err.message}`,
          severity: 'error'
        });
      }
    }
    
    // 生成验证结果
    return {
      isValid: errors.length === 0,
      errors,
      warnings,
      metadata: {
        validatedAt: new Date(),
        duration: Date.now() - startTime,
        rulesApplied: appliedRules
      }
    };
  }
}

module.exports = {
  MedicalDataValidator
};

// 第七步：运行所有测试，确保它们通过

// 第八步：重构代码，提高可维护性和性能
// 这一步通常会在测试通过后进行，以改进代码的质量
// 由于这是一个示例，我们省略了具体的重构步骤

// 测试驱动开发的迭代过程：
// 1. 编写失败的测试 -> 2. 实现最小可行代码使测试通过 -> 3. 重构代码 -> 回到步骤1
// 这个过程被称为"红-绿-重构"循环

// 通过TDD方法，我们首先明确了患者ID验证的规则和期望行为
// 然后才开始实现代码，确保实现满足所有测试要求
// 这种方式有助于确保代码质量和功能正确性 