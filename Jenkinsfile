pipeline {
    agent any

    environment {
        VENV = ".venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
    steps {
        sh '''
            /usr/local/bin/python3.11 --version
            /usr/local/bin/python3.11 -m venv .venv
            . .venv/bin/activate
            pip install --upgrade pip
            pip install -r requirements.txt
            playwright install
        '''
            }
        }


        stage('Run Playwright Tests') {
            steps {
                sh '''
                    . $VENV/bin/activate
                    pytest
                '''
            }
        }
    }

    post {
        always {
            publishHTML(target: [
                reportDir: 'reports/html',
                reportFiles: 'report.html',
                reportName: 'Playwright HTML Report',
                keepAll: true,
                alwaysLinkToLastBuild: true
            ])

            allure([
                includeProperties: false,
                results: [[path: 'reports/allure-results']]
            ])

            archiveArtifacts artifacts: 'screenshots/**, videos/**, traces/**', allowEmptyArchive: true
        }
    }
}
