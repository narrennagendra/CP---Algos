def max_skill(level,time_taken,jobs_taken):
    if level == n:
        return 0
    ans = max_skill(level+1, time_taken, jobs_taken)
    if time_taken + time[level] <= x and jobs_taken + 1 <= k:
        ans = max(ans, skill[level]+max_skill(level+1, time_taken + time[level], jobs_taken + 1))
    return ans
    
    
for _ in range(int(input())):
    n = int(input())
    x, k = map(int, input().split())
    time = []
    skill = []
    for _ in range(n):
        t, s = map(int, input().split())
        time.append(t)
        skill.append(s)
    print(max_skill(0,0,0))
