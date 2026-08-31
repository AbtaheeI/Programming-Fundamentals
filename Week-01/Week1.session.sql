
-- ============================================================
-- Week 1 · Joins practice
-- Run schema.sql first.
--
-- Write each query below its comment. Predict the row count
-- BEFORE you run it, and write your prediction down.
-- ============================================================


-- ------------------------------------------------------------
-- PART 1 — INNER JOIN
-- ------------------------------------------------------------

-- 1. Every order with the name of the customer who placed it.
--    PREDICT: how many rows? Which customer is missing, and why?

-- SELECT name
-- FROM customers c INNER JOIN orders o ON c.id = o.customer_id


-- 2. All orders placed by Australian customers.

-- SELECT name
-- FROM customers c INNER JOIN orders o ON c.id = o.customer_id
-- WHERE LOWER(country) = 'australia'


-- 3. Total amount spent per customer. Only customers who have ordered.

-- SELECT customer_id, SUM(o.amount)
-- FROM customers c INNER JOIN orders o ON c.id = o.customer_id
-- GROUP BY customer_id



-- ------------------------------------------------------------
-- PART 2 — LEFT JOIN
-- ------------------------------------------------------------

-- 4. Every customer, with their order details where they exist.
--    PREDICT: how many rows now? What appears in the order
--    columns for the customer with no orders?

-- SELECT *
-- FROM customers c LEFT orders o ON c.id = o.customer_id
-- WHERE o.order_date IS NOT NULL

-- 5. Same as above, but only Australian customers.
--    Think: does this condition go in ON or WHERE?
-- Goes on the where because it's a condition on the left table and not the right

-- SELECT *
-- FROM customers c LEFT JOIN orders o ON c.id = o.customer_id
-- WHERE o.order_date IS NOT NULL AND country = 'Australia'


-- 6. Every customer, with their Coat order attached if they
--    bought one. Customers who bought no coat must still appear.
--    This is the filter trap. Get the placement right.

-- SELECT *
-- FROM customers c LEFT JOIN orders o ON c.id = o.customer_id and o.product = 'Coat'



-- ------------------------------------------------------------
-- PART 3 — RIGHT JOIN
-- ------------------------------------------------------------

-- 7. Every order, with customer details where they exist.
--    PREDICT: which order shows NULL customer columns, and why?



-- 8. Rewrite query 7 as a LEFT JOIN with the same result.
--    (This is why most codebases never use RIGHT JOIN.)




-- ------------------------------------------------------------
-- PART 4 — The anti-join
-- ------------------------------------------------------------

-- 9. Customers who have never placed an order.
--    Which orders column do you test for NULL? Pick one that
--    could never legitimately be NULL on a real matched row.




-- 10. Orders whose customer no longer exists (orphaned rows).




-- ------------------------------------------------------------
-- PART 5 — COUNT and the phantom row
-- ------------------------------------------------------------

-- 11. Every customer with the number of orders they have placed.
--     Customers with none must show 0.




-- 12. Run query 11 again, but with COUNT(*) instead of
--     COUNT(<column>). Compare the two results for Priya.
--     Write down which returns 0, which returns 1, and why.




-- 13. Every customer with their total spend. Customers with no
--     orders should show 0, not NULL.
--     (You need a function that substitutes a value for NULL.
--      Look up COALESCE.)




-- ------------------------------------------------------------
-- PART 6 — Stretch
-- ------------------------------------------------------------

-- 14. Customers who have bought a Coat, using only a join.
--     Watch for duplicates.




-- 15. For each city, how many customers and how many total
--     orders. Cities with customers but no orders must appear.




-- 16. Every customer with the amount of their single largest
--     order. Customers with no orders show NULL.