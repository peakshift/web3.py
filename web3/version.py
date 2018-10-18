from web3.module import (
    Module,
)


class Version(Module):
    @property
    def api(self):
        from web3 import __version__
        return __version__

    @property
    def node(self) -> str:
        return self.web3.manager.request_blocking("web3_clientVersion", [])

    @property
    def network(self) -> str:
        return self.web3.manager.request_blocking("net_version", [])

    @property
    def ethereum(self) -> str:
        return self.web3.manager.request_blocking("eth_protocolVersion", [])
