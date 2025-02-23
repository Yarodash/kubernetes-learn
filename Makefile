create:
	kubectl create -f k8s/dev-namespace.yaml
	kubectl create -f k8s/service.yaml
	kubectl create -f k8s/storage.yaml
	kubectl create -f k8s/volume-claim.yaml

delete:
	kubectl delete -f k8s/service.yaml --ignore-not-found=true
	kubectl delete -f k8s/storage.yaml --ignore-not-found=true
	kubectl delete -f k8s/volume-claim.yaml --ignore-not-found=true
	kubectl delete -f k8s/deploy.yaml --ignore-not-found=true
	kubectl delete -f k8s/dev-namespace.yaml --ignore-not-found=true

build:
	docker build -t yarodash/echo-app ./app

push:
	docker image push yarodash/echo-app

deploy:
	kubectl delete -f k8s/deploy.yaml --ignore-not-found=true
	kubectl create -f k8s/deploy.yaml

fast-setup: build push create deploy
