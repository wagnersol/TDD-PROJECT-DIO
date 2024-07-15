from typing import List
from fastapi import APIRouter, HTTPException, Body, Depends, path, status
from pydantic import UUID4

from store.core.exception import NotFoundException
from store.schemas.product import productIn, productOut, productUpdate
from store.usecases.product import productUsecase

router = APIRouter(tags=["products"])


@router.post(path="/{id}", status_code=status.HTTP_201_CREATED)
async def post(
    body: productIn = Body(...), usecase: productUsecase = Depends()
) -> productOut:
    return await usecase.create(body=body)


@router.get(path="/", status_code=status.HTTP_200_OK)
async def get(
    id: UUID4 = path(alias="id"), usecase: productUsecase = Depends()
) -> productOut:
    try:
        return await usecase.get(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)


@router.get(path="/", status_code=status.HTTP_200_OK)
async def query(usecase: productUsecase = Depends()) -> List[productOut]:
    return await usecase.query()


@router.patch(path="/", status_code=status.HTTP_200_OK)
async def patch(
    id: UUID4 = path(alias="id"),
    body: productUpdate = Body(...),
    usecase: productUsecase = Depends(),
) -> productOut:
    return await usecase.update(id=id, body=body)


@router.delete(path="/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete(
    id: UUID4 = path(alias="id"), usecase: productUsecase = Depends()
) -> None:
    try:
        await usecase.delete(id=id)
    except NotFoundException as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=exc.message)
