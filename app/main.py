from dotenv import load_dotenv # necessário para carregar o arquivo .env!!!
load_dotenv() # VARIÁVEIS DE AMBIENTE DEVEM SER CARREGADAS ANTES DE QUALQUER IMPORT!! -> e load_dotenv é obrigatório com Uvicorn 

from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.auth_routes import router as auth_router


app = FastAPI(
    title="User Manager API",
    version="1.0.0"
)

app.include_router(user_router)
app.include_router(auth_router)
