# AWS-SG-IP-Updater 

A Python application that updates your security group based off of your current IP address. 

## Prerequisites
* [AWS CLI](https://aws.amazon.com/cli/) installed and configured with a default profile
* AWS Profile specified has necessary permissions to update an EC2 Security Group

## How do I get set up? 

* Run `pip install --upgrade -r requirements.txt` to install the Boto3 & Requirements libraries. 

## ToDo 

* add in more error handling 
* Change response to be a friendly message vs. json output 
* Add in functionality to be able to pass in which AWSCLI profile you want to use. 
* Add in remove IP functionality

## Details
I frequently use a VPN, especially when on public or unknown Wi-Fi. For this reason I always had to login to the AWS Console anytime I wanted to connect to my EC2 instances to update security groups due to my always changing IP. I decided to write this python script to solve this problem.