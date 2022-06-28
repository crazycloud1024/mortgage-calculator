from fastapi import APIRouter
from app.api.v1.lpr import (lpr)

api_v1 = APIRouter()

api_v1.include_router(lpr.router, tags=["lrpAPI"])
