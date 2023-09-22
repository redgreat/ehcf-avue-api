#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# @author by wangcw
# @generate at 2023/9/20 14:46

from __future__ import annotations

from app.core.db import get_db
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text


async def cumulative(db: AsyncSession = Depends(get_db)):
    print("调用第一步！")
    sql = text(
        """
    SELECT JSON_ARRAYAGG(S.J)
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
        print("进try了！")
        res = await db.execute(sql)
        print("0", res)
        result = list(res.mappings())
        print("1", result)
        result = dict(data=result)
        print("2", result)
    except Exception as e:
        print(e)
    return dict(status="seuccess!")
