# On EC2

aws configure  # (set keys, region us-east-2)

aws ecr get-login-password --region us-east-2 | \
  docker login --username AWS --password-stdin 598927569795.dkr.ecr.us-east-2.amazonaws.com

docker pull 598927569795.dkr.ecr.us-east-2.amazonaws.com/housing-api:latest

docker run -d -p 80:80 --name housing-api \
  598927569795.dkr.ecr.us-east-2.amazonaws.com/housing-api:latest