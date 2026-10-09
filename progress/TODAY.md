# 今日实课 · 2026-10-09（周五 · 继续补课）

> 类型：**补交 / 强化 Day01**（不上 Day02）  
> 目录：`week1-fastapi/day01-get-post/`

## 原因
截至今天上午：GitHub 仍只有 `main`，无 `study/week1-day01`；9/21–10/08 仅 chore 更新了 `progress/TODAY.md`，Day01 代码与清单仍未交付。继续还债，稳住再开新课。

## 今天先只求「15 分钟起步」
只要做到下面 3 步就算达标：
1. `git pull` 后建分支 `study/week1-day01`
2. 在 `main.py` 里只写一个 `GET /health` 返回 `{"status": "ok"}`，`uvicorn` 跑起来，浏览器打开 `/docs` 能看到它
3. commit + push —— 老师就能开始 review 了

做完还有劲，再接着写 `GET /todos`（先返回空数组）。

> 节奏需要调整就直接回复老师：每天 1 小时、隔天一课、或者先暂停一周都可以。说一声就行，计划会跟着改。

## 完整做法（约 3 小时，可拆成小块）
- 第 1 小时：读 `NOTES.md` + `VIDEOS.md` 里的「必读文档」（官方文档优先），边读边在本地跑 `/health`
- 第 2 小时：只做 `GET /todos` + `POST /todos`，用 Swagger（`/docs`）手动测
- 第 3 小时：补 422 自测、提交并 push；有余力再回答抽查题
- 卡住超过 20 分钟：先回去看官方文档对应小节，仍不行再看视频片段，或直接把报错贴给老师

## 清单
1. [ ] `git pull`
2. [ ] 先读本目录 `NOTES.md` + `VIDEOS.md`「必读文档」（视频仅文档卡壳时可选）
3. [ ] 实现 `GET /todos`、`POST /todos`（内存 `fake_db`）
4. [ ] 自测：POST→GET；缺 `title` → 422；`/health` ok
5. [ ] push 分支 `study/week1-day01`（哪怕只完成一半也先 push，方便 review）
6. [ ] 老师 review；并回复上午抽查题

## 验收
- `/health` ok
- GET 返回数组；POST 201 + 自增 id
- 非法 body / 缺 title → 422
- GitHub 能看到 `study/week1-day01` 提交
