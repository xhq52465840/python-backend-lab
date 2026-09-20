# Day 04 · Postgres 跑起来

**阶段**：A2 · week2

## 清单
1. 视频：库/表/主键概念
2. `cd week2-postgres && cp .env.example .env && docker compose up -d`
3. `pip install -r requirements.txt && alembic upgrade head`
4. `uvicorn app.main:app --reload`，检查 `GET /health`

## 验收
- [ ] `docker compose exec db psql -U todolab -d todolab -c '\\dt'` 看到 users/todos
- [ ] health 返回 db up
