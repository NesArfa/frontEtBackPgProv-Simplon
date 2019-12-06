## Building a frontend-backend to learn kubenetes

* Frontend: a html page with javascript using jQuery.js
* Backend: a python script using sqlalchemy and flask
* Database: a PostgreSQL based on a pod set up by the administrator (Loick)

Build docker images for the frontend (`frontend`) and backend (`APY1`), e.g:
```buildoutcfg
docker build -t john-axel-front:1.0.6 frontend/
```
Tag and push to AWS:
```buildoutcfg
docker tag john-axel-front:1.0.6 *****.dkr.ecr.eu-west-1.amazonaws.com/john-axel-front:1.0.6
docker push *****.dkr.ecr.eu-west-1.amazonaws.com/john-axel-front:1.0.6
```
Create load balancer service on k8s:
```buildoutcfg
kubectl -n johnaxel-apy-ns apply -f frontend/podLB.yaml
kubectl -n johnaxel-apy-ns apply -f frontend/podLBfront.yaml
```
Add labels
```buildoutcfg
kubectl -n johnaxel-apy-ns label svc svc-load-front tier=tier-apy1-backendd
kubectl -n johnaxel-apy-ns label svc svc-load-front role=load-front
kubectl -n johnaxel-apy-ns label svc svc-load-apy tier=tier-apy1-backendd
kubectl -n johnaxel-apy-ns label svc svc-load-apy role=load-front
```
Deploy front and backend
```buildoutcfg
kubectl -n johnaxel-apy-ns apply -f frontend/deploypod.yaml
kubectl -n johnaxel-apy-ns apply -f APY1/deploy-apy1.yaml
```
Add the network polcy
```buildoutcfg
kubectl -n johnaxel-apy-ns apply -f APY1/networkPolicyBack_Loick.yaml
```

Navigate to the external load balancer and see if it works...
