# NovaBrain 3.0 前端技术栈文档 v3

## 技术栈概览

NovaBrain 3.0 前端采用现代化的技术栈，通过组件化、类型安全和响应式设计，提供高性能、可维护的用户界面。本文档详细介绍当前前端技术选型及架构设计。

### 核心框架与语言

- **TypeScript** 4.9+ - 静态类型检查，提高代码质量和可维护性
- **React** 18.2.0 - 用户界面开发框架
- **Next.js** 13.4.0 - React 应用框架，提供服务端渲染(SSR)、静态生成(SSG)和路由功能

### 状态管理

- **Redux Toolkit** 1.9.5 - 全局状态管理
- **React Query** 4.29.5 - 服务器状态管理
- **Zustand** 4.3.8 - 局部状态管理（轻量级替代方案）

### UI 组件库

- **Chakra UI** 2.7.0 - 主要组件库
- **TanStack Table** 8.9.3 - 表格组件
- **Recharts** 2.7.2 - 数据可视化图表
- **React Flow** 11.7.4 - 流程图和节点编辑器（Low-Code 引擎核心）

### 样式解决方案

- **Emotion** 11.10.8 - CSS-in-JS 解决方案
- **TailwindCSS** 3.3.2 - 实用优先的 CSS 框架

### API 与网络

- **Axios** 1.4.0 - HTTP 客户端
- **SWR** 2.1.5 - 数据获取与缓存
- **Socket.IO Client** 4.6.1 - WebSocket 连接
- **gRPC-Web** 1.4.2 - gRPC 客户端支持

### 工具链与构建

- **Vite** 4.3.9 - 前端构建工具
- **ESLint** 8.41.0 - 代码质量检查
- **Prettier** 2.8.8 - 代码格式化
- **Jest** 29.5.0 - 单元测试框架
- **Testing Library** 14.0.0 - DOM 测试工具
- **Cypress** 12.13.0 - E2E 测试框架

### 国际化与本地化

- **react-i18next** 12.3.1 - 多语言支持
- **date-fns** 2.30.0 - 日期处理与格式化

## 架构设计

### 前端应用架构

```
src/
├── components/           # 共享组件
│   ├── common/           # 通用 UI 组件
│   ├── layout/           # 布局组件
│   ├── forms/            # 表单组件
│   └── visualizations/   # 可视化组件
├── pages/                # 页面组件与路由
├── hooks/                # 自定义 hooks
├── services/             # API 服务封装
│   ├── api/              # REST API 客户端
│   ├── grpc/             # gRPC 客户端
│   └── socket/           # WebSocket 客户端
├── store/                # Redux 全局状态管理
│   ├── slices/           # Redux 切片
│   └── middleware/       # Redux 中间件
├── utils/                # 工具函数
├── types/                # 类型定义
├── styles/               # 全局样式
└── config/               # 应用配置
```

### 代码组织原则

1. **组件设计**
   - 业务组件与通用组件分离
   - 采用原子设计方法论
   - 组件尽可能保持纯函数特性

2. **状态管理策略**
   - 全局状态：用户会话、应用配置等
   - 服务端状态：所有 API 数据通过 React Query 管理
   - 本地状态：组件内部状态使用 useState 或 Zustand

3. **路由组织**
   - 采用 Next.js 文件系统路由
   - 实现基于角色的路由权限控制
   - 路由守卫用于认证和授权检查

## 前后端接口集成

### API 集成策略

1. **REST API**
   - 所有常规 CRUD 操作
   - 遵循 REST 最佳实践
   - 使用 Axios 拦截器处理认证和错误

2. **gRPC 集成**
   - 用于性能关键型操作（如实时流程监控）
   - 模型推理请求
   - 大数据查询

3. **WebSocket**
   - 实时通知和警报
   - 流程执行状态更新
   - 协作功能

### 接口契约与类型生成

- 使用 OpenAPI 规范描述 REST 接口
- 从 OpenAPI 自动生成 TypeScript 类型定义和客户端代码
- Proto 文件自动生成 gRPC TypeScript 客户端

### 错误处理策略

- 全局错误边界捕获未处理异常
- 请求错误统一处理机制
- 友好的错误提示和恢复机制
- 错误日志上报系统

## 状态管理详解

### Redux 全局状态结构

```typescript
interface RootState {
  auth: {
    user: User | null;
    isAuthenticated: boolean;
    permissions: string[];
  };
  ui: {
    theme: 'light' | 'dark';
    sidebar: {
      isOpen: boolean;
      activeTab: string;
    };
    notifications: Notification[];
  };
  workspace: {
    currentProject: Project | null;
    recentProjects: Project[];
    savedWorkflows: Workflow[];
  };
  // ... 其他状态
}
```

### 数据获取模式

```typescript
// 使用 React Query 进行数据获取
const { data, isLoading, error } = useQuery({
  queryKey: ['models', modelId],
  queryFn: () => modelsApi.getModelById(modelId),
  staleTime: 5 * 60 * 1000, // 5分钟缓存
});

// 使用 SWR 获取数据（替代方案）
const { data, error } = useSWR(
  `/api/v1/models/${modelId}`,
  fetcher,
  { revalidateOnFocus: false }
);
```

## 性能优化

### 已实施的优化措施

1. **代码分割**
   - 基于路由的代码分割
   - 动态导入大型组件

2. **资源优化**
   - 图片优化（WebP 格式、响应式尺寸）
   - 字体优化与预加载

3. **渲染优化**
   - 虚拟列表（对大数据集）
   - React.memo 和 useMemo 避免不必要渲染
   - 使用 Web Workers 进行复杂计算

4. **缓存策略**
   - 服务端数据缓存 (React Query)
   - 本地存储缓存用户偏好

