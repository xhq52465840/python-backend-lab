# python-backend-lab

## 新课程流程（按天进入并提交）

本仓库现在按“周 → 天”组织课程。每天只在对应的 day 文件夹内学习和提交：

1. `git pull`
2. 打开当天目录，例如 `week1-fastapi/day01-get-post/`
3. 按顺序阅读 `VIDEOS.md`、`NOTES.md`，再执行 `README.md` 中的任务
4. 在当天目录修改代码并完成自测
5. `git add`、`git commit`、`git push`
6. 老师根据当天提交的 commits review

详细说明见 [LEARNING_FLOW.md](./LEARNING_FLOW.md)，第 1 周课程见 [week1-fastapi/](./week1-fastapi/)，当天指针见 [progress/TODAY.md](./progress/TODAY.md)。

资深前端 → Python 后端 → 全栈 → Agent 专家 的跟练仓库。

## 先看这个（详细总路线）

**[PATH.md](./PATH.md)** —— 按你的背景写的完整路线：验收标准、周计划、视频、作业、与 [ai-agent-book](https://github.com/bojieli/ai-agent-book) 的衔接。

**[DAILY_PLAN.md](./DAILY_PLAN.md)** —— 每天 3 小时的具体学习节奏、前 14 天任务与阶段出口。

简版周计划仍见 [COURSE.md](./COURSE.md)。

## 你现在立刻做

1. 打开 `progress/TODAY.md`，确认当天 day 目录
2. 进入 `week1-fastapi/day01-get-post/`，按 `VIDEOS.md`、`NOTES.md`、`README.md` 的顺序学习
3. 完成 TODO 后提交并 push，等待老师 review commits
4. 按 [DAILY_PLAN.md](./DAILY_PLAN.md) 每天完成 3 小时学习与复盘

## 本地跑第 1 周

```bash
git clone https://github.com/xhq52465840/python-backend-lab.git
cd python-backend-lab/week1-fastapi/day01-get-post
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

打开 http://127.0.0.1:8000/docs

## 目录

| 路径 | 内容 |
|------|------|
| `PATH.md` | **详细总路线（主文档）** |
| `DAILY_PLAN.md` | 每天 3 小时的学习计划 |
| `COURSE.md` | 简版周计划与视频链接 |
| `curriculum/` | 按天课表与验收说明 |
| `progress/TODAY.md` | 抽查后更新的当天实课 |
| `LEARNING_FLOW.md` | 按天学习、提交与 review 的固定流程 |
| `week1-fastapi/` | 第 1 周：按 day 文件夹组织的 FastAPI 课程 |
| `week1-fastapi-crud/` | 第 1 周旧目录，保留作参考 |
| `week2-postgres/` | 第 2 周：完整的 PostgreSQL + SQLAlchemy + Alembic + FastAPI 骨架（不再是占位目录） |
| `week3-auth-tests/` | 鉴权与测试占位 |
| `week4-docker-cicd/` | Docker + CI/CD 占位 |
| `.github/workflows/ci.yml` | 起步 CI |

`week2-postgres/` 已包含 Docker Compose 数据库、SQLAlchemy 模型与 Session、Alembic 初始迁移、FastAPI 健康检查、SQL 练习和起步测试；接下来按其中的 TODO 完成 CRUD 与第二次迁移。

## 最终目标对齐

1. 普通 Python 后端工程师（API + Postgres + 测试 + Compose + Actions + 本地部署）
2. 全栈（前端优势接自己的后端）
3. 精读并实践 [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)，精通 Agent 工程
