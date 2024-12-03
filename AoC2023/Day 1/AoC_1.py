import sys

def main():
    sum=0
    with open('AoC1.txt', 'r') as f:
        while True:
            input = f.readline().strip()
            if len(input): 
                i = 0
                j = len(input.strip())-1
                while not input[i].isnumeric():
                    i+=1
                while not input[j].isnumeric():
                    if j<i:
                        j=i
                        break
                    j-=1
                sum += int(str(input[i])+str(input[j]))
                sys.stdout.write(str(input[i])+str(input[j])+'\n') 
            else:
                break
        
        
    print(sum)   
     
if __name__ == '__main__':
    main()