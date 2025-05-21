# 基础代谢率(BMR)计算器 - 验证思路

## 1. 测试策略概述

### 1.1 测试范围
- PersonData数据类的验证
- 输入数据验证功能
- BMR计算功能
- 异常处理机制

### 1.2 测试级别
- 单元测试：验证每个组件的独立功能
- 集成测试：验证组件间的协作

## 2. 测试场景设计

### 2.1 PersonData类测试
1. **基本实例化测试**
   - 使用有效数据创建实例
   - 验证属性值正确设置

2. **类型提示验证**
   - 确保gender只接受"男"或"女"
   - 确保age是整数类型
   - 确保height和weight是数值类型

### 2.2 数据验证测试
1. **性别验证**
   - 有效值："男"、"女"
   - 无效值：空字符串、其他字符串、数字等

2. **年龄验证**
   - 有效范围：0-120
   - 边界值：0, 1, 119, 120
   - 无效值：负数、超过120、小数、非数字

3. **身高验证**
   - 有效范围：30-250cm
   - 边界值：30, 30.1, 249.9, 250
   - 无效值：负数、0、超过250、非数字

4. **体重验证**
   - 有效范围：2-300kg
   - 边界值：2, 2.1, 299.9, 300
   - 无效值：负数、0、超过300、非数字

### 2.3 BMR计算测试
1. **男性BMR计算**
   - 标准用例（如：25岁，175cm，70kg）
   - 边界值组合
   - 预期结果验证

2. **女性BMR计算**
   - 标准用例（如：30岁，160cm，55kg）
   - 边界值组合
   - 预期结果验证

3. **计算精度测试**
   - 验证四舍五入功能
   - 验证计算过程中的浮点数精度

### 2.4 异常处理测试
1. **输入验证异常**
   - 每种验证规则的违反情况
   - 异常消息的准确性
   - 异常类型的正确性

2. **计算异常**
   - 可能的计算错误情况
   - 异常捕获和转换
   - 错误消息的清晰性

## 3. 测试用例设计

### 3.1 PersonData类测试用例
```python
def test_person_data_creation_valid():
    """测试使用有效数据创建PersonData实例"""
    person = PersonData(gender="男", age=25, height=175.0, weight=70.0)
    assert person.gender == "男"
    assert person.age == 25
    assert person.height == 175.0
    assert person.weight == 70.0
```

### 3.2 数据验证测试用例
```python
def test_validate_gender():
    """测试性别验证"""
    # 有效情况
    person_valid = PersonData(gender="男", age=25, height=175.0, weight=70.0)
    assert validate_person_data(person_valid) is None
    
    # 无效情况
    person_invalid = PersonData(gender="其他", age=25, height=175.0, weight=70.0)
    with pytest.raises(BMRInputError, match="性别必须是'男'或'女'"):
        validate_person_data(person_invalid)
```

### 3.3 BMR计算测试用例
```python
def test_calculate_bmr_male():
    """测试男性BMR计算"""
    person = PersonData(gender="男", age=25, height=175.0, weight=70.0)
    bmr = calculate_bmr(person)
    # 根据Harris-Benedict公式计算的预期值
    expected = round(66.5 + (13.75 * 70) + (5.003 * 175) - (6.755 * 25))
    assert bmr == expected
```

## 4. 测试执行计划

1. **准备阶段**
   - 设置测试环境
   - 准备测试数据
   - 配置测试框架（pytest）

2. **执行顺序**
   - 数据类测试
   - 验证功能测试
   - 计算功能测试
   - 异常处理测试

3. **验证标准**
   - 所有测试用例必须通过
   - 代码覆盖率必须达到100%
   - 所有边界条件都必须测试
   - 所有异常路径都必须验证

## 5. 下一步行动

1. 创建`test_calculate_bmr.py`文件
2. 实现所有设计的测试用例
3. 运行测试并验证失败（符合TDD的"Red"阶段）
4. 准备开始实现功能代码 