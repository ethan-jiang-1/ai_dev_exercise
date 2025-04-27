// tdd_example_code_java.java - 测试驱动开发示例
// 本文件展示如何使用TDD方法实现医疗数据验证服务中的患者ID验证规则

// 第一步：编写测试用例（使用JUnit测试框架）

// PatientIdValidatorTest.java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Date;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

/**
 * 患者ID验证器的测试类
 */
public class PatientIdValidatorTest {
    
    @Test
    public void testValidPatientIdFormat() {
        // 有效的患者ID：以P开头，后跟8位数字
        assertTrue(PatientIdValidator.validatePatientId("P12345678"));
        assertTrue(PatientIdValidator.validatePatientId("P00000001"));
        assertTrue(PatientIdValidator.validatePatientId("P99999999"));
    }
    
    @Test
    public void testRejectWithoutPPrefix() {
        // 无P前缀的患者ID
        assertFalse(PatientIdValidator.validatePatientId("12345678"));
        assertFalse(PatientIdValidator.validatePatientId("A12345678"));
    }
    
    @Test
    public void testRejectIncorrectLength() {
        // 长度不正确的患者ID
        assertFalse(PatientIdValidator.validatePatientId("P1234567"));   // 太短
        assertFalse(PatientIdValidator.validatePatientId("P123456789")); // 太长
    }
    
    @Test
    public void testRejectNonNumericAfterP() {
        // P后包含非数字字符的患者ID
        assertFalse(PatientIdValidator.validatePatientId("PABCDEFGH"));
        assertFalse(PatientIdValidator.validatePatientId("P1234567A"));
        assertFalse(PatientIdValidator.validatePatientId("P-1234567"));
    }
    
    @Test
    public void testRejectNullValue() {
        // 空值患者ID
        assertFalse(PatientIdValidator.validatePatientId(null));
    }
    
    @Test
    public void testHandleEmptyString() {
        // 空字符串患者ID
        assertFalse(PatientIdValidator.validatePatientId(""));
    }
    
    @Test
    public void testHandlePatientIdWithSpaces() {
        // 包含空格的患者ID
        assertFalse(PatientIdValidator.validatePatientId("P 1234567"));
        assertFalse(PatientIdValidator.validatePatientId(" P12345678"));
        assertFalse(PatientIdValidator.validatePatientId("P12345678 "));
    }
}

// 第二步：运行测试，此时所有测试应该失败，因为我们尚未实现验证函数

// 第三步：实现最小可行的验证函数，使测试通过

// PatientIdValidator.java
/**
 * 患者ID验证类
 * 用于验证患者ID是否符合格式要求（以P开头，后跟8位数字）
 */
public class PatientIdValidator {
    
    /**
     * 验证患者ID是否符合格式要求（以P开头，后跟8位数字）
     * 
     * @param patientId 要验证的患者ID
     * @return 验证是否通过
     */
    public static boolean validatePatientId(String patientId) {
        // 如果patientId为null，返回false
        if (patientId == null) {
            return false;
        }
        
        // 使用正则表达式验证格式：P开头，后跟8位数字
        String patternString = "^P\\d{8}$";
        Pattern pattern = Pattern.compile(patternString);
        return pattern.matcher(patientId).matches();
    }
}

// 第四步：将这个验证器集成到更广泛的验证框架中

// ValidationRule.java
/**
 * 验证规则接口
 */
public interface ValidationRule {
    String getId();
    String getName();
    String getDescription();
    String getCategory();
    String getSeverity();
    ValidationResult validate(Map<String, Object> data);
    List<String> getDependencies();
    String getErrorMessage();
    String getVersion();
}

// ValidationResult.java
/**
 * 验证结果类
 */
public class ValidationResult {
    private boolean isValid;
    private ValidationError error;
    
    public ValidationResult(boolean isValid, ValidationError error) {
        this.isValid = isValid;
        this.error = error;
    }
    
    public boolean isValid() {
        return isValid;
    }
    
    public ValidationError getError() {
        return error;
    }
}

// ValidationError.java
/**
 * 验证错误类
 */
public class ValidationError {
    private String path;
    private Object value;
    private String message;
    
    public ValidationError(String path, Object value, String message) {
        this.path = path;
        this.value = value;
        this.message = message;
    }
    
    public String getPath() {
        return path;
    }
    
    public Object getValue() {
        return value;
    }
    
    public String getMessage() {
        return message;
    }
}

// PatientIdFormatRule.java
/**
 * 患者ID格式验证规则
 */
public class PatientIdFormatRule implements ValidationRule {
    
    @Override
    public String getId() {
        return "PATIENT_ID_FORMAT";
    }
    
    @Override
    public String getName() {
        return "患者ID格式验证";
    }
    
    @Override
    public String getDescription() {
        return "验证患者ID是否符合指定格式：以P开头，后跟8位数字";
    }
    
