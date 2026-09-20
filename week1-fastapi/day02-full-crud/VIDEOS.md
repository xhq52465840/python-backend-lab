# Day02 视频与资料（当前栈、短时分段）

> 文档优先，视频可选；官方文档先于视频。

## 今天的目标

- 路径参数：`/todos/{todo_id}`
- `PUT` 更新与 `DELETE` 删除
- 正确返回状态码
- 找不到资源时返回 `404`

总观看与阅读时间控制在约 **45–60 分钟**；到点就开始做代码，不要 binge 长课。

## 1）官方文档优先（必读）

官方文档是当前 FastAPI 的事实来源，先读与今天任务直接相关的部分：

- [路径参数](https://fastapi.tiangolo.com/zh/tutorial/path-params/)
- [响应状态码](https://fastapi.tiangolo.com/zh/tutorial/response-status-code/)
- [错误处理与 `HTTPException`](https://fastapi.tiangolo.com/zh/tutorial/handling-errors/)
- [更新请求体（PUT）](https://fastapi.tiangolo.com/zh/tutorial/body-updates/)

重点确认：路径参数如何校验、`status_code` 如何声明、资源不存在时如何抛出 `HTTPException(status_code=404, ...)`，以及 PUT 的更新语义。

## 2）中文主线（推荐）

**【2026 最新版】FastAPI 从入门到实战**  
https://www.bilibili.com/video/BV19CFYzwE3J/

只看今天相关的片段：路径参数、按 ID 获取资源、PUT 更新、DELETE 删除、状态码和 404/异常处理。跳过环境安装、数据库及与今天作业无关的内容；视频观看最多约 **45–60 分钟**。

## 3）英文替代短课

**FastAPI Crash Course 2025**  
https://www.youtube.com/watch?v=nWWPlEO0he8

只看其中与路径参数、CRUD 更新/删除、状态码和错误响应直接相关的部分。它是替代路线，不需要与中文主线重复观看；仍以官方文档为准。

## 4）旧长课降级说明

**OUTDATED RISK / 仅可选，不是主线：** freeCodeCamp 19 小时课程  
https://www.youtube.com/watch?v=0sOvCWFmrtA

如确实需要另一种讲法，只能截取 GET-one、PUT、DELETE 的相关片段，不能整课观看。其 API 写法可能过时；若与官方文档、Pydantic v2 或本仓库代码冲突，**立即以官方文档为准**。