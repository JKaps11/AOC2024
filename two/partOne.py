num_safe = 0
with open("aoc2input", "r") as file:
#    test_count = 0
    for line in file:
        #if test_count > 200:
        #    break
        last_inc_num = 0
        last_dec_num = 999999

        isSafeInc = True
        isSafeDec = True
        
        num = ""
#        test_list = []
        for i in range(0, len(line)):
            if line[i] == " " or line[i] == "\n":
            
                num = int(num)
#                test_list.append(num)
    
                if not(1 <= abs(last_inc_num-num) <= 3) and not(i < (len(str(num))+1)): 
#                    print(f"activating: length(str(bum)) = {len(str(num))} ")
                    isSafeDec = False
                    isSafeInc = False
                    break

                if last_inc_num > num:
                    isSafeInc = False

                if last_dec_num < num:
                    isSafeDec = False
                
                last_inc_num = num
                last_dec_num = num
                
                num = ""
            num += line[i]

        if isSafeInc or isSafeDec:
            num_safe += 1
            #print(f"Safe: {test_list}")
        #print(f"Unsafe: {test_list}")
#        test_count += 1
        

print(f"Number of safe reports: {num_safe}") 
