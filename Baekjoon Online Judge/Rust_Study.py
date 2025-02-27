_ = input()

plans = list(map(int, input().split()))
executions = list(map(int, input().split()))

print(sum(plan <= execution for plan, execution in zip(plans, executions)))
