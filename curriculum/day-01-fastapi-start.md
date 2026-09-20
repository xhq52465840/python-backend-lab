# Day 01 · FastAPI 起步（默认新课）

**阶段**：A1 · week1  
**时长**：约 3 小时

## 今日目标
跑通 `week1-fastapi-crud`，完成列表与创建。

## 清单
1. 视频：FastAPI 环境与第一个路由、`/docs`（freeCodeCamp 开头或黑马对应段）
2. `cd week1-fastapi-crud && python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
3. `uvicorn app.main:app --reload`，打开 `/docs`
4. 实现 `GET /todos`、`POST /todos`（改 `app/main.py` 里 TODO）

## 验收标准
- [ ] `/docs` 可交互
- [ ] POST 能创建；GET 能看到
- [ ] 非法 body 返回 422

## 若上午抽查判定为强化日
不要上本课；改为重做抽查暴露的薄弱点（老师会写在 `progress/TODAY.md`）。
