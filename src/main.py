import asyncio
from entities.student import Student

print("Hello Python")


async def say_hello(ms: int):
    print("Hello world!")
    await asyncio.sleep(ms)
    print("Hello again!")


async def application():
    await say_hello(2)


task = application()
asyncio.run(task)

name: str = "324235"

s01 = Student(name="Tom", score=20)
s02 = Student(name="Jerry", score=19)

s01.print_score()
s02.print_score()

s01.get_grade()


print("Good bye Python")
