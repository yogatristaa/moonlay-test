## Analysis

```
docker stats

ID            NAME                 CPU %       MEM USAGE / LIMIT  MEM %       NET IO          BLOCK IO           PIDS        CPU TIME      AVG CPU %
7026e708d097  task3_web_1          0.00%       5.485MB / 2.038GB  0.27%       2.88kB / 768B   1.012MB / 12.29kB  5           165.757ms     0.36%
a95bd71bf18d  task3_db_1           0.01%       22.11MB / 2.038GB  1.08%       2.748kB / 768B  0B / 52.54MB       6           1.343146s     2.96%
8a6f296a5780  task3_stress-test_1  396.65%     6.705MB / 2.038GB  0.33%       3.122kB / 768B  0B / 0B            10          2m57.899258s  390.59%
```

- Container stress-test consumes approximately 400% CPU. This behaviour is expected on this container which run a stress test command ["--cpu", "4", "--timeout", "300s"] , which running a load of 4 cores cpu for 300 seconds. But, the memory usage is relatively low.

- Container web which running a nginx webserver and container db which runing a postgres relatively idle. This behaviour shows that the stress test workload is only happen on the stress-test container.

## Suggestions
1. Apply Resource Limits

Limit CPU and memory to prevent the container from impacting other services/containers:
```
stress-test:
  image: polinux/stress
    command: ["--cpu", "4", "--timeout", "300s"]
    deploy:
    resources:
    limits:
      cpus: '1'
      memory: 128M
```

2. Separate Stress Test

If the docker compose is not intended as package of stress test action we can separate the stress-test container to spawn it on demand.