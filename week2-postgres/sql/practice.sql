-- Week 2 SQL drills. Run inside: docker compose exec db psql -U todolab -d todolab
-- Fill answers below each prompt (or copy to sql/my-answers.sql).

-- Seed (optional if API not ready):
-- INSERT INTO users (id, email, password_hash) VALUES (1, 'demo@example.com', 'x') ON CONFLICT DO NOTHING;
-- INSERT INTO todos (user_id, title, completed) VALUES (1, 'learn sql', false), (1, 'learn index', true);

-- 1) 每个用户未完成待办数量，按数量降序
-- YOUR SQL:


-- 2) 最近 7 天新建的待办
-- YOUR SQL:


-- 3) 演示事务：故意制造错误并 ROLLBACK（写注释说明你观察到什么）
-- BEGIN;
-- ...
-- ROLLBACK;

-- 4) 证明 email UNIQUE：尝试插入重复 email，记录报错信息
-- YOUR NOTES:


-- 5) 软删除设计：写出 ALTER TABLE 加 deleted_at，以及「列表默认过滤已删」的 SELECT
-- YOUR SQL:


-- 6) EXPLAIN：对比 user_id 条件在有/无索引时的计划（ix_todos_user_id 已存在时可 DROP INDEX 再对比，最后加回）
-- EXPLAIN ANALYZE SELECT * FROM todos WHERE user_id = 1;
