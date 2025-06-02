## 每个 ExTDD 练习的目录结构 (针对 feature的详尽说明, 核心思想)

每个TDD练习周期（例如，针对BMI模块的 `ExTDD_01_BMICalculation`）的产出物，将归档在 `ai_wellness_advisor/dev_cycles/{module_name}/ExTDD_XX_{FeatureName}/` 目录下。其中 `{module_name}` 对应如 `bmi`, `dcnc` 等模块名。其内部结构和文件说明如下：

```
ai_wellness_advisor/
├── src/                            # (Source Code Snapshot) TDD周期内的源代码快照
│   └── {module_name}/              # 例如 bmi/
│       ├── README_{feature_name}.md
│       └── {feature_name}.py
├── tests/                          # (Test Code Snapshot) TDD周期内的测试代码快照
│   └── {module_name}/              # 例如 bmi/
│       └── test_{feature_name}.py
├── dev_cycles/                     # (User Story, Design and Planning Documents) 思考、设计、约束、验证等文档
│   └── {module_name}/              # 例如 bmi/
│       └── ExTDD_XX_{feature_name}/ # 例如 ExTDD_01_BMICalculation/
│           ├── _user_story_{feature_name}.md
│           ├── _s1_think_options_{feature_name}.md
│           ├── _s2_think_design_{feature_name}.md
│           ├── _s3_think_validation_{feature_name}.md
│           └── _constraints_{feature_name}.md # (Optional)
```