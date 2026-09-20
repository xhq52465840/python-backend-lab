# 学习路线（简版）

> 详细版请看 **[PATH.md](./PATH.md)**；全仓库资料规则见 **[STANDARDS.md](./STANDARDS.md)**。

## 资料标准

官方文档是事实来源；课程按当前 FastAPI 与 **Pydantic v2** 学习，不把已弃用 API 作为默认写法。视频只使用 2025 年及以后、且与当天任务直接相关的片段。

## FastAPI 主线资料（当前）

- 中文主线（2026）：[FastAPI 从入门到实战](https://www.bilibili.com/video/BV19CFYzwE3J/)，按每个 `VIDEOS.md` 只看相关片段
- 官方文档（优先）：[FastAPI 中文文档](https://fastapi.tiangolo.com/zh/)
- 英文替代短课（2025）：[FastAPI Crash Course 2025](https://www.youtube.com/watch?v=nWWPlEO0he8)
- 测试：[FastAPI 测试教程](https://fastapi.tiangolo.com/zh/tutorial/testing/) + [pytest 官方文档](https://docs.pytest.org/en/stable/)

## 阶段出口（摘自 PATH.md）

| 阶段 | 你要能独立做到 |
|------|----------------|
| A1 FastAPI | week1 CRUD + PR CI 绿 |
| A2 数据库 | Postgres + 迁移 + JOIN/事务/索引心智 |
| A3 鉴权测试 | JWT + 防 IDOR + ≥10 测试 |
| A4 部署 | Compose 本地一键部署 + Actions |
| A5 项目 | 简历级 API |
| B 全栈 | 前端对接自己的 API |
| C Agent | ai-agent-book 第 1–5 章扎实 + 自建 Agent |

## 下一步教材

https://github.com/bojieli/ai-agent-book

官方前置：能改中等复杂度 Python、懂 Git/JSON/REST。用本仓库 Phase A 补齐后再进书。

## Week 1 · FastAPI（约 3 个工作日）

### Day 1

- 先读 FastAPI 官方 First Steps、Path Parameters、Request Body
- 中文主线只看环境、第一条路由、路径/查询参数、请求体的相关片段（45–60 分钟内）
- 作业：完成 `GET /todos`、`POST /todos`，理解 `/docs` 与 422

### Day 2

- 先读官方 Path Parameters、Response Status Code、HTTPException、Body Updates
- 中文主线只看路径参数、PUT、DELETE、状态码与 404 的相关片段（45–60 分钟内）
- 作业：完成 `GET/PUT/DELETE /todos/{id}` 与正确 404

### Day 3

- 先读 FastAPI Testing 官方文档与 pytest 官方入门
- 中文主线只看测试/pytest/PR-CI 相关片段；Actions 只做 20–30 分钟的近期概念导入
- 作业：补齐 `tests/`，`pytest` 全绿，开 PR 并检查 Actions

## Phase A2 · Week 2 Postgres（约 6–7 个工作日）

- 先读 PostgreSQL、SQLAlchemy 2.x 与 Alembic 官方文档，再做当前版本练习
- 作业：Compose 起 Postgres、迁移、完整 CRUD、JOIN、事务与索引
- 出口：数据持久化、至少两次迁移、能解释 `EXPLAIN`

## Phase A3 · 鉴权与测试（约 5 个工作日）

- 先读 FastAPI Security、JWT/密码哈希库和 pytest 官方文档
- 作业：register/login、Bearer、权限边界、防 IDOR、至少 10 个测试
- 出口：401/403/404 与核心失败路径覆盖，CI 绿

## Phase A4 · Docker / CI / 本地部署（约 4 个工作日）

- 先读 Docker 与 GitHub Actions 官方文档
- 作业：API + Postgres 的 Compose、一键启动、PR lint + pytest、部署说明
- 出口：本地生产形态跑通，Actions 自动检查

## Phase A5 · 简历级项目（约 8–12 个工作日）

每天按 `PATH.md` 推进一块：模型、路由、测试、Compose、CI 和 README。出口是能在 15 分钟内讲清请求、校验、service、DB、鉴权、迁移与回滚。