

```
docker build -t kreczko/htcondor-in-a-box .
docker run --name condor-test -td kreczko/htcondor-in-a-box
docker exec -ti condor-test bash
```
