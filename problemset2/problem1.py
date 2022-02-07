from minheap import MinHeap
from maxheap import MaxHeap
from kheap import TopKHeap
from medianheap import MedianMaintainingHeap
import logging

logging.basicConfig(level=logging.INFO)


def test_min_heap():
    h = MinHeap()
    print("Inserting: 5, 2, 4, -1 and 7 in that order.")
    h.insert(5)
    print(f"\t Heap = {h}")
    assert h.min_element() == 5
    h.insert(2)
    print(f"\t Heap = {h}")
    assert h.min_element() == 2
    h.insert(4)
    print(f"\t Heap = {h}")
    assert h.min_element() == 2
    h.insert(-1)
    print(f"\t Heap = {h}")
    assert h.min_element() == -1
    h.insert(7)
    print(f"\t Heap = {h}")
    assert h.min_element() == -1
    h.satisfies_assertions()

    print("Deleting minimum element")
    h.delete_min()
    print(f"\t Heap = {h}")
    assert h.min_element() == 2
    h.delete_min()
    print(f"\t Heap = {h}")
    assert h.min_element() == 4
    h.delete_min()
    print(f"\t Heap = {h}")
    assert h.min_element() == 5
    h.delete_min()
    print(f"\t Heap = {h}")
    assert h.min_element() == 7
    # Test delete_max on heap of size 1, should result in empty heap.
    h.delete_min()
    print(f"\t Heap = {h}")
    assert h.size() == 0, "Minheap.delete_min() on heap of size 1, should result in empty heap"
    print("All tests passed: 10 points!")


def test_k_heap():
    h = TopKHeap(5)
    # Force the array A
    h.A = [-10, -9, -8, -4, 0]
    # Force the heap to this heap
    [h.H.insert(elt) for elt in [1, 4, 5, 6, 15, 22, 31, 7]]

    print("Initial data structure: ")
    print("\t A = ", h.A)
    print("\t H = ", h.H)

    # Insert an element -2
    print("Test 1: Inserting element -2")
    h.insert(-2)
    print("\t A = ", h.A)
    print("\t H = ", h.H)
    # After insertion h.A should be [-10, -9, -8, -4, -2]
    # After insertion h.H should be [None, 0, 1, 5, 4, 15, 22, 31, 7, 6]
    assert h.A == [-10, -9, -8, -4, -2]
    assert h.H.min_element() == 0, "Minimum element of the heap is no longer 0"
    h.satisfies_assertions()

    print("Test2: Inserting element -11")
    h.insert(-11)
    print("\t A = ", h.A)
    print("\t H = ", h.H)
    assert h.A == [-11, -10, -9, -8, -4]
    assert h.H.min_element() == -2
    h.satisfies_assertions()

    print("Test 3 delete_top_k(3)")
    h.delete_top_k(3)
    print("\t A = ", h.A)
    print("\t H = ", h.H)
    h.satisfies_assertions()
    assert h.A == [-11, -10, -9, -4, -2]
    assert h.H.min_element() == 0
    h.satisfies_assertions()

    print("Test 4 delete_top_k(4)")
    h.delete_top_k(4)
    print("\t A = ", h.A)
    print("\t H = ", h.H)
    assert h.A == [-11, -10, -9, -4, 0]
    h.satisfies_assertions()

    print("Test 5 delete_top_k(0)")
    h.delete_top_k(0)
    print("\t A = ", h.A)
    print("\t H = ", h.H)
    assert h.A == [-10, -9, -4, 0, 1]
    h.satisfies_assertions()

    print("Test 6 delete_top_k(1)")
    h.delete_top_k(1)
    print("\t A = ", h.A)
    print("\t H = ", h.H)
    assert h.A == [-10, -4, 0, 1, 4]
    h.satisfies_assertions()
    print("All tests passed - 15 points!")


def test_max_heap():
    h = MaxHeap()
    print("Inserting: 5, 2, 4, -1 and 7 in that order.")
    h.insert(5)
    print(f"\t Heap = {h}")
    assert h.max_element() == 5
    h.insert(2)
    print(f"\t Heap = {h}")
    assert h.max_element() == 5
    h.insert(4)
    print(f"\t Heap = {h}")
    assert h.max_element() == 5
    h.insert(-1)
    print(f"\t Heap = {h}")
    assert h.max_element() == 5
    h.insert(7)
    print(f"\t Heap = {h}")
    assert h.max_element() == 7
    h.satisfies_assertions()

    print("Deleting maximum element")
    h.delete_max()
    print(f"\t Heap = {h}")
    assert h.max_element() == 5
    h.delete_max()
    print(f"\t Heap = {h}")
    assert h.max_element() == 4
    h.delete_max()
    print(f"\t Heap = {h}")
    assert h.max_element() == 2
    h.delete_max()
    print(f"\t Heap = {h}")
    assert h.max_element() == -1
    # Test delete_max on heap of size 1, should result in empty heap.
    h.delete_max()
    print(f"\t Heap = {h}")
    print("All tests passed: 5 points!")


def test_median_heap():
    m = MedianMaintainingHeap()
    print("Inserting 1, 5, 2, 4, 18, -4, 7, 9")

    m.insert(1)
    print(m)
    print(m.get_median())
    m.satisfies_assertions()
    assert (
        m.get_median() == 1
    ), f"expected median = 1, your code returned {m.get_median()}"

    m.insert(5)
    print(m)
    print(m.get_median())
    m.satisfies_assertions()
    assert (
        m.get_median() == 3
    ), f"expected median = 3.0, your code returned {m.get_median()}"

    m.insert(2)
    print(m)
    print(m.get_median())
    m.satisfies_assertions()

    assert (
        m.get_median() == 2
    ), f"expected median = 2, your code returned {m.get_median()}"
    m.insert(4)
    print(m)
    print(m.get_median())
    m.satisfies_assertions()
    assert (
        m.get_median() == 3
    ), f"expected median = 3, your code returned {m.get_median()}"

    m.insert(18)
    print(m)
    print(m.get_median())
    m.satisfies_assertions()
    assert (
        m.get_median() == 4
    ), f"expected median = 4, your code returned {m.get_median()}"

    m.insert(-4)
    print(m)
    print(m.get_median())
    m.satisfies_assertions()
    assert (
        m.get_median() == 3
    ), f"expected median = 3, your code returned {m.get_median()}"

    m.insert(7)
    print(m)
    print(m.get_median())
    m.satisfies_assertions()
    assert (
        m.get_median() == 4
    ), f"expected median = 4, your code returned {m.get_median()}"

    m.insert(9)
    print(m)
    print(m.get_median())
    m.satisfies_assertions()
    assert (
        m.get_median() == 4.5
    ), f"expected median = 4.5, your code returned {m.get_median()}"

    print("All tests passed: 15 points")


def main():
    test_min_heap()
    test_k_heap()
    test_max_heap()
    test_median_heap()


if __name__ == "__main__":
    logging.info("Starting script")
    main()
    logging.info("Finished script")
