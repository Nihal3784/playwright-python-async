pipeline {
    agent any

    environment {
        // Email credentials stored in Jenkins
        JENKINS_EMAIL_CREDENTIALS = 'jenkins_email_pass'
        RECIPIENT_EMAIL = 'nihal.j@cronberry.com'
        TZ = 'Asia/Kolkata' // Force timezone for cron and build
    }

    triggers {
        // Cron in IST timezone
        // 15 16 * * * -> 16:15 IST
        cron('15 16 * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Playwright Tests') {
            steps {
                // Run tests and generate reports
                sh 'pytest --alluredir=reports/allure-results'
            }
        }

        stage('Generate Allure Report') {
            steps {
                sh 'allure generate reports/allure-results --clean -o reports/allure-report || true'
            }
        }
    }

    post {
        always {
            node {
                // Archive Screenshots & Allure reports
                archiveArtifacts artifacts: 'screenshots/**, reports/**', allowEmptyArchive: true

                // Send email notification
                emailext(
                    subject: "Jenkins Build ${currentBuild.fullDisplayName}",
                    body: """Build Status: ${currentBuild.currentResult}

Check the reports and screenshots attached.

Jenkins Console: ${env.BUILD_URL}""",
                    to: "${env.RECIPIENT_EMAIL}",
                    attachLog: true,
                    attachmentsPattern: 'screenshots/**, reports/**',
                    mimeType: 'text/html',
                    credentialsId: "${env.JENKINS_EMAIL_CREDENTIALS}"
                )
            }
        }

        success {
            echo "Build succeeded!"
        }

        failure {
            echo "Build failed!"
        }
    }
}
