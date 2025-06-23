SELECT
    *
FROM {{ ref('sales_by_item') }} AS sbi
WHERE
    sbi.total_units_sold > 0 AND sbi.total_amount <= 0
