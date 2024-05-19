pipeline {
    agent {
        label 'windows'
    }

    environment {
        SERVER_IMAGE_NAME = 'fairtrade_flask_ml'
        APP_IMAGE_NAME = 'fairtrade_django'
        DOCKER_HUB_USERNAME = 'pythospach'
        DOCKER_PATH = 'C:/Program Files/Docker/Docker/resources/bin'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', 
                url: 'https://github.com/abhinav1829/FairTrade.git'
            }
        }

        stage('Pull') {
            steps {
                bat """
                "${DOCKER_PATH}/docker.exe" pull ${DOCKER_HUB_USERNAME}/${SERVER_IMAGE_NAME}:latest
                "${DOCKER_PATH}/docker.exe" pull ${DOCKER_HUB_USERNAME}/${APP_IMAGE_NAME}:latest
                """
            }
        }

        stage('Compose') {
            steps {
                bat """
                "${DOCKER_PATH}/docker-compose.exe" -f "${PROJECT_DIR}/docker-compose.yml" up -d
                """
            }
        }

        stage('Test') {
            steps {
                bat """
                "${DOCKER_PATH}/docker-compose.exe" exec django python manage.py test
                """
            }
        }
    }
}