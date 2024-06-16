from fastapi import FastAPI
# uvicorn main:app --reload

app = FastAPI()

@app.get("/")   
async def index():
    return {"name" : "First data"}

todos = ["become a wolf", "take over the world", "eat some food", "sleep", "repeat"]

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos" : todos}

# get single todo
@app.get("/todos/{id}")
async def get_todo(id: int):
    try:
        return {"todo" : todos[id]}
    except:
        return {"error" : "Todo does not exist"}

# create a todo
@app.post("/create-todo")
async def create_todo(todo: str):
    todos.append(todo)
    return {"message" : "Todo created successfully"}

# update a todo
@app.put("/update-todo/{id}")
async def update_todo(id: int, todo: str):
    try:
        todos[id] = todo
        return {"message" : "Todo updated successfully"}
    except:
        return {"error" : "Todo does not exist"}

# delete a todo