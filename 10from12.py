def chess(k, l, m, n):
    if(k == m or m == n): return "YES"
    if(m-n == k-l): return "YES"
    if ((k + l) == (m + n)): return "YES"
    else: return "NO"
print(chess(6, 7, 7, 6))