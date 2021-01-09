import json
import math


def statement(invoice, plays):

    def amount_for(a_performance):
        result = 0
        if play_for(perf)["type"] == "tragedy":
            result = 40000
            if a_performance["audience"] > 30:
                result += 1000 * (a_performance["audience"] - 30)
        elif play_for(perf)["type"] == "comedy":
            result = 30000
            if a_performance["audience"] > 20:
                result += 10000 + 500 * (a_performance["audience"] - 20)
            result += 300 * a_performance["audience"]
        else:
            raise Exception("알 수 없는 장르")
        return result

    def play_for(a_performance):
        return plays[a_performance["playID"]]

    def volume_credits_for(a_performance):
        result = 0
        result += max(a_performance["audience"] - 30, 0)
        if play_for(a_performance)["type"] == "comedy":
            result += math.floor(a_performance["audience"] / 5)
        return result

    def usd(a_number):
        return '${:,.2f}'.format(a_number / 100)

    def total_volume_credits():
        result = 0
        for perf in invoice["performances"]:
            result += volume_credits_for(perf)
        return result

    total_amount = 0
    result = f"청구 내역 (고객명: {invoice['customer']})\n"

    for perf in invoice["performances"]:
        result += f' {play_for(perf)["name"]}: {usd(amount_for(perf))} ({perf["audience"]}석)\n'
        total_amount += amount_for(perf)

    result += f"총액: {usd(total_amount)}\n"
    result += f"적립 포인트': {total_volume_credits()}점\n"
    return result


if __name__ == '__main__':
    with open('invoices.json') as json_file:
        invoice = json.load(json_file)[0]

    with open('plays.json') as json_file:
        plays = json.load(json_file)

    print(statement(invoice, plays))


