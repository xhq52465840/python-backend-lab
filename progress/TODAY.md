# 今日实课 · 2026-09-25（周五 · 继续补课）

> 类型：**补交 / 强化 Day01**（不上 Day02）  
> 目录：`week1-fastapi/day01-get-post/`

## 原因
截至今天上午：GitHub 仍只有 `main`，无 `study/week1-day01`；9/21–24 仅 chore 更新了 `progress/TODAY.md`，Day01 代码与清单仍未交付。继续还债，稳住再开新课。

## 清单
1. [ ] `git pull`
2. [ ] 先读本目录 `NOTES.md` + `VIDEOS.md`「必读文档」（视频仅文档卡壳时可选）
3. [ ] 实现 `GET /todos`、`POST /todos`（内存 `fake_db`）
4. [ ] 自测：POST→GET；缺 `title` → 422；`/health` ok
5. [ ] push 分支 `study/week1-day01`
6. [ ] 老师 review；并回复上午抽查题

## 验收
- `/health` ok
- GET 返回数组；POST 201 + 自增 id
- 非法 body / 缺 title → 422
- GitHub 能看到 `study/week1-day01` 提交
