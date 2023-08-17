# Websocket messages streaming tool

This is a tool for the Skanestas test task.

## Installation

Please install Python 3.9 or higher. 

Take requirements.txt form the repo and use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Usage

Go to the directory of the downloaded project and execute the main file.

```bash
python3 python_home/wss_stream.py
```
To stop the tool just kill the process.

## Design description

1. Tool takes takes desired(default is 10) quantity of messages from the source "wss://test-ws.skns.dev/raw-messages". Let's call it "message window".
2. It parses messages to the Python objects and put it to the list with length equal to "message window" length. 
3. Then the tool sort the list according the "id" keys.
4. It connects to the target source and sends each list's element with deleting this element from the list.
The tool sens it to "wss://test-ws.skns.dev/ordered-messages/kovtun".
5. On the 4th step it also counts time of the sending of the all set of messages from the "message window". And if time is less then previous smallest time, tool will "record" it by sending to the screen.

