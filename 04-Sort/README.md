
# Sort


```python
%load_ext lab_black
```

 

## 0. Overview

- **제자리 정렬(in-place sort)**

    - 정렬할 항목의 수에 비해 아주 작은 저장 공간을 사용하는 방법


- **안정적 정렬(stable sort)**

    - 데이터 요소의 상대적인 순서를 보존
    - 데이터의 두 항목(요소)이 같을 때, 정렬 전의 위치 상태를 똑같이 유지

 

## 1. 2차 정렬

### 1) Bubble Sort

- 인접한 두 항목을 비교하여 정렬

- 시간복잡도는 $O(n^2)$


```python
seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
```


```python
length = len(seq) - 1
for num in range(length, 0, -1):
    for idx in range(num):
        # seq[idx] > seq[idx + 1] then Swap
        if seq[idx] > seq[idx + 1]:
            seq[idx], seq[idx + 1] = seq[idx + 1], seq[idx]
```


```python
# 함수로 만들기
def bubble_sort(seq):
    length = len(seq) - 1
    for num in range(length, 0, -1):
        for idx in range(num):
            if seq[idx] > seq[idx + 1]:
                seq[idx], seq[idx + 1] = seq[idx + 1], seq[idx]
    return seq
```


```python
seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]

bubble_sort(seq)
```




    [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]



 

### 2) Selection sort

- 가장 작거나 큰 요소를 찾아서 첫 번째 요소 또는 마지막 요소와 위치를 바꿔줌

- 위의 과정을 반복함

- 시간 복잡도는 $O(n^2)$


```python
seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
```


```python
for i in range(len(seq) - 1):
    min_idx = i
    for j in range(i + 1, len(seq)):
        if seq[min_idx] > seq[j]:
            min_idx = j
    seq[i], seq[min_idx] = seq[min_idx], seq[i]
```


```python
seq
```




    [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]




```python
# 함수로 만들기
def selection_sort(seq):
    for i in range(len(seq) - 1):
        min_idx = i
        for j in range(i + 1, len(seq)):
            if seq[min_idx] > seq[j]:
                min_idx = j
        seq[i], seq[min_idx] = seq[min_idx], seq[i]
    return seq
```


```python
seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]

selection_sort(seq)
```




    [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]



 

### 3) Insertion sort

- 배열의 맨 처음 정렬된 부분에, 정렬되지 않은 항목을 반복적으로 삽입

- 이미 정렬 되어 있는 경우 $O(n)$

- 평균 시간복잡도는 $O(n^2)$


```python
seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
```


