
from app.database.repository import Repository
from app.database.connection import ConnectionManager

db_mgr = ConnectionManager() 
repo_instance = Repository(db_mgr)

def orchestra(CommandResult):
    if(CommandResult.action == "exit"):
        db_mgr.disconnect()
        return False
    elif(CommandResult.action == "load"):
        repo_instance.load(CommandResult.name,CommandResult.path)
    elif(CommandResult.action == "ping"): # ping the database
        repo_instance.query_ping() 
    elif(CommandResult.action == "query"): 
        repo_instance.query() 

    elif(CommandResult.action == "dataready"): 
        repo_instance.dataready() 


    return True