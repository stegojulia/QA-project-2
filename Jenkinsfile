pipeline {
    agent any
    environment {
            PATH = "/home/julia/.local/bin:$PATH"
            ANS_HOME = tool('ansible')
    }
    stages {    

        stage('Test') {
            steps {
                
                sh "python3 -m venv venv"
                sh "bash ./venv/bin/activate"
                sh "pip3 install -r requirements.txt"
                
                dir('service-1') {
                    sh "DATABASE_URL=\"sqlite:///test.db\" /var/lib/jenkins/.local/bin/pytest"
                }
                dir('service-2') {
                    sh "DATABASE_URL=\"sqlite:///test.db\" /var/lib/jenkins/.local/bin/pytest"
                }
                dir('service-3') {
                    sh "DATABASE_URL=\"sqlite:///test.db\" /var/lib/jenkins/.local/bin/pytest"
                }
                dir('service-4') {
                    sh "DATABASE_URL=\"sqlite:///test.db\" /var/lib/jenkins/.local/bin/pytest"
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
