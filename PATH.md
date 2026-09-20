# 总路线：资深前端 → Python 后端工程师 → 全栈 + Agent 专家

> 仓库：https://github.com/xhq52465840/python-backend-lab  
> 下一步教材：https://github.com/bojieli/ai-agent-book  
> 读者画像：资深前端；后端当新手教；目标不是「看过」，而是「能独立交付」。

---

## 0. 你的终点长什么样（先对齐验收标准）

### 阶段终点 A：普通 Python 后端工程师（可投简历里的后端/全栈初级～中级）

你能独立完成下面这件事，且能向别人讲清楚「为什么这样设计」：

1. 用 **FastAPI** 做一个带鉴权的 REST API（注册登录、CRUD、分页、过滤、错误码约定）。
2. 用 **PostgreSQL** 建模（用户/业务表、外键、索引），会写 JOIN / 聚合 / 事务；用 **Alembic** 做迁移。
3. 写 **pytest**（至少覆盖鉴权、权限边界、主要失败路径）；本地 `pytest` 绿。
4. 用 **Docker Compose** 一键起：API + Postgres（可选 Redis）；`.env` 管密钥，从不提交密钥。
5. 用 **GitHub Actions**：PR 自动 lint + test；`main` 合并后可构建镜像（本地部署不强制上云）。
6. 本地部署：本机或一台 Linux 虚拟机上，用 Compose 跑通生产形态（反向代理可选 nginx/caddy）。
7. 能读懂别人的 Python 项目结构：`pyproject.toml` / `uv`、分层（router / service / repository）、依赖注入。

### 阶段终点 B：全栈工程师（前端优势 + 后端可独立）

在 A 的基础上再加：

1. 前端（你已会）对接自己的 API：OpenAPI 生成客户端或手写类型安全请求层。
2. 一次完整交付：注册登录页 + 业务页 + 后端 + DB + 本地 Compose 部署。
3. 会排查全链路问题：网络、CORS、Cookie/JWT、SQL 慢查询、容器日志。

### 阶段终点 C：精通 Agent 开发（以 ai-agent-book 为骨架）

书的核心公式：**Agent = LLM + 上下文 + 工具**；生产视角：**Agent = Model + Harness**。

你要达到：

1. 能从零实现一个 **最小 ReAct Agent**（消息列表、工具调用循环、终止条件）。
2. 懂上下文工程：消息结构、提示词、压缩、注入风险。
3. 接过 RAG / 用户记忆 / MCP 工具；能做简单评估集。
4. 能做一个可用的 **Coding Agent 或业务 Agent**（带工具、日志、失败重试），并写 README 说明架构。
5. 第 8 章（后训练）可作为选修：不挡「精通工程侧 Agent」；有算力再深入。

书官方前置（摘自 FAQ，已对照你的背景）：

- 能读改中等复杂度 Python ← **本仓库 Phase A 专门补**
- 用过 ChatGPT/Claude 等 ← 你大概率已有
- 熟悉 Cursor 等 AI 编程工具 ← 你正在用
- 懂命令行、Git、JSON、REST ← 前端经验已覆盖大半，缺的是 Python 侧落地

---

## 1. 用前端经验「翻译」后端（减少陌生感）

| 你熟悉的前端概念 | 后端对应物 | 学习时抓住什么 |
|---|---|---|
| React 组件 props / state | Pydantic 模型 / 请求体校验 | 边界数据必须校验，别信客户端 |
| `fetch` / axios | FastAPI 路由 + `httpx` 测接口 | 状态码是契约的一部分 |
| TypeScript interface | Pydantic / dataclass / TypedDict | Python 类型提示 + 运行时校验 |
| Context / Redux | 服务端「无状态」+ DB / Redis 会话 | HTTP 无状态；状态在库里 |
| npm scripts | Makefile / `uv run` / Compose | 可复现环境比「我机器能跑」重要 |
| ESLint + CI | ruff + pytest + Actions | 同样用流水线守门 |
| localStorage | Postgres 行；JWT 只放声明 | 别把敏感数据塞进 token |
| Webpack/Vite 打包 | Docker 镜像分层 | 镜像 = 可部署产物 |
| SPA 路由 | API 路由 + 反向代理 | `/api` 与静态资源分离 |

原则：**你不是从零学编程，是在学另一套运行时与持久化。** 每天刻意用「前端类比」记概念，但作业必须用 Python 亲手写。

---

## 2. 总时间表（可按每周 10～15 小时伸缩）

