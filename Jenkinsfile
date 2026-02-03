pipeline {
    agent any

    options {
        timestamps()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    environment {
        VENV_DIR = ".venv"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Verify Python') {
            steps {
                sh '''
                    echo "Python location:"
                    which python3
                    python3 --version
                '''
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    rm -rf ${VENV_DIR}
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate

                    python --version
                    python -m pip install --upgrade pip setuptools wheel
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Install Playwright Browsers') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    playwright install --with-deps
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate

                    pytest \
                      -v \
                      --tb=short \
                      --html=reports/pytest-report.html \
                      --self-contained-html \
                      --alluredir=reports/allure-results
                '''
            }
        }
    }

    post {
        always {
            echo "Archiving test reports"
            archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true
        }

        failure {
            echo "Build failed"
        }

        success {
            echo "Build successful"
        }

        cleanup {
            sh 'rm -rf ${VENV_DIR}'
        }
    }
}
