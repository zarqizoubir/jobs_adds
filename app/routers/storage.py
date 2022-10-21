import os
from starlette.responses import FileResponse
from fastapi import Depends, APIRouter,UploadFile


router = APIRouter(
    prefix="/storage",
    tags=["Storage"]
)




@router.get("/")
def get_file():
    return "Not Working For Now"

@router.post("/")
async def Upload_File(file:UploadFile):
    os.makedirs("storage",exist_ok=False)
    new_file= open(f"storage/{file.filename}","wb")
    content =await file.read()
    new_file.write(content)

    return {
        "Message":"Succes"
    }
