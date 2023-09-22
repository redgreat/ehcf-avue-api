from fastapi import FastAPI, HTTPException, Request
from starlette.middleware.cors import CORSMiddleware
from app.routes import views
from app.core import config
from starlette.responses import JSONResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 权限验证
@app.middleware("http")
async def verify_app_key(request: Request, call_next):
    if request.url.path in ["/docs", "/openapi.json"]:
        response = await call_next(request)
    else:
        app_key = request.headers.get("appKey")
        if app_key != config.APP_KEY or app_key is None:
            # raise HTTPException(status_code=401, detail="Unauthorized")
            return JSONResponse(status_code=401, content={"detail": "Unauthorized"})
        response = await call_next(request)
    return response


app.include_router(views.router)
