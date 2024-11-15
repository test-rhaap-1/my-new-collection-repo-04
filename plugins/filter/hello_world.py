"""A hello-world filter plugin in my_new_collection_namespace_04.my_new_collection_name_04."""

from __future__ import absolute_import, annotations, division, print_function


__metaclass__ = type  # pylint: disable=C0103

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from typing import Callable


DOCUMENTATION = """
    name: hello_world
    author: My_new_collection_namespace_04 My_new_collection_name_04
    version_added: "1.0.0"
    short_description: Demo filter plugin that returns a Hello message.
    description:
      - This is a demo filter plugin designed to return Hello message.
    options:
      name:
        description: Value specified here is appended to the Hello message.
        type: str
"""

EXAMPLES = """
# hello_world filter example

- name: Display a hello message
  ansible.builtin.debug:
    msg: "{{ 'ansible-creator' | my_new_collection_namespace_04.my_new_collection_name_04.hello_world }}"
"""


def _hello_world(name: str) -> str:
    """Returns Hello message.

    Args:
        name: The name to greet.

    Returns:
        str: The greeting message.
    """
    return "Hello, " + name


class FilterModule:
    """filter plugin."""

    def filters(self: FilterModule) -> dict[str, Callable[[str], str]]:
        """Map filter plugin names to their functions.

        Returns:
            dict: The filter plugin functions.
        """
        return {"hello_world": _hello_world}
