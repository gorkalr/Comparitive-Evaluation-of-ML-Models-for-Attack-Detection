import re

def extract_features(url):
    features = []

    # 1. URL length
    features.append(len(url))

    # 2. Dot count
    features.append(url.count("."))

    # 3. Digit count
    features.append(sum(char.isdigit() for char in url))

    # 4. Special character count
    features.append(len(re.findall(r"[<>'\";/|&=?]", url)))

    # 5. HTTPS present or not
    features.append(1 if url.startswith("https") else 0)

    return features
