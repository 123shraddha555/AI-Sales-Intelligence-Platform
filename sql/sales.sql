CREATE DATABASE sales_intelligence;
SHOW DATABASES;
USE sales_intelligence;
SELECT DATABASE();

CREATE TABLE sales (
    row_id INT,
    order_id VARCHAR(50),
    order_date DATE,
    ship_date DATE,
    ship_mode VARCHAR(50),
    customer_id VARCHAR(50),
    customer_name VARCHAR(100),
    segment VARCHAR(50),
    country VARCHAR(50),
    city VARCHAR(100),
    state VARCHAR(100),
    postal_code VARCHAR(20),
    region VARCHAR(50),
    product_id VARCHAR(50),
    category VARCHAR(50),
    sub_category VARCHAR(50),
    product_name VARCHAR(255),
    sales DECIMAL(12,3),
    quantity INT,
    discount DECIMAL(5,2),
    profit DECIMAL(12,3),
    order_year INT,
    order_month INT,
    order_quarter INT,
    shipping_days INT
);

SHOW TABLES;

SELECT COUNT(*) AS total_rows
FROM sales;

SELECT * FROM sales LIMIT 5;

-- verify row count
SELECT COUNT(*) AS total_rows FROM sales;


-- test a real SQL analysis query
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY category
ORDER BY total_sales DESC;


-- Region Performance
SELECT
    region,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY region
ORDER BY total_sales DESC;

-- Find loss-making sub-categories
SELECT
    sub_category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY sub_category
HAVING SUM(profit) < 0
ORDER BY total_profit ASC;

-- Monthly sales trend
SELECT
    order_year,
    order_month,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY order_year, order_month
ORDER BY order_year, order_month;

-- check the highest-selling products
SELECT
    product_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY product_name
ORDER BY total_sales DESC
LIMIT 10;

-- profit margin by category
SELECT
    category,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit,
    ROUND((SUM(profit) / SUM(sales)) * 100, 2) AS profit_margin
FROM sales
GROUP BY category
ORDER BY profit_margin DESC;


-- top 10 customers by sales.
 SELECT
    customer_name,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY customer_name
ORDER BY total_sales DESC
LIMIT 10;


-- which states generate the highest sales and profit.
SELECT
    state,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY state
ORDER BY total_sales DESC
LIMIT 10;

-- top loss-making states
SELECT
    state,
    SUM(sales) AS total_sales,
    SUM(profit) AS total_profit
FROM sales
GROUP BY state
HAVING SUM(profit) < 0
ORDER BY total_profit ASC;

SELECT
    order_id,
    sales,
    profit,
    CASE
        WHEN profit >= 100 THEN 'High Profit'
        WHEN profit >= 0 THEN 'Low Profit'
        ELSE 'Loss'
    END AS profit_category
FROM sales
LIMIT 20;

-- Count each profit category
SELECT
    CASE
        WHEN profit >= 100 THEN 'High Profit'
        WHEN profit >= 0 THEN 'Low Profit'
        ELSE 'Loss'
    END AS profit_category,
    COUNT(*) AS order_count
FROM sales
GROUP BY profit_category
ORDER BY order_count DESC;

-- first calculate sales and profit for every category, then calculate the profit margin from that result.
WITH category_summary AS (
    SELECT
        category,
        SUM(sales) AS total_sales,
        SUM(profit) AS total_profit
    FROM sales
    GROUP BY category
)
SELECT
    category,
    total_sales,
    total_profit,
    ROUND((total_profit / total_sales) * 100, 2) AS profit_margin
FROM category_summary
ORDER BY profit_margin DESC;




WITH subcategory_sales AS (
    SELECT
        sub_category,
        SUM(sales) AS total_sales
    FROM sales
    GROUP BY sub_category
)
SELECT
    sub_category,
    total_sales,
    RANK() OVER (ORDER BY total_sales DESC) AS sales_rank
FROM subcategory_sales
ORDER BY sales_rank;



WITH subcategory_sales AS (
    SELECT
        sub_category,
        SUM(sales) AS total_sales
    FROM sales
    GROUP BY sub_category
)
SELECT
    sub_category,
    total_sales,
    ROW_NUMBER() OVER (ORDER BY total_sales DESC) AS row_num
FROM subcategory_sales
ORDER BY row_num;



-- WITH subcategory_sales AS (
--     SELECT
--         sub_category,
--         SUM(sales) AS total_sales
--     FROM sales
--     GROUP BY sub_category
-- )
-- SELECT
--     sub_category,
--     total_sales,
--     DENSE_RANK() OVER (ORDER BY total_sales DESC) AS dense_rank
-- FROM subcategory_sales
-- ORDER BY dense_rank;


SELECT VERSION();


SELECT
    category,
    DENSE_RANK() OVER (ORDER BY category) AS rnk
FROM sales
LIMIT 10;

SELECT
    category,
    DENSE_RANK() OVER (ORDER BY category) AS rnk
FROM sales
LIMIT 10;


WITH product_sales AS (
    SELECT
        category,
        product_name,
        SUM(sales) AS total_sales
    FROM sales
    GROUP BY category, product_name
)
SELECT
    category,
    product_name,
    total_sales,
    RANK() OVER (
        PARTITION BY category
        ORDER BY total_sales DESC
    ) AS sales_rank
FROM product_sales;



WITH product_sales AS (
    SELECT
        category,
        product_name,
        SUM(sales) AS total_sales
    FROM sales
    GROUP BY category, product_name
)
SELECT
    category,
    product_name,
    total_sales,
    RANK() OVER (
        PARTITION BY category
        ORDER BY total_sales DESC
    ) AS sales_rank
FROM product_sales;


WITH product_sales AS (
    SELECT
        category,
        product_name,
        SUM(sales) AS total_sales
    FROM sales
    GROUP BY category, product_name
),
ranked_products AS (
    SELECT
        category,
        product_name,
        total_sales,
        RANK() OVER (
            PARTITION BY category
            ORDER BY total_sales DESC
        ) AS sales_rank
    FROM product_sales
)
SELECT
    category,
    product_name,
    total_sales,
    sales_rank
FROM ranked_products
WHERE sales_rank <= 3
ORDER BY category, sales_rank;


-- Top 3 products in each category
WITH product_sales AS (
    SELECT
        category,
        product_name,
        SUM(sales) AS total_sales
    FROM sales
    GROUP BY category, product_name
),
ranked_products AS (
    SELECT
        category,
        product_name,
        total_sales,
        RANK() OVER (
            PARTITION BY category
            ORDER BY total_sales DESC
        ) AS sales_rank
    FROM product_sales
)
SELECT
    category,
    product_name,
    total_sales,
    sales_rank
FROM ranked_products
WHERE sales_rank <= 3
ORDER BY category, sales_rank;