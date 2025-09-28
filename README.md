# Gallerysite

This repository contains a small Django gallery application and manifests to run with Docker Compose (development) and Kubernetes (cluster).  It was set as the final project of the `Container Technology Foundations` short course in Sept 2025.

Overview
- Django app source: `gallery/`, `gallerysite/` (Django project)
- Docker Compose: `compose.yaml` (development)
- Kubernetes manifests: `k8s/` (Deployments, Services, PVCs, Secret, k6 script)

Quick start (development with Docker Compose)
1. Create a Python virtualenv and install dependencies (optional if using Docker):

	python -m venv .venv
	source .venv/bin/activate
	pip install -r requirements.txt

2. Run with Docker Compose (uses the included `compose.yaml`):

	docker compose -f compose.yaml up --build

	- The Django app will be available at http://localhost:8000
	- The Postgres data directory is mounted to `./db` in the repo.

Kubernetes (manifests)
All kubernetes manifests live in the `k8s/` directory. They include:

- `secret-db.yaml`         : Secret storing Postgres credentials
- `postgres-pvc.yaml`      : PVC for Postgres data
- `postgres-deployment.yaml` : Postgres Deployment
- `postgres-service.yaml`  : ClusterIP Service for Postgres
- `media-pvc.yaml`         : PVC for Django media/uploads
- `django-deployment.yaml` : Django Deployment
- `django-service.yaml`    : ClusterIP Service for Django
- `k6-gallery-test.js`     : k6 load test script

Deploy to Kubernetes
1. Build and push the Django image to a registry accessible by your cluster (for this assessment, the docker registry name is `jaga`):

	docker build -t <your-registry>/gallerysite:latest .
	docker push <your-registry>/gallerysite:latest

	Update `k8s/django-deployment.yaml` and set the `image:` field to your image ref.

2. Apply manifests in order (Secret, PVCs, Postgres, Django):

	kubectl apply -f k8s/secret-db.yaml
	kubectl apply -f k8s/postgres-pvc.yaml
	kubectl apply -f k8s/postgres-deployment.yaml
	kubectl apply -f k8s/postgres-service.yaml
	kubectl apply -f k8s/media-pvc.yaml
	kubectl apply -f k8s/django-deployment.yaml
	kubectl apply -f k8s/django-service.yaml

Accessing the app
- Quick (local):
  - Port-forward the service:

	 kubectl port-forward svc/gallery-django 8000:8000

	 Then open: http://localhost:8000


Testing & load testing
- Reproducible load test with k6:
  - Start port-forward as above, then run:

	 k6 run k8s/k6-gallery-test.js

  - To target a NodePort, set `TARGET_URL`:

	 TARGET_URL='http://<node-ip>:30080/' k6 run k8s/k6-gallery-test.js


Troubleshooting
- ALLOWED_HOSTS: The Django settings read `ALLOWED_HOSTS` from an environment variable (set in `k8s/django-deployment.yaml`) — don't set `'*'` in production.
- DB connection issues: check the `gallery-postgres` service and pod logs.

Useful kubectl commands
- kubectl get pods -l app=gallery-django -o wide
- kubectl logs deployment/gallery-django
- kubectl describe pod <pod-name>
- kubectl top pods


