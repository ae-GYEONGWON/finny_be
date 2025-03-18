from typing import List, Optional

from fastapi import APIRouter
from pydantic import BaseModel
from starlette.responses import JSONResponse

from src.auth.routes import router as auth_router
from src.market.routes import router as market_router
from src.orders.routes import router as orders_router
from src.portfolio.routes import router as portfolio_router


class ErrorMessage(BaseModel):
    msg: str


class ErrorResponse(BaseModel):
    detail: Optional[List[ErrorMessage]]


api_router = APIRouter(
    default_response_class=JSONResponse,
    responses={
        400: {"model": ErrorResponse},
        401: {"model": ErrorResponse},
        403: {"model": ErrorResponse},
        404: {"model": ErrorResponse},
        500: {"model": ErrorResponse},
    },
)

# 라우터 등록
api_router.include_router(auth_router, prefix="/auth", tags=["Auth"])
api_router.include_router(orders_router, prefix="/orders", tags=["Orders"])
api_router.include_router(portfolio_router, prefix="/portfolio", tags=["Portfolio"])
api_router.include_router(market_router, prefix="/market", tags=["Market"])
