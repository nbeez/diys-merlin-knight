import json

class calculate:
    """Performs the donkey's work of putting information from two json dumps viz.
    1. List of items
    2. List of payees
    together and create a list of who-owes-whom-what
    """
    def helpful_links(self):
        print("nothing yet...")
        
class item_list:
    """ JSON for the item list recieved from the gui: 
    {"item-list":{
            "name":"a",
            "date":"1/1/2001",
            "items-bought":[
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
    def helpful_links(self):
        print("http://www.doughellmann.com/PyMOTW/json/")
        print("http://docs.python.org/library/json.html")
        
      
    