| 阶段 | 时长（建议） | 产出 | 仓库位置 |
|---|---|---|---|
| **A0** Python 语法补齐 | 1～2 周 | 能不查文档写函数/类/模块 | 笔记即可 |
| **A1** FastAPI 基础 | 2 周 | week1 完成 + PR 绿 | `week1-fastapi-crud` |
| **A2** PostgreSQL + ORM | 3 周 | 待办持久化 + 迁移 | `week2-postgres` |
| **A3** 鉴权 + 测试 | 2 周 | JWT + ≥10 测试 | `week3-auth-tests` |
| **A4** Docker + CI + 本地部署 | 2 周 | Compose 一键起 + Actions | `week4-docker-cicd` |
| **A5** 简历级后端项目 | 3～4 周 | 博客/记账/任务系统 API | 新目录或新仓 |
| **B** 全栈打通 | 2～3 周 | 前端对接你自己的 API | 可另开前端仓 |
| **C0** Agent 预备 | 1 周 | 最小 LLM 工具调用 Demo | `phase-c-prep/`（后续加） |
| **C1** ai-agent-book 第 1–5 章 | 6～10 周 | 每章实验 + 自建 coding agent | fork 该书仓库 |
| **C2** 第 6–7、9–10 章 | 4～6 周 | 评估集 + 多 Agent / 交互 | 同上 |
| **C3** 第 8 章（选修） | 视算力 | 了解 SFT/RL 即可 | 同上 |
| **D** 毕业作品 | 4～8 周 | 全栈产品 + Agent 能力 | 独立产品仓 |

合计主路径大约 **5～8 个月**（每周 10～15h）。更快可压缩 A0、并行 B 与 A5。

---

## 3. Phase A0 — Python 语法（前端转 Python 必过清单）

即使「能看懂」，也请用下面清单自测；不会的就补，不要假装会。

### 必会清单（每条写 10 行代码证明）

1. 虚拟环境：`python -m venv .venv`，激活，`pip` / 更好用 `uv`。
2. 基本类型：`str/int/float/bool/None`、`list/dict/set/tuple`。
3. 控制流：`if/for/while`、推导式、`enumerate`、`zip`。
4. 函数：默认参数、`*args/**kwargs`、类型注解、`raise`。
5. 模块：`import`、包结构、`if __name__ == "__main__"`。
6. 类：`__init__`、实例方法、`@dataclass`、简单继承。
7. 异常：`try/except/finally`、自定义异常。
8. 文件与路径：`pathlib.Path`、读写文本/JSON。
9. 异步入门：`async def`、`await`（FastAPI 会用到）。
10. 测试入门：`assert`、pytest 函数命名 `test_*`。

### 推荐材料（选一条主线即可）

