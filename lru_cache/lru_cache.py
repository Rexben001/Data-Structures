from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """

    def __init__(self, limit=10):
        self.limit = limit
        self.contents = DoublyLinkedList()
        self.dict = {}
        self.count = 0

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """

    def get(self, key):
        if self.contents.length == 0:
            return None
        elif key in self.dict:
            #get the node
            node = self.dict[key]
            # add to the end
            self.contents.move_to_end(node)
            # return the nodes value which is the second element
            return node.value[1]
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """

    def set(self, key, value):
        # check if the key is in the dict
        if key in self.dict:
            # get the node using the key
            node = self.dict[key]
            # replace the value with key and value
            node.value = (key, value)
            return
        if self.limit == self.count:
            # delete the key from the cache at the head
            del self.dict[self.contents.head.value[0]]
            # remove the node from the head
            self.contents.remove_from_head()
            # decrease the size/count
            self.count -= 1
        # add the value to the tail
        self.contents.add_to_tail((key, value))
        # add the tail node to the dict
        self.dict[key] = self.contents.tail
        # increase the size/count
        self.count += 1
