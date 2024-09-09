def smallestGap(array):
    max_value = max(array)
    min_value = min(array)
    m_gap = max_value - min_value
    
    b = len(array)
    for i in range (b):
        for j in range(i+1, b):
           gap = abs(array[i] - array[j])
           if gap < m_gap:
               m_gap = gap
    return m_gap
                

def main():
    array_a = [50, 120, 250, 100, 20, 300, 200]
    array_b = [12.4, 45.9, 8.1, 79.8, -13.64, 5.09]
    final_a = smallestGap(array_a)
    print("The smallest gap between the numbers in the array is: ", final_a)
    final_b = smallestGap(array_b)
    print("The smallest gap between the numbers in the array is: ", final_b)
main()
