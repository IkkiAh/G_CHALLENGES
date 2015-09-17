n = int(raw_input());
array = raw_input().split();
array = map(int, array);
result = 0
for x in range(0,n):
    result += array[x];
print result