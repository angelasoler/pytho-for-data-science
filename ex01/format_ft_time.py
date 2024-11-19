import time

secs_since_epoch = time.time()
t_epoch = time.gmtime(0)
str_epoch = time.strftime("%B %-d, %Y", t_epoch)
time_now = time.localtime()
str_time_now = time.strftime("%b %d %Y", time_now)
decimal = f"{secs_since_epoch % 1:.4f}"[1:]

print(f'Seconds since {str_epoch}: {int(secs_since_epoch):,}{decimal} or {secs_since_epoch:.2e} in scientific notation')
print(str_time_now)