- 视频（英文）：freeCodeCamp Python 入门长课（若语法已熟可跳，只做清单自测）。
- 文档：官方 [Python Tutorial](https://docs.python.org/3/tutorial/) 前半。
- 对照学习：把一段 React hooks 逻辑改写成 Python 函数 + dataclass。

### A0 出门考试（限时 90 分钟，不准抄大段教程）

写一个 CLI：读取 JSON 文件里的用户列表，按 `age` 过滤，输出新 JSON；带 `argparse`；写 3 个 pytest。

通过标准：别人克隆后按 README 能跑通。

---

## 4. Phase A1 — FastAPI（对应仓库 week1）

### 目标能力

- 解释 HTTP 方法与幂等：GET 安全；PUT 幂等；POST 非幂等。
- 会用路径参数、查询参数、Body、响应模型、状态码。
- 会用 `/docs`（OpenAPI）当契约。
- 会用 `TestClient` 测接口。

### 视频主线（跟做，不要只看）

1. **主线（强烈推荐）**：[Python API Development · freeCodeCamp · ~19h](https://www.youtube.com/watch?v=0sOvCWFmrtA)  
   - 本阶段只跟到：CRUD + Pydantic + 自动文档（数据库段先听个印象，下周再深啃）。
2. **中文**：[黑马 FastAPI 入门到实战](https://www.bilibili.com/video/BV1zV2QBtE39/)（路由、依赖注入、Pydantic）。
3. **速览**：[FastAPI Crash Course 2025](https://www.youtube.com/watch?v=nWWPlEO0he8)。

### 本周作业（必须交 PR）

目录：`week1-fastapi-crud/`

按 README 完成 TODO 1～6：

- [ ] `GET/POST/GET:id/PUT/DELETE` 待办
- [ ] 404 / 422 行为正确（非法 body 应 422）
- [ ] `pytest` 覆盖创建、列表、更新、删除、404
- [ ] 分支 `week1-done` → PR → Actions 绿

### 概念深挖（写进笔记，用自己的话）

1. 为什么 FastAPI 要 Pydantic？和 TypeScript 编译期检查差在哪？
2. 依赖注入（`Depends`）解决什么问题？类比 NestJS / Angular DI。
3. 为什么「内存 fake_db」不能上生产？下一阶段如何替换？

### A1 出门考试

合上教程，从空文件夹 30 分钟搭一个「笔记 API」（title, content），带 health 与两个测试。

---

## 5. Phase A2 — 数据库（要「很了解」，不是只会 CRUD）

### 你要达到的「了解」级别

**会用：**

- 建库建表、主键/外键、唯一约束、非空、默认值。
- `SELECT/INSERT/UPDATE/DELETE`、`WHERE/ORDER BY/LIMIT`。
- `INNER/LEFT JOIN`、`GROUP BY` + `COUNT/SUM`。
- 事务：`BEGIN/COMMIT/ROLLBACK`（转账/扣库存心智模型）。
- 索引：什么时候加、为何会变慢、用 `EXPLAIN` 看一眼。

**会工程化：**

- SQLAlchemy 2.x 或 SQLModel 映射。
- Alembic：改模型 → 生成迁移 → 升级/回滚。
- 连接串、连接池、时区与 UTC。
- N+1 问题与 `selectinload` / join 加载。

**暂不要求（了解即可）：** 分库分表、复杂锁、复制集运维。

### 视频 / 练习

1. freeCodeCamp 主线里的 **Postgres + SQLAlchemy** 整段（必须跟做）。
2. [PostgreSQL Full Course](https://www.youtube.com/watch?v=qw--VYLpxG4)。
3. 文字：[W3Schools PostgreSQL](https://www.w3schools.com/postgresql/) 每章练习做完。
4. 短开篇：[Intro to PostgreSQL Part 1](https://www.youtube.com/watch?v=74IWNUja05w)。

### 本仓库作业（week2，后续会补骨架；你可先自建）

建议表设计（待办系统升级）：

```text
users(id, email UNIQUE, password_hash, created_at)
todos(id, user_id FK → users, title, completed, created_at, updated_at)
```

验收：

- [ ] Docker 起 Postgres（或本机安装）。
- [ ] Alembic 至少 2 次迁移（建表 → 加字段）。
- [ ] 待办 CRUD 全部落库；重启数据还在。
- [ ] 手写 5 条 SQL（含 JOIN 与按用户统计待办数）。
- [ ] 用 `EXPLAIN` 对比：无索引 vs 有索引的 `WHERE user_id = ?`。

### SQL 必练题（自己建表做）

1. 查每个用户未完成待办数量，按数量降序。
2. 查最近 7 天新建待办。
3. 事务：把两个用户的某字段互换，中途失败要回滚。
4. 防止重复邮箱：证明 UNIQUE 约束生效。
5. 软删除：加 `deleted_at`，列表默认过滤已删。

### A2 出门考试

画出「博客：用户-文章-标签（多对多）」ER 图，写出建表 SQL，说明需要哪些索引及原因。

---

## 6. Phase A3 — 鉴权、安全与测试

### 目标

- 密码只存哈希（bcrypt/argon2），永不存明文。
- JWT：access token 内容、过期、为何 refresh 要小心。
- 权限：只能改自己的资源（IDOR 防御）。
- CORS：前端跨域时怎么配（你前端经验会很快懂）。
- pytest fixture、工厂数据、覆盖失败路径。

### 视频

继续 freeCodeCamp 主线 **JWT + pytest** 段；对照 FastAPI 官方 Security 教程。

### 作业验收

- [ ] `POST /auth/register`、`POST /auth/login`
- [ ] 受保护路由：`Authorization: Bearer ...`
- [ ] 用户 A 不能改用户 B 的 todo（测 403/404）
- [ ] ≥10 个测试；CI 全绿
- [ ] README 写清如何拿到 token 调 `/docs`

### 安全清单（背下来）

1. 密钥进环境变量。
2. 生产关 debug。
3. 依赖版本锁定（`uv.lock` / `requirements.txt`）。
4. 限流以后再学；先做到「不瞎暴露管理接口」。

---

## 7. Phase A4 — Docker、CI/CD、本地化部署

### 概念分层（别混）

| 词 | 含义 | 你要会的程度 |
|---|---|---|
| 镜像 | 只读模板 | 会写 Dockerfile |
| 容器 | 镜像的运行实例 | 会 `run/logs/exec` |
| Compose | 多容器编排 | 会写 `services/volumes/ports` |
| CI | 持续集成：自动测 | PR 上跑 ruff+pytest |
| CD | 持续交付/部署 | 本阶段做到「自动构建」；部署可先手动 Compose |
| 本地化部署 | 在你控制的机器上跑 | 本机或局域网 VM，不依赖云厂商也行 |

### 视频

1. 主线 freeCodeCamp 的 Docker + Actions 段。
2. [Docker for Beginners](https://www.youtube.com/watch?v=fqMOX6JJhGo)。
3. [GitHub Actions + Docker](https://www.youtube.com/watch?v=R8_veQiYBjI)。

### 作业验收（本地化部署）

- [ ] `docker compose up --build` 起 API + Postgres。
- [ ] 宿主机浏览器打开 `/docs` 可用。
- [ ] 数据在 named volume，删容器不丢库（除非你删 volume）。
- [ ] Actions：PR → 测试；可选 push 镜像到 GHCR。
- [ ] 一份 `DEPLOY.md`：从零一台 Ubuntu 怎么装 Docker、拷项目、起服务、看日志、更新版本。

### 推荐本地部署拓扑（简单可靠）

```text
浏览器 → (可选 Caddy/Nginx :80) → API 容器 :8000 → Postgres 容器 :5432
```

先不做 K8s。普通工程师日常够用的是 **Compose + 反向代理 + 备份 volume**。

---

## 8. Phase A5 — 简历级后端项目（证明「普通 Python 工程师」）

选 **一个** 做透（推荐「个人任务/项目管理 API」或「简易博客 API」）：

### 功能清单

- 用户注册登录、个人资料
- 核心业务资源完整 CRUD + 分页 + 搜索
- 至少一对多或多数多关系
- 统一错误响应格式
- OpenAPI 完整
- 测试覆盖核心路径
- Compose + CI
- README：架构图（可用 mermaid）、如何跑、如何测、如何部署

### 加分（选 2 个）

- Redis 缓存热点读
- 后台任务（发邮件假实现 / ARQ / Celery 入门）
- 结构化日志 + request id
- 简易管理角色（admin）

### 通过标准（自我答辩 15 分钟）

能讲清：请求进路由 → 校验 → service → DB → 响应；鉴权在哪一层；迁移怎么做；CI 跑了什么；如何回滚一次坏迁移。

---

## 9. Phase B — 全栈打通（发挥你的前端优势）

1. 用你最熟的前端栈（React/Vue 等）接 Phase A5 API。
2. 处理好：CORS、token 存储（内存/ httpOnly cookie 方案对比）、401 刷新或重登。
3. 错误与加载态按前端工程标准做完。
4. 同一套 Compose：可选加 `web` 服务（Nginx 托管前端静态资源）。

验收：演示「注册 → 登录 → 业务操作 → 刷新仍登录或安全失效」全流程。

---

## 10. Phase C0 — 进 Agent 书之前的 1 周预备

书要求你能改中等 Python；预备周专门对齐 Agent 编程模型。

### 必做小实验（每个半天）

1. **裸调用 LLM HTTP API**（OpenAI 兼容即可）：发 messages，打印回复。
2. **工具调用**：让模型返回「要调的函数名+参数」，你本地执行后再塞回 messages（手写 ReAct 循环，不引框架）。
3. **结构化输出**：要求 JSON，用 Pydantic 校验失败则重试。
4. **装 `uv`**，会跑 `uv sync` / `uv run`（Agent 书官方推荐）。

### 建议申请的 Key（书 README 列表，国内可访问优先）

Kimi / 智谱 / Siliconflow / DeepSeek / OpenRouter 等，至少一个能跑通实验即可。

---

## 11. Phase C — 《深入理解 AI Agent》精读与实验计划

教材：https://github.com/bojieli/ai-agent-book  

在线：https://bojieli.github.io/ai-agent-book/astro/  
PDF：仓库 Releases `latest`。

学习建议官方文档：`docs/zh-CN/LEARNING.md`（三层阅读：Starter / Builder / Maintainer）。

### 总策略（对你这种目标「精通」的人）

1. **先读薄再读厚**：每章先看目录与关键洞察，再精读，再动手。
2. **实验不是看代码**：读懂原则后，尽量用 Cursor **自己实现一遍**，对照官方实验验收。
3. **第 1–5 章必须扎实**；官方说这五章够做一个可用 coding agent。
4. **第 8 章可后置**：精通工程侧 Agent 不依赖训练卡。
5. 每章结束写一页「架构笔记」：输入、状态、工具、失败如何处理。

### 章节节奏与你的验收

| 章 | 主题 | 建议时长 | 你的最低验收 | 官方推荐 Starter 实验 |
|---|---|---|---|---|
| 1 | Agent 入门 | 1 周 | 手写 ReAct 循环；说清 Harness | `chapter1/context` |
| 2 | 上下文工程 | 1～2 周 | 能解释 KV cache 与提示注入；做压缩小实验 | `context-compression` |
| 3 | 记忆与知识库 | 1～2 周 | 实现最小 RAG（切分→嵌入→检索→生成） | `user-memory` |
| 4 | 工具与 MCP | 1 周 | 实现 2～3 个工具 + 读懂 MCP | `execution-tools` |
| 5 | Coding Agent | 2 周 | **自建迷你 Coding Agent**（读文件/改文件/跑命令，有权限边界） | `coding-agent` |
| 6 | 交互扩展 | 1～2 周 | 理解异步事件；选做语音或 browser-use | `live-audio` 等 |
| 7 | 评估 | 1～2 周 | 给自己的 Agent 建 ≥15 条任务的评估集 | `tau2-bench-eval` 等 |
| 8 | 后训练 | 选修 | 能讲清 SFT vs RL 适用场景即可 | 按算力 |
| 9 | 持续进化 | 1 周 | 从失败轨迹改 prompt/工具/程序 | `trajectory-verifier` |
| 10 | 多 Agent | 1 周 | 两 Agent 分工完成一个研究/开发任务 | `parallel-web-research` |

### 与「全栈 + Agent」结合的毕业方向（Phase D 选题）

选一个贴近你前端优势的：

1. **带 UI 的 Coding Agent 工作台**（任务队列、diff 展示、工具调用时间线）。
2. **站内智能客服 / 文档助手**：你的产品文档 RAG + 工具（查订单假数据）+ 管理后台。
3. **前端工程 Agent**：自动跑 lint/test、开 PR 描述、根据 CI 日志建议修复（接 GitHub API——你已有连接器）。

毕业作品必须包含：架构说明、评估集、本地 Compose 部署、演示视频或 GIF。

---

## 12. 每周执行节奏（请照此执行，而不是「有空再学」）

假设每周 12 小时：

| 块 | 时间 | 做什么 |
|---|---|---|
| 看视频 / 读书 | 4h | 1.25x，卡点暂停自己敲 |
| 动手作业 | 6h | 只认 PR 与测试绿 |
| 复盘 | 2h | 用自己的话写「本周 5 条」；卡点记进 issue |

规则：

- **同一时间只做一个阶段出口**，不要 A2 没完就跳去读 Agent 第 5 章。
- 允许用 AI 写代码，但你必须能删掉 AI 代码后自己重写关键路径。
- 每周至少 1 次「合上文档限时实现」。

---

## 13. 现在立刻做什么（今天～本周）

1. Clone 本仓，完成 **week1** 全部 TODO，开 PR，看 CI。
2. 同步开始 A0 自测清单（缺啥补啥，每天 30～60 分钟）。
3. 收藏 Agent 书 PDF，但 **先不要深读第 3 章以后**，避免焦虑。
4. 本周结束时发我：week1 PR 链接 + 你卡在哪一步（我按报错带你改）。

---

## 14. 材料总表（收藏夹）

### 后端主线

- https://www.youtube.com/watch?v=0sOvCWFmrtA  
- https://www.bilibili.com/video/BV1zV2QBtE39/  
- https://www.youtube.com/watch?v=qw--VYLpxG4  
- https://www.youtube.com/watch?v=fqMOX6JJhGo  
- https://www.youtube.com/watch?v=R8_veQiYBjI  
- FastAPI 官方文档：https://fastapi.tiangolo.com/zh/  
- SQLAlchemy 2.0：https://docs.sqlalchemy.org/  

### Agent

- https://github.com/bojieli/ai-agent-book  
- 学习建议：https://github.com/bojieli/ai-agent-book/blob/main/docs/zh-CN/LEARNING.md  
- 在线阅读：https://bojieli.github.io/ai-agent-book/astro/  

### 本仓库

- 跟练入口：`README.md`、`COURSE.md`（简版）、本文件 `PATH.md`（详版）

---

## 15. 我（助手）怎么带你

你按阶段推进时，可以直接丢：

- 「week1 TODO3 我这样写报错：…」
- 「帮我 review 这个 PR」
- 「按 A2 验收清单检查我仓库」
- 「Agent 书第 1 章实验跑不起来」

我会按**当前阶段验收标准**带你，而不是东一榔头西一棒子。

---

*最后更新：与「资深前端 → 普通 Python 后端 → 全栈 → ai-agent-book → Agent 专家」目标对齐。*
