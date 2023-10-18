import os
import json
import logging
from types import SimpleNamespace
from typing import Optional, OrderedDict, List

class Human(SimpleNamespace):
    def __init__(self, id:str):
        self.id = id
        
        self.vars_stat = OrderedDict()
        self.vars_html = OrderedDict()
        
        self.files = SimpleNamespace()
        self.files.json = os.path.join("docs", "data", f"{self.id}.json")
        self.files.log = os.path.join("logs", f"{self.id}.log")
        self.files.html = os.path.join("docs", "data", f"{self.id}.html")
        self.files.image = os.path.join("docs", "data", f"{self.id}.png")
        self.files.text = os.path.join("docs", "data", f"{self.id}.html")

        if os.path.exists(self.files.json):
            obj = json.load(open(self.files.json, "r"))
            assert obj["id"] == self.id
            self.vars_stat.update(obj["vars_stat"])
            self.vars_html.update(obj["vars_html"])

        self.save()
    
    def save(self):
        with open(self.files.json, "w") as f:
            json.dump(self.__dict__, f, indent=4, default=lambda x: x.__dict__)
