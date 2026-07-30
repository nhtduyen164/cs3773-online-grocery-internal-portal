# User Stories and Test Cases

## Login and User Management

1. **Internal User Login**

   As a store employee, I want to log in with a username and password so that I can access the internal grocery store portal securely.

   **Test Case:**
   
   * Create a preloaded user account for Cashier with username “employee1” and password “password123”; for Manager with username "manager1" and password "admin123".
   * Open the login page.
   * Enter “employee1” or "manager1" in the username text box.
   * Enter “password123” or "admin123" in the password text box.
   * Click the login button.
   * I should be taken to the internal portal dashboard.
   * Log out of the system.
   * Open the login page again.
   * Enter “employee1” or "manager1" in the username text box.
   * Enter “password1234” or "admin1234" in the password text box.
   * Click the login button.
   * I should see an error message saying that the username or password is incorrect.

2. **Internal User Logout**

   As a store employee, I want to log out of the internal portal so that my account cannot be used by another person on the same device.

   **Test Case:**
   
   * Log in with a valid staff account.
   * I should be taken to the internal portal dashboard.
   * Click the logout button.
   * I should be redirected to the login page.
   * Try to open the product catalog page again.
   * I should be redirected to the login page because I am no longer logged in.

3. **Prevent Unauthorized Access**

   As a store employee, I want the system to block users who are not logged in so that only authorized staff can access internal store information.

   **Test Case:**

   * Open the system without logging in.
   * Try to open the product catalog page.
   * I should be redirected to the login page.
   * Try to open the add product page without logging in.
   * I should be redirected to the login page.
   * Log in with a valid staff account.
   * Open the product catalog page.
   * I should be able to view the product catalog.

## Product Catalog Management

1. **View Product Catalog**

   As a store employee, I want to view the list of grocery products so that I can see the products currently stored in the system.

   **Test Case:**

   * Log in with a valid staff account.
   * Create a product named “Organic Bananas” with image “bananas.png”, price $0.59, quantity on hand 150, and description “Sold per pound, organic”.
   * Create a product named “Whole Milk (1 Gallon)” with image “milk.png”, price $2.99, quantity on hand 80, and description “Vitamin D whole milk”.
   * Open the product catalog page.
   * I should see “Organic Bananas” listed with image, price $0.59, quantity on hand 150, and description “Sold per pound, organic”.
   * I should see “Whole Milk (1 Gallon)” listed with image, price $2.99, quantity on hand 80, and description “Vitamin D whole milk”.

2. **Add New Product**

   As a store employee, I want to add a new grocery product to the catalog so that the store can offer new items for sale.

   **Test Case:**

   * Log in with a valid staff account.
   * Open the add product page.
   * Enter “Roma Tomatoes” in the product name text box.
   * Upload or enter the image “tomatoes.png”.
   * Enter 1.99 in the Regular Price text box.
   * Enter 120 in the Stock Quantity text box.
   * Enter “Sold per pound” in the Description text box.
   * Click the submit button.
   * I should see a confirmation message that the product was added successfully.
   * Open the product catalog page.
   * I should see “Roma Tomatoes” listed with image, price $1.99, quantity 120, and description “Sold per pound”.

3. **Reject Invalid Product Information**

   As a store employee, I want the system to reject invalid product information so that incorrect product data is not saved in the catalog.

   **Test Case:**

   * Log in with a valid staff account.
   * Open the add product page.
   * Leave the product name text box empty.
   * Enter -2.99 in the price text box.
   * Enter 5.5 in the quantity text box.
   * Click the submit button.
   * I should see an error message saying "Please fill out this field" at the product name.
   * I should see an error message saying "Value must be greater than or equal to 0." in the the regular price text box.
   * I should see an error message saying "Please enter a valid value. The two nearest values are # and #" in the stock quantity text box.
   * Open the product catalog page.
   * I should not see the invalid product listed in the catalog.
   
