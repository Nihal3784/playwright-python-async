pipeline {
    agent any

    // 1. Schedule nightly run (cron)
    triggers {
        cron('5 16 * * *') // runs daily at ~2 AM, H avoids collisions
    }

    environment {
        // Email credentials stored in Jenkins Credentials as "jenkins_email"
        SMTP_USER = credentials('jenkins_email_user')
        SMTP_PASS = credentials('jenkins_email_pass')

        // Playwright project paths
        REPORTS_DIR = 'reports'
        SCREENSHOTS_DIR = 'screenshots'
    }

    options {
        // Keep build logs for 30 days
        buildDiscarder(logRotator(daysToKeepStr: '30'))
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python -m venv .venv'
                sh '. .venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest tests --alluredir=$REPORTS_DIR --capture=tee-sys
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh '''
                    allure generate $REPORTS_DIR -o $REPORTS_DIR/html --clean
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/html/**', fingerprint: true
            archiveArtifacts artifacts: 'screenshots/**', fingerprint: true
            archiveArtifacts artifacts: 'logs/**', fingerprint: true
        }

        success {
            mail bcc: '',
                 body: "Build SUCCESSFUL\nCheck reports and screenshots attached.",
                 cc: '',
                 from: 'jenkins@example.com',
                 replyTo: 'jenkins@example.com',
                 subject: "Jenkins Build SUCCESS: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 to: 'nihal.j@cronberry.com'
        }

        failure {
            mail bcc: '',
                 body: "Build FAILED\nCheck reports and screenshots attached.",
                 cc: '',
                 from: 'jenkins@example.com',
                 replyTo: 'jenkins@example.com',
                 subject: "Jenkins Build FAILURE: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                 to: 'nihal.j@cronberry.com'
        }
    }
}
