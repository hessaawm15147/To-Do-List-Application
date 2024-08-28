tasks = []

# Step 1: Add, view, and remove tasks
def add_task(task):
    tasks.append(task)

def view_tasks():
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

def remove_task(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)

add_task("Finish homework")
add_task("Exercise")
add_task("Pay bills")
add_task("Grocery shopping")
add_task("Dentist appointment")
add_task("Buy groceries")
add_task("Clean the bathroom")
add_task("Visit the doctor")
add_task("Buy supplies")
add_task("Wash the car")
add_task("Order new shoes")
add_task("Do laundry")
add_task("Feed the dog")
add_task("Make dinner")
add_task("Mow the lawn")
add_task("Gardening")
add_task("Clean the kitchen")
add_task("Clean the living room")
add_task("Clean the bedroom")
add_task("Clean the basement")
add_task("Clean the garage")
add_task("Clean the pool")
add_task("Pick up dry cleaning")
add_task("Clean the house")
add_task("Make dinner")
add_task("Read a book")
add_task("Write Code")

view_tasks()
remove_task(0)
view_tasks()
