from fastapi import FastAPI
from app.api import align

app = FastAPI(title="Smart File Aligner")

app.include_router(align.router)

