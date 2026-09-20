# Week 2 — PostgreSQL + SQLAlchemy + Alembic

目标：把 Week 1 的内存待办换成 **真数据库**；学会迁移、JOIN、事务、索引。

> 建议：Week 1 CRUD 先做完再深啃本周。若 Week 1 未完成，可先起 Postgres 练 SQL（见 `sql/practice.sql`）。

## 你会学到什么

1. 用 Docker Compose 起 PostgreSQL
2. SQLAlchemy 2.x 模型与 Session
3. Alembic 迁移（建表 → 改表）
4. FastAPI 依赖注入拿到 DB session
5. 手写 SQL 练习（JOIN / 聚合 / 事务 / EXPLAIN）

## 0. 准备

需要本机已装 Docker Desktop（或 Docker Engine + Compose）。

```bash
cd week2-postgres
cp .env.example .env
docker compose up -d
# 等几秒，确认库起来：
docker compose ps
```

Python 环境：

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
```

跑迁移（第一次）：

```bash
alembic upgrade head
```

起 API：

```bash
uvicorn app.main:app --reload
```

打开 http://127.0.0.1:8000/docs

停库：`docker compose down`（数据在 volume 里，一般会保留；若加 `-v` 会删数据）。

## 目录说明

| 路径 | 作用 |
|------|------|
| `docker-compose.yml` | Postgres 16 |
| `app/models.py` | User / Todo 表映射（已给） |
| `app/db.py` | engine / Session |
| `app/schemas.py` | Pydantic 入参出参 |
| `app/routers/todos.py` | **你的主战场：CRUD TODO** |
| `alembic/` | 迁移工具；已有初始迁移 |
| `sql/practice.sql` | 必做 SQL 题 |
| `tests/` | 起步测试 |

## 你的 TODO（按顺序）

### A. 跑通骨架（今晚就能做）

- [ ] `docker compose up -d` 成功
- [ ] `alembic upgrade head` 成功
- [ ] `GET /health` 返回 ok，且能连上库（见实现）
- [ ] 用 `psql` 或任意 GUI 看到 `users` / `todos` 表

连接串（与 `.env.example` 一致）：

`postgresql+psycopg://todolab:todolab@localhost:5432/todolab`

进库示例：

```bash
docker compose exec db psql -U todolab -d todolab
\\dt
\\q
```

### B. 实现待办 CRUD（落库）

在 `app/routers/todos.py` 把标了 `TODO` 的函数补全：

- [ ] `GET /todos` — 列表（可先不做分页）
- [ ] `POST /todos` — 创建（本周可暂时用固定 `user_id=1`，见下方种子用户）
- [ ] `GET /todos/{id}` — 404 处理
- [ ] `PUT /todos/{id}` — 更新
- [ ] `DELETE /todos/{id}` — 删除
- [ ] 重启 API 后数据仍在（证明不是内存）

种子用户：首次启动时 `main.py` 会确保存在 `id=1` 的演示用户（email=`demo@example.com`）。Week 3 再换成真正注册登录。

### C. 第二次迁移（练 Alembic）

- [ ] 给 `todos` 加一列 `priority`（Integer，默认 0）
- [ ] `alembic revision --autogenerate -m "add todo priority"`
- [ ] 检查生成的文件，再 `alembic upgrade head`
- [ ] 更新 schema / 路由支持 priority

### D. SQL 必练（`sql/practice.sql`）

在 `psql` 里做完并保留你的答案（可另存 `sql/my-answers.sql`，**不要提交密码**）。

### E. 出门考试

画出「用户-文章-标签（多对多）」ER 图，写出建表 SQL + 该加的索引及原因。把答案放到 `sql/er-blog.md`（可选提交）。

## 视频（跟做）

1. freeCodeCamp API 课里的 Postgres + SQLAlchemy 段：https://www.youtube.com/watch?v=0sOvCWFmrtA
2. PostgreSQL 全课：https://www.youtube.com/watch?v=qw--VYLpxG4
3. W3Schools 练习：https://www.w3schools.com/postgresql/

## 提交

```bash
git checkout -b week2-done
# ...完成 TODO...
git add week2-postgres
git commit -m "week2: persist todos with postgres"
git push -u origin week2-done
```

然后开 PR。
