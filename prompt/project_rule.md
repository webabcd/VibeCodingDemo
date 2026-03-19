## “电商后台管理系统”项目规则
### 1. 技术栈约束
- 核心框架：React 18.2.0、TypeScript 5.2.2、Vite 5.0.10
- 路由：react-router-dom 6.20.1（使用路由懒加载）
- 状态管理：Zustand 4.4.6（禁用 Redux/Mobx）
- UI 库：Ant Design 5.12.8（统一使用官方主题配置）
- 样式：Tailwind CSS 3.3.5 + CSS Modules（禁用内联 style）
- 网络请求：Axios 1.6.2（统一封装请求拦截器）
- 校验：Zod 3.22.4（接口参数/表单校验）
- 测试：Vitest 1.0.4 + React Testing Library（生成代码需包含单测）

### 2. 目录结构规范
```
src/
├── api/                # 接口请求封装（按模块拆分）
│   ├── user/           # 用户模块接口
│   ├── order/          # 订单模块接口
│   └── request.ts      # Axios 封装基类（请求拦截、响应拦截）
├── components/         # 通用组件（全局复用，如按钮、输入框）
├── hooks/              # 自定义 Hooks（如 useAuth、useRequest）
├── layouts/            # 布局组件（如侧边栏、头部、主布局）
├── pages/              # 业务页面（按模块拆分）
│   ├── dashboard/      # 仪表盘（首页数据概览）
│   ├── user/           # 用户管理（列表、新增、编辑、删除）
│   └── orde/           # 订单管理（列表、详情、状态修改）
├── store/              # Zustand 状态管理（全局状态）
├── types/              # TypeScript 类型定义（接口、枚举、类型别名）
└── utils/              # 工具函数（如时间格式化、数据校验）
```

### 3. 业务逻辑约束
- 接口请求：
  - 所有接口需添加超时时间（10s），失败自动重试 1 次
  - 响应错误统一处理（401 跳转登录，500 提示服务器错误）
  - 接口返回数据必须定义 TypeScript 接口（放在 src/types/api 目录）
- 表单处理：
  - 表单提交前必须做 Zod 校验，校验失败提示具体字段错误
  - 表单组件需实现防抖（输入间隔 500ms），避免频繁触发校验
- 权限控制：
  - 页面级权限：基于 react-router 路由守卫实现
  - 按钮级权限：封装 AuthButton 组件，基于用户角色控制显示/隐藏

### 4. 部署与交付
- 构建命令：
  - 开发环境：`npm run dev`
  - 测试环境：`npm run build:test`
  - 生产环境：`npm run build:prod`
- 打包优化：
  - 自动移除 console.log/debugger
  - 开启代码分割、Tree Shaking
  - 静态资源 CDN 路径替换（配置在 .env 中）
- 交付物：
  - 生成可运行的打包文件（dist 目录）
  - 自动生成项目 README.md（包含启动、打包、部署说明）
  - 生成单元测试报告（coverage 目录）