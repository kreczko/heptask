

```
docker build -t kreczko/htcondor-in-a-box . -f Dockerfile.htcondor
docker run --name htcondor -td kreczko/htcondor-in-a-box
docker exec -ti htcondor bash
```