    @Override
    public String getCategory() {
        return "患者数据";
    }
    
    @Override
    public String getSeverity() {
        return "error";
    }
    
    @Override
    public ValidationResult validate(Map<String, Object> data) {
        // 如果数据中没有patientId字段，返回错误
        if (!data.containsKey("patientId")) {
            return new ValidationResult(false, 
                new ValidationError("patientId", null, "患者ID是必填字段"));
        }
        
        String patientId = (String) data.get("patientId");
        boolean isValid = PatientIdValidator.validatePatientId(patientId);
        
        // 返回验证结果
        if (isValid) {
            return new ValidationResult(true, null);
        } else {
            return new ValidationResult(false, 
                new ValidationError("patientId", patientId, "患者ID格式不正确，应为P开头后跟8位数字"));
        }
    }
    
    @Override
    public List<String> getDependencies() {
        return new ArrayList<>();
    }
    
    @Override
    public String getErrorMessage() {
        return "患者ID格式不正确，应为P开头后跟8位数字";
    }
    
    @Override
    public String getVersion() {
        return "1.0.0";
    }
}

// 第五步：编写集成测试，测试规则在验证器框架中的使用

// MedicalDataValidatorTest.java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.Map;
import java.util.HashMap;
import java.util.Arrays;

/**
 * 医疗数据验证器的集成测试
 */
public class MedicalDataValidatorTest {
    
    private MedicalDataValidator validator;
    
    @BeforeEach
    public void setUp() {
        // 为每个测试创建一个新的验证器实例
        validator = new MedicalDataValidator();
        // 注册患者ID验证规则
        validator.registerRule(new PatientIdFormatRule());
    }
    
    @Test
    public void testValidateCorrectPatientId() {
        Map<String, Object> data = new HashMap<>();
        data.put("patientId", "P12345678");
        data.put("name", "张三");
        
        MedicalValidationResult result = validator.validate(data, 
            Arrays.asList("PATIENT_ID_FORMAT"));
        
        assertTrue(result.isValid());
        assertEquals(0, result.getErrors().size());
    }
    
    @Test
    public void testRejectIncorrectPatientId() {
        Map<String, Object> data = new HashMap<>();
        data.put("patientId", "12345678"); // 缺少P前缀
        data.put("name", "张三");
        
        MedicalValidationResult result = validator.validate(data, 
            Arrays.asList("PATIENT_ID_FORMAT"));
        
        assertFalse(result.isValid());
        assertEquals(1, result.getErrors().size());
        assertEquals("PATIENT_ID_FORMAT", result.getErrors().get(0).getRuleId());
        assertEquals("patientId", result.getErrors().get(0).getPath());
    }
    
    @Test
    public void testRejectDataWithoutPatientId() {
        Map<String, Object> data = new HashMap<>();
        data.put("name", "张三");
        
        MedicalValidationResult result = validator.validate(data, 
            Arrays.asList("PATIENT_ID_FORMAT"));
        
        assertFalse(result.isValid());
        assertEquals(1, result.getErrors().size());
        assertEquals("PATIENT_ID_FORMAT", result.getErrors().get(0).getRuleId());
        assertEquals("patientId", result.getErrors().get(0).getPath());
    }
}

// 第六步：实现验证器框架的基本结构（为了使集成测试通过）

// MedicalDataValidator.java
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;
import java.util.Date;

/**
 * 医疗数据验证器类
 * 用于验证医疗数据是否符合预定义的规则
 */
public class MedicalDataValidator {
    
    private Map<String, ValidationRule> rules;
    
    /**
     * 构造函数
     */
    public MedicalDataValidator() {
        this.rules = new HashMap<>();
    }
    
    /**
     * 注册验证规则
     * 
     * @param rule 验证规则对象
     */
    public void registerRule(ValidationRule rule) {
        this.rules.put(rule.getId(), rule);
    }
    
    /**
     * 验证数据
     * 
     * @param data 待验证的数据
     * @param ruleIds 要应用的规则ID列表
     * @return 验证结果
     */
    public MedicalValidationResult validate(Map<String, Object> data, List<String> ruleIds) {
        return validate(data, ruleIds, new HashMap<>());
    }
    
