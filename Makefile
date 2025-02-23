all:
	docker build -t yarodash/test-app ./test
	docker image push yarodash/test-app
	kubectl delete -f ./deploy.yaml
	kubectl create -f ./deploy.yaml
