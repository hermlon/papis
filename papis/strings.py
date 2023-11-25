from typing import Any, Optional, NamedTuple, Union


class FormattedString(NamedTuple):
    """A tuple that defines a ``(formatter, string)`` pair.

    .. autoattribute:: formatter
    .. autoattribute:: value
    """

    #: The formatter that should be used on the string :attr:`value`. If none
    #: is provided, the default formatter is used, as defined by
    #: :ref:`config-settings-formatter`.
    formatter: Optional[str]
    #: Value of the
    value: str

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return repr(self.value)

    def __bool__(self) -> bool:
        return bool(self.value)

    # NOTE: __eq__ and __hash__ are implemented to ensure that formatted
    # strings can be used in 'click.option' with 'click.Choice'. This is not
    # very intuitive, as strings with the same text, but different formatters
    # will be equal.

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, str):
            return self.value == other
        elif isinstance(other, FormattedString):
            return self.value == other.value
        else:
            return False

    def __hash__(self) -> int:
        return hash(self.value)


AnyString = Union[str, FormattedString]


no_documents_retrieved_message = "No documents retrieved"
no_folder_attached_to_document = "Document has no folder attached"
time_format = "%Y-%m-%d-%H:%M:%S"
