-- Joined sale_items and transactions__sale_items table
SELECT
    t.transaction_id,
    t.ds,
    t.location_id,
    si.sale_item_name,
    tsi.sale_item_quantity,
    si.sale_item_price

FROM carmichael_industries.transactions AS t

LEFT JOIN carmichael_industries.transactions__sale_items AS tsi
    ON t.transaction_id = tsi.transaction_id

LEFT JOIN carmichael_industries.sale_items AS si
    ON tsi.sale_item_id = si.sale_item_id
