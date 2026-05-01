pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t csv-analyzer .'
            }
        }

        stage('Run Docker Container') {
            steps {
                bat 'docker run --rm csv-analyzer'
            }
        }
    }
}