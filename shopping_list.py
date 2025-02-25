# shopping list
shopping_cart = [
  ["tooth paste", "q-tips", "milk"],
  ["milk", "candy", "apples"],
  ["planner", "pencils", "q-tips"]
]


# user inputs




# functions
def update_list(s_list):
  row = int(input("Which list to update? ")) - 1
  col = int(input("Which item in list to update? ")) - 1
  new_item = input("What is the new item? ")

  s_list[row][col] = new_item

def view_item(s_list):
  row = int(input("which list? ")) - 1
  col = int(input("which position? ")) - 1
  print(s_list[row][col])

def view_list(s_list):
  lst_to_str = ""
  row = int(input("Which list? ")) - 1
  for i in range(len(s_list[row]) - 1):
    lst_to_str += s_list[row][i] + ", "
  lst_to_str += f"and {s_list[row][-1]}"
  print(lst_to_str)

def all_in_one(s_list):
  new_list = []
  for lst in s_list:
    for item in lst:
      new_list.append(item)
  return new_list

def count_items(s_list):
  item_to_find = input("What are you looking for? ")
  count = 0
  for lst in s_list:
    for item in lst:
      if item.lower() == item_to_find.lower():
        count += 1
  return count

def drink_more_milk(s_list):
  for i in range(len(s_list)):
    if 'milk' not in s_list[i]:
      s_list[i].append('milk')

def milk_and_cookies(s_list):
  for i in range(len(s_list)):
    for j in range(len(s_list[i])):
      if 'milk' in s_list[i][j]:
        s_list[i][j] += " and cookies"

view_list(shopping_cart)
milk_and_cookies(shopping_cart)
view_list(shopping_cart)
