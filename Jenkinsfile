pipeline {
    agent any
    environment {
            PATH = "/home/julia/.local/bin:$PATH"
            ANS_HOME = tool('ansible')
    }
    stages {    

        stage('Test') {
            steps {
                dir('service-1') {
                    sh DATABASE_URL="sqlite:///test.db" pytest 
                }
                dir('service-2') {
                    sh DATABASE_URL="sqlite:///test.db" pytest 
                }
                dir('service-3') {
                    sh DATABASE_URL="sqlite:///test.db" pytest 
                }
                dir('service-4') {
                    sh DATABASE_URL="sqlite:///test.db" pytest 
                }
            }
        }
        stage('Deploy') {
            steps {
                ansiblePlaybook become: true, inventory: './inventory.yaml', playbook: './playbook.yaml'
            }
        }
    }
}
