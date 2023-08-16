import json
from websocket import create_connection

N = 10

'''
ws = create_connection("wss://test-ws.skns.dev/raw-messages")
message_list = []
for i in range(5):
    result = ws.recv()
    print(type(result))
    json_result = json.loads(result)
    print("---")
    print(type(json_result))
    print("***")
    #print(result["id"])
    print(json_result)
    print(json_result["id"])
    #json_result["id"] = int(json_result["id"])
    message_list.append(json_result)

message_list.sort(key=lambda x: x["id"], reverse=True)
print(message_list)
ws.close()
'''
#обязательно добавить контекст менеджер для коннекшена. Также можно добавить ООП

import asyncio
import websockets

async def my_websocket_function():
    async with websockets.connect('wss://test-ws.skns.dev/raw-messages') as websocket_recv:
        messages = []
        counter_of_messages = 0
        while True:
            response = await websocket_recv.recv()
            json_result = json.loads(response)
            messages.append(json_result)
            counter_of_messages += 1
            if counter_of_messages == N:
                #сортировка массива
                messages.sort(key=lambda x: x["id"], reverse=True)
                #отправка результата
                async with websockets.connect('wss://test-ws.skns.dev/ordered-messages/kovtun') as websocket_send:
                #websocket_send = websockets.connect('wss://test-ws.skns.dev/ordered-messages/kovtun')
                    while len(messages) > 0:
                        #print(messages)
                        await websocket_send.send(json.dumps(messages.pop()))
                #websocket_send.close()
                counter_of_messages = 0


# Запуск функции в асинхронном режиме
asyncio.get_event_loop().run_until_complete(my_websocket_function())


'''
ws_recv = create_connection("wss://test-ws.skns.dev/raw-messages")
messages = []
counter_of_messages = 0
while True:
    result = ws_recv.recv()
    json_result = json.loads(result)
    messages.append(json_result)
    counter_of_messages += 1
    if counter_of_messages == N:
        # сортировка массива
        messages.sort(key=lambda x: x["id"], reverse=True)
        # отправка результата
        ws_send = create_connection("wss://test-ws.skns.dev/ordered-messages/kovtun")
        while len(messages) > 0:
            ws_send.send(json.dumps(messages.pop()))
        ws_send.close()
        counter_of_messages = 0
'''