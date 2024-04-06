import asyncio
import logging
import sys

from bot import config

async def main():
    await config.dp.start_polling(config.bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
