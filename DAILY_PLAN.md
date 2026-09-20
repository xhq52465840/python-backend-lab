# 每日学习计划（每天 3 小时）

节奏：每天约 **3 小时** × 7 天 ≈ **21 小时/周**。比原先「每周 10～15 小时」更快，总时长大约压到 **4～6 个月**（仍含 Agent 书与毕业作品）。

每天时间块建议（可按你作息改）：

| 块 | 时长 | 内容 |
|----|------|------|
| 块 1 | 60–75 分 | 看视频 / 读 PATH 对应章节（1.25x，卡点自己敲） |
| 块 2 | 90–100 分 | 动手作业（只认代码与 PR） |
| 块 3 | 20–30 分 | 复盘 + 回答当日测验（助手会出题） |

规则：同一时间只做一个阶段出口；允许用 AI，但关键路径要能自己重写。

---

## 进度状态（自己改勾选）

当前阶段：`A1-week1`（改成你真正在做的：`A0` / `A1-week1` / `A2-week2` / …）

- [ ] A0 Python 自测出门考试通过
- [ ] A1 week1 CRUD + PR CI 绿
- [ ] A2 week2 Postgres + SQL 题 + 第二次迁移
- [ ] A3 鉴权 + ≥10 测试
- [ ] A4 Compose 本地部署 + Actions
- [ ] A5 简历级 API
- [ ] B 全栈对接
- [ ] C0 Agent 预备小实验
- [ ] C1 ai-agent-book 第 1–5 章
- [ ] C2 第 6–7、9–10 章
- [ ] D 毕业作品

---

## 第 1～14 天（后端点火，可按完成情况顺延）

### Day 1（今天可开始）
- 视频：FastAPI 入门 / freeCodeCamp 开头环境段
- 作业：跑通 `week1`；完成 `GET/POST /todos`
- 测验方向：HTTP 方法幂等；Pydantic 和 TypeScript 差在哪

### Day 2
- 视频：路径参数、状态码、自动文档
- 作业：week1 剩余 CRUD + 404
- 测验：422 何时出现

### Day 3
- 作业：week1 pytest 全绿；开 PR
- 出门考试：30 分钟空文件夹笔记 API
- **出口：A1 完成**

### Day 4
- 视频：PostgreSQL 安装与基本 SELECT
- 作业：`week2` `docker compose up`；`alembic upgrade head`；`GET /health`
- 测验：主键 / 外键 / UNIQUE

### Day 5–6
- 视频：SQLAlchemy + FastAPI 依赖注入
- 作业：实现 week2 todos CRUD 落库；证明重启数据仍在
- 测验：Session / commit 是什么

### Day 7
- 作业：SQL `practice.sql` 题 1–3；`EXPLAIN` 看一眼
- 复盘本周 5 条笔记

### Day 8–9
- 作业：Alembic 第二次迁移加 `priority`；更新 API
- SQL 题 4–6
- 测验：迁移与「直接改库」的风险

### Day 10
- 出门考试：博客 ER + 建表 SQL + 索引理由
- **出口：A2 完成**

### Day 11–14
- 视频：JWT + pytest（freeCodeCamp 对应段）
- 作业：开始 week3（注册登录、Bearer、防 IDOR）
- 每天保留 20 分钟测验

（Day 15 起按 `PATH.md` Phase A3→A5→B→C 继续；助手每日提醒会按你的勾选推进。）

---

## 3 小时不够 / 有一天请假

- 最少保底：**45 分钟**只做测验 + 读笔记，不算「断签」但阶段会顺延。
- 请假在对话里说一声，助手会把日计划后移。

---

## 和助手怎么配合

每天提醒到达后，请尽量回复三行：

1. 今天实际学了什么（或「请假」）
2. 作业是否完成（是/否/卡在…）
3. 测验答案

助手会记录进度，并给出明天的具体任务。
