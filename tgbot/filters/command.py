from dataclasses import dataclass

from aiogram import types
from aiogram.dispatcher.filters import BoundFilter

from tgbot.config import CommandInfo


@dataclass
class CommandFilter(BoundFilter):
    key = 'command'
    command: CommandInfo

    async def check(self, obj):
        if not isinstance(obj, types.Message):
            raise NotImplementedError("CommandFilter can only be used with Message")
        message: types.Message = obj
        return f"/{self.command.command}" == message.text or self.command.alias == message.text
