import heapq

def k_way_merge(sorted_runs):
    return list(heapq.merge(*sorted_runs))

if __name__ == "__main__":
    assert k_way_merge([[1, 5, 9], [2, 6, 10], [3, 4, 8]]) == [1, 2, 3, 4, 5, 6, 8, 9, 10]
    print("[PASS] 048_external_merge_sort")
