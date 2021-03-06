# generated by datamodel-codegen:
#   filename:  cancel_sale.json

from __future__ import annotations

from pydantic import BaseModel
from pydantic import Extra


class CancelSaleParameter(BaseModel):
    class Config:
        extra = Extra.forbid

    cs_asset_contract: str
    cs_asset_token_id: str
    cs_sale_type: str
    cs_sale_asset: str
