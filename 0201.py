sw_n = int(input())
s = input().split()
st_n = int(input())
task = []
for i in range(st_n):
  task.append(input().split())

for i in range(len(s)):
  s[i] = int(s[i])

for i in range(len(task)):
  for j in range(2):
    task[i][j] = int(task[i][j])


def boy(n):
  m = n
  while(m<sw_n):
    if s[m-1] == 0:
      s[m-1] = 1
    else:
      s[m-1] = 0
    m = m + n

def girl(n):
  m = n-1
  if s[m] == 0:
    s[m] = 1
  else:
    s[m] = 0
  a = 1
  while (True):
    if ((m-a) < 0) or ((m+a) >= sw_n):
      break
    elif (s[m-a]) == (s[m+a]):
      if s[m-a] == 0:
        s[m-a] = 1
        s[m+a] = 1
      else:
        s[m-a] = 0
        s[m+a] = 0
      a += 1
    else:
      break

for i in range(st_n):
  if task[i][0] == 1:
    boy(task[i][1])
  else:
    girl(task[i][1])

result = " ".join(map(str, s))
print(result)