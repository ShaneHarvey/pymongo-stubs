from typing import Any, Mapping, Match, Union

class CertificateError(ValueError): ...
def _dnsname_match(dn, hostname: str, max_wildcards: int = 1) -> Union[bool, None, Match[str]]: ...
def _ipaddress_match(ipname: str, host_ip: str) -> bool: ...
def match_hostname(cert: Mapping[str, Any], hostname: str) -> None: ...