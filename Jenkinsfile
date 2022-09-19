pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin 352708296901.dkr.ecr.eu-north-1.amazonaws.com
                docker build -t danishain-bot:0.0.$BUILD_NUMBER .
                docker tag danishain-bot:0.0.$BUILD_NUMBER 352708296901.dkr.ecr.eu-north-1.amazonaws.com/danishain-bot:0.0.$BUILD_NUMBER
                docker push 352708296901.dkr.ecr.eu-north-1.amazonaws.com/danishain-bot:0.0.$BUILD_NUMBER
                '''
            }
        }
        stage('Stage II') {
            steps {
                sh 'echo "stage II..."'
            }
        }
        stage('Stage III ...') {
            steps {
                sh 'echo echo "stage III......"'
            }
        }
    }
}