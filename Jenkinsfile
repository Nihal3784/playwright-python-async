pipeline {
    agent any

    environment {
        TZ = 'Asia/Kolkata' // Force IST timezone
    }

    triggers {
        cron('20 16 * * *') // 4:15 PM IST daily
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
            // Archive reports/screenshots
            archiveArtifacts artifacts: 'screenshots/**, reports/**', allowEmptyArchive: true

            // Send email notification (SMTP credentials configured in Jenkins)
            emailext(
                subject: "Jenkins Build ${currentBuild.fullDisplayName}",
                body: """Build Status: ${currentBuild.currentResult}

Check the reports and screenshots attached.

Jenkins Console: ${env.BUILD_URL}""",
                to: 'nihal.j@cronberry.com',
                attachLog: true,
                attachmentsPattern: 'screenshots/**, reports/**',
                mimeType: 'text/html'
            )
        }

        success {
            echo "Build succeeded!"
        }

        failure {
            echo "Build failed!"
        }
    }
}
