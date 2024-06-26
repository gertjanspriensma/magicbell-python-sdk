import typing

from ._base import BaseModel


class ChannelConfiguration(BaseModel):
    providers: typing.Dict


class Channel(BaseModel):
    slug: str
    configuration: typing.Optional[ChannelConfiguration] = None


class WrappedChannels(BaseModel):
    channels: typing.List[Channel]
