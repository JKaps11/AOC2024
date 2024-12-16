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
            continue
            

        elif not(isSafeDiff):
            #print(f"Unsafe list before check: {test_list}")
            # Testing Diffenece
            #print("testing difference")
            element = 0
            for i in range(1, len(test_list)-1):
                if not(1<= abs(test_list[i-1] - test_list[i]) <= 3) and not(isCorrected):
                    
                    if i == len(test_list)- 1:
                        element=test_list.pop(i)
                        isSafeDiff = True
                        isCorrected = True
                        
                     
                    elif 1<= abs(test_list[i-1] - test_list[i+1]) <= 3:
                        element = test_list.pop(i)
                        isSafeDiff = True
                        isCorrected = True
                        break
                    
                elif isCorrected:
                    isSafeDiff = False
                    break
        
        elif not(isSafeInc):
            element = 0
            for i in range(1, len(test_list)):
                if i == len(test_list):
                    continue
                if test_list[i-1] > test_list[i] and not(isCorrected):
                    isSafeInc = True
                    element = test_list.pop(i)
                    idx = i
                    isCorrected = True    
                    continue

                elif test_list[i-1] > test_list[i] and isCorrected:
                    isSafeInc = False
                    test_list.insert(idx, element)
                    break

        elif not(isSafeDec):
            element = 0
            for i in range(1, len(test_list)):
                if test_list[i-1] < test_list[i] and not(isCorrected):
                    isCorrected = True
                    isSafeDec = True
                    continue
                elif test_list[i-1] < test_list[i] and isCorrected:
                    isSafeDec = False
                    break
        
        if isSafeDiff and (isSafeInc or isSafeDec):
            num_safe +=1

        test_count += 1
        

print(f"Number of safe reports: {num_safe}") 
