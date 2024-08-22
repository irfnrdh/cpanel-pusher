<?php

require 'vendor/autoload.php';

use phpseclib3\Net\SSH2;

$ssh_host = 'your_server_ip';
$ssh_port = 22;
$ssh_user = 'your_ssh_username';
$ssh_password = 'your_ssh_password'; // Your SSH password

$github_username = 'your_github_username';
$github_token = 'your_github_personal_access_token';
$github_repo_url = "https://$github_username:$github_token@github.com/yourusername/yourrepository.git";
$project_directory = '/path/to/your/project/directory';

$commands = [
    "cd $project_directory && git clone $github_repo_url",
    "cd $project_directory && composer install",
    "cd $project_directory && npm install",
    "cd $project_directory && npm run build",
];

try {
    // Initialize SSH connection
    $ssh = new SSH2($ssh_host, $ssh_port);

    // Authenticate using password
    if (!$ssh->login($ssh_user, $ssh_password)) {
        throw new Exception('Login failed');
    }

    // Execute commands
    foreach ($commands as $command) {
        echo "Executing: $command\n";
        $output = $ssh->exec($command);
        echo "OUTPUT:\n$output\n";
    }

} catch (Exception $e) {
    echo 'Error: ' . $e->getMessage() . "\n";
}
