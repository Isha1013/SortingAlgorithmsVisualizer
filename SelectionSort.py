import time

def select_sort(data, DrawArray, timeTick):
    for firstUnsorted in range(len(data) - 1):
        minVal = firstUnsorted
        for i in range((firstUnsorted + 1), len(data)):
            DrawArray(data, ['#00A36C' if x == i or x == minVal else '#FFBF00' for x in range(len(data))] )
            time.sleep(timeTick)

            if data[i] < data[minVal]:
                minVal = i
                
        data[minVal], data[firstUnsorted] = data[firstUnsorted], data[minVal]
        
    DrawArray(data, ['#00A36C' for _ in range(len(data))])