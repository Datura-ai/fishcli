from typing import List

from pydantic import BaseModel


class Datum(BaseModel):
    value: str


class Stake(BaseModel):
    data: List[Datum]


class Rank(BaseModel):
    uid: int
    data: List[Datum]


class Trust(BaseModel):
    data: List[Datum]


class Consensus(BaseModel):
    data: List[Datum]


class Incentive(BaseModel):
    data: List[Datum]


class Dividend(BaseModel):
    data: List[Datum]


class Emission(BaseModel):
    data: List[Datum]


class ValidatorTrust(BaseModel):
    data: List[Datum]


class Axon(BaseModel):
    data: List[Datum]


class BoolData(BaseModel):
    value: bool


class Active(BaseModel):
    data: List[BoolData]


class LastUpdate(BaseModel):
    data: List[Datum]


class Coldkey(BaseModel):
    data: List[Datum]


class ValidatorPermit(BaseModel):
    data: List[BoolData]


class HotKey(BaseModel):
    key: str


class Uids(BaseModel):
    stake: List[Stake]
    rank: List[Rank]
    trust: List[Trust]
    consensus: List[Consensus]
    incentive: List[Incentive]
    dividends: List[Dividend]
    emission: List[Emission]
    validatorTrust: List[ValidatorTrust]
    axons: List[Axon]
    active: List[Active]
    lastUpdate: List[LastUpdate]
    coldkey: List[Coldkey]
    validatorPermit: List[ValidatorPermit]
    hotkey: List[HotKey]


class Difficulty(BaseModel):
    value: str


class Subnet(BaseModel):
    uids: Uids
    difficulty: List[Difficulty]


class TotalIssuance(BaseModel):
    value: int
    blockNumber: int


class Data(BaseModel):
    subnets: List[Subnet]
    totalIssuance: List[TotalIssuance]


class FetchMetagraphData(BaseModel):
    data: Data
