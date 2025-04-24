n=int(input())
songs=list(map(int,input().split()))

songs_set = set()
left = 0
ans = 0

for right in range(n):
    while songs[right] in songs_set:
        songs_set.remove(songs[left])
        left+=1
    songs_set.add(songs[right])
    ans=max(right-left+1,ans)

print(ans)

