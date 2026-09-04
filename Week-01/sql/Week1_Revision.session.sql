-- Customers who have never placed an order.
-- Orders whose customer no longer exists.
-- Every customer with the number of orders they've placed — customers with none showing 0.
-- Every customer, with their Coat order attached if they bought one. Customers who bought no coat must still appear.
-- For each city, how many customers and how many total orders. Cities with customers but no orders must appear.


-- Q1
-- SELECT *
-- FROM customers c LEFT JOIN orders o ON c.id = o.customer_id
-- WHERE o.id IS NULL

-- Q2
-- SELECT *
-- FROM customers c LEFT JOIN orders o ON c.id = o.customer_id
-- WHERE c.id IS NULL

-- Q3 
-- SELECT c.id, COUNT(o.id)
-- FROM customers c LEFT JOIN orders o ON c.id = o.customer_id
-- GROUP BY c.id

-- Q4
-- SELECT c.id, o.product
-- FROM customers c LEFT JOIN orders o ON c.id = o.customer_id AND o.product = 'Coat'

-- Q5
-- SELECT c.city, COUNT(DISTINCT(c.id)),COUNT(o.id)
-- FROM customers c LEFT JOIN orders o ON c.id = o.customer_id
-- GROUP BY c.city

