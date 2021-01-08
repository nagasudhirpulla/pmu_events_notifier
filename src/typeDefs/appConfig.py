from typing import TypedDict, List


class IDbConfig(TypedDict):
    host: str
    port: int
    name: str
    username: str
    password: str


class IEmailConfig(TypedDict):
    emailAddress: str
    username: str
    password: str
    host: str


class IPersonInfo(TypedDict):
    name: str
    email: str


class IAppConfig(TypedDict):
    dbConfig: IDbConfig
    emailConfig: IEmailConfig
    persons: List[IPersonInfo]
    hrsOffset: int
    dataFilePath: str
