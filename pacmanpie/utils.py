from typing import ItemsView, Any


def _generate_variable_expression(name: str, value: Any) -> str:
    value = f"'{value}'" if isinstance(str, value) else value
    return f"{name}={value}"


def generate_repr(self) -> str:
    class_name: str = self.__class__.__name__
    class_items: ItemsView[str, Any] = self.__dict__.items()
    return \
        f"<{class_name} object: {' '.join(_generate_variable_expression(name, value) for name, value in class_items if not name.startswith('_'))}>"
