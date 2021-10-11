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
                sh "docker run jackwhelan/cvi-monitor-precode:${BUILD_TAG} pylint cvi_monitor"
            }
        }
        stage('Run Monitor Service Unit Tests') { 
            steps {
                sh "docker run jackwhelan/cvi-monitor-precode:${BUILD_TAG} pytest"
            }
        }
    }
}