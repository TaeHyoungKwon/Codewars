def convert_minutes_to_seconds(time):
    minutes, seconds = time.split(":")
    return int(minutes) * 60 + int(seconds)


if __name__ == "__main__":
    time = "16:39"
    print(convert_minutes_to_seconds(time))
