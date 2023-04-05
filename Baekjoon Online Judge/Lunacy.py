def solution(target: float) -> str:
    return f"Objects weighing {target:.2f} on Earth will weigh {target * 0.167:.2f} on the moon."


if __name__ == "__main__":
    while (target := float(input())) != -1.0:
        print(solution(target))
