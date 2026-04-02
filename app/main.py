from dotenv import load_dotenv # necessário para carregar o arquivo .env!!!
load_dotenv() # VARIÁVEIS DE AMBIENTE DEVEM SER CARREGADAS ANTES DE QUALQUER IMPORT!! -> e load_dotenv é obrigatório com Uvicorn 

from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.auth_routes import router as auth_router
from app.utils.init_admin import create_initial_admin
from fastapi.middleware.cors import CORSMiddleware
import logging


app = FastAPI(
    title="User Manager API",
    version="1.0.0"
)

# Domínios permitidos (ajuste conforme necessário)
origins = [
    "http://localhost:5500",
    "http://127.0.0.1:5500",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # lista de domínios permitidos
    allow_credentials=True,
    allow_methods=["*"],    # permite GET, POST, PUT, DELETE, etc
    allow_headers=["*"],    # permite todos headers (Authorization incluído)
)

logger = logging.getLogger(__name__)

@app.on_event("startup")
def startup_event():
    try:
        create_initial_admin()
        logger.info("Superusuário verificado/criado com sucesso")
    except Exception as e:
        logger.error(f"Erro ao criar superusuário: {e}")

app.include_router(user_router)
app.include_router(auth_router)
