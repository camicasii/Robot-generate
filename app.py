from fastapi import FastAPI
from fastapi.responses import StreamingResponse,JSONResponse
from os.path import exists
from imageHandle import image
some_file_path = "./hola.png"
app = FastAPI()
n=0

@app.get("/token/{item_id}")
def main(item_id: int):
    def iterfile():  #
       pathlib = f'./img/{item_id}.png'
       if(not exists(pathlib)):
        print("paso")
        k=image(pathlib,item_id)
        # k.save(pathlib,"PNG")
       with open(pathlib,mode="rb") as file_like:  #
           yield from file_like  #

    return StreamingResponse(iterfile(), media_type="image/PNG")