# 学习怎么走（按你的要求定的标准流程）

> **先读 [STANDARDS.md](./STANDARDS.md)**：本仓库只教当前、可维护的现代技术栈；官方文档是事实来源，FastAPI 按当前版本 + Pydantic v2 学习。

```text
git pull
 → 打开 weekN-xxx/dayMM-yyy/
 → 看 VIDEOS.md（视频）+ NOTES.md（知识点文档）
 → 按 README.md 做任务、改本目录代码
 → git commit + push（建议分支 study/weekN-dayMM）
 → 老师 review 你当天提交
 → 工作日 10:00 抽查旧知识决定强化/上新；18:00 验收
```

## 资料与视频硬规则

- 官方文档必须先读，视频只是辅助；冲突时以官方文档和当前代码为准。
- 视频必须为 **2025 年或更新**，或直接使用官方文档；不把旧长课作为主线。
- 每天只看与当天目标直接相关的片段，并遵守当天 45–60 分钟上限。

## 目录约定

- `week1-fastapi/day01-get-post/` … 第 1 周按天
- 每天文件夹内固定三件套：`README.md`（任务） / `NOTES.md`（文档） / `VIDEOS.md`（视频）
- `progress/TODAY.md`：当天实课指针（指向哪个 day 文件夹）

## 老师每天 review 什么

1. 你是否推送到对应 day 目录
2. 代码能否跑通、测试是否合理
3. 是否只改了作业范围、有没有提交 `.venv`
4. 需要改进的点（命名、错误处理、多余代码）