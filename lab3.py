import random
import time


def generate_random_list(random_range, length):
    return random.sample(range(random_range), length)


def bubble_sort(list1):
    for i in range(len(list1)-1, 0, -1):
        for j in range(i):
            if list1[j] > list1[j+1]:
                temp_val = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp_val
    return list1


def selection_sort(list1):
    min_id = None
    for start in range(len(list1)):
        for i in range(start, len(list1)):
            if min_id is None or list1[i] < list1[min_id]:
                min_id = i
        temp_val = list1[start]
        list1[start] = list1[min_id]
        list1[min_id] = temp_val
    return list1


def quick_sort(list1):
    if len(list1) in [0, 1]:
        return list1
    else:
        pivot = list1[0]
        i = 0
        for j in range(len(list1)-1):
            if list1[j+1] < pivot:
                list1[j+1], list1[i+1] = list1[i+1], list1[j+1]
                i += 1
        list1[0], list1[i] = list1[i], list1[0]
        first_part = quick_sort(list1[:i])
        second_part = quick_sort(list1[i+1:])
        first_part.append(list1[i])
        return first_part + second_part


def main():
    random_list = generate_random_list(10000, 5000)

    start_time = time.time()
    bubble_sort(random_list.copy())
    print("Bubble sort execution time: {} s".format(round(time.time() - start_time, 2)))

    start_time = time.time()
    selection_sort(random_list.copy())
    print("Selection sort execution time: {} s".format(round(time.time() - start_time, 2)))

    start_time = time.time()
    print("Quick sort execution time: {} s".format(round(time.time() - start_time, 2)))

if __name__ == "__main__":
    main()