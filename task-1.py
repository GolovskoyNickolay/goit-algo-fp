# Клас для вузла однозв'язного списку
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


# Функція для реверсування однозв'язного списку
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev


# Функція сортування однозв'язного списку методом злиття
def merge_sort(head):
    if not head or not head.next:
        return head

    # Знайти середину списку
    middle = get_middle(head)
    next_to_middle = middle.next
    middle.next = None

    # Рекурсивно сортувати дві половини
    left = merge_sort(head)
    right = merge_sort(next_to_middle)

    # Об'єднати відсортовані половини
    sorted_list = merge_sorted_lists(left, right)
    return sorted_list


def get_middle(head):
    if not head:
        return head

    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


# Функція об'єднання двох відсортованих списків в один відсортований список
def merge_sorted_lists(l1, l2):
    dummy = ListNode()
    tail = dummy

    while l1 and l2:
        if l1.value < l2.value:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    if l1:
        tail.next = l1
    if l2:
        tail.next = l2

    return dummy.next


# Функція для виведення елементів списку
def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Приклад використання
if __name__ == "__main__":
    # Створення однозв'язного списку: 4 -> 2 -> 1 -> 3 -> None
    head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))

    print("Початковий список:")
    print_list(head)

    # Реверсування списку
    reversed_head = reverse_list(head)
    print("\nРеверсований список:")
    print_list(reversed_head)

    # Сортування списку
    sorted_head = merge_sort(reversed_head)
    print("\nВідсортований список:")
    print_list(sorted_head)

    # Об'єднання двох відсортованих списків
    list1 = ListNode(1, ListNode(3, ListNode(5)))
    list2 = ListNode(2, ListNode(4, ListNode(6)))
    merged_head = merge_sorted_lists(list1, list2)
    print("\nОб'єднаний відсортований список:")
    print_list(merged_head)
