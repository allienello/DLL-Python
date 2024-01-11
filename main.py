
from typing import TypeVar, List

T = TypeVar("T") #gen type
Node = TypeVar("Node")  # node object


class Node:
    """
    Implementation of a doubly linked list node.
    Skeleton code given through class.
    """
    __slots__ = ["value", "next", "prev", "child"]

    def __init__(self, value: T, next: Node = None, prev: Node = None, child: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        """
        self.next = next
        self.prev = prev
        self.value = value

        # The child attribute is only used for the application problem
        self.child = child

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Skeleton code given by class.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    # My Code Below #

    def empty(self) -> bool:
        """
        Tests if the DLL is empty.

        :return: True if empty, False if not empty.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if not self.head:
            return True
        else:
            return False

    def push(self, val: T, back: bool = True) -> None:
        """
        Adds a node containing val to the back or front of the DLL; updates size accordingly.

        :param back: If true, add val to the back of the DLL. If false, add to the front.
        :return: None

        Time complexity: O(1)
        Space complexity: O(1)
        """
        newnode = Node(val)

        if back: # if back is true (add to back)
            if self.tail: # if the tail exists
                newnode.prev = self.tail # prev pointer is now the tail
                self.tail.next = newnode
                self.tail = newnode
            else: # if DLL is empty
                self.head = newnode
                self.tail = newnode
        else: # if back is false (add to front)
            if self.head: # if the head exists
                newnode.next = self.head
                self.head.prev = newnode
                self.head = newnode
            else: # if DLL is empty
                self.head = newnode
                self.tail = newnode

        self.size += 1 # increase size

        return None

    def pop(self, back: bool = True) -> None:
        """
        Removes a node from the back or front of the DLL; updates size accordingly.

        :param back: If true, remove from the back of the DLL. If false, remove from the front.
        :return: None

        Time Complexity: O(1)
        Space Complexity: O(1)
        """
        if back:
            if self.tail:
                if self.tail.prev:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev
                else:
                    self.head = None
                    self.tail = None
        else:
            if self.head:
                if self.head.next:
                    self.head.next.prev = None
                    self.head = self.head.next
                else:
                    self.head = None
                    self.tail = None

        self.size -= 1

        return None

    def list_to_dll(self, source: List[T]) -> None:
        """
        Creates a DLL from a Python list. If nodes exists in the DLL, it should be cleared
        and replaced by source.

        :param source: Standard Python list from which to construct DLL.
        :return: None

        Time complexity: O(n)
        Space complexity: O(n)
        """
        self.size = 0
        self.head = None
        self.tail = None

        for i in source:
            self.push(i)

        return None

    def dll_to_list(self) -> List[T]:
        """
        Creates a standard Python list from a DLL.

        :return list: Returns list[T] containing the values of the
        nodes in the DLL.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        dll_list = []
        current = self.head

        while current:
            dll_list.append(current.value)
            current = current.next

        return dll_list

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Constructs list of Nodes with value v in the DLL and returns the
        associated Node object list.

        :param val:T: Value to find in the DLL.
        :return list[Node]: List of the Node objects in the DLL whose value is val. If val
        does not exist in DLL, returns empty list.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        find_list = []
        current = self.head

        while current:
            if current.value == val:
                if find_first:
                    find_list.append(current)
                    return find_list
                find_list.append(current)
            current = current.next

        return find_list

    def find(self, val: T) -> Node:
        """
        Finds first Node with value val in the DLL and returns the
        associated Node object.

        :param val:T: Value to find in the DLL.
        :return: First Node object in the DLL whose value is val. If val
        does not exist in the DLL, returns None.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        find_list = self._find_nodes(val)

        if find_list:
            return find_list[0]
        else:
            return None

    def find_all(self, val: T) -> List[Node]:
        """
        Finds all Node objects with value val in the DLL and returns a
        standard Python list of the associated Node objects.

        :param val:T: Value to find in the DLL.
        :return List[Node]: Standard Python list of all Node objects in the DLL
        whose value is val. If val does not exist in the DLL, returns an empty list.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        find_list = self._find_nodes(val)

        if find_list:
            return find_list
        else:
            return []

    def _remove_node(self, to_remove: Node) -> None:
        """
        Given a reference to a node in the DLL, removes it.

        :param to_remove: Node: Node to be removed from the DLL.
        :return: None

        Time complexity: O(1)
        Space complexity: O(1)
        """
        if to_remove is None:
            return

        if to_remove.prev:
            to_remove.prev.next = to_remove.next
        else:
            self.head = to_remove.next

        if to_remove.next:
            to_remove.next.prev = to_remove.prev
        else:
            self.tail = to_remove.prev

        self.size -= 1

        return None


    def remove(self, val: T) -> bool:
        """
        Removes first Node with value val in the DLL.

        :param val:T: Value to remove from the DLL.
        :return: True if a Node with value val was found and removed
        from the DLL, else False.

        Time complexity: O(n)
        Space complexity: O(1)
        """
        if self.find(val): # if node to be removed is found
            self._remove_node(self.find(val)) # remove that node
            return True
        else:
            return False

    def remove_all(self, val: T) -> int:
        """
        Removes all Node objects with value val in the DLL.

        :param val:T: Value to remove from the DLL.
        :return: Number of Node objects with value val removed from the
        DLL. If no node containing val exists in the DLL, returns 0.

        Time complexity: O(n)
        Space complexity: O(n)
        """
        node_list = self.find_all(val)

        for node in node_list:
            self._remove_node(node)

        return len(node_list)

    def reverse(self) -> None:
        """
        Reverses the DLL in-place by modifying all next and prev references
        of Node objects in the DLL. Updates self.head and self.tail accordingly.

        :return: None

        Time complexity: O(n)
        Space complexity: O(1)
        """
        if self.head is None:
            return None

        if self.head == self.tail:
            return None

        current = self.head

        while current:
            temp = current.next
            current.next = current.prev
            current.prev = temp
            current = current.prev

        temp = self.head
        self.head = self.tail
        self.tail = temp

        return None


"""
APPLICATION PROBLEM
~
The objective of this problem is to implement the 
logic of a forward and backward button on a web browser. However,
there is a twist. A browser attack that manipulates browser history by
redirecting the site many times exists on certain sites. In this problem, 
there is a function which will determine if sites are bad. If the site is 
indeed bad, it is skipped over.
~
"""

class BrowserHistory:

    def __init__(self, homepage: str):
        """
        Initializes an instance of the DLL class and adds the parameter
        homepage to the DLL; also initializes current as the tail since the
        functions traverse the tail from the back.

        :param homepage: The first element of the DLL.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        self.dll = DLL() # initialize instance of the dll class
        self.dll.push(homepage) # add the homepage to the dll
        self.current = self.dll.tail # since the functions traverse the dll from the back

    def get_current_url(self) -> str:
        """
        Gets the URL the browser is currently on by accessing the value of
        the DLL.

        :return: The URL the browser is currently set to.

        Time complexity: O(1)
        Space complexity: O(1)
        """
        return str(self.current.value)

    def visit(self, url: str) -> None:
        """
        Visit the URL supplied to the method; if there are other URLs after
        the current, remove them from the DLL.

        :return: None

        Time complexity: O(n)
        Space complexity: O(1)
        """
        while self.current:
            if self.dll.tail is not self.current:
                self.dll.pop()
            else:
                self.dll.push(url)
                self.current = self.dll.tail
                break

    def backward(self) -> None:
        """
        Return to the last page in history, if there is no previous page
        don't go back. Skip over any 'bad' sites defined by metrics_api.

        :return: None

        Time complexity: O(n)
        Space complexity: O(1)
        """
        while self.current.prev:
            new_current = self.current.prev
            if not metrics_api(new_current.value):
                self.current = new_current
                break
            self.current = self.current.prev

    def forward(self) -> None:
        """
        Visit the page ahead of the current one in history, if currently on
        the most recent page then stay at the same page. Skip over bad pages.

        :return: None

        Time complexity: O(n)
        Space complexity: O(1)
        """
        while self.current.next:
            new_current = self.current.next
            if not metrics_api(new_current.value):
                self.current = new_current
                break
            self.current = self.current.next

# Code below given to test the application problem #
intervention_set = set(['https://malicious.com', 'https://phishing.com', 'https://malware.com'])
def metrics_api(url: str) -> bool:
    """
    Uses the intervention_set to determine what URLs are bad and which are good.

    :param url: The url to check.
    :returns: True if this is a malicious website, False otherwise.
    """
    if url in intervention_set:
        return True
    return False
