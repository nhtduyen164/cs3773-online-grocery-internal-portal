# User Stories and Test Cases

## Login and User Management

1. **Internal User Login**

As a store employee, I want to log in with a username and password so that I can access the internal grocery store portal securely.

**Test Case:** 
* Successful login
* Login with incorrect password
* Login with unknown username
* Protected page access without login

2. **Internal User Logout**

As a store employee, I want to log out of the internal portal so that my account cannot be used by another person on the same device.

**Test Case:**
* Successful logout
* Access protected page after logout

## Product Catalog Management

1. **View Product Catalog**

As a store employee, I want to view the list of grocery products, so that I can see the products currently stored in the system.

**Test Case:**

* View product catalog with existing products
* View product catalog when no products exist
* View product catalog without login

## Add New Product

As a store employee, I want to add a new grocery product to the catalog, so that the online grocery store can offer new items for sale.

**Test Case:**

* Add product with valid information
* Add product without product name
* Add product with invalid price
* Add product with invalid quantity
* Add product without login

## Edit Existing Product

As a store employee, I want to update an existing product’s information, so that the catalog stays accurate when product details change.

**Test Case:** 

* Edit product with valid updated information
* Edit product with invalid price
* Edit product with invalid quantity
* Edit product without login

## Mark Product as Out of Stock/Discontinued

As a store employee, I want to mark a product as out of stock or discontinued, so that the catalog correctly shows whether the product is currently available.

**Test Case:**

* Mark product as out-of-stock
* Mark product as discontinued
* Change product status back to available
* Change product status without login

## Inventory, Discounts, Search, and Orders

1. **Track Stock Level**

   As a store employee, I want to view the current stock quantity for each product so that I can know which items are available for sale.

   **Test Case:**

   * Create a product named “Apples” with quantity 25.
   * List the product catalog.
   * I should see “Apples” listed with quantity 25.
   * Create a product named “Milk” with quantity 10.
   * Update the quantity of “Milk” to 6.
   * List the product catalog.
   * I should see “Milk” listed with quantity 6.

2. **Mark Products as Out of Stock**

   As a store employee, I want products with zero quantity to be marked as out of stock so that I can quickly identify unavailable items.

   **Test Case:**

   * Create a product named “Bread” with quantity 0.
   * List the product catalog.
   * I should see “Bread” marked as out of stock.
   * Create a product named “Eggs” with quantity 12.
   * Ask for the product catalog.
   * I should not see “Eggs” marked as out of stock.

3. **Allow for Creation of Discount Code**

   As a store manager, I want to create discount codes so that promotional discounts can be stored and used in the system.

   **Test Case:**

   * Create a discount code named “SAVE10” with a 10% discount.
   * Ask for the list of discount codes.
   * I should see “SAVE10” listed with a 10% discount.
   * Create a discount code named “SAVE10” again.
   * I should get an error because duplicate discount codes should not be allowed.

4. **Allow for Creation of Sale Items**

   As a store manager, I want to mark products as sale items so that discounted products can be clearly identified.

   **Test Case:**

   * Create a product named “Cereal” with price $5.00.
   * Mark “Cereal” as a sale item with a sale price of $4.00.
   * Ask for the product catalog.
   * I should see “Cereal” marked as a sale item with a sale price of $4.00.
   * Create a product named “Orange Juice” with price $6.00.
   * Ask for the product catalog.
   * I should not see “Orange Juice” marked as a sale item.

5. **Search by Name/Description**

   As a store employee, I want to search for products by name or description so that I can quickly find specific items in the catalog.

   **Test Case:**

   * Create a product named “Organic Apples” with description “Fresh red apples.”
   * Search for “Apples.”
   * I should see “Organic Apples” in the search results.
   * Create a product named “Whole Milk” with description “One gallon milk.”
   * Search for “gallon.”
   * I should see “Whole Milk” in the search results.
   * Search for “steak.”
   * I should not see products that do not match “steak” in the name or description.

6. **Sort by Price**

   As a store employee, I want to sort products by price so that I can view products from lowest to highest or highest to lowest price.

   **Test Case:**

   * Create a product named “Bananas” with price $1.50.
   * Create a product named “Chicken” with price $9.99.
   * Create a product named “Rice” with price $3.00.
   * Sort products by price from lowest to highest.
   * I should see the order “Bananas”, “Rice”, “Chicken.”
   * Sort products by price from highest to lowest.
   * I should see the order “Chicken”, “Rice”, “Bananas.”

7. **Sort by Availability**

   As a store employee, I want to sort products by availability so that available products can be separated from unavailable products.

   **Test Case:**

   * Create a product named “Tomatoes” with quantity 15.
   * Create a product named “Strawberries” with quantity 0.
   * Sort products by availability.
   * I should see available products separated from out-of-stock products.
   * Ask for available products only.
   * I should see “Tomatoes” but not “Strawberries.”

8. **Show Currently Placed Orders**

   As a store employee, I want to view currently placed customer orders so that I can see which orders need to be processed.

   **Test Case:**

   * Create an order for customer “Vincent Vega” with status “Placed.”
   * Ask for the list of currently placed orders.
   * I should see the order for “Vincent Vega.”
   * Create an order for customer “Marsellus Wallace” with status “Executed.”
   * Ask for the list of currently placed orders.
   * I should not see the executed order for “Marsellus Wallace.”

9. **Show Detailed Information of an Order**

   As a store employee, I want to view detailed information for an order so that I can see the customer, items, quantities, prices, and total amount.

   **Test Case:**

   * Create an order for customer “Vincent Vega” containing 2 apples at $1.00 each and 1 milk at $4.00.
   * Open the order details.
   * I should see customer “Vincent Vega.”
   * I should see 2 apples, 1 milk, and a total of $6.00.

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

    * Create an order for customer “Cliff Booth.”
    * Create an order for customer “Rick Dalton.”
    * Sort orders by customer name.
    * I should see “Cliff Booth” before “Rick Dalton.”

12. **Sort by Order Size in Dollar Amount**

    As a store employee, I want to sort orders by total dollar amount so that I can identify larger or smaller orders.

    **Test Case:**

    * Create an order with a total amount of $25.00.
    * Create an order with a total amount of $75.00.
    * Sort orders by total amount from lowest to highest.
    * I should see the $25.00 order before the $75.00 order.
    * Sort orders by total amount from highest to lowest.
    * I should see the $75.00 order before the $25.00 order.

13. **Execute an Order**

    As a store employee, I want to execute a customer order so that the order status is updated and the purchased item quantities are removed from inventory.

    **Test Case:**

    * Create a product named “Apples” with quantity 25.
    * Create a placed order for 5 apples.
    * Execute the order.
    * I should see the order status changed to “Executed.”
    * I should see the quantity of “Apples” reduced to 20.
    * Create a product named “Milk” with quantity 10.
    * Create a placed order for 3 milk.
    * Execute the order.
    * I should see the order status changed to “Executed.”
    * I should see the quantity of “Milk” reduced to 7.

14. **Prevent Order Execution When Inventory Is Insufficient**

    As a store employee, I want the system to prevent order execution when there is not enough inventory so that product quantities do not become negative.

    **Test Case:**

    * Create a product named “Bread” with quantity 2.
    * Create a placed order for 5 bread.
    * Try to execute the order.
    * I should get an error saying there is not enough inventory.
    * I should see the order remain in “Placed” status.
    * I should see the quantity of “Bread” remain 2.
