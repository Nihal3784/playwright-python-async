pipeline {
    agent any

    environment {
        PATH = "/usr/local/bin:/opt/homebrew/bin:${env.PATH}"
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
        which python3
        python3 --version

        python3 -m venv .venv
        . .venv/bin/activate

        python3 -m pip install --upgrade pip
        python3 -m pip install -r requirements.txt

        python3 -m playwright install
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
