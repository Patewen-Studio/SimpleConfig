from typing import List, Optional
from simpleconfig.errors import ParseException


def prepare_item(item: str) -> str:
    return item.strip()


def prepare_value(value: str) -> str:
    comment = value.find("//")
    if comment != -1:
        return value[:comment]
    return value


class SimpleConfig:
    def __init__(self, delimiter: str = "=") -> None:
        self.data = {}
        self.delimiter = delimiter

    def update_data(self, field: List[str]) -> None:
        if len(field) < 2:
            raise ParseException("One of the variables has no input, maybe you forgot to enter a value?")

        key = field[0]
        value = field[1]

        prepared_key = prepare_item(key)
        delete_comment = prepare_value(value)
        prepared_value = prepare_item(delete_comment)
        self.data.update({prepared_key: prepared_value})

    def parse(self, path: str) -> None:
        with open(path) as file:
            self.base_parse(file.read())

    def base_parse(self, data: str) -> None:
        lines = data.splitlines()
        for field in lines:
            if not field:
                continue
            elif self.delimiter not in field:
                raise ParseException(f"`{lines}` isn't allowed syntax")
            field_ = field.split(self.delimiter)
            self.update_data(field_)

    def get(self, item: str) -> str:
        return self.data[item]

    def int(self, item: str) -> Optional[int]:
        try:
            return int(self.get(item))
        
        except ValueError as e:
            print(e)
    
    def boolean(self, item: str) -> Optional[bool]:
        try:
            return bool(self.get(item))
        
        except ValueError:
            return 
    
    def float(self, item: str) -> Optional[float]:
        try:
            return float(self.get(item))
        
        except ValueError:
            return 
        
    def generate_iter(self, item: str, to_type: type = str, delimiter: str = ",", return_list: bool = False):
        "Function of generation `map` object"
        
        try:
            res = map(to_type, self.get(item).split(delimiter))
            if return_list:
                return list(res)
            return res 
        
        except TypeError:
            raise ParseException("Function `generate_iter` returned a typing error, is this the correct type?")
        