```python
for i in range(1, len(seq)):
    j = i
    while j > 0 and seq[j - 1] > seq[j]:
        seq[j - 1], seq[j] = seq[j], seq[j - 1]  # swap
        j -= 1
    print(seq)
```

    [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
    [2, 4, 5, 1, 6, 2, 7, 10, 13, 8]
    [1, 2, 4, 5, 6, 2, 7, 10, 13, 8]
    [1, 2, 4, 5, 6, 2, 7, 10, 13, 8]
    [1, 2, 2, 4, 5, 6, 7, 10, 13, 8]
    [1, 2, 2, 4, 5, 6, 7, 10, 13, 8]
    [1, 2, 2, 4, 5, 6, 7, 10, 13, 8]
    [1, 2, 2, 4, 5, 6, 7, 10, 13, 8]
    [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]
    


```python
seq
```




    [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]




```python
# 함수로 만들기
def insertion_sort(seq):
    for i in range(1, len(seq)):
        j = i
        while j > 0 and seq[j - 1] > seq[j]:
            seq[j - 1], seq[j] = seq[j], seq[j - 1]
            j -= 1
    return seq
```


```python
seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]

insertion_sort(seq)
```




    [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]



 

### 4) Gnome sort

- 이동하면서 잘못 정렬된 값을 찾을 경우, 교환하면서 정렬

- 평균(또는 최악) 시간복잡도는 $O(n^2)$


```python
seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]
```


```python
idx = 0
while idx < len(seq):
    if idx == 0 or seq[idx - 1] <= seq[idx]:
        idx += 1
    else:
        seq[idx], seq[idx - 1] = seq[idx - 1], seq[idx]
        idx -= 1
```


```python
seq
```




    [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]




```python
# 함수로 만들기
def gnome_sort(seq):
    idx = 0
    while idx < len(seq):
        if idx == 0 or seq[idx - 1] <= seq[idx]:
            idx += 1
        else:
            seq[idx], seq[idx - 1] = seq[idx - 1], seq[idx]
            idx -= 1
    return seq
```


```python
seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]

gnome_sort(seq)
```




    [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]



 

## 2. 로그 선형 정렬

### 1) Merge sort

- 리스트를 반으로 나누어 정렬 되지 않은 리스트를 만듦

- 정렬되지 않은 두 리스트의 크기가 1이 될때까지 반으로 나눔

- 그런 다음, 리스트를 merge해 나가면서 정렬

- 시간복잡도는 $O(n \log n)$


```python
# 두 함수로 나눠서 구현
# 한 함수에서는 배열을 나누고
# 다른 함수에서는 배열을 병함
def merge_sort(seq):
    if len(seq) < 2:
        return seq
    # 배열을 나눠줌
    mid = len(seq) // 2
    left = merge_sort_sep(seq[:mid])
    right = merge_sort_sep(seq[mid:])
    # 나눈 후 Merge 해줌
    return merge(left, right)
```


```python
def merge(left, right):
    if not left or not right:
        return left or right
    result = []
    l_idx, r_idx = 0, 0
    while l_idx < len(left) and r_idx < len(right):
        if left[l_idx] <= right[r_idx]:
            result.append(left[l_idx])
            l_idx += 1
        else:
            result.append(right[r_idx])
            r_idx += 1
    if left[l_idx:]:
        result.extend(left[l_idx:])
    if right[r_idx:]:
        result.extend(right[r_idx:])
    return result
```


```python
seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]

merge_sort(seq)
```




    [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]



 

### 2) Quick sort

- 리스트에서 기준이 되는 하나의 요소를 피벗(pivot)이라 함

- 피벗(pivot)을 잘 선택하는 것이 성능의 핵심

- 피벗을 기준으로 리스트를 둘로 나눔


```python
def quick_sort(seq):
    if len(seq) < 2:
        return seq

    pivot_idx = len(seq) // 2  # 피벗 인덱스
    pivot = seq[pivot_idx]  # 피벗

    before = [x for i, x in enumerate(seq) if x <= pivot and i != pivot_idx]
    after = [x for i, x in enumerate(seq) if x > pivot and i != pivot_idx]

    print(before, [pivot], after)

    return quick_sort(before) + [pivot] + quick_sort(after)
```


```python
seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]

quick_sort(seq)
```

    [2, 1] [2] [4, 5, 6, 7, 10, 13, 8]
    [] [1] [2]
    [4, 5, 6] [7] [10, 13, 8]
    [4] [5] [6]
    [10, 8] [13] []
    [] [8] [10]
    




    [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]



 

### 3) Heap sort

- 시간복잡도 $O(n \log n)$

#### Heap

- 각 노드가 하위 노드보다 작은(또는 큰) 이진트리

- 리스트에서 가장 작은(또는 가장 큰)요소에 반복적으로 접근하는 프로그램에 유용

- 가장 작은(또는 큰) 요소를 처리하는 데에는 $O(1)$

- 그 외는 $O(\log{n})$


```python
import heapq
```


```python
def heap_sort(seq):
    h = []
    for val in seq:
        heapq.heappush(h, val)
    return [heapq.heappop(h) for _ in range(len(h))]
```


```python
seq = [4, 5, 2, 1, 6, 2, 7, 10, 13, 8]

heap_sort(seq)
```




    [1, 2, 2, 4, 5, 6, 7, 8, 10, 13]


