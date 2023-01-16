pipeline {
    agent {
        docker {
            // TODO build & push your Jenkins agent image, place the URL heree
            label 'danishain'
            image '352708296901.dkr.ecr.eu-north-1.amazonaws.com/danishain-jenkins-ex1:latest'
            args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        REGISTRY_URL = "public.ecr.aws/r7m7o9d4"
        IMAGE_TAG = "0.0.$BUILD_NUMBER"
        IMAGE_NAME = "danishain-bot-dev"
        }
    stages {
        stage('Build') {
            steps {
                // TODO dev bot build stage
                sh '''
                echo "building..."
                aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                docker build -t $IMAGE_NAME:$IMAGE_TAG . -f services/bot/Dockerfile
                docker tag $IMAGE_NAME:$IMAGE_TAG $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                echo "done"
                '''
            }
        }

        stage('Trigger Deploy') {
            steps {
                build job: 'BotDeploy', wait: false, parameters: [
                    string(name: 'BOT_IMAGE_NAME', value: "${REGISTRY_URL}/${IMAGE_NAME}:${IMAGE_TAG}")
                ]
            }
        }
    }
}