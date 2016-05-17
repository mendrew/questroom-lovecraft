

INIT_VALUE = 5

MAX_VALUE = 40

OVERFLOW_DELTA = 2

def get_time(current_value, stack=[]):

    if stack == []:
        overflow = 0
        last_value = current_value
        stack.append(overflow)
        stack.append(last_value)


    last_value = stack.pop()
    overflow = stack.pop()


    if last_value < OVERFLOW_DELTA and current_value > (MAX_VALUE - OVERFLOW_DELTA):
        overflow = overflow - 1
    elif last_value > (MAX_VALUE - OVERFLOW_DELTA) and current_value < OVERFLOW_DELTA:
        overflow = overflow + 1

    real_cur_value = current_value + (MAX_VALUE) * overflow


    if overflow >= 0:
        delta = abs(INIT_VALUE - real_cur_value)
    else:
        real_cur_value = abs(INIT_VALUE + abs(MAX_VALUE * overflow) - abs(current_value))
        delta = - real_cur_value
    # print("Overflow_value: {}, real_cur_value {}, delta {}".format(overflow, real_cur_value, delta))

    if INIT_VALUE <= real_cur_value:
        cur_time = 0 + delta/2  - int(delta/24) * 12
    else:
        cur_time = 12 - (delta/2 - int(delta/24) * 12)

    if cur_time == 12:
        cur_time = 0

    stack.append(overflow)
    last_value = current_value
    stack.append(last_value)

    return cur_time


if __name__ == "__main__":
    stack = []
    for value in range(0, MAX_VALUE-1) + range(0,MAX_VALUE-1) + range(MAX_VALUE, 0) + range(MAX_VALUE-1, 0):
    # for value in range(MAX_VALUE-1, -1, -1) + range(MAX_VALUE-1, -1, -1) + range(MAX_VALUE-1, -1, -1):
        cur_time = get_time(value, stack)
        print("Value: {} time {}".format(value, cur_time))
