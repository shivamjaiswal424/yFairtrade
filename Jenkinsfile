pipeline {
    agent any

    environment {
        SESSION_IMAGE_NAME = 'fairtrade_session'
        SERVER_IMAGE_NAME = 'fairtrade_server'
        APP_IMAGE_NAME = 'fairtrade'
        DOCKER_HUB_USERNAME = 'pythospach'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', 
                url: 'https://github.com/abhinav1829/FairTrade.git'
            }
        }

        stage('Pull Docker Images') {
            steps {
                sh """
                docker pull ${DOCKER_HUB_USERNAME}/${SESSION_IMAGE_NAME}:latest
                docker pull ${DOCKER_HUB_USERNAME}/${SERVER_IMAGE_NAME}:latest
                docker pull ${DOCKER_HUB_USERNAME}/${APP_IMAGE_NAME}:latest
                """
            }
        }


        stage('Run Docker Compose') {
            steps {
                script {
                    dir('/home/shivam/Desktop/fairtrade') {
                        sh '/usr/bin/docker-compose up -d'
                    }
                }
            }
        }
    }
}