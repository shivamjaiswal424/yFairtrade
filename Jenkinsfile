pipeline {
    agent any

    environment {
        SERVER_IMAGE_NAME = 'pythospach/fairtrade_flask_ml'
        APP_IMAGE_NAME = 'pythospach/fairtrade_django'
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
                docker pull ${DOCKER_HUB_USERNAME}/${SERVER_IMAGE_NAME}:latest
                docker pull ${DOCKER_HUB_USERNAME}/${APP_IMAGE_NAME}:latest
                """
            }
        }

        stage('Run Docker Compose') {
            steps {
                script {
                    dir('C:/Users/Pythospach/Documents/GitHub/FairTrade') {
                        bat 'docker-compose up -d'
                    }
                }
            }
        }
    }
}