import math

from ctci.datastructures.linkedlist import LinkedList

def sum_lists(num1, num2):
    num1_node = num1.head
    num2_node = num2.head

    num1_sum = 0
    power = 0

    while num1_node:
        num1_sum += num1_node.data * math.pow(10, power)
        power += 1
        num1_node = num1_node.next

    num2_sum = 0
    power = 0

    while num2_node:
        num2_sum += num2_node.data * math.pow(10, power)
        power += 1
        num2_node = num2_node.next

    answer = int(num1_sum + num2_sum)
    answer_list = LinkedList()

    power = math.floor(math.log10(answer))

    while power >= 0:
        digit = answer // math.pow(10, power)
        answer_list.add(int(digit))
        answer %= math.pow(10, power)
        power -= 1

    return answer_list
