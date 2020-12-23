# Using puppet to make the work more easy
exec { 'Custom_header_response':
    command  => 'sudo apt-get update;
    sudo apt-get -y install nginx;
    sudo sed -i "18i add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default;
    sudo service nginx restart',
    provider => 'shell'
}