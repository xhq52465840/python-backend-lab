# 每日学习计划（每天约 3 小时 · 工作日主学）

老师模式：
- **工作日 10:00**：布置今日清单 + 抽查旧知识
- **工作日 18:00**：问你完成了没 + 巩固测验（含少量旧知识）

每天时间块（可微调）：

| 块 | 时长 | 内容 |
|----|------|------|
| 块 1 | 60–75 分 | 视频 / 阅读（1.25x，卡点自己敲） |
| 块 2 | 90–100 分 | 动手作业（只认代码、测试、PR） |
| 块 3 | 20–30 分 | 复盘笔记；准备傍晚测验 |

仓库：https://github.com/xhq52465840/python-backend-lab  
总路线：`PATH.md`  
主线视频：https://www.youtube.com/watch?v=0sOvCWFmrtA  

---

## 总进度勾选（自己改，老师也会盯）

当前阶段：`A1-week1`

- [ ] A0 Python 出门考试通过
- [ ] A1 week1 CRUD + PR CI 绿
- [ ] A2 week2 Postgres + SQL + 第二次迁移
- [ ] A3 鉴权 + ≥10 测试
- [ ] A4 Compose 本地部署 + Actions
- [ ] A5 简历级 API
- [ ] B 全栈对接
- [ ] C0 Agent 预备
- [ ] C1 ai-agent-book 第 1–5 章
- [ ] C2 第 6–7、9–10 章
- [ ] D 毕业作品

请假或某天只学 45 分钟：在对话里说一声，日期顺延，不算放弃。

---

## Phase A0（若语法不熟：插在最前 2～4 个工作日）

### A0-D1
- 读：Python 官方 Tutorial 前半或自选入门视频
- 做：虚拟环境、`list/dict`、函数、类型注解各写一小段
- 验收：能激活 `.venv` 并 `pip list`

### A0-D2
- 做：`pathlib` 读写 JSON；`dataclass`；3 个 `pytest`
- 出门考试：限时 90 分钟 CLI（按 age 过滤 JSON）+ README
- 验收：别人按 README 能跑通 → 勾选 A0

---

## Phase A1 · Week1 FastAPI（约 3 个工作日）

### Day 1（A1）
- 视频：freeCodeCamp / 黑马 FastAPI 开头（环境、第一个路由、`/docs`）
- 作业：`week1-fastapi-crud` 跑通；完成 `GET /todos`、`POST /todos`
- 验收：`/docs` 能点通；非法 body 出现 422
- 旧知预备：HTTP 方法幂等（傍晚会问）

### Day 2（A1）
- 视频：路径参数、状态码、Pydantic 模型
- 作业：`GET/PUT/DELETE /todos/{id}` + 正确 404
- 验收：手动在 `/docs` 走完增删改查

### Day 3（A1）
- 作业：补全 `tests/`；`pytest` 全绿；分支 `week1-done` 开 PR，看 Actions
- 出门考试：30 分钟空文件夹「笔记 API」+ 2 个测试
- **出口：勾选 A1**

---

## Phase A2 · Week2 Postgres（约 6～7 个工作日）

### Day 4（A2）
- 视频：PostgreSQL 是什么、表/行/主键
- 作业：`week2-postgres`：`docker compose up -d`；`cp .env.example .env`；`alembic upgrade head`；`uvicorn`；`GET /health` 显示 db up
- 验收：`psql` 里 `\dt` 看到 `users`/`todos`

### Day 5（A2）
- 视频：SQLAlchemy Session、依赖注入
- 作业：实现 `POST /todos`、`GET /todos` 落库
- 验收：重启 API 后数据还在

### Day 6（A2）
- 作业：实现 get/update/delete；404 行为正确；至少 2 个本地测试（可设 `WEEK2_DB_TESTS=1`）
- 验收：CRUD 全通

### Day 7（A2）
- 作业：`sql/practice.sql` 题 1～3；写 `sql/my-answers.sql`（勿提交密钥）
- 验收：能讲清 JOIN 与 GROUP BY 各解决什么

### Day 8（A2）
- 作业：Alembic 第二次迁移加 `todos.priority`；API/schema 跟上
- 验收：`alembic upgrade head`；新字段可用

### Day 9（A2）
- 作业：SQL 题 4～6；`EXPLAIN ANALYZE` 对比
- 出门考试：博客「用户-文章-标签」ER + 建表 SQL + 索引理由 → `sql/er-blog.md`
- **出口：勾选 A2**；开 `week2-done` PR

---

## Phase A3 · 鉴权与测试（约 5 个工作日）

### Day 10–11
- 视频：密码哈希、JWT、Bearer
- 作业：在 week3（或扩展 week2）实现 register/login；受保护路由
- 验收：无 token 不能改数据

### Day 12–13
- 作业：防 IDOR（A 不能改 B）；≥10 个 pytest；CI 绿
- 验收：测试里覆盖 401/403/404

### Day 14
- 复盘安全清单；README 写清如何拿 token 调 `/docs`
- **出口：勾选 A3**

---

## Phase A4 · Docker / CI / 本地部署（约 4 个工作日）

### Day 15–16
- 视频：Dockerfile、Compose、volume
- 作业：API+Postgres 一键 `compose up --build`；写 `DEPLOY.md` 初稿

### Day 17–18
- 视频：GitHub Actions
- 作业：PR 跑 lint+pytest；可选推镜像；完善 `DEPLOY.md`
- **出口：勾选 A4**

---

## Phase A5 · 简历级项目（约 8～12 个工作日）

每天：按 `PATH.md` A5 功能清单推进一块（模型 / 路由 / 测试 / Compose）。  
周末可加练，但不强制。  
**出口：能 15 分钟答辩架构** → 勾选 A5

---

## Phase B · 全栈（约 5～8 个工作日）

前端对接自己的 API：CORS、token、401、Compose 可选加 web 服务。  
**出口：演示注册→登录→业务→刷新** → 勾选 B

---

## Phase C0～D（Agent）

按 `PATH.md` Phase C；每日仍 10:00 布置 / 18:00 验收。  
第 1–5 章未扎实前不要跳第 8 章训练。

---

## 傍晚回复模板（请尽量按这个回老师）

```
完成度：全部完成 / 部分完成（卡在：…） / 请假
今日做了：…
测验：
1. …
2. …
3. …
```
