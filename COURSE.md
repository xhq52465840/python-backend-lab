# 学习路线

目标：独立写出带数据库的 FastAPI 后端，并用 GitHub Actions 自动测试。

## 主线视频

- 英文：[Python API Development (freeCodeCamp)](https://www.youtube.com/watch?v=0sOvCWFmrtA)
- 中文：[黑马 FastAPI 从入门到实战](https://www.bilibili.com/video/BV1zV2QBtE39/)
- SQL 补课：[PostgreSQL Full Course](https://www.youtube.com/watch?v=qw--VYLpxG4)
- Docker 补课：[Docker for Beginners](https://www.youtube.com/watch?v=fqMOX6JJhGo)
- Actions 补课：[GitHub Actions + Docker](https://www.youtube.com/watch?v=R8_veQiYBjI)

## 周计划

### Week 1 — FastAPI 基础（本仓库 `week1-fastapi-crud`）

- 路由、路径/查询参数、请求体、Pydantic、状态码、`/docs`
- 练习：完成内存版待办 CRUD（见该目录 README 的 TODO）

### Week 2–3 — PostgreSQL + ORM（`week2-postgres`）

- SQL、表设计、SQLAlchemy / SQLModel、Alembic
- 练习：把待办持久化到 Postgres

### Week 4–5 — 认证与测试（`week3-auth-tests`）

- 密码哈希、JWT、受保护路由、pytest
- 练习：注册登录 + 至少 5 个测试

### Week 6 — Docker + CI/CD（`week4-docker-cicd`）

- Dockerfile、Compose、GitHub Actions
- 练习：PR 自动跑测试；可选推送镜像

### Week 7–8 — 综合项目

- 博客或记账 API，满足 README 里的简历清单
