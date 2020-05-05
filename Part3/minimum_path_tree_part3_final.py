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

  def make_priority_table(triangle):
    table = []

    import random

    for i in range(len(triangle)):
      for j in range(len(triangle[i])):
        table.append([triangle[i][j], (i, j), float('inf'), None])
    
    table[0][2] = triangle[0][0] 
    return table

  def find_min_idx(table):
    min_val = float('inf')
    for i in range(len(table)):
      if table[i][2] < min_val:
        min_idx = table[i][1]
        min_val = table[i][2]
    return min_idx, min_val 

  def dijkstra_min_path(triangle, table):
    N = len(table)
    num_ver_completed = 0
    while (True):
      min_idx, min_path = find_min_idx(table)
      # print(min_idx)
      # if (left_child_idx > N):
      #   num_ver_completed += 1
      parent_idx = int(min_idx[0]/2 * (2 + (min_idx[0] - 1)) + min_idx[1])
      left_child_idx = int((min_idx[0] + 1)/ 2* (2 + min_idx[0]) + min_idx[1])
      right_child_idx = left_child_idx + 1

      # num_ver_completed += 1

      if (left_child_idx < N):
        left_sum = table[parent_idx][2] + table[left_child_idx][0]
        if (left_sum < table[left_child_idx][2]):
          table[left_child_idx][2] = left_sum
          table[left_child_idx][3] = table[parent_idx][1]

        right_sum = table[parent_idx][2] + table[right_child_idx][0]
        if (right_sum < table[right_child_idx][2]):
          table[right_child_idx][2] = right_sum
          table[right_child_idx][3] = table[parent_idx][1]

        table[parent_idx][2] = float('inf')
      else:
        return min_path

  triangle = make_triangle(n)
  table = make_priority_table(triangle)
  
  start_time = time.time()

  path = dijkstra_min_path(triangle, table)

  t_temp = time.time() - start_time

  return path, triangle, t_temp

threshold = 60  # what is the largest time for one operation you want to run

def plot_efficiency(threshold):
  import time

  n = []
  t = []

  n_temp = 1
  while(True):
    min_path, _, t_temp= minimum_path_triangle(n_temp)

    # if t_temp>threshold:
    #   break

    n.append(n_temp)
    t.append(t_temp)

    n_temp *= 1.75

    n_temp = int(n_temp)

    if (n_temp > 100):
      break

  return n, t

n, t = plot_efficiency(threshold)

import matplotlib.pyplot as plt
plt.plot(n, t, 'o')
plt.title("Dijkstra Greedy Algorithm Running Time")
plt.xlabel("size of the base (n)")
plt.ylabel("run-time (t)")
plt.savefig("greedy.png")

