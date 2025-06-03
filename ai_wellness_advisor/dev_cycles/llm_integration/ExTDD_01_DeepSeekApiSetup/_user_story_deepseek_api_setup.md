# User Story: DEEPSEEK API基础配置与调用验证 (deepseek_api_setup)

作为开发者，在正式实现复杂的健康建议功能前，我首先需要验证与DEEPSEEK API的基础通信链路。我希望创建一个最小化的模块，该模块能够：

1.  正确加载和使用 `DEEPSEEK_API_KEY` 及其他必要配置（通过 `utils_llm`）。
2.  构造一个简单的请求发送给DEEPSEEK模型。
3.  成功接收模型返回的一个简单JSON格式响应。
4.  （推荐）使用Pydantic模型来解析和验证这个JSON响应，确保数据结构符合预期。

此练习的目的是打通配置、熟悉API调用流程，并为后续功能开发建立一个可靠的起点。 