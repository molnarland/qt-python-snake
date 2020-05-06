# This Python file uses the following encoding: utf-8

# if __name__ == "__main__":
#     pass

def loop():
  is_alive = True

  last_frame_time = time.time()
  while is_alive:
#    print("loop")
    current_time = time.time()
    if current_time >= last_frame_time + 1:
      last_frame_time = current_time
      print(current_time)
#      is_alive = False
