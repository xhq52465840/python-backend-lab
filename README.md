# python-backend-lab

后端 Python（FastAPI）+ 数据库（PostgreSQL）+ CI/CD（GitHub Actions）跟练仓库。

配合视频主线：[freeCodeCamp Python API Development（约 19 小时）](https://www.youtube.com/watch?v=0sOvCWFmrtA)
中文可并行：[黑马 FastAPI 入门到实战](https://www.bilibili.com/video/BV1zV2QBtE39/)

## 怎么用

1. 克隆本仓库
2. 打开 `COURSE.md` 看整体路线
3. 从 `week1-fastapi-crud/` 开始动手
4. 每完成一周，开一个 PR 到 `main`（练 Git + 以后接 CI）

## 目录

| 路径 | 内容 |
|------|------|
| `COURSE.md` | 6–8 周学习计划与视频链接 |
| `week1-fastapi-crud/` | 第 1 周：内存版待办 API |
| `week2-postgres/` | 第 2–3 周占位（接数据库） |
| `week3-auth-tests/` | 第 4–5 周占位（JWT + pytest） |
| `week4-docker-cicd/` | 第 6 周占位（Docker + Actions） |
| `.github/workflows/ci.yml` | 起步 CI：对 week1 跑测试 |

## 本地快速跑第 1 周

```bash
cd week1-fastapi-crud
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

浏览器打开 http://127.0.0.1:8000/docs

## 建议节奏

每天 1–2 小时。卡壳了把报错和代码片段发给助手即可。
