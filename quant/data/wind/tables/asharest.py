from ....common.db.sql import VARCHAR as VARCHAR2, Numeric as NUMBER, DateTime, Column, BaseModel


class AShareST(BaseModel):
    """
    中国A股特别处理

    Attributes
    ----------
    object_id: VARCHAR2(100)
        对象ID   
    s_info_windcode: VARCHAR2(40)
        Wind代码   
    s_type_st: VARCHAR2(8)
        特别处理类型   S:特别处理(ST)Z:暂停上市P:特别转让服务(PT)L:退市整理
    entry_dt: VARCHAR2(8)
        实施日期   
    remove_dt: VARCHAR2(8)
        撤销日期   

    """
    object_id = Column(VARCHAR2(100))
    s_info_windcode = Column(VARCHAR2(40))
    s_type_st = Column(VARCHAR2(8))
    entry_dt = Column(VARCHAR2(8))
    remove_dt = Column(VARCHAR2(8))
    