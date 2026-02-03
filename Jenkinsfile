pipeline {
    agent any

    options {
        timestamps()
        ansiColor('xterm')
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    environment {
        PYTHON_BIN = "/opt/homebrew/bin/python3.11"
        VENV_DIR  = ".venv"
        PIP_CACHE_DIR = "${WORKSPACE}/.pip-cache"
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
                    echo "Using Python binary:"
                    ${PYTHON_BIN} --version
                    which ${PYTHON_BIN}
                '''
            }
        }

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                    rm -rf ${VENV_DIR}
                    ${PYTHON_BIN} -m venv ${VENV_DIR}
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

            script {
                if (fileExists('reports/pytest-report.html')) {
                    echo "Pytest HTML report generated"
                } else {
                    echo "Pytest HTML report not found"
                }
            }
        }

        failure {
            echo "Build failed"
        }

        success {
            echo "Build successful"
        }

        cleanup {
            sh '''
                echo "Cleaning workspace virtual environment"
                rm -rf ${VENV_DIR}
            '''
        }
    }
}
