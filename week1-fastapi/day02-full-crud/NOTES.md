# Day02 知识点文档

## 1. 路径参数
```python
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    ...
```
`todo_id` 从 URL 解析，类型不对会 422。

## 2. 404 Not Found
资源不存在时：
```python
raise HTTPException(status_code=404, detail="Todo not found")
```

## 3. PUT 与部分更新
可以用一个 `TodoUpdate`，字段全是 Optional；只更新客户端传来的非 None 字段。

## 4. DELETE 与 204
删除成功常用 `204 No Content`，响应体为空。

## 5. 幂等（复习）
- GET：可重复，不改状态
- PUT：同一请求重复，结果应一致
- POST：重复可能创建多条
- DELETE：删一次与再删（已不存在）的语义要约定（今天：不存在 → 404）
