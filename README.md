# python-backend-lab

资深前端 → Python 后端 → 全栈 → Agent 专家 的跟练仓库。

## 先看这个（详细总路线）

**[PATH.md](./PATH.md)** —— 按你的背景写的完整路线：验收标准、周计划、视频、作业、与 [ai-agent-book](https://github.com/bojieli/ai-agent-book) 的衔接。

简版周计划仍见 [COURSE.md](./COURSE.md)。

## 你现在立刻做

1. 打开 `PATH.md` 第 13 节「现在立刻做什么」
2. 进入 `week1-fastapi-crud/` 按 README 完成 TODO
3. 开 PR，看 GitHub Actions 是否绿灯

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
| `COURSE.md` | 简版周计划与视频链接 |
| `week1-fastapi-crud/` | 第 1 周：内存版待办 API |
| `week2-postgres/` | 数据库周占位 |
| `week3-auth-tests/` | 鉴权与测试占位 |
| `week4-docker-cicd/` | Docker + CI/CD 占位 |
| `.github/workflows/ci.yml` | 起步 CI |

## 最终目标对齐

1. 普通 Python 后端工程师（API + Postgres + 测试 + Compose + Actions + 本地部署）
2. 全栈（前端优势接自己的后端）
3. 精读并实践 [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)，精通 Agent 工程
