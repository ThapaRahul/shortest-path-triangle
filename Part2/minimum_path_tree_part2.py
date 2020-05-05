# Rahul Thapa

def minimum_path_triangle(n):
  import time
  def make_triangle(n):
    triangle = []

    import random

    for i in range(n):
      temp_list = []
      for j in range(0, i+1):
        temp_list.append(random.randint(1, n**2))
      triangle.append(temp_list)

    return triangle

  triangle = make_triangle(n)

  memo = []
  
  start_time = time.time()
  for i in range(n):
    memo.append(triangle[n-1][i])

  for k in range(n-2, -1, -1):
    for i in range(len(triangle[k])):
      memo[i] = triangle[k][i] + min(memo[i], memo[i+1])

  t_temp = time.time() - start_time

  return triangle, memo[0], t_temp

minimum_path_triangle(10)

threshold = 60  # what is the largest time for one operation you want to run

def plot_efficiency(threshold):
  import time

  n = []
  t = []

  n_temp = 3000
  while(True):
    min_path, _, t_temp= minimum_path_triangle(n_temp)

    if t_temp>threshold:
      break

    n.append(n_temp)
    t.append(t_temp)

    n_temp += 1

    if (n_temp > 3005):
      break

  return n, t

n, t = plot_efficiency(threshold)

import matplotlib.pyplot as plt
plt.plot(n, t, 'o')
plt.title("Dynamic Programming Algorithm Running Time")
plt.xlabel("size of the base (n)")
plt.ylabel("run-time (t)")
plt.savefig("dymamic.png")

