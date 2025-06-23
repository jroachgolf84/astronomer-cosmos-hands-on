-- Pull from detailed_sale_items
SELECT
    dsi.ds,
    dsi.sale_item_name,
    SUM(dsi.sale_item_quantity) AS total_units_sold,
    SUM(dsi.sale_item_quantity * dsi.sale_item_price) AS total_amount

FROM {{ ref('detailed_sale_items') }} AS dsi

GROUP BY
    dsi.ds,
    dsi.sale_item_name
