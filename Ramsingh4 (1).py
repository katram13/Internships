def countDivisible(array, positive_int):
    count = 0
    for x in array:
        if x % positive_int == 0:
            count += 1
    return count

def main():
    array_a = [20, 21, 25, 28, 33, 34, 35, 36, 41, 42]
    positive_int_a = 7
    final_a = countDivisible(array_a,positive_int_a)
    print(f"The amount of numbers that are divisible by {positive_int_a} are: {final_a}")

    array_b = [18, 54, 76, 81, 36, 48, 99]
    positive_int_b = 9
    final_b = countDivisible(array_b, positive_int_b)
    print(f"The amount of numbers that are divisible by {positive_int_b} are: {final_b}")

main()