4. **Edit Existing Product**

   As a store employee, I want to update an existing product’s information so that the catalog stays accurate when product details change.
   
   **Test Case:** 
   
   * Log in with a valid staff account.
   * Create a product named “Chicken Breast” with image “chicken_breast.png”, price $5.49, stock quantity 10, and description “Boneless, per pound”.
   * Open the product catalog page.
   * Click the edit button for “Chicken Breast”.
   * Change the price to $4.49.
   * Change the quantity to 70.
   * Change the description to “Boneless, skinless, per pound”.
   * Click the save button.
   * I should be redirected to the product catalog page and see a confirmation message that "Product updated successfully."
   * I should see “Chicken Breast” listed with price $4.49, quantity 70, and description “Boneless, skinless, per pound”.

5. **Mark Product as Out of Stock/Low Stock**

   As a store employee, I want to mark a product as out of stock or discontinued so that the catalog correctly shows whether the product is currently available.
   
   **Test Case:**
   
   * Log in with a valid staff account.
   * Create a product named “Free-Range Eggs (Dozen)” with quantity 60.
   * Open the product catalog page and choose edit product.
   * Change the stock quantity to 0 of “Free-Range Eggs”.
   * I should see “Free-Range Eggs (Dozen)” listed as out of stock in the catalog.
   * Change the stock quantity to the number less then the current number of “Free-Range Eggs (Dozen)”.
   * I should see “Free-Range Egss (Dozen)” listed as low stock in the catalog.
   * The status change should be saved in the database.

## Inventory, Discounts, Search, and Orders

1. **Track Stock Level**

   As a store employee, I want to view the current stock quantity for each product so that I can know which items are available for sale.

   **Test Case:**

   * Create a product named “Ground Coffee (12oz)” with quantity 55.
   * List the product catalog.
   * I should see “Ground Coffee (12oz)” listed with quantity 55.
   * Create a product named “Sourdough Bread” with quantity 50.
   * Update the quantity of “Sourdough Bread” to 45.
   * List the product catalog.
   * I should see “Sourdough Bread” listed with quantity 45.

2. **Mark Products as Out of Stock**

   As a store employee, I want products with zero quantity to be marked as out of stock so that I can quickly identify unavailable items.

   **Test Case:**

   * Create a product named “Sourdough Bread” with quantity 0.
   * List the product catalog.
   * I should see “Sourdough Bread” marked as out of stock.
   * Create a product named “Free-Range Eggs (Dozen)” with quantity 12.
   * Ask for the product catalog.
   * I should not see “Free-Range Eggs (Dozen)” marked as out of stock.

3. **Allow for Creation of Discount Code**

   As a store manager, I want to create discount codes so that promotional discounts can be stored and used in the system.

   **Test Case:**

   * Create a discount code named “WELCOME10” with a 10% discount for new customers.
   * Ask for the list of discount codes.
   * I should see “WELCOME10” listed with a 10% discount.
   * Create a discount code named “WELCOME10” again.
   * I should get an error because duplicate discount codes should not be allowed.

4. **Allow for Creation of Sale Items**

   As a store manager, I want to mark products as sale items so that discounted products can be clearly identified.

   **Test Case:**

   * Create a product named “Cheddar Cheese Block” with price $6.79.
   * Mark “Cereal” as a sale item with a sale price of $5.49.
   * Ask for the product catalog.
   * I should see “Cheddar Cheese Block” marked as a sale item with a sale price of $5.49.
   * Create a product named “Chicken Breast” with price $4.49.
   * Ask for the product catalog.
   * I should not see “Chicken Breast” marked as a sale item.

5. **Search by Name/Description**

   As a store employee, I want to search for products by name or description so that I can quickly find specific items in the catalog.

   **Test Case:**

   * Create a product named “Organic Bananas” with description “Sold per pound, organic”.
   * Search for “Bananas.”
   * I should see “Organic Bananas” in the search results.
   * Create a product named “Cheddar Cheese Block” with description “Sharp cheddar, 8oz block.”
   * Search for “block.”
   * I should see “Cheddar Cheese Block” in the search results.
   * Search for “steak.”
   * I should not see products that do not match “steak” in the name or description.

