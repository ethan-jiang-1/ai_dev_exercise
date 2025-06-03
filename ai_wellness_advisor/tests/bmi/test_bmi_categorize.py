import pytest
from ai_wellness_advisor.src.bmi.bmi_categorize import categorize_bmi

# AC1 & AC3: 正常分类 - 偏瘦 (Underweight)
def test_categorize_underweight_lower_bound():
    assert categorize_bmi(10.0) == "偏瘦 (Underweight)"

def test_categorize_underweight_just_below_healthy():
    assert categorize_bmi(18.49) == "偏瘦 (Underweight)"

# AC1 & AC3: 正常分类 - 健康体重 (Healthy Weight)
def test_categorize_healthy_lower_bound():
    assert categorize_bmi(18.5) == "健康体重 (Healthy Weight)"

def test_categorize_healthy_mid_range():
    assert categorize_bmi(22.0) == "健康体重 (Healthy Weight)"

def test_categorize_healthy_just_below_overweight():
    assert categorize_bmi(23.99) == "健康体重 (Healthy Weight)"

# AC1 & AC3: 正常分类 - 超重 (Overweight)
def test_categorize_overweight_lower_bound():
    assert categorize_bmi(24.0) == "超重 (Overweight)"

def test_categorize_overweight_mid_range():
    assert categorize_bmi(26.0) == "超重 (Overweight)"

def test_categorize_overweight_just_below_pre_obese():
    assert categorize_bmi(27.99) == "超重 (Overweight)"

# AC1 & AC3: 正常分类 - 肥胖前期 (Pre-obese)
def test_categorize_pre_obese_lower_bound():
    assert categorize_bmi(28.0) == "肥胖前期 (Pre-obese)"

def test_categorize_pre_obese_mid_range():
    assert categorize_bmi(29.0) == "肥胖前期 (Pre-obese)"

def test_categorize_pre_obese_just_below_obese():
    assert categorize_bmi(29.99) == "肥胖前期 (Pre-obese)"

# AC1 & AC3: 正常分类 - 肥胖 (Obese)
def test_categorize_obese_lower_bound():
    assert categorize_bmi(30.0) == "肥胖 (Obese)"

def test_categorize_obese_high_value():
    assert categorize_bmi(40.0) == "肥胖 (Obese)"

# AC2: 无效输入 - 零值
def test_categorize_invalid_bmi_zero():
    with pytest.raises(ValueError, match="BMI值必须是有效的正数"):
        categorize_bmi(0)

# AC2: 无效输入 - 负值
def test_categorize_invalid_bmi_negative():
    with pytest.raises(ValueError, match="BMI值必须是有效的正数"):
        categorize_bmi(-5.0)

# AC2: 无效输入 - 非数字 (字符串)
def test_categorize_invalid_bmi_string():
    with pytest.raises(ValueError, match="BMI值必须是有效的数字"):
        categorize_bmi("abc")

# AC2: 无效输入 - None
def test_categorize_invalid_bmi_none():
    with pytest.raises(ValueError, match="BMI值必须是有效的数字"):
        categorize_bmi(None)