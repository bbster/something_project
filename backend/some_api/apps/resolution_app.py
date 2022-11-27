# from fastapi import FastAPI
# from datetime import datetime
#
# from db.models import Resolution
#
# app = FastAPI()
#
#
# @app.get("/app/resolution")
# async def get_resolution():
#     # for resolution in db:
#     #
#     #     pass
#     result = {
#         'message': "",
#         'email': "",
#         'create_at': datetime.now(),
#     }
#
#     return result
#
#
# @app.get("app/resolution/{id}")
# def detail_resolution(resolution_id: int):
#     pass
#
#
# @app.post("/app/resolution")
# def post_resolution(resolution: Resolution):
#     resolution = Resolution()
#     return resolution
#
#
# @app.delete("/app/resolution/{id}")
# def delete_resolution(resolution_id: int):
#     pass
