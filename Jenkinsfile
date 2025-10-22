pipeline {
    agent {
        docker {
            image 'python:3.9-slim' // Use an official Python Docker image
            args '-v /var/run/docker.sock:/var/run/docker.sock' // If you need Docker inside Docker
        }
    }
    stages {
        stage('Checkout Code') {
            steps {
                // This step automatically clones your repository
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Jenkins will run these commands inside the python:3.9-slim container
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m sanity'
            }
        }
    }
}