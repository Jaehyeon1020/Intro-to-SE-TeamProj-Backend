from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

from .view import stores, users


def include_router(app):
  app.include_router(stores.router)
  app.include_router(users.router)


def start_application():
  app = FastAPI()
  include_router(app)

  app.add_middleware(
      CORSMiddleware,
      allow_origins=["http://localhost:3000", "http://localhost:3002",
                     "https://localhost:3000", "https://localhost:3002"],
      allow_credentials=True,
      allow_methods=["*"],
      allow_headers=["*"],
  )

  return app


if __name__ == "__main__":
  uvicorn.run("main:app", reload=True)  # , port=5000, host='192.168.0.15')

app = start_application()
