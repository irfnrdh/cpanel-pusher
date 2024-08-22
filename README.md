# CPanel Pusher

Cpanel Pusher is Git Auto Clone and Deploy to CPanel over SSH

## Why?

- Most of Github Action for Cpanel using over FTP or OverSSH to with https://github.com/marketplace/actions/ssh-deploy
- We Need Not Full Auto but with control
- We can change everyhing in that script in local

## How?
- Generate Token `https://github.com/settings/tokens?type=beta`
- `git clone https://github.com/irfnrdh/cpanel-pusher.git && composer install && php deploy`
