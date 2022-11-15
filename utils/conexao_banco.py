

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm.session import sessionmaker
initial = 'postgresql+asyncpg://'
userepassword = 'lsottatjfyeluh:cab1c44d49503426eca5afbc0c2dd4a8042284ca121c7d69b0b903dcfeb5df47'
host = '@ec2-54-147-36-107.compute-1.amazonaws.com/'
db = 'd45cl2103817o3'
DATABASE_URL = f'{initial}{userepassword}{host}{db}'
print(DATABASE_URL)

engine = create_async_engine(DATABASE_URL)
async_session = sessionmaker(engine, class_=AsyncSession)


