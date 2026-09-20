# 总路线：资深前端 → Python 后端工程师 → 全栈 + Agent 专家

> 全仓库资料硬规则见 [STANDARDS.md](./STANDARDS.md)：官方文档是事实来源；当前 FastAPI + Pydantic v2 是默认栈；视频必须为 2025 年及以后，过时 API 不作为默认教学。

## 0. 终点与验收标准

### 阶段终点 A：普通 Python 后端工程师

你能独立完成并解释：

1. 用 FastAPI 做带鉴权的 REST API（注册登录、CRUD、分页、过滤、错误码）。
2. 用 PostgreSQL 建模（用户/业务表、外键、索引），会写 JOIN / 聚合 / 事务；用 Alembic 做迁移。
3. 写 pytest（覆盖鉴权、权限边界、主要失败路径），本地测试全绿。
4. 用 Docker Compose 一键起 API + Postgres；密钥只进环境变量。
5. 用 GitHub Actions 在 PR 自动 lint + test。
6. 能读懂 `pyproject.toml` / `uv`、分层、依赖注入与数据库连接。

### 阶段终点 B：全栈工程师

在 A 的基础上，用前端对接自己的 API，处理 OpenAPI、CORS、token、401、加载态和错误态，并完成一套本地可运行的全栈产品。

### 阶段终点 C：Agent 工程师

能从零实现最小 ReAct Agent，理解上下文、工具调用、RAG、MCP、评估与失败重试，并完成带权限边界的 Coding Agent 或业务 Agent。

## 1. 学习资料标准

