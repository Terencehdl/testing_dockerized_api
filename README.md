# CI/CD Pipeline for API Testing

I've created a CI/CD pipeline to automate testing for an API. This pipeline tests an API that predicts sentiment in English phrases.

## API Overview

- **Endpoints**: `/status`, `/permissions`, `/v1/sentiment`, `/v2/sentiment`
- **Docker Image**: `datascientest/fastapi:1.0.0`
- **Manual Test**: `docker container run -p 8000:8000 datascientest/fastapi:1.0.0`

## Testing Scenarios

### 1. Authentication

Test the login system by sending GET requests to `/permissions` using different usernames and passwords.

### 2. Authorization

Check user rights by testing `/v1/sentiment` and `/v2/sentiment` endpoints for different users.

### 3. Content

Test API functionality by analyzing sentiment for specific phrases.

## Testing Setup

- Separate Docker containers for each scenario.
- Dockerfiles for each container.
- `docker-compose.yml` for orchestration.
- Use `setup.sh` to build images and start the pipeline.

## Result

- After the pipeline runs, check `api_test.log` for test results.

## Files Included

- `docker-compose.yml`: Pipeline orchestration.
- `Dockerfile.*`: Dockerfiles for test containers.
- `setup.sh`: Script to build images and start the pipeline.
- `api_test.log`: Log of test results.
- `log.txt`: Captured logs and outputs.

Feel free to adapt this pipeline to your needs. Enjoy seamless API testing!

## License

This project is licensed under the [MIT License](LICENSE).
