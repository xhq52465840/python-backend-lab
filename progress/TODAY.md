# 今日实课 · 2026-10-28（周三 · 收尾 Day01）

> 类型：**Day01 收尾 + 补弱**（半熟：先修昨天 review 的问题，再完成主任务；暂不上 Day02）  
> 目录：`week1-fastapi/day01-get-post/`

## 原因
昨天傍晚你推了 `study/week1-day01`（1c0abec「第一天demo」），路径参数、Enum、路由顺序、分页都练到了，没有用过时 API，很好 👍。  
但 Day01 主任务 `GET/POST /todos` 还没做，review 里也有几处要改，所以今天按「半熟」处理：先补弱，再收尾主任务。

## 先读文档（视频仅文档卡壳时可选）
- 本目录 `NOTES.md`
- 官方：Request Body（Pydantic `BaseModel` 做请求体）
- 官方：Query Parameters and String Validations（`Query(ge=1)` 等校验）
- 官方：Path Parameters → Predefined values（Enum 比较）

## 第 1 步 · 修昨天 review 的 3 个点（约 40 分钟）
1. `item_id is ItemInt.THIRTY_THREE` → 改成 `==`，或直接把参数类型声明成 `ItemInt`
2. POST 请求体用 `dict` → 改成 Pydantic `BaseModel`
3. 分页参数加 `Query(ge=1)` 校验；`pageSize` 给默认值，不要 `int | None`

## 第 2 步 · Day01 主任务（约 1.5 小时）
- `GET /todos` 返回列表（内存 `fake_db`）
- `POST /todos`：`TodoCreate(BaseModel)` 做请求体，`status_code=201`，自增 id
- 用 `/docs` 手动测：POST → GET；缺 `title` → 422

## 第 3 步 · 提交（约 20 分钟）
- 继续在 `study/week1-day01` 上 commit + push（先 `git pull`，分支落后 main 的话按昨天巩固题方法同步）
- 卡住超过 20 分钟：先回官方文档对应小节，仍不行把报错贴过来

## 清单
1. [ ] `git pull`，切到 `study/week1-day01`
2. [ ] 读上面文档
3. [ ] 修 review 的 3 点
4. [ ] 实现 `GET /todos`、`POST /todos`
5. [ ] 自测：POST→GET；缺 `title` → 422；`/health` ok
6. [ ] push；回复上午抽查题

## 验收（傍晚）
- GET 返回数组；POST 201 + 自增 id；缺 title → 422
- review 3 点已修
- 验收通过 → 明天上 Day02
