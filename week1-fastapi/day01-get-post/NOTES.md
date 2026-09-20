# Day01 知识点文档

## 1. FastAPI 是什么
用 Python 写 HTTP API 的框架。你写「路径 + 函数」，它负责把请求解析成参数，把返回值变成 JSON，并自动生成 `/docs`（OpenAPI/Swagger）。

前端类比：有点像用框架写后端路由，而不是手写一堆 `http.createServer`。

## 2. 路径操作（Path Operation）
```python
@app.get("/todos")
def list_todos():
    ...
```
- `get/post/put/delete` 对应 HTTP 方法
- `"/todos"` 是路径
- 函数返回的 dict/list/Pydantic 模型会变成响应体

## 3. Pydantic 模型
用来描述「请求体长什么样」：
```python
class TodoCreate(BaseModel):
    title: str
    completed: bool = False
```
请求进来时 FastAPI 会校验；不合法直接 **422**，进不了你的业务函数。

和 TypeScript 的差别：
- TS：主要在**编译你的前端代码**时检查
- Pydantic：在**服务器运行时**检查任何人发来的 JSON（含 curl）

## 4. 状态码（今天用到的）
- `200` 成功（默认 GET）
- `201` 创建成功（POST 常用）
- `422` 请求体校验失败

## 5. 内存 `fake_db`
今天数据放在进程内存的 list 里。重启进程数据会丢——这是刻意的，第 2 周再换成 Postgres。

## 6. 自测怎么做
用 `/docs` 点 Try it out，或：
```bash
curl -s http://127.0.0.1:8000/todos
curl -s -X POST http://127.0.0.1:8000/todos -H 'Content-Type: application/json' -d '{"title":"hi"}'
```
