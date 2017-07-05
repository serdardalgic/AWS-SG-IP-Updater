import boto3
import getopt
import requests
import sys

# boto3    - The AWS SDK for Python
# getopt   - Helps scripts to parse the args in sys.argv
# requests - Python HTTP for Humans
# sys      - Provides access to variables used by the interpreter

    # Create a function to get current PUBLIC IP, returns correctly formated CIDR
def get_current_ip():
    """Returns your current IP in correct CIDR format for AWS"""
    r = requests.get(r'http://jsonip.com')
    return r.json()['ip'] + '/32'

def add_ip(current_ip, sg_id, port, protocol):
    """Add current IP to the security group"""

    # setup client for ec2
    client = boto3.client("ec2")

    # execute security group ingress Boto3 commands
    # TODO: Add in try for graceful error handling
    response = client.authorize_security_group_ingress(
        GroupId=sg_id,
        IpProtocol=protocol,
        FromPort=port,
        ToPort=port,
        CidrIp=current_ip
    )
    print response

def remove_ip(current_ip, sg_id, port, protocol):
    """remove current IP from the security group"""

    # setup client for ec2
    client = boto3.client("ec2")

    # execute security group revoke ingress Boto3 commands
    response = client.revoke_security_group_ingress(
        GroupId=sg_id,
        IpProtocol=protocol,
        FromPort=port,
        ToPort=port,
        CidrIp=current_ip
    )
    print response

# Define the usage of the app
def usage():
    """Prints usage information"""
    print
    print "AWS Security Group IP Updater"
    print
    print "Usage: aws-sg-ip-updater.py -s sg-abc123456"
    print " NOTE: This does require the AWSCLI be installed and configured"
    print "-h --help                 - this message"
    print "-s --sg_id                - id of the security group"
    print "-f --profile              - profile name to use from AWSCLI config"
    print "-p --port                 - port for rule"
    print "-t --protocol             - networking protcal for the rule"
    print "-r --remove               - remove current IP from security group"
    print
    print
    print "Examples:"
    print "aws-sg-ip-updater.py --sg_id sg-abc123456"
    print "aws-sg-ip-updater.py --sg_id sg-abc123456 --port 22 --protocol tcp"
    print
    sys.exit(0)

def main():
    # define global variables
    sg_id = ""
    profile = "default" # Still need to add in functionality to use other AWS profiles
    port = 22 # setting default as 22
    protocol = "tcp" # Hard coding tcp as default protocol
    remove = False

    if not len(sys.argv[1:]):
        usage()

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hs:f:p:t:r",
                                   ["help", "sg_id=", "profile=", "port=", "protocol=","remove"])
    except getopt.GetoptError as err:
        # print error and help information
        print str(err) # will print something like "option -q not recognized"
        usage()

    for o, a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-s", "--sg_id"):
            sg_id = a
        elif o in ("-f", "--profile"):
            profile = a
        elif o in ("-p", "--port"):
            port = int(a)
        elif o in ("-t", "--protocol"):
            protocol = a
        elif o in ("-r", "--remove"):
            remove = True
        else:
            assert False, "Unhandled Option"

    # get current public ip
    ip = get_current_ip()

    # add or remove current ip to the security group
    if remove == True:
        remove_ip(ip, sg_id, port, protocol)
    else:
        add_ip(ip, sg_id, port, protocol)

if __name__ == "__main__":
    main()
