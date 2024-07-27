from dataclasses import asdict

from exchange.app import App
from exchange.settings import configuration
from exchange.api import router


def main():
    return (App(host='0.0.0.0', port=8000, **asdict(configuration.app))
            .included_cors()
            .included_routers(routers=[router]))


if __name__ == '__main__':
    main()
