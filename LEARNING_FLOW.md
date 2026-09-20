# 学习怎么走

> 先读 [STANDARDS.md](./STANDARDS.md)。

## 材料优先级（你提的，已定为标准）

1. **文档为主**：官方文档 + 当天 `NOTES.md` + 仓库代码（可保证跟现行版本）
2. **视频为辅**：只有文档看不懂、需要演示时才看；视频无法保证永远最新
3. **冲突时**：永远听文档和本仓库可运行代码，不听旧视频里的过时 API

## 每天操作流程

```text
git pull
 → 打开 weekN-xxx/dayMM-yyy/
 → 先读 NOTES.md + VIDEOS.md 里的「必读文档」链接
 → 文档不够再看短视频（可选）
 → 按 README.md 做任务、改本目录代码
 → git commit + push（建议 study/weekN-dayMM）
 → 老师 review 提交
 → 工作日 10:00 抽查；18:00 验收
```

## 目录约定

- `week1-fastapi/day01-get-post/` … 按周按天
- 每天：`README.md`（任务）/ `NOTES.md`（知识点）/ `VIDEOS.md`（文档链接 + 可选视频）
- `progress/TODAY.md`：当天指针

## 老师 review 什么

提交是否在对应 day 目录、能否跑通、有无过时写法、有没有误交 `.venv`。
