import numpy as np

def imageRowToBlackWhiteCountArray(image_row):
    white_count = 0
    black_count = 0

    black_white_count_array = np.array([],dtype=int)

    for i in image_row:
        if i == 0:
            if white_count != 0:
                black_white_count_array = np.append(black_white_count_array, white_count)
                white_count = 0
            black_count += 1    
        else:
            if black_count != 0:
                black_white_count_array = np.append(black_white_count_array,black_count)
                black_count = 0
            white_count += 1

    if white_count != 0:
        black_white_count_array = np.append(black_white_count_array, white_count)
    else:
        black_white_count_array = np.append(black_white_count_array, black_count)

    return black_white_count_array

def boardDetect(black_white_count_array, threshold):
    same_count = 0
    array_length = len(black_white_count_array)
    current_base_value = black_white_count_array[0]

    for i in range(0, array_length - 1):
        if same_count != 7:
            if black_white_count_array[i] in (black_white_count_array[i+1] + 1, black_white_count_array[i+1] - 1, black_white_count_array[i+1]) and black_white_count_array[i] <= current_base_value + threshold and black_white_count_array[i] >= current_base_value - threshold:
                same_count += 1
                
                if same_count == 1:
                    current_base_value = black_white_count_array[i]

                if same_count == 1 and i > 1 and black_white_count_array[i - 1] > black_white_count_array[i]:
                    print("Executed")
                    same_count += 1

            else:
                same_count = 0
        else:
            return i, current_base_value
    
    return 0,0
        #   0 1 2 3 4 5 6 7 8 9 101112
image_row = [0,0,0,1,1,1,0,0,0,1,1,0,1,0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,1,1,1,1,0,1,0]

black_white_count_array = imageRowToBlackWhiteCountArray(image_row)

end_index, current_base_value = boardDetect(black_white_count_array,threshold=1)
print(end_index)
print(current_base_value)

starting_index = end_index - 7
print(black_white_count_array)
print(starting_index)

# print("All I care about: " + str(starting_index))
# print(black_white_count_array)
# print("Starting index " + str(black_white_count_array[starting_index]))
# print(starting_index)
# print(len(black_white_count_array) - 6)

uncompressed_starting_index = np.sum(a=black_white_count_array[0:starting_index], dtype=int)



