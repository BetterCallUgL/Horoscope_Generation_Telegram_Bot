import asyncio
import logging

from aio_pika import Message, connect
from aio_pika.abc import AbstractIncomingMessage
from generation import zodiac_model


async def main() -> None:
    # коннектимся к порту, создаём канал и очередь в которую будем принимать
    connection = await connect("amqp://guest:guest@localhost/")
    channel = await connection.channel()
    exchange = channel.default_exchange
    queue = await channel.declare_queue("rpc_queue")

    print(" [!] Awaiting RPC requests")
    # итерируемся по очереди
    async with queue.iterator() as qiterator:
        message: AbstractIncomingMessage
        async for message in qiterator:
            try:
                async with message.process(requeue=False):
                    assert message.reply_to is not None

                    # декодируем сообщение и генерируем сообщения
                    sentence = message.body.decode()
                    print(f" [!] Recieved {sentence}")
                    response = str(zodiac_model('UGLUGL/Horoscope_Generation').generate_zodiac(sentence)).encode()
                    
                    # отправляем сгенерированное сообщение в очередь.
                    await exchange.publish(
                        Message(
                            body=response,
                            correlation_id=message.correlation_id,
                        ),
                        routing_key=message.reply_to,
                    )
                    print("Request complete")
            except Exception:
                logging.exception("Processing error for message %r", message)


if __name__ == "__main__":
    asyncio.run(main())
