class MaxHeap: #O(logn)
    def __int__(self):
        self.heap = []

    def _swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j],self.heap[i]

    def get_left_child_index(index):
        return (index * 2) + 1

    def get_right_child_index(index):
        return (index * 2) + 2

    def get_parent_index(index):
        return (index -1) // 2

    def heapify_up(self):
        current_index = len(self.heap) - 1
        while current_index > 0:
            parent_index = self.get_parent_index(current_index)
            if self.heap[current_index] > self.heap[parent_index]:
                self._swap(current_index,parent_index)
                current_index = parent_index
            else:
                break

    def pop(self):
        if len(self.heap) == 0:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down()

        return max_value

    def heapify_down(self):
        current = 0
        while True:
            left_child_index = self.get_left_child_index(current)
            right_child_index = self.get_right_child_index(current)
            largest = current


            if (left_child_index < len(self.heap) and
                    self.heap[left_child_index] > self.heap[current]):
                largest = left_child_index

            if (right_child_index < len(self.heap) and
                    self.heap[right_child_index] > self.heap[largest]):
                largest = right_child_index

            if largest != current:
                self._swap(current,largest)
                current = largest

            else:
                break

#minheap
import heapq
heap = [8,4,1,7]
heapq.heapify(heap)
print(heap)
min_element = heapq.heappop(heap)
print(heap)
add_new = heapq.heappush(heap,3)
print(heap)



