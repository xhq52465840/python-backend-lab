# Day03 知识点文档

## 1. 为什么要自动化测试
`/docs` 手点会漏；pytest 保证你改代码后旧行为还在。CI 在云端再跑一遍，避免「我机器能跑」。

## 2. TestClient
```python
from fastapi.testclient import TestClient
client = TestClient(app)
r = client.post("/todos", json={"title": "x"})
```
不需要真的起服务器端口。

## 3. 测试隔离
每个测试前清空 `fake_db`，避免顺序污染。

## 4. PR 与 CI
Push 到分支 → 开 Pull Request → `.github/workflows` 里的任务自动跑。老师 review 看：测试是否充分、命名是否清楚、有没有把 `.venv` 提交上来。
