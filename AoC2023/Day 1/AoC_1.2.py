# Template Codeforces
import sys
import re

def main():
    sum=0
    with open('AoC1.txt', 'r') as f:
        while True:
            input = f.readline().strip()
            nums = {'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
            if len(input): 
                print(input)

                nums_appear = {num: [i.start() for i in re.finditer(num, input)] for (key, num) in nums.items()}    
                nums_str = {key:[i.start() for i in re.finditer(key, input)] for key in nums}
                final_dic = nums_appear | nums_str

                for k, v in final_dic.copy().items():
                    if len(v) == 0:
                        del final_dic[k]

                minimo = 100
                left = ''
                for key, value in final_dic.items():
                    for val in value:
                        if 0 <= val < minimo:
                            minimo = val
                            left = key
                
                maximo = -1
                right = ''
                for key, value in final_dic.items():
                    for val in value:
                        if maximo < max(value):
                            maximo = max(value)
                            right = key
                
                
                if len(left) != 1:
                    left = nums[left]
                if len(right) != 1:
                    right = nums[right]

                values = str(left)+str(right)
                print(values)
                sum += int(values)                

            else:
                break
        
    print(sum)   
     
if __name__ == '__main__':
    main()