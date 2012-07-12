from calculator.verify_input_format import verifier

class verifier_tsting:
    def __init__(self):
        print("Doesnt do anything")

    def blah(self):
        """ format in xml:
        <item-list name="a" date="1/1/2001">
           <item name="b" price="40">
                <participant-list>
                    <participant name="c"/>
                    <participant name="d"/>
                </participant-list>
           </item>
           <item name="e" price="100">
                <participant-list>
                    <participant name="f"/>
                    <participant name="g"/>
                    <participant name="h"/>
                </participant-list>
           </item>
        </item-list>
        Equivalent in json:
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
        print("Doesnt do anything either")

item_list_json_eg = '{"item-list":{"name":"a","date":"1/1/2001","item":[{"name":"b", "price":"40","participant-list":{"participant":[{"name":"c"},{"name":"d"}]}},{"name":"e", "price":100,"participant-list":{"participant":[{"name":"f"},{"name":"g"},{"name":"h"}]}}]}}'
v = verifier()
verification_success = v.verify_item_list(item_list_json_eg)
print("Status of item list verification: ", verification_success)