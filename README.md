# AWS-SG-IP-Updater

A Python application that updates your security group based off of your current IP address.

## Prerequisites
* [AWS CLI](https://aws.amazon.com/cli/) installed and configured with a default profile
* AWS Profile specified has necessary permissions to update an EC2 Security Group

## How do I get set up?

* Run `pip install --upgrade -r requirements.txt` to install the Boto3 & Requirements libraries.

## Debugging and development

* Development requirements are written inside `requirements-dev.txt` file. You
  can use ipdb for debugging and developing the script. You need to use
  python3.6 or higher for the following instructions

  ```
  % export PYTHONBREAKPOINT=ipdb.set_trace
  ```

  If you put `breakpoint()` line, this is going to open ipdb debugger.

## ToDo

* add in more error handling
* Change response to be a friendly message vs. json output
* Add in functionality to be able to pass in which AWSCLI profile you want to use.

