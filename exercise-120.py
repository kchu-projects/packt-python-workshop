import execnet
from execnet import makegateway


def square(channel):
    while not channel.isclosed():
        number = channel.receive()
        number_squared = number ** 2
        channel.send(number_squared)


gateway = makegateway()
channel = gateway.remote_exec(square)


for i in range(10):
    channel.send(i)
    i_squared = channel.receive()
    print(f"{i} squared is {i_squared}")
