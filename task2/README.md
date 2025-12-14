For this task I use phyton (FastAPI) as the api and Postgre as the Database

## Setup
### 1. Clone .env file
```
cp .env.example .env
```

### 2. Generate TLS Cert
```
mkdir -p certs

openssl req -x509 -nodes -days 365 \
  -newkey rsa:2048 \
  -keyout certs/myapp.local.key \
  -out certs/myapp.local.crt \
  -subj "/CN=myapp.local"
```

### 3. Create Basic Auth
```
mkdir -p auth

docker run --rm -it httpd:2.4-alpine \
  htpasswd -nb admin strongpassword \
  > auth/testpasswd
```
Replace ```admin``` and ```strongpassword``` with desired credentials.

### 4. Config Local DNS
Add the following line to /etc/hosts:
```
127.0.0.1 myapp.local
```

## Running The Containers
### 1. Build Image for API
```
docker build -t api:1.0 .
```

### 2. Run Docker Compose
```
docker compose up

or

docker compose up -d
```

## Access The API
### 1. Root endpoint
```
curl -k -u admin:strongpassword https://myapp.local:8443/
```

Expected response
```
{"message":"TEST"}
```

### 2. Health check
```
curl -k -u admin:strongpassword https://myapp.local:8443/healthz
```

Expected response
```
{"status":"ok"}
```