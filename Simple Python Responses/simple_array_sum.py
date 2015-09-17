n = int(raw_input());
array = raw_input().split();
array = map(int, array);
res = 0;

for x in range(0,n):
    y = array[x];
    res += y;

print res;
