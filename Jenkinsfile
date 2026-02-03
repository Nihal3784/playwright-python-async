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
        script {
            if (fileExists('reports/html/report.html')) {
                publishHTML(target: [
                    reportDir: 'reports/html',
                    reportFiles: 'report.html',
                    reportName: 'Playwright HTML Report',
                    keepAll: true
                ])
            } else {
                echo "HTML report not found, skipping publish"
            }
        }

        archiveArtifacts artifacts: 'screenshots/**, videos/**, traces/**', allowEmptyArchive: true
        }
    }
}
