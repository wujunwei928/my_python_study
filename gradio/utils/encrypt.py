import hashlib
import base64


def md5_encode(input_text: str) -> str:
    m = hashlib.md5()
    m.update(input_text.encode("utf-8"))
    return m.hexdigest()


def sha1_encode(input_text: str) -> str:
    m = hashlib.sha1()
    m.update(input_text.encode("utf-8"))
    return m.hexdigest()


def md5_encode_upper(input_text: str) -> str:
    return md5_encode(input_text).upper()


def base64_encode(input_text: str) -> str:
    return base64.b64encode(input_text.encode("utf-8")).decode("utf-8")


def base64_decode(input_text: str) -> str:
    return base64.b64decode(input_text.encode("utf-8")).decode("utf-8")
