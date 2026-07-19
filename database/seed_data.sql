-- Sample data for development/testing.

-- ---------------------------------------------------------------------------
-- Users
-- ---------------------------------------------------------------------------
INSERT INTO users (id, username, email, password_hash, role) VALUES
    (1, 'alice_johnson', 'alice@example.com', 'ADMIN123!', 'admin'),
    (2, 'bob_martinez',  'bob@example.com',   'MANAGER123!', 'manager'),
    (3, 'carla_nguyen',  'carla@example.com', 'CASHIER123!', 'cashier');

-- ---------------------------------------------------------------------------
-- Products (grocery store)
-- ---------------------------------------------------------------------------
INSERT INTO products (
    id,
    name,
    description,
    image_path,
    price,
    stock_quantity,
    is_on_sale,
    sale_price
) VALUES
    (
        1,
        'Organic Bananas',
        'Sold per pound, organic',
        'images/products/placeholder.png',
        0.59,
        150,
        0,
        NULL
    ),
    (
        2,
        'Whole Milk (1 Gallon)',
        'Vitamin D whole milk',
        'images/products/placeholder.png',
        3.49,
        80,
        1,
        2.99
    ),
    (
        3,
        'Sourdough Bread',
        'Fresh baked in-store daily',
        'images/products/placeholder.png',
        4.99,
        45,
        0,
        NULL
    ),
    (
        4,
        'Free-Range Eggs (Dozen)',
        'Large brown eggs',
        'images/products/placeholder.png',
        5.29,
        60,
        0,
        NULL
    ),
    (
        5,
        'Cheddar Cheese Block',
        'Sharp cheddar, 8oz block',
        'images/products/placeholder.png',
        6.79,
        40,
        1,
        5.49
    ),
    (
        6,
        'Roma Tomatoes',
        'Sold per pound',
        'images/products/placeholder.png',
        1.99,
        120,
        0,
        NULL
    ),
    (
        7,
        'Chicken Breast',
        'Boneless, skinless, per pound',
        'images/products/placeholder.png',
        4.49,
        70,
        0,
        NULL
    ),
    (
        8,
        'Ground Coffee (12oz)',
        'Medium roast, whole bean or ground',
        'images/products/placeholder.png',
        8.99,
        55,
        0,
        NULL
    );

-- ---------------------------------------------------------------------------
-- Discounts
-- ---------------------------------------------------------------------------
INSERT INTO discounts (id, code, description, discount_type, discount_value, starts_at, expires_at, max_uses, times_used, is_active) VALUES
    (1, 'WELCOME10', '10% off for new customers',        'percentage', 10.00, '2026-01-01 00:00:00', NULL,                  100, 12, 1),
    (2, 'SUMMER5',   '$5 off summer promotion',           'fixed',      5.00,  '2026-06-01 00:00:00', '2026-08-31 23:59:59', NULL, 5,  1),
    (3, 'BULKSAVE15','15% off bulk orders (expired)',     'percentage', 15.00, '2026-01-01 00:00:00', '2026-03-31 23:59:59', 50,  20, 0);

-- ---------------------------------------------------------------------------
-- Orders
-- ---------------------------------------------------------------------------

-- Order 1
--   Subtotal: 3x0.59 + 2x3.49 + 1x4.99 = 13.74 ; 10% off = 1.37 ; total = 12.37
INSERT INTO orders (id, discount_id, status, subtotal, discount_amount, total_amount) VALUES
    (1, 1, 'completed', 13.74, 1.37, 12.37);

-- Order 2
--   Subtotal: 1x5.29 + 2x6.79 + 3x4.49 = 32.34 ; total = 32.34
INSERT INTO orders (id, discount_id, status, subtotal, discount_amount, total_amount) VALUES
    (2, NULL, 'pending', 32.34, 0.00, 32.34);

-- Order 3
--   Subtotal: 4x1.99 + 1x8.99 + 1x3.49 = 20.44 ; $5 off = 5.00 ; total = 15.44
INSERT INTO orders (id, discount_id, status, subtotal, discount_amount, total_amount) VALUES
    (3, 2, 'pending', 20.44, 5.00, 15.44);

-- ---------------------------------------------------------------------------
-- Order Items
-- ---------------------------------------------------------------------------

-- Order 1 items
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
    (1, 1, 3, 0.59),  -- Organic Bananas x3
    (1, 2, 2, 3.49),  -- Whole Milk x2
    (1, 3, 1, 4.99);  -- Sourdough Bread x1

-- Order 2 items
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
    (2, 4, 1, 5.29),  -- Free-Range Eggs x1
    (2, 5, 2, 6.79),  -- Cheddar Cheese x2
    (2, 7, 3, 4.49);  -- Chicken Breast x3

-- Order 3 items
INSERT INTO order_items (order_id, product_id, quantity, unit_price) VALUES
    (3, 6, 4, 1.99),  -- Roma Tomatoes x4
    (3, 8, 1, 8.99),  -- Ground Coffee x1
    (3, 2, 1, 3.49);  -- Whole Milk x1
