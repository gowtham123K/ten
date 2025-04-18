pipeline {
    agent any

    stages {
        stage("cloning") {
            steps {
                git url: 'https://github.com/gowtham123K/ten.git', branch: 'main'
            }
        }

        stage("dependency") {
            steps {
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    python -m pip install --upgrade pip
                    pip install pytest
                '''
            }
        }

        stage("testing") {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    pytest test_hello.py
                '''
            }
        }

        stage("deploy") {
            steps {
                bat '''
                    call venv\\Scripts\\activate
                    python hello.py
                '''
            }
        }
    }
}
