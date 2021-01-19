import time

def bubble_sort(data, DrawArray, timeTick):
    for _ in range(len(data)-1):
        for i in range(len(data)-1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                DrawArray(data, ['#00A36C' if x == i or x == (i+1) else '#FFBF00' for x in range(len(data))] )
                time.sleep(timeTick)

    DrawArray(data, ['#00A36C' for _ in range(len(data))] )

   