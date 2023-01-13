import asyncio
import uuid
from typing import MutableMapping

from aio_pika import Message, connect
from aio_pika.abc import (
    AbstractChannel, AbstractConnection, AbstractIncomingMessage, AbstractQueue,
)


class RpcClient:
    connection: AbstractConnection
    channel: AbstractChannel
    callback_queue: AbstractQueue
    loop: asyncio.AbstractEventLoop

    def __init__(self) -> None:
        self.futures: MutableMapping[str, asyncio.Future] = {}
        self.loop = asyncio.get_running_loop()

    # подключение к порту, создание канала и очереди
    async def connect(self) -> "RpcClient":
        self.connection = await connect(
            "amqp://guest:guest@localhost/", loop=self.loop,
        )
        self.channel = await self.connection.channel()
        self.callback_queue = await self.channel.declare_queue(exclusive=True)
        await self.callback_queue.consume(self.on_response)

        return self

    def on_response(self, message: AbstractIncomingMessage) -> None:
        future: asyncio.Future = self.futures.pop(message.correlation_id)
        future.set_result(message.body)

    # отправка сообщения и ожидания ввода
    async def call(self, sentence: str) -> str:
        correlation_id = str(uuid.uuid4())
        future = self.loop.create_future()

        self.futures[correlation_id] = future

        await self.channel.default_exchange.publish(
            Message(
                sentence.encode(),
                content_type="text/plain",
                correlation_id=correlation_id,
                reply_to=self.callback_queue.name,
            ),
            routing_key="rpc_queue",
        )

        return await future


async def zodiac_generate(sentence: str) -> str:
    rpc = await RpcClient().connect()
    responce = await rpc.call(sentence)
    return responce.decode()
