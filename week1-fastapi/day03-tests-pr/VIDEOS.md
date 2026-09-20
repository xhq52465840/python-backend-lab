# Day03 视频与资料（测试、PR、当前栈）

## 今天的目标

- 用 FastAPI 官方推荐方式测试接口
- 用现代 pytest 写出覆盖成功与失败路径的测试
- 了解 PR 与 GitHub Actions 的基本概念

总学习时间约 **45–60 分钟**。视频只看与今天任务直接相关的片段，随后开始写测试和开 PR。

## 1）官方文档优先（必读）

### FastAPI 测试

- [FastAPI 测试教程（中文）](https://fastapi.tiangolo.com/zh/tutorial/testing/)
- [FastAPI Testing（英文当前版，可对照）](https://fastapi.tiangolo.com/tutorial/testing/)

重点掌握 `TestClient`、测试函数、状态码断言，以及对 404 等失败路径的覆盖。

### pytest

- [pytest 官方文档](https://docs.pytest.org/en/stable/)
- [pytest 入门：写第一个测试](https://docs.pytest.org/en/stable/getting-started.html)

只学习今天需要的 `test_` 函数、断言、失败输出和最小 fixture；不要为看视频而引入过时测试写法。

### GitHub Actions（仅概念）

- [GitHub Actions：了解 GitHub Actions](https://docs.github.com/zh/actions/get-started/understand-github-actions)
- [GitHub Actions：快速入门](https://docs.github.com/zh/actions/quickstart)

只做近期概念导入，最多 **20–30 分钟**：workflow、job、step、触发器，以及 PR 如何触发检查。今天不深入复杂部署、矩阵或自托管 runner。

## 2）中文主线（推荐）

**【2026 最新版】FastAPI 从入门到实战**  
https://www.bilibili.com/video/BV19CFYzwE3J/

只看与今天直接相关的测试、pytest、接口验证和 PR/CI 入门片段；跳过 CRUD 重复内容、数据库和部署。建议观看约 **20–30 分钟**，剩余时间用于官方文档和实作；全日仍不超过 45–60 分钟。

## 3）英文替代短课

**FastAPI Crash Course 2025**  
https://www.youtube.com/watch?v=nWWPlEO0he8

只在需要另一种解释时看其中与测试、接口验证或错误响应直接相关的部分；不要重复观看无关 CRUD 内容。官方 FastAPI/pytest 文档优先。

## 4）旧长课降级说明

**OUTDATED RISK / 仅可选，不是主线：** freeCodeCamp 19 小时课程  
https://www.youtube.com/watch?v=0sOvCWFmrtA

如确实需要补充，只能截取测试相关片段，不要整课观看。其依赖和 API 写法可能过时；若与官方测试文档、当前 pytest 或本仓库代码冲突，**以官方文档为准**。