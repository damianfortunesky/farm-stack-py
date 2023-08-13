from fastapi import FastAPI, HTTPException
from database import get_all_tasks, create_task, get_one_task
from models import Task

app = FastAPI() # correr servidor -> uvicorn main:app --reload

@app.get("/")
async def root():
    return {"message": "Raiz App"}


@app.get("/api/tasks")
async def get_tasks():

    tasks = await get_all_tasks()

    return {"message": "Se listan todas las tareas"}


@app.get(f"/api/tasks({id})")
async def get_task():
    return {"message": "Se lista tarea"}


@app.post("/api/tasks", response_model=Task)
async def save_task(task: Task):

    #Valido que no exista duplicado
    taskFound = await get_one_task(task.title)

    if taskFound:
        # Lanza error dato existente
        raise HTTPException(409, "Ya existe esa tarea")
    
    response = await create_task(task.dict())

    if response:
        return response
    raise HTTPException(400, 'Algo salio mal')


 
@app.put(f"/api/tasks({id})")
async def update_task():
    return {"message": "Se actualiza tarea"}


@app.delete(f"/api/tasks({id})")
async def delete_task():
    return {"message": "Se elimina tarea"}

