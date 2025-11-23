pipeline {
    agent any
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
        stage('Run Tests inside Docker') {
            steps {
                // Runs tests inside the official python docker image using the host's docker daemon.
                // The Jenkins agent must have Docker installed and permission to run it.
                sh '''
                  docker run --rm \
                    -v ${WORKSPACE}:${WORKSPACE} \
                    -w ${WORKSPACE} \
                    python:3.9-slim \
                    bash -lc "pip install -r requirements.txt && pytest --alluredir=${ALLURE_RESULTS} || true"
                '''
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