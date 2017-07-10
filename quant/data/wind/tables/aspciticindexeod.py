from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class ASPCITICIndexEOD(BaseModel):
    """
    中信标普指数行情

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        指数Wind代码   
    trade_dt: VARCHAR2(8)
        交易日期   
    s_dq_preclose: NUMBER(20,4)
        昨收盘价   
    s_dq_open: NUMBER(20,4)
        开盘价   
    s_dq_high: NUMBER(20,4)
        最高价   
    s_dq_low: NUMBER(20,4)
        最低价   
    s_dq_close: NUMBER(20,4)
        收盘价   
    s_dq_volume: NUMBER(20,4)
        成交量(手)   
    s_dq_amount: NUMBER(20,4)
        成交金额(千元)   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    trade_dt = Column(VARCHAR2(8))
    s_dq_preclose = Column(NUMBER(20,4))
    s_dq_open = Column(NUMBER(20,4))
    s_dq_high = Column(NUMBER(20,4))
    s_dq_low = Column(NUMBER(20,4))
    s_dq_close = Column(NUMBER(20,4))
    s_dq_volume = Column(NUMBER(20,4))
    s_dq_amount = Column(NUMBER(20,4))
    