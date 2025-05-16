# SignalHub

SignalHub is a project designed to send and visualize messages through shell scripts.

<div align="center">

<img src="https://github.com/honeok/archive/actions/workflows/shellcheck.yml/badge.svg" alt="Build Status" />
<img src="https://img.shields.io/github/license/honeok/signalhub.svg?style=flat" alt="License" />
<img src="https://img.shields.io/github/last-commit/honeok/signalhub" alt="Commit" />

<img src="https://cdn.skyimg.net/up/2025/5/17/82bf7c28.webp" alt="Nginx" width="80%">

</div>

## 🔧 How to Install

🐳 Docker
```shell
docker run -d --restart=unless-stopped -p 5000:5000 --name signalhub honeok/signalhub
```
SignalHub is now running on <http://0.0.0.0:5000>.

Storage Options:
- **Default:** SQLite is used for lightweight and easy setup.  
- **Optional:** MySQL can be used for advanced setups and better scalability.  

> Deployment  
> For a reliable and persistent deployment, it is highly recommended to use **Docker Compose**.  
> This ensures easy management of database and application configurations, making the setup reproducible and maintainable.

## License

This project is licensed under the GPL-3.0 License. See the [LICENSE](./LICENSE) file for more details.