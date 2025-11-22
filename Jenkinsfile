pipeline {
    agent {
        docker {
            image 'python:3.9-slim'
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }
    environment {
        RECIPIENTS = 'tejadigitalworld@gmail.com' // <-- change this to your email list (comma-separated)
        ALLURE_RESULTS = 'allure-results'
        ALLURE_REPORT = 'allure-report'
    }
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install python deps (ensure allure-pytest is in requirements or install explicitly)
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests (collect Allure results)') {
            steps {
                // Run tests and collect allure results. Adjust command if you use a custom test runner.
                // If you do not use pytest, update this to your test command that writes to ${ALLURE_RESULTS}.
                sh 'pytest --alluredir=${ALLURE_RESULTS} || true'
            }
        }
        stage('Publish Allure Report') {
            steps {
                // This uses the Allure Jenkins plugin to generate a report from ${ALLURE_RESULTS}.
                // The Allure plugin must be installed on the Jenkins master.
                script {
                    allure includeProperties: false, jdk: '', results: [[path: "${env.ALLURE_RESULTS}"]]
                }
            }
        }
    }
    post {
        always {
            // Archive the generated Allure report directory (if any)
            archiveArtifacts artifacts: "${env.ALLURE_REPORT}/**", allowEmptyArchive: true

            // Zip the report folder so it can be attached to email
            sh "if [ -d \"${env.ALLURE_REPORT}\" ]; then zip -r allure-report.zip ${env.ALLURE_REPORT}; fi" 

            // Send email with attachment using Email Extension plugin (emailext)
            // Requires: Email Extension plugin + SMTP configured in Jenkins global settings
            emailext(
                to: "${env.RECIPIENTS}",
                subject: "Jenkins: Build ${env.JOB_NAME} #${env.BUILD_NUMBER} - ${currentBuild.currentResult}",
                body: "Build: ${env.BUILD_URL}\n\nPlease find attached the Allure report (if it was generated).",
                attachLog: true,
                attachmentsPattern: 'allure-report.zip'
            )
        }
    }
}