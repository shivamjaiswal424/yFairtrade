pipeline {
    agent any

    environment {
        SESSION_IMAGE_NAME = 'fairtrade_session:latest'
        SERVER_IMAGE_NAME = 'fairtrade_server:latest'
        APP_IMAGE_NAME = 'fairtrade:latest'
        DOCKER_HUB_USERNAME = 'pythospach'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', 
                url: 'https://github.com/adityavit36/speproject.git'
            }
        }

        stage('Pull Docker Images') {
            steps {
                script {
                    // Pull carprice Docker image from Docker Hub
                    docker.image("${DOCKER_HUB_USERNAME}/${CARPRICE_IMAGE_NAME}:latest").pull()

                    // Pull predictor-app Docker image from Docker Hub
                    docker.image("${DOCKER_HUB_USERNAME}/${PREDICTOR_IMAGE_NAME}:latest").pull()

                    // Pull model-loader Docker image from Docker Hub
                    docker.image("${DOCKER_HUB_USERNAME}/${MODEL_LOADER_IMAGE_NAME}:latest").pull()
                }
            }
        }

        stage('Run Docker Compose') {
            steps {
                script {
                    dir('/home/aditya/adityamin/MLOPS/mlops/src') {
                        sh '/usr/local/bin/docker-compose up -d'
                    }
                }
            }
        }
    }
}