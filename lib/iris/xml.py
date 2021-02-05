# Copyright Iris contributors
#
# This file is part of Iris and is released under the LGPL license.
# See COPYING and COPYING.LESSER in the root of the repository for full
# licensing details.
"""
Utility functions for xml input/output.
"""

from xml.dom.minidom import Document


def sort_xml_attrs(doc):
    """
    Takes an xml document and returns a copy with all element
    attributes sorted in alphabetical order.

    """

    def _walk_nodes(node):
        """Note: _walk_nodes is called recursively on child elements."""

        # we don't want to copy the children here, so take a shallow copy
        new_node = node.cloneNode(deep=False)

        # Versions of python <3.8 order attributes in alphabetical order.
        # Python >=3.8 order attributes in insert order.  For consistent behaviour
        # across both, we'll go with alphabetical order always.
        # Remove all the attribute nodes, then add back in alphabetical order.
        attrs = [
            new_node.getAttributeNode(attr_name).cloneNode(deep=True)
            for attr_name in sorted(node.attributes.keys())
        ]
        for attr in attrs:
            new_node.removeAttributeNode(attr)
        for attr in attrs:
            new_node.setAttributeNode(attr)

        if node.childNodes:
            children = [_walk_nodes(x) for x in node.childNodes]
            for c in children:
                new_node.appendChild(c)

        return new_node

    nodes = _walk_nodes(doc.documentElement)

    ndoc = Document()
    ndoc.appendChild(nodes)
    return ndoc
