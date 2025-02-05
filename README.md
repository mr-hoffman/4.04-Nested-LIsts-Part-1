# 4.04-Nested-Lists-Part-1

## Nested Lists and For Loops

The goal of this lab is to practice using and accessing items from lists of lists.

You have a few errands to run and have created a few shopping lists to help you remember what to buy. You stored your notes in a nested list, `shopping_cart`. This program will allow the user to ask for a specific item by its index or update what items are in the cart. The user can request to view list to see the items in a specific shopping list.

### Shopping Cart

```python
shopping_cart = [
  ["tooth paste", "q-tips", "milk"],
  ["milk", "candy", "apples"],
  ["planner", "pencils", "q-tips"]
]
```

### User Inputs

Your user should be asked what they want to do, using one of the following commands. Based on the command entered, you will ask for additional information, then pass that info into one of the appropriate functions (described below).

* `update`:
  * The program asks which shopping list the user wants to update, which position it should update, and the new value to update.
* `view item`:
  * The program asks which shoping list the item is in and which postion it occupies, then prints the item's name.
* `view list`:
  * The program asks which shopping list the user wants and prints all the items associated with that shopping list (nicely formated as a single string).
 
### Functions

* `update_list`:
  * Takes in an integer representing the index of the shopping list, an integer representing the index of the item to update, and a string representing the new value for that item. Does not alter the length of the list.
* `print_item`:
  * Takes an int representing the index of the shopping list followed by an int representing the index of the item to print.
*   `print_list`:
  * Takes an int representing the index of the shopping list to print.
* Add any other functions (and appropriate inputs) as you see fit.

### Example

```python
>>> What would you like to do? view list
>>> Which shopping list would you like to see? 1
tooth paste, q-tips, gum
