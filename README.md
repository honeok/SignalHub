# SignalHub

SignalHub is a project designed to send and visualize messages through shell scripts.

<p>
  <a href="https://github.com/honeok/SignalHub/actions/workflows/publish.yml/badge.svg" target="_blank">
    <img src="https://github.com/honeok/SignalHub/actions/workflows/publish.yml/badge.svg" alt="Build Status" />
  </a>
  <a href="./LICENSE" target="_blank">
    <img src="https://img.shields.io/github/license/honeok/signalhub.svg?style=flat" alt="License" />
  </a>
  <a href="https://github.com/honeok/signalhub" target="_blank">
    <img src="https://img.shields.io/github/last-commit/honeok/signalhub" alt="Last Commit" />
  </a>
  <a href="https://github.com/honeok/signalhub" target="_blank">
    <img src="https://img.shields.io/github/commit-activity/m/honeok/signalhub.svg" alt="Commit Activity" />
  </a>
  <a href="https://hub.docker.com/r/honeok/signalhub" target="_blank">
    <img src="https://img.shields.io/docker/pulls/honeok/signalhub" alt="Docker Pulls" />
  </a>
  <a href="https://github.com/honeok/SignalHub" target="_blank">
    <img src="https://img.shields.io/github/stars/honeok/SignalHub?style=flat" alt="GitHub Stars" />
  </a>
  <a href="https://img.shields.io/github/issues/honeok/signalhub.svg" target="_blank">
    <img src="https://img.shields.io/github/issues/honeok/signalhub.svg" alt="Issues" />
  </a>
</p>

<p align="center">
  <img src="https://cdn.img2ipfs.com/ipfs/QmPfNWxGPJ5cYL4fL6wdHcYdTWmiqb1y2tKM9X1NbzeF85?filename=image.png"
       alt="Image">
</p>

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

## ⭐ Star History

[![Star History Chart](https://api.star-history.com/svg?repos=honeok/SignalHubs&type=Date)](https://star-history.com/#honeok/SignalHub&Date)

感谢你的支持！如果你喜欢这个项目，欢迎给我一个⭐Star！