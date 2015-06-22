class Node(object):
 
    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev
        self.next = next
 
 
class DoubleLinkedList(object):
 
    head = None
    tail = None
 
    def append(self, data):
        new_node = Node(data, None, None)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            new_node.next = None
            self.tail.next = new_node
            self.tail = new_node
        return new_node
 
    def remove(self, node_value):
        current_node = self.tail
 
        while current_node is not None:
            if current_node.data != node_value:
                # if it's not the first element
                current_node = current_node.prev
                #if current_node.prev is not None:
                    #current_node.prev.next = current_node.next
                    #current_node.next.prev = current_node.prev
                #else:
                    # otherwise we have no prev (it's None), head is the next one, and prev becomes None
                    #self.head = current_node.next
                    #current_node.next.prev = None
            else:
                if current_node.prev is not None:
                    current_node.prev.next = current_node.next
                if current_node.next is not None:
                    current_node.next.prev = current_node.prev
                current_node = None

    def remove_tail(self):
        node = self.tail
        self.tail = self.tail.prev
        if self.tail != None:
            self.tail.next = None
        else:
            self.head = None
        return node
