pipeline {
    agent any

    tools {
        nodejs 'node'
    }

    environment {
        VENV = ".venv"
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    . $VENV/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                    playwright install
                '''
            }
        }

        stage('Run Tests') {
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
                reportName: 'Playwright HTML Report'
            ])

            allure([
                includeProperties: false,
                jdk: '',
                results: [[path: 'reports/allure-results']]
            ])

            archiveArtifacts artifacts: 'screenshots/**, videos/**, traces/**', allowEmptyArchive: true
        }
    }
}
