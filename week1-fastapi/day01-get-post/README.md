# Day01 · 跑通 FastAPI + GET/POST

## 今天你要交付什么
在本文件夹内完成内存版待办的 **列表** 与 **创建**，并推送到 GitHub。

## 步骤（按顺序勾）
1. [ ] 看完 `VIDEOS.md` 列出的片段（可 1.25x）
2. [ ] 读完 `NOTES.md`（不懂的词先记下来）
3. [ ] 创建 venv 并安装依赖：
   ```bash
   cd week1-fastapi/day01-get-post
   python -m venv .venv
   source .venv/bin/activate   # Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```
4. [ ] 打开 http://127.0.0.1:8000/docs
5. [ ] 实现 `GET /todos`、`POST /todos`（改 `app/main.py` 里 TODO）
6. [ ] 自测：POST 一条，再 GET 能看到；乱传 body 应 422
7. [ ] 提交推送：
   ```bash
   git checkout -b study/week1-day01
   git add week1-fastapi/day01-get-post
   git commit -m "study(week1-day01): implement GET/POST todos"
   git push -u origin study/week1-day01
   ```

## 验收标准（老师 review 也会看这些）
- `/health` 仍返回 ok
- `GET /todos` 返回数组
- `POST /todos` 返回 201，带自增 id
- 非法 JSON/缺 title → 422
