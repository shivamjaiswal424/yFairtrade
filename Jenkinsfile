pipeline {
    agent {
        label 'windows'
    }

    environment {
        SERVER_IMAGE_NAME = 'fairtrade_flask_ml'
        APP_IMAGE_NAME = 'fairtrade_django'
        DOCKER_HUB_USERNAME = 'pythospach'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', 
                url: 'https://github.com/abhinav1829/FairTrade.git'
            }
        }

        // stage('Pull') {
        //     steps {
        //         bat """
        //         docker pull ${DOCKER_HUB_USERNAME}/${SERVER_IMAGE_NAME}:latest
        //         docker pull ${DOCKER_HUB_USERNAME}/${APP_IMAGE_NAME}:latest
        //         """
        //     }
        // }

        stage('Compose') {
            steps {
                // bat """
                // docker-compose -f "${PROJECT_DIR}/docker-compose.yml" up -d
                // """
                bat """
                docker-compose up -d
                """
            }
        }

        stage('Test') {
            steps {
                bat """
                docker-compose exec django python manage.py test
                """
            }
        }
    }
    post {
        always {
            bat 'docker-compose down'
        }
    }
}