import simplejson
from fastapi import APIRouter, Request
from app.extensions.logger import logger
from app.api.v1.lpr.tools import equal_principal_interest_tool

router = APIRouter()


@router.post("/lrp/equal_principal_interest")
async def equal_principal_interest(request: Request):
    data = await request.body()
    data = data.decode('UTF-8')
    logger.info(simplejson.loads(data))
    data = simplejson.loads(data)

    # loan_money, month_lpr, number_loan_month
    loan_money = 1000000
    number_loan_year = 10
    number_loan_month = 12 * number_loan_year
    print(data.get("lpr_year_value", 0))
    year_lpr = int(float(data.get("lpr_year_value", 0)))
    month_lpr = year_lpr / 100 / 12
    ret = equal_principal_interest_tool(loan_money, month_lpr, number_loan_month)
    logger.info(ret)
    logger.info(type(ret))
    res = simplejson.dumps(ret)
    logger.info(res)
    logger.info(type(res))
    return ret


@router.post("/lrp/equal_principal")
async def equal_principal(request: Request):
    pass
    #TODO miss li
