/**
 * 回退响应系统
 * 当RAG系统不可用时提供专业的备用回复
 */

const FALLBACK_RESPONSES = {
  // 深度约会分析回退响应
  deep_analysis: {
    展示财富: `从你的描述来看，这位男士在约会中展示收入和生活品质，可能是为了建立吸引力。但如果伴随着对你的要求和限制，这确实需要仔细分析：

**行为模式解读：**
• **高价值展示（DHV）**：通过展示资源来建立吸引力，这在社交动力学中很常见
• **框架设定**：试图定义关系中的权力动态，建立主导地位
• **符合性测试**：通过设定标准来观察你的反应和服从度
• **边界划定**：对私生活的保护可能反映独立性，但也可能是回避亲密感

**深层心理分析：**
1. **安全感不足** - 过度展示财富可能掩盖内在的不安全感
2. **控制倾向** - 设定过高要求可能反映对关系的控制欲
3. **社交策略** - 可能受到某些社交理论影响，采用特定的吸引策略

**建议应对策略：**
1. **保持独立判断** - 不要因财富展示而忽视人品和相处感受
2. **温和测试边界** - 通过轻松话题观察他的反应灵活性
3. **关注情感连接** - 真正的吸引力来自情感共鸣，不仅是物质条件
4. **信任直觉感受** - 如果感到被评判或压制，这种感觉通常是准确的

**核心提醒：**
优质的伴侣会欣赏真实的你，而不是试图按照他的标准改造你。健康的关系应该让双方都感到被接纳和支持。`,

    打压行为: `遇到带有打压性质的约会行为确实让人困扰。这种行为模式需要仔细分析：

**可能的动机：**
• 测试你的自信水平和反应
• 建立主导地位或控制感
• 通过对比来提升自己的价值感
• 不成熟的社交技巧表现

**健康的应对方式：**
1. **信任直觉** - 如果感到不舒服，这种感觉很可能是准确的
2. **温和回应** - 可以幽默地重新定义对话框架
3. **设定边界** - 明确表达什么行为是不可接受的
4. **评估兼容性** - 考虑这种沟通风格是否适合长期关系

**记住核心原则：**
- 你值得被尊重和欣赏
- 健康的关系建立在相互支持的基础上
- 不要为了迎合他人而牺牲自己的自尊`,

    过高要求: `当约会对象提出过高要求时，这可能反映了他们对关系的某些期待或不安全感：

**深层分析：**
• 可能反映个人的不安全感和控制欲
• 试图筛选"合适"的伴侣
• 可能来自过往经历的防御机制
• 对关系有完美主义倾向

**智慧应对：**
1. **保持真实** - 不要为了满足要求而伪装自己
2. **双向筛选** - 你也在评估对方是否适合你
3. **沟通期待** - 开诚布公地讨论彼此的期望
4. **时间验证** - 用时间来观察对方的真实人格

**自我提醒：**
- 合适的人会欣赏真实的你
- 关系应该让你成为更好的自己，而不是不同的人
- 相互成长比单方面迎合更重要`,

    默认: `基于你描述的约会情况，我能感受到你的困惑。这种复杂的互动确实需要仔细分析：

**核心建议：**
1. **信任自己的感受** - 你的直觉和感受都是有效的信息
2. **观察行为一致性** - 看对方的言行是否一致
3. **保持个人边界** - 不要因为约会而妥协核心价值观
4. **理性分析动机** - 试图理解对方行为背后的真实意图

**长期考虑：**
• 这种相处模式是否可持续？
• 你们的价值观和期待是否匹配？
• 这段关系是否让你感到被支持和理解？

记住，好的关系应该让双方都感到舒适和被尊重。如果持续感到压力或困惑，可能需要重新评估这段关系的兼容性。`
  },

  // 简单问题回退响应
  simple_reply: {
    问候: "你好！我是你的情感安全助理，随时为你提供约会和关系方面的专业建议。",
    感谢: "不客气！帮助你建立健康的情感关系是我的使命。",
    默认: "我理解你的关心。虽然专业知识库暂时不可用，但我仍然愿意为你提供基础的情感支持和建议。"
  }
};

/**
 * 获取合适的回退响应
 * @param {string} userInput - 用户输入
 * @param {string} analysisType - 分析类型
 * @returns {string} 回退响应
 */
function getFallbackResponse(userInput, analysisType = 'deep_analysis') {
  const input = userInput.toLowerCase();
  
  if (analysisType === 'simple_reply') {
    if (input.includes('你好') || input.includes('hi') || input.includes('hello')) {
      return FALLBACK_RESPONSES.simple_reply.问候;
    }
    if (input.includes('谢谢') || input.includes('感谢')) {
      return FALLBACK_RESPONSES.simple_reply.感谢;
    }
    return FALLBACK_RESPONSES.simple_reply.默认;
  }
  
  // 深度分析回退响应
  if (input.includes('展示') && (input.includes('收入') || input.includes('财富') || input.includes('钱'))) {
    return FALLBACK_RESPONSES.deep_analysis.展示财富;
  }
  
  if (input.includes('打压') || input.includes('贬低') || input.includes('挖苦')) {
    return FALLBACK_RESPONSES.deep_analysis.打压行为;
  }
  
  if (input.includes('要求') && (input.includes('高') || input.includes('严格'))) {
    return FALLBACK_RESPONSES.deep_analysis.过高要求;
  }
  
  return FALLBACK_RESPONSES.deep_analysis.默认;
}

/**
 * 构建完整的回退响应对象
 * @param {string} userInput - 用户输入
 * @param {string} analysisType - 分析类型
 * @param {string} errorMessage - 错误消息
 * @returns {Object} 回退响应对象
 */
function buildFallbackResponse(userInput, analysisType = 'deep_analysis', errorMessage = 'RAG系统暂时不可用') {
  const response = getFallbackResponse(userInput, analysisType);
  
  return {
    success: false,
    error: errorMessage,
    response: response,
    metadata: {
      processing_steps: ['文本输入', '意图识别', 'RAG系统回退', '备用回复生成'],
      processing_type: `${analysisType}_fallback`,
      has_audio: false,
      has_transcription: false,
      response_length: response.length,
      tokens_used: 0,
      model_used: 'fallback-system',
      timestamp: new Date().toISOString(),
      fallback_reason: errorMessage
    },
    troubleshooting: {
      suggestion: '专业知识库正在恢复中，请稍后重试获得更详细的分析',
      tips: [
        '当前提供的是基础情感建议',
        '系统会在知识库恢复后提供更专业的分析',
        '如有紧急情况，建议咨询专业情感咨询师'
      ]
    }
  };
}

module.exports = {
  getFallbackResponse,
  buildFallbackResponse,
  FALLBACK_RESPONSES
};