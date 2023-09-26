import json
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse


from app.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

router = APIRouter()


@router.get("/cumulative", tags=["业务累计服务信息"])
async def view_cumulative(
    provider_code: str = "1001", db: AsyncSession = Depends(get_db)
):
    sql = text(
        """
    SELECT JsonValue as data
    FROM home_viewdata
    WHERE DataType=1
      AND ProviderCode = \'{}\';
    """.format(
            provider_code
        )
    )

    try:
        res = await db.execute(sql)
        result = list(res.mappings())
        if result:
            result = json.loads(jsonable_encoder(result[0].get("data")))
            return result
        else:
            return {"data": "无数据！"}
    except Exception as e:
        e = dict(error=e)
        return e


@router.get("/userarea", tags=["服务网络-地图信息"])
async def view_userarea(
    provider_code: str = "1001", area_type: int = 3, db: AsyncSession = Depends(get_db)
):
    sql = text(
        """SELECT JSON_ARRAYAGG(JSON_OBJECT("name", "", "value", S.ServicerCnt, 
            "lng", S.Alng, "lat", S.Alat, "zoom", 1)) AS data
        FROM (SELECT ServicerCnt, Alng, Alat
        FROM home_usermapdaily
        WHERE ProviderCode = \'{}\' AND AreaType = {}
        GROUP BY AreaCode) AS S;""".format(
            provider_code, area_type
        )
    )

    try:
        res = await db.execute(sql)
        result = list(res.mappings())
        if result:
            result = json.loads(jsonable_encoder(result[0].get("data")))
            return result
        else:
            return ()
    except Exception as e:
        e = dict(error=e)
        return e


@router.get("/worktimetrend", tags=["近1周作业结束时段分布"])
async def view_worktimetrend(
    provider_code: str = "1001", db: AsyncSession = Depends(get_db)
):
    sql = text(
        """
    SELECT JsonValue as data
    FROM home_viewdata
    WHERE DataType=2
      AND ProviderCode = \'{}\';
    """.format(
            provider_code
        )
    )

    try:
        res = await db.execute(sql)
        result = list(res.mappings())
        if result:
            result = json.loads(jsonable_encoder(result[0].get("data")))
            return result
        else:
            return ()
    except Exception as e:
        e = dict(error=e)
        return e


@router.get("/ordercreatetrend", tags=["下单量变化趋势"])
async def view_ordercreatetrend(
    provider_code: str = "1001", db: AsyncSession = Depends(get_db)
):
    sql = text(
        """
    SELECT JsonValue as data
    FROM home_viewdata
    WHERE DataType=3
      AND ProviderCode = \'{}\';
    """.format(
            provider_code
        )
    )

    try:
        res = await db.execute(sql)
        result = list(res.mappings())
        if result:
            result = json.loads(jsonable_encoder(result[0].get("data")))
            return result
        else:
            return ()
    except Exception as e:
        e = dict(error=e)
        return e


@router.get("/ordertypedetail", tags=["各工单类型下单明细"])
async def view_ordertypedetail(
    provider_code: str = "1001", db: AsyncSession = Depends(get_db)
):
    sql = text(
        """
    SELECT JsonValue as data
    FROM home_viewdata
    WHERE DataType=4
      AND ProviderCode = \'{}\';
    """.format(
            provider_code
        )
    )

    try:
        res = await db.execute(sql)
        result = list(res.mappings())
        if result:
            result = json.loads(jsonable_encoder(result[0].get("data")))
            return result
        else:
            return ()
    except Exception as e:
        e = dict(error=e)
        return e


@router.get("/ordercusttop", tags=["累计下单客户TOP10"])
async def view_ordercusttop(
    provider_code: str = "1001", db: AsyncSession = Depends(get_db)
):
    sql = text(
        """
    SELECT ProviderCode,JSON_ARRAYAGG(JSON_OBJECT("type1", CustomerName, "type2", CreateCnt,
    "type3", CONCAT(ROUND((CreateCnt/TotalCnt)*100,2),'%') )) AS data
    FROM home_ordercusttop
    WHERE ProviderCode = \'{}\'
    GROUP BY ProviderCode;
    """.format(
            provider_code
        )
    )

    try:
        res = await db.execute(sql)
        result = list(res.mappings())
        if result:
            result = json.loads(jsonable_encoder(result[0].get("data")))
            return result
        else:
            return ()
    except Exception as e:
        e = dict(error=e)
        return e


@router.get("/ordercusttrend", tags=["各工单类型下单明细"])
async def view_ordercusttrend(
    provider_code: str = "1001", db: AsyncSession = Depends(get_db)
):
    sql = text(
        """
    SELECT JsonValue as data
    FROM home_viewdata
    WHERE DataType=5
      AND ProviderCode = \'{}\';
    """.format(
            provider_code
        )
    )

    try:
        res = await db.execute(sql)
        result = list(res.mappings())
        if result:
            result = json.loads(jsonable_encoder(result[0].get("data")))
            return result
        else:
            return ()
    except Exception as e:
        e = dict(error=e)
        return e
