from email import policy
from email.parser import BytesParser
from email.header import decode_header, make_header

def decode_value(value):
    if value is None:
        return None
    # decode_header returns list of (bytes/str, encoding)
    try:
        return str(make_header(decode_header(value)))
    except Exception:
        return value

def analyze_header_file(path):
    # Read raw bytes so we preserve charset info
    with open(path, "rb") as f:
        msg = BytesParser(policy=policy.default).parse(f)

    # headers we want to inspect (common ones)
    headers = ["MIME-Version", "Date", "Subject", "Delivered-To", "From", "To", "Return-Path", "Message-ID", "Received"]
    result = {}
    for h in headers:
        if h.lower() == "received":
            # Received may occur many times; keep all
            result["Received"] = msg.get_all("Received", failobj=[])
        else:
            raw = msg.get(h)
            result[h] = decode_value(raw)

    return result

if __name__ == "__main__":
    path = input("Enter the path for the raw email file: ").strip()
    try:
        data = analyze_header_file(path)
    except Exception as e:
        print("Failed to parse file:", e)
    else:
        for k, v in data.items():
            if v is None or (isinstance(v, list) and not v):
                print(f"{k}: (not found)")
            elif isinstance(v, list):
                print(f"{k}:")
                for item in v:
                    print("  ", item)
            else:
                print(f"{k}: {v}")
