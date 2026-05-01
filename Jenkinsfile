pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t csv-analyzer .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run --rm csv-analyzer'
            }
        }
    }
}