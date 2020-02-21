import re

class MessageStruct:
    '''
        {
            "attachments": [],
            "avatar_url": "https://i.groupme.com/123456789",
            "created_at": 1302623328,
            "group_id": "1234567890",
            "id": "1234567890",
            "name": "John",
            "sender_id": "12345",
            "sender_type": "user",
            "source_guid": "GUID",
            "system": false,
            "text": "Hello world ☃☃",
            "user_id": "1234567890"
        }
    '''
    def __init__(self, data):
        print(data)
        self._data = data

        if "name" in data:
            self.sender_name = data["name"]
        if "text" in data:
            self.text = data["text"]
        self.tokens = self.tokenize(self.text)
        return
    
    def tokenize(self, text):
        # ignore BOT_NAME in message
        text_arr = text.lower().split(" ")
        try:
            invocation_keyword = text_arr[0]
            cmd = text_arr[1]
            p = re.compile(cmd)
            for m in p.finditer(text):
                start_idx = (m.start() + len(m.group()) + 1)
                cmd_args = text[start_idx:].strip()
                print("query: {}, len: {}".format(cmd_args, len(cmd_args)))
            return {
                "invocation_keyword": invocation_keyword,
                "cmd": cmd,
                "cmd_args": cmd_args
            }
        except:
            raise Exception("Tokenization exception")
