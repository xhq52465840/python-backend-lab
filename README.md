# python-backend-lab

## 学习导航（先看）

- **[PATH.md](./PATH.md)**：总路线，说明学习阶段、目标与出口。
- **[DAILY_PLAN.md](./DAILY_PLAN.md)**：日计划总表，按天安排学习节奏与任务。
- **[curriculum/](./curriculum/)**：按天课表，现在就能看，包含每个学习日的目标、清单和验收标准。
- **[progress/TODAY.md](./progress/TODAY.md)**：当天实课，上午抽查后更新；以这里的最终清单作为当天正式任务。
- **[curriculum/ACCEPTANCE.md](./curriculum/ACCEPTANCE.md)**：验收说明，解释抽查分流、晚间验收和阶段出口。

资深前端 → Python 后端 → 全栈 → Agent 专家 的跟练仓库。

## 先看这个（详细总路线）

**[PATH.md](./PATH.md)** —— 按你的背景写的完整路线：验收标准、周计划、视频、作业、与 [ai-agent-book](https://github.com/bojieli/ai-agent-book) 的衔接。

**[DAILY_PLAN.md](./DAILY_PLAN.md)** —— 每天 3 小时的具体学习节奏、前 14 天任务与阶段出口。

简版周计划仍见 [COURSE.md](./COURSE.md)。

## 你现在立刻做

1. 打开 `PATH.md` 第 13 节「现在立刻做什么」
2. 进入 `week1-fastapi-crud/` 按 README 完成 TODO
3. 开 PR，看 GitHub Actions 是否绿灯
4. 按 [DAILY_PLAN.md](./DAILY_PLAN.md) 每天完成 3 小时学习与复盘

## 本地跑第 1 周

```bash
git clone https://github.com/xhq52465840/python-backend-lab.git
cd python-backend-lab/week1-fastapi-crud
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
| `week1-fastapi-crud/` | 第 1 周：内存版待办 API |
| `week2-postgres/` | 第 2 周：完整的 PostgreSQL + SQLAlchemy + Alembic + FastAPI 骨架（不再是占位目录） |
| `week3-auth-tests/` | 鉴权与测试占位 |
| `week4-docker-cicd/` | Docker + CI/CD 占位 |
| `.github/workflows/ci.yml` | 起步 CI |

`week2-postgres/` 已包含 Docker Compose 数据库、SQLAlchemy 模型与 Session、Alembic 初始迁移、FastAPI 健康检查、SQL 练习和起步测试；接下来按其中的 TODO 完成 CRUD 与第二次迁移。

## 最终目标对齐

1. 普通 Python 后端工程师（API + Postgres + 测试 + Compose + Actions + 本地部署）
2. 全栈（前端优势接自己的后端）
3. 精读并实践 [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)，精通 Agent 工程
