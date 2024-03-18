import pandas as pd

if __name__ == "__main__":
    d = {
        "1": ["Juan", "Martinez"],
        "2": ["Pedro", "Martinez"]
    }
    df = pd.DataFrame(d)
    print(df)
