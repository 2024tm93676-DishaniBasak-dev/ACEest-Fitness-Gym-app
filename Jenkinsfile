pipeline {
    agent any

    tools {
        sonarScanner 'sonar-scanner'
    }

    stages {

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest'
            }
        }

      stage('SonarQube Analysis') {
            steps {
                 withSonarQubeEnv('SonarQube') {
                    sh '/opt/homebrew/Cellar/sonar-scanner/8.1.0.6389/libexec/bin/sonar-scanner'
                }
            }
        }

    }
}