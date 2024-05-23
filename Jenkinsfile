pipeline {
    agent any

    environment {
        // Define any environment variables here if needed
    }

    stages {
        stage('Clone repository') {
            steps {
                script {
                    echo 'Cloning the repository...'
                    git url: 'https://github.com/Douaebouchaaboud/genielog'
                }
            }
        }
        stage('Install dependencies') {
            steps {
                script {
                    echo 'Installing dependencies...'
                    sh 'pip install -r requirements.txt'
                }
            }
        }
        stage('Run tests') {
            steps {
                script {
                    echo 'Running tests...'
                    sh 'python manage.py test'
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            // Add any cleanup tasks here if needed
        }
        success {
            echo 'Build completed successfully!'
        }
        failure {
            echo 'Build failed. Please check the logs.'
        }
    }
}
