from dotenv import load_dotenv # necessário para carregar o arquivo .env!!!
load_dotenv() # VARIÁVEIS DE AMBIENTE DEVEM SER CARREGADAS ANTES DE QUALQUER IMPORT!! -> e load_dotenv é obrigatório com Uvicorn 

from fastapi import FastAPI
from app.routes.user_routes import router as user_router
from app.routes.auth_routes import router as auth_router
from app.utils.init_admin import create_initial_admin
import logging


app = FastAPI(
    title="User Manager API",
    version="1.0.0"
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
