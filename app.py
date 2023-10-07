from fastapi import FastAPI,HTTPException
from fastapi.middleware.cors import CORSMiddleware
import json



# Initializing the FastAPI app
app = FastAPI()
app.title = "DATOS CHALLENGE"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Carga el contenido del archivo JSON al iniciar la aplicación
with open("data.json", "r") as json_file:
    data_storage = json.load(json_file)

# Ruta para obtener todos los datos

@app.post("/upload/")
async def upload_json(data: dict):
    try:
        # Agrega los datos JSON recibidos al almacenamiento
        data_storage.append(data)
        return {"message": "Datos JSON recibidos con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al procesar los datos: {str(e)}")

@app.get("/data/")
async def get_data():
    # Devuelve todos los datos almacenados
    return data_storage

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)