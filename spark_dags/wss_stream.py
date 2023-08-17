import json
from websocket import create_connection
from time import time

N = 10
ws_recv = create_connection("wss://test-ws.skns.dev/raw-messages")


def message_handler(message_window):
    time_max: float = 100.0
    messages = []
    counter_of_messages = 0
    while True:
        result = ws_recv.recv()
        json_result = json.loads(result)
        messages.append(json_result)
        counter_of_messages += 1
        if counter_of_messages == message_window:
            # sorting of the messages' list
            messages.sort(key=lambda x: x["id"], reverse=True)
            '''
            for i in range(N):
                print(messages[i]["id"])
            print("\n")
            '''
            # sending results with showing the sending time
            time_initial = time()
            ws_send = create_connection("wss://test-ws.skns.dev/ordered-messages/kovtun")
            while len(messages) > 0:
                ws_send.send(json.dumps(messages.pop()))
            ws_send.close()
            time_diff = time() - time_initial
            if time_diff < time_max:
                time_max = time_diff
                print(time_diff)  # showing the minimum time taken to send all N ordered messages

            counter_of_messages = 0


if __name__ == '__main__':
    message_handler(N)