6. **Sort by Price**

   As a store employee, I want to sort products by price so that I can view products from lowest to highest or highest to lowest price.

   **Test Case:**

   * Create a product named “Cheddar Cheese Block” with price $5.49.
   * Create a product named “Chicken Breast” with price $4.49.
   * Create a product named “Free-Range Eggs (Dozen)” with price $5.29.
   * Sort products by price from low to high.
   * I should see the order “Chicken Breast”, “Free-Range Eggs (Dozen)”, “Cheddar Cheese Block.”
   * Sort products by price from high to low.
   * I should see the order “Cheddar Cheese Block”, “Free-Range Eggs (Dozen)”, “Chicken Breast.”

7. **Sort by Availability**

   As a store employee, I want to sort products by availability so that available products can be separated from unavailable products.

   **Test Case:**

   * Create a product named “Roma Tomatoes” with quantity 120.
   * Create a product named “Cheddar Cheese Block” with quantity 40.
   * Sort products by availability.
   * I should see in-stock products first then low-stock products after.
   * Ask for available products only.
   * I should see “Roma Tomatoes” first but "Cheddar Cheese Block" listed at the end of the list.

8. **Show Currently Placed Orders**

   As a store employee, I want to view currently placed customer orders so that I can see which orders need to be processed.

   **Test Case:**

   * Create an order for customer “Sophia Martinez” with status “Placed.”
   * Ask for the list of currently placed orders.
   * I should see the order for “Sophia Martinez.”
   * Create an order for customer “Daniel Brooks” with status “Executed.”
   * Ask for the list of currently placed orders.
   * I should not see the executed order for “Daniel Brooks.”

9. **Show Detailed Information of an Order**

   As a store employee, I want to view detailed information for an order so that I can see the customer, items, quantities, prices, and total amount.

   **Test Case:**

   * Create an order for customer “Sophia Martinez” containing 4 Roma Tomatoes at $1.99 each, 1 Ground Coffee (12oz) at $8.99 and 1 Whole Milk (1 Gallon) at $3.49.
   * Open the order details.
   * I should see customer “Vincent Vega.”
   * I should see 4 tomatoes, 1 ground coffee and 1 milk, and a total of $20.44.

10. **Sort by Order Time**

    As a store employee, I want to sort orders by order time so that I can process older or newer orders first.

    **Test Case:**

    * Create one order at 9:00 AM.
    * Create another order at 10:00 AM.
    * Sort orders by oldest first.
    * I should see the 9:00 AM order before the 10:00 AM order.
    * Sort orders by newest first.
    * I should see the 10:00 AM order before the 9:00 AM order.

11. **Sort by Customer**

    As a store employee, I want to sort orders by customer so that I can organize orders by customer name.

    **Test Case:**

    * Create an order for customer “Daniel Brooks.”
    * Create an order for customer “Olivia Carter.”
    * Sort orders by customer name.
    * I should see “Daniel Brooks” before “Olivia Carter.”

12. **Sort by Order Size in Dollar Amount**

    As a store employee, I want to sort orders by total dollar amount so that I can identify larger or smaller orders.

    **Test Case:**

    * Create an order with a total amount of $12.37.
    * Create an order with a total amount of $32.34.
    * Sort orders by total amount from lowest to highest.
    * I should see the $12.37 order before the $32.34 order.
    * Sort orders by total amount from highest to lowest.
    * I should see the $32.34 order before the $12.37 order.

13. **Execute an Order**

    As a store employee, I want to execute a customer order so that the order status is updated and the purchased item quantities are removed from inventory.

    **Test Case:**

    * Create a product named “Organic Bananas” with quantity 25.
    * Create a placed order for 5 bananas.
    * Execute the order.
    * I should see the order status changed to “Executed.”
    * I should see the quantity of “Organic Bananas” reduced to 20.
    * Create a product named “Whole Milk (1 Gallon)” with quantity 10.
    * Create a placed order for 3 milk.
    * Execute the order.
    * I should see the order status changed to “Executed.”
    * I should see the quantity of “Whole Milk (1 Gallon)” reduced to 7.

14. **Prevent Order Execution When Inventory Is Insufficient**

    As a store employee, I want the system to prevent order execution when there is not enough inventory so that product quantities do not become negative.

    **Test Case:**

    * Create a product named “Bread” with quantity 2.
    * Create a placed order for 5 bread.
    * Try to execute the order.
    * I should get an error saying there is not enough inventory.
    * I should see the order remain in “Placed” status.
    * I should see the quantity of “Bread” remain 2.
