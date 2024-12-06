num_safe = 0
with open("aoc2input", "r") as file:
    test_count = 0
    for line in file:
        #if test_count > :
        #    break
        last_inc_num = 0
        last_dec_num = 999999

        isSafeInc = True
        isSafeDec = True
        isSafeDiff = True

        num = ""
        test_list = []
        isCorrected = False
        for i in range(0, len(line)):
            if line[i] == " " or line[i] == "\n":
            
                num = int(num)
                test_list.append(num)
    
                if not(1 <= abs(last_inc_num-num) <= 3) and not(i < (len(str(num))+1)):
                    # print(f"activating: length(str(bum)) = {len(str(num))} ")
                    isSafeDiff = False
                    break

                if last_inc_num > num:
                    isSafeInc = False

                if last_dec_num < num:
                    isSafeDec = False
                
                last_inc_num = num
                last_dec_num = num
                
                num = ""
            num += line[i]

        if (isSafeInc or isSafeDec) and isSafeDiff:
            num_safe += 1
           # print(f"Safe: {test_list}")

        elif not(isSafeDiff):
            # print(f"Unsafe list before check: {test_list}")
            # Testing Diffenece
            # print("testing difference")
            element = 0
            idx = 0
            for i in range(1, len(test_list)):
                if not(1<= abs(test_list[i-1] - test_list[i]) <= 3) and not(isCorrected):
                    element = test_list.pop(i)
                    i = i
                    # print(f"Popping element: {element}")
                    isCorrected = True
                    continue
                elif not(1<= abs(test_list[i-1] - test_list[i]) <= 3) and isCorrected:
                    test_list.insert(idx, element)
                    isCorrected = False
                    break
            
        elif not(isSafeInc):
            # print(f"Unsafe list before check: {test_list}")
 
            # Testing increasing list
             # print("testing increasing")
            element = 0
            idx = 0
            for i in range(1, len(test_list)):
                if isCorrected and i == (len(test_list)):
                    continue
                if test_list[i-1] > test_list[i] and not(isCorrected):
                    element = test_list.pop(i)
                    i = i
                    isCorrected = True
                    # print(f"Popping element: {element}")
                    continue
                elif test_list[i-1] > test_list[i] and isCorrected:
                    test_list.insert(idx, element)
                    isCorrected = False
                    break

        elif not(isSafeDec):
            # print(f"Unsafe list before check: {test_list}")
            # Testing Decreasing list
            # print("testing decreasing")
            element = 0
            idx = 0
            for i in range(1, len(test_list)):
                if isCorrected and i == (len(test_list)):
                    continue
                if test_list[i-1] < test_list[i] and not(isCorrected):
                    isCorrected = True
                    continue
                elif test_list[i-1] < test_list[i] and isCorrected:
                    test_list.insert(idx, element)
                    isCorrected = False
                    break
        
        if isCorrected:
            num_safe +=1
          #  print(f"Safe: {test_list}")
        #else:
            # print("still unsafe")


        test_count += 1
        

print(f"Number of safe reports: {num_safe}") 
