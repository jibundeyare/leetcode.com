class UnionFindDict():
    def __init__(self):
        self.items = {}
        self.sizes = {}
        self.ranks = {}
        # counts how many disjoint sets there are
        self.disjoint_sets = 0

    def __len__(self) -> int:
        return len(self.items)

    def add(self, item: int|str, parent: int|str=None) -> bool:
        if item in self.items:
            return False

        self.disjoint_sets += 1

        if parent is None:
            self.items[item] = item
            self.sizes[item] = 1
            self.ranks[item] = 0
        else:
            self.items[item] = parent
            self.sizes[item] = 0
            self.ranks[item] = self.ranks[parent] + 1

        return True

    def union(self, a: int|str, b: int|str) -> None:
        self.union_by_rank(a, b)

    def union_by_size(self, a: int|str, b: int|str) -> None:
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return

        self.disjoint_sets -= 1

        if self.sizes[a] < self.sizes[b]:
            # b becomes a parent of a
            # a becomes a child of b
            self.items[a] = b
            self.sizes[b] += self.sizes[a]
            self.sizes[a] = 0
            self.ranks[a] = self.ranks[b] + 1
        else:
            # self.sizes[a] >= self.sizes[b]:
            # a becomes a parent of b
            # b becomes a child of a
            self.items[b] = a
            self.sizes[a] += self.sizes[b]
            self.sizes[b] = 0
            self.ranks[b] = self.ranks[a] + 1

    def union_by_rank(self, a: int|str, b: int|str) -> None:
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return

        self.disjoint_sets -= 1

        if self.ranks[a] > self.ranks[b]:
            # b becomes a parent of a
            # a becomes a child of b
            self.items[a] = b
            self.sizes[b] += self.sizes[a]
            self.sizes[a] = 0
            self.ranks[a] = self.ranks[b] + 1
        else:
            # self.ranks[a] <= self.ranks[b]:
            # a becomes a parent of b
            # b becomes a child of a
            self.items[b] = a
            self.sizes[a] += self.sizes[b]
            self.sizes[b] = 0
            self.ranks[b] = self.ranks[a] + 1

    def find(self, item: int|str) -> int|str:
        if self.items[item] == item:
            return item
        else:
            stack = [item]
            parent = self.items[item]

            while self.items[parent] != parent:
                stack.append(parent)
                parent = self.items[parent]

            while stack:
                item = stack.pop()
                self.items[item] = parent
                self.sizes[item] = 0
                self.ranks[item] = 1

            return parent

    def is_connected(self, a: int|str, b: int|str) -> bool:
        return self.find(a) == self.find(b)

    def is_root(self, item: int|str) -> bool:
        return self.find(item) == item

    def get_size(self, item: int|str) -> int:
        return self.sizes[self.find(item)]

if __name__ == '__main__':
    # test library

    n = 10

    union_find_dict = UnionFindDict()

    for i in range(n):
        union_find_dict.add(i)

    len(union_find_dict)

    for i in range(0, n, 3):
        if i + 1 < len(union_find_dict):
            union_find_dict.union_by_rank(i, i + 1)

        if i + 2 < len(union_find_dict):
            union_find_dict.union_by_rank(i, i + 2)

    union_find_dict.union_by_size(0, 3)

    for i in range(n):
        print(f'{i=}')
        print(f'{union_find_dict.is_connected(0, i)=}')
        print(f'{union_find_dict.is_root(i)=}')
        print(f'{union_find_dict.get_size(i)=}')
        print()

    print(f'{union_find_dict.disjoint_sets=}')
    print(f'{union_find_dict.items=}')
    print(f'{union_find_dict.sizes=}')
    print(f'{union_find_dict.ranks=}')

