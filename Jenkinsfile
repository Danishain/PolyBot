pipeline {
   agent {
        docker {
            image '352708296901.dkr.ecr.eu-north-1.amazonaws.com/danishain-jenkins-agent'
             args  '--user root -v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

   options {
        buildDiscarder(logRotator(daysToKeepStr: '30'))
        disableConcurrentBuilds()
        timestamps()
        }
   environment {
        REGISTRY_URL = "352708296901.dkr.ecr.eu-north-1.amazonaws.com"
        IMAGE_TAG = "0.0.$BUILD_NUMBER"
        IMAGE_NAME = "danishain-bot"
        }
    stages {
        stage('Build') {
            steps {
                sh '''
                aws ecr get-login-password --region eu-north-1 | docker login --username AWS --password-stdin $REGISTRY_URL
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                docker tag $IMAGE_NAME:$IMAGE_TAG $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                docker push $REGISTRY_URL/$IMAGE_NAME:$IMAGE_TAG
                '''
            }
            post {
                always {
                    sh '''
                    docker image prune -f --filter "label=app=bot"
                    '''
                }
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