pipeline {
    agent any
    environment {
            PATH = "/home/julia/.local/bin:$PATH"
            ANS_HOME = tool('ansible')
    }
    stages {    

        stage('Test') {
            steps {
                echo "${env.PATH}"
            }
        }
        stage('Deploy') {
            steps {
                ansiblePlaybook become: true, inventory: './inventory.yaml', playbook: './playbook.yaml'
            }
        }
    }
}
