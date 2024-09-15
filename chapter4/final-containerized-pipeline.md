Picking up the pipeline from chapter 2, we can now use docker to skip installing the dependencies!

Before creating a pipeline with below install the 2 plugins - Docker plugin and Docker pipeline

```
pipeline {
    stages {
        stage('Checkout Code') {
            agent any
            steps {
                git branch: 'main', url: 'https://github.com/raghav710/sample-flaskql-calculator'
            }
        }
        stage('Build and Test') {
            agent {
                docker { 
                    image 'raghavmdu/flaskql-calculator:latest' 
                    args '-v .:/app'
                }
                reuseNode true
            }
            steps {
                bat 'cd /app && python -m pytest'
            }
        }
    }
}
```

However the above is known NOT to work in windows, so we could settle for the simpler

```
pipeline {
    agent any
    stages {
        stage('Checkout Code') {
            agent any
            steps {
                git branch: 'main', url: 'https://github.com/raghav710/sample-flaskql-calculator'
            }
        }
        stage('Build and Test') {
           
            steps {
                bat 'docker run -v C:\\Users\\LENOVO\\sample-flaskql-calculator:/app raghavmdu/flaskql-calculator:latest  python -m pytest /app'
            }
        }
    }
}
```