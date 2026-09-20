# 今日实课 · 2026-09-20（周日）

> 今日学习目录：`week1-fastapi/day01-get-post/`

## 固定流程

`git pull` → 进入 `week1-fastapi/day01-get-post/` → 阅读 `VIDEOS.md` + `NOTES.md` + `README.md` → 完成任务并自测 → `git add` / `git commit` / `git push` → 老师 review 当天 commits。

## 今日清单

1. [ ] `git pull`
2. [ ] 进入 `week1-fastapi/day01-get-post/`
3. [ ] 看完 `VIDEOS.md`，读完 `NOTES.md`，再按 `README.md` 操作
4. [ ] 跑通 FastAPI `/docs`，实现 `GET /todos` 与 `POST /todos`
5. [ ] 自测：创建后能列表，非法 body 返回 422
6. [ ] 提交并 push
7. [ ] 等老师 review commits

## 验收标准

- [ ] `/health` 仍返回 `{"status": "ok"}`
- [ ] `GET /todos` 返回数组
- [ ] `POST /todos` 返回 201 并带自增 id
- [ ] 非法 JSON 或缺少 `title` 返回 422
