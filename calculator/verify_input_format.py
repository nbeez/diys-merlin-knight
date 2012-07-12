import json
import validictory
from validictory.validator import ValidationError

class verifier:
    """ This class verifies the content formats of the json dumps
    recieved from the gui. The two dumps are:
    1. List of items
    2. List of payees
    {"item-list":{
            "name":"a",
            "date":"1/1/2001",
            "item":[
                {"name":"b", "price":40,
                "participant-list":{
                    "participant":[{"name":"c"},{"name":"d"}]}
                },
                {"name":"e", "price":100,
                "participant-list":{
                    "participant":[{"name":"f"},{"name":"g"},{"name":"h"}]}
                }]
            }
        }
    """
    def __init__(self):
        print("This class verifies the item and payee list formats")
        self.participant_schema = {"type":"string"}
        self.participant_list_schema = {"type":"array","items":self.participant_schema}
        self.item_schema = {"type":"object","properties":{
            "name":{"type":"string"},
            "price":{"type":"string"},
            "participant-list":{"type":self.participant_list_schema}
        }}
        self.item_list_schema = {"type":"object","properties":
                                {"item-list":{"type":"object","properties":{
                                    "name":{"type":"string"},
                                    "date":{"type":"string","format":"date"},
                                    "item":{"type":"array", "items":self.item_schema}
                                }}}
                           }

    def verify_item_list(self, item_list_json_eg):
        validictory.validate(item_list_json_eg, self.item_list_schema)
#        try:
#            validictory.validate(item_list_json_eg, self.item_list_schema)
#        except(ValidationError):
#            print("ValidationError in json")
#            return False
#        return True



