from typing import Any, Callable, Self

from sqlalchemy.exc import ArgumentError
from sqlalchemy.sql import Select

# 1. 透過繼承，建立一個擁有新 where 功能的 Select 類別
class CustomSelect(Select):
    def select_from(self, *froms) -> Self:
        return super().select_from(*froms)

    def where(self, *whereclause):
        return super().where(*whereclause)

    def where_if(self, condition: Any, predicate: Callable[[], Any]):
        """
        當 condition 為 True 時，才執行 lambda 並加入 where 條件
        """
        if condition:
            # 呼叫父類別的原生 where
            return super().where(predicate())
        return self


# 2. 重新封裝同樣名稱的 select
def select(*entities, **kwargs) -> CustomSelect:
    """
    替代官方的 select()，回傳繼承自原生 Select 且支援 .where_if() 的物件。
    """
    if kwargs:
        raise ArgumentError("select() 不允許傳入關鍵字引數")

    # 實例化自定義的子類別
    return CustomSelect(*entities)