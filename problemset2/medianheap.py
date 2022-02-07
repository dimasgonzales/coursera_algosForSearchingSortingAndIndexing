from selectors import EpollSelector
from minheap import MinHeap
from maxheap import MaxHeap


class MedianMaintainingHeap:
    def __init__(self):
        self.hmin = MinHeap()
        self.hmax = MaxHeap()

    def size(self):
        return self.hmin.size() + self.hmax.size()

    def satisfies_assertions(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0
            return
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1
            return
        # 1. min heap min element >= max heap max element
        assert (
            self.hmax.max_element() <= self.hmin.min_element()
        ), f"Failed: Max element of max heap = {self.hmax.max_element()} > min element of min heap {self.hmin.min_element()}"
        # 2. size of max heap must be equal or one lessthan min heap.
        s_min = self.hmin.size()
        s_max = self.hmax.size()
        assert (
            s_min == s_max or s_max == s_min - 1
        ), f"Heap sizes are unbalanced. Min heap size = {s_min} and Maxheap size = {s_max}"

    def __repr__(self):
        return "Maxheap:" + str(self.hmax) + " Minheap:" + str(self.hmin)

    def get_median(self):
        if self.hmin.size() == 0:
            assert self.hmax.size() == 0, "Sizes are not balanced"
            assert False, "Cannot ask for median from empty heaps"
        if self.hmax.size() == 0:
            assert self.hmin.size() == 1, "Sizes are not balanced"
            return self.hmin.min_element()
        # your code here

        median_value = None
        if self.size() % 2 == 0:  # even case
            median_value = (self.hmax.max_element() + self.hmin.min_element()) / 2
        else:
            median_value = self.hmin.min_element()
        return median_value

    # function: balance_heap_sizes
    # ensure that the size of hmax == size of hmin or size of hmax +1 == size of hmin
    # If the condition above does not hold, move the max element from max heap into the min heap or
    # vice versa as needed to balance the sizes.
    # This function could be called from insert/delete_median methods
    def balance_heap_sizes(self):
        # your code here
        heap_delta = self.hmin.size() - self.hmax.size()
        if (heap_delta == 0) or (heap_delta == 1):
            return

        if self.hmin.size() > self.hmax.size():
            min_ele = self.hmin.min_element()
            self.hmax.insert(min_ele)
            self.hmin.delete_min()            
        else:
            max_ele = self.hmax.max_element()
            self.hmin.insert(max_ele)
            self.hmax.delete_max()
        self.balance_heap_sizes()

    def insert(self, elt):
        # Handle the case when either heap is empty
        if self.hmin.size() == 0:
            # min heap is empty -- directly insert into min heap
            self.hmin.insert(elt)
            return
        if self.hmax.size() == 0:
            # max heap is empty -- this better happen only if min heap has size 1.
            assert self.hmin.size() == 1
            if elt > self.hmin.min_element():
                # Element needs to go into the min heap
                current_min = self.hmin.min_element()
                self.hmin.delete_min()
                self.hmin.insert(elt)
                self.hmax.insert(current_min)
                # done!
            else:
                # Element goes into the max heap -- just insert it there.
                self.hmax.insert(elt)
            return
        # Now assume both heaps are non-empty
        # your code here
        maxheap_root = self.hmax.max_element()
        if elt < maxheap_root:
            self.hmax.insert(elt)
        else:
            self.hmin.insert(elt)
        self.balance_heap_sizes()

    def delete_median(self):
        self.hmax.delete_max()
        self.balance_heap_sizes()
