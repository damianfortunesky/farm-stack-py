from motor.motor_asyncio import AsyncIOMotorClient

# Importo mis modelos
from models import Task

client = AsyncIOMotorClient('mongodb://localhost')

database = client.taskdatabase

collection = database.tasks


async def get_one_task_id(id):
    task = await collection.find_one({'_id': id})
    return task

async def get_one_task(title):
    task = await collection.find_one({'title': title})
    return task


async def create_task(task):
    new_task = await collection.insert_one(task)
    
    create_task = await collection.find_one({'_id': new_task.inserted_id})
    
    return create_task


async def get_all_tasks():
    
    tasks = []

    # Un cursor es un cojunto de datos, nosotros tenemos que recorrerlo.
    cursor = await collection.find({})

    for document in cursor:
        tasks.append(Task(**document)) # Le paso mi modelo para que convierta el documento. 

    return cursor


async def update_task(id: str, task):
    
    await collection.update_one({'_id': id}), {'$set': task}
    
    document = await collection.find_one({'_id': id})
    
    return document

async def delete_task(id: str):
    await collection.delete_one({'_id': id})
    return True