### 性能监控

- Lighthouse CI 集成
- Web Vitals 指标收集
- 性能预算设定

## 测试策略

### 测试类型与覆盖率目标

- **单元测试**: 覆盖率 > 80%
  - 工具函数
  - Hooks
  - Redux reducer 和 action

- **组件测试**: 覆盖率 > 70%
  - 交互测试
  - 快照测试

- **集成测试**: 覆盖率 > 60%
  - 页面组件
  - 集成外部服务的功能

- **E2E 测试**: 覆盖关键用户流程
  - 登录/注册
  - 模型部署
  - 流程设计

### 测试示例

```typescript
// 组件测试示例
describe('ModelCard', () => {
  it('renders model information correctly', () => {
    const model = {
      id: 'model-1',
      name: 'Test Model',
      version: '1.0.0',
      accuracy: 0.95,
    };
    
    render(<ModelCard model={model} />);
    
    expect(screen.getByText('Test Model')).toBeInTheDocument();
    expect(screen.getByText('v1.0.0')).toBeInTheDocument();
    expect(screen.getByText('95%')).toBeInTheDocument();
  });
  
  it('triggers deploy action when deploy button is clicked', () => {
    const mockDeploy = jest.fn();
    const model = { id: 'model-1', name: 'Test Model' };
    
    render(<ModelCard model={model} onDeploy={mockDeploy} />);
    
    fireEvent.click(screen.getByText('Deploy'));
    
    expect(mockDeploy).toHaveBeenCalledWith('model-1');
  });
});
```

## 可访问性与兼容性

### 可访问性标准

- 符合 WCAG 2.1 AA 级标准
- 支持键盘导航
- 屏幕阅读器兼容
- 颜色对比度符合标准

### 浏览器支持

- Chrome (最新版)
- Firefox (最新版)
- Safari (最新版)
- Edge (最新版)
- 不支持 IE 11

## 部署与环境

### 环境配置

- **开发环境**: local.novabrain.ai
- **测试环境**: test.novabrain.ai
- **预发布环境**: staging.novabrain.ai
- **生产环境**: app.novabrain.ai

### 环境变量管理

```typescript
// .env.example
NEXT_PUBLIC_API_URL=https://api.novabrain.ai/v1
NEXT_PUBLIC_SOCKET_URL=wss://ws.novabrain.ai
NEXT_PUBLIC_GRPC_URL=https://grpc.novabrain.ai
```

### CI/CD 流程

- GitHub Actions 自动化测试和构建
- Docker 容器化部署
- AWS S3 + CloudFront 静态资源分发
- 蓝绿部署策略

## 安全考量

- HTTPS 请求强制
- JWT 认证
- CSRF 保护
- CSP 配置
- XSS 防护
- 敏感信息处理（不在前端存储）

## 后续规划与技术债务

### 待改进项

1. 迁移部分类组件到函数组件
2. 状态管理优化，减少不必要的全局状态
3. API 请求层封装重构
4. 添加更多自动化测试

### 正在评估的技术

- Svelte/SvelteKit 用于特定模块
- GraphQL 替代部分 REST API
- WebAssembly 用于计算密集型任务
- Micro-Frontend 架构评估

## 团队协作与最佳实践

### 协作流程

- GitHub Flow 工作流
- PR 模板和检查列表
- 代码审查指南
- 配对编程实践

### 文档规范

- 使用 JSDoc 注释
- 每个组件/模块/工具附带使用说明
- Storybook 用于组件文档和开发

### 前后端协作

- 明确的 API 契约定义
- 开发前的接口评审
- Mock 服务器用于前端独立开发

## 附录

### 关键依赖版本完整列表

```json
"dependencies": {
  "@chakra-ui/react": "2.7.0",
  "@emotion/react": "11.10.8",
  "@emotion/styled": "11.10.8",
  "@reduxjs/toolkit": "1.9.5",
  "@tanstack/react-query": "4.29.5",
  "@tanstack/react-table": "8.9.3",
  "axios": "1.4.0",
  "date-fns": "2.30.0",
  "framer-motion": "10.12.16",
  "i18next": "22.5.0",
  "lodash": "4.17.21",
  "next": "13.4.0",
  "react": "18.2.0",
  "react-dom": "18.2.0",
  "react-flow-renderer": "11.7.4",
  "react-i18next": "12.3.1",
  "react-redux": "8.0.7",
  "recharts": "2.7.2",
  "socket.io-client": "4.6.1",
  "swr": "2.1.5",
  "typescript": "5.0.4",
  "zod": "3.21.4",
  "zustand": "4.3.8"
},
"devDependencies": {
  "@testing-library/jest-dom": "5.16.5",
  "@testing-library/react": "14.0.0",
  "@testing-library/user-event": "14.4.3",
  "@types/jest": "29.5.2",
  "@types/node": "20.2.5",
  "@types/react": "18.2.9",
  "@typescript-eslint/eslint-plugin": "5.59.9",
  "@typescript-eslint/parser": "5.59.9",
  "cypress": "12.13.0",
  "eslint": "8.41.0",
  "eslint-config-next": "13.4.4",
  "eslint-plugin-react": "7.32.2",
  "eslint-plugin-react-hooks": "4.6.0",
  "jest": "29.5.0",
  "jest-environment-jsdom": "29.5.0",
  "msw": "1.2.1",
  "prettier": "2.8.8",
  "tailwindcss": "3.3.2",
  "vite": "4.3.9"
}
```

### 相关资源链接

- [前端开发 Wiki](https://wiki.novabrain.internal/frontend)
- [UI 组件库 Storybook](https://storybook.novabrain.internal)
- [API 文档](https://api-docs.novabrain.internal) 