pipeline {
    agent {
        docker {
            // TODO build & push your Jenkins agent image, place the URL here
            label 'danishain'
            image '352708296901.dkr.ecr.eu-north-1.amazonaws.com/danishain-jenkins-ex1:latest'
            args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        REGISTRY_URL = "352708296901.dkr.ecr.eu-north-1.amazonaws.com"
        IMAGE_TAG = "0.0.$BUILD_NUMBER"
        IMAGE_NAME = "danishain-bot"
        WORKSPACE = "/home/ec2-user/workspace/dev/BotBuild/"
        }
    stages {
        stage('Build') {
            steps {
                // TODO dev bot build stage
                sh '''
                echo "building..."
                aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                docker build -t $IMAGE_NAME:$IMAGE_TAG services/bot
                echo "done"
                '''
            }
        }

        stage('Trigger Deploy') {
            steps {
                build job: 'BotDeploy', wait: false, parameters: [
                    string(name: 'BOT_IMAGE_NAME', value: "${IMAGE_NAME}:${IMAGE_TAG}")
                ]
            }
        }
    }
}