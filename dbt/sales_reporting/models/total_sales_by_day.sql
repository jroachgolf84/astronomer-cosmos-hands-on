SELECT
    t.ds,
    t.location_id,
    SUM(t.total_amount) AS total_daily_sales

FROM carmichael_industries.transactions AS t

GROUP BY
    t.ds,
    t.location_id
