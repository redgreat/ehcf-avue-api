import json
from fastapi.encoders import jsonable_encoder
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import JSONResponse

from app.core.db import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text

router = APIRouter()


@router.get("/cumulative", tags=["业务累计服务信息"])
async def view_cumulative(db: AsyncSession = Depends(get_db)):
    sql = text(
        """
    SELECT JSON_ARRAYAGG(S.J) AS data
    FROM (
    SELECT ProviderCode,JSON_OBJECT("backgroundColor", "rgba(55, 137, 224, 0.2)",
        "prefixText", "下单总量",
        "value", IFNULL(CntNum,0),
        "suffixText", "单") AS J
    FROM home_ordertotalcnt
    WHERE ProviderCode = '1001'
      AND CntType=1
    UNION
    SELECT ProviderCode,JSON_OBJECT("backgroundColor", "rgba(55, 137, 224, 0.2)",
        "prefixText", "完成工单总量",
        "value", IFNULL(CntNum,0),
        "suffixText", "单") AS J
    FROM home_ordertotalcnt
    WHERE ProviderCode = '1001'
      AND CntType=2
    UNION
    SELECT ProviderCode,JSON_OBJECT("backgroundColor", "rgba(55, 137, 224, 0.2)",
        "prefixText", "关闭工单总量",
        "value", IFNULL(CntNum,0),
        "suffixText", "单") AS J
    FROM home_ordertotalcnt
    WHERE ProviderCode = '1001'
      AND CntType=3
    UNION
    SELECT ProviderCode,JSON_OBJECT("backgroundColor", "rgba(55, 137, 224, 0.2)",
        "prefixText", "质检驳回工单总量",
        "value", IFNULL(CntNum,0),
        "suffixText", "单") AS J
    FROM home_ordertotalcnt
    WHERE ProviderCode = '1001'
      AND CntType=4
    UNION
    SELECT ProviderCode,JSON_OBJECT("backgroundColor", "rgba(55, 137, 224, 0.2)",
        "prefixText", "服务客户总数",
        "value", IFNULL(CntNum,0),
        "suffixText", "个") AS J
    FROM home_ordertotalcnt
    WHERE ProviderCode = '1001'
      AND CntType=5
    UNION
    SELECT ProviderCode,JSON_OBJECT("backgroundColor", "rgba(55, 137, 224, 0.2)",
        "prefixText", "服务施工人数",
        "value", IFNULL(CntNum,0),
        "suffixText", "人") AS J
    FROM home_ordertotalcnt
    WHERE ProviderCode = '1001'
      AND CntType=6) AS S
    GROUP BY S.ProviderCode;
    """
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