- **官方文档优先**：视频只是辅助；与官方文档或当前仓库代码冲突时，以官方文档为准。
- **FastAPI 当前主线**：[FastAPI 中文官方文档](https://fastapi.tiangolo.com/zh/)。
- **中文主线视频（2026）**：[FastAPI 从入门到实战](https://www.bilibili.com/video/BV19CFYzwE3J/)，每天只看 `VIDEOS.md` 指定片段。
- **英文替代短课（2025）**：[FastAPI Crash Course 2025](https://www.youtube.com/watch?v=nWWPlEO0he8)，只看当天相关部分。
- 任何旧长课都不是主线；如果材料提到它，必须标注 **OUTDATED RISK / optional only**，冲突时优先官方文档。

## 2. 用前端经验翻译后端

| 前端概念 | 后端对应物 | 学习时抓住什么 |
|---|---|---|
| React props / state | Pydantic 模型 / 请求体校验 | 边界数据必须校验 |
| `fetch` / axios | FastAPI 路由 + `httpx` 测接口 | 状态码是契约 |
| TypeScript interface | Pydantic / dataclass / TypedDict | 类型提示 + 运行时校验 |
| Context / Redux | 无状态服务 + DB / Redis | 状态在库里 |
| npm scripts | Makefile / `uv run` / Compose | 环境可复现 |
| ESLint + CI | ruff + pytest + Actions | 流水线守门 |

## 3. 总时间表

| 阶段 | 时长（建议） | 产出 | 仓库位置 |
|---|---:|---|---|
| **A0** Python 语法补齐 | 1–2 周 | 能独立写函数/类/模块 | 笔记即可 |
| **A1** FastAPI 基础 | 1–2 周 | week1 完成 + PR 绿 | `week1-fastapi/` |
| **A2** PostgreSQL + ORM | 3 周 | 待办持久化 + 迁移 | `week2-postgres/` |
| **A3** 鉴权 + 测试 | 2 周 | JWT + ≥10 测试 | `week3-auth-tests/` |
| **A4** Docker + CI | 2 周 | Compose 一键起 + Actions | `week4-docker-cicd/` |
| **A5** 简历级项目 | 3–4 周 | 博客/记账/任务系统 API | 新目录或新仓 |
| **B** 全栈打通 | 2–3 周 | 前端对接自己的 API | 可另开前端仓 |
| **C** Agent | 6–16 周 | 实验 + 自建 Agent | `phase-c-prep/` / 书仓 |

## 4. Phase A0 — Python 语法

必会：虚拟环境、基本类型、控制流、函数与类型注解、模块、dataclass、异常、`pathlib`/JSON、`async`、pytest 入门。优先阅读 [Python 官方 Tutorial](https://docs.python.org/3/tutorial/)。

### 出门考试

限时 90 分钟写一个 CLI：读取 JSON 用户列表，按 `age` 过滤后输出新 JSON，带 `argparse` 和 3 个 pytest。别人按 README 能跑通才算通过。

## 5. Phase A1 — FastAPI（对应 `week1-fastapi/`）

### 目标能力

- 解释 HTTP 方法与幂等：GET 安全；PUT 幂等；POST 通常非幂等。
- 会用路径参数、查询参数、Body、响应模型和状态码。
- 会用 `/docs` 作为 OpenAPI 契约。
- 会用 `TestClient` 测接口。

### 当前资料主线

1. 先读 [FastAPI 中文官方文档](https://fastapi.tiangolo.com/zh/)。
2. 中文视频用 [BV19CFYzwE3J](https://www.bilibili.com/video/BV19CFYzwE3J/)，按 Day01–Day03 的 `VIDEOS.md` 分段，单日视频/阅读总时长约 45–60 分钟。
3. 英文替代用 [FastAPI Crash Course 2025](https://www.youtube.com/watch?v=nWWPlEO0he8) 的相关片段。
4. Day03 测试以 [FastAPI Testing](https://fastapi.tiangolo.com/zh/tutorial/testing/) 与 [pytest 官方文档](https://docs.pytest.org/en/stable/) 为准；Actions 只做 20–30 分钟近期概念导入。

### 本周作业

目录：`week1-fastapi/`。

- [ ] `GET/POST/GET:id/PUT/DELETE` 待办
- [ ] 404 / 422 行为正确
- [ ] pytest 覆盖创建、列表、更新、删除、404
- [ ] 分支 `week1-done` → PR → Actions 绿

### A1 出门考试

合上教程，从空文件夹 30 分钟搭一个「笔记 API」（title、content、health），带两个测试。

## 6. Phase A2 — 数据库

先读 PostgreSQL、SQLAlchemy 2.x、Alembic 官方文档。会建表、主键/外键、约束、CRUD、JOIN、聚合、事务、索引与 `EXPLAIN`；实现待办持久化、至少两次迁移、5 条 SQL 练习，并解释 N+1 与加载策略。

A2 出门考试：画「用户-文章-标签」多对多 ER 图，写建表 SQL，说明索引理由。

## 7. Phase A3 — 鉴权、安全与测试

目标：密码只存哈希；理解 JWT/access token/过期；Bearer；CORS；防 IDOR；fixture、工厂数据和失败路径测试。

验收：`register/login`、受保护路由、用户 A 不能改用户 B、至少 10 个 pytest、CI 全绿，README 写清如何拿 token 调 `/docs`。

## 8. Phase A4 — Docker、CI/CD、本地部署

读 Docker 与 GitHub Actions 官方文档。完成 API + Postgres 的 `docker compose up --build`、named volume、PR lint + pytest、可选镜像构建，并写从 Ubuntu 安装到更新回滚的 `DEPLOY.md`。

推荐拓扑：浏览器 → Caddy/Nginx（可选）→ API :8000 → Postgres :5432。先不做 K8s。

## 9. Phase A5 — 简历级后端项目

选一个做透：个人任务/项目管理 API 或简易博客 API。必须包含注册登录、核心资源 CRUD、分页/搜索、关系、统一错误、OpenAPI、测试、Compose、CI 和架构 README。加分项可选 Redis、后台任务、结构化日志或 admin 角色。

通过标准：能讲清请求 → 校验 → service → DB → 响应，鉴权位置、迁移与回滚、CI 内容。

## 10. Phase B — 全栈打通

用熟悉的前端栈接 API，处理 CORS、token 存储、401 刷新或重登、错误/加载态，完成注册 → 登录 → 业务操作 → 刷新的演示。

## 11. Phase C0–C — Agent

预备实验：裸调用 LLM API、工具调用循环、Pydantic 结构化输出与 `uv`。随后精读 ai-agent-book 第 1–5 章：Agent 入门、上下文、记忆/RAG、工具/MCP、Coding Agent；第 8 章后置为选修。

教材：[ai-agent-book](https://github.com/bojieli/ai-agent-book)；学习建议：[LEARNING.md](https://github.com/bojieli/ai-agent-book/blob/main/docs/zh-CN/LEARNING.md)。

## 12. 每周执行节奏

假设每周 10–15 小时：看文档/视频 4h，动手作业 6h，复盘 2h。一次只推进一个阶段出口；允许 AI 辅助，但关键路径必须能脱离 AI 重写；每周至少一次合上文档限时实现。

## 13. 现在立刻做什么

1. 进入 `week1-fastapi/`，按 Day01–Day03 的 `VIDEOS.md` 和官方文档完成 TODO，开 PR，看 CI。
2. 同步做 A0 自测清单，每天 30–60 分钟。
3. A1 未完成前不要跳 Agent 书的后半部分。
4. 每周结束记录 PR 链接与卡点，按当前标准复盘。