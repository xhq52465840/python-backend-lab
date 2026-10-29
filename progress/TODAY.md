# 今日实课 · 2026-10-29（周四 · 继续收尾 Day01）

> 类型：**Day01 收尾 + 补弱**（`study/week1-day01` 自 10/27 傍晚 1c0abec 后没有新提交，昨天的任务原样顺延；暂不上 Day02）  
> 目录：`week1-fastapi/day01-get-post/`

## 原因
昨天的 review 3 点和 `GET/POST /todos` 主任务都还没提交。Day01 没验收就上 Day02，后面的 CRUD 会站不稳，所以今天还是把 Day01 做完。今天任务量和昨天一样，3 小时内能做完。

## 先读文档（视频仅文档卡壳时可选，见本目录 `VIDEOS.md`）
- 本目录 `NOTES.md`
- 官方：Request Body（Pydantic `BaseModel` 做请求体）
- 官方：Query Parameters and String Validations（`Annotated[int, Query(ge=1, le=100)]`）
- 官方：Path Parameters → Predefined values（Enum 比较、`.value`）
- 官方：Response Model / Response Status Code（`response_model`、`status_code=201`）

## 第 1 步 · 修 review 的 3 个点（约 40 分钟）
1. `item_id is ItemInt.THIRTY_THREE` → 改成 `==`，或直接把参数类型声明成 `ItemInt`
2. POST 请求体用 `dict` → 改成 Pydantic `BaseModel`
3. 分页参数用 `Annotated[int, Query(ge=1)]` 校验；`pageSize` 给默认值，不要 `int | None`

## 第 2 步 · Day01 主任务（约 1.5 小时）
- `GET /todos` 返回列表（内存 `fake_db`），`response_model=list[Todo]`
- `POST /todos`：`TodoCreate(BaseModel)` 做请求体，`response_model=Todo`，`status_code=201`，自增 id
- 用 `/docs` 手动测：POST → GET；缺 `title` → 422

## 第 3 步 · 提交（约 20 分钟）
- 在 `study/week1-day01` 上 commit + push（先 `git pull`；分支落后 main 就 `git merge origin/main` 同步）
- 做到一半也先 push 一次，方便我 review
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
- 验收通过 → 明天（周五）上 Day02
