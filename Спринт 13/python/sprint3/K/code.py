def merge(arr, lf, mid, rg):
	# Your code
	# “ヽ(´▽｀)ノ”
	pass


def merge_sort(arr, lf, rg):
	# Your code
	# “ヽ(´▽｀)ノ”
	pass

def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected

if __name__ == '__main__':
    test()


def main():
    count_line = int(input())
    flower_mans = [None] * count_line
    for i in range(count_line):
        start, end = map(int, input().split())
        flower_mans[i] = [start, end]

    flower_mans.sort()
    results = []
    idx = 0
    big_start, big_end = flower_mans[idx]
    idx += 1
    while idx < count_line:
        if big_start <= flower_mans[idx][0] <= big_end:
            _, curr_end = flower_mans[idx]
            idx += 1
            if curr_end > big_end:
                big_end = curr_end
        else:
            results.append([big_start, big_end])
            big_start, big_end = flower_mans[idx]
            idx += 1
    results.append([big_start, big_end])

    for res in results:
        print(*res)


if __name__ == '__main__':
    main()