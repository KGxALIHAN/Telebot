import asyncio
from handlers import (myinfo,random,start,review_dialog,add_dish,get_dish)
from config import dp,bot,db


dp.include_router(start.start_router)
dp.include_router(random.random_router)
dp.include_router(myinfo.my_info_router)
dp.include_router(review_dialog.review_router)
dp.include_router(add_dish.admin_dish_router)
dp.include_router(get_dish.get_dish_router)

async def main():
    db.create_tables()
    await dp.start_polling(bot)



if __name__=='__main__':
    asyncio.run(main())



