pipeline {
    agent any
    stages {
        stage('Build Monitor Service Precode Image') {
            steps {
                sh "docker build -t jackwhelan/cvi-monitor-precode:${BUILD_TAG} services/cvi-monitor -f services/cvi-monitor/precode.Dockerfile"
            }
        }
        stage('Run Monitor Service Linting') { 
            steps {
                sh "docker run --name ${BUILD_TAG}-linting jackwhelan/cvi-monitor-precode:${BUILD_TAG} pylint monitor_server"
            }
        }
        stage('Run Monitor Service Unit Tests') {
            steps {
                sh "docker run --name ${BUILD_TAG}-unit-tests jackwhelan/cvi-monitor-precode:${BUILD_TAG} pytest"
            }
        }
        stage('Docker Cleanup') {
            steps {
                sh "docker stop ${BUILD_TAG}-linting ${BUILD_TAG}-unit-tests | true"
                sh "docker rm ${BUILD_TAG}-linting ${BUILD_TAG}-unit-tests | true"
                sh "docker rmi jackwhelan/cvi-monitor-precode:${BUILD_TAG} | true"
            }
        }
    }
}
