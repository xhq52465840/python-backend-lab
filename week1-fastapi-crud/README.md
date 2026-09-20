# Week 1 — FastAPI 内存版待办 API

目标：不碰数据库，先把 HTTP API 写顺。

## 启动

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

打开 http://127.0.0.1:8000/docs 自己点一点。

## 已提供

- `GET /health` — 健康检查（已写好，CI 会测）
- `Todo` 模型骨架
- 内存列表 `fake_db`

## 你的 TODO（按顺序做）

1. `GET /todos` — 返回全部待办
2. `POST /todos` — 创建（title 必填，completed 默认 false）
3. `GET /todos/{todo_id}` — 查一条；不存在返回 404
4. `PUT /todos/{todo_id}` — 更新 title / completed
5. `DELETE /todos/{todo_id}` — 删除；不存在返回 404
6. 给上述接口补上 pytest（可参考 `tests/test_health.py`）

做完后：

```bash
pytest
git checkout -b week1-done
git add .
git commit -m "week1: finish in-memory todo CRUD"
git push -u origin week1-done
```

然后在 GitHub 开 PR，看 Actions 是否绿灯。