    /**
     * 验证数据（带选项）
     * 
     * @param data 待验证的数据
     * @param ruleIds 要应用的规则ID列表
     * @param options 验证选项
     * @return 验证结果
     */
    public MedicalValidationResult validate(Map<String, Object> data, List<String> ruleIds, 
                                          Map<String, Object> options) {
        long startTime = System.currentTimeMillis();
        List<MedicalValidationError> errors = new ArrayList<>();
        List<MedicalValidationError> warnings = new ArrayList<>();
        List<String> appliedRules = new ArrayList<>();
        
        // 依次应用每个规则
        for (String ruleId : ruleIds) {
            ValidationRule rule = this.rules.get(ruleId);
            
            // 如果规则不存在，跳过
            if (rule == null) {
                continue;
            }
            
            appliedRules.add(ruleId);
            
            try {
                // 执行验证函数
                ValidationResult result = rule.validate(data);
                
                // 如果验证失败，添加错误
                if (!result.isValid() && result.getError() != null) {
                    MedicalValidationError error = new MedicalValidationError(
                        rule.getId(),
                        result.getError().getPath(),
                        result.getError().getValue(),
                        result.getError().getMessage() != null ? 
                            result.getError().getMessage() : rule.getErrorMessage(),
                        rule.getSeverity()
                    );
                    
                    if ("warning".equals(rule.getSeverity())) {
                        warnings.add(error);
                    } else {
                        errors.add(error);
                    }
                }
            } catch (Exception e) {
                // 捕获验证过程中的异常
                errors.add(new MedicalValidationError(
                    rule.getId(),
                    "",
                    null,
                    "验证过程发生错误: " + e.getMessage(),
                    "error"
                ));
            }
        }
        
        // 生成验证结果
        MedicalValidationMetadata metadata = new MedicalValidationMetadata(
            new Date(),
            System.currentTimeMillis() - startTime,
            appliedRules
        );
        
        return new MedicalValidationResult(
            errors.isEmpty(),
            errors,
            warnings,
            metadata
        );
    }
}

// MedicalValidationResult.java
import java.util.List;

/**
 * 医疗数据验证结果类
 */
public class MedicalValidationResult {
    private boolean isValid;
    private List<MedicalValidationError> errors;
    private List<MedicalValidationError> warnings;
    private MedicalValidationMetadata metadata;
    
    /**
     * 构造函数
     * 
     * @param isValid 是否有效
     * @param errors 错误列表
     * @param warnings 警告列表
     * @param metadata 元数据
     */
    public MedicalValidationResult(boolean isValid, List<MedicalValidationError> errors,
                                  List<MedicalValidationError> warnings,
                                  MedicalValidationMetadata metadata) {
        this.isValid = isValid;
        this.errors = errors;
        this.warnings = warnings;
        this.metadata = metadata;
    }
    
    public boolean isValid() {
        return isValid;
    }
    
    public List<MedicalValidationError> getErrors() {
        return errors;
    }
    
    public List<MedicalValidationError> getWarnings() {
        return warnings;
    }
    
    public MedicalValidationMetadata getMetadata() {
        return metadata;
    }
}

// MedicalValidationError.java
/**
 * 医疗数据验证错误类
 */
public class MedicalValidationError {
    private String ruleId;
    private String path;
    private Object value;
    private String message;
    private String severity;
    
    /**
     * 构造函数
     * 
     * @param ruleId 规则ID
     * @param path 错误路径
     * @param value 错误值
     * @param message 错误消息
     * @param severity 严重程度
     */
    public MedicalValidationError(String ruleId, String path, Object value,
                                 String message, String severity) {
        this.ruleId = ruleId;
        this.path = path;
        this.value = value;
        this.message = message;
        this.severity = severity;
    }
    
    public String getRuleId() {
        return ruleId;
    }
    
    public String getPath() {
        return path;
    }
    
    public Object getValue() {
        return value;
    }
    
    public String getMessage() {
        return message;
    }
    
    public String getSeverity() {
        return severity;
    }
}

// MedicalValidationMetadata.java
import java.util.Date;
import java.util.List;

/**
 * 医疗数据验证元数据类
 */
public class MedicalValidationMetadata {
    private Date validatedAt;
    private long duration;
    private List<String> rulesApplied;
    
    /**
     * 构造函数
     * 
     * @param validatedAt 验证时间
     * @param duration 验证耗时（毫秒）
     * @param rulesApplied 应用的规则ID列表
     */
    public MedicalValidationMetadata(Date validatedAt, long duration,
                                    List<String> rulesApplied) {
        this.validatedAt = validatedAt;
        this.duration = duration;
        this.rulesApplied = rulesApplied;
    }
    
    public Date getValidatedAt() {
        return validatedAt;
    }
    
    public long getDuration() {
        return duration;
    }
    
    public List<String> getRulesApplied() {
        return rulesApplied;
    }
}

// 第七步：运行所有测试，确保它们通过

// 第八步：重构代码，提高可维护性和性能
// 这一步通常会在测试通过后进行，以改进代码的质量
// 由于这是一个示例，我们省略了具体的重构步骤

/*
 * 测试驱动开发的迭代过程：
 * 1. 编写失败的测试 -> 2. 实现最小可行代码使测试通过 -> 3. 重构代码 -> 回到步骤1
 * 这个过程被称为"红-绿-重构"循环
 *
 * 通过TDD方法，我们首先明确了患者ID验证的规则和期望行为
 * 然后才开始实现代码，确保实现满足所有测试要求
 * 这种方式有助于确保代码质量和功能正确性
 */ 