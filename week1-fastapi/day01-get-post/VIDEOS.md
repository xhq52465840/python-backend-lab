# Day01 视频与资料（以「现在能用」为准）

## 先说结论

- **作业代码**已经按当前栈：FastAPI 新版本 + **Pydantic v2**（见本目录 `requirements.txt`）。
- **权威来源**永远是官方文档（持续更新），视频只是带路。
- 旧长课（例如 2021 年 freeCodeCamp 19h）里的**思路还在**（路由、校验、文档），但个别 API 写法可能过时（如 Pydantic v1 的 `.dict()` → v2 的 `model_dump()`）。**Day01 不要以它为主。**

## 今天上限：约 45–60 分钟

到点就停，去做本目录代码。

---

## 1）必读（比任何视频都新）· 约 20–30 分钟

官方中文教程（跟当前版本走）：

1. First Steps：https://fastapi.tiangolo.com/zh/tutorial/first-steps/
2. 路径操作入门：https://fastapi.tiangolo.com/zh/tutorial/first-steps/
3. Request Body（Pydantic 模型）：https://fastapi.tiangolo.com/zh/tutorial/body/

读的时候对照本目录 `NOTES.md` + `app/main.py`。

---

## 2）主视频（二选一，新课优先）

### 选项 A · 中文（2025/2026 向，推荐你）

**【2026最新版】FastAPI 从入门到实战**  
https://www.bilibili.com/video/BV19CFYzwE3J/

今天只看：`01 介绍` → `02 环境` → `03 第一个程序` → `05～07 路径/查询/请求体` 相关开头。  
**合计约 45～60 分钟就停。**

备选（黑马，2025-12 更新说明）：  
https://www.bilibili.com/video/BV1zV2QBtE39/  
同样只看导学 + 第一个程序 + 路由/Pydantic 开头。

### 选项 B · 英文短课（2025）

**FastAPI Crash Course 2025（约 42 分钟）**  
https://www.youtube.com/watch?v=nWWPlEO0he8

可整集看完，或看到 GET/POST + `/docs` 清楚即可。

---

## 3）可选补充（短）

- Pydantic 为何重要（2024，偏概念）：https://www.youtube.com/watch?v=502XOB0u8OY
- Real Python 文字入门（2025 更新）：https://realpython.com/get-started-with-fastapi/

---

## 4）降级 / 不要当主教材

~~freeCodeCamp 19 小时长课（约 2021）~~  
https://www.youtube.com/watch?v=0sOvCWFmrtA  

仅作以后「多听一种讲法」的可选材料；若与官方文档或本仓库代码冲突，**以官方文档 + 本仓库代码为准**